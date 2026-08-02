---
title: "Failled to Move audit log mailbox exchange 2013 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160792/failled-to-move-audit-log-mailbox-exchange-2013-to
question_id: 1160792
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Failled to Move audit log mailbox exchange 2013 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160792/failled-to-move-audit-log-mailbox-exchange-2013-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello 

Exchange migration 2013 to 2019. Move arbitration mailboxes, all 6 Mailboxes are moving successfully and completed but one of those  audit log mailbox "SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9} " stuck since 24 hour bei 20%

I have already restarted the server

i need help please

Thx

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-22*

Hello Andy,

I'm trying to move the Arbitration Mailbox SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9} but the command doesn't work. I always get an error message. Cann you help please?

this is the command 

```
Get-Mailbox -Arbitration -Identity “SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}” | New-MoveReqeust -TargetDatabase "DB001"
```

Output:

```
New-MoveReqeust : The name "New-MoveReqeust" was not recognized as the name of a cmdlet, a function, a script file
or an executable program. Check the spelling of the name, or if the path is correct
(if included), and repeat the procedure.
In line:1 characters:90
```
