---
title: "How can I get the size of folders in an exchange 365 mailbox?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1281654/how-can-i-get-the-size-of-folders-in-an-exchange-3
question_id: 1281654
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How can I get the size of folders in an exchange 365 mailbox?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1281654/how-can-i-get-the-size-of-folders-in-an-exchange-3 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A post box has grown about 50 GB in a year and I want to find out how is this possible. For this, I want to get the sizes of all folders. How can I accomplish this?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 3 · updated: 2023-05-10*

If you have access to the mailbox, both Outlook and OWA will readily show you this info. In Outlook, right-click on the root folder > Data file properties > Folder size > Server data. In OWA, go to Settings > General > Storage (or directly https://outlook.office.com/mail/options/general/storage)

As an admin, you can also get the same data via PowerShell:

`Get-MailboxFolderStatistics ******@domain.com | select Name,Folder*Size,Items*`
