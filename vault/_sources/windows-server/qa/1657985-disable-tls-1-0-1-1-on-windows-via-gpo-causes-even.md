---
title: "Disable TLS 1.0/1.1 on Windows via GPO causes eventlog warning with 0x80004002 error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1657985/disable-tls-1-0-1-1-on-windows-via-gpo-causes-even
question_id: 1657985
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Disable TLS 1.0/1.1 on Windows via GPO causes eventlog warning with 0x80004002 error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1657985/disable-tls-1-0-1-1-on-windows-via-gpo-causes-even (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

we are using GPO for some time to disable TLS 1.0 and 1.1 on all clients and servers. This was working until lately. 

We use GPP registry settings to set those values:

```
HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server\Enabled = 0 HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server\DisabledByDefault = 1
HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server\Enabled = 0 HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server\DisabledByDefault = 1
```

Since some weeks (March patch day?) all systems report warnings in eventlog, when this GPO applies. Event 4106 from Group Policy Registry. 

This includes Windows Server 2019, 2022 or Windows 11 23H2, all on patch level April 2024.

The computer 'DisabledByDefault' preference item in the 'Security Config All Systems {xxx}' Group Policy Object did not apply because its targeting item failed with error code '0x80004002 No such interface supported' This error was suppressed.

The computer 'Enabled' preference item in the 'Security Config All Systems {xxx}' Group Policy Object did not apply because its targeting item failed with error code '0x80004002 No such interface supported' This error was suppressed.

Also we have another error code on some machines:

The computer 'Enabled' preference item in the 'Security Config All Systems {xxx}' Group Policy Object did not apply because its targeting item failed with error code '0x8007203a The server is not operational.' This error was suppressed.

When I check the registry, the registry entries exist, since they were set successfully before.

If I delete them, they are not recreated by the GPO. But I can recreate them manually. 

This only happens with the entries for TLS 1.0 and TLS 1.1. This does not happen for entries like SSL 3.0 or older protocols. 

Any ideas? Can someone reproduce this?

Best regards,

Ingo

## Answers

_No answers on this thread._
