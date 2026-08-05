---
title: "The \"Exchange Delegation Federation\" Certificate expired"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2148844/the-exchange-delegation-federation-certificate-exp
question_id: 2148844
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# The "Exchange Delegation Federation" Certificate expired

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2148844/the-exchange-delegation-federation-certificate-exp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am the hybrid environment with the Exchange server 2019 as the on-prem with 3 Nodes in two sides (DC and DR)

-  casmbx01 and casmbx02 in DC Site

-  casmbx03 in DR Site

The "Exchange Delegation Federation" Certificate expired on 12/23/2024.

Can anyone guide me on how to renew it step by step?

And what are the impacts?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-20*

Hi, @SUN PHEARA  

If the federation certificate has expired, you will need to remove all federation domains from the federation trust, and then delete and recreate the federation trust. For more information, see Renew the federation certificate: Exchange 2013 Help | Microsoft Learn

If the Exchange Delegation Federation certificate expires, it can cause the following problems: 

-  Users may not be able to retrieve free/busy and calendar information between on-premises and Exchange Online environments. 

-  If the federated certificate is invalid, running the Hybrid Configuration Wizard (HCW) may fail. 

-  It may be necessary to remove and recreate federated trusts, which can be a complex process. 

You can refer to these similar cases.

Exchange 2019 Delegation Federation certificate expired hybrid - Microsoft Q&A

Exchange Delegation Federation certificate expired - Microsoft Q&A

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
