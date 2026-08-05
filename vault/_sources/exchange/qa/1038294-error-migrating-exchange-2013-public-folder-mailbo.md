---
title: "Error migrating Exchange 2013 public folder mailbox to Exchange 2019 db"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1038294/error-migrating-exchange-2013-public-folder-mailbo
question_id: 1038294
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Error migrating Exchange 2013 public folder mailbox to Exchange 2019 db

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1038294/error-migrating-exchange-2013-public-folder-mailbo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Ran this command.      

Get-Mailbox -PublicFolder -Server servername | New-MoveRequest -TargetDatabase DB#    

Got this result    

DisplayName         StatusDetail TotalMailboxSize           TotalArchiveSize PercentComplete    

-----------    

         ------------ ----------------           ---------------- ---------------  

PublicFolderMailbox FailedOther  461 MB (483,390,626 bytes)                  95

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-07*

Check these articles for help - https://learn.microsoft.com/en-us/exchange/troubleshoot/public-folders/public-folder-migration-fails     

https://community.spiceworks.com/how_to/185867-migrate-mail-enabled-public-folders-in-hybrid-mode

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-06*

I was able to figure this out myself.  had to clean up some legacy items left over from previous migrations.      

Ran a script to identify the errors from this article.    

https://learn.microsoft.com/en-us/Exchange/collaboration/public-folders/migrate-to-exchange-online?view=exchserver-2019
