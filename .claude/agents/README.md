# Subagent team

`CLAUDE.md` ("Operational lessons") names four agents that are dispatched by name during
validation and implementation waves:

| Agent | Role |
|---|---|
| `wiki-implementer` | Writes/edits synthesis pages under the CLAUDE.md contract |
| `sre-validator` | Validates pages against the raw tier; runs the live-query bank |
| `adversarial-reviewer` | Tries to refute findings — see the independence rule below |
| `researcher` | Corpus/reference sweeps that return protocol-grade findings |

**The definitions are not written yet.** This directory exists so the location is tracked and
the constraints below are inherited rather than rediscovered; authoring them is a separate
change, not part of the repo tidy that created this file.

## Constraints any definition here must honor

- **Model tier.** Every agent carries an explicit `model:` — `sonnet` for implementation,
  review, and research; `haiku` for mechanical/bulk work. Never the top tier: the main session
  model plans, orchestrates, and verifies; it does not burn tokens on delegable legwork.
- **Concurrency.** Max 3 agents at once. Higher concurrency stalled/crashed agents twice
  (2026-07-04/05: a 7-agent wave lost 5 of 6). Run waves of ≤3.
- **Validation independence.** `adversarial-reviewer` must not be the implementer's model
  family. Where a different family isn't available, any sign-off it feeds must be labeled
  "same-family — NOT independent". No self-adjudication.
- **Research agents return protocol-grade findings** — per-claim `file.md:line` citations and
  extracted/`(inferred)` tags, per the query-answering protocol in `CLAUDE.md`. The layer that
  writes the user-facing answer runs the Final self-check; a subagent having touched the wiki
  does not discharge it.

## Loading

A `.claude/agents/` directory created mid-session is **not** hot-reloaded — Claude Code must be
restarted before the team loads by name. In-session workaround: dispatch `general-purpose` with
the agent file injected as the system prompt plus the matching `model:`.
