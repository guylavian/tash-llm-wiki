"""coverage.py — tiers-covered parsing + the H1 (out-of-coverage) rule. stdlib only, no network.

The LIBRARY half of the former gate_probe.py: `load_tiers_covered()` reads each domain's
`tiers-covered:` from taxonomy.md, and `gate_verdict()` is the H1 coverage rule. These live in the
package so the LangGraph gate node (wikikb.graph.nodes) and the CI probe (tests/gate_probe.py) import
the SAME code — the faithfulness invariant. lint.gate_banner inlines the identical one-line H1 check.
"""
import re

from wikikb import paths


def load_tiers_covered(path=None):
    """domain -> [covered tiers], from `### <domain>` blocks + `- tiers-covered: [...]` in taxonomy.md.
    Skips the <!-- template --> comment so its placeholder block stays inert."""
    path = str(path or paths.TAXONOMY)
    tiers, cur, in_comment = {}, None, False
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if in_comment:
                if "-->" in line:
                    in_comment = False
                continue
            if "<!--" in line:
                in_comment = "-->" not in line
                continue
            if line.startswith("## "):           # left the ## Domains section
                cur = None
            h = re.match(r"^###\s+([a-z][a-z0-9-]+)\s*$", line)
            if h:
                cur = h.group(1)
                continue
            m = re.match(r"^\s*-\s*tiers-covered:\s*\[(.*?)\]", line)
            if m and cur:
                tiers[cur] = [t.strip() for t in m.group(1).split(",") if t.strip()]
    return tiers


def gate_verdict(question_tier, covered):
    """The gate's tier-arm, deterministic: fire iff the question's tier isn't covered."""
    return "out-of-coverage" if question_tier not in covered else "none"
