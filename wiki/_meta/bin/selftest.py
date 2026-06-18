#!/usr/bin/env python3
"""selftest.py — offline smoke test for the wiki tooling. stdlib only, no network.

A tripwire against silent breakage from the content-mutating tools (corpus_to_vault,
backfill, crosslink, index) and the kb.py/lint changes. Runs each tool and asserts
the invariants that "looks fine by eye" doesn't catch. Exit 0 = all pass, 1 = failure.

    python3 wiki/_meta/bin/selftest.py
"""
import os
import re
import subprocess
import sys

BIN = os.path.dirname(os.path.abspath(__file__))
WIKI = os.path.dirname(os.path.dirname(BIN))
REF = os.path.join(WIKI, "reference")
PY = sys.executable
checks = []


def run(*args):
    p = subprocess.run([PY, os.path.join(BIN, args[0])] + list(args[1:]),
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def check(name, ok, detail=""):
    checks.append((name, ok, detail))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  — {detail}" if detail and not ok else ""))


# 1. kb.py reads the vault reference tier and reports a domain with notes
rc, out = run("kb.py", "domains")
m = re.search(r"keycloak\s+(\d+)\s+notes", out)
n_kb = int(m.group(1)) if m else 0
check("kb.py domains lists keycloak with notes", rc == 0 and n_kb > 0, f"rc={rc} n={n_kb}")

# 2. kb.py search returns ranked hits
rc, out = run("kb.py", "--domain", "keycloak", "search", "dpop sender constrained", "--limit", "3")
check("kb.py search returns hits", rc == 0 and "hit(s)" in out, out[:120])

# 3. abstract ranking signal is present in reference notes (regression guard for #4)
abstracts = 0
refdir = os.path.join(REF, "keycloak")
if os.path.isdir(refdir):
    for fn in os.listdir(refdir):
        if fn.endswith(".md") and not fn.startswith("_"):
            with open(os.path.join(refdir, fn), encoding="utf-8") as fh:
                if re.search(r"^abstract:", fh.read(), re.M):
                    abstracts += 1
check("reference notes carry abstract:", abstracts > 0, f"{abstracts} notes with abstract")

# 4. lint has no ERRORS (exit 0 under --strict)
rc, out = run("lint.py", "--strict")
check("lint.py --strict is clean (no errors)", rc == 0, out[-200:])

# 5. routing + reference indexes are not stale
rc, out = run("index.py", "--check")
check("index.py --check up to date", rc == 0, out[-200:])

# 6. every kb: token resolves (crosslink reports no 'unresolved' line)
rc, out = run("crosslink.py")
check("crosslink.py 0 unresolved kb: tokens", rc == 0 and "unresolved" not in out, out[:160])

# 7. no orphan reference notes (every body note linked by a group index)
body, linked = set(), set()
if os.path.isdir(refdir):
    for fn in os.listdir(refdir):
        if fn.endswith(".md") and not fn.startswith("_"):
            body.add(fn[:-3])
        if fn.startswith("_ref-") and fn.endswith(".md"):
            with open(os.path.join(refdir, fn), encoding="utf-8") as fh:
                linked |= {t.strip() for t in re.findall(r"\[\[([^\]|#]+)", fh.read())}
orphans = body - linked
check("0 orphan reference notes", len(orphans) == 0, f"{len(orphans)} orphans e.g. {list(orphans)[:3]}")

# 8. gated pointer index exists and is non-empty
gated = os.path.join(refdir, "_gated-kb-index.md")
gok = os.path.exists(gated) and open(gated, encoding="utf-8").read().count("\n## ") > 0
check("gated KB index present + non-empty", gok)

# 9. reference-tier integrity (FIX 2): no drift vs _meta/reference.lock.json
rc, out = run("corpus_to_vault.py", "--verify")
check("reference tier matches integrity lock (no hand-edits)", rc == 0, out.strip()[-400:])

# 10. Phase-3 dense layer is OPTIONAL: kb.py --hybrid must still return hits when the
# embedding library / vendored model / index is absent (graceful degradation, no hard dep)
rc, out = run("kb.py", "--domain", "keycloak", "search", "dpop sender constrained", "--hybrid", "--limit", "2")
check("kb.py --hybrid degrades to lexical (no model)", rc == 0 and "hit(s)" in out, out[:160])

failed = [n for n, ok, _ in checks if not ok]
print(f"\n{len(checks) - len(failed)}/{len(checks)} checks passed")
sys.exit(1 if failed else 0)
