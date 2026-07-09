# llm-wiki — self-contained amd64 image: vault + wikikb toolchain + the full optional tier
# (langgraph graph-by-default, litellm gateway, dense/hybrid retrieval with the vendored model).
# Build:  docker buildx build --platform linux/amd64 -t llm-wiki:amd64 --load .
# Run:    docker run --rm -p 8642:8642 llm-wiki:amd64                    # JSON API on :8642
#         docker run --rm -i llm-wiki:amd64 python3 -m wikikb mcp        # MCP over stdio
# Python 3.12: the requirements-online.txt pins all ship cp312 manylinux wheels (cp314 lags).
FROM --platform=linux/amd64 python:3.12-slim

# CPU-only torch first — the default PyPI linux torch bundles CUDA (~2.5 GB of dead weight here).
RUN pip install --no-cache-dir torch==2.12.1 --index-url https://download.pytorch.org/whl/cpu

# Pinned to the VERIFIED working set from this repo's .venv-online/.venv-embed (py3.12) —
# requirements-online.txt's tokenizers==0.21.0 pin conflicts with litellm 1.83.7 and is
# documented in that file as unverified.
RUN pip install --no-cache-dir \
    litellm==1.83.7 langgraph==1.2.6 tokenizers==0.22.2 \
    numpy==2.5.0 sentence-transformers==5.6.0 transformers==5.12.1

COPY . /wiki
ENV PYTHONPATH=/wiki/_meta
WORKDIR /wiki/_meta

# Point WIKI_LLM at a model endpoint at run time if you want synthesized (non-extractive) answers, e.g.
#   -e WIKI_LLM=local -e WIKI_LLM_MODEL=ollama/qwen2.5:3b -e WIKI_LLM_API_BASE=http://host.docker.internal:11434
EXPOSE 8642

# Client PDF upload (opt-in, off by default — see serve.py's do_PUT for the trust boundary): mount the
# vault so an upload actually persists past the container's lifetime, pass --allow-upload explicitly,
# then PUT the raw file (no multipart) to /upload/<domain>/<filename>.pdf:
#   docker run --rm -p 8642:8642 -v $(pwd):/wiki llm-wiki:amd64 \
#     python3 -m wikikb serve --bind 0.0.0.0 --port 8642 --allow-upload
#   curl -T guide.pdf http://localhost:8642/upload/keycloak/guide.pdf
# Uploads land ONLY in _sources/<domain>/_raw/pdfs/ (never reference/ or corpora/); the operator still
# runs pdf_to_corpus -> corpus_to_vault -> wikikb build to fold a drop into the wiki (CLAUDE.md, INGEST).

# 0.0.0.0 here is a DELIBERATE, container-specific operator choice, not this project's default posture:
# serve.py itself binds loopback (127.0.0.1) by default (see serve.py's module docstring) because it's
# usually run bare-metal alongside its caller; inside a container, loopback is only reachable from
# INSIDE the container, so the image's CMD binds the container's own 0.0.0.0 and relies on `docker run
# -p` to control what's actually exposed on the host — the equivalent of an explicit --bind choice, not
# an accidental wider-than-default one.
CMD ["python3", "-m", "wikikb", "serve", "--bind", "0.0.0.0", "--port", "8642"]
