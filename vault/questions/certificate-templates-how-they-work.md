---
origin: eval-cohort
title: What are certificate templates and how do they work?
type: question
domain: active-directory
slug: certificate-templates-how-they-work
summary: Certificate templates are the rules/settings an Enterprise CA applies to incoming certificate requests — stored in AD DS for forest-wide consistency, only usable by Enterprise CAs, and the enforcement point for TPM key attestation.
sources:
  - note:_sources/active-directory/ad-certificate-services.md
  - web:https://learn.microsoft.com/windows-server/identity/ad-cs/ (Microsoft Learn — Certificate templates concepts, fetched 2026-06-18)
  - kb:ad-ds-tpm-key-attestation
provenance:
  extracted: 8
  inferred: 1
  ambiguous: 0
question_tier: conceptual
status: draft
updated: 2026-07-25
graph_community: "Active Directory — Domain Services Overview"
---

# What are certificate templates and how do they work?

**Certificate templates are predefined sets of rules and settings that an Enterprise CA applies to incoming certificate requests — they preconfigure a certificate for a specific task and tell the client how to build a valid request.**

## Body

### What they are

A certificate template is a policy object that defines the properties of a certificate the CA can issue — key sizes, cryptographic algorithms, intended purposes (Extended Key Usage), validity period, issuance requirements, and which security principals are authorized to enroll. Rather than crafting every certificate manually, an admin defines a template once and clients request certificates against it.

- **Only an Enterprise CA can issue from a template** — Standalone CAs have no templates, so the request itself must carry all certificate details. ([[certificate-templates]]:27-28)
- Templates are stored in **AD DS**, so every CA in the forest sees the current standard template — this keeps certificate policy consistent forest-wide. ([[certificate-templates]]:29-30)
- They are managed with the **Certificate Templates snap-in** (certtmpl.msc): copy an existing template, modify its settings, and control which users/computers can **read** the template and **enroll** for it via the read/enroll ACL. Managing templates needs **Domain Admins** (or equivalent). ([[ad-certificate-services]]:46-50; [[certificate-templates]]:31-34)

### How they work — the issuance flow

1. **Admin defines a template** — copies a built-in template (e.g. "Domain Controller", "Web Server", "User") and customizes the settings.
2. **Template published to AD** — the template object is written into the AD configuration partition under `CN=Certificate Templates,CN=Public Key Services,CN=Services,CN=Configuration`.
3. **Template assigned to a CA** — the CA's configuration lists which templates it is authorized to issue. Only published+assigned templates appear to requesting clients.
4. **Client enrolls** — the client reads the template via the Certificate Services policy module, builds a PKCS#10 request matching the template's requirements, submits it, and the CA validates the request against the template rules before issuing.
5. **Autoenrollment** — via Group Policy, domain-joined machines and users automatically enroll for certificates whose templates have the "Autoenroll" permission enabled, without user interaction. ([[ad-certificate-services]]:31-34)

### Key settings templates control

- **Key size and algorithm** — e.g. RSA 2048-bit, ECDSA P-256
- **Extended Key Usage (EKU)** — what the cert can do: Server Authentication, Client Authentication, Code Signing, Smart Card Logon
- **Validity period** — how long the certificate is valid (may differ from the CA's own cert lifetime)
- **Enrollment permissions** — which users/groups can Read, Enroll, and Autoenroll
- **Subject name construction** — built from AD attributes (CN=user principal name, or a custom build pattern)
- **Issuance requirements** — CA certificate manager approval, number of authorized signatures, re-enrollment with same key
- **Key archival** — whether the private key is escrowed by the CA
- **TPM key attestation** — require (or prefer) that the private key be bound to a Trusted Platform Module, preventing key export (RSA keys only, Enterprise-CA-only, not for third-party smartcard KSPs). ([[ad-certificate-services]]:60-62; `_sources/active-directory/ad-certificate-services.md:79-83`)

### Why templates matter for security

Because the read/enroll permissions on a template directly authorize who can obtain that certificate type, templates are a sensitive object class worth auditing alongside other privileged AD delegations. An overly permissive template (e.g. "Domain Controller" template made enrollable by all workstations) could allow unauthorized cert requests that enable lateral movement or privilege escalation. ([[certificate-templates]]:39-42, *inferred* — consistent with least-privilege guidance in [[securing-active-directory]])

## See also
- [[certificate-templates]] — the entity page
- [[ad-certificate-services]] — the AD CS role overview
- [[certification-authority-types]] — Enterprise vs Standalone, Root vs Subordinate
- [[securing-active-directory]] — least-privilege guidance

## References

### RH ground-truth (kb: / note:)
- `note:_sources/active-directory/ad-certificate-services.md` — raw source note (AD CS distilled from Microsoft Learn)

### Wiki
- [[certificate-templates]] — `entities/certificate-templates.md`
- [[ad-certificate-services]] — `topics/ad-certificate-services.md`
- [[certification-authority-types]] — `entities/certification-authority-types.md`
- **web:** Microsoft Learn — Certificate templates concepts (fetched 2026-06-18)

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-tpm-key-attestation|TPM Key Attestation]]
<!-- crosslink:end -->
