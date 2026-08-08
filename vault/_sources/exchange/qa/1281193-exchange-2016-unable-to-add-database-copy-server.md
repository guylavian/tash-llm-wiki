---
title: "Exchange 2016 Unable to add database copy server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1281193/exchange-2016-unable-to-add-database-copy-server
question_id: 1281193
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 Unable to add database copy server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1281193/exchange-2016-unable-to-add-database-copy-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have 2 exchange 2016 STD servers

I have an database (its around 1TB at the moment) when I try to add Database copy I keep getting this error message "Server "Server01" has reached the maximum databases limit of 5."

On Server01 I can only see 3 database mounted

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-10*

Hi @lalajee  ,

You may be misunderstanding the counting. The database Copy will also occupy a place. The "5 databases" is a limitation on "active database" + "database copy". Database copies also count towards the database count.

 

Please refer the following.

If you try to add a database copy on EX19 based on the above picture, your issue will be reproduced.

 

 

Best regards,

Shaofan Lv

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
