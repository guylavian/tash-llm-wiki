---
title: "Two active directory support for ADFS authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1089033/two-active-directory-support-for-adfs-authenticati
question_id: 1089033
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Two active directory support for ADFS authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1089033/two-active-directory-support-for-adfs-authenticati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Community,     

I have a customer with a tricky scenario.    

Two Active Directory  example.com , first.com     

Microsoft exchange is integrated with example.com only     

First.com users will use exchange services of example.com     

If I use ADFS integration for OWA, How will the authentication happen for first.com users     

Can ADFS handle two separate domains ?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-22*

@Pierre Audonnet - MSFT   I am trying to provide MFA to users. As per your comment I can have two AD integrated via ADFS. Will the adfs server understand once the request comes in from exchange server - it has to re-direct to the secondary domain?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-11-15*

Those are two different things here.    

From an AD FS perspective, it is fine to come from any trusted domain.    

From an Exchange's perspective, the authentication is one thing, but the account needs a mailbox, I guess. So, I'll let the Exchange SME comment on that part (I guess in a case of a resource domain where the user is in A and the mailbox in B, they might be scenarios where that is applicable).
