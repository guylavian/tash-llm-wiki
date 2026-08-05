---
title: "[Migrated from MSDN Exchange Dev]Exchange 2019 does not search forwarded message with attachment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/208204/migrated-from-msdn-exchange-dev-exchange-2019-does
question_id: 208204
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Exchange 2019 does not search forwarded message with attachment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/208204/migrated-from-msdn-exchange-dev-exchange-2019-does (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.    

Hi everyone.    

We encountered a very strange bug with exchange search.    

Context:    

Outlook working in on-line mode (running on terminal servers, so we can`t chnage it to cached mode due high IO)    

When user get message with any attached file AND forward it, the message disappears from the search results. Outlook search showing forwarded message from "SENT" folder, but do not showing original message in "INBOX"    

There is an example on sreenshot    

    

as you can see, search showing only 3 results, while we have 4 messages (2 in inbox, 2 in sent).    

OWA have same issue.    

Users do not use Conversation View, as some correspondence may contain dozens of messages that are difficult to view in this form.    

This problem appear after upgrading to Exchange 2019 (CU3) from 2016. Now we installed CU8, but this bug still here...    

Has anyone encountered a similar bug?

## Answer (community) — community member

*upvotes: 1 · updated: 2020-12-23*

Hi ,  

Do you have this issue with forwarding emails without attachments?  

After forwarding, can you see the original mail in your mailbox?  

Only one user have this issue or all have?  

-  Please check and make sure all Exchange servers are running normal, especially the “MS search service” and “MS search host controller”.  

  

2.Confirm that the database where the user is located has search index enabled, and the value of IndexEnabled should be true by running:    Get-mailbox <user name> | fl name,database  

    Get-MailboxDatabase <db name> | fl Name,IndexEnabled  

3.Check the status of the database and content index by running below command. If ContentIndexState shows FailedAndSuspended or Failed status, try to rebuild the database content index directory.

```
Get-MailboxDatabaseCopyStatus | ft Name,Status,ContentIndexState
```

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Hi @MarcoMandricardo-1414 , @Antoл K       

In the past month, I have installed several Exchange 2019 CU versions that you mentioned as having issue. And many experiments have been carried out in the environment, but unfortunately we have not been able to successfully reproduce your problem. In addition, I also searched and researched cases of search problems caused by BigFunnel, but no specific solutions were found in the cases.    

Considering that the problem has already affected your actual use, in order to further investigate the root cause of the problem, it is recommended that you open a case with Microsoft for further investigation.    

If you successfully solve the problem, you can also share your solution here. This will be beneficial to other community members as well.    

I will continue to test and research to find more relevant information.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-05*

Hi @Lucas Liu-MSFT   , сan you please tell me if there is any information about the bug  over the past month? Is the issue reported as a bug? There will be a new CU coming soon, it would be great to get a bug fix in it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-20*

hi,    

we have a problem like this, but with all mail,    

if the first action is forward, the next search always don't display it in inbox folder search.    

we have this scenario:    

Exchange 2019 CU7 Version 15.2 ‎(Build 721.2)‎    

with outlook in online mode because of RDP server    

Microsoft Outlook 2016 (16.0.5110.1000) MSO (16.0.5110.1001)  32bit    

i have check bifunnell search index and i have 0 element not index. but the problem is still here.    

someone has microsoft support for ask a solution?    

please not tell me to use cached mode. i have an RDP farm.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-23*

Without attachments search working fine, you can see it on screenshot.  

After forwarding - yes, the original message exist in inbox, but search don`t showing it.  

Only one user - no, all users, also i have tested this bug on 3 installations of Exchange Server 2019 in different Active Directory forests.  

- 

-  Service working, we tryed to restart it, but unsuccessfully  

- 

-  As i know, exchane 2019 does not have IndexEnabled attribute in mailbox database, because search engine was changed.  

P.S. Mailbox migration from one MDB to another fix issue with exsiting messages. But after migration new emails having same problem.
