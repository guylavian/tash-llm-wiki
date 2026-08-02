---
title: "Memory is growing with Connect-ExchangeOnline."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1362574/memory-is-growing-with-connect-exchangeonline
question_id: 1362574
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-online", "office-exchange-other-l1", "windows-business-windows-server-user-experience-powershell"]
---
# Memory is growing with Connect-ExchangeOnline.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1362574/memory-is-growing-with-connect-exchangeonline (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am seeing a higher utilization of memory with my code.   

I am creating a Runspace and then I am creating a temporary Powershell session for connecting to Exchange online using Connect-ExchangeOnline command. And after every 15mins I am checking that exchange connection token has expired or not using Get-ConnectionInformation. If token is expired I am disconnecting exchange connection using DIsconnect-ExchangeOnline and again connecting to exchange, and in this process my memory is shooting up the memory.  

I have also tried disposing runspace after Disconnect-ExchangeOnline but it is not releasing the memory.  

Can someone please advice?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-11*

Hello there,

It would be better if you could share your Code.

It is possible that using the ExchangeOnlineManagement v3 module takes up to 300MB. It is recommended that you try using the current release: Version 3.2.0

https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2?view=exchange-ps#release-notes

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer–
