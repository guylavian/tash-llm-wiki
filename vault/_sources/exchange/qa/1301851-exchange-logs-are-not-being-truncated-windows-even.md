---
title: "Exchange Logs are not being truncated,Windows Event Viewer - Application shows error 8007064A"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1301851/exchange-logs-are-not-being-truncated-windows-even
question_id: 1301851
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange Logs are not being truncated,Windows Event Viewer - Application shows error 8007064A

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1301851/exchange-logs-are-not-being-truncated-windows-even (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Windows Event Viewer show errors below:

The Microsoft Exchange Replication service VSS Writer (Instance 333baced-1839-4d69-b260-b2bf63c97adf) failed with error 8007064A when processing the backup completion event.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-09*

Try to modify regedit HKLM\Software\Microsoft\ExchangeServer\V14\Replay\Parameters

New DWORD , Name = EnableVSSWriter, value=0

Then Restart Exchange Replication Service.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-06-09*

Hi @xiaoding133  

Have you done a full backup of your Exchange server?

Refer to the steps in this link: Use Windows Server Backup to back up Exchange Server

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
