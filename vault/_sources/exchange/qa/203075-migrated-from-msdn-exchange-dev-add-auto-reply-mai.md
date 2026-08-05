---
title: "[Migrated from MSDN Exchange Dev]add auto reply mail to a distribution group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/203075/migrated-from-msdn-exchange-dev-add-auto-reply-mai
question_id: 203075
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]add auto reply mail to a distribution group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/203075/migrated-from-msdn-exchange-dev-add-auto-reply-mai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.    

hello,    

i use Centre d'administration Exchange    

i try to put an auto reply mail to the distribuitin group info@xxxxxxxxxxxxx  .com,     

do you have any idea ?    

thanks for your response

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-18*

Hi,    

According to my research and test, the Distribution group itself cannot implement the OOF function, because it is only responsible for distributing the received mail to all members in the group. So you could create a new mailbox and add it to distribution group, then create an Inbox rule for this mailbox, when receives an email from the distribution group, it will send an automatic reply email. But it should be noted that in order to have the rule send automatic replies to your email messages while you're gone, you must leave Outlook running.    

About how to create the inbox rule you could refer to: Use rules to create an out of office message    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
