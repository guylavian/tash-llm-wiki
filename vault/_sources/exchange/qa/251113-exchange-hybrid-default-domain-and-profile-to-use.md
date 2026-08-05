---
title: "Exchange Hybrid - default domain and profile to use"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/251113/exchange-hybrid-default-domain-and-profile-to-use
question_id: 251113
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange Hybrid - default domain and profile to use

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/251113/exchange-hybrid-default-domain-and-profile-to-use (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,  

We have non-Hybrid environment and currently we configured Hybrid using Hybrid Configuration Wizard. We wanted to know which is the default domain/recommended domain that should be used in Hybrid setup. As we can see two domains, one that is synced with Azure and the second, xxx.onmicrosoft.com.  

We also wanted to know, which default MAPI profile should be used to connect to mailboxes in Hybrid setup. Should we create a MAPI profile with Exchange Online user or Exchange On-premises user?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-01*

Hi @ExUser44   ,    

I agree with what Andy said. And it should be noted that before you do hybrid deployment, please make sure that your on-premises accepted domain has been added to Microsoft 365.    

For more information you could refer to: Create a hybrid deployment with the Hybrid Configuration wizard    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
