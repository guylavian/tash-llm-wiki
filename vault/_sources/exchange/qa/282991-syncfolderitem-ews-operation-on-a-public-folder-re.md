---
title: "SyncFolderItem EWS operation on a public folder returns different item id for same item depending on item properties fetched"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/282991/syncfolderitem-ews-operation-on-a-public-folder-re
question_id: 282991
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# SyncFolderItem EWS operation on a public folder returns different item id for same item depending on item properties fetched

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/282991/syncfolderitem-ews-operation-on-a-public-folder-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Perform the following on an Exchange Online deployment -  

-  Create a Primary and Secondary public folder mailbox, with a folder on each of the mailbox. Powershell will have to be used to create such a folder.  

-  Using impersonated access, call SyncFolderItems EWS operation for a folder residing on the primary mailbox. Make sure to use a user which has its PublicFolderInformation property (from GetUserSettings operation) configured to secondary public folder mailbox.  

-  For the first time fetch only ids, for the second time fetch ids and subject.  

It was noticed that the ids returned for the same item differ based on the item properties fetched in the item shape attribute. The same behavior does not occur for FindItems EWS operation.  

Server Version Info returned  

MajorVersion="15"  

MinorVersion="20"  

MajorBuildNumber="3868"  

MinorBuildNumber="33"  

Version="V2018_01_08"  

Can someone let me know, what could be wrong?

## Answers

_No answers on this thread._
