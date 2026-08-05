---
title: "Winnit Ports 6400 on Exchange server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2263027/winnit-ports-6400-on-exchange-server
question_id: 2263027
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Winnit Ports 6400 on Exchange server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2263027/winnit-ports-6400-on-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have run an external scan on my environment and we find that port 6400 is listening on our exchange server for the wininit process is this a normal operation / process

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-05-06*

Hi Kenneth Salcedo,

Thank you for posting your question in the Microsoft Q&A forum.

Based on my research, Microsoft's genuine "wininit.exe" should reside in "C:\Windows\System32". It is a critical system process, an essential Windows file and not to be removed.

You could check suggestions in the following link to confirm if that "wininit.exe" listening port 6400 is genuine:

The process wininit.exe (127.0.0.1) has initiated the restart of computer - Microsoft Q&A

Additionally, please understand that our “Exchange Server Management” tag mainly focus on issues related to managing and using Exchange server features and daily work.  Wininit.exe related issues are more relevant to windows server side, if you need further assistance for Wininit process, you can post questions under “Windows server” related tags.

Thanks for your understanding.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
