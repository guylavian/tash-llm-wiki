---
title: "[Migrated from MSDN Exchange Dev] Hybrid Exchange - Unable to purge deleted mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/147884/migrated-from-msdn-exchange-dev-hybrid-exchange-un
question_id: 147884
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# [Migrated from MSDN Exchange Dev] Hybrid Exchange - Unable to purge deleted mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/147884/migrated-from-msdn-exchange-dev-hybrid-exchange-un (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] Hybrid Exchange - Unable to purge deleted mailbox  

User mailbox has been migrated to O365. Wanted to delete mailbox of a user without deleting the user account and create a new mailbox for the user. (Long story, office keeps crashing and we suspect possible corrupt items in mailbox. Tried everything else even MS support is of not much help).  

Deleted the mailbox using Delete-remotemailbox. How do I purge the deleted mailbox?  

There are no holds on the mailbox and license has been removed.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-02*

Hi,    

Generally we follow below methods to remove an o365 mailbox in hybrid:    

Move the AD Account to an OU not synced with AADConnect to Azure.    

In on-premises Exchange, using Disable-RemoteMailbox (remove the mailbox but not the user account) or Remove-RemoteMailbox (remove the user account as well).    

If the steps above not working for you, you could also try removing the entire object in Azure like this article introduces:    

Get-MsolUser -ReturnDeletedUsers - | FL UserPrincipalName,ObjectID    

Remove-MsolUser -ObjectId <GUID> -RemoveFromRecycleBin -Force    

Remove-Mailbox -Identity user@keyman  .com -PermanentlyDelete    

As for the -PermanentlyClearPreviousMailboxInfo parameter mentioned in the original thread, please refer to the introduction in this KB: Permanently Clear Previous Mailbox Info    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
