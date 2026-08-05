---
title: "Public Folder Migration Issue (Exchange 2013 to Exchange Online)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1159188/public-folder-migration-issue-exchange-2013-to-exc
question_id: 1159188
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Public Folder Migration Issue (Exchange 2013 to Exchange Online)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1159188/public-folder-migration-issue-exchange-2013-to-exc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi There

I'm having a problem migrating Public Folders from Exchange 2013 to Exchange Online. Following the guide here:
https://learn.microsoft.com/en-us/exchange/collaboration/public-folders/migrate-to-exchange-online?view=exchserver-2019

I ran the sourcesidevalidation.ps1 script first which found some public folders with invalid characters in their name. Using the command supplied by MS I renamed those folders.

When continuing through Step 3 (generating the .CSV files) I get the following error:

These are the folders that the script renamed and looks like it has moved the old ones to some sort of recycle area.

The script will not continue until these folders are renamed.

Can I either A) rename these folders here ? or B) Purge the dumpster area to get ride of them?

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-11*

I would suggest you try to connect to Exchange Online with PowerShell and check whether there exists issue with it: Basic auth - Connect to Exchange Online PowerShell (Check with prerequisites before connecting)

Suppose you could connect to Exchange online successfully. I would suggest trying again with that script.

If you cannot connect to Exchange online, I suggest you temporarily disable the firewall. Based on my search, this issue may be related to the firewall blocking the connect request.
