# `_sources/` — raw harvest staging (NOT wiki content)

Raw harvest notes for upstream **`web:` tier** standards (IETF RFCs & drafts,
OpenID Foundation specs, OWASP, reputable practitioner docs), fetched on the
networked **build plane** and consumed downstream by the air-gapped OpenCode
runtime.

- **Excluded from the content scanners.** `lint.py` scans only
  `topics/ entities/ questions/` (`PAGE_DIRS`); `crosslink.py`/`tags.py` follow the
  same convention. Files here are never linted, linked, or counted as pages —
  same discipline as `kb/` and `_meta/`.
- **Not ground truth.** This is upstream/community material, distinct from the
  immutable RHBK corpus in `../../kb/` and `../../references/`. Never write RHBK
  ground-truth here, and never write harvested upstream text into `kb/`.
- **Provenance, not transcripts.** Each `<id>.md` records the source URL, fetch
  date, spec status/revision, the load-bearing requirements (paraphrased — no long
  verbatim excerpts, copyright), and which wiki concept pages it feeds. The full
  text stays at its URL.
- **Delta-friendly.** The `_meta/.manifest.json` records each source so re-runs
  only re-distill genuinely new/changed material.

One file per harvested source (or tightly-related cluster). Grow via the wiki
INGEST op in `../CLAUDE.md`.
