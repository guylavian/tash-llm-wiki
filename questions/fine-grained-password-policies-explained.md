---
origin: eval-cohort
title: What are fine-grained password policies and when do you use them?
type: question
domain: active-directory
slug: fine-grained-password-policies-explained
summary: FGPP (Password Settings Objects) let a single AD domain enforce different password and lockout rules per user/group — used whenever the org needs stricter controls for privileged accounts, compliance tiers, or service accounts without spinning up extra domains.
sources:
  - kb:ad-ds-fine-grained-password-policies
  - kb:ad-ds-advanced-ad-ds-management-using-active-directory-administrative-center-level-200
  - note:_sources/active-directory/_raw/identity/ad-ds/manage/AD-DS-Simplified-Administration.md
provenance:
  extracted: 8
  inferred: 2
  ambiguous: 0
question_tier: conceptual
status: draft
updated: 2026-07-12
---

# What are fine-grained password policies and when do you use them?

**Fine-grained password policies (FGPP) let AD administrators define multiple password and account-lockout policies within a single domain, rather than being limited to one domain-wide policy from the Default Domain Policy GPO.**

## Body

### What they are

FGPPs are implemented as **Password Settings Objects (PSOs)** stored in the **Password Settings Container** under the domain's `System` container in AD (`reference/active-directory/ad-ds-fine-grained-password-policies.md:17-19`). Each PSO carries the full set of password/lockout settings:

- Minimum/maximum password age
- Minimum password length
- Password history count
- Complexity enabled/disabled
- Reversible encryption
- Lockout threshold, duration, and observation window
- Precedence (for conflict resolution when multiple PSOs apply)

**Key mechanics** (`entities/fine-grained-password-policies.md:30-33`):
- Apply only to **global security groups** and **user objects** (not OUs — scope by OU via a shadow group).
- Require **Windows Server 2012 Domain Functional Level** or higher.
- Default delegation: only **Domain Admins** can create/manage, but the right is delegable.
- When multiple PSOs apply to a user, the one with the **lowest precedence number** wins.

### History

Windows Server 2008 introduced FGPP programmatically (LDP.exe / ADSI Edit only). Windows Server 2012 added the first **GUI** in Active Directory Administrative Center (ADAC) (`reference/active-directory/ad-ds-advanced-ad-ds-management-using-active-directory-administrative-center-level-200.md:217-219`). The AD PowerShell module provides cmdlets since Windows Server 2008 R2 (`reference/active-directory/ad-ds-advanced-ad-ds-management-using-active-directory-administrative-center-level-200.md:237-251`).

### When to use them

**1. Privileged account hardening** — the most common use case. Apply a stricter PSO (longer password, lower lockout threshold, shorter max age) to `Domain Admins`, `Enterprise Admins`, and other Tier-0 groups, while regular users keep the default lighter policy (`reference/active-directory/ad-ds-fine-grained-password-policies.md:17-19`). This is the native control for the "stricter rules for privileged accounts" posture [[securing-active-directory]] recommends.

**2. Compliance tiers** — PCI-DSS, HIPAA, or FedRAMP may require different password standards per user class (e.g., 15-char minimum for privileged, 8-char for standard). FGPP lets the same domain satisfy both without domain proliferation.

**3. Service accounts** — service accounts often need different policies (e.g., no lockout, very long password age) than interactive users. Apply a permissive PSO to the service-account group (`inferred` — no single source states this directly, but it follows from the PSO-and-group assignment model).

**4. Mergers and acquisitions** — when two orgs with different password policies consolidate into one domain during a migration window, FGPP preserves each org's policy on their respective user sets until harmonization.

**5. Avoiding multi-domain complexity** — before FGPP, differing password requirements forced administrators to create separate domains. FGPP eliminates that architectural pressure (`reference/active-directory/ad-ds-reviewing-the-domain-models.md:35` — a domain-design document explicitly says FGPP "can also impact the domain design model that you select").

### Management tools

| Tool | Cmdlet / Path |
|---|---|
| ADAC (GUI) | `System → Password Settings Container → New → Password Settings` |
| PowerShell | `New-ADFineGrainedPasswordPolicy`, `Set-ADFineGrainedPasswordPolicy`, `Add-ADFineGrainedPasswordPolicySubject`, `Get-ADUserResultantPasswordPolicy` |

`reference/active-directory/ad-ds-fine-grained-password-policies.md:37-86` covers the full PowerShell creation workflow with examples.

### Precedence resolution

When a user is a member of multiple groups each with a different PSO, the PSO with the **lowest Precedence value** wins. ADAC shows the resultant policy via **View Resultant Password Settings** on any user object (`reference/active-directory/ad-ds-advanced-ad-ds-management-using-active-directory-administrative-center-level-200.md:253-261`).

### Pre-FGPP alternative (the "before" story)

Before Windows Server 2008, to have different password rules in the same org, you had to either write a custom password filter or deploy **multiple domains**. FGPP was the direct response to that pain point (`reference/active-directory/ad-ds-reviewing-the-domain-models.md:35` — "you had to either create a password filter or deploy multiple domains").

## See also
- [[fine-grained-password-policies]] — entity page
- [[securing-active-directory]]
- [[group-policy]]
- [[active-directory-overview]]

## References

### RH ground-truth (`kb:` / `ref:`)
- **ad-ds-fine-grained-password-policies** — "Configure fine grained password policies for Active Directory Domain Services in Windows Server" (Microsoft Learn)
- **ad-ds-advanced-ad-ds-management-using-active-directory-administrative-center-level-200** — "Advanced AD DS management using ADAC" (Microsoft Learn)
- **ad-ds-reviewing-the-domain-models** — "Reviewing the Domain Models" (Microsoft Learn)

### Wiki
- [[fine-grained-password-policies]]
- [[securing-active-directory]]
- [[active-directory-overview]]
- [[group-policy]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-fine-grained-password-policies|Configure fine grained password policies for Active Directory Domain Services in Windows Server]]
- [[ad-ds-advanced-ad-ds-management-using-active-directory-administrative-center-level-200|Advanced AD DS Management Using Active Directory Administrative Center (Level 200)]]
<!-- crosslink:end -->
