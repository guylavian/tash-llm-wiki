---
title: "after updating the exchange cu11 2019 patch, normal user rights use get-mailboxdatabase-status | select Mounted get is empty"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1249911/after-updating-the-exchange-cu11-2019-patch-normal
question_id: 1249911
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# after updating the exchange cu11 2019 patch, normal user rights use get-mailboxdatabase-status | select Mounted get is empty

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1249911/after-updating-the-exchange-cu11-2019-patch-normal (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question



## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-21*

Hi @ 徐文青（Wenqing），

Based on your warning message that you cannot connect to the Microsoft Exchange Information Store service, restart the service when you run the get-mailboxdatabase command?

In my tests, when I stopped this service, I also failed to get the mount information with the same warning:

 
Please refer to the following steps to check if this service is running:

1.       Open Control Panel and select Large Icons

2.       Click the Administrative Tools and select services

3.       Open the services and select the Microsoft Exchange Information Store

4.       Check if it is running

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
