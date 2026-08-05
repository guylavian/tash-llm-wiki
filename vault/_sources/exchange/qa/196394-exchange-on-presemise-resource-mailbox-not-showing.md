---
title: "Exchange On-presemise resource mailbox not showing in exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/196394/exchange-on-presemise-resource-mailbox-not-showing
question_id: 196394
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Exchange On-presemise resource mailbox not showing in exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/196394/exchange-on-presemise-resource-mailbox-not-showing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Need help with the following issue.  

Recently, we deploy an Exchange hybrid, and everything working as expected but the Exchange resource mailbox (Hosted in on-premises) not showing in the exchange online.  

Any Idea?  

Thank You  

Nur Hossain

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-14*

Hi @Nur Hossain      

Agree with the reply above from AshokM. Move the resource mailbox to the synced OU in AD, after the synchronization you will see the resource mailbox account list in Users->Active users and show as Synced from on-premises.    

    

    

Then we can move this resource mailbox from on-premise to cloud. Detailed stsp here: Move mailboxes between on-premises and Exchange Online organizations in hybrid deployments    

Exchange admin center->Recipients->Migration. Click +, Migrate to Exchange Online. Then create the migeation batch.     

After the migration complete, we are able to see the migrated resource mailbox in cloud.    

Also note that, we still need to manage that mailbox on-premise, or we will get the error information like below    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
