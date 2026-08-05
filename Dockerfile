# llm-wiki — self-contained amd64 image: vault + wikikb toolchain + the full optional tier
# (langgraph graph-by-default, litellm gateway, dense/hybrid retrieval with the vendored model).
# Build:  docker buildx build --platform linux/amd64 -t llm-wiki:amd64 --load .
# Run:    docker run --rm -p 8642:8642 llm-wiki:amd64                    # JSON API on :8642
#         docker run --rm -i llm-wiki:amd64 python3 -m wikikb mcp        # MCP over stdio
# Python 3.12: the requirements.txt pins all ship cp312 manylinux wheels (cp314 lags).
FROM --platform=linux/amd64 python:3.12-slim

# The pins live in the two requirements files, not inline here — see their headers for WHY each
# version. Copied BEFORE the vault so a content-only change doesn't invalidate the pip layers.
COPY requirements.txt requirements-torch-cpu.txt /wiki/

# CPU-only torch first, from its own index — the default PyPI linux torch bundles CUDA (~2.5 GB of
# dead weight here). The --index-url is inside requirements-torch-cpu.txt, hence the separate file:
# it must NOT apply to the pins below (litellm/langgraph aren't on download.pytorch.org).
RUN pip install --no-cache-dir -r /wiki/requirements-torch-cpu.txt \
 && pip install --no-cache-dir -r /wiki/requirements.txt

COPY . /wiki
ENV PYTHONPATH=/wiki/_meta
WORKDIR /wiki/_meta

# CONTENT LAYOUT: everything the wiki needs lives under /wiki/vault (moved there 2026-08-05) —
# the page tiers, the immutable reference/_sources tiers, the generated indexes, taxonomy.md and
# .manifest.json. That single directory IS the knowledge base, so migrating between hosts is a
# copy of it and nothing else.
#
# This image bakes a snapshot of it. To serve HOST content instead, bind-mount over it and point
# the code at the mount (see docker-compose.yml, which does exactly this):
#     -v /srv/llm-wiki/vault:/data/vault  -e WIKIKB_VAULT_ROOT=/data/vault
# A bind mount SHADOWS the baked copy rather than merging with it, so seed the host directory
# first (`cp -a ./vault/. /srv/llm-wiki/vault/`) or the container serves an empty wiki.
ENV PYTHONIOENCODING=utf-8

# Point WIKI_LLM at a model endpoint at run time if you want synthesized (non-extractive) answers, e.g.
#   -e WIKI_LLM=local -e WIKI_LLM_MODEL=ollama/qwen2.5:3b -e WIKI_LLM_API_BASE=http://host.docker.internal:11434
EXPOSE 8642

# OPERATION MODE (WIKIKB_MODE) — one image, two postures, chosen at run time:
#   airgapped (default) vault + MCP + the PDF upload/ingest chain; no outbound connection, and the
#                       /scrape paths answer exactly like an unknown path (not fingerprintable).
#   online              the same surface PLUS the web scraper (mounted, 501 until implemented).
# The modes are ADDITIVE, so nothing is lost by running airgapped. An unknown value exits 2 rather
# than falling back — a mode is a posture, not a preference.
#   docker run --rm -p 8642:8642 -e WIKIKB_MODE=online llm-wiki:amd64

# Client PDF upload (opt-in, off by default — see serve.py's do_PUT for the trust boundary): mount the
# vault so an upload actually persists past the container's lifetime, enable uploads explicitly, then
# PUT the raw file (no multipart) to /upload/<domain>/<filename>.pdf:
#   docker run --rm -p 8642:8642 -v /srv/llm-wiki/vault:/data/vault \
#     -e WIKIKB_VAULT_ROOT=/data/vault -e WIKIKB_ALLOW_UPLOAD=1 llm-wiki:amd64
#   curl -T guide.pdf http://localhost:8642/upload/keycloak/guide.pdf
#   curl http://localhost:8642/jobs/<job_id>          # the conversion the upload queued
# Uploads land ONLY in vault/_sources/<domain>/_raw/pdfs/ (never reference/ or corpora/). Storing the
# file also QUEUES pdf_to_corpus --append -> corpus_to_vault -> build as a background job, so the drop
# becomes crosslinked Markdown without a second command; WIKIKB_AUTO_INGEST=0 restores store-only.

# API docs: GET /docs is a self-contained HTML reference (no CDN — it renders air-gapped); GET
# /openapi.json is the OpenAPI 3.1 document to point Swagger UI / Postman / an SDK generator at.

# CONFIG COMES FROM THE ENVIRONMENT, not from flags baked here — WIKIKB_PORT / WIKIKB_BIND /
# WIKIKB_MCP_PATH / WIKIKB_ALLOW_UPLOAD (see .env.example). CMD stays exec-form with no arguments
# because exec form performs NO shell expansion: `--port $WIKIKB_PORT` here would pass the literal
# string "$WIKIKB_PORT" to argparse. serve.py reads the env for its defaults instead, so `docker run
# -e WIKIKB_PORT=9000` works without a shell wrapper or an entrypoint script.
#
# WIKIKB_BIND=0.0.0.0 is a DELIBERATE, container-specific operator choice, not this project's default
# posture: serve.py binds loopback (127.0.0.1) by default because it is usually run bare-metal
# alongside its caller; inside a container, loopback is reachable only from INSIDE the container, so
# the image binds the container's own 0.0.0.0 and relies on `docker run -p` to control real exposure.
# Set WIKIKB_API_TOKEN whenever that published port is reachable from anything but localhost.
# WIKIKB_MODE is baked as the DEFAULT posture, not a preference: an image whose mode is unset would
# behave differently depending on the operator's shell. airgapped is the mode that can do less.
ENV WIKIKB_BIND=0.0.0.0 \
    WIKIKB_PORT=8642 \
    WIKIKB_MCP_PATH=/mcp \
    WIKIKB_MODE=airgapped
CMD ["python3", "-m", "wikikb", "serve"]
