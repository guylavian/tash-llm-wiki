---
title: "[Migrated from MSDN Exchange Dev] exchange delete user but when i recreate its not appear"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/130514/migrated-from-msdn-exchange-dev-exchange-delete-us
question_id: 130514
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] exchange delete user but when i recreate its not appear

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/130514/migrated-from-msdn-exchange-dev-exchange-delete-us (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi,  

i delete in exchange an user that i created with existant user in active directory, but when i want to recreate this user its not appear.  

but in active directory the user is here.  

do you have an idea to reappear the user which is deleted in exchange ?  

Source link : https://social.msdn.microsoft.com/Forums/office/en-US/b40c6f89-a349-4f57-accb-eafee476afcc/exchange-delete-user-but-when-i-recreate-its-not-appear?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-19*

When deleting a mailbox from the Exchange server, the user's mailbox and its AD account will be deleted:    

    

This deleted mailbox will become "disable" status which hosted on database(Please note: This disabled mailbox is only kept in the database for 30 days by default, if you cannot find this mailbox with command below, you will cannot recover this mailbox):    

    

If you want to recover this mailbox, you need to recreate this an AD user first, then use command below to reconnect this mailbox to this AD account:    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
