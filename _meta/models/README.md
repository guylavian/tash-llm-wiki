# Offline embedding model — vendoring (air-gapped)

The Phase-3 dense layer (`_meta/wikikb/embed.py`) loads a sentence-transformers model **by
local path** — never from the network. Vendor it once on a connected machine, copy it here,
and the air-gapped workstation uses it offline.

Default model: **`bge-small-en-v1.5`** (~130 MB, 384-dim, strong for short-passage retrieval).
Override with `python3 -m wikikb embed --model <name>` (the dir name under `_meta/models/` must match).

## 1. On a networked machine — fetch the library + model

```bash
# library wheels (transfer these to the air-gapped box and `pip install --no-index`)
pip download numpy sentence-transformers -d ./wheels

# the model, saved as a self-contained directory
python3 -c "from sentence_transformers import SentenceTransformer; \
            SentenceTransformer('BAAI/bge-small-en-v1.5').save('bge-small-en-v1.5')"
```

## 2. Transfer to the air-gapped workstation

```bash
# install the library offline
pip install --no-index --find-links ./wheels numpy sentence-transformers
# place the model directory here (the name must match --model)
cp -r bge-small-en-v1.5  <repo>/wiki/_meta/models/bge-small-en-v1.5
```

`python3 -m wikikb embed --domains` should now report `library=yes model[bge-small-en-v1.5]=yes`.

## 3. Build the index (delta-aware) and use it

```bash
python3 -m wikikb embed --domain keycloak         --build
python3 -m wikikb embed --domain active-directory --build
# retrieval auto-uses it:
python3 -m wikikb kb --domain keycloak search "proof of possession token binding" --hybrid
python3 -m wikikb evaluate --route --graph --hybrid   # the acceptance-proof run
```

## Build notes (observed — Phase 1 activation, 2026-06-25)
- **Python:** use **3.10–3.13** for the venv (`torch` has no 3.14 wheels yet). A dedicated
  venv (e.g. `_meta/.venv-embed/`, gitignored) keeps the system Python clean and matches the
  "library is an optional local dep" model. Run the build with that venv's python:
  `_meta/.venv-embed/bin/python -m wikikb embed --domain <d> --build`.
- **Pin threads or the build dies mid-encode:** `OMP_NUM_THREADS=2 TOKENIZERS_PARALLELISM=false`.
  Without it, large-corpus `enc.encode(...)` spawns torch workers that leak semaphores and the
  process is killed before writing the index (small encodes pass, full builds don't). This is the
  one non-obvious knob.
- **Cost (CPU, BGE-small, M-series):** keycloak 831 notes → 7166 chunks ≈ **3.5 min**;
  active-directory 235 → 3228 chunks ≈ **1.5 min**. Notes-first domains (cisco-ios-xe) have 0
  `reference/` bodies → empty index, instant.
- **Acceptance (paired exact→paraphrase, `evaluate --hybrid` vs lexical):** exact ranks held or
  improved (dpop 7→4, kerberos 1→1, token-exchange 2→1 — **no regression**); paraphrases lifted
  hard (dpop 118→26, kerberos 87→31, token-exchange 10→3); recall @5 37%→58%, @10 closure
  74%→84%; mean context/query 84.7k→46.9k tokens.
- **Goldens stay lexical — do NOT re-record from `--hybrid`.** `selftest.py` runs under the system
  Python (no `sentence-transformers`), where `--hybrid` degrades to lexical. The committed
  `eval/baseline.eval*.out` are the dense-absent baseline; the model+index are gitignored, so a
  fresh checkout reproduces the lexical goldens. Re-recording them from a dense-enabled run would
  break `selftest` everywhere the model isn't vendored.

## Notes
- **Offline only.** `embed.py` loads the model by path; it never calls the network. If the
  library or model is absent, every consumer (`python3 -m wikikb kb ... --hybrid`, `python3 -m wikikb evaluate --hybrid`) degrades
  to **lexical** — the dense layer is an optional accelerator, never a hard dependency.
- **Derived + regenerable.** The model dir and the built index (`_meta/embeddings/*.npz`) are
  NOT committed (see `_meta/.gitignore`); rebuild from the immutable reference tier any time.
- **Delta-aware.** `--build` re-embeds only notes whose content hash changed (same sha256
  scheme `manifest.py` uses), so routine rebuilds are cheap.
