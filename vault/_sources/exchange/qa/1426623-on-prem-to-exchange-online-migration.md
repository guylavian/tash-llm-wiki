---
title: "On Prem to Exchange online migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1426623/on-prem-to-exchange-online-migration
question_id: 1426623
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# On Prem to Exchange online migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1426623/on-prem-to-exchange-online-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently running exchange on prem, no dag.  Single server.

We're wanting to do a cutover migration to get rid of exchange on prem permanently... however, we're currently syncing local AD with entra via AD Sync/Connect.  We've been syncing for licensing purposed for office 365 apps and have just recently upgraded to E3 licensing.

Is it possible to complete this without using a hybrid method?  Possibly turn off ad sync, migrate all mailboxes/public folders, turn off exchange, then re-enable sync?  Does anyone have a good reference for this?

Thank you!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-16*

Hi @Jason Smith,

It is possible to migrate without a hybrid deployment, while as you know cutover migration would not work when you are running dirsync.

You may need to disable the sync and re-enable it after the migration.

Below are several threads in the same situation:

Exchange cutover migration will work with AAD connect sync user?

Disable DirSync - Perform cutover migration - Re-enable DirSync

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
