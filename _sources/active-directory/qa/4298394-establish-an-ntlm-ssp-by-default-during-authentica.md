---
title: "Establish an NTLM SSP by default during authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4298394/establish-an-ntlm-ssp-by-default-during-authentica
question_id: 4298394
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Establish an NTLM SSP by default during authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4298394/establish-an-ntlm-ssp-by-default-during-authentica (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Problem: how to establish an SSP in the NTLM protocol mandatory, without the possibility of disabling it on the receiving side(server).  

Where and what parameters need to configure? Is it in Group Policy or Registry? My team didn't find it.  

The parameters known to me, such as "Minimum session security for NTLMSSP based (including secure RPC) servers" and "Minimal session security for NTLM SSP based (including secure RPC) clients, do not make the use of SSP mandatory, because we can disable it for example with the help of the linux program "responder" and the "—lm" or "—disable-ess" key.

I will be very grateful for your help!

Thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-25*

Hi, I'm Elise, and I'd be happy to help with your issue.

For this type of issue I would recommended posting in the Q&A forum, as this is the intended audience for these type of queries:

https://learn.microsoft.com/answers/

Kind Regards,

Elise
