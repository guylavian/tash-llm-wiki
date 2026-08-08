---
title: "Managed identity is exchange administrator but can't HiddenFromAddressListsEnabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1188129/managed-identity-is-exchange-administrator-but-can
question_id: 1188129
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Managed identity is exchange administrator but can't HiddenFromAddressListsEnabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1188129/managed-identity-is-exchange-administrator-but-can (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to migrate from a runas account in Azure Automation to a managed identity. I have followed the instructions on   

this page. and I can convert a mailbox to shared successfully, but I can't run

Set-Mailbox "$mailbox" -HiddenFromAddressListsEnabled $true

without getting the following error.

what am I missing? thanks.

```
|Microsoft.Exchange.Data.Directory.InsufficientPermissionsException|Source server:TY0PR0101MB4562.apcprd01.prod.exchangelabs.com doesn't have write permission to tar

Active directory response: 00002098: SecErr: DSID-031514A0, problem 4003 (INSUFF_ACCESS_RIGHTS), data 0
```

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-10*

Hi @Scott Holland  ,

Please make sure you were using the primary .onmicrosoft.com domain for your organization as the value of the `Organization` parameter when connecting to Exchange Online Powershell.

Below is a thread which discusses a similar error message for reference:

Cannot run set-casmailbox in O365 with App Registration

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
