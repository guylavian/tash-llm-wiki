---
title: "WAP and ADFS on differant domains"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/355859/wap-and-adfs-on-differant-domains
question_id: 355859
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# WAP and ADFS on differant domains

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/355859/wap-and-adfs-on-differant-domains (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've setup an adfs that works well inside our network however there is a need now to use it to access a site from outside the domain. I was looking at setting up a WAP in our DMZ however the internal and external domain are different. Everything I've looked over states the internal and external domain have to be the same in order to get this working properly. Is there a was around this?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-14*

The WAP servers do not have a requirement to be domain joined at all when they are solely used as ADFS Proxy servers.  

You need to domain joined them only if you intend to publish non-claim aware applications using Kerberos constrained delegation. If not, they can even be in a workgroup.
