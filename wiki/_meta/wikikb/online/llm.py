#!/usr/bin/env python3
"""llm.py — OPTIONAL, offline-first LLM gateway (LiteLLM SDK). The generation-side twin of embed.py.

This is the single seam through which the wiki's operations may call a language model. It exists ONLY
when deliberately enabled and defaults to a LOCAL loopback endpoint (Ollama / vLLM — the design's
~27B target). With the optional `litellm` dep absent OR `WIKI_LLM` off, the wiki behaves exactly as
today: the host runtime (Claude Code / OpenCode) drives the prose ops and `complete()` returns None so
callers use their deterministic extractive fallback. NEVER raises (the embed.dense_rank contract).

AIR-GAP CONTRACT (COUNCIL-DIRECTIVES.md BF-5/BF-6):
  - NO module-scope third-party import: `litellm` is imported lazily inside complete()/probe() only.
  - Import-time-read env guards are set at MODULE TOP (below) BEFORE any lazy litellm import, so
    litellm never attempts its GitHub price-map refresh / telemetry on import.
  - Before any completion() the model+endpoint pass a LOCAL gate: provider ∈ allowlist AND api_base
    host is a loopback IP. Non-loopback (incl. a bare cloud model id with no api_base) is REFUSED
    unless the explicit double opt-in — WIKI_LLM_ALLOW_REMOTE=1 AND a provider key env present.
  - `available()` is config-only (lib + config + WIKI_LLM!=off); it does NOT probe a live socket.
    Use `--probe` for an active reachability check.

Config: env vars (WIKI_LLM_MODEL / WIKI_LLM_API_BASE / WIKI_LLM_MAX_TOKENS / WIKI_LLM_TEMPERATURE)
override an optional, gitignored `_meta/llm.config.yaml` (a tiny flat key:value subset — see
llm.config.yaml.sample). Stdlib only; no PyYAML.

Usage:
    python3 llm.py --status                 # which path is active (off / local / blocked / ready)
    python3 llm.py --probe                  # ACTIVE: attempt a tiny local completion (guarded)
    WIKI_LLM=local python3 llm.py --status
"""
import argparse
import ipaddress
import os
import sys
from urllib.parse import urlparse

from wikikb import paths
WIKI = str(paths.WIKI)
META = str(paths.META)
CONFIG_PATH = str(paths.LLM_CONFIG)

# ---- BF-5: import-time-read env guard at MODULE TOP, before ANY lazy `import litellm`. Pure stdlib
# os write (no third-party import here); idempotent with cost.py's identical setdefault. ----
os.environ.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")   # never refresh the price map over the net

sys.dont_write_bytecode = True

DEFAULT_ALLOWLIST = ("ollama", "ollama_chat", "vllm", "openai")  # 'openai' = local vLLM ONLY (loopback-gated)
LOOPBACK_NAMES = {"localhost", "127.0.0.1", "::1"}
# provider key envs that, WITH WIKI_LLM_ALLOW_REMOTE=1, unlock the opt-in remote path
PROVIDER_KEYS = ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "AZURE_API_KEY", "COHERE_API_KEY",
                 "GEMINI_API_KEY", "MISTRAL_API_KEY", "GROQ_API_KEY")


class RemoteBlocked(Exception):
    """A non-loopback model/endpoint was requested without the WIKI_LLM_ALLOW_REMOTE double opt-in."""


# ---------- mode + config (stdlib) -----------------------------------------------------------

def mode():
    return os.environ.get("WIKI_LLM", "off").strip().lower()


def _parse_simple_yaml(text):
    """Minimal FLAT key:value YAML subset (scalars, bools, ints/floats, and `[a, b]` lists) — enough
    for llm.config.yaml. NOT a general YAML parser (no nesting). Strips ` #` inline comments and
    surrounding quotes. Mirrors how the rest of the toolchain regex-reads frontmatter (stdlib only)."""
    cfg = {}
    for raw in text.splitlines():
        line = raw
        if " #" in line:
            line = line[:line.index(" #")]          # inline comment (space+hash); URLs have no ' #'
        line = line.rstrip()
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if not v:
            continue
        if v.startswith("[") and v.endswith("]"):
            cfg[k] = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
            continue
        v = v.strip("\"'")
        low = v.lower()
        if low in ("true", "false"):
            cfg[k] = (low == "true")
        else:
            try:
                cfg[k] = int(v)
            except ValueError:
                try:
                    cfg[k] = float(v)
                except ValueError:
                    cfg[k] = v
    return cfg


def load_config():
    """File config (optional) overlaid by env vars. Env wins so an operator can override without
    editing the gitignored file."""
    cfg = {}
    if os.path.isfile(CONFIG_PATH):
        try:
            cfg.update(_parse_simple_yaml(open(CONFIG_PATH, encoding="utf-8-sig").read()))  # tolerate a BOM
        except Exception:
            pass
    for key, env in (("model", "WIKI_LLM_MODEL"), ("api_base", "WIKI_LLM_API_BASE"),
                     ("max_tokens", "WIKI_LLM_MAX_TOKENS"), ("temperature", "WIKI_LLM_TEMPERATURE")):
        v = os.environ.get(env)
        if v is not None:
            cfg[key] = v
    return cfg


def allowlist():
    al = load_config().get("provider_allowlist")
    if isinstance(al, str):                       # a scalar `provider_allowlist: ollama` -> [ollama]
        al = [al]                                 # (else set('ollama') -> {'o','l','a','m'} would wrongly block)
    return set(al) if al else set(DEFAULT_ALLOWLIST)


# ---------- availability (config-only; never a live socket) ----------------------------------

def have_library():
    try:
        import litellm  # noqa: F401  (lazy — never at module scope)
        return True
    except Exception:
        return False


def available():
    """True iff a model COULD be called: WIKI_LLM != off AND litellm importable AND a model configured.
    Deliberately does NOT open a socket (BF-6). complete() still enforces the loopback gate."""
    return mode() != "off" and have_library() and bool(load_config().get("model"))


def status_str():
    m = mode()
    if m == "off":
        return "llm: off (WIKI_LLM unset/off — host runtime drives ops; extractive fallback)"
    if not have_library():
        return "llm: %s but `litellm` not installed — gateway inactive (extractive fallback)" % m
    cfg = load_config()
    model = cfg.get("model")
    if not model:
        return "llm: %s but no model configured (set WIKI_LLM_MODEL or _meta/llm.config.yaml)" % m
    api_base = cfg.get("api_base")
    try:
        _enforce_local(model, api_base)
        gate = "local-ok" if _is_local(model, api_base) else "remote (opt-in)"
    except RemoteBlocked:
        if _provider_of(model) in allowlist() and not api_base:
            gate = ("BLOCKED — no api_base; set WIKI_LLM_API_BASE to a loopback URL "
                    "(e.g. http://127.0.0.1:8000/v1) for this local provider")
        else:
            gate = "BLOCKED (non-loopback; set WIKI_LLM_ALLOW_REMOTE=1 + a provider key to allow remote)"
    return "llm: %s model=%s api_base=%s gate=%s" % (m, model, api_base or "(default)", gate)


# ---------- the local gate (BF-6) ------------------------------------------------------------

def _provider_of(model):
    return (model or "").split("/", 1)[0].lower() if "/" in (model or "") else (model or "").lower()


def _effective_api_base(model, api_base):
    """Ollama defaults to a loopback endpoint, so supply it explicitly when omitted: (a) the loopback
    gate then sees a concrete loopback host (the common env-only `WIKI_LLM_MODEL=ollama/...` setup
    works without a banner steering the user toward the REMOTE opt-in), and (b) litellm can't silently
    fall back to a remote OLLAMA_API_BASE env. ONLY for ollama — NEVER 'openai' (could be a cloud host)."""
    if not api_base and _provider_of(model) in ("ollama", "ollama_chat"):
        return "http://127.0.0.1:11434"
    return api_base


def _is_loopback_host(host):
    if not host:
        return False
    if host in LOOPBACK_NAMES:
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def _has_provider_key():
    return any(os.environ.get(k) for k in PROVIDER_KEYS)


def _is_local(model, api_base):
    api_base = _effective_api_base(model, api_base)            # ollama -> explicit loopback (A2)
    host = urlparse(api_base).hostname if api_base else None
    return _provider_of(model) in allowlist() and _is_loopback_host(host)


def _enforce_local(model, api_base):
    """Allow iff (provider ∈ allowlist AND api_base host is loopback). Otherwise allow ONLY the
    explicit double opt-in (WIKI_LLM_ALLOW_REMOTE=1 AND a provider key present). Else RemoteBlocked.
    A bare cloud model id (no api_base) is non-loopback -> blocked unless opt-in (BF-6)."""
    if _is_local(model, api_base):
        return
    if os.environ.get("WIKI_LLM_ALLOW_REMOTE") == "1" and _has_provider_key():
        return
    raise RemoteBlocked(
        "refusing non-loopback model=%r api_base=%r (provider=%r). Default is local-only; set "
        "WIKI_LLM_ALLOW_REMOTE=1 AND a provider key env to opt into remote." %
        (model, api_base, _provider_of(model)))


# ---------- the gateway call (never raises; returns the response or None) ---------------------

def complete(messages, model=None, **kw):
    """Call the configured model and return the LiteLLM response object, or None when the gateway is
    off / unavailable / blocked / errors. NEVER raises — the caller extracts text via text_of() and
    falls back to its deterministic extractive answer on None (the embed.dense_rank contract).
    `cost.measure()` reads usage off the returned object."""
    if mode() == "off" or not have_library():
        return None
    cfg = load_config()
    model = model or cfg.get("model")
    if not model:
        return None
    api_base = kw.pop("api_base", None) or cfg.get("api_base")
    api_base = _effective_api_base(model, api_base)  # ollama -> explicit loopback so litellm can't go remote (A2)
    try:
        _enforce_local(model, api_base)             # BF-6 — before the import/call
    except RemoteBlocked:
        return None                                  # refuse silently; --probe surfaces the reason
    try:
        import litellm
        litellm.telemetry = False                    # attr toggles AFTER import, BEFORE the call (BF-5)
        litellm.suppress_debug_info = True
        try:
            litellm.success_callback = []
        except Exception:
            pass
        # local vLLM (openai/* on loopback) needs a dummy key to avoid AuthenticationError pre-socket
        if _provider_of(model) == "openai" and not os.environ.get("OPENAI_API_KEY"):
            kw.setdefault("api_key", "sk-noop")
        # pop these from kw FIRST so a caller passing temperature/max_tokens (e.g. --probe's
        # max_tokens=8) doesn't collide with the explicit kwargs below -> TypeError (A1). kw wins.
        temperature = kw.pop("temperature", cfg.get("temperature", 0))
        try:
            temperature = float(temperature)
        except (TypeError, ValueError):
            temperature = 0
        max_tokens = kw.pop("max_tokens", cfg.get("max_tokens", 2048))
        try:
            max_tokens = int(max_tokens)
        except (TypeError, ValueError):
            max_tokens = 2048
        return litellm.completion(model=model, messages=messages, api_base=api_base,
                                  temperature=temperature, max_tokens=max_tokens, **kw)
    except Exception:
        return None


def text_of(resp):
    """Extract the assistant text from a LiteLLM response, or None (defensive)."""
    try:
        return resp.choices[0].message.content
    except Exception:
        try:
            return resp["choices"][0]["message"]["content"]
        except Exception:
            return None


# ---------- CLI ------------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--status", action="store_true", help="report the gateway state (no socket)")
    ap.add_argument("--probe", action="store_true", help="ACTIVE: attempt a tiny local completion (guarded)")
    args = ap.parse_args()
    if args.probe:
        if not available():
            print("probe: unavailable — %s" % status_str())
            sys.exit(0)
        resp = complete([{"role": "user", "content": "ping (reply with the single word: pong)"}],
                        max_tokens=8)
        txt = text_of(resp)
        print("probe: %s" % ("OK — %r" % (txt or "")[:40] if resp is not None else
                              "no response (endpoint down / blocked) — %s" % status_str()))
        sys.exit(0)
    print(status_str())


if __name__ == "__main__":
    main()
