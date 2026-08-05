---
title: "GPO password strategy half working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1393299/gpo-password-strategy-half-working
question_id: 1393299
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO password strategy half working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1393299/gpo-password-strategy-half-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Hi,

Let me explain my problem :

I created a GPO "password strategy" which applies to a test session (before deployment on all workstations) which aims to strengthen password security on local sessions.

On my test PC I can clearly see the GPO which applies with the Gpresult command and in the group policy settings on the test PC I have the same settings as in my GPO so everything is OK in terms of rights and security. priority of the GPO.

However when I do a "net user test" on my DC server it tells me a password duration of 40 days instead of 90 defined in the GPO and a minimum password duration of 1 days instead of 0 days on my GPO.

I've looked everywhere but can't see where its settings apply (no local gpo and no other gpo with password parameter).

So i'm here asking for help please :)

Have a good day,
```

## Answers

_No answers on this thread._
