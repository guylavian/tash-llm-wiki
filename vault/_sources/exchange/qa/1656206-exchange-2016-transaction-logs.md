---
title: "Exchange 2016 transaction logs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1656206/exchange-2016-transaction-logs
question_id: 1656206
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 transaction logs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1656206/exchange-2016-transaction-logs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We recovered a Exchange 2016 server to a new location, and the server is running fine, DB is clean. We have noticed that there is missing emails from when we moved the server.

We have logged in to the old server and have access to all the old transaction logs from the missing period. We have copied them across to the new server and tun eseutil /r e00 /l "path to recovered logs" /d "path to DB folder" /i and it completes, but we are still not seeing he recovered emails.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2024-04-22*

Hi @Craig Hester,

Users can see all emails in cache mode of Outlook. This is because these emails have been correctly cached to the local OST file before moving to the server. But OWA accesses the mailbox of database directly from the server, so if the mails are not on the server, they will not be displayed in OWA. If you want to keep these mails, you can export them into PST files via Outlook Export feature.  Export emails, contacts, and calendar items to Outlook using a .pst file - Microsoft Support
