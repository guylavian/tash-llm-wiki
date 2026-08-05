---
title: "[Migrated from MSDN Exchange Dev] Mail wont move instantly to subfolder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/130544/migrated-from-msdn-exchange-dev-mail-wont-move-ins
question_id: 130544
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# [Migrated from MSDN Exchange Dev] Mail wont move instantly to subfolder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/130544/migrated-from-msdn-exchange-dev-mail-wont-move-ins (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] Mail wont move instantly to subfolder  

Hi,   

Weird problem:  

We got an Exchange 2016 (Version 15.1 Build 2106.2) onpremise mailserver. We are working on an remote desktop server with Microsoft Office Standard 2016 (16.0.5056.1000) installed. When we receive an e-mail in our Sales mailbox (added with full permissions by ECP) and trying to move the e-mail to a subfolder it wont move. After switching back to my personal e-mailadres and moving back to the sales inbox the message is gone. If I open the subfolder where I dragged the e-mail it's in their. Also tried to add the mailbox by username and password in my Outlook and the same issue appears.   

When I send an e-mail to my personal e-mailadres and drags it to an subfolder it's working properly.  

Looks something is going wrong with only the sales mailbox.  

Somebody knows whats going wrong or what I can check?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-22*

Hi Joy,  

In the OWA it's working fine, permissions I'm going to try. Already created a new DB and moved the mailbox. This didn't fix the issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-19*

Hi,    

Have you tried using OWA to perform the same action to move the message to subfolder? Did you get any error?    

You could also login to the sales mailbox and set the mailbox folder permission for your account like this link introduces: Unable to delete/move/rename an Inbox subfolder using Outlook or OWA    

If you still not able to move the messages to subfolder after performing all the steps above, we could try moving this sales mailbox to another database which will repair the issue of it.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
