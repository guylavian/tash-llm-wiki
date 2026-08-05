---
title: "Enabling \"Send NTLMv2 Response only. Refuse LM & NTLM\" Settings in Domain Controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1041325/enabling-send-ntlmv2-response-only-refuse-lm-ntlm
question_id: 1041325
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Enabling "Send NTLMv2 Response only. Refuse LM & NTLM" Settings in Domain Controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1041325/enabling-send-ntlmv2-response-only-refuse-lm-ntlm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,     

Could you help to advise on below GPO setting. What will be the impact after enable this setting?    

Enabling "Send NTLMv2 Response only. Refuse LM & NTLM" Settings in Domain Controllers

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-10*

Hi,    

The following link outlines the different options for this GPO:    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-lan-manager-authentication-level    

Here's what it says:    

Client devices use NTLMv2 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers refuse to accept LM and NTLM authentication, and they'll accept only NTLMv2 authentication.    

--------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
