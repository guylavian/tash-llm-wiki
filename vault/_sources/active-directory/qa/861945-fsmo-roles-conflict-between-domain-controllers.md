---
title: "FSMO Roles Conflict between Domain Controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/861945/fsmo-roles-conflict-between-domain-controllers
question_id: 861945
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# FSMO Roles Conflict between Domain Controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/861945/fsmo-roles-conflict-between-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

One site has two domain controllers DC01 and DC02, replication is not good , DC01 is claiming PDC and Infra while other one [DC02] is claiming all 5 roles, this is sort of strange scenario, the other guy tried to transfer or seize roles which was failed.  

Any suggestion will be appreciated.  

Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-05-24*

It sounds like the two have been disconnected at some point and roles were seized to other one. In this case you don't have much choice but to pick one and rebuild the other from scratch.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-05-24*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiagDC1.log`  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiagDC2.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.
