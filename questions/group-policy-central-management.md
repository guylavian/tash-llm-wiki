---
origin: eval-cohort
title: How does Group Policy centrally manage computer and user settings in Active Directory?
type: question
domain: active-directory
slug: group-policy-central-management
summary: Group Policy centralizes management through Group Policy Objects (GPOs)—a container in AD (domain partition) + a template in SYSVOL—linked to sites, domains, or OUs, with client-side extensions applying Computer Configuration at startup and User Configuration at sign-in, processed in LSDOU order.
sources:
  - kb:ad-ds-group-policy-overview
  - kb:ad-ds-group-policy-processing
  - kb:ad-ds-group-policy-scope
provenance_extracted: 8
provenance_inferred: 1
provenance_ambiguous: 0
tags: [group-policy, directory-services, concept]
question_tier: conceptual
status: draft
updated: 2026-07-12
graph_community: "Active Directory — Domain Services Overview"
---

# How does Group Policy centrally manage computer and user settings in Active Directory?

**Group Policy is Active Directory's mechanism for defining and enforcing configurations across computers and users through Group Policy Objects (GPOs) linked into the AD hierarchy, applied by client-side extensions at startup and sign-in.**

## The GPO: two physical halves

A GPO has two components that must stay synchronized:

- **Group Policy container (GPC)** — stored in the **domain partition of Active Directory** and replicated via AD replication (`ad-ds-group-policy-overview.md:21-24`). Contains version info, status, and the list of settings classes (extracted).
- **Group Policy template (GPT)** — files in the **SYSVOL** share on every domain controller, replicated via FRS (legacy) or DFSR (`ad-ds-group-policy-overview.md:21-24`). Contains the actual policy data: registry.pol, security templates, scripts, etc. (extracted).

These two halves can desync if SYSVOL replication is unhealthy — a GPO visible in AD may not apply because its template hasn't reached the DC (`topics/group-policy.md:52-54`) (extracted).

## Computer vs User configuration

Settings are split into two categories (`ad-ds-group-policy-overview.md:26-27`):

- **Computer Configuration** — system-wide settings (firewall rules, power management, security policies). Applied at **computer startup** (extracted).
- **User Configuration** — per-user settings (folder redirection, Internet Explorer, desktop preferences). Applied at **user sign-in** (extracted).

## Scope: linking to the AD hierarchy

You establish a GPO's scope by **linking** it to an Active Directory container object (`ad-ds-group-policy-scope.md:17`). Four levels in precedence order (lowest to highest):

1. **Local** — the machine's local GPO (extracted; `ad-ds-group-policy-scope.md:47`)
2. **Site** — linked to an AD site, spanning potentially multiple domains (extracted; `ad-ds-group-policy-scope.md:49`)
3. **Domain** — applies to all users/computers in the domain (extracted; `ad-ds-group-policy-scope.md:51`)
4. **OU** — linked to an Organizational Unit, the most granular scope (extracted; `ad-ds-group-policy-scope.md:53`)

This is the **LSDOU** processing order. Each subsequent GPO can override settings from earlier ones — "last-writer-wins" (`ad-ds-group-policy-scope.md:134`). Within the same container level, lower link-order numbers (applied later) have higher precedence (extracted; `ad-ds-group-policy-scope.md:90`).

## Processing flow

At startup/sign-in, the Group Policy service (`ad-ds-group-policy-processing.md:35-37`):

1. Queries AD for the computer/user's site, domain, and OU chain
2. Collects all GPOs linked to those containers
3. Filters them via **security filtering** (must have Read + Apply Group Policy permissions) and **WMI filtering** (a query evaluated on the target machine) (`ad-ds-group-policy-scope.md:122-130`)
4. Passes each applicable GPO to the relevant **client-side extension (CSE)** — each CSE is an isolated component that processes its specific policy type (registry, security, scripts, etc.) (`ad-ds-group-policy-overview.md:40-42`)

## Inheritance modifiers

- **Enforced** (link property) — prevents lower-level GPOs from overriding this GPO's settings (`ad-ds-group-policy-processing.md:49-51`)
- **Block Inheritance** (container property) — prevents settings from higher-level containers from applying to this OU/domain, **except** enforced GPOs (`ad-ds-group-policy-processing.md:55-56`)
- **Loopback processing** — applies the computer's GPO user-configuration settings to any user who logs on (Merge or Replace mode) (`ad-ds-group-policy-processing.md:84-94`)

## Background refresh

After the initial foreground application, Group Policy refreshes in the background every **90 minutes** by default (with a random offset of up to 30 minutes) (`ad-ds-group-policy-processing.md:43`). Domain controllers check every 5 minutes (`ad-ds-group-policy-processing.md:100`). Trigger manually with `gpupdate.exe` or `Invoke-GPUpdate` PowerShell (extracted; `ad-ds-group-policy-processing.md:112-116`).

## Authoring tools

- **Group Policy Management Console (GPMC / gpmc.msc)** — the primary tool for creating, editing, linking, backing up, and modeling GPOs (`entities/ad-admin-tools.md:63-65`)
- **Local Group Policy Editor (gpedit.msc)** — for editing the local GPO only
- The **PDC Emulator FSMO role holder** is the default DC GPMC edits against (`topics/group-policy.md:46-48`) (inferred — connects the edit target to the FSMO role)

## Contradictions / caveats

The GPO's two halves (container in AD, template in SYSVOL) replicate independently and can desync if SYSVOL replication (FRS/DFSR) is unhealthy — a GPO can appear in AD but fail to apply because its template didn't reach the DC (`topics/group-policy.md:52-54`).

## References

### RH ground-truth (`kb:` / `ref:`)
- `kb:ad-ds-group-policy-overview` — [Group Policy overview for Windows Server](reference/active-directory/ad-ds-group-policy-overview.md)
- `kb:ad-ds-group-policy-processing` — [Group Policy processing for Windows](reference/active-directory/ad-ds-group-policy-processing.md)
- `kb:ad-ds-group-policy-scope` — [Group Policy scope in Windows](reference/active-directory/ad-ds-group-policy-scope.md)

### Wiki
- [[group-policy]] — the canonical synthesis page
- [[ad-admin-tools]] — GPMC as a primary AD administration tool
- [[active-directory-overview]] — broader AD context

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-group-policy-overview|Group Policy overview for Windows Server]]
- [[ad-ds-group-policy-processing|Group Policy processing for Windows]]
- [[ad-ds-group-policy-scope|Group Policy scope in Windows]]
<!-- crosslink:end -->
