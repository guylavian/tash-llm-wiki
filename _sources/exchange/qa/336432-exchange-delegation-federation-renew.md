---
title: "Exchange Delegation Federation renew"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/336432/exchange-delegation-federation-renew
question_id: 336432
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange Delegation Federation renew

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/336432/exchange-delegation-federation-renew (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a hybrid 2013 exchange setup and with in EAC\Servers\Certificates I see that 'Exchange Delegation Federation' self-signed certificate is about to expire but has a 'Renew' button.  

Questions:  

What impact will this have if I select 'Renew, then okay'?  

Are there other steps maybe via powershell that I should be doing instead?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-30*

@Crod      

There exist two situations: this certificate is expired or expire soon:    

-  If the federation certificate hasn't expired, you can update the existing federation trust with a new federation certificate.    

-  If the federation certificate has already expired, you need to remove all federated domains from the federation trust, and then remove and recreate the federation trust.    

For more detailed information, you can have a look about this article: Renew the federation certificate    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
