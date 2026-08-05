---
title: "Can't access Public Folders after Exchange 2019 CU 14 update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1602282/cant-access-public-folders-after-exchange-2019-cu
question_id: 1602282
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Can't access Public Folders after Exchange 2019 CU 14 update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1602282/cant-access-public-folders-after-exchange-2019-cu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We upgraded both our Exchange 2019 CU13 servers to CU14 a week ago. One server houses our user mailbox database, the other houses the System database, including our Public Folder mailbox. There are no other Exchange servers in our network.
Everything seemed to go smoothly, and mail has been flowing as it should all week.
Yesterday, it was brought to my attention that no one could find or access any of our Public Calendars. Pulling up EAC/Public Folders gives: "No public folders exist in this organization."
When I type Get-MailboxStatistics -Database "DB2" | Select DisplayName, ItemCount, TotalItemSize | Sort-Object TotalItemSize -Descending in EMS, it does show our Public Folder mailbox with an item count of 9,781 items.
I've tried Get-Mailbox -Database DB2 -PublicFolder | New-MoveRequest -TargetDatabase DB1 to move it to the other server, but that does nothing. I've also tried unmounting and remounting the database, to no avail.
Any ideas on how I can make the Public Folder mailbox visible to Exchange again?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-02-28*

I wonder if Extended Protection broke something.
I would open a ticket with Microsoft support.
