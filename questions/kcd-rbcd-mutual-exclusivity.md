---
title: Are classic KCD and RBCD mutually exclusive on the same accounts?
type: question
domain: active-directory
slug: kcd-rbcd-mutual-exclusivity
summary: No — classic constrained delegation (msDS-AllowedToDelegateTo, on the front-end account) and RBCD (msDS-AllowedToActOnBehalfOfOtherIdentity, a security descriptor on the resource account) are independent attributes on different objects and can coexist. Both configured on the same accounts is a documented escalation pattern, not a benign "both work" — monitor SD writes via Event 5136.
sources:
  - kb:ad-ds-schema-updates
  - kb:ad-ds-configure-kerberos-delegation-group-managed-service-accounts
  - kb:ad-ds-appendix-l-events-to-monitor
  - kb:ad-ds-advanced-audit-policy-configuration
provenance_extracted: 6
provenance_inferred: 3
provenance_ambiguous: 0
question_tier: conceptual
tags: [ad-authn, security]
status: draft
updated: 2026-07-05
graph_community: "Group Managed Service Accounts (gMSA)"
---

# Are classic KCD and RBCD mutually exclusive on the same accounts?

**No. The two mechanisms use independent attributes on different objects — classic KCD lives on the front-end account, RBCD on the resource — so nothing prevents both being configured at once; and when both ARE present on the same accounts, treat it as an audit finding (documented attack surface), not a benign redundancy.**

## Question

> Traditional constrained delegation and resource-based constrained delegation — are
> they mutually exclusive on the same account, or can both be configured? What happens
> if both are set?

## Answer

**The two attributes are distinct and live on different objects:**

- **RBCD** is the `msDS-AllowedToActOnBehalfOfOtherIdentity` attribute — per the schema
  definition, "used for access checks to determine if a requester has permission to act
  on the behalf of other identities **to services running as this account**", i.e. it is
  stored on the **resource** (back-end) account
  (`reference/active-directory/ad-ds-schema-updates.md:4770-4772`; attribute OID
  1.2.840.113556.1.4.2182, `:4773`; single-valued, `:4776`).
- **Classic KCD** is the `msDS-AllowedToDelegateTo` attribute on the **front-end**
  service account — it "defines where the SPNs for delegation will be added"
  (`reference/active-directory/ad-ds-configure-kerberos-delegation-group-managed-service-accounts.md:25`),
  set/cleared directly on the delegating identity (`:40`, `:56`).

**Mutual exclusivity: none documented.** No note in the AD corpus marks the two as
exclusive; they are independent attributes on distinct objects, so both can be
configured simultaneously (inferred — from the attribute independence above and the
absence of any exclusivity statement corpus-wide) (inferred).

**Behavior when both are set:** the KDC evaluates them on different sides of the
S4U2Proxy exchange — the front-end's `msDS-AllowedToDelegateTo` list in the classic
path, the resource's `msDS-AllowedToActOnBehalfOfOtherIdentity` security descriptor in
the RBCD path, where the RBCD access check replaces the forwardable-ticket check
(inferred — MS-SFU-based KDC decision flow as detailed in
[[kerberos-rbcd-s4u-delegation-detailed]] §2, which tags its own MS-SFU claims
(inferred)) (inferred).

## The caveat this question is really about

Both mechanisms configured/misconfigurable on the same accounts is a **documented AD
attack pattern**, not a curiosity: RBCD requires only `WriteProperty` on the resource's
`msDS-AllowedToActOnBehalfOfOtherIdentity` — a right that can be held by a
resource-side admin rather than a domain admin — making an SD write the escalation
primitive (see the "RBCD as attack vector" analysis in
[[kerberos-rbcd-s4u-delegation-detailed]] §3). Operational monitoring is corpus-backed:

- **Event 5136 — "A directory service object was modified"** is the
  directory-service-changes event to watch for writes to that SD
  (`reference/active-directory/ad-ds-appendix-l-events-to-monitor.md:340`;
  same event in the audit-policy reference,
  `reference/active-directory/ad-ds-advanced-audit-policy-configuration.md:491`).
- Recommended practice (inferred): alert on 5136 events whose modified attribute is
  `msDS-AllowedToActOnBehalfOfOtherIdentity`, and periodically review any account that
  carries BOTH delegation attributes (inferred).

## Contradictions / caveats

- The "what happens when both are set" precedence flow rests on MS-SFU protocol
  documentation as synthesized in [[kerberos-rbcd-s4u-delegation-detailed]] — the RHBK
  corpus itself does not narrate the dual-configuration case; hence the (inferred) tags.
  Verify against MS-SFU §3.2.5.2 before relying on precedence details in an incident.

## See also

- [[kerberos-rbcd-s4u-delegation-detailed]]
- [[active-directory-implementation-review]]

## References

**Ground-truth corpus (`kb:`)**
- kb:ad-ds-schema-updates — Windows Server AD DS schema updates (msDS-AllowedToActOnBehalfOfOtherIdentity definition; lines 4770-4776)
- kb:ad-ds-configure-kerberos-delegation-group-managed-service-accounts — Configure Kerberos delegation for gMSA (msDS-AllowedToDelegateTo; lines 25, 40, 56)
- kb:ad-ds-appendix-l-events-to-monitor — Appendix L: Events to Monitor (5136; line 340)
- kb:ad-ds-advanced-audit-policy-configuration — Advanced Audit Policy Configuration (5136; line 491)

**Wiki + upstream**
- [[kerberos-rbcd-s4u-delegation-detailed]] — the KDC decision flow (§2) and RBCD-as-attack-vector analysis (§3) this page builds on.

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-schema-updates|Schema updates in Windows Server]]
- [[ad-ds-configure-kerberos-delegation-group-managed-service-accounts|Configuring Kerberos Delegation for Group Managed Service Accounts]]
- [[ad-ds-appendix-l-events-to-monitor|Appendix L]]
- [[ad-ds-advanced-audit-policy-configuration|Advanced Audit Policy Configuration settings]]
<!-- crosslink:end -->
