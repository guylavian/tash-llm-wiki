---
title: "How to check which Exchange Online Inbox Rule moved email to folder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1657102/how-to-check-which-exchange-online-inbox-rule-move
question_id: 1657102
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to check which Exchange Online Inbox Rule moved email to folder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1657102/how-to-check-which-exchange-online-inbox-rule-move (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Problem: Sometimes mails are moved to a folder, but there is no inbox rule which seems to do that.

Additional Infos: We are using 100% Exchange Online with Outlook Web, and NOT a locally installed Outlook App, which could have an own rule set. So the inbox rule must come from EXO. In the EXO message trace of the moved email, I can see the following status: “The message was delivered to the recipient's mailbox. Because of an Inbox rule the recipient set up, the message was delivered to the following folder: Folder: xxx”.  

I already checked all rules via Powershell incl. hidden rules without any result:

```
Get-InboxRule -Mailbox xxx -IncludeHidden
```

Question: How can I investigate, which rule or other process moved the mail somewhere else.

Many thanks for your help  

Joachim Denk

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-04-17*

You may have an orphaned rule

Start Outlook the /cleanrules switch ( Backup any rules first)

or 

mfcmapi

https://learn.microsoft.com/en-us/outlook/troubleshoot/data-files/delete-corrupted-public-folder-rule
