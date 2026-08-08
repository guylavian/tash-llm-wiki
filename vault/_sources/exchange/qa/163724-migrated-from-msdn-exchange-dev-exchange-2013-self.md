---
title: "[Migrated from MSDN Exchange Dev] Exchange 2013 Self signed Certificate about to or has already expired with Edge transport server."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/163724/migrated-from-msdn-exchange-dev-exchange-2013-self
question_id: 163724
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] Exchange 2013 Self signed Certificate about to or has already expired with Edge transport server.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/163724/migrated-from-msdn-exchange-dev-exchange-2013-self (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange have been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link] Exchange 2013 Self signed Certificate about to or has already expired with Edge transport server.  

[Original post]  

Good Morning to all,  

Just a brief background of my infrastructure it' quite simple: 1 exchange server, 1 edge server  

Our exchange server is mainly been used as an SMTP server and incoming mails are being received and synced to our CRM system.  

My first attept I tried renewing the cert for exchange server only then once I was done the emails won't go out thru Edge transport. I figure there is somethin I need to do there as well that I missed out. From what I've gathered so far is I need to redo the something about the subscription from my exchange to edge transport. Is this true? and if it is can point me on how to go about it? I don't have a development environment so I can't play and try it whenever I can unfortunately.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-11-16*

Hi,    

 From what I've gathered so far is I need to redo the something about the subscription from my exchange to edge transport. Is this true?    

Yes. As indicated in this official article, you need to recreate the Edge Subscription:    

If you renew or replace a certificate that was issued by a CA on a subscribed Edge Transport server, you need to remove the old certificate, and then delete and recreate the Edge Subscription. For more information, see Edge Subscription process.    

Basically the steps to rebuild the Edge subscription are as follows:    

-  On the Edge server run: New-EdgeSubscription –FileName "C:\EdgeSubscription.xml".    

-  Copy the EdgeSubscription.xml file to the Maibox server.    

-  On the Mailbox server, import the Edge subscription file by running the New-EdgeSubscription cmdlet.    

 For more information, you may refer to Edge Subscriptions.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
