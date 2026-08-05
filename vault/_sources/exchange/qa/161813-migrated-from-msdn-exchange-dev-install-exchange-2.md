---
title: "[Migrated from MSDN Exchange Dev] Install Exchange 2010 Management Tools on Windows 10"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/161813/migrated-from-msdn-exchange-dev-install-exchange-2
question_id: 161813
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Install Exchange 2010 Management Tools on Windows 10

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/161813/migrated-from-msdn-exchange-dev-install-exchange-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/4f46a481-007f-4ee8-9a5f-fb1a00f95a16/install-exchange-2010-management-tools-on-windows-10?forum=exchangesvrdevelopment  

Hello,  

I am trying to install exchange 2010 management tools on my Windows 10 PC.  

I've downloaded Exchange 2010 SP3 and run the installer selecting only the Management Tools. When it runs the prerequisites check, it fails on the tools with error: This computer does not belong to a valid Active Directory site. Check the site and subnet definitions.  

Both the server and my PC are part of the same domain. Windows 10 is running 20H2 19042.630 and the exchange server version is 14.03.0487.000  

What mistake am I making?  

Any help is much appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

Please make sure the PC is added into subnets of AD sites and service.    

Also, check if you have met Exchange Server system requirements and Exchange Server prerequisites.    

If still got failed, go to C:\ExchangeSetupLogs\ExchangeSetup.log and post the error information please.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
