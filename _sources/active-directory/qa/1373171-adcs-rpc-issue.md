---
title: "ADCS RPC issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1373171/adcs-rpc-issue
question_id: 1373171
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# ADCS RPC issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1373171/adcs-rpc-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have freshly installed an ADCS server, root enterprise, standalone integrated to a domain.

All seems OK, all port is open (same VLAN with domain controler without firewall)

I can request certificate from another server without any problem, but only the domain controler can't request beceause RPC error ...

I have tried, a lot of solution found on internet :

RPC service is started

Communcation port is open

Some registry key that contain certsrv is present

Acces right on DCOM, user group ... is ok (by default)

I don't understand why only the domain controler have this issue ...

Need help please :s

"Sorry for my English"

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-21*

Thx for reply.

Yes all port is open, both server are on the same subnet and the windows firewall is disabled.

Port tested with Portqry and telnet

The request is working with another server (not a DC) in the same subnet like DC

Only the DC this issue  

I have try all solution from the link :s

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-21*

Hello

Thank you for your question and reaching out.

The ports 445 and 139 are used by the CA to try to reach the requesting DC; therefore, please double-check that these ports are open in your firewall (or turn it off completely for checking purposes).

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/error-0x800706ba-certificate-enrollment

--If the reply is helpful, please Upvote and Accept as answer--
