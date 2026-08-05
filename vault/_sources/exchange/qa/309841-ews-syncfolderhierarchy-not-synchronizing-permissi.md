---
title: "EWS SyncFolderHierarchy not synchronizing permission changes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/309841/ews-syncfolderhierarchy-not-synchronizing-permissi
question_id: 309841
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# EWS SyncFolderHierarchy not synchronizing permission changes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/309841/ews-syncfolderhierarchy-not-synchronizing-permissi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Please consider following on user mailbox -     

-  Call SyncFolderHierarchy repeatedly on msgfolderroot till no changes are returned, store sync state returned. Use EWS impersonation for access.    

-  Change permissions on one of the folder returned.    

-  Repeat step 1 with stored sync state.    

It has been noticed that folder for which permissions are changed is not being returned. Documentation does mention that this should work. This is being tried on an Exchange Online mailbox.

## Answers

_No answers on this thread._
