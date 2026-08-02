---
title: "I have installed Windows Server 2022 with kerberos authentication. We are trying to connect to this server from a java based RDP client. Connection is failing with error KRB5KDC_ERR_ETYPE_NOSUPP from server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1289486/i-have-installed-windows-server-2022-with-kerberos
question_id: 1289486
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# I have installed Windows Server 2022 with kerberos authentication. We are trying to connect to this server from a java based RDP client. Connection is failing with error KRB5KDC_ERR_ETYPE_NOSUPP from server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1289486/i-have-installed-windows-server-2022-with-kerberos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have installed Windows Server 2022 with kerberos authentication. 

We are trying to connect to this server from a java based RDP client. Connection is failing with error KRB5KDC_ERR_ETYPE_NOSUPP from server. Below is the snapshot of the network traffic.

The error is coming from server.

Screenshot of client encryption type is also attached.

AES encryption type is enabled for the user.

Is there any configuration to enable debug logging for kerberos to see what encryption types are supported on server. How to configure kerberos encryption type on Windows 2022 server.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-23*

We have this setting configured to use all encryption types.

Also this machine is a domain controller.

Even with this setting we get the same error.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-23*

Hello Sai,

Thank you for your question and for reaching out with your question today.

The following article outlines what encryption types are compatible with Kerberos:

https://learn.microsoft.com/windows/security/threat-protection/security-policy-settings/network-security-configure-encryption-types-allowed-for-kerberos

You can find what types are in use under:

Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options

If the reply was helpful, please don’t forget to upvote or accept as answer.

Best regards.
