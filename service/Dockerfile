# Air-gapped serving image. Base MUST be pinned by DIGEST from the internal mirror (NFR-5).
# OPEN QUESTION OQ-4 (spec.md): the internal mirror's digest for python:3.12-slim is unknown
# from the build sandbox and the rules forbid external fetch. Replace the placeholder below
# with the mirror's resolved digest before building:
#   docker pull <INTERNAL_MIRROR>/python:3.12-slim && docker inspect --format '{{index .RepoDigests 0}}' ...
ARG BASE=<INTERNAL_MIRROR>/python:3.12-slim@sha256:<PIN_FROM_INTERNAL_MIRROR>
FROM ${BASE}

# Default image = lexical (zero ML deps). For the embedding target, build with
#   --build-arg REQ=requirements-embedding.txt
ARG REQ=requirements.txt
ARG PIP_INDEX_URL=<INTERNAL_MIRROR>

WORKDIR /app
COPY requirements.txt requirements-embedding.txt ./
RUN pip install --no-cache-dir --index-url "${PIP_INDEX_URL}" -r "${REQ}"

COPY wiki_router ./wiki_router

# The curated repo is mounted READ-ONLY at /repo (NFR-1 stateless, FR-1 source of truth).
ENV WIKI_REPO_ROOT=/repo \
    WIKI_RANKER=lexical \
    PYTHONUNBUFFERED=1
EXPOSE 8000

# Local-only healthcheck against /healthz (FR-7).
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/healthz').status==200 else 1)"

# Factory entrypoint avoids an import-time repo scan (design.md).
CMD ["uvicorn", "wiki_router.app:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
