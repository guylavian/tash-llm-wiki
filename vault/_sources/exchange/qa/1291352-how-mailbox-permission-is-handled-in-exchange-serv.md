---
title: "How mailbox permission is handled in exchange server cross forest migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1291352/how-mailbox-permission-is-handled-in-exchange-serv
question_id: 1291352
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# How mailbox permission is handled in exchange server cross forest migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1291352/how-mailbox-permission-is-handled-in-exchange-serv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All, We are migrating our existing exchange 2016 server to a new forest (in Exchange 2019). We are panning to use MS native tool/method to move mailboxes (new-move request). My question is, how the maibox permission- such as full mailbox, send-as, application impersonation are handled in this method. Are the permissions also migrated along with the move request?            Any help is really appreciated.. thanks !

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-01*

@Kael Yao-MSFT that was helpful, thank for your help

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-26*

Hi @Acloudguy  

Based on my test, the delegate permissions would get lost after the migration and you may need to re-assign the permissions.

This TechNet article also discusses this behavior: Mailbox auto-mapping is lost for migrated users after cross-forest migration

To me I would suggest use some scripts to export the permissions before migration and later re-assign permissions.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
