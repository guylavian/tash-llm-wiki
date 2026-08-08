---
title: "Exchange Online Archive folder permission to others"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160160/exchange-online-archive-folder-permission-to-other
question_id: 1160160
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online Archive folder permission to others

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160160/exchange-online-archive-folder-permission-to-other (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have below requirement:

User A wants to share his Online archive to others but not to his primary mailbox section. Without providing the entire mailbox full access, how this can be achieved. We tried individual folder permission from Outlook, but works for Primary mailbox section and not for Online Archive. Any help would be greatly appreciated.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2023-01-12*

It cannot. The only way to access someone else's Online archive is via Full Access permissions, combined with Automapping. Technically you can do it without automapping too, by configuring the mailbox as additional account or accessing it via the Open another mailbox functionality in OWA. Either way, Full Access is needed, which in turn gives access to the primary mailbox as well.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-01-13*

Based on my experience and tests, even if we (as delegators) could assign other people (as delegates) permission to access our archive mailbox folders, these delegates will still not be able to access these folders. 

To let other delegates can access our archive folders, Full Access permission to the primary mailbox is needed. When we assign the Full Access permissions to a delegate, this delegate to which we assign the permissions can then access our online archive and make changes there.
