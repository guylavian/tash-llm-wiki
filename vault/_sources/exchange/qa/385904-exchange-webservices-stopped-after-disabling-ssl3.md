---
title: "Exchange webservices stopped after disabling SSL3.0 and enabling TLS 1.2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/385904/exchange-webservices-stopped-after-disabling-ssl3
question_id: 385904
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Exchange webservices stopped after disabling SSL3.0 and enabling TLS 1.2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/385904/exchange-webservices-stopped-after-disabling-ssl3 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All,  

we have exchange2013 CU23 in our environment. CAS and MBX roles are on separate physical servers.   

At present we have hybrid environment with mailboxes on-premise and exchange online.  

Exchange webservices stopped when we disabled SSL3.0 and enabled TLS 1.2 on exchange servers.  

Request your assistance to fix this issue.  

Regards,  

Mohammed Nasim Shah

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-18*

I would suggest going through https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-2-enabling-tls-1-2-and/ba-p/607761 as a starter and making sure you have set the SystemDefaultTlsVersions correctly and have the correct CU's etc.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

Hi All,  

Is there any suggestion or tips?  

Regards,  

Nasim
