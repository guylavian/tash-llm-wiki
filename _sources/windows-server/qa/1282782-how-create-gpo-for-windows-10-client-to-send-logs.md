---
title: "how create GPO for windows 10 client to send logs to Windows 2012 r2 AD Server."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1282782/how-create-gpo-for-windows-10-client-to-send-logs
question_id: 1282782
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# how create GPO for windows 10 client to send logs to Windows 2012 r2 AD Server.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1282782/how-create-gpo-for-windows-10-client-to-send-logs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Windows 2012 r2 Server with AD and DNS role. which is monitoring other same domain joined Servers logs like Application, System and Security through WinRM.

I have Qty 1200 windows 10 Client 21 h2 Domain Client desktop machines in my network.

Which is giving only Security logs to the AD server.

I want to reconfigure windows 10 clients for sending Application and System logs too by GPO.

Please suggest the right procedure to make it happen.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-11*

A better option may be to set up a dedicated event collector.  

https://learn.microsoft.com/en-us/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
