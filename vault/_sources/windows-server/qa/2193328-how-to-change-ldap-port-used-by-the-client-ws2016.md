---
title: "How to change LDAP port used by the client(WS2016)?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193328/how-to-change-ldap-port-used-by-the-client-ws2016
question_id: 2193328
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-networking-other"]
---
# How to change LDAP port used by the client(WS2016)?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193328/how-to-change-ldap-port-used-by-the-client-ws2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone

We have application from Cisco running on windows server 2016. This application is leveraging Active directory(AD) on the domain controller(DC).

The application is using the non-secure LDAP port 389 to communicate with the AD. We have a requirement to change the port used to 636 which is the secure one.

On AD server, the port 636 is opened and the CA certificate is implemented already. I contacted the application vendor(Cisco) and they said that this configuration should be made on the windows level and the application doesn't expose any option to change the LDAP port number.

How we can make the application server(client) use the port 636 instead of the port 389 to communicate with the AD server? is that done from the registry or group policy? much appreciated if someone can share the detailed steps.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-24*

Thanks for your reply Zunhui. I saw that article but it doesn't show how to make the client using the secure LDAP port 636 to communicate with LDAP server.

Is there any MS documentation in this regards?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-24*

Hello,

The LDAP is used to read from and write to Active Directory. By default, LDAP traffic is transmitted unsecured. You can make LDAP traffic confidential and secure by using SSL/Transport Layer Security (TLS) technology. Then listen on port 636 on the client. For details, you can refer to the following link:

Enable Lightweight Directory Access Protocol (LDAP) over Secure Sockets Layer (SSL) - Windows Server | Microsoft Learn

Best Regards

Zunhui
