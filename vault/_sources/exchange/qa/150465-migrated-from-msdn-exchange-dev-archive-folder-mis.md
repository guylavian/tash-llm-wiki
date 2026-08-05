---
title: "[Migrated from MSDN Exchange Dev] Archive folder missing in OWA and outlook2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/150465/migrated-from-msdn-exchange-dev-archive-folder-mis
question_id: 150465
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] Archive folder missing in OWA and outlook2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/150465/migrated-from-msdn-exchange-dev-archive-folder-mis (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange have been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link] Archive folder missing in OWA and outlook2016  

[Original post]  

Hi,  

Archive folder missing in OWA and outlook 2016. or (not visible )  

While clicking https://outlook.office.com/mail/archive it redirects and goes to https://outlook.office.com/mail/inbox.  

Get-MailboxFolderStatistics username | Select Name,FolderSize,ItemsinFolder  

it shows archive folder in the list.  

Please help  

Thanks  

JK

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-20*

Hi ,  

We changed PR_ATTR_HIDDEN property .and this issue got fix.  

Thank you very much for the solution.  

Thanks & Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

Hi ,  

We are got schedule to try today as per user . Will keep you posted.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-04*

Can it be done with powershell script . Please assist on this request.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-04*

Hi JK,    

Based on my experience, this issue might occur when the PR_ATTR_HIDDEN property of the Archive folder is set to True. Please follow the steps below to modify the property and see how it goes:    

-  Download and extract the MFCMAPI tool from http://mfcmapi.codeplex.com.    

-  Launch mfcmapi.exe, click OK through the intro screen. Click Session > Logon, select the Outlook profile for the affected mailbox, click OK.    

-  Double click on the affected mailbox, expand Root-Mailbox > IPM_SUBTREE(or Root Container > Top of information Store supposing you are running Online mode), locate the Archive folder.    

-  On the right pane, double click the PR_ATTR_HIDDEN property, clear the checkbox of Boolean, click OK, close all MFCMAPI windows, restart Outlook or OWA and check the result:    

     

Here is a document for your reference: Default folder is missing in Outlook and Outlook on the web.
