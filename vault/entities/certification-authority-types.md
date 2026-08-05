---
title: CA types — Enterprise/Standalone × Root/Subordinate
type: entity
domain: active-directory
slug: certification-authority-types
summary: The two independent axes that classify an AD CS certification authority — Enterprise (AD-integrated, templates, autoenrollment) vs Standalone (no AD, manual approval), and Root (self-signed trust anchor, keep offline) vs Subordinate (intermediate/policy and issuing).
sources:
  - note:_sources/active-directory/ad-certificate-services.md
  - web:https://learn.microsoft.com/windows-server/identity/ad-cs/ (Microsoft Learn — What is the Certification Authority Role Service?, fetched 2026-06-18)
provenance_extracted: 7
provenance_inferred: 0
provenance_ambiguous: 0
tags: [ad-certificate-services, concept]
status: draft
updated: 2026-06-18
graph_community: "Active Directory — Domain Services Overview"
---

# CA types — Enterprise/Standalone × Root/Subordinate

**An AD CS CA is classified on two independent axes: its relationship to AD
(Enterprise vs Standalone) and its position in the hierarchy (Root vs Subordinate).**

## Body

**Axis 1 — Enterprise vs Standalone**

| | Enterprise CA | Standalone CA |
|---|---|---|
| AD DS dependency | Integrated; publishes certs + CRLs to AD | None |
| Templates | Uses [[certificate-templates]] | No templates — request carries all info |
| Approval | Can auto-approve from AD identity | Requests queue for manual approval by default |
| Autoenrollment | Yes | No |
| Smartcard sign-in | Yes (maps certs to AD accounts) | No |
| Typical use | Online issuing CA in an AD forest | Offline root, or no-AD / non-Microsoft directory |

**Axis 2 — Root vs Subordinate**

- **Root CA** — top of the hierarchy; **self-signed** (Subject = Issuer); trusted
  unconditionally once its cert is on clients. Compromise cascades to every cert
  below it, so keep it an **Offline Root CA** (disconnected, physically secured).
- **Subordinate CA** — receives its cert from a parent. An **intermediate / policy
  CA** separates certificate classes (assurance level, geography) and may be
  offline; **issuing CAs** at the bottom serve end entities and must stay online.

The two axes combine: the four installable kinds are Enterprise Root, Enterprise
Subordinate, Standalone Root, and Standalone Subordinate. A common secure topology is
a **Standalone offline root** over **Enterprise online issuing** CAs.

## See also
- [[ad-certificate-services]]
- [[certificate-templates]]
