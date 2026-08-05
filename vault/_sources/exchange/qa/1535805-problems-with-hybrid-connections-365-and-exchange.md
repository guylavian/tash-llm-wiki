---
title: "Problems with hybrid connections 365 and exchange server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1535805/problems-with-hybrid-connections-365-and-exchange
question_id: 1535805
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Problems with hybrid connections 365 and exchange server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1535805/problems-with-hybrid-connections-365-and-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a big problem with my 365 communication, when I send to my main SMTP for example alias@contoso.local it tells me an error, but when I send ******@contoso.localonmicrosoft.com the message is sent, I have tried everything, I have validated the connectors but and it gives me a positive message, from my 365 accounts to premise, there is no problem, the emails arrive using @contoso.local, how could I repair this. Thank you very much in advance.
Exchange Online Plan 1 and Exchange Server 2019

Remote Server returned '550 5.1.10 RESOLVER.ADR.RecipientNotFound; Recipient not found by SMTP address lookup'

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-02-17*

alias@contoso.local is not a valid accepted domain in 365 or Azure. 
Have you added all the internet routable domains to Azure and validated them and do your accounts have that routable domain set correctly as the primary on their accounts?
https://learn.microsoft.com/en-us/microsoft-365/enterprise/prepare-a-non-routable-domain-for-directory-synchronization?view=o365-worldwide#what-if-i-only-have-a-local-on-premises-domain

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-19*

Thank you and for your feedback, connected to azure ad, and add an OU, but I have not changed the local domain, as you told me, is it necessary to reconfigure the login for my entire domain, or can I only make the change for the users in that OU, I already have the public domain added in domain and trusts.For privacy, cover the domain, in 365 I have configured the domains, in my local organization, I have ****.local and ***.gob.gt

This user is not in my organization, he is only in 365, but I cannot send him to my main SMTP, only to ***gobgt.onmicrosoft.com from on-prem account.

I don't have any problem from my 365 to my premise, the problem is from my premise to 365, in which I cannot send using the default *****.gob.gt
