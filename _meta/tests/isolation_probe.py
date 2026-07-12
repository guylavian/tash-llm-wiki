#!/usr/bin/env python3
"""isolation_probe.py — EMPIRICAL examinee-isolation check (R1, consensus 2026-07-12).

Static review proved cwd= is not enough: opencode anchors its project dir to $PWD
(session DB evidence, 2026-07-12 morning smoke). This probe runs ONE trivial case
through run300.ask() and asserts, from opencode's own session database:
  (a) a session was created whose `directory` is inside the case-snapshot workspace
      root — i.e. env["PWD"]=snap took effect;
  (b) no new file appeared in the LIVE vault's questions/ during the probe.
Safe to run while a v1 cohort is live: v1 sessions anchor to the runner's PWD, never
to the workspace root, so they cannot false-positive (a).

Usage: python3 isolation_probe.py [opencode-model-ref]   (default: local LM Studio)
Exit 0 = isolated; 1 = assertion failed; 2 = environment problem (no DB / no model).
"""
import pathlib, sqlite3, sys, time, types

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "eval"))
import run300

DB = pathlib.Path.home() / ".local/share/opencode/opencode.db"


def main():
    model = sys.argv[1] if len(sys.argv) > 1 else "lmstudio/liquid/lfm2.5-1.2b"
    if not DB.is_file():
        print("no opencode session DB at %s" % DB)
        return 2
    args = types.SimpleNamespace(model=model, workers=1, timeout=240,
                                 max_consecutive_timeouts=0, no_expand=False,
                                 allow_dirty=True)
    man = run300.build_manifest(args, str(run300.HERE / "cases300.jsonl"))
    src = run300.materialize_cohort_snapshot(man)
    live_q = run300.WIKI / "questions"
    before = {p.name for p in live_q.glob("*.md")}
    t0_ms = int(time.time() * 1000)
    ans = run300.ask({"id": "isolation-probe", "question": "Reply with exactly: OK"},
                     model, args.timeout, source_root=src)
    after = {p.name for p in live_q.glob("*.md")}
    con = sqlite3.connect("file:%s?mode=ro" % DB, uri=True)
    rows = con.execute("SELECT directory FROM session WHERE time_created >= ?",
                       (t0_ms,)).fetchall()
    con.close()
    ws = str(run300.WORKSPACE_ROOT)
    anchored = [d for (d,) in rows if d and d.startswith(ws)]
    print("answer head: %r" % ans[:60])
    print("new sessions since t0: %d, workspace-anchored: %d" % (len(rows), len(anchored)))
    ok = True
    if not anchored:
        print("FAIL (a): no session anchored under %s — PWD fix not effective" % ws)
        ok = False
    else:
        print("PASS (a): session directory %s" % anchored[0])
    leaked = after - before
    if leaked:
        print("FAIL (b): live-vault questions/ gained files during probe: %s" % sorted(leaked))
        ok = False
    else:
        print("PASS (b): live-vault questions/ unchanged")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
