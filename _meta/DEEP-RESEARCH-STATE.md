# Deep-research checkpoint

Run: 2026-07-19, single session, no interruption.

- [x] Phase 1 — recon (lint --status, selftest.py timing, README/AGENTS/QUERY-CARD/eval-README/pyproject read, dir listings, CI check)
- [x] Phase 2 — verified S1-S9 (all true; S3/S7 needed corrected specifics), found N1-N11 new
- [x] Phase 3 — report written: `_meta/DEEP-RESEARCH-2026-07-19.md`
- [x] Phase 4 — fix run (this session, args contained "fix"): 5 commits, lint clean after each
  - dbfa746 S2: pyproject.toml packages (mcp/serve/tkg)
  - 74c4a9d S5: tags.py backfill --apply (25/90 pages; rest have no slug-keyword match)
  - 7b8cc14 S4: manifest seed (116 NEW -> 0; 6 GONE + 4 PENDING refs remain, content work not mechanical)
  - 0a2e7f4 S6: eval/README.md v2->v4 correction (20->29 cases)
  - c1aa664 S1: _meta/ROADMAP.md committed

STATUS: COMPLETE. All 5 requested P0 fixes applied and committed. Not fixed
(out of scope per the command's explicit list): N1 (Docker Kuzu dead config,
the report's only true P0), N2 (stale README counts), S3b (citation-grounding
lint false positives), N4/N6/N8/N10 (serve auth, tkg atomic write, grade300 CI
gating, undocumented SIGINT flake) — all tracked in ROADMAP.md Now/Later.
A future run of this skill should treat this as closed and start a fresh audit.
