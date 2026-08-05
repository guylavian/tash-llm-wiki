---
title: "Exchange服务器报ID74的错误"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1636130/exchange-id74
question_id: 1636130
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange服务器报ID74的错误

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1636130/exchange-id74 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

您好

近期发现Exchange服务器上出现ID为74的报错，想了解是什么原因导致

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-02*

你好，

                请问实际工作中是否遇到什么问题？

 

              这个报错的原因是 Exchange服务器上检测到了一个连接泄露，关联到进程w3wp.exe, PID 18156的客户端连接（可能是一个与分配角色或权限相关的操作）没有正确关闭，可能会导致资源耗费。

 

建议您先尝试重新连接、关闭任何不必要的后台任务或进程（也考虑重启Exchange服务器）

 

如果没有解决问题，请：

1.审查与“项目临时管理员”角色相关的权限，确保没有过时的权限或者非法访问，再检查一下最近是否有相关权限更改。如果确实和特定的角色或权限设置有关，建议重新配置权限或撤销相关更改。重启Exchange服务器。

2.检查w3wp.exe的资源使用情况。右键点击任务栏的空白区，选择“任务管理器”。在左侧导航栏中，展开“进程”节点，找到名为“w3wp.exe”的进程。右键单击“w3wp.exe”，选择“属性”。在性能标签页中，可以看到该进程的CPU、内存、磁盘和网络使用情况，如果w3wp.exe占据的内存在持续增加，说明可能存在内存泄露。如果存在内存泄露，请告知我。

 

如果仍然没有解决问题，请检查Exchange的日志文件并截图给我（日志文件的默认地址在exchange服务器上的C:\Program Files\Microsoft\Exchange Server\V15\Logs）。

 

 

注意：这里是公开论坛，请注意隐藏隐私信息，比如域名
