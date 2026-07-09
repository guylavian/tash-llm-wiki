#!/usr/bin/env python3
"""fabrication_probe.py — verify the ANSWER-TIME fabricated-citation check. stdlib only.

WHY: the zero-citation withhold (`graph/nodes.py::synthesize_node`, `grounding_fail`) only catches
a model that cites NONE of the retrieved sources. The still-open PRODUCTION_READINESS sign-off
blocker (PLAN-graphify-pdf-upload.md Phase 3 item 2) is the OPEN class it misses: the model cites a
REAL retrieved source but asserts a distinctive identifier (ENV/CONST, GUID, invented flag) that
appears in NONE of the retrieved context — the `SSO_HTTPS_CIPHER_SUITES` fabrication, at answer
time. `lint.ungrounded_against_context` is the deterministic check that closes it; this probe
exercises that function directly (FAITHFUL: same import gate_page_probe.py/gate_probe.py use).

Tests CHECK BEHAVIOUR (does the function flag/not-flag a given answer+context+query), not answer
correctness — O(1) per case, no LLM, no network. The negative cases (identifier present in context;
identifier only in the query; a cipher-suite-like constant) are the calibration proof — a probe with
only positive cases only shows over-eager firing, not correctness.

Exit: 0 all pass · 1 a case failed (CI gate).

Usage:
    python3 wiki/_meta/tests/fabrication_probe.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))      # _meta/tests
META = os.path.dirname(HERE)                            # _meta
sys.dont_write_bytecode = True
sys.path.insert(0, META)                               # test bootstrap: make `import wikikb` importable
from wikikb.quality import lint  # faithful: reuse the real extraction/exclusion machinery


def probe_fabricated_identifier_flagged():
    """An answer asserts an ENV/CONST identifier that appears in neither the retrieved context nor
    the query -> flagged, non-empty list, exact token returned."""
    answer = "Set SSO_HTTPS_CIPHER_SUITES to restrict the allowed TLS ciphers."
    context = "[kb:1] The server supports configuring HTTPS via standard Keycloak options."
    query = "how do I restrict TLS ciphers"
    got = lint.ungrounded_against_context(answer, context, query)
    ok = got == ["SSO_HTTPS_CIPHER_SUITES"]
    return ok, ["got=%r" % got]


def probe_identifier_in_context_not_flagged():
    """The SAME identifier, but this time it genuinely appears in the retrieved context -> NOT
    flagged (case-insensitive match)."""
    answer = "Set SSO_HTTPS_CIPHER_SUITES to restrict the allowed TLS ciphers."
    context = "[kb:1] The sso_https_cipher_suites option restricts the allowed TLS cipher suites."
    query = "how do I restrict TLS ciphers"
    got = lint.ungrounded_against_context(answer, context, query)
    ok = got == []
    return ok, ["got=%r" % got]


def probe_identifier_only_in_query_not_flagged():
    """An identifier that appears ONLY in the user's own question (they asked about it by name) is
    not a fabrication — the model is reflecting the question, not inventing a fact."""
    answer = "KC_FEATURE_TOKEN_EXCHANGE is not documented anywhere in this corpus."
    context = "[kb:1] The corpus discusses several KC_ prefixed environment variables."
    query = "does KC_FEATURE_TOKEN_EXCHANGE exist?"
    got = lint.ungrounded_against_context(answer, context, query)
    ok = got == []
    return ok, ["got=%r" % got]


def probe_cipher_constant_excluded():
    """A cipher-suite-shaped constant (domain vocab that varies in punctuation, per
    lint._is_distinctive_artifact) is excluded even when it appears nowhere in context/query —
    the same exclusion `ungrounded_citations` (page-level) already applies."""
    answer = "The negotiated suite was TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384."
    context = "[kb:1] TLS configuration is handled by the standard HTTPS options."
    query = "what cipher suite got negotiated"
    got = lint.ungrounded_against_context(answer, context, query)
    ok = got == []
    return ok, ["got=%r" % got]


def probe_clean_answer_no_false_positive():
    """A normal answer with no distinctive ENV/CONST-shaped claims at all -> [] (no false
    positives on ordinary prose)."""
    answer = "LDAP user federation syncs users from the directory into Keycloak's local store."
    context = "[kb:1] LDAP federation providers synchronize users on a configurable schedule."
    query = "how does ldap user federation work"
    got = lint.ungrounded_against_context(answer, context, query)
    ok = got == []
    return ok, ["got=%r" % got]


def main():
    probes = [
        ("fabricated identifier absent from context+query -> flagged", probe_fabricated_identifier_flagged),
        ("same identifier present in context -> NOT flagged", probe_identifier_in_context_not_flagged),
        ("identifier only in the query -> NOT flagged", probe_identifier_only_in_query_not_flagged),
        ("cipher-suite-shaped constant -> excluded", probe_cipher_constant_excluded),
        ("ordinary answer with no distinctive claims -> no false positive", probe_clean_answer_no_false_positive),
    ]
    print("=" * 82)
    print("FABRICATION PROBE — answer-time anti-fabrication check (lint.ungrounded_against_context)")
    print("=" * 82)
    fails = 0
    for name, fn in probes:
        try:
            ok, reasons = fn()
        except Exception as e:                          # noqa: BLE001 — a probe crash is still a FAIL
            ok, reasons = False, ["raised %r" % e]
        if not ok:
            fails += 1
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
        for r in reasons:
            print("          %s" % r)
    print("-" * 82)
    print("%d/%d passed%s" % (len(probes) - fails, len(probes), "" if not fails else "  — FAILURES ABOVE"))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
