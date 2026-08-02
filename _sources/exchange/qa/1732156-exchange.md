---
title: "Exchange服务器升级迁移以后，脱机地址簿更新或重建"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1732156/exchange
question_id: 1732156
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange服务器升级迁移以后，脱机地址簿更新或重建

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1732156/exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

您好

近期将Exchange从2016升级到最新的2019版本，旧2016服务器已经卸载。

发现Outlook客户端的地址簿更新出现问题，如下图

随后检查服务器上使用get-offlineaddressbook 检查地址簿设置，发现OriginatingServer是旧2016服务器

根据以上情况，如何解决Outlook地址簿更新失败的问题？

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-26*

Hi,

欢迎来到微软论坛！

组织内所有用户都出现这个问题吗？看起来似乎是OAB无法找到新的Exchange 2019服务器导致的，您可以先检查OAB的url是否正确配置为新的2019服务器：

Get-OABVirtualDirectory

如果不正确，请通过命令正确配置它：

```
Get-OABVirtualDirectory | Set-OABVirtualDirectory -InternalUrl "https://new2019server.contoso.com/OAB" -ExternalUrl https://new2019server.contoso.com/OAB
```

有任何更新请随时与我们联系。
