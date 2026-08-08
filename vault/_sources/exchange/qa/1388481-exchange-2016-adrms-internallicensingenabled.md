---
title: "exchange 2016集成ADRMS功能时，修改InternalLicensingEnabled状态时报错"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1388481/exchange-2016-adrms-internallicensingenabled
question_id: 1388481
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange 2016集成ADRMS功能时，修改InternalLicensingEnabled状态时报错

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1388481/exchange-2016-adrms-internallicensingenabled (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

执行的命令

Set-IRMConfiguration -InternalLicensingEnabled $true

具体报错

```
请求因 HTTP 状态 401 失败: Unauthorized。 ---> 从 https://win-k8o1hngkiol.test.com/_wmcs/certification/server.asmx 获取
服务器信息失败。
    + CategoryInfo          : InvalidOperation: (:) [Set-IRMConfiguration]，Exception
    + FullyQualifiedErrorId : [Server=WIN-K8O1HNGKIOL,RequestId=9eae45f5-051b-4b04-9975-c7811d86f614,TimeStamp=2023/10
   /11 8:14:13] [FailureCategory=Cmdlet-Exception] CC7E8B18,Microsoft.Exchange.Management.RightsManagement.SetIRMConf
  iguration
    + PSComputerName        : win-k8o1hngkiol.test.com
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-12*

您好 @ 龚德沨，

很高兴得知您已找到解决方案并感谢您将其分享出来。

由于Microsoft问答社区有一项政策，即“问题作者不能接受自己的答案。他们只能接受别人的回答。“根据这里介绍的场景：Answering your own questions on Microsoft Q&A，我会对这个线程做一个简短的总结：

问题症状：

在exchange 2016和ADRMS 集成后，无法运行Set-IRMConfiguration

并得到以下报错：

```
请求因 HTTP 状态 401 失败: Unauthorized。 ---> 从 https://win-k8o1hngkiol.test.com/_wmcs/certification/server.asmx 获取服务器信息失败。
```

解决方案：

IIS管理器中身份验证方式启用内核模式身份认证。

您可以单击此摘要的“接受答案”按钮以关闭此线程，这可以使其他社区成员在阅读此线程时更容易看到有用的信息。

感谢您的操作~

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-12*

找到问题了，IIS管理器中身份验证需要启用内核模式身份认证
