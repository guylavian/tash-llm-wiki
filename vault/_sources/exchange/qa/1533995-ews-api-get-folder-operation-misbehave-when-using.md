---
title: "ews api get folder operation misbehave when using email alias"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1533995/ews-api-get-folder-operation-misbehave-when-using
question_id: 1533995
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-development-routing-development-other", "m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-development", "office-exchange-other-l1"]
---
# ews api get folder operation misbehave when using email alias

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1533995/ews-api-get-folder-operation-misbehave-when-using (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an outlook licensed account whose mailbox is A, and it's alias mailbox is set as B. Moreover, we have an unlicensed mailbox with same name B. When we use GetFolder operation with impersonation being A and mailbox being B, we can get the archive message folder root of A. However, if we use it with impersonation being B, then we'll get access denied. Is it possible that B is incorrectly linked to A? In our opinion, it should simply show mailbox not enabled or not found error instead of the access denied error.
Thank you~!

## Answers

_No answers on this thread._
