---
title: "What is ExchangePublishedUser?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2126037/what-is-exchangepublisheduser
question_id: 2126037
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# What is ExchangePublishedUser?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2126037/what-is-exchangepublisheduser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I'm checking calendar permissions for a user in Exchange Online and get this output.

Those listed as ExchangePublishedUser are no longer active accounts (shared and unlicensed).

Why they are listed in the calendar permissions list and how to get rid of them?

```
PS C:\WINDOWS\system32> Get-MailboxFolderPermission -Identity "******@company.com:\Calendar" | ft User,AccessRights

User                                                     AccessRights                           
----                                                     ------------                           
Default                                                  {AvailabilityOnly}                     
Anonymous                                                {None}                                 
******@company.com                  {AvailabilityOnly}                     
******@company.com                    {AvailabilityOnly}                      Michael Fox                                              {ReadItems, CreateItems, FolderVisible}
Peter Pan                                                {PublishingEditor}
```

## Answers

_No answers on this thread._
