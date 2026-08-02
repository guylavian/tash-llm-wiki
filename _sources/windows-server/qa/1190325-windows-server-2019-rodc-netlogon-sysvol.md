---
title: "Windows server 2019 作为RODC， 缺少netlogon、sysvol共享"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190325/windows-server-2019-rodc-netlogon-sysvol
question_id: 1190325
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Windows server 2019 作为RODC， 缺少netlogon、sysvol共享

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190325/windows-server-2019-rodc-netlogon-sysvol (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

RODC 域控无netlogon、sysvol共享，告警如下

```
PS C:\Windows\system32> dcdiag /q
         警告: 当我们尝试访问 test-12 时，DsGetDcName 返回了 \\test-01 的信息。
         服务器没有响应或被认为不适合。
         ......................... test-12  没有通过测试 Advertising
         无法连接到 NETLOGON 共享! (\\test-12 \netlogon)
         [test-12 ] net use 或 LsaPolicy 操作失败，错误为 67，找不到网络名。。
         ......................... test-12 没有通过测试 NetLogons
         发生了一个错误事件。EventID: 0x00000422
            生成时间: 03/16/2023   20:46:06
            事件字符串:
            处理组策略失败。Windows 尝试从域控制器读取文件 \\*****\SysVol\*****\Policies\{E53F4F79-EBED-464D-849D-7********}\gpt.ini，但是没有成功。只有解决此事件后才会应用组策略设置。该问题可能是暂时的，并可能由下列一个或多个 原因引起:
         ......................... test-12 没有通过测试 SystemLog
```

## Answers

_No answers on this thread._
