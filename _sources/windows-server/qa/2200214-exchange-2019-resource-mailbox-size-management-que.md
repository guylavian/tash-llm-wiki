---
title: "Exchange 2019 resource mailbox size management questions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2200214/exchange-2019-resource-mailbox-size-management-que
question_id: 2200214
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# Exchange 2019 resource mailbox size management questions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2200214/exchange-2019-resource-mailbox-size-management-que (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings,

I run an exchange 2019 server on-premise for my organization.  We are currently setting up resource mailboxes to manage equipment such as vehicle checkouts.  When I manage a normal user mailbox, there is a menu option called "mailbox usage" that shows me the current usage of the mailbox, and more options that can be expanded to set the quota for that user's mailbox.  However, this option is missing for resource mailboxes.

How can I determine the current usage of a resource mailbox?

How can I set the quota on a resource mailbox?

Do all resource mailboxes share they same quota, or can they be independently sized?

Thank you,

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-30*

Greetings Neuvi,

Thank you for the shell command, that worked.  Sadly, the data is not displayed in the management console, the right info panel is mostly blank, but the command line provided the info I need.

Here is the response I received from the command:

```
ProhibitSendQuota            : Unlimited
ProhibitSendReceiveQuota     : Unlimited
RecoverableItemsQuota        : 30 GB (32,212,254,720 bytes)
RecoverableItemsWarningQuota : 20 GB (21,474,836,480 bytes)
CalendarLoggingQuota         : 6 GB (6,442,450,944 bytes)
IssueWarningQuota            : Unlimited
RulesQuota                   : 256 KB (262,144 bytes)
ArchiveQuota                 : 100 GB (107,374,182,400 bytes)
ArchiveWarningQuota          : 90 GB (96,636,764,160 bytes)
```

If the Quota says "Unlimited" is the mailbox size truly unlimited, or is there a hard-coded limit?
