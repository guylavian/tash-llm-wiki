---
title: "Server 2025 domain controller in Active Directory shows DC version as \"Unknown\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5547811/server-2025-domain-controller-in-active-directory
question_id: 5547811
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor", "Q&A User"]
---
# Server 2025 domain controller in Active Directory shows DC version as "Unknown"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5547811/server-2025-domain-controller-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

We deployed two new Windows Server 2025 Standard in our domain as new domain controllers. But both in the Active Directory, the DC Version shows "Unknown". Searched on Microsoft and Google online, seems it is a known issue. Just wondering if there's any fix so far. Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-09-09*

Thank you, Quinnie, 

For the DC role, these "unknown" DC versions do have a critical impact on the domain users. We have a few random domain users who lost trust relationship with the DC, leading to issues with SYSVOL and Netlogon. The domain user needs to restart the PC a couple of times of PC and then can connect to the DC and read the SYSVOL. 

We have to spend a lot of time to reverse the DC back to Server 2022. May need to wait a bit longer for the server 2025. 

Regards,

G Huang

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-09-08*

Dear Gang Huang,

We understand that after deploying two Windows Server 2025 Standard domain controllers, the DC Version appears as “Unknown” in Active Directory. This behavior has been reported by other users and is currently recognized as a known issue.

The issue stems from schema and metadata updates not yet fully reflected in certain Active Directory tools. While it does not impact domain controller functionality, Microsoft is actively investigating and may release a fix in a future cumulative update. In the meantime, you can verify the DC build and role using PowerShell commands such as `Get-ADDomainController` or `dcdiag`, which provide accurate operational details.

We recommend monitoring the Microsoft Q&A thread on this topic for updates and guidance. If you encounter replication or trust issues, please let us know so we can assist further.

Best regards,

Quinnie Quoc.
