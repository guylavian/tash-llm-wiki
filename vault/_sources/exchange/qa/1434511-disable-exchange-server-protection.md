---
title: "Disable Exchange Server protection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1434511/disable-exchange-server-protection
question_id: 1434511
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# Disable Exchange Server protection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1434511/disable-exchange-server-protection (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Exchange Server 365 Online with custom mail spam protection.   

How to disable a default Exchange Server email protection to make it stop sending emails to Junk folder or to quarantine mailbox?

Till now I found the following commands in powershell:

```
Disable-HostedContentFilterRule $name
Disable-AntiPhishRule $name
Disable-MalwareFilterRule $name
Disable-SafeAttachmentRule $name
Disable-SafeLinksRule $name
```

Is it enough?   

The problem is that the default rules cannot be disabled.   

Is there any better solution for it?

## Answers

_No answers on this thread._
