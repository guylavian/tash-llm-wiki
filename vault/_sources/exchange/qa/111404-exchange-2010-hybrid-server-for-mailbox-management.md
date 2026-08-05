---
title: "Exchange 2010 Hybrid Server for mailbox management"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/111404/exchange-2010-hybrid-server-for-mailbox-management
question_id: 111404
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange 2010 Hybrid Server for mailbox management

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/111404/exchange-2010-hybrid-server-for-mailbox-management (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

I'm in the middle of a migration for Exchange 2010 to Office 365. Once the mailboxes are migrated and I am ready to decommission the Exchange 2010, do I still need a new Hybrid server on prem to manage the mailboxes?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-30*

Hi @KashifRashid-5415 , agree with Andy suggests.    

If you use AAD sync, your synced online users can only be managed within on-premise AD, as a result, it is necessary to keep an on-premise Exchange server to manage user’s mailbox. Like the Scenario two in the official document.    

And if you have all of the mailboxes in Exchange Online and do not need to manage users from on-premises and no longer have a need for directory synchronization or password synchronization. You can safely disable directory synchronization and remove Exchange from the on-premises environment. Just like Scenario one introducees    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
