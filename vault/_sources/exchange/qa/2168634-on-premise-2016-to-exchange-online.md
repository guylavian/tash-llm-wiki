---
title: "On premise 2016 to exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2168634/on-premise-2016-to-exchange-online
question_id: 2168634
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# On premise 2016 to exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2168634/on-premise-2016-to-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all, i have a hosted exchange 2016 with 22 tenanats that I need to migrate. I don't want to install AAD connect or hybrid.

Is there a way to do it manually by importing a CSV file?

Or do a cutover with selective mailboxes?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-27*

Hi @Ella Taylor, If you want to move only certain mailboxes, you can use a cutover migration, which lets you select specific mailboxes instead of moving all at once.

You create a list of the mailboxes you want to migrate using a CSV file and upload it when you start the migration. Microsoft 365 will only migrate the mailboxes you’ve listed.

This is a more automated way and saves time compared to manually handling each mailbox. However, if you have a lot of mailboxes or large mailboxes, the manual approach can be time-consuming, so you might want to plan accordingly

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-27*

Hi @Ella Taylor,  

If you want to move only certain mailboxes, you can use a cutover migration, which lets you select specific mailboxes instead of moving all at once.

You create a list of the mailboxes you want to migrate using a CSV file and upload it when you start the migration. Microsoft 365 will only migrate the mailboxes you’ve listed.

This is a more automated way and saves time compared to manually handling each mailbox.  

However, if you have a lot of mailboxes or large mailboxes, the manual approach can be time-consuming, so you might want to plan accordingly
