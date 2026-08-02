"""graph/fileback.py — opt-in persistence for served answers (`ask --file-back` / mcp `file_back`).

Answers served over MCP/HTTP normally live only in the caller's chat; the wiki's amortization
loop (CLAUDE.md QUERY step 5) expects them filed into `questions/`. This writes the shared
`public_result` dict as a `questions/<slug>.md` DRAFT page under the filing rules the gate
enforces: `status: draft` always, `provenance: needs-review` (a machine cannot honestly assign
per-claim counts — lint warns until a human/LLM pass does), banner lines kept in the body, and
an existing slug is NEVER overwritten (dedup > freshness; update by hand or via QUERY).
Withheld/ungrounded answers are refused — strict mode exists precisely so those don't persist.
"""
import datetime
import os
import re

from wikikb import paths

QUESTIONS = str(paths.WIKI / "questions")
FOOTER = ("> Auto-filed by `wikikb ask --file-back` — machine-generated draft. Verify the answer "
          "against its References and assign real provenance counts before promoting past draft.")


def _slug(query):
    s = re.sub(r"[^a-z0-9]+", "-", query.lower()).strip("-")
    return s[:70].rstrip("-") or "question"


TIERS = ("conceptual", "support-kb", "scenarios")


def _yq(s):
    """Double-quoted YAML scalar. Control characters are collapsed to spaces so a
    caller-supplied string can never terminate the frontmatter block early and forge
    fields after it (the newline-injection class the 2026-07-22 gatekeeper review caught)."""
    s = re.sub(r"[\x00-\x1f\x7f]+", " ", str(s))
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def file_answer(result, question_tier=None):
    """result: the `public_result` dict. Returns {filed: bool, path: str|None, reason: str}."""
    err = paths.eval_lock_error()
    if err:
        return {"filed": False, "path": None, "reason": "eval lock: " + err}
    # filing is always strict, independent of how the answer was SERVED: a flagged answer may
    # still be shown to the caller (flag-by-default), but it must not persist into the vault
    if result.get("withheld"):
        return {"filed": False, "path": None, "reason": "answer was withheld (ungrounded) — not filing"}
    if result.get("grounding_fail") or result.get("ungrounded_identifiers") or result.get("premise_flags"):
        return {"filed": False, "path": None,
                "reason": "answer carries grounding/premise flags — not filing (serve-only)"}
    answer = (result.get("answer") or "").strip()
    if not answer:
        return {"filed": False, "path": None, "reason": "empty answer"}
    if not result.get("cited"):
        return {"filed": False, "path": None, "reason": "no cited sources — nothing to ground the page"}
    domain = result.get("domain")
    if not domain:
        return {"filed": False, "path": None, "reason": "no routed domain — file by hand with QUERY"}
    query = result.get("query") or ""
    slug = _slug(query)
    path = os.path.join(QUESTIONS, slug + ".md")
    if os.path.exists(path):
        return {"filed": False, "path": path, "reason": "questions/%s.md already exists — update it via QUERY" % slug}

    # summary: first prose line that isn't a banner/heading
    summary = next((ln.strip() for ln in answer.splitlines()
                    if ln.strip() and not ln.strip().startswith(("⚠️", "#", ">", "-", "["))), query)[:220]
    fm = ["---",
          "title: " + _yq(query[:300]),
          "type: question",
          "domain: " + domain,
          "slug: " + slug,
          "summary: " + _yq(summary),
          "sources:"]
    fm += ["  - kb:%s" % cid for cid in result.get("cited")]
    fm += ["provenance: needs-review"]
    if question_tier in TIERS:   # enum-checked here too — MCP arg is not schema-enforced server-side
        fm += ["question_tier: " + question_tier]
    fm += ["status: draft",
           "updated: " + datetime.date.today().isoformat(),
           "---"]
    body = "\n".join(fm) + "\n\n# %s\n\n%s\n\n%s\n" % (re.sub(r"\s+", " ", query)[:300], answer, FOOTER)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    return {"filed": True, "path": path, "reason": "filed as draft"}
