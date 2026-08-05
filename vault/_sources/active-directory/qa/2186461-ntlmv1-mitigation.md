---
title: "NTLMv1 Mitigation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186461/ntlmv1-mitigation
question_id: 2186461
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# NTLMv1 Mitigation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186461/ntlmv1-mitigation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Our company in plan to mitigate NTLMv1 and I still in the process of test the thing out to see what the behaviors are by changing the LAN manager authentication level to "5-Send NTLMv2 response only\refuse LM & NTLM" at client side first.

Environment:

Client (W2K) ----------- ADDC(WinSvr2016)

Client:

LAN manager authentication level to "5-Send NTLMv2 response only\refuse LM & NTLM"

ADDC:

LAN manager authentication level to "1-Send LM & NTLM response"

Security event log from ADDC still showing NTLMv1, is the normal behavior?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-28*

Hello, 

According to previous cases, if the security level negotiation uses the "traditional" method, it will cause the problem that the authentication actually uses NTLMv2 but reports NTLMv1 in the event log. For details, you can refer to the following link: 

Audit event shows authentication package as NTLMv1 instead of NTLMv2 - Windows Server | Microsoft Learn

I hope the above information is helpful to you.

Best Regards

Zunhui
