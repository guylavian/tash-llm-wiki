---
title: "Windows 2022 domain controller TLS 1.3 Support"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5874142/windows-2022-domain-controller-tls-1-3-support
question_id: 5874142
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Windows 2022 domain controller TLS 1.3 Support

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5874142/windows-2022-domain-controller-tls-1-3-support (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an active directory domain with Windows 2022 domain controllers.

We also have two factors authentication appliances RSA Authentication Manager 8.8 P 03.

Today, those appliances communicate successfully with our DCs in TLS 1.2.

If we turn those appliances in TLS 1.3 only, Communication fails with our DC.

Here is the result from a Nmap scan on one of those appliances: TLSv1.2:

|     ciphers:

|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (secp256r1) - A

|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (secp256r1) - A

|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (secp256r1) - A

|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (secp256r1) - A

|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A

|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A

|     compressors:

|       NULL

|     cipher preference: server

|   TLSv1.3:

|     ciphers:

|       TLS_AKE_WITH_AES_256_GCM_SHA384 (secp256r1) - A

|       TLS_AKE_WITH_AES_128_GCM_SHA256 (secp256r1) - A

How make it work with TLS 1.3 ?

## Answer (community) — community member

*upvotes: 0 · updated: 2026-04-28*

Windows Server 2022 supports TLS 1.3 at the OS level, but Active Directory domain controller protocols and many Windows authentication stacks are still based on TLS 1.2, and TLS 1.3 cannot simply be forced end‑to‑end for all AD communications.

From the information available, the reliable path is to keep TLS 1.2 enabled between the RSA Authentication Manager appliances and the Windows Server 2022 domain controllers and ensure that strong, supported TLS 1.2 cipher suites are available on both sides.

For Windows Server 2022/Windows 11, TLS 1.3 is supported, but TLS 1.2 remains the primary, broadly compatible option. Microsoft guidance for similar services (for example, Azure Front Door and Entra Private Access) is to use strong TLS 1.2 cipher suites such as:

-  TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

-  TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

These are already present in the RSA appliance’s TLS 1.2 list and are also among the recommended/supported cipher suites on Microsoft services.

To keep the setup working securely:

-  Leave TLS 1.2 enabled on the RSA appliances and domain controllers.

-  Ensure that at least one of the strong ECDHE+AES‑GCM TLS 1.2 cipher suites is enabled and prioritized on the Windows Server 2022 DCs (for example via Group Policy or the OS cipher configuration), matching what the appliance offers.

-  Avoid aggressively disabling TLS 1.2 or narrowing cipher suites until connectivity is confirmed stable, as overly strict cipher policies can cause “no common algorithm” or handshake failures.

There is no supported configuration in the provided material that allows enforcing TLS 1.3‑only between these RSA appliances and Windows Server 2022 domain controllers; the supported and recommended approach is strong TLS 1.2 with modern cipher suites.

References:

-  TLS 1.3 support

-  TLS encryption with Azure Front Door (front-door-standard-premium)

-  Ciphers for Microsoft Entra Private Access

-  Transport Layer Security (TLS) connections might fail or timeout when connecting or attempting a resumption

-  TLS requirement for SQL Server - Microsoft Q&A
