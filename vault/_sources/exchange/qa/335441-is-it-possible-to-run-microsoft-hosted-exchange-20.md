---
title: "Is it possible to run Microsoft Hosted Exchange 2010 in coexistence with Exchange 2016?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/335441/is-it-possible-to-run-microsoft-hosted-exchange-20
question_id: 335441
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Is it possible to run Microsoft Hosted Exchange 2010 in coexistence with Exchange 2016?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/335441/is-it-possible-to-run-microsoft-hosted-exchange-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So we have a customer that still runs Microsoft Hosted Exchange 2010, so it's not your traditional standard server.  Does anyone know if it would be possible to install a second Exchange server in the network and setup coexistence between the two?  The goal is to temporary be able to setup this Exchange 2016 server as a frontend for mobile devices and Outlook to connect to while leaving the mailboxes on exchange 2010.  In the mean time most of the companies hosted on this server will migrate to a completely new domain with a new Exchange 2019 server or Office365.  So the purpose is a temporary frontend server for port 443 and 25.   I have not found anything about this online so I assume this is not possible or supported.    We have setup coexistence between two servers (Exchange 2010 Standard and Exchange 2016 Standard) but not the Hosted Exchange version.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-30*

@Caspar      

Microsoft Hosted Exchange 2010    

Do you mean this one? Exchange 2010 SP1 Information for Hosted Service Providers    

Exchange 2016 only supported coexist with Exchange 2010 SP3 RU 11 and later. It cannot coexist with Exchange 2010 SP1. So, even if you can create a new machine(you may cannot create new computer in that domain), you still cannot install exchange 2016 to coexist with Exchange 2010 SP1.    

In this situation, I would suggest you create a new domain and create Exchange and mailbox in it, then contact your provider to export mailbox data from hosted Exchange server, after that import data to mailbox on your new Exchange server.    

By the way, Exchange 2010 reached its end of support on October 13, 2020, I would suggest you try to migrate data for better security.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
