---
title: "DC diag 错误，FSMO主机角色绑定失败"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1694919/dc-diag-fsmo
question_id: 1694919
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# DC diag 错误，FSMO主机角色绑定失败

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1694919/dc-diag-fsmo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

我有 6台DC 在 操作主机角色上运行FSMO时，出现警告，其他DC运行DCDIAG时没有类似报错

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-12*

尊敬的客户，您好！  

感谢您在Q&A论坛发帖。  

请尝试以管理员身份运行这个命令看看是否还有相同的警告。  

错误 1326 通常表示尝试绑定到 LDAP 服务器的用户没有执行此操作所需的权限。

若要排查此问题，可以尝试以下步骤：

1.确保您用于运行 Dcdiag 的用户帐户具有绑定到 LDAP 服务器所需的权限。此帐户应是 Domain Admins 组的成员。

2.验证您尝试连接到的域控制器是否可用（开机并正常运行的）并响应 LDAP 请求。可以使用“ping”命令测试与域控制器的连接。

3.检查域控制器上的 DNS 设置，并确保它们正确无误。不正确的 DNS 设置可能会导致 LDAP 绑定问题。

4.检查域控制器上的防火墙设置，并确保它们不会阻止 LDAP 流量。  

希望上述的回复对您有帮助。

如有任何问题，欢迎您随时咨询我们。

Best Regards,

Daisy Zhou

============================================

如果答案有帮助，请点击“接受答案”并点赞。
