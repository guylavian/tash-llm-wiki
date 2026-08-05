---
title: "Active Directory OS Upgrade from Windows Server 2016 to Windows Server 2022."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1663669/active-directory-os-upgrade-from-windows-server-20
question_id: 1663669
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory OS Upgrade from Windows Server 2016 to Windows Server 2022.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1663669/active-directory-os-upgrade-from-windows-server-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team,

```
We are planning to Upgrade our Active Directory Operating System from Windows Server 2016 to Windows Server 2022 without raising the AD Forest/Domain Level. we will keep the current AD Functional Level Windows Server 2012 R2. in this scenario, will it require verifying Application Compatibility before the OS Upgrade ? please advise.
```Thanks,

Sameer
```

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-07*

Hello!

It is always recommended to verify application compatibility before upgrading the operating system, even if you are not raising the AD Forest/Domain Level. This is because some applications may have dependencies on specific operating system components or features that may not be available in the new operating system. It is best to check with the application vendors to ensure compatibility with Windows Server 2022 before proceeding with the upgrade.

About how to perform an in place upgrade, please refer to this link:

https://learn.microsoft.com/en-us/windows-server/get-started/perform-in-place-upgrade

Best Regards, 

Hania Lian

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
