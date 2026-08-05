---
title: "outlook exchange模式 数据文件位置为 online （office版本 2016）"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1397619/outlook-exchange-online-office-2016
question_id: 1397619
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# outlook exchange模式 数据文件位置为 online （office版本 2016）

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1397619/outlook-exchange-online-office-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

通过使用 office 2016 设定outlook exchange模式时

注册可以成功

邮件收发正常

问题1：但是无法将接收到的邮件移动到本地（会出现报错：报错内容：邮件已删除，或已经移动）

问题2：数据文件位置并非本地地址，而现实为online

问题3：数据文件-设置-高级-使用缓存exchange模式  功能无法使用（默认灰色）

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-24*

你好，非常感谢给予帮助

如上述步骤进行操作，无法对3.在“脱机设置”下，选中“使用缓存 Exchange 模式”。 进行勾选（状态为灰色）

追加测试的内容

1.用同一个账号，在其他PC进行outlook设定时，可正常使用

怀疑PC 某个配置是否异常

2.outlook重启配置，office重新安装，都无效

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-23*

你好 @WENCHENG CUI  ，

欢迎来到我们的论坛，

根据我的经验，问题1和2都是因为问题3没有启用缓存模式导致的。

根据您的描述，您在 Outlook 中无法使用“数据文件-设置-高级-使用缓存 Exchange 模式”功能，因为该选项默认为灰色。这可能是由于您的 Exchange 管理员已禁用此功能所致。

此外，如果你想启用Exchange 缓存模式，请按照以下步骤操作：

-  单击“文件” > “帐户设置” > “帐户设置”。

-  单击“Exchange”或“Microsoft 365”，然后单击“更改”。

-  在“脱机设置”下，选中“使用缓存 Exchange 模式”。

-  退出，然后重启 Outlook。

如果还是不行，请移除问题Outlook账号并尝试重新添加看是否生效。

此致，

Jarvis Sun

如果以上回复对您有所帮助，请不要忘记将其“标记为答案”. 如果有任何问题，请在这里告知我们。
