---
title: "Exchange Online AuditLogSearch, no Move operations visible"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164770/exchange-online-auditlogsearch-no-move-operations
question_id: 1164770
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online AuditLogSearch, no Move operations visible

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164770/exchange-online-auditlogsearch-no-move-operations (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

With auditlogsearch we do get all kinds of operations like SoftDelete, HardDelete, MoveToDeletedItems etc.  

But we had an issue were a lot of mails where moved to another folder.

Why doesn't a move operation show up in the auditlog?

I'm using the script on this page:

[https://learn.microsoft.com/en-us/microsoft-365/troubleshoot/audit-logs/mailbox-audit-logs

Where Move should also be an operation that should be logged.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-01-27*

Did you enable owner logging?

[https://learn.microsoft.com/en-us/microsoft-365/troubleshoot/audit-logs/mailbox-audit-logs#owner-mailbox-audit-logginghttps://learn.microsoft.com/en-us/microsoft-365/troubleshoot/audit-logs/mailbox-audit-logs#owner-mailbox-audit-logging
