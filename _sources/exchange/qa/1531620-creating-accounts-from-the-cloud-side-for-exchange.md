---
title: "Creating accounts from the cloud side for exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1531620/creating-accounts-from-the-cloud-side-for-exchange
question_id: 1531620
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Creating accounts from the cloud side for exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1531620/creating-accounts-from-the-cloud-side-for-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a domain syncing with Azure Sync, and Exchange in a hybrid environment.
We've been creating accounts in local AD, but would like to establish the Exchange side in the cloud to avoid the need to migrate the mailbox.  Is this a good practice?  We tried it, but the account never registered back to the on prem Exchange, and wasn't available through O365 OWA.
Is there a best practice for AD/Exchange in order to have things sync back down?  Password change is working in both directions.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-13*

Hi @Bruce Johnson  

Cloud only accounts cannot be managed by on premise servers.
If you have a hybrid environment, you can move all mailboxes to exchange online and keep at least one Exchange server to be able to modify Exchange attributes.

Please don’t forget to accept helpful answer
