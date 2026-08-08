---
title: "Exchange Hybrid migration fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1392367/exchange-hybrid-migration-fails
question_id: 1392367
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Hybrid migration fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1392367/exchange-hybrid-migration-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am running Exchange 2019 with CU 13 on a Windows server 2022 Datacenter.

I want to test in a Lab environment to migrate from exchange on premise to M365/.

When I run the Hybrid configuration is fails on below:

Not sure where to look for the issue. Tried few options on other website, but not the desire solution so far.

Anyone familiar with above issue?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-16*

Hi @w raspe  

Could you provide detailed error log?  you could check to see if you missed any prerequisites for Microsoft Hybrid Agent.

Also have you checked these two threads and referred to the methods there?

(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

https://www.reddit.com/r/exchangeserver/comments/oo1sek/hybrid_agent_fails_at_validating_hybrid_agent_for/

https://www.reddit.com/r/exchangeserver/comments/b6kbxq/validating_hybrid_agent_for_exchange_usage_is/

1.HybridManagement.psm Test-HybridConnectivity -O365 Endpoints = Ok

2.Enabled TLS 1.2 for .net 2 + 4

3.MRSProxy Enabled $false + $true + Basic Auth true + iis Reset 

4.Restart-WebAppPool MSExchangeServicesAppPool

5.Reinstalled Exchange Server

6.Renewed Exchange certificates

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
