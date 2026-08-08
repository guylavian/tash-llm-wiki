---
title: "[Migrated from MSDN Exchange Dev]Exchange 2019 is not syncing old emails with outlook mobile app only"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/138842/migrated-from-msdn-exchange-dev-exchange-2019-is-n
question_id: 138842
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Exchange 2019 is not syncing old emails with outlook mobile app only

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/138842/migrated-from-msdn-exchange-dev-exchange-2019-is-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

currently, I have an issue for outlook mobile app to sync the old emails and emails into subfolders, even though the sync is working properly with any other mobile app.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-26*

November is a good‘I said no’ time found out why starla lost her mind about that, I said YES BUT STAR CAge elm street sky rules

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-26*

Hi ,    

-  Please try to clean up the cached information in Outlook for mobile, then uninstall and reinstall Outlook. Then login your account again.    

-  Please login on the different mobile decive to check whether the issue was related with mobile types.    

-  Are the old emails that cannot be displayed are older than a certain day? If so,  you could change the setting “Mail days to sync” of Password and Accounts to be No Limit on your mobile. Then restart Outlook or Mail app to check whether the issue still exists.    

    

-  If the email that is not displayed is of a random date, then the problem may be caused by Active Sync. Please check whether there are Active Sync related error logs in the event viewer and IIS Log. If so, check the error message and HTTP status codes. If possible, please share with us, but you need to pay attention to covering your personal information.    

For more information :The HTTP status code in IIS 7 and later versions    

    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
