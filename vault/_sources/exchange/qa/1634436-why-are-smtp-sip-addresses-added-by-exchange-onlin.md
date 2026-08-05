---
title: "Why are smtp, sip addresses added by Exchange Online (presumably) ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1634436/why-are-smtp-sip-addresses-added-by-exchange-onlin
question_id: 1634436
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Why are smtp, sip addresses added by Exchange Online (presumably) ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1634436/why-are-smtp-sip-addresses-added-by-exchange-onlin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

The environment is hybrid; some users are created on-premises and synced via AAD Connect, some users are cloud only.

The exchange is the cloud one.

I am gathering information about the mail addresses with the Exchange Online module, with this command:  Get-Mailbox $mailaddr | Select -ExpandProperty EmailAddresses

Could you please explain to me, or guide me to the resources to understand:

-  Why is a SIP address automatically created for both hybrid and cloud users?

-  Why some cloud users have a MOERA address created (the smtp:*@domain.onmicrosoft.com address) and other cloud users don't?

Thank you in advance!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-28*

1.Why is a SIP address automatically created for both hybrid and cloud users?

Did you assign the Teams licenses to the users?

Based on my test, if you only assign Exchange Online license, the user only has SMTP address, and if you assign Teams license, it will create SIP addresses for the user.

2.Why some cloud users have a MOERA address created (the smtp:*@domain.onmicrosoft.com address) and other cloud users don't?

Microsoft Online Email Routing Address (MOERA) is automatically generated and included in the proxyAddresses attribute within Microsoft Entra ID, a process commonly referred to as proxy calculation.

Does the “cloud users”  mean that the users are created in Exchange Online directly?

Reference: Microsoft Entra UserPrincipalName population - Microsoft Entra ID | Microsoft Learn
