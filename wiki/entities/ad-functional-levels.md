---
title: Active Directory Functional Levels
type: entity
domain: active-directory
slug: ad-functional-levels
summary: Domain and forest functional levels control which features AD DS exposes and which Windows Server versions are permitted as domain controllers; they are one-way raises that cannot be rolled back except by forest recovery.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels (Microsoft Learn — Active Directory Domain Services Functional Levels, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/raise-domain-forest-functional-levels (Microsoft Learn — Raise Domain and Forest Functional Levels in AD DS on Windows Server, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers (Microsoft Learn — Upgrade domain controllers to a newer version of Windows Server, fetched 2026-06-18)
provenance_extracted: 20
provenance_inferred: 3
provenance_ambiguous: 0
tags: [directory-services, deploy, concept]
status: draft
updated: 2026-06-18
---

# Active Directory Functional Levels

**Domain and forest functional levels determine which AD DS capabilities are available and which Windows Server releases are allowed as domain controllers — they are a one-way ratchet.**

## Domain vs forest functional level

- **Domain functional level (DFL)** — controls features within a single domain; all DCs in that domain must meet the level.
- **Forest functional level (FFL)** — controls forest-wide features; all DCs in all domains in the forest must meet the level, and the current DFL must already be at or above the target.

A DFL can be set higher than the FFL, but never lower. When all DCs in a forest run Windows Server 2025 and the FFL is raised to 2025, all DFLs are raised automatically. (inferred)

## Functional level interoperability matrix

| DC OS | WS 2025 FL | WS 2016 FL | WS 2012 R2 FL |
|---|---|---|---|
| Windows Server 2025 | Supported | Supported | Not supported |
| Windows Server 2022 | Not supported | Supported | Supported |
| Windows Server 2019 | Not supported | Supported | Supported |
| Windows Server 2016 | Not supported | Supported | Supported |
| Windows Server 2012 R2 | Not supported | Not supported | Supported |

Windows Server 2019 and 2022 do not add a new functional level — they use WS 2016 as the maximum. No new FLs have been added since WS 2016 (as of 2026).

## Feature unlocks by level

### Windows Server 2016 DFL/FFL
- **FFL**: Privileged Access Management (PAM) via Microsoft Identity Manager (MIM).
- **DFL**: Automatic rolling of NTLM/password-based secrets for PKI-required accounts; Kerberos PKInit Freshness Extension SID; per-device NTLM restriction.
- **Prerequisite**: DFSR is required for SYSVOL replication. Windows Server 2016 is the last version supporting FRS.

### Windows Server 2012 R2 DFL/FFL
- **DFL**: Protected Users group DC-side enforcement (no NTLM, no DES/RC4, no unconstrained delegation, 4-hour TGT cap); Authentication Policies; Authentication Policy Silos.

### Windows Server 2025 DFL/FFL
- **DFL**: Database 32k pages optional feature (see [[ad-database-and-32k-pages]]).

## Raising functional levels

**Prerequisites** before raising:

1. All DCs in the scope run at least the target Windows Server version.
2. For WS 2025 DFL: domain must already be at WS 2016 FL (earlier OS versions do not support WS 2025 DCs).
3. Forest and domains are replication-error-free.
4. Back up all GC/FSMO holders.

**Via PowerShell:**

```powershell
# Raise domain FL
Set-ADDomainMode -Identity <domain> -DomainMode <level>

# Raise forest FL
Set-ADForestMode -Identity <forest> -ForestMode <level>
```

**Via GUI:** Active Directory Domains and Trusts → right-click domain → Raise Domain Functional Level; then right-click the root node → Raise Forest Functional Level.

## Rollback rules

Functional level raises are **irreversible** in general — to undo one you must perform a forest recovery. The exceptions are:

- WS 2012 R2 FFL → can roll back to WS 2012 R2 (if upgrading from that baseline).
- WS 2008 R2 FFL → can roll back to WS 2008 R2.
- DFL raised to WS 2016 when FFL is WS 2012 or lower → can roll back DFL to WS 2012 or WS 2012 R2.

## Minimum FL requirements for new DC OS versions

- Windows Server 2019 or later requires forest FL ≥ WS 2008.
- Windows Server 2016 requires forest FL ≥ WS 2003.
- If the forest FL is lower than the minimum required, promotion is blocked until old DCs are removed and the FL is raised.

## Contradictions / caveats

- Functional levels do not affect member servers or workstations — only what DCs can do with each other.
- "Windows Server 2016 functional level" applies to WS 2016, 2019, and 2022 DCs alike; 2019 and 2022 do not contribute new FL features.
- Raising FFL to WS 2025 while any non-2025 DCs remain is blocked; all must be upgraded first. (inferred)

## Reference notes

- [[ad-ds-active-directory-functional-levels]]
- [[ad-ds-raise-domain-forest-functional-levels]]
- [[ad-ds-upgrade-domain-controllers]]

## See also

- [[ad-ds-deployment]]
- [[upgrade-domain-controllers]]
- [[adprep-and-schema-updates]]
- [[ad-database-and-32k-pages]]
- [[fsmo-roles]]
