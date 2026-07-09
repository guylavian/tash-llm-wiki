#!/bin/sh
# Obsidian → Graphify sync: rebuild the curated semantic graph after wiki edits.
# Chain: crosslink (kb: → [[links]]) → index → tkg ingest (typed graph)
#        → graphify_export (curated graph.json) → graphify cluster-only (communities/report/viz)
# Install as a git hook:  git config core.hooksPath _meta/hooks
# NOTE: never run `graphify update .` on the wiki — it re-extracts headings (noise)
#       and clobbers the curated export. This script is the write path to graphify-out/.
set -e
META="$(cd "$(dirname "$0")" && pwd)"
cd "$META"
python3 -m wikikb crosslink --apply
python3 -m wikikb index
python3 -m wikikb tkg ingest
python3 -m wikikb.tkg.graphify_export
python3 -m wikikb.tkg.viewer
command -v graphify >/dev/null && graphify cluster-only "$META/.." --no-label
echo "graph sync done — graphify-out/graph.{json,html} + _meta/tkg/graph.html current"
