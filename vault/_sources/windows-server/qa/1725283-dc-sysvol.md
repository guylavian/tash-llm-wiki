---
title: "删除DC上失败的sysvol共享目录"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1725283/dc-sysvol
question_id: 1725283
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# 删除DC上失败的sysvol共享目录

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1725283/dc-sysvol (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

您好

近期发现域中的SYSVOL目录多出来几个复制失败的。检查发现这里面包含的域控是很早之前就故障删除的域控服务器。

如何将这些报错的目录从现有的域环境中删除？

仍然残留这些信息是否是因为当时分支域控服务器在清除时未清理干净？

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-06-25*

你好，下图，我这边的操作系统是server2019

中间位置红色X的失败复制，如何删除

另外如何对SYSVOL进行备份
