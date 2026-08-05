---
title: "Cannot create file share witness for Exchange 2019 DAG. getting error Element not found."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190476/cannot-create-file-share-witness-for-exchange-2019
question_id: 1190476
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Cannot create file share witness for Exchange 2019 DAG. getting error Element not found.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190476/cannot-create-file-share-witness-for-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have tried creating the file share witness with Exchange powershell and failover cluster manager. The folder and share was created,  but then I get the error "Unable to save property changes for 'File Share Witness'. Element not found."

Both the exchange trusted subsystem and cluster account have full access

I can access the share from both servers.

The FailoverClustering  Diagnostic log has the errors below.

[RES] File Share Witness <File Share Witness>: Failed to open the core NetName resource, error 1168.

[RES] File Share Witness <File Share Witness>: Failed to retrieve the virtual server token from the core netname resource with 1168.

[RES] File Share Witness <File Share Witness>: Validation of input property buffer failed, error 1168.

I have not found any documentation that deals with the error "Element not found".

## Answers

_No answers on this thread._
