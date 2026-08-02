---
title: "OWA打开选项，提示：There was a problem loading your options. Please try again。"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1632595/owa-there-was-a-problem-loading-your-options-pleas
question_id: 1632595
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# OWA打开选项，提示：There was a problem loading your options. Please try again。

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1632595/owa-there-was-a-problem-loading-your-options-pleas (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange Server 2016 CU23的环境，所有用户在使用OWA打开“选项”时，提示：There was a problem loading your options. Please try again，使用不同的浏览器都是这样子，什么原因导致的？应该如何处理这个问题？

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-03-27*

已经解决，这个问题跟SharingPolicy有关，使用Get-SharingPolicy查询时，发现丢失了，重新生成后恢复正常：New-SharingPolicy -Name "默认共享策略" -Domains '*: CalendarSharingFreeBusySimple' -Enabled $true -Default，但是为什么这条策略会影响到这个功能呢？有什么关联的吗？
