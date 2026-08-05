---
title: "exchange升级后Outlook弹窗"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1770142/exchange-outlook
question_id: 1770142
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange升级后Outlook弹窗

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1770142/exchange-outlook (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

您好

近期将客户exchange由2016升级到了2019。原来采用了exchange01.abc.com和exchange02.abc.com的地址。虚拟目录，外部url是mail.abc.com，内部url是exchange01.abc.com和exchange02.abc.com。

升级后服务器名称为exchange03.abc.com和exchange04.abc.com的地址，虚拟目录，外部url是mail.def.com.cn，内部url是mail.def.com.cn。使用公网验证证书*.def.com.cn。

使用Outlook连接后，每次启动都会弹窗，显示证书不匹配，outlook有连接到exchange03.abc.com和exchange04.abc.com的地址

这个问题该如何排查

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-27*

您好 @连国 于，

欢迎来到微软论坛。

根据您的描述，在升级到Exchange2019后，登陆Outlook会显示证书不匹配警告的弹窗。

我建议您按照以下步骤来排查问题：

1.重新建立一个profile，强制Outlook使用新的配置文件。因为，刚升级到Exchange2019，可能客户端的旧缓存依然存在，会导致无法匹配新的URL。

2.Ctrl+鼠标右键点击outlook选择Test Email AutoConfiguration...

选择Use Autodiscover，点击Test按钮查看所有URL是否设置正确。

3.在DNS Manager中查看DNS中的URL是否都配置正确。

如果答案有帮助，请点击“接受答案”并投赞成票。如果您对此答案有其他疑问，请点击“评论”。
