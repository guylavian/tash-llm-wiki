---
title: "UploadItems EWS operation does not work properly for public folders."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/282932/uploaditems-ews-operation-does-not-work-properly-f
question_id: 282932
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# UploadItems EWS operation does not work properly for public folders.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/282932/uploaditems-ews-operation-does-not-work-properly-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Perform the following on an Exchange Online deployment -  

-  Create a Primary and Secondary public folder mailbox, with a folder on each of the mailbox. Powershell will have to be used to create such a folder.  

-  Using impersonated access, download items using ExportItems EWS operation. Make sure to use a user which has its PublicFolderInformation property (from GetUserSettings operation) configured to secondary public folder mailbox.  

-  Use a post from the folder on the primary mailbox to call the UploadItems EWS operation with the UpdateOrCreate operation.  

It has been noticed that a duplicate post is created for such an item, even if a post with the same id is present in that folder. Calling with "Update" instead of "UpdateOrCreate" fails with "item not found" error.  

Making a GetItem EWS call with same id returns that item.  

Server Version Info returned  

MajorVersion="15"   

MinorVersion="20"   

MajorBuildNumber="3868"   

MinorBuildNumber="33"   

Version="V2018_01_08"  

Can someone let me know, what could be wrong?

## Answers

_No answers on this thread._
