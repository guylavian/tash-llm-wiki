# Offline embedding model — vendoring (air-gapped)

The Phase-3 dense layer (`_meta/bin/embed.py`) loads a sentence-transformers model **by
local path** — never from the network. Vendor it once on a connected machine, copy it here,
and the air-gapped workstation uses it offline.

Default model: **`bge-small-en-v1.5`** (~130 MB, 384-dim, strong for short-passage retrieval).
Override with `embed.py --model <name>` (the dir name under `_meta/models/` must match).

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

`embed.py --domains` should now report `library=yes model[bge-small-en-v1.5]=yes`.

## 3. Build the index (delta-aware) and use it

```bash
python3 _meta/bin/embed.py --domain keycloak         --build
python3 _meta/bin/embed.py --domain active-directory --build
# retrieval auto-uses it:
python3 _meta/bin/kb.py --domain keycloak search "proof of possession token binding" --hybrid
python3 _meta/bin/eval.py --route --graph --hybrid   # the acceptance-proof run
```

## Notes
- **Offline only.** `embed.py` loads the model by path; it never calls the network. If the
  library or model is absent, every consumer (`kb.py --hybrid`, `eval.py --hybrid`) degrades
  to **lexical** — the dense layer is an optional accelerator, never a hard dependency.
- **Derived + regenerable.** The model dir and the built index (`_meta/embeddings/*.npz`) are
  NOT committed (see `_meta/.gitignore`); rebuild from the immutable reference tier any time.
- **Delta-aware.** `--build` re-embeds only notes whose content hash changed (same sha256
  scheme `manifest.py` uses), so routine rebuilds are cheap.
