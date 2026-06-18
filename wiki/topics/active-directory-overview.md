---
title: Active Directory — Domain Services Overview
type: topic
domain: active-directory
slug: active-directory-overview
summary: The orientation page for the active-directory brain — what AD DS is (forest/domain/OU hierarchy, multi-master replication, the single-master FSMO roles, DNS/Kerberos dependencies) and the spine other AD pages hang off.
sources:
  - note:_sources/active-directory/fsmo-roles.md
  - web:https://learn.microsoft.com/windows-server/identity/ad-ds/ (Microsoft Learn — AD DS, fetched 2026-06-18)
provenance:
  extracted: 4
  inferred: 2
  ambiguous: 0
tags: [directory-services, concept]
status: draft
updated: 2026-06-18
---

# Active Directory — Domain Services Overview

**The seed/orientation topic for the `active-directory` domain: AD DS is
Microsoft's directory service — a hierarchical, multi-master-replicated store of
users, computers, and policy, hard-wired to DNS for locating services and to
Kerberos/NTLM for authentication.**

## Body

Active Directory Domain Services (AD DS) organizes objects into a hierarchy:

- **Forest** — the top security/replication boundary; shares one schema and global
  catalog.
- **Domain** — a partition of the forest with its own security policy and
  replication scope.
- **Organizational Unit (OU)** — the unit that [[group-policy]] and delegation
  attach to.

Replication between domain controllers (DCs) is **multi-master** — any DC can
accept a write and converge it to the rest. The exceptions are the five
**single-master** operations governed by the [[fsmo-roles]] (Schema, Domain Naming,
RID, PDC Emulator, Infrastructure Master). Most "AD is broken" tickets trace back
to one of three dependencies: a missing FSMO holder, broken **DNS** (DCs are
located via `_msdcs` SRV records), or **time skew** breaking Kerberos (inferred —
this is the recurring root-cause pattern across the failure modes below).

This page is intentionally a spine. Detailed mechanics live on entity pages and the
review MOC; grow them via INGEST as notes land in `_sources/active-directory/`.

## Contradictions / caveats

This is a notes-first domain seeded from Microsoft Learn — facts are paraphrased
from the upstream docs and lab knowledge, not a Red Hat-style support corpus.
Version-specific behavior (Windows Server 2016/2019/2022/2025 functional levels)
should be called out per claim as pages mature.

## See also
- [[fsmo-roles]]
- [[active-directory-implementation-review]]
