---
title: "If I have a hybrid environment for Exchange would it show that my domain is federated"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2110789/if-i-have-a-hybrid-environment-for-exchange-would
question_id: 2110789
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# If I have a hybrid environment for Exchange would it show that my domain is federated

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2110789/if-i-have-a-hybrid-environment-for-exchange-would (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

If I'm in a hybrid environment with hosted exchange and exchange online, would it show then that I have a federated domain?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-10-25*

I dont see that with my hybrid domains.  Are you using ADFS on-prem?

Whats the status of that domain?

You can easily see if Azure says its federated:

https://portal.azure.com/#view/Microsoft_AAD_IAM/DomainsList.ReactView

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-25*

Hi, @Ryan McGuire

When you're in a hybrid environment with both hosted Exchange and Exchange Online , your domain might appear as a federated domain in the M365 Admin Centre.

This is normal and expected behaviour because hybrid deployments involve creating a federated trust between the on-premises Exchange organization and Exchange Online, which enables secure mail routing, a unified global address list (GAL), free/busy, and calendar sharing.

This is usually due to the following reasons:

-  When you set up a hybrid environment, some configurations often include setting up federation trusts.

-  Federation is used to enable single sign-on (SSO) and ensure seamless authentication between AD and AAD.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
