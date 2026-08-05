---
title: "EWS API : In-Place Archive Folder Item Count Issue."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2151180/ews-api-in-place-archive-folder-item-count-issue
question_id: 2151180
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-other-l1"]
---
# EWS API : In-Place Archive Folder Item Count Issue.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2151180/ews-api-in-place-archive-folder-item-count-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

I’m working on a C# application using the Exchange Web Services API to retrieve the email count from In-Place Archive folders, including nested ones.

Here’s the code I’m using to get folder Item Count:

Microsoft.Exchange.WebServices.Data.Folder ParentFolder =  Folder.Bind(service, FolderName).Result;

Microsoft.Exchange.WebServices.Data.SearchFilter.SearchFilterCollection FilterCollection = new SearchFilter.SearchFilterCollection(LogicalOperator.Or);

FindFoldersResults FoldersResults = ParentFolder.FindFolders(FilterCollection, objFoldView).Result;

Issue: The API response successfully retrieves the folders (no errors or exceptions), but the `ItemCount` property always returns `0`. Even when attempting to retrieve emails directly using the folder ID, the result is still empty.

However, when I check the user's In-Place Archive folder and nested folders manually, emails are present.

Has anyone encountered this issue before, or is there a workaround to retrieve the correct item counts for archive folders?

Thanks,

Ritu Yadav

## Answers

_No answers on this thread._
