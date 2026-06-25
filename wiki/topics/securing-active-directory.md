---
title: Securing Active Directory (best practices)
type: topic
domain: active-directory
slug: securing-active-directory
summary: Microsoft's defensive model for AD — reduce the attack surface (entry points, credential-theft targets), enforce least-privilege/tiered administration with secure admin hosts, monitor for signs of compromise, and plan for breach recovery; the spine over the securing-AD reference appendices.
sources:
  - web:https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory (Microsoft Learn — Best practices for securing Active Directory, fetched 2026-06-18)
  - web:https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/implementing-least-privilege-administrative-models (Microsoft Learn — Least-privilege administrative models, fetched 2026-06-18)
provenance_extracted: 7
provenance_inferred: 3
provenance_ambiguous: 0
symptoms:
  - "pass-the-hash"
  - "credential theft"
  - "privilege escalation"
tags: [security, directory-services, concept]
status: draft
updated: 2026-06-18
---

# Securing Active Directory (best practices)

**AD security is about protecting the directory from compromise, not preventing every
attack attempt: shrink the attack surface, contain privilege, watch for compromise,
and plan to recover.**

## Body

The Microsoft guidance organizes into four moves:

1. **Understand and reduce the attack surface.** Common entry points are unpatched
   systems, weak antimalware, and outdated apps/OS. Attackers start on one or two
   hosts and escalate laterally — so the most **attractive accounts for credential
   theft** are highly privileged ones (Domain/Enterprise Admins) that log on widely.
2. **Least-privilege & tiered administration.** Don't run daily work as a privileged
   account; separate admin tiers so a workstation compromise can't harvest
   domain-admin credentials. Use **secure administrative hosts** (hardened,
   internet-isolated jump hosts) for privileged work, and delegate narrowly via OUs
   rather than handing out broad group membership.
3. **Protect privileged credentials.** This is where [[windows-laps]] (unique,
   rotated local-admin passwords to stop pass-the-hash/lateral movement) and
   [[group-managed-service-accounts]] (no human-managed service passwords) fit the
   defensive model directly (inferred — these features implement the credential-theft
   mitigations the guidance calls for).
4. **Monitor and plan for compromise.** Audit and monitor for signs of compromise,
   and pre-build a recovery capability — assume breach. When the directory itself is
   destroyed, recovery is [[ad-forest-recovery]].

The reference tier carries the detailed playbooks behind this spine: privileged/
protected accounts and groups, securing the built-in Administrator and the Enterprise/
Domain/Administrators groups, reducing the attack surface, monitoring for compromise,
and events to monitor.

## Contradictions / caveats

- Securing AD is a program, not a setting — the guidance is explicit that no
  IT infrastructure is ever perfectly immune; the goal is raising cost and
  containing blast radius (inferred framing from the source).
- Tiered admin and secure admin hosts add operational friction; teams often skip
  them, which is precisely the gap credential-theft attacks exploit (inferred).

## Reference notes
- [[ad-ds-best-practices-for-securing-active-directory]]
- [[ad-ds-implementing-least-privilege-administrative-models]]

## See also
- [[windows-laps]]
- [[group-managed-service-accounts]]
- [[ad-forest-recovery]]
- [[active-directory-implementation-review]]
- [[tiered-administration-model]]
- [[secure-administrative-hosts]]
- [[credential-theft-and-attractive-accounts]]
- [[protected-accounts-and-groups]]
- [[monitoring-ad-for-compromise]]
- [[advanced-audit-policy]]
- [[software-restriction-policies]]
- [[reducing-ad-attack-surface]]
