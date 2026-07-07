# Docker Setup for Keycloak/RHBK Wiki with Kuzu

This directory contains Docker configuration to run the wiki toolchain with all dependencies, including Kuzu for the TKG backend.

## Quick Start

```bash
# From the wiki/_meta directory
cd /Users/guylavian/Downloads/skills/keycloak-admin/wiki/_meta

# Build and start the container
docker-compose up -d

# Verify Kuzu is available
docker-compose exec wiki python3 -m wikikb tkg graph-status

# Build the TKG graph
docker-compose exec wiki python3 -m wikikb tkg ingest

# Run queries
docker-compose exec wiki python3 -m wikikb tkg temporal-query --as-of 26.2
docker-compose exec wiki python3 -m wikikb tkg cross-domain-query "keycloak active-directory"

# Run other wiki commands
docker-compose exec wiki python3 -m wikikb lint
docker-compose exec wiki python3 -m wikikb index
docker-compose exec wiki python3 tests/selftest.py
```

## What's Included

- **Python 3.12** with all build dependencies
- **cmake** and build-essential for compiling Kuzu
- **Kuzu** Python package (compiled from source)
- **Optional online tier** (LiteLLM, LangGraph) from requirements-online.txt
- **Volume mounts** for live editing and persistent data

## Architecture

```
Host Machine                    Docker Container
├── wiki/                  →    /wiki/ (mounted)
│   ├── topics/                 (live edits reflected)
│   ├── entities/
│   ├── questions/
│   └── _meta/
│       ├── tkg/           →    tkg-data volume (persistent)
│       └── embeddings/    →    embeddings-data volume (persistent)
```

## Environment Variables

Set in `docker-compose.yml`:

- `WIKI_TKG=kuzu` - Enable Kuzu backend
- `LITELLM_LOCAL_MODEL_COST_MAP=True` - Air-gap safety
- `GRAPHITI_TELEMETRY_ENABLED=False` - No telemetry
- `KUZU_DISABLE_TELEMETRY=1` - No telemetry

## Connecting to Local Ollama (Optional)

If you have Ollama running on your host machine and want to use it from the container:

1. Uncomment `network_mode: host` in `docker-compose.yml`, OR
2. Use `host.docker.internal` as the API base:
   ```yaml
   environment:
     - WIKI_LLM=local
     - WIKI_LLM_API_BASE=http://host.docker.internal:11434
   ```

## Persistent Data

Two Docker volumes preserve data across container restarts:
- `tkg-data` - The Kuzu database (`_meta/tkg/kuzu/`)
- `embeddings-data` - Dense embeddings (`_meta/embeddings/`)

To reset:
```bash
docker-compose down -v  # Removes volumes
docker-compose up -d
```

## Interactive Shell

```bash
# Get a shell inside the container
docker-compose exec wiki bash

# Run commands directly
cd /wiki/_meta
python3 -m wikikb --help
```

## Building Without Docker Compose

```bash
# Build the image
docker build -t keycloak-wiki -f _meta/Dockerfile ..

# Run interactively
docker run -it --rm \
  -v "$(pwd)/..:/wiki" \
  -e WIKI_TKG=kuzu \
  keycloak-wiki bash
```

## Troubleshooting

### Kuzu build fails
- The Dockerfile installs cmake and build-essential
- If build still fails, check Docker has enough memory (4GB+ recommended)

### Permission issues
- The container runs as root by default
- Files created in mounted volumes will be owned by root
- Add `user: "${UID}:${GID}"` to docker-compose.yml if needed

### TKG commands fail
- Verify Kuzu installed: `docker-compose exec wiki python3 -c "import kuzu; print('OK')"`
- Check backend status: `docker-compose exec wiki python3 -m wikikb tkg graph-status`
- Ensure `WIKI_TKG=kuzu` is set

## Air-Gap Compliance

The Docker setup maintains the wiki's air-gap design:
- Kuzu is **embedded** (file-based database, no network)
- No external network calls during operation
- Telemetry disabled for all components
- Optional LLM tier uses local loopback only (Ollama on host)

## Next Steps

After setup:
1. Build the TKG: `docker-compose exec wiki python3 -m wikikb tkg ingest`
2. Run tests: `docker-compose exec wiki python3 tests/selftest.py`
3. Query the graph: `docker-compose exec wiki python3 -m wikikb tkg temporal-query --as-of 26.2`
4. Verify: `docker-compose exec wiki python3 -m wikikb lint --status`
