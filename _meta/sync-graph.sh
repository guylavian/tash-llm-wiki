#!/bin/sh
# Obsidian → Graphify sync: rebuild the curated semantic graph after wiki edits.
# Chain: crosslink (kb: → [[links]]) → index → tkg ingest (typed graph)
#        → graphify_export (curated graph.json) → graphify cluster-only (communities/report/viz)
#        → graphlinks (writes communities back as graph_community: frontmatter — the reverse leg)
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
# graphlinks needs community_name on graph.json's nodes, which only `graphify cluster-only`
# adds — if graphify isn't installed (guard above skipped) the field is simply absent and
# graphlinks upserts/removes zero pages, so the script still succeeds either way.
python3 -m wikikb graphlinks --apply
echo "graph sync done — graphify-out/graph.{json,html} + _meta/tkg/graph.html current"
