---
title: KB5014754 strong certificate mapping — RHBK OIDC claim mapping failure
type: question
domain: keycloak
slug: kb5014754-adfs-rhbk-claim-mapping
summary: "KB-grounded analysis of intermittent claim mapping failure after KB5014754 enforcement when RHBK does OIDC federation against AD FS. The KB cannot determine the root cause because KB5014754 and strong certificate mapping are absent from the corpus and AD FS is out of scope — but the closest analogous pattern is the mutable-AD-attribute link-loss documented in kb:7128299."
sources:
  - kb:7128299
  - ref:rhbk-26-4-newfeatures.md
  - ref:rhbk-26-4-migration-changes.md
  - ref:rhbk-26-6-migration-changes.md
  - ref:rhsso-7-4-identity-broker.md
  - ref:rhbk-26-4-assembly-managing-clients-server-administration-guide.md
  - ref:_meta/wikikb/tkg/versions.py
provenance:
  extracted: 2
  inferred: 4
  ambiguous: 1
status: draft
updated: 2026-07-07
---

# KB5014754 strong certificate mapping — RHBK OIDC claim mapping failure

**The KB cannot determine a definitive root cause for this scenario.** KB5014754 (Strong Certificate Mapping enforcement) is absent from the corpus (`wiki/reference/keycloak/`, `wiki/reference/active-directory/`); AD FS is explicitly out-of-scope for this wiki (`[[windows-server-identity-coverage-gaps]]:69-71`); no wiki page covers the interaction between DC-side strong certificate mapping enforcement and RHBK OIDC identity brokering. The three questions are answered below with what the KB does and does not contain.

## 1. Root cause (KB-grounded)

The KB's closest analogous pattern is `[[ad-idp-link-loss-objectguid]]` / `kb:7128299` (Intermittent Loss of Active Directory Identity Provider Link in RHBK): a federated link fails when the attribute used as the unique identifier in the Identity Provider mapper is mutable and changes between logins. The `doc-7128299:34-39` root cause is that RHBK's Username Template Importer mapper uses a mutable AD attribute (sAMAccountName, userPrincipalName, cn); when AD changes it, the incoming identifier no longer matches the stored federated link.

The KB does NOT confirm whether KB5014754 triggers this same mechanism. The inference is: KB5014754 enforcement changes how the KDC maps certificates to AD user objects (from weak Subject+Issuer to strong SAN/altSecurityIdentities matching). If this changes the claims AD FS emits to RHBK (e.g. the `sub` or email claim now reflects the strong-mapped identifier), the same link-mismatch pattern would apply. But this is `(inferred)` — absent from the KB corpus, and the AD FS behavior post-KB5014754 is not in scope.

## 2. tkg facts relevant to this RHBK version vs later versions

From `versions.py:41-60` (tkg), the RHBK release timeline:

| Version | Date (errata-confirmed) |
|---------|------------------------|
| 26.0    | 2024-11-21 |
| 26.2    | 2025-06-09 |
| 26.4    | 2025-11-13 |
| 26.6    | 2026-06-03 |

KB5014754 enforcement was phased (Phase 2: early 2024, Phase 3: rolling 2024–2025). The tkg has NO AD FS or certificate-mapping temporal facts, so it provides only a date-anchor: RHBK 26.0 was released during active KB5014754 enforcement, while 26.4+ was released well after. No RHBK release note in the KB claims to have addressed post-KB5014754 AD FS claim mapping changes.

Two version-specific changes in the KB reference notes are relevant to the general brokering area: RHBK 26.4 introduced a generic OAuth 2.0 broker (`rhbk-26-4-newfeatures.md:63`) and stricter SAML SubjectConfirmationData validation (`rhbk-26-4-migration-changes.md:92-93`); 26.6 continued SAML broker validation hardening (`rhbk-26-6-migration-changes.md:45-46`). These changes affect SAML brokering, not AD FS OIDC federation specifically — `(ambiguous)` whether OIDC broker claim handling changed between versions.

## 3. Stale facts that must not leak

Three fact clusters in the KB look related but are NOT applicable to this scenario:

1. **`[[ad-idp-link-loss-objectguid]]` (kb:7128299) — mutable AD attribute link loss.** This is about an AD *admin* changing sAMAccountName/UPN, breaking the federated link. It is NOT about certificate mapping enforcement. Only the mechanism (IdP mapper keyed on a changing identifier) is directionally analogous — do NOT state that this IS the root cause for KB5014754.

2. **X.509 authenticator identity mapping** (`rhbk-26-0-configuring-authentication-server-administration-guide.md:673-754` and equivalents in 26.2/26.4). These docs describe RHBK's built-in X.509 client certificate authenticator — mapping SubjectDN/SAN to username/email/custom attribute within RHBK's own authentication flow. NOT about AD FS OIDC federation claims.

3. **CERT_SUBJECT SAML key name** (`rhbk-26-4-assembly-managing-clients-server-administration-guide.md:744`). The KB states that `CERT_SUBJECT` key name format is "expected by Microsoft Active Directory Federation Services" — but this is about SAML key name format when RHBK acts as a SAML IdP, NOT about OIDC claim mapping with AD FS as the IdP. Do not cite this as relevant to OIDC claim mapping post-KB5014754.

## References

**RH ground-truth:**
- `kb:7128299` — Intermittent Loss of Active Directory Identity Provider Link in RHBK (closest analogous pattern)
- `ref:rhbk-26-4-newfeatures.md` — OAuth 2.0 generic broker (26.4 feature)
- `ref:rhbk-26-4-migration-changes.md` — SAML SubjectConfirmationData validation
- `ref:rhbk-26-6-migration-changes.md` — SAML broker validation hardening
- `ref:rhsso-7-4-identity-broker.md` — Protocol-based identity providers (SAML v2.0 and OIDC v1.0)
- `ref:rhbk-26-4-assembly-managing-clients-server-administration-guide.md` — CERT_SUBJECT key name "expected by Microsoft Active Directory Federation Services"
- `ref:_meta/wikikb/tkg/versions.py` — RHBK version release dates (tkg)

**Wiki:**
- `[[ad-idp-link-loss-objectguid]]` — AD federated link loss due to mutable attribute (stale — not directly applicable)
- `[[identity-brokering]]` — RHBK identity brokering overview
- `[[windows-server-identity-coverage-gaps]]` — Documents AD FS as out of scope

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[doc-7128299|Intermittent Loss of Active Directory Identity Provider Link in RHBK]]
<!-- crosslink:end -->
