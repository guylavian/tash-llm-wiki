---
title: Active Directory Trusts
type: topic
domain: active-directory
slug: ad-trusts
summary: How AD DS trusts (forest, external, realm) authenticate across domain/forest boundaries, the prerequisites merge-vs-trust decisions depend on, and field reports where Kerberos over a trust breaks down to NTLM (or fails outright) with no confirmed fix in the community corpus.
sources:
  - "web:https://learn.microsoft.com/en-us/answers/questions/1126926/kerberos-authentication-with-one-way-forest-trust (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/122265/kerberos-realm-trust-extra-settings (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1401941/after-active-directory-cross-forest-trust-member-s (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1476166/active-directory-external-one-way-trust-permission (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1185287/different-active-directory-trusts-and-the-prerequi (Microsoft Q&A, fetched 2026-07-25)"
provenance_extracted: 5
provenance_inferred: 1
provenance_ambiguous: 2
tags: [trusts, directory-services, troubleshooting]
status: draft
updated: 2026-07-25
---

# Active Directory Trusts

**An AD DS trust lets security principals in one domain/forest authenticate to
resources in another; the community field reports in this corpus skew toward
one-way and cross-forest configurations where Kerberos degrades to NTLM (or
fails) and where the *prerequisites* for the trust — not the trust wizard
itself — turn out to be the actual blocker.**

## Community Q&A (upstream)

> Microsoft Q&A threads, not Microsoft support statements. Several of the
> threads in this cluster reflect narrower, less-answered questions than other
> AD topics — two below received zero community answers and are included as
> documented, unresolved field reports rather than confirmed fixes.

### One-way forest trust: Kerberos fails, falls back to NTLM, then also fails

A one-way trust (`prod.local` trusted, `dev.local` trusting) configured with
forest-wide authentication produced `KDC_ERR_S_PRINCIPAL_UNKNOWN` (web:1126926)
on Kerberos and a total NTLM fallback failure for a service account doing DCOM
against a CA in the trusting domain — the same setup worked immediately once
switched to a two-way trust. A Microsoft-vendor-affiliated answer suggested switching to
**Selective Authentication** and explicitly granting "Allowed to Authenticate"
to the service account on the target resource, but the thread has no further
reply confirming this resolved it (web:1126926) **(ambiguous)** — treat as an
untested hypothesis, not a confirmed fix, when a one-way trust's Kerberos path
won't come up.

### Kerberos Realm Trust to a non-Windows realm: DNS and ports first

Setting up a Kerberos Realm Trust to a non-Windows KDC (e.g. MIT Kerberos) via
`netdom trust /add /realm` requires, per a Microsoft-vendor-affiliated answer:
(1) a secondary DNS zone or conditional forwarder so each realm can resolve the
other's DCs, (2) the standard [[dns-for-ad-ds]]-adjacent AD trust port set
(documented under "Active Directory and Active Directory Domain Services Port
Requirements") open between them, and only then — if needed — `ksetup`/`ktpass`
to align specific Kerberos authentication-type support between the two realms;
`kadmin`/`kadmin.local` are non-Windows-side tools, not part of the Windows
configuration (web:122265).

### Merge vs. trust — and what lost forest-admin credentials block

For a company with two legacy domains (`A.com`, `B.com`) wanting either to merge
or to trust bidirectionally, a Microsoft Moderator's answer frames the decision:
migration is generally preferred where feasible (fewer DCs, less privileged
surface to maintain long-term), with a trust relationship as the lower-effort
interim option, and recommends **enabling SID history** plus a migration tool
(ADMT, or a third-party tool such as Quest Migration Manager) to preserve
existing logins during a merge. Critically: because `A.com` had lost its forest
admin/recovery credentials (only a sub-domain's admin credentials survived),
the answer confirms this **does** block a successful trust/migration setup —
establishing a domain trust requires credentials in the enterprise/domain admin
group of the *root* domain, so recovering (or rebuilding) that root-domain
administrative access is a hard prerequisite before either path can proceed
(web:1185287).

### Cross-forest trust and external one-way trust: unresolved field reports

Two threads in this cluster report concrete symptoms with **no community
answer at all** in the corpus — worth recording as documented gaps rather than
silently dropping:
- A member server joined to a domain with a cross-forest trust in place throws
  an unspecified error adding a cross-forest resource; no diagnosis was ever
  posted (web:1401941).
- Across an external one-way trust, a user from the trusted domain (who has
  local-admin rights on a resource server in the trusting domain via a
  transitive group membership) gets an authentication prompt and then
  "Username or Password is incorrect" when trying to add a *different*
  trusting-domain group to the local Administrators group via `netplwiz` — and
  a firewall trace shows the client attempting Kerberos/LDAP (ports 88/389)
  against the **trusted** domain's DCs rather than the trusting domain's,
  suggesting the client resolved the wrong domain for that particular
  operation. No answer was posted confirming whether this is a design
  limitation of external trusts or a client-side misconfiguration
  (web:1476166) **(ambiguous)**.

## Contradictions / caveats

- Both unresolved threads (web:1401941, web:1476166) are reported here as
  observed symptoms only — do not treat either as a confirmed AD DS behavior;
  they are corpus gaps, and the "likely cause" for the external-trust
  credential prompt is a reasonable but unverified inference from the reported
  firewall trace, not a documented mechanism (inferred).
- The Selective-Authentication fix for one-way-trust Kerberos failure
  (web:1126926) is the standard documented remedy for this class of problem in
  general AD guidance, but this specific thread never confirms it worked —
  flag it as unconfirmed when citing it for a break-fix answer.

## See also
- [[ad-logical-structure-design]]
- [[forest-design-models]]
- [[domain-design]]
- [[dns-for-ad-ds]]
- [[active-directory-implementation-review]]
- [[security-identifiers-sid]]
