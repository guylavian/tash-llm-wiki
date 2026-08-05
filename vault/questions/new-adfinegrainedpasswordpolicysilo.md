---
title: What does New-ADFineGrainedPasswordPolicySilo create?
type: question
domain: active-directory
slug: new-adfinegrainedpasswordpolicysilo
summary: The cmdlet New-ADFineGrainedPasswordPolicySilo does not exist. It conflates New-ADFineGrainedPasswordPolicy (creates a PSO) and New-ADAuthenticationPolicySilo (creates an authentication policy silo).
sources:
  - note:_sources/active-directory/_raw/identity/ad-ds/get-started/adac/fine-grained-password-policies.md
  - note:_sources/active-directory/_raw/identity/ad-ds/manage/How-to-Configure-Protected-Accounts.md
provenance:
  extracted: 2
  inferred: 1
  ambiguous: 0
question_tier: conceptual
tags: [authn, authz]
status: draft
updated: 2026-07-12
graph_community: "Active Directory — Domain Services Overview"
---

# What does `New-ADFineGrainedPasswordPolicySilo` create?

**The cmdlet `New-ADFineGrainedPasswordPolicySilo` does not exist in the Active Directory PowerShell module.** It is a conflation of two separate, real cmdlets:

1. **`New-ADFineGrainedPasswordPolicy`** — creates a fine-grained password policy, also known as a Password Settings Object (PSO), in Active Directory. This cmdlet accepts parameters such as `ComplexityEnabled`, `LockoutThreshold`, `MinPasswordLength`, `MaxPasswordAge`, etc., and stores the resulting object in the Password Settings Container under the System container of the domain (`fine-grained-password-policies.md:53-75`).

2. **`New-ADAuthenticationPolicySilo`** — creates an authentication policy silo, a container object that groups user, computer, and service accounts to apply common authentication policies (part of the Windows Server 2012 R2+ authentication policy and silo feature). Its key parameter is `-Enforce` to move from audit-only to enforcement mode (`How-to-Configure-Protected-Accounts.md:431-434`).

If the goal was to create a fine-grained password policy, the correct cmdlet is `New-ADFineGrainedPasswordPolicy`. If the goal was to create a silo for authentication policies, the correct cmdlet is `New-ADAuthenticationPolicySilo`.

## See also
- [[fine-grained-password-policies]] (wanted page)
- [[authentication-policy-silos]] (wanted page)
