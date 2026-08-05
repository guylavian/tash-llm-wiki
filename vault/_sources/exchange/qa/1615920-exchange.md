---
title: "Exchange中发往通讯组的邮件默认是多久失效，我应如何查看和修改？"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1615920/exchange
question_id: 1615920
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange中发往通讯组的邮件默认是多久失效，我应如何查看和修改？

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1615920/exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange2019中发往通讯组的邮件默认是多久失效，现在好像是3天未审批会失效退信，我应如何查看现在是设置了多久失效，如果需要修改应如何操作？谢谢。

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-13*

Hi @ting wang   

默认情况下，Exchange 2019中发往通讯组的邮件失效时间为2天。

https://learn.microsoft.com/zh-cn/exchange/mail-flow/queues/message-intervals?view=exchserver-2019#configuration-options-for-message-expiration

您可以尝试通过打开Exchange管理控制台，进入“组织配置”部分，然后选择“传输设置”选项卡，再双击“消息过期”来查看或更改此设置。

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
