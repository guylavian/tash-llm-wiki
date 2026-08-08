---
title: "Exchange 2016: STOREDRV; mailbox server is offline (ID 4009)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/216473/exchange-2016-storedrv-mailbox-server-is-offline-i
question_id: 216473
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016: STOREDRV; mailbox server is offline (ID 4009)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/216473/exchange-2016-storedrv-mailbox-server-is-offline-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

432 4.3.2 STOREDRV; mailbox server is offline; STOREDRV.Deliver.Exception:ConnectionFailedTransientException.MapiExceptionNetworkError; Failed to process message due to a transient exception with message Underlying MAPI stream threw exception  

i ckecked https://www.frankysweb.de/exchange-2016-storedrv-mailbox-server-is-offline-id-4009/    website and do this plan but my problem not solved  

help me!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-04*

Agree with KaelYao and would also suggest   

-  Filtering the event logs to only show CRITICAL & ERROR events  

-  Review the APPLICATION & SYSTEM events for anything related to the database or Exchange  

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-04*

@javad alamian       

Hi,    

I noticed that you mentioned "sometimes my exchnage 2016  mailbox queues status stay retry and give error" in this post.    

Do you have the exact same error message "MapiExceptionRpcServerTooBusy" in event 4009 as in the link you provided?    

If not, please post a screenshot or text of the error message in event 4009 if possible.    

(Note: Don't forget to hide your personal information for security)    

I need to ask the following questions in order to get some more information:    

-  How many Exchange servers do you have in your environment? And what's the CU version of your Exchange server?    

-  Will the messages be successfully delivered eventually? Or will they remain stuck in the queue?    

-  Besides event 4009, can you find other error or warning events generated in the application log?    

-  Was the server under heavy load when the problem happened?    

Here are some suggestions:    

-  Upgrade to the latest CU version    

-  Disable the anti-virus software on your server if there are any    

-  Make sure all the Exchange related service are running    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
