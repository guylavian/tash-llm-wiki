---
title: "Exchange Server2019禁用NTLMv1验证，使用NTLMv2验证"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1640120/exchange-server2019-ntlmv1-ntlmv2
question_id: 1640120
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server2019禁用NTLMv1验证，使用NTLMv2验证

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1640120/exchange-server2019-ntlmv1-ntlmv2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

您好

想对Exchange Server2019的客户端验证做调整，要求如下：

1、Exchange Server2019禁用NTLMv1验证，使用NTLMv2验证

2、如果客户端不支持NTLMv2验证，可以使用NTLMv1验证

3、禁用其他低版本的验证方式

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-02*

您好，

听起来您需要的是安全级别4，

可能的值

 

建议您先审核您的设备，保证所有设备都支持NTLMv1或是NTLMv2

第一步：审核！
