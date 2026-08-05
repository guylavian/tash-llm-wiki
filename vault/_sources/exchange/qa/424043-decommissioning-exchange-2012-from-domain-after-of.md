---
title: "Decommissioning Exchange 2012 from Domain after Office 365 Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/424043/decommissioning-exchange-2012-from-domain-after-of
question_id: 424043
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Decommissioning Exchange 2012 from Domain after Office 365 Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/424043/decommissioning-exchange-2012-from-domain-after-of (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm in the process of migrating an bunch of servers to newer Windows Server 2019 and unsure about this one old server.    

-  It's older domain controller that has Exchange 2013 installed but all services disabled.    

-  I have no idea how the migration to Office 365 was performed (before my time here), but the client is in Office 365 for their email.    

-  I have migrated AzureAD Connect from this older server to the new domain controller.    

My understanding is that I should be able to uninstall the software, but get errors about mailboxes still existing on the server.    

Also multiple Microsoft articles suggest that you need to main the last Exchange server due to directory Sync.    

This is one example - https://learn.microsoft.com/en-us/exchange/decommission-on-premises-exchange#scenario-two     

Is it safe to start the Exchange services and decomm the mailbox errors and then uninstall the software?    

Does anyone have any advise on this one?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-08*

@Daniel Burrowes      

If you still need to use AAD Connect, you must keep at least one Exchange on-premises. If you uninstall all Exchange on-premises server, this operation will remove mail attributes from local AD account and sync to AAD, it will effect the using of Exchange online mailbox.    

So, if you still need to use AAD Connect and want to remove old DC, you need to:    

-  Turn on this Exchange 2013    

-  Create Exchange 2019 on Windows server 2019 to coexist Exchange 2013.    

-  Migrate system mailboxes from Exchange 2013 to Exchange 2019.    

-  You will could uninstall Exchange 2013 and remove old DC.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
