# Measured token / $ cost — vendoring (air-gapped)

`_meta/wikikb/cost.py` reports two **orthogonal** cost quantities (see
`_meta/MIGRATION-litellm-langgraph.md` §5 + `COUNCIL-DIRECTIVES.md` BF-1/BF-3/BF-8):

| Quantity | Function | Default (offline, no deps) |
|---|---|---|
| **Retrieval proxy** (index + snippets + opened bodies) | `proxy_tokens(n_chars) -> float` | `n_chars / 4` — the historical heuristic, **byte-identical** |
| **Measured generation tokens** | `count_tokens(text, model) -> int` | `len(text) // 4` heuristic **until a tokenizer is vendored** |
| **Measured generation $** | `price_usd(model, p, c)` | `(None, "unpriced/local")` — local models are unpriced |

The retrieval proxy is **always** the chars/4 heuristic and never changes — it is what
`route`/`expand`/`embed` are tuned against. Only the **measured generation path** gains accuracy
when you vendor the optional pieces below. Everything degrades gracefully offline (the `embed.py`
contract): with nothing vendored, `cost.py` is pure stdlib and opens no socket.

## 1. Real per-model token counts (tier-1 of `count_tokens`)

`count_tokens` is two-tier: **tier-1** loads a HuggingFace `tokenizers` `Tokenizer` from a vendored
`tokenizer.json` **by path** (no network) and returns `len(tok.encode(text).ids)`; **tier-2** is the
`len(text)//4` heuristic. (There is no third "reuse the embedding model's tokenizer" tier — `embed.py`
exposes no such helper; see `COUNCIL-DIRECTIVES.md` BF-3.)

On a networked machine, fetch the library wheel + the model's tokenizer, then transfer:

```bash
pip install transformers tokenizers          # networked box ONLY (prereq for the export below; NOT transferred)

# library (Rust-compiled wheel — MUST match the air-gapped box's CPython-version + OS + arch + ABI).
# --platform takes a wheel PLATFORM TAG (e.g. manylinux2014_x86_64, macosx_11_0_arm64), not a Rust triple;
# --abi is required for an ABI-specific compiled wheel or pip falls back to the running interpreter's ABI.
pip download tokenizers -d ./wheels \
  --platform <platform-tag> --python-version <X.Y> --abi <abi-tag> --implementation cp --only-binary=:all:

# the tokenizer.json for the LOCAL model you serve via Ollama/vLLM, e.g. qwen2.5. cost.py's tier-1
# needs a FAST (Rust) tokenizer — only a fast tokenizer emits tokenizer.json; assert it before transfer:
python3 -c "from transformers import AutoTokenizer; \
            t = AutoTokenizer.from_pretrained('Qwen/Qwen2.5-32B-Instruct', use_fast=True); \
            assert t.is_fast, 'need a fast tokenizer to emit tokenizer.json'; \
            t.save_pretrained('qwen2.5-32b')"
ls qwen2.5-32b/tokenizer.json                 # MUST exist before you copy it over
```

On the air-gapped workstation:

```bash
pip install --no-index --find-links ./wheels tokenizers
# place tokenizer.json where cost.py looks: _meta/models/<model>/tokenizer.json
mkdir -p <repo>/wiki/_meta/models/qwen2.5-32b
cp qwen2.5-32b/tokenizer.json <repo>/wiki/_meta/models/qwen2.5-32b/tokenizer.json
```

`python3 -m wikikb cost --status --model qwen2.5-32b` should then report `measured tokens via vendored tokenizer`.
The model dir is shared with `embed.py` (it loads sentence-transformers models from the same
`_meta/models/<name>/`); a tokenizer.json can sit alongside an embedding model dir.

> **Compiled-wheel caveat.** `tokenizers` (and, in the online tier, `tiktoken`/`pydantic-core`) ship
> Rust/C **binary wheels**. `pip download` them on a box whose **CPython version + OS + CPU arch + ABI**
> all match the air-gapped target (pin all four: `--python-version`, `--platform`, `--implementation cp`,
> `--abi`), or the offline `--no-index` install fails. Always pass `--only-binary=:all:` so a missing
> wheel surfaces on the networked box, not the sealed one.

## 2. Generation `$` (best-effort, offline)

`price_usd` reads LiteLLM's **bundled static** price map via the guarded `litellm.cost_per_token()`
(a TUPLE `(prompt, completion)` — summed). It opens **no socket**: the GitHub price-map refresh is
disabled by `LITELLM_LOCAL_MODEL_COST_MAP`, which `llm.py` sets at module top **before** any litellm
import (Phase 2, BF-5). Local `ollama/*` models generally have **no** price entry, so the honest
result is `(None, "unpriced/local")` — **not** `$0.00` (BF-8). Real `$` appears only on the opt-in
remote path. For local capacity planning, lead with **tokens + latency** (free, stdlib), not `$`.

## Notes
- **Offline only / no socket.** Vendored tokenizer = a file read; `litellm` is imported lazily and
  only for pricing. A selftest network-tripwire (`selftest.py`) blocks sockets and asserts the cost
  path completes — run it after vendoring.
- **Derived + regenerable.** The run-total ledger `_meta/eval/cost_report.json` and any `_meta/.llm_cache/`
  are gitignored; vendored tokenizers live under the gitignored `_meta/models/` (keep the READMEs).
- **Reserved for the measured path.** `count_tokens` / `price_usd` are NEVER wired into the retrieval
  proxy — they activate only under `python3 -m wikikb evaluate --measure-llm` (Phase 3) with the local gateway running.
