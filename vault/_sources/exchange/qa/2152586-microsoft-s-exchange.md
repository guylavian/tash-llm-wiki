---
title: "Microsoft’s Exchange & @hotmail.com / @outlook.com domains Spam problem."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2152586/microsoft-s-exchange-@hotmail-com-@outlook-com-dom
question_id: 2152586
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Microsoft’s Exchange & @hotmail.com / @outlook.com domains Spam problem.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2152586/microsoft-s-exchange-@hotmail-com-@outlook-com-dom (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The email sent from a Microsoft’s Windows virtual machine using an application written in Microsoft’s Visual Studio and using the Microsoft’s SMTP server received at @yahoo.com and @googlemail.com, but it didn't even end up in the Junk Email at Microsoft’s email addresses @hotmail.com and @outlook.com.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-22*

查看 SMTP 服务器日志：检查 SMTP 服务器上的日志，查看向 Hotmail 或 Outlook 地址发送邮件时是否有任何错误或退回。
