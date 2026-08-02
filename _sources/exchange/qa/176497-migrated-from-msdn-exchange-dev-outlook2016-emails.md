---
title: "[Migrated from MSDN Exchange Dev]Outlook2016 emails missing after drag to other mailbox."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/176497/migrated-from-msdn-exchange-dev-outlook2016-emails
question_id: 176497
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Outlook2016 emails missing after drag to other mailbox.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/176497/migrated-from-msdn-exchange-dev-outlook2016-emails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Hi,  

Our Environment is on a Exchange 2016 with Office 2016.  

We have a user who has moved/dragged some emails from the primary mailbox to a Shared mailbox ,however now the emails are missing from both primary and Shared mailbox.  

We were able to reproduce the issue from the specific sender. Any emails sent by that sender are missing from Outlook after moving. We have created a new mailbox , swapped PC still no luck.  

Thanks,  

Oj350350

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-26*

Hi,    

Only one user’s email have this issue or all users have?    

After moving the mail, the mail disappears immediately, or after a certain period of time, the mail disappears?    

-  Please try to logon OWA and add the shared mailbox, then try to move a test email to shared mailbox and see if there have the same issue.    

-  Please run “outlook /safe” in the run to start outlook as safe mode, to avoid interference caused by add-in.    

-  Please check the View Settings in the outlook, if you set it, only the type of mail you set will be displayed.    

     

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
