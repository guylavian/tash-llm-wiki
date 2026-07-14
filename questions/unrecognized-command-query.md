---
title: Why do I get "Unrecognized command '/query'"?
type: question
question_tier: conceptual
domain: keycloak
slug: unrecognized-command-query
summary: The local wiki/query workflow is exposed as `wikikb ask` and `GET /ask`; `/query` is not a documented runtime command in this vault.
sources:
  - ref:query-card-md
  - ref:opencode-command-query-md
  - ref:wikikb-serve-py
provenance:
  extracted: 3
  inferred: 1
  ambiguous: 0
status: draft
updated: 2026-07-12
---

# Why do I get "Unrecognized command '/query'"?

`/query` is not a supported runtime command in this repo's documented wiki interface. The query protocol here says to use `wikikb ask` for the QUERY operation, and the CLI fallback is `python3 -m wikikb ask "$ARGUMENTS" --json` (`QUERY-CARD.md:13-16`). The HTTP surface exposes `GET /ask`, `GET /route`, `GET /search`, `GET /page/<slug>`, and `GET /expand`, but not `/query` (`_meta/wikikb/serve/serve.py:19-28`).

The local `.opencode/command/query.md` file exists, but it is a command definition that points back to `wikikb ask`; it is not evidence of a built-in `/query` slash command in the runtime that produced your error (`.opencode/command/query.md:1-16`). So the error most likely means the shell/client you are using does not have a `/query` command registered, or it is using a different command namespace than the repo's wiki workflow.

Use one of these instead:

- `wikikb ask "<question>"`
- `python3 -m wikikb ask "<question>" --json`
- `GET /ask?q=<question>` if you are using the local HTTP API (`_meta/wikikb/serve/serve.py:19-25`)

If you expected `/query` to work inside a specific client, check that client's command registration or alias layer. In this repo, the canonical entry point is `ask`, not `query` (`QUERY-CARD.md:12-16`).

## References

### RH ground-truth
- `ref:query-card-md` — QUERY protocol card
- `ref:opencode-command-query-md` — `.opencode/command/query.md`
- `ref:wikikb-serve-py` — local wiki HTTP API surface

### Wiki
- None
