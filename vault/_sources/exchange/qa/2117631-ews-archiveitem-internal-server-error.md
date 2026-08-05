---
title: "EWS ArchiveItem internal server error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2117631/ews-archiveitem-internal-server-error
question_id: 2117631
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# EWS ArchiveItem internal server error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2117631/ews-archiveitem-internal-server-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are using the ArchiveItem operation on a mailbox on O365 with enabled online archive. The request is identical to the one in the reference, with a real item id of course.

https://learn.microsoft.com/en-us/exchange/client-developer/web-service-reference/archiveitem-operation

The Exchange server replies with an InternalServerError:

An internal server error occurred. The operation failed., Unable to cast object of type 'Microsoft.Exchange.Services.Core.Types.MoveItemRequest' to type 'Microsoft.Exchange.Services.Core.ILegacyServiceCommandFactory'.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-12*

Hi @Simon Hain  ,

Welcome to the Microsoft Q&A platform!

According to your description, you're encountering an issue with the ArchiveItem operation in Exchange Online. The error message you're receiving, "Unable to cast object of type 'Microsoft.Exchange.Services.Core.Types.MoveItemRequest' to type 'Microsoft.Exchange.Services.Core.ILegacyServiceCommandFactory'," suggests there might be a problem with how the request is being interpreted or processed by the Exchange server. 

Here are a few steps that might help you troubleshoot and potentially resolve this issue:

-  Ensure that the request you're sending matches the expected format exactly. Even a small discrepancy could lead to errors.

-  Make sure you are using the correct version of the Exchange Web Services (EWS) API. Sometimes, mismatched versions can cause issues.

-  Ensure the account you're using has the necessary permissions to perform the ArchiveItem operation on the mailbox. Lack of proper permissions can lead to internal server errors.

-  Verify that the item IDs you are using in the request are valid and that the items actually exist in the mailbox.

-  If you have control over the Exchange Online environment, ensure that it is fully updated. Sometimes, such errors can be due to bugs that have been fixed in more recent updates.

-  Enable detailed logging of the requests and responses if possible. Sometimes, additional context from the logs can provide more insights into the root cause of the error.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
