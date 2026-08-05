---
title: "Exchange Server 2013 Outlook 2021 Problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1162194/exchange-server-2013-outlook-2021-problem
question_id: 1162194
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Server 2013 Outlook 2021 Problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1162194/exchange-server-2013-outlook-2021-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are Running Exchange 2013 and Outlook 2021 on a PC. The PC uses Windows 11 22H2 and the Server has Windows Server 2012 R2 Std. On all Clients even with Outlook 2021, any Mailbox works fine. When i however go to an Account which ran on a Failed Exchange 2007 Account. (Failed to Decomission) It will not Connect and asks Permanantly for a Password. If i click Cancel it will Fail too. I need Help!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-21*

We are only using Exchange 2013. No Exchange 2007 anymore.  

It is only on one Computer, and only one User!! This is so **Frustrating  

**  

I tried:

-  Deleting all Outlook References from Local Registry

-  Deleting Office

-  Installing Office 2013  

   Failing with Outlook 2013  

   Deleting Office 2013

-  Installing Office 2016
   Failing with Outlook 2016  

   Deleting Office 2016

-  Installing Office 2019  

   Failing with Outlook 2019  

   Deleting Office 2019

-  Resetting Profiles

-  Resetting Active Directory User

Nothing is working, it is so frustating you do not and could not Believe it!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-19*

Hi @Maximilian Schäfer,

When i however go to an Account which ran on a Failed Exchange 2007 Account. (Failed to Decomission) It will not Connect and asks Permanantly for a Password. If i click Cancel it will Fail too. I need Help!

Do you mean the Exchange 2007 account is added to the Outlook 2021 client but failed to connect? 

If this is the case, it's likely to be an expected behavior considering the fact that Exchange 2007 has reached end of support long ago. Also, according to Exchange Server supportability matrix, even Exchange 2013 is not officially supported to be used together with Outlook 2021, so not to mention it's an Exchange 2007 account.

Do you still need to use the Exchange 2007 account in Outlook client? If yes, you may need to use an earlier version of Outlook like Outlook 2013. If this failed account is no longer needed to be used, you can just delete it from the Outlook profile. 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
