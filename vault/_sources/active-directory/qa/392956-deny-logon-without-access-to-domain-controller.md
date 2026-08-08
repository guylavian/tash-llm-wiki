---
title: "Deny logon without access to domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/392956/deny-logon-without-access-to-domain-controller
question_id: 392956
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Deny logon without access to domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/392956/deny-logon-without-access-to-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I need to deny login to users who do not have connectivity to domain controller via VPN or LAN.  

This way you could always apply GPOs to users rather than remote users.  

Thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-13*

Hi,  

Based on my understanding, you want to prevent users logging on to any devices if there is no domain controller available to authenticate them, right?  

If I misunderstand you, please feel to let me know.  

To prevent prevent users logging on to any devices when there is no domain controller available, we can change Number of previous logons to cache to 0  

under Computer Configuration\Windows Settings\Security Settings\Local Policies\Security Options  

"This way you could always apply GPOs to users rather than remote users."  

Not sure the purpose you want to achieve, would you please tell more about your question?  

Best Regards,
