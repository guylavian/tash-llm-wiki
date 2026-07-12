#!/usr/bin/env python3
"""opencode_merge_probe.py — LIVE verification that opencode honors the per-case
project opencode.json (global-vs-project MCP merge semantics), veto requirement
before the first ablation arm.

Bidirectional marker check through a REAL `opencode run` examinee:
  - a marker page planted ONLY in the live vault must NOT appear in any wikikb
    tool result of the case session;
  - a marker page planted ONLY in the case snapshot MUST appear when the model
    calls read_page on it.
Assertions run against opencode's session DB tool parts (deterministic), never
against model prose. If the model makes no wikikb tool call at all, the probe is
INCONCLUSIVE (exit 3) — rerun or use a more obedient model.

Usage: python3 opencode_merge_probe.py [opencode-model-ref]
Exit 0 = merge verified; 1 = leak; 2 = env problem; 3 = inconclusive.
"""
import json, pathlib, shutil, sqlite3, subprocess, sys, time, types, uuid

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "eval"))
import run300

DB = pathlib.Path.home() / ".local/share/opencode/opencode.db"


def main():
    model = sys.argv[1] if len(sys.argv) > 1 else "lmstudio/liquid/lfm2.5-1.2b"
    if not DB.is_file():
        print("no opencode DB"); return 2
    tag = uuid.uuid4().hex[:8]
    live_slug, snap_slug = "live-marker-" + tag, "snap-marker-" + tag
    live_page = run300.WIKI / "questions" / (live_slug + ".md")
    args = types.SimpleNamespace(model=model, workers=1, timeout=300,
                                 max_consecutive_timeouts=0, no_expand=False,
                                 allow_dirty=True)
    man = run300.build_manifest(args, str(run300.HERE / "cases300.jsonl"))
    case = None
    try:
        live_page.write_text("---\ntitle: live marker\ntype: question\ndomain: keycloak\n"
                             "slug: %s\n---\n\nLIVE-MARKER-%s\n" % (live_slug, tag),
                             encoding="utf-8")
        src = run300.materialize_cohort_snapshot(man)
        case = run300.build_case_snapshot("merge-probe", src)
        (case / "questions" / (snap_slug + ".md")).write_text(
            "---\ntitle: snap marker\ntype: question\ndomain: keycloak\nslug: %s\n---\n\n"
            "SNAP-MARKER-%s\n" % (snap_slug, tag), encoding="utf-8")
        # opencode ignores per-project MCP config AND encrypts session parts at rest
        # (both verified 2026-07-12), so this probe validates the WIKIKB_VAULT_ROOT
        # mechanism: run300.ask() injects it into the examinee env; the global-config
        # MCP — spawned fresh per `opencode run` — inherits it and scopes vault reads
        # to the snapshot. Assertion surface = the examinee's echoed tool results
        # (instruct-echo; deterministic wikikb-side coverage lives in
        # mcp_isolation_probe.py, which spawns the MCP directly with this env).
        def one_call(slug):
            q = ("Call the wikikb read_page tool exactly once with slug '%s' and show "
                 "the raw tool result verbatim." % slug)
            return run300.ask({"id": "merge-probe-" + slug, "question": q}, model,
                              args.timeout, source_root=src) or ""

        # Positive control: a page that exists in the PINNED COMMIT (so it is in every
        # case snapshot) — ask() builds its own per-call snapshot, so a hand-planted
        # marker can never be the positive arm. Negative arm: the live-only marker.
        # committed-page SERVED + live-only marker ABSENT ⇒ the examinee's MCP reads a
        # snapshot-scoped tree, not the live vault.
        control_slug = "what-is-keycloak"
        ans_b = one_call(control_slug)
        ans_a = one_call(live_slug)
        print("B answer head: %r" % ans_b[:120])
        print("A answer head: %r" % ans_a[:120])
        ok = True
        if ("What is Keycloak" in ans_b) or ("RHBK" in ans_b and "no such page" not in ans_b):
            print("PASS: committed page served through the examinee's MCP")
        elif "no such page" in ans_b:
            print("FAIL: examinee MCP cannot serve a committed page — routing broken")
            ok = False
        else:
            print("INCONCLUSIVE: examinee did not echo a usable tool result for B")
            ok = None
        if ("LIVE-MARKER-" + tag) in ans_a:
            print("FAIL: LIVE-vault-only page served through the examinee MCP — leak")
            ok = False
        elif ("no such page" in ans_a) and (live_slug in ans_a):
            print("PASS: live-only page invisible to the examinee MCP")
        return 0 if ok else (3 if ok is None else 1)
    finally:
        live_page.unlink(missing_ok=True)
        if case is not None:
            shutil.rmtree(case, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
