#!/usr/bin/env python3
"""Acceptance check for the IPv4-vs-version redaction fix in wikidoc.py.

Runnable, stdlib + PyYAML only (PyYAML is wikidoc's sole dep). No framework.
Run:  python3 tools/test_wikidoc_ip.py   ->  prints "ALL PASS" and exits 0.
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wikidoc  # noqa: E402

# A compliant, routable frontmatter (type:concept => no decision-tree requirement).
FM = (
    "---\n"
    "domain: test\n"
    "title: T\n"
    "product: RHBK\n"
    "applies_to: ['26.6']\n"
    "routable: true\n"
    "type: concept\n"
    "inject: section\n"
    "authority: internal-distilled\n"
    "source_provenance:\n"
    "  - ref: RHBK Test Guide\n"
    "    visibility: public\n"
    "keywords: [a, b, c, d, e]\n"
    "last_verified: '2026-06-28'\n"
    "---\n"
)


def check(body: str):
    """Validate FM+body, return (errors, warns) Finding lists."""
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "doc.md"
        p.write_text(FM + "\n" + body + "\n", encoding="utf-8")
        f = wikidoc.validate_file(p)
    return ([x for x in f if x.level == "error"],
            [x for x in f if x.level == "warn"])


def ip_errs(errs):
    return [e for e in errs if "IPv4" in e.msg]


def ip_warns(warns):
    return [w for w in warns if w.code == "IP_OR_VERSION"]


fails = []


def expect(name, cond, detail=""):
    print(f"  {'PASS' if cond else 'FAIL'}  {name}{'' if cond else '  -> ' + detail}")
    if not cond:
        fails.append(name)


# A — version strings: 23.2.0.0.0 never flagged; 2.0.0.0 at most a warning, never error.
errs, warns = check("Bundled bc-fips is 2.0.0.0 and DriverVersion 23.2.0.0.0.")
expect("A: no errors on version strings", len(errs) == 0, str([e.msg for e in errs]))
expect("A: 23.2.0.0.0 produces no IP finding",
       not any("23.2.0.0.0" in x.msg for x in errs + warns),
       str([x.msg for x in errs + warns]))
expect("A: 2.0.0.0 is at most a warning",
       not any("2.0.0.0" in e.msg for e in errs), str([e.msg for e in errs]))

# B — private 10/8 => 1 error.
errs, _ = check("Connect to host 10.12.3.4 for the cache.")
expect("B: 10.12.3.4 -> 1 IP error", len(ip_errs(errs)) == 1, str([e.msg for e in errs]))

# C — 192.168/16, 172.16/12, loopback => error each.
errs, _ = check("Hosts 192.168.1.1 and 172.20.0.5 and 127.0.0.1 are internal.")
expect("C: three private IPs -> 3 IP errors", len(ip_errs(errs)) == 3,
       str([e.msg for e in errs]))

# D — public 8.8.8.8 => warning, not error.
errs, warns = check("Resolver is 8.8.8.8 by default.")
expect("D: 8.8.8.8 -> no error", len(ip_errs(errs)) == 0, str([e.msg for e in errs]))
expect("D: 8.8.8.8 -> warning", len(ip_warns(warns)) == 1, str([w.msg for w in warns]))

# E — compliant body (redacted ***, example.internal) still passes with 0 errors.
errs, _ = check("Set password to ***; admin at https://sso.example.internal/admin.")
expect("E: compliant body -> 0 errors", len(errs) == 0, str([e.msg for e in errs]))

# Guard: secret-assignment + JWT REDACT patterns stay ERROR (not downgraded).
errs, _ = check("password=hunter2 in the config.")
expect("guard: secret assignment stays error",
       any(e.code == "REDACT" for e in errs), str([e.msg for e in errs]))

print()
if fails:
    print(f"FAILED: {fails}")
    sys.exit(1)
print("ALL PASS")
