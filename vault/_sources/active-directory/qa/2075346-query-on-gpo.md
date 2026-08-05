---
title: "Query on GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2075346/query-on-gpo
question_id: 2075346
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Query on GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2075346/query-on-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All

I have a requirement to enable the GPOs listed below on Windows Servers (2022/2019/2016). What could be the possible impact of applying these GPOs? Please guide me as i am not sure.

```
Network security: Force logoff when logon hours expire-->Enabled
Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Network security: Force logoff when logon hours expire

Network security: LAN Manager authentication level-->Send NTLMv2 response only
Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Network security: LAN Manager authentication level

Network security: Minimum session security for NTLM SSP based (including secure RPC) clients-->Require NTLMv2 session security, Require 128-bit encryption
Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Network security: Minimum session security for NTLM SSP based (including secure RPC) clients

Network security: Minimum session security for NTLM SSP based (including secure RPC) servers-->Require NTLMv2 session security, Require 128-bit encryption
Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Network security: Minimum session security for NTLM SSP based (including secure RPC) servers
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-23*

Thanks alot. Before marking as answer can you please help me on the below two gpos

```
Network security: Restrict NTLM: Audit Incoming NTLM Traffic:Enable auditing for all accounts

Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Network security: Restrict NTLM: Audit Incoming NTLM Traffic

Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers:Audit all or higher

Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Restrict NTLM: Outgoing NTLM traffic to remote servers
```
