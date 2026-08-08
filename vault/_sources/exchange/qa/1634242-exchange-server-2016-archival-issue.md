---
title: "Exchange Server 2016 - Archival Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1634242/exchange-server-2016-archival-issue
question_id: 1634242
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-licensing", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Server 2016 - Archival Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1634242/exchange-server-2016-archival-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have tried to explain the request in below format, Can anyone let me know the possibility for the below request to resolve.

Exchange Server 2016 - Enterprise Edition License is installed.

Main Mailbox
The user is currently using with Outlook Application

Main Mailbox
The user is currently using with Outlook Application

Archival Mailbox
After 365 days, Emails from Main MailBox are moved to Archival Mailbox.

Exchange Server - Archival Mailbox - Current Status

User - Allowed
Reply/Forward to Emails on Archival Mailbox

User - Allowed
Delete on Archival Mailbox

User - Allowed
Move Emails from Archival to Main Mailbox

Exchange Server - Archival Mailbox - Requirement

User - Allowed
Reply/Forward to Emails on Archival Mailbox

User - Restricted
Delete on Archival Mailbox

User - Restricted
Move Emails from Archival to Main Mailbox

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-27*

Not possible, as the user is still an owner of his own mailbox, and any additional mailboxes "attached" to it, such as the Online Archive. You can address the deletion requirements by placing the mailbox on litigation hold, effectively ensuring any deleted item is still preserved, but there is no way to restrict moving of items.
