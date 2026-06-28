# LLM-Wiki Serving Layer

Read-only routing + retrieval over the curated wiki, air-gapped. SDD docs: `spec.md` →
`design.md` → `tasks.md` → code → `TRACEABILITY.md`. This service does **no generation**.

## Run locally (lexical, zero ML deps)

```bash
python3.12 -m venv .venv && . .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install --index-url <INTERNAL_MIRROR> -r requirements.txt
export WIKI_REPO_ROOT=/path/to/repo                     # repo containing references/
uvicorn wiki_router.app:create_app --factory --host 0.0.0.0 --port 8000
```

## curl

```bash
curl -s localhost:8000/healthz
curl -s -X POST localhost:8000/route -H 'Content-Type: application/json' \
     -d '{"query":"ISPN000541 cache dns","version":"26.6","k":5}'
curl -s "localhost:8000/get?path=references/observability.md&section=ispn000541-cache-dns-failure"
curl -s -X POST localhost:8000/reload -H "X-Admin-Token: $WIKI_ADMIN_TOKEN"
curl -s localhost:8000/metrics
```

## Embedding / hybrid (optional, Stage 1)

```bash
pip install --index-url <INTERNAL_MIRROR> -r requirements-embedding.txt
export WIKI_RANKER=hybrid                                # or: embedding
export WIKI_EMBED_ENDPOINT=http://127.0.0.1:11434/v1/embeddings   # loopback only
# no endpoint/model => service starts and serves lexical with a warning (FR-9)
```

## Docker

```bash
# 1) fill the base digest (spec OQ-4) from the internal mirror, then:
docker build -t wiki-router:lexical \
  --build-arg BASE=<INTERNAL_MIRROR>/python:3.12-slim@sha256:<DIGEST> \
  --build-arg PIP_INDEX_URL=<INTERNAL_MIRROR> .
docker run --rm -p 8000:8000 -v /path/to/repo:/repo:ro wiki-router:lexical
# embedding image: add --build-arg REQ=requirements-embedding.txt
```

## Tests

```bash
service/.venv-svc/bin/python service/tests/test_router.py      # plain runner -> "ALL PASS"
# or: service/.venv-svc/bin/python -m pytest service/tests/test_router.py
```

## Config (env)

`WIKI_REPO_ROOT` · `WIKI_RANKER`=lexical|embedding|hybrid · `WIKI_EMBED_ENDPOINT` (loopback) ·
`WIKI_EMBED_MODEL_PATH` · `WIKI_EMBED_STORE` · `WIKI_ADMIN_TOKEN` (gates `/reload`) ·
`WIKI_DEFAULT_K`. See `design.md` for the table.
