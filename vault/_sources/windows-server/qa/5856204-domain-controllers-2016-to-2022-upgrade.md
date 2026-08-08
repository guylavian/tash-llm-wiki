---
title: "Domain controllers 2016 to 2022 upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5856204/domain-controllers-2016-to-2022-upgrade
question_id: 5856204
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Domain controllers 2016 to 2022 upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5856204/domain-controllers-2016-to-2022-upgrade (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,

We are planning to upgrade domain controllers from 2016 to 2022, we already have few servers running with 2022 so there is no schema upgrade required . but only concern or doubt for me here is about the TLS version, I believe 2022 TLS 1.0 and 1.1 will be disabled by default there are few apps which are relying on tls 1.1 and they are about to migrate that as well but this will take some time and we cannot hold the upgrade.  In this case if we enable tls 1.1 and 1.0 via registry will it support in 2022?

Hope 2022 wont support SMB 1.0 also and it will be disabled by default.

Also is there any command to check the TLS enabled versions in the server?

## Answer (community) — community member

*upvotes: 0 · updated: 2026-04-09*

Windows Server 2022 supports TLS 1.0 and 1.1, but these legacy protocols are being disabled by default in more recent Windows builds and are considered insecure.

-  TLS 1.0/1.1 support on Windows Server 2022

-  TLS 1.0 and 1.1 are deprecated but can still be re‑enabled on supported Windows versions, including Server 2022, via registry configuration.

-  To override the system default and enable TLS 1.0 or 1.1, set the `Enabled` DWORD to `1` under the SCHANNEL protocol keys, for example:

-  TLS 1.0 client and server:

```
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client]
        "Enabled" = dword:00000001
    [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server]
        "Enabled" = dword:00000001
```

-  TLS 1.1 client and server similarly under `Protocols\TLS 1.1\Client` and `...\Server`.

-  This re‑enables TLS 1.0/1.1 system‑wide for SCHANNEL on Server 2022, so legacy apps depending on these protocols can continue to connect while the migration is completed.

-  Direct registry editing is risky; Group Policy or other management tools are recommended where possible.

-  Security and fallback behavior

-  Microsoft recommends removing dependencies on TLS 1.0 and 1.1 and using TLS 1.2 or higher wherever possible.

-  Legacy TLS may be removed entirely in future releases, so this should be treated as a temporary compatibility measure.

-  SMB 1.0 on Windows Server 2022

-  The provided context does not explicitly describe SMB 1.0 behavior on Windows Server 2022, so no statement can be made here based on the available information.

-  Checking which TLS versions are enabled

-  The context does not provide a specific command‑line tool or command to list enabled TLS protocol versions.

-  Enabled protocols are controlled via SCHANNEL registry keys and, for WinHTTP/WinINet scenarios, via Internet Options and Group Policy:

-  Internet Options → Advanced tab → scroll to the TLS settings to see which protocols are enabled for WinINet/Internet Explorer–based components.

-  Group Policy: `Local Computer Policy` → `Computer Configuration` or `User Configuration` → `Administrative Templates` → `Windows Components` → `Internet Explorer` → `Internet Control Panel` → `Advanced Page` → Turn off encryption support. This policy can enforce which TLS versions are used for those components.

-  Important registry paths related to TLS behavior for WinHTTP include:

-  `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\winhttp\ForceDefaultSecureProtocols`

-  `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\winhttp\EnableInsecureTlsFallback`
    These control default secure protocols and whether fallback to TLS 1.0/1.1 is allowed for WinHTTP‑based applications.

In summary, Windows Server 2022 can still support TLS 1.0 and 1.1 if explicitly re‑enabled via SCHANNEL registry settings, but this should be used only as a temporary compatibility step while applications are migrated to TLS 1.2 or higher.

References:

-  TLS 1.0 and TLS 1.1 deprecation in Windows

-  KB5017811—Manage Transport Layer Security (TLS) 1.0 and 1.1 after default behavior change on September 20, 2022

-  Resources for deprecated features

-  Enable support for TLS 1.2 in your environment for Microsoft Entra TLS 1.1 and 1.0 deprecation
