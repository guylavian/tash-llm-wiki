# Optional LLM gateway — offline bring-up (air-gapped)

`_meta/wikikb/llm.py` is the single, OPTIONAL seam through which the wiki may call a language model. It
defaults OFF and local-only. With it absent/off the wiki is exactly today's offline system (the host
runtime drives the prose ops; `complete()` returns None → deterministic extractive fallback). Mirrors
the `embed.py` dependency contract: lazy import, behind a flag, graceful degradation.

## Modes (`WIKI_LLM`)
| `WIKI_LLM` | Behaviour |
|---|---|
| unset / `off` (default) | gateway inactive — today's offline, host-runtime-driven wiki |
| `local` | call the configured LOCAL loopback model (Ollama/vLLM) |
| `cloud` | same, but intended for the opt-in remote path (still needs the double opt-in below) |

## 1. Run a local model (no internet at query time)

```bash
# Ollama (default port 11434). Pull the model ONCE on a connected box, or copy its blobs in.
ollama pull qwen2.5:32b
ollama serve            # serves http://127.0.0.1:11434
# (vLLM alternative: serve an OpenAI-compatible endpoint at http://127.0.0.1:8000/v1,
#  configure model: "openai/<served-name>" + api_base: "http://127.0.0.1:8000/v1")
```

## 2. Vendor the LiteLLM library offline

```bash
# on a networked machine — match the air-gapped box's CPython-version + OS + arch + ABI. --platform
# takes a wheel PLATFORM TAG (manylinux2014_x86_64 / macosx_11_0_arm64), not a Rust triple; --abi is
# required for compiled wheels (litellm pulls tiktoken/pydantic-core). See requirements-online.txt.
pip download -r wiki/_meta/requirements-online.txt -d ./wheels \
    --platform <platform-tag> --python-version <X.Y> --abi <abi-tag> --implementation cp --only-binary=:all:
# on the air-gapped workstation:
pip install --no-index --find-links ./wheels litellm
```

## 3. Configure + enable

```bash
cp wiki/_meta/llm.config.yaml.sample wiki/_meta/llm.config.yaml   # then edit (gitignored)
export WIKI_LLM=local
python3 -m wikikb llm --status      # -> llm: local model=ollama/qwen2.5:32b ... gate=local-ok
python3 -m wikikb llm --probe       # ACTIVE: a tiny local completion (expects 'pong')
```

## Air-gap guarantees (enforced, not just configured)
- **No socket on import.** `litellm` is imported lazily; `LITELLM_LOCAL_MODEL_COST_MAP=True` is set at
  `llm.py` module top so litellm never refreshes its price map over the network; telemetry is disabled.
- **Loopback gate (BF-6).** Before any completion, the model's provider must be in `provider_allowlist`
  **and** `api_base` must resolve to a loopback IP. A non-loopback endpoint — including a bare cloud
  model id with no `api_base` — is **refused** (`complete()` returns None; `--probe`/`--status` show
  `BLOCKED`).
- **Opt-in remote (deliberate).** To allow a cloud model (and real `$` cost), set BOTH
  `WIKI_LLM_ALLOW_REMOTE=1` **and** a provider key env (e.g. `OPENAI_API_KEY`). This is the only way
  past the loopback gate. Keys stay out of git and out of `llm.config.yaml`.

## Notes
- **Optional + regenerable.** `llm.config.yaml`, `wheels/`, `.llm_cache/`, `.checkpoints/`, and the
  `_meta/eval/cost_report.json` ledger are gitignored. Keep the READMEs.
- **Verify the pins.** litellm/langgraph wheels for newer CPython (e.g. 3.14) may lag; confirm
  availability for your target Python and re-verify each API symbol against the pinned version's
  source (COUNCIL-DIRECTIVES.md §3) before relying on it.
