---
title: "How to fix the Weak SSL/TLS Key Exchange on port 1433 for Windows Server 2012 with SQL Server 2014?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1421758/how-to-fix-the-weak-ssl-tls-key-exchange-on-port-1
question_id: 1421758
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# How to fix the Weak SSL/TLS Key Exchange on port 1433 for Windows Server 2012 with SQL Server 2014?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1421758/how-to-fix-the-weak-ssl-tls-key-exchange-on-port-1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Our server system is old, but we are not allowed to update the OS.

The OS is Windows Server 2012, SQL Server 2014 is also installed on the server, and we were detected by Qualys to have a vulnerability problem in the system: Weak SSL/TLS Key Exchange, port 1433/tcp over SSL.

We tried to set the "SSL Config Settings" in gpedit.msc, and changed the value to the following, but there is still the vulnerability on port1433.

TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256_P256,TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256_P256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256_P256,TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA_P256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA_P256,TLS_RSA_WITH_AES_128_CBC_SHA256,TLS_RSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384_P384,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384_P384,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_P256,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA_P256,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA_P256,TLS_RSA_WITH_AES_256_CBC_SHA256,TLS_RSA_WITH_AES_256_CBC_SHA

How should I set the required KEY value? like long enough?

The vulnerability information is as follows:

Weak SSL/TLS Key Exchange， port 1433/tcp over SSL

THREAT:

QID Detection Logic:

For a SSL enabled port, the scanner probes and maintains a list of supported SSL/TLS versions. For each supported version, the scanner does a

SSL handshake to get a list of KEX methods supported by the server. It reports all KEX methods that are considered weak. The criteria of a weak

KEX method is as follows:

The SSL/TLS server supports key exchanges that are cryptographically weaker than recommended. Key exchanges should provide at least 112 bits

of security, which translates to a minimum key size of 2048 bits for Diffie Hellman and RSA key exchanges.

IMPACT:

An attacker with access to sufficient computational power might be able to recover the session key and decrypt session content.

SOLUTION:

Change the SSL/TLS server configuration to only allow strong key exchanges. Key exchanges should provide at least 112 bits of security, which

translates to a minimum key size of 2048 bits for Diffie Hellman and RSA key exchanges.

Best Regards,

David

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-11-10*

Hello David.

Maybe you could check the TLS configuration and change it from within the Windows Registry: read the article at https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/security/enable-tls-1-2-server.

Bye.
