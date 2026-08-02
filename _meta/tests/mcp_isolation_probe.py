#!/usr/bin/env python3
"""mcp_isolation_probe.py — blocker-1/2 verification: a page filed into the LIVE vault
mid-run must be INVISIBLE to a case's wikikb MCP, and eval-born (`origin: eval-cohort`)
pages must be stripped from cohort snapshots.

Method (no model needed — talks the MCP stdio protocol directly, exactly as opencode would):
  1. plant a marker page in the LIVE vault questions/ (removed on exit);
  2. materialize a cohort snapshot (git archive of HEAD) + one case snapshot;
  3. spawn the MCP with the exact examinee env — live-package PYTHONPATH (the global
     opencode config's) + WIKIKB_VAULT_ROOT=<case> (injected by run300.ask; opencode
     ignores per-project MCP config, falsified 2026-07-12) → wiki_read_page(marker) must
     FAIL (invisible);
  4. control: spawn the MCP with the LIVE env, no override → wiki_read_page(marker) must
     SUCCEED (proves the probe detects leakage when it exists);
  5. assert the snapshot contains no page tagged `origin: eval-cohort` (same
     frontmatter-bounded check production uses).

Exit 0 = isolated; 1 = leak/assertion failure; 2 = environment problem.
"""
import json, pathlib, re, subprocess, sys, types, uuid

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "eval"))
import run300


def mcp_call(env_extra, tool, args, cwd):
    # cwd matters: `python -m` puts cwd ahead of PYTHONPATH, so we must NOT run from a
    # directory containing a wikikb package (opencode spawns MCP from the project dir,
    # which never contains one at its root — mirror that).
    reqs = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
         "params": {"name": tool, "arguments": args}},
    ]
    payload = "".join(json.dumps(r) + "\n" for r in reqs)
    p = subprocess.run([sys.executable, "-m", "wikikb", "mcp"], input=payload,
                       capture_output=True, text=True, timeout=60, cwd=cwd,
                       env={"PATH": "/usr/bin:/bin", **env_extra})
    for line in p.stdout.splitlines():
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if obj.get("id") == 2:
            return obj
    return {"error": {"message": "no rpc response; stderr: " + p.stderr[-200:]}}


def found(resp):
    if "error" in resp:
        return False
    result = resp.get("result", {})
    if result.get("isError"):
        return False
    return "MCP-ISOLATION-MARKER" in json.dumps(result)


def main():
    marker_slug = "mcp-isolation-marker-" + uuid.uuid4().hex[:8]
    marker = run300.WIKI / "questions" / (marker_slug + ".md")
    args = types.SimpleNamespace(model="probe", workers=1, timeout=60,
                                 max_consecutive_timeouts=0, no_expand=False,
                                 allow_dirty=True)
    man = run300.build_manifest(args, str(run300.HERE / "cases300.jsonl"))
    snap = case = None
    ok = True
    try:
        marker.write_text("---\ntitle: MCP isolation marker\ntype: question\n"
                          "domain: keycloak\nslug: %s\n---\n\nMCP-ISOLATION-MARKER\n"
                          % marker_slug, encoding="utf-8")
        src = run300.materialize_cohort_snapshot(man)
        case = run300.build_case_snapshot("mcp-probe", src)
        live_meta = str(run300.WIKI / "_meta")

        live = mcp_call({"PYTHONPATH": live_meta}, "wiki_read_page", {"slug": marker_slug},
                        cwd=str(run300.WIKI))
        if not found(live):
            print("FAIL (control): live-vault MCP cannot see the marker — probe cannot "
                  "detect leakage; response: %s" % json.dumps(live)[:200])
            return 2
        print("PASS (control): live-vault MCP sees the marker")

        # exactly what the examinee's env produces: global-config PYTHONPATH (live
        # package) + WIKIKB_VAULT_ROOT scoping the vault reads to the case snapshot
        iso = mcp_call({"PYTHONPATH": live_meta, "WIKIKB_VAULT_ROOT": str(case)},
                       "wiki_read_page", {"slug": marker_slug}, cwd=str(case))
        if found(iso):
            print("FAIL (isolation): snapshot-routed MCP sees the mid-run filed page")
            ok = False
        else:
            print("PASS (isolation): mid-run filed page invisible to the case MCP")

        leaked = []
        for d in ("questions", "topics", "entities"):
            for p in (case / d).glob("*.md") if (case / d).is_dir() else []:
                fm = run300._frontmatter_block(p.read_text(encoding="utf-8", errors="replace"))
                if re.search(r"^origin:\s*eval-cohort\s*$", fm, re.M):
                    leaked.append(p.name)
        if leaked:
            print("FAIL (origin-filter): eval-born pages present in snapshot: %s" % leaked[:5])
            ok = False
        else:
            print("PASS (origin-filter): no origin:eval-cohort page in the case snapshot "
                  "(stripped at materialize: %d)" % len(man.get("eval_born_pages_stripped", [])))
        return 0 if ok else 1
    finally:
        marker.unlink(missing_ok=True)
        if case is not None:
            import shutil
            shutil.rmtree(case, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
