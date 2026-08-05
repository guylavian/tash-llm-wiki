---
title: "Public Folders Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1021122/public-folders-exchange-2019
question_id: 1021122
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Public Folders Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1021122/public-folders-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have an issue with public folder who they not see in outlook.    

We configure them on Exchange on-prem 2019 (version 15.2.1118.12)    

Could you please help me with this issue ?    

I tried with powershell to remove/add permission (PublicFolderClientPermission) however it is not working (the users don’t see the public folders)    

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-27*

This issue occurs because the AutoDiscover service can't discover the email address that is stamped on the public folder mailbox.    

Check this MS Article - https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/outlook-users-cannot-access-public-folders

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-26*

Hi,

Thank your for your reply BenOu-MSFT

-   The users previously added to access to this public folder see it. New users cannot see it (i tried with a test account and i have the same issue)

-   and 3. No we cannot saw it and cannot added it like you mentioned on your link.  

    4.The Outlook client version is Microsoft Office 2016 Standard (version : 16.0.4266.1001)

The test account is owner of this public folder
