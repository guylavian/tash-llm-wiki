---
title: Active Directory Certificate Services (AD CS)
type: topic
domain: active-directory
slug: ad-certificate-services
summary: The Windows Server PKI role — what a CA does, the enterprise/standalone and root/subordinate axes, private-key protection (HSM, offline root), template-driven issuance, off-network enrollment (CEP/CES), and how Windows decides trust via CTLs.
sources:
  - note:_sources/active-directory/ad-certificate-services.md
  - web:https://learn.microsoft.com/windows-server/identity/ad-cs/ (Microsoft Learn — AD CS, fetched 2026-06-18)
provenance_extracted: 8
provenance_inferred: 2
provenance_ambiguous: 0
tags: [ad-certificate-services, security, concept]
status: draft
updated: 2026-06-18
---

# Active Directory Certificate Services (AD CS)

**The Windows Server PKI role: a certification authority (CA) that issues, renews,
and revokes the certificates underpinning LDAPS, smartcard sign-in, code/document
signing, and federation token certs.**

## Body

A CA vouches for an identity by issuing a digitally signed certificate and then
manages its lifecycle. AD CS CAs are classified on two independent axes — see
[[certification-authority-types]]:

- **Enterprise vs Standalone** — Enterprise CAs are AD-integrated, use
  [[certificate-templates]], support **autoenrollment** and **smartcard sign-in**,
  and publish certs/CRLs to AD; Standalone CAs have no AD dependency, no templates,
  and queue requests for manual approval (the right choice for an **offline root**).
- **Root vs Subordinate** — a self-signed root anchors trust and should be kept
  **offline**; subordinate (intermediate/policy and issuing) CAs do the day-to-day
  issuing.

**Key protection is the crux of CA security.** The CA's private key is its identity;
compromise of a root CA compromises the whole hierarchy. Protect keys with an
**HSM** (CryptoAPI/CSP device; one network HSM can serve multiple CAs) and keep
roots disconnected and physically secured. Issuing CAs must keep their key online to
sign (inferred trade-off: availability vs exposure, mitigated by the offline-root +
online-issuer split).

**Issuance is template-driven on Enterprise CAs.** Templates live in AD DS so the
whole forest shares one consistent policy — see [[certificate-templates]]. For
machines off the corporate network or not domain-joined, the **Certificate
Enrollment Policy Web Service (CEP)** + **Certificate Enrollment Web Service (CES)**
provide HTTPS/WS-Trust policy retrieval and **key-based renewal** (an existing valid
cert authenticates its own renewal). Both web services need a Server-Authentication
SSL cert and disallow anonymous auth.

**Windows decides whether to trust a chain** using **certificate trust lists (CTLs)**
from the Microsoft Root Certificate Program, refreshed daily by the **CTL Updater**
from Windows Update. In disconnected environments, redirect the updater to an
internal share and curate roots via `certutil -syncWithWU` / `-generateSSTFromWU` +
Group Policy rather than disabling auto-update.

**Higher assurance:** **TPM key attestation** lets the CA verify the requested key is
bound to a trusted TPM (RSA keys only; Enterprise CA only) — configured on the
template.

## Contradictions / caveats

- Smartcard sign-in and autoenrollment are **Enterprise-CA-only** features (they need
  AD integration + templates); a Standalone CA cannot provide them.
- AD CS is the PKI that issues the certs other identity components consume (LDAPS for
  [[dns-for-ad-ds]]/directory traffic, machine/user auth) — it is foundational
  infrastructure, distinct from but adjacent to the directory itself.

## See also
- [[certification-authority-types]]
- [[certificate-templates]]
- [[securing-active-directory]]
- [[active-directory-overview]]
