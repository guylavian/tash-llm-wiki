---
title: FSMO (Operations-Master) Roles
type: entity
domain: active-directory
slug: fsmo-roles
summary: The five single-master roles that sit on top of AD's otherwise multi-master replication — two forest-wide (Schema, Domain Naming) and three per-domain (RID, PDC Emulator, Infrastructure Master) — plus how to view, transfer, and seize them.
sources:
  - note:_sources/active-directory/fsmo-roles.md
  - web:https://learn.microsoft.com/windows-server/identity/ad-ds/ (Microsoft Learn — FSMO roles, fetched 2026-06-18)
provenance:
  extracted: 6
  inferred: 1
  ambiguous: 0
symptoms:
  - "RID pool.*exhaust"
  - "KRB_AP_ERR_SKEW"
  - "cannot create.*(user|computer)"
tags: [fsmo, directory-services, concept]
status: draft
updated: 2026-06-18
---

# FSMO (Operations-Master) Roles

**The five operations AD performs single-master instead of multi-master — each
held by exactly one DC at a time.**

## Body

Forest-wide (one holder per forest):
- **Schema Master** — only DC that can write schema changes.
- **Domain Naming Master** — adds/removes domains & application partitions.

Per-domain (one holder per domain):
- **RID Master** — issues RID pools so every SID is unique; exhaustion stops new
  principal creation.
- **PDC Emulator** — domain authoritative time source, preferential password/lockout
  processing, default GPO edit target, legacy PDC. The most runtime-critical role.
- **Infrastructure Master** — maintains cross-domain references; **must not** be on a
  Global Catalog in a multi-domain forest unless all DCs are GCs.

Operations: view with `netdom query fsmo` / `Get-ADForest` / `Get-ADDomain`;
**transfer** gracefully with `Move-ADDirectoryServerOperationMasterRole`; **seize**
(`-Force`) only when the holder is permanently dead — then never resurrect the old
holder (split-brain risk).

## Contradictions / caveats

Concentrating all five roles on one DC is common in small single-domain forests and
is fine operationally, but makes that DC a single point of failure for every
single-master operation (inferred — a sizing/placement judgment, not an upstream
rule).

## See also
- [[active-directory-overview]]
- [[active-directory-implementation-review]]
