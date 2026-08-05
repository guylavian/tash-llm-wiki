---
title: "Virtual Domain Controller - Replication Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/336235/virtual-domain-controller-replication-issue
question_id: 336235
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Virtual Domain Controller - Replication Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/336235/virtual-domain-controller-replication-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After importing Virtual Domain controller 2008 from one hyper V host to other same 2008 hyper V host. We are facing replication issue . Attached is the screenshot for reference. Kindly suggest the solution.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-29*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.
