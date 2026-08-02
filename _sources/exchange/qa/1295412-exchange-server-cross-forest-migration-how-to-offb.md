---
title: "Exchange server cross-forest migration - How to offboard\\rollback ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1295412/exchange-server-cross-forest-migration-how-to-offb
question_id: 1295412
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange server cross-forest migration - How to offboard\rollback ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1295412/exchange-server-cross-forest-migration-how-to-offb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We have a plan to migrate mailbox from one forest to another using MS native migration tools - New-MoveRequest or the New-MigrationBatch.

Migration method used as per the instruction below.

https://learn.microsoft.com/en-us/exchange/architecture/mailbox-servers/prep-mailboxes-for-cross-forest-moves?view=exchserver-2019

My question is how can we rollback\offboard the mailbox migration, i.e if needed how do we move the mailbox back to source forest? I don't see any MS article detailing this, any help in this is really appreciated !

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-06-02*

Hi @Acloudguy  

To me It may depend on which migration process you are in when you want to reverse the change.

For example, if you have finished the migration to another forest, you can simply re-do the migration to move the user and the mailbox back to the original forest.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
