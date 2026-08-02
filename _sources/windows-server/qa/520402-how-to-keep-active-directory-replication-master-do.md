---
title: "how to keep active directory replication master domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/520402/how-to-keep-active-directory-replication-master-do
question_id: 520402
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# how to keep active directory replication master domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/520402/how-to-keep-active-directory-replication-master-do (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear: Support   

I have domain controller main then i replicate 2 server from main domain so now i need to shutdown old one and keep the new replication the master so how to configure that   because when i shutdown old one i can't join new user to active directory  because the old one shutdown .  

Kind Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-23*

This is unzip   

https://1drv.ms/u/s!AiIYpgM28tttj2eGJZQb4WFtUAja?e=ICxZ8e

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-22*

Please check link share   

https://1drv.ms/u/s!AiIYpgM28tttj2YYXbtZrgDtgQbb  

Kind Regards

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-20*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-19*

You need this information from main server or replication server   

Thank you for answer

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-19*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.
