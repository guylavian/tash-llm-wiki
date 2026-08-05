---
title: "Migrate public folder mailbox to exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2121071/migrate-public-folder-mailbox-to-exchange-online
question_id: 2121071
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Migrate public folder mailbox to exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2121071/migrate-public-folder-mailbox-to-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,

We have an exchange 2016 hybrid environment and mailbox can migrate to Exchange online. The public folder mailbox was published to exchange online, so both on-premise exchange user and exchange online user can manage and access the public folder. 

We are planning to migrate the public folder mailbox to exchange online: 

-  As the public folder published to EXO already, what is the next step to migrate public folder mailbox? 

-  If the public folder mailbox migrated to exchange online, do the on-premise user cannot access the public folder?

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-11-20*

You cant migrate the public folder mailbox to ExO, just the folders themselves.

In other words, you migrate folders from the on-prem public folder mailboxes to public folder mailboxes in Exchange Online. The PF mailboxes themselves are not moved. 

https://learn.microsoft.com/en-us/exchange/collaboration/public-folders/migrate-to-exchange-online?view=exchserver-2019
