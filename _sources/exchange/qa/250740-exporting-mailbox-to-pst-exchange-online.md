---
title: "Exporting Mailbox to PST Exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/250740/exporting-mailbox-to-pst-exchange-online
question_id: 250740
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exporting Mailbox to PST Exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/250740/exporting-mailbox-to-pst-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Forum, Im new to the forum and there for this is my 1st post. I've been looking for a way to export mailboxs to PST. We have Exchange online.(we do not have any physical exchange server) I am exchange admin. I have tried giving myself Mailbox Import Export role I only get these option. ![61844-image.png][1] [1]: /api/attachments/61844-image.png?platform=QnA What am i doing wrong. I do not prefer using any 3th party tools to export mails. Im able to connect powershell to Exchange online, but unable to find the commands to export mailboxes to PST.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-01-29*

You're not doing anything wrong, there simply isnt an "export to PST" functionality in Exchange Online. The closest you can get is using eDiscovery export: https://learn.microsoft.com/en-us/microsoft-365/compliance/export-search-results?view=o365-worldwide    

Or you can export via Outlook.
