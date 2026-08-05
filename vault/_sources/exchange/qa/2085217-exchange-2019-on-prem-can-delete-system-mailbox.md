---
title: "Exchange 2019 on prem Can delete System Mailbox?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2085217/exchange-2019-on-prem-can-delete-system-mailbox
question_id: 2085217
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 on prem Can delete System Mailbox?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2085217/exchange-2019-on-prem-can-delete-system-mailbox (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello I have at least 5 System Mailboxes but I do not know if they are used by the server.

actually I am moving some maiboxes to others DB because I want to delete the bigger one instead of shrinking, I fount that on the bigger db are stored these System Mailboxes... 

Can I delete them? or also them need to be moved to the new DB?

Thanks for your Help

Regards

Alberto

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-02*

Hi @Alberto Catagni (Fattore Digitale)  ,

Welcome to the Microsoft Q&A platform!

Based on your description, you are dealing with some system mailboxes in Exchange Server. System mailboxes, such as arbitration, monitoring, and audit log mailboxes, play a vital role in the functioning of the server. Here are what you need to know: 

-  Arbitration mailboxes: These are used for tasks such as review and approval workflows. You need to move them to the new database before you can delete the old database. 

-  Monitoring mailboxes: These mailboxes are tied to the specific database where they were created and do not need to be moved. They are automatically deleted when the database is deleted. 

-  Audit log mailboxes: These mailboxes store administrator audit logs and In-Place eDiscovery searches. Like arbitration mailboxes, they should be moved to a new database. To identify and move these mailboxes, you can use PowerShell commands. For example, to list arbitration mailboxes, you can use: 

```
Get-Mailbox -Arbitration | Format-List Name, DisplayName, Database
```

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
