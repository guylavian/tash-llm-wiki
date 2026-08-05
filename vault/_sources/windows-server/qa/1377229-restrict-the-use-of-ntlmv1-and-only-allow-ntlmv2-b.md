---
title: "Restrict the use of NTLMv1 and only allow NTLMv2, but permit NTLMv1 if the client or server does not support NTLMv2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1377229/restrict-the-use-of-ntlmv1-and-only-allow-ntlmv2-b
question_id: 1377229
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Restrict the use of NTLMv1 and only allow NTLMv2, but permit NTLMv1 if the client or server does not support NTLMv2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1377229/restrict-the-use-of-ntlmv1-and-only-allow-ntlmv2-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We want to restrict the use of NTLMv1 and only allow NTLMv2, but permit NTLMv1 if the client or server does not support NTLMv2, allowing for fallback to NTLMv1 when necessary.

In summary, the requirements are as follows:

-NTLMv2 - Allowed.

-NTLMv1 - Allowed only if NTLMv2 is not supported.

-LM - Blocked.

-Domain Controller - Should accept only NTLM and NTLMv2 authentication.

We aim to implement these requirements using the below GPO settings. What would be the ideal GPO setting to meet these requirements?

Setting number 5 appears to be quite restrictive, but it's unclear whether it will fallback to NTLMv1 if NTLMv2 is not supported.

Computer Configuration\Windows Settings\Security Settings\Local Policies\Security Options

-  "Send LM & NTLM responses" - Client devices use LM and NTLM authentication, and they never use NTLMv2 session security. Domain controllers accept LM, NTLM, and NTLMv2 authentication.

2)"Send LM & NTLM – use NTLMv2 session security if negotiated" - Client devices use LM and NTLM authentication, and they use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.

3)"Send NTLM response only" - Client devices use NTLMv1 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.

4)"Send NTLMv2 response only" - Client devices use NTLMv2 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.

5)"Send NTLMv2 response only. Refuse LM" - Client devices use NTLMv2 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers refuse to accept LM authentication, and they'll accept only NTLM and NTLMv2 authentication.

6)"Send NTLMv2 response only. Refuse LM & NTLM" - Client devices use NTLMv2 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers refuse to accept LM and NTLM authentication, and they'll accept only NTLMv2 authentication.

Thanks much.

Regards,

Raj

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-09-27*

Sounds like you'll want level 3      

Client devices use NTLMv2 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-lan-manager-authentication-level#possible-values      

 --please don't forget to close up the thread here by marking answer if the reply is helpful--
