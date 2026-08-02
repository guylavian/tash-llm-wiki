---
title: "Unified Messaging Exchange server 2016 issue..."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/190506/unified-messaging-exchange-server-2016-issue
question_id: 190506
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Unified Messaging Exchange server 2016 issue...

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/190506/unified-messaging-exchange-server-2016-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Unified Messaging can't validate or generate a UM PIN for mailbox 'mailbox@keyman  .com' : An error occurred    

while accessing the user's mailbox. Details: The underlying connection was closed: An unexpected error occurred on a    

receive.    

This issue started recently not exactly sure when. We are running Exchange 2016 CU18    

I cannot view the UM details for any UM enabled user in EAC. I also cannot enable or disable UM for any user.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-09*

Problem with all mailboxes.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-09*

Hi @Ivan R  ,    

Have you checked the state of the arbitration mailbox? Is it happening to specific mailbox or all mailbox?    

Can you check for events MSExchange Unified Messaging to find out the inner exception?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-09*

Hi @Anonymous   ,  

Have you made any changes to related settings recently?  

1.Please check to see if “SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}” exists. According to my understanding, this system mailbox used by Unified Messaging in Exchange 2016 for storing UM console attending files and other information.  

For more information you could refer to: Arbitration mailboxes  

2.Please try to run the following command to check if you could view the detail information of UM:

```
Get-UmMailbox -Identity <> | fl
```

3.Please try to run the following command to enable the UM for user:

```
Enable-UMMailbox -Identity <> -UMMailboxPolicy <> -Extensions <>
```

In addition, please try to reproduce the issue. When the error occurs, check whether there is a related error log in the Event viewer. If it exists, please share it with us, please pay attention to is to cover your personal privacy information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
