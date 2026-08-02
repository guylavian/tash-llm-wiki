---
title: "Exchange Server 2016 Hybrid EXO Throttling"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2077487/exchange-server-2016-hybrid-exo-throttling
question_id: 2077487
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2016 Hybrid EXO Throttling

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2077487/exchange-server-2016-hybrid-exo-throttling (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey folks, 

maybe somebody here have a hint for me. The MS Support is not very helpful. 

Our mails connecting to EXO are blocked for 60 mins/hr, so forever. Actually I have paused throttling / blocking for 2 weeks now. In this time the MS support was not able to help me. 

The actual build number for our Exchange DAG is 15.1.2507.39, so the newest available build. BUT 1 Server in the DAG hast the build number 15.1.2507.17 in his header. And I assume this is the reason for the throttling. 

btw, online in the out-of-date connecting on-premises Exchange servers report, the status is "resolved". But you can see that the mails were blocked. -> this must be a bug. 

The only way MS can read the build number are the headers and because of that I think it has to do with the false SMTP server ID from this one Server.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-07*

Hey @Anonymous  , 

-  where could I find this? I don't think so but I don't know how to find this. 

-  Nope

-  we don't want to AND it has to work

-  I know, I found this too, but ALL my Servers are up to date and the newest CU ist installed. 

-  Already happened and also not very helpful

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-25*

Hi, @Steve_1337

It sounds like your EXO connection and local Exchange server are experiencing mail throttling.

1.Make sure that all servers in the DAG are running the same version. The server with build number 15.1.2507.17 should be updated to match the other server (15.1.2507.39).

Exchange Server build numbers and release dates | Microsoft Learn

2.If a difference in build number is causing the problem, you need to update the outdated server.

Upgrade Exchange to the latest Cumulative Update | Microsoft Learn

3.Check the full SMTP headers of the blocked email to see exactly what server information is being used and diagnose if an outdated server is indeed the problem.

4.You can read these two articles on how to pause throttling and block obsolete on-premises Exchange Servers.

Throttling and Blocking Email from Persistently Vulnerable Exchange Servers to Exchange Online - Microsoft Community Hub

How to pause throttling and blocking of out-of-date on-premises Exchange Servers - Microsoft Community Hub

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
