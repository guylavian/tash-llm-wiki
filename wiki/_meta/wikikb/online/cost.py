#!/usr/bin/env python3
"""cost.py — token / $ / latency accounting for the wiki retriever + (optional) LLM tier.

stdlib only by DEFAULT, no network. This is the measurement seam behind eval.py. It owns the
two ORTHOGONAL cost quantities the wiki tracks (see _meta/MIGRATION-litellm-langgraph.md §5 +
COUNCIL-DIRECTIVES.md BF-1):

  1. RETRIEVAL cost  — the context-token PROXY eval.py already prints (index + snippets + opened
     bodies). Exposed as `proxy_tokens(n_chars) -> FLOAT`. It MUST reproduce eval.py's historical
     float arithmetic byte-for-byte: `n_chars / CHARS_PER_TOKEN`, never an integer floor. This is
     the number router-skip / graph-rescue / dense are tuned against; it must not regress.

  2. GENERATION cost — real per-call token / $ / latency, populated ONLY when the optional local
     LLM gateway (llm.py, Phase 2+) actually runs. Token counting is `count_tokens(text) -> INT`
     via a vendored-by-path tokenizer (Phase 1) with a stdlib heuristic fallback. NEVER wired into
     the proxy. `$` comes from LiteLLM's bundled static price map (Phase 3), best-effort, tagged
     `unpriced/local` for local models. NO call to `litellm.token_counter` — it triggers a tiktoken
     network download (COUNCIL-DIRECTIVES.md §3).

DEGRADATION CONTRACT (mirrors embed.py): `have_library()` / `available()` / `status_str()` report
which path is live; with the optional deps/model absent every measured value is `None` and the
heuristic stands in, so `import cost` is stdlib-safe and the frozen eval baseline is unchanged.

Usage:
    python3 cost.py --status                 # which path is active (heuristic vs measured)
    python3 cost.py --tokens "some text"     # token estimate for a string (vendored or heuristic)
"""
import argparse
import json
import os
import sys
import time

from wikikb import paths
WIKI = str(paths.WIKI)
META = str(paths.META)
MODELS_DIR = str(paths.MODELS)
REPORT_PATH = str(paths.COST_REPORT)

# The declared home of the air-gap chars/token heuristic. eval.py sources its CHARS_PER_TOKEN from
# here; embed.py's CHARS_PER_TOKEN and lint.py's per-page token estimate inline the same literal 4
# (lint.py MUST — BF-11 forbids a module-scope cost import). The value (4) is identical across all three.
CHARS_PER_TOKEN = 4

sys.dont_write_bytecode = True

# price_usd() reads LiteLLM's bundled static price map; this env var (consulted at litellm IMPORT
# time) disables its GitHub price-map refresh so the $ path stays offline even if price_usd is called
# before llm.py is imported (BF-5 belt-and-suspenders; a pure stdlib write, no 3rd-party import here;
# idempotent with llm.py's identical setdefault).
os.environ.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")


# ---------- (1) RETRIEVAL proxy — FLOAT, byte-identical to eval.py history (BF-1) -------------

def proxy_tokens(n_chars):
    """Context-token PROXY for the retrieval cost. FLOAT division — reproduces eval.py's exact
    `bytes / CHARS_PER_TOKEN` arithmetic. MUST NOT floor (an int floor flips the printed mean,
    verified 98325->98324 on cases.jsonl). Wired into eval.py's idx_t/snip_t/body_t."""
    return n_chars / CHARS_PER_TOKEN


# ---------- (2) GENERATION token count — INT, measured path only -----------------------------
# Phase 0 ships the heuristic tier only; Phase 1 prepends a vendored-tokenizer tier. This is
# NEVER wired into proxy_tokens(); it counts real strings for the --measure-llm generation column.

_TOK_CACHE = {}


def _vendored_tokenizer(model):
    """A HuggingFace `tokenizers` Tokenizer loaded from a vendored tokenizer.json BY PATH (no
    network), or None. Looks at _meta/models/<model>/tokenizer.json. Lazy + guarded: the
    `tokenizers` import and the file load are both optional (Phase 1 dep). Returns None on any
    failure so count_tokens() degrades to the heuristic."""
    if not model:
        return None
    if model in _TOK_CACHE:
        return _TOK_CACHE[model]
    tok = None
    path = os.path.join(MODELS_DIR, model, "tokenizer.json")
    if os.path.isfile(path):
        try:
            from tokenizers import Tokenizer  # lazy, optional (Rust wheel; see requirements-online.txt)
            tok = Tokenizer.from_file(path)
        except Exception:
            tok = None
    _TOK_CACHE[model] = tok
    return tok


def count_tokens(text, model=None):
    """Real per-string token count for the MEASURED generation path. Returns an INT.
    Tier 1: vendored tokenizer.json by path (`len(tok.encode(text).ids)`) — offline, per-model.
    Tier 2 (fallback): the chars/token heuristic `len(text) // CHARS_PER_TOKEN`.
    (The plan's third "reuse embed.py's tokenizer" tier was dropped — embed.py exposes no such
    helper; see COUNCIL-DIRECTIVES.md BF-3.)"""
    text = text or ""
    tok = _vendored_tokenizer(model)
    if tok is not None:
        try:
            return len(tok.encode(text).ids)
        except Exception:
            pass
    return len(text) // CHARS_PER_TOKEN


# ---------- availability (never raises on import) — mirrors embed.py ---------------------------

def have_tokenizer_library():
    try:
        import tokenizers  # noqa: F401
        return True
    except Exception:
        return False


def have_library():
    """True iff the measured-cost dependency surface (the tokenizer lib for real token counts)
    is importable. Phase 3 also consults llm.available() for the $ path. False -> heuristic only."""
    return have_tokenizer_library()


def available(model=None):
    """True iff a REAL per-model token count is possible (library importable AND a tokenizer.json
    vendored for `model`). False -> count_tokens() returns the heuristic. Generation $ additionally
    requires llm.available() (checked at measure-time, Phase 3)."""
    return have_tokenizer_library() and _vendored_tokenizer(model) is not None


def status_str(model=None):
    if available(model):
        return "cost: measured tokens via vendored tokenizer[%s]; $ best-effort (unpriced/local)" % model
    if have_tokenizer_library():
        return "cost: heuristic (chars/%d) — no tokenizer vendored at _meta/models/<model>/" % CHARS_PER_TOKEN
    return "cost: heuristic (chars/%d) — `tokenizers` not installed (measured tokens disabled)" % CHARS_PER_TOKEN


# ---------- (3) $ pricing — best-effort, offline; tagged unpriced/local (Phase 3, BF-8) -------

def price_usd(model, prompt_tokens, completion_tokens):
    """Best-effort generation $ from LiteLLM's bundled static price map via the guarded
    `litellm.cost_per_token()` (which returns a TUPLE). Returns (usd|None, tag). litellm is imported
    lazily; the price-map network refresh is disabled by the `LITELLM_LOCAL_MODEL_COST_MAP` env that
    llm.py sets at MODULE TOP before any litellm import (Phase 2, BF-5), so this stays offline. Local
    models (ollama/*) generally have NO price entry -> (None, 'unpriced/local'), NOT $0.00 (BF-8).
    No caller until Phase 3 (--measure-llm)."""
    try:
        import litellm  # lazy, optional
    except Exception:
        return None, "unpriced/local"
    try:
        p, c = litellm.cost_per_token(model=model, prompt_tokens=prompt_tokens,
                                      completion_tokens=completion_tokens)  # returns a TUPLE
        total = (p or 0.0) + (c or 0.0)
        return (total, "priced") if total > 0 else (None, "unpriced/local")
    except Exception:
        return None, "unpriced/local"


# ---------- defensive response parsing (BF-8) — never raises / never KeyErrors ----------------

def _as_int(x):
    """Coerce to int, or None on any non-numeric value — so parse_response never raises on a junk
    usage token (e.g. a stray 'n/a' or an object). Numeric strings ('120') still coerce (BF-8/B1)."""
    try:
        return int(x)
    except (TypeError, ValueError):
        return None


def parse_response(resp, model=None, latency_ms=None):
    """Extract a well-formed measured-usage dict from a LiteLLM response object. DEFENSIVE: every
    field via getattr/.get, absent -> None; `_hidden_params` is private/version-dependent and ABSENT
    for local models, so it is read with .get only (BF-8). `cost_per_token` returns a TUPLE -> summed
    via price_usd. Used by measure() (Phase 3) and unit-tested by cost_probe.py (Phase 2) with a stub.
    Returns keys: gen_prompt_tok, gen_completion_tok, gen_cost_usd, gen_latency_ms, cached, price_tag."""
    usage = getattr(resp, "usage", None)
    pt = ct = None
    if usage is not None:
        pt = getattr(usage, "prompt_tokens", None)
        ct = getattr(usage, "completion_tokens", None)
        if pt is None and isinstance(usage, dict):
            pt, ct = usage.get("prompt_tokens"), usage.get("completion_tokens")
    pt, ct = _as_int(pt), _as_int(ct)          # coerce defensively — a junk token must not crash (B1)
    hp = getattr(resp, "_hidden_params", {}) or {}
    if not isinstance(hp, dict):
        hp = {}
    gen_cost = hp.get("response_cost")
    cached = bool(hp.get("cache_hit", False))
    tag = "priced" if gen_cost is not None else "unpriced/local"
    if gen_cost is None and model is not None and pt is not None:
        gen_cost, tag = price_usd(model, pt, ct or 0)
    return {
        "gen_prompt_tok": pt,
        "gen_completion_tok": ct,
        "gen_cost_usd": gen_cost,
        "gen_latency_ms": latency_ms,
        "cached": cached,
        "price_tag": tag,
    }


# ---------- budget gate — pure stdlib, raises OUR exception (BF-9) -----------------------------

class BudgetExceeded(Exception):
    """Raised when a measured/proxy total exceeds a configured budget. Drives eval.py exit code 3."""


def check_budget(value, limit, kind="tokens"):
    """Raise BudgetExceeded iff `limit` is set and `value` > `limit`. `value` for the token budget
    is the SAME float proxy mean eval prints (BF-1) — pass/fail tracks the displayed number."""
    if limit is not None and value is not None and value > limit:
        raise BudgetExceeded("%s budget exceeded: %.2f > %.2f" % (kind, value, limit))
    return False


# ---------- measure() — wrap the LLM gateway, time it, parse defensively (Phase 3) ------------

def measure(messages, model=None, domain=None, recorder=None):
    """Call the optional LLM gateway with `messages`, time it, and return a defensive measured-usage
    dict (parse_response shape) plus an `active` flag. OFFLINE / gateway-off / blocked / error ->
    active=False and all gen_* None (the 'n/a (offline)' case). NEVER raises (the dense_rank
    contract). Optionally accumulates into a UsageRecorder. `llm` is a local stdlib module imported
    lazily so cost.py stays import-light and there is no import-order coupling."""
    inactive = {"gen_prompt_tok": None, "gen_completion_tok": None, "gen_cost_usd": None,
                "gen_latency_ms": None, "cached": False, "price_tag": "n/a", "active": False}
    try:
        from wikikb.online import llm  # noqa: local stdlib gateway module
    except Exception:
        return dict(inactive)
    if not llm.available():
        return dict(inactive)
    model = model or llm.load_config().get("model")
    elapsed_ms = timer()
    resp = llm.complete(messages, model=model)
    ms = elapsed_ms()
    if resp is None:
        return dict(inactive)
    try:
        d = parse_response(resp, model=model, latency_ms=ms)   # defense-in-depth (B1): never escape
    except Exception:
        return dict(inactive)
    d["active"] = True
    if recorder is not None:
        recorder.record(prompt_tokens=d["gen_prompt_tok"] or 0,
                        completion_tokens=d["gen_completion_tok"] or 0,
                        usd=d["gen_cost_usd"], latency_ms=d["gen_latency_ms"],
                        domain=domain, cached=d["cached"])
    return d


# ---------- usage ledger — stdlib; shaped like LangChain's OpenAICallbackHandler --------------

class UsageRecorder:
    """Accumulates measured generation usage across an eval/QUERY run. stdlib only. The LLM tier
    (Phase 3) feeds it; with no LLM calls it stays empty and writes a zeroed report."""

    def __init__(self):
        self.calls = 0
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.usd = 0.0
        self.priced_calls = 0
        self.latency_ms = []
        self.by_domain = {}
        self.cache_hits = 0

    def record(self, prompt_tokens=0, completion_tokens=0, usd=None, latency_ms=None,
               domain=None, cached=False):
        self.calls += 1
        self.prompt_tokens += int(prompt_tokens or 0)
        self.completion_tokens += int(completion_tokens or 0)
        if usd is not None:
            self.usd += float(usd)
            self.priced_calls += 1
        if latency_ms is not None:
            self.latency_ms.append(float(latency_ms))
        if cached:
            self.cache_hits += 1
        if domain:
            d = self.by_domain.setdefault(domain, {"calls": 0, "prompt_tokens": 0,
                                                    "completion_tokens": 0, "usd": 0.0})
            d["calls"] += 1
            d["prompt_tokens"] += int(prompt_tokens or 0)
            d["completion_tokens"] += int(completion_tokens or 0)
            if usd is not None:
                d["usd"] += float(usd)

    def _pct(self, p):
        if not self.latency_ms:
            return None
        s = sorted(self.latency_ms)
        k = max(0, min(len(s) - 1, int(round((p / 100.0) * (len(s) - 1)))))
        return s[k]

    def summary(self):
        return {
            "calls": self.calls,
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "usd": round(self.usd, 6) if self.priced_calls else None,
            "priced_calls": self.priced_calls,
            "cache_hits": self.cache_hits,
            "latency_ms_p50": self._pct(50),
            "latency_ms_p95": self._pct(95),
            "by_domain": self.by_domain,
        }

    def write_report(self, path=REPORT_PATH):
        """Write the run-total ledger (gitignored, regenerable like the embeddings index)."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(self.summary(), fh, indent=2, sort_keys=True)
            fh.write("\n")
        return path


# ---------- latency helper (stdlib) -----------------------------------------------------------

def timer():
    """Return a callable that yields elapsed milliseconds since it was created (time.perf_counter)."""
    t0 = time.perf_counter()
    return lambda: (time.perf_counter() - t0) * 1000.0


# ---------- CLI -------------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--status", action="store_true", help="report which cost path is active")
    ap.add_argument("--tokens", metavar="TEXT", help="token estimate for a string (vendored or heuristic)")
    ap.add_argument("--model", default=None, help="model name (selects a vendored tokenizer if present)")
    args = ap.parse_args()
    if args.tokens is not None:
        print("%d tokens (%s)  proxy=%.2f" % (count_tokens(args.tokens, args.model),
              "vendored" if available(args.model) else "heuristic", proxy_tokens(len(args.tokens))))
        return
    print(status_str(args.model))


if __name__ == "__main__":
    main()
