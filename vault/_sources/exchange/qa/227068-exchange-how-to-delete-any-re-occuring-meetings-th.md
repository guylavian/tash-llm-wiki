---
title: "Exchange how to delete  any re-occuring meetings that are booked for the future with Powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/227068/exchange-how-to-delete-any-re-occuring-meetings-th
question_id: 227068
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange how to delete  any re-occuring meetings that are booked for the future with Powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/227068/exchange-how-to-delete-any-re-occuring-meetings-th (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Delete  any re-occuring meetings that are booked for the future with Powershell

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-13*

Hi @Jayakumar Janardhanan   ,  

You could following the steps to delete the recurring meetings. Please pay attention to the following things before running the commands: By default, Search-Mailbox is available only in the Mailbox Search or Mailbox Import Export roles, and these roles aren't assigned to any role groups.You need to add both of the roles to a role group.Only the Mailbox Import Export role gives you access to the DeleteContent parameter. And run the Search-Mailbox each mailbox returns up to 10,000 results each time.  

1.Please run the following command in the Exchange Management shell to preview eligible results:

```
Get-Mailbox -ResultSize Unlimited | Search-Mailbox -SearchQuery "kind:meetings AND Subject:'' AND From:<>" –EstimateResultOnly
```

2.Then run the following command in the Exchange Management shell to delete all eligible meeting series from both the organizer mailbox and the attendees mailbox:

```
Get-Mailbox -ResultSize Unlimited | Search-Mailbox -SearchQuery "kind:meetings AND Subject:'' AND From:<>" -DeleteContent
```

For more information you could refer to: Search-Mailbox

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
