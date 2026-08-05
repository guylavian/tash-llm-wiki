---
title: "exchange server 2019 hybrid mode storage question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2109959/exchange-server-2019-hybrid-mode-storage-question
question_id: 2109959
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange server 2019 hybrid mode storage question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2109959/exchange-server-2019-hybrid-mode-storage-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we have an exchange server 2019 running as a hybrid server with 365. all of our users have been migrated to 365 and we are currently looking to stop routing mail through exchange server and send it directly to 365. but I fear we have missed something. we currently do Veeam incremental backups from exchange server and it seems to backup about 10 gigs of new data every day but the drives aren't filling up so where is this data coming from/ what is it and do I need to worry about it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-24*

Hi,@chase frank

Thanks for posting your question in the Microsoft Q&A forum.

Based on your description, you want to email and send directly to 365. You need to update the MX record in your Domain Name System (DNS) and the MX record should point to your Office 365 environment so that the email flow points directly to Office 365.

You can refer to this link for details:https://learn.microsoft.com/en-us/exchange/transport-routing

We can only address questions about Exchange, about Veeam Incremental Backup, can only provide personal advice, for official advice, you can contact Veeam vendor.

Veeam incremental backups capture the changes that have occurred in the data since the last backup cycle. In the case of an Exchange server, these changes could include new emails, deleted items, calendar updates, and other modifications made by users throughout the day. 

Even though it seems like 10 GB of new data is being backed up daily, it doesn't necessarily mean that your drives will fill up at the rate of 10 GB per day.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
