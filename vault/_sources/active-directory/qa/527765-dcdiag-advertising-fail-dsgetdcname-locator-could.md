---
title: "DCDIAG - Advertising fail - DsGetDcName - Locator could not find the server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/527765/dcdiag-advertising-fail-dsgetdcname-locator-could
question_id: 527765
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# DCDIAG - Advertising fail - DsGetDcName - Locator could not find the server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/527765/dcdiag-advertising-fail-dsgetdcname-locator-could (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have an issue with some Domain Controller... Whenever I ran a DCDiag and test the advertising it will fail... But if I we're to ran the same command right away it will then pass.

PS> dcdiag /s:ServerName /test:advertising

Directory Server Diagnosis

Performing initial setup:  

* Identified AD Forest.  

Done gathering initial info.

Doing initial required tests

Testing server: ServerName  

Starting test: Connectivity  

......................... ServerName passed test Connectivity

Doing primary tests

Testing server: ServerName  

Starting test: Advertising  

Fatal Error:DsGetDcName (ServerName) call failed, error 1722  

The Locator could not find the server.  

......................... ServerName failed test Advertising

PS> dcdiag /s:ServerName /test:advertising

Directory Server Diagnosis

Performing initial setup:  

* Identified AD Forest.  

Done gathering initial info.

Doing initial required tests

Testing server: ServerName  

Starting test: Connectivity  

......................... ServerName passed test Connectivity

Doing primary tests

Testing server: QSC\QSC-DC-02  

Starting test: Advertising  

......................... ServerName passed test Advertising

Any idea why??? and how it could be resolved.

Thank you for your help,  

Martin

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-25*

Hello @Haggus75   ,    

I would suggest you to please check Windows event viewer for AD related and advertising related logs.    

Also , Please verify time should same of all DC.    

If the reply was helpful, please don’t forget to upvote or accept as answer.     

Thanks, Prakash

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-25*

Could be some sort of network latency issue.  

--please don't forget to Accept as answer if the reply is helpful--
