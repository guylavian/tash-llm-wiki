---
title: "Enforce the use of NTLMv2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1025547/enforce-the-use-of-ntlmv2
question_id: 1025547
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_affiliations: ["Mvp"]
---
# Enforce the use of NTLMv2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1025547/enforce-the-use-of-ntlmv2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

If I want to enforce the use of NTLMv2 with the below GPO settings do I have to apply this to both the domain controller and the clients ?    

It seems like if I only apply this to the client then when I reboot the client I get the warning below.    

Or..... If I only apply this to the domain controllers will that force all the clients to use NTLMv2 when they authenticate with the domain controller ?    

    

    

Thanks for any reply     

/R    

Andy

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-09-27*

Maybe this one helps.    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-restrict-ntlm-add-server-exceptions-in-this-domain    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-16*

you have to make sure you make sure to configure the client-side policy first send only NTLM v2 request before you apply on Domain controller side and monitor which are still sending NTLM v1 , LM request to change them on core config level. We have done this breaking down to 4 changes, 

-  Send NTLM responses only –Clients use NTLM authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.

-  Send NTLMv2 responses only –Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.

-  Send NTLMv2 responses only\refuse LM –Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM (accept only NTLM and NTLMv2 authentication).

-  Send NTLMv2 responses only\refuse LM & NTLM –Clients use NTLMv2 authentication only and use NTLMv2 session security if the server supports it. Domain controllers refuse LM and NTLM (accept only NTLMv2 authentication).

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-28*

Hi,    

Thanks for reply @Scott Dawson       

If I deploy it to the domain controller, then I guess all clients will be affected right away ? I would like to implement this in segments, say 50 and 50 machines, but I guess that would not work since I have to deploy it on the domain controllers for the system to work ? Right ?     

I know I can implement logging, So I guess I would have to do that first.....     

comments ?    

/R    

Andy

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-28*

Hi,    

Thanks for the reply, but not the answer I was looking for I belive.    

The link you refer to is "Network Security: Restrict NTLM: NTLM authentication in this domain", and since I want to only use NTLMv2 It would be enough to configure "Network security: LAN Manager authentication level - Send NTLMv2 responses only. Refuse LM & NTLM", am I not wrong ?    

If I don't understand correctly, the link you provide is an exception, so that I can list some computers to be allowed with NTLM?    

But again, my question is "If I want to enforce the use of NTLMv2 with the below GPO settings do I have to apply this to both the domain controller and the clients ? Or I might not understand this correctly so please explain :)    

Thanks again for answers.    

/R    

Andy
