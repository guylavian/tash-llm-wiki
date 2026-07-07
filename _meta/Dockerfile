# Dockerfile for Keycloak/RHBK Wiki with Kuzu TKG backend
# Build context: parent directory (wiki/)
# Build: docker build -t keycloak-wiki -f _meta/Dockerfile .

FROM python:3.12-slim

# Install build dependencies for Kuzu
RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /wiki

# Copy the entire wiki structure
COPY . /wiki/

# Install Kuzu (will compile from source using cmake)
RUN pip install --no-cache-dir kuzu

# Install optional online tier dependencies if file exists
RUN if [ -f _meta/requirements-online.txt ]; then \
        pip install --no-cache-dir -r _meta/requirements-online.txt || true; \
    fi

# Set environment variables for air-gap safety
ENV LITELLM_LOCAL_MODEL_COST_MAP=True
ENV GRAPHITI_TELEMETRY_ENABLED=False
ENV KUZU_DISABLE_TELEMETRY=1
ENV PYTHONDONTWRITEBYTECODE=1

# Default to Kuzu backend enabled
ENV WIKI_TKG=kuzu

# Set Python path to find wikikb package
ENV PYTHONPATH=/wiki/_meta

# Expose port for potential future HTTP API (not currently used)
EXPOSE 8080

# Default command: show TKG status
WORKDIR /wiki/_meta
CMD ["python3", "-m", "wikikb", "tkg", "graph-status"]
