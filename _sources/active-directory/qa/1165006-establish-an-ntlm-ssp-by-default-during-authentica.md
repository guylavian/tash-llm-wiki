---
title: "Establish an NTLM SSP by default during authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1165006/establish-an-ntlm-ssp-by-default-during-authentica
question_id: 1165006
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Volunteer Moderator"]
---
# Establish an NTLM SSP by default during authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1165006/establish-an-ntlm-ssp-by-default-during-authentica (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Problem: how to establish an SSP in the NTLM protocol mandatory, without the possibility of disabling it on the receiving side(server).

Where and what parameters need to configure? Is it in Group Policy or Registry? My team didn't find it.  

The parameters known to me, such as "Minimum session security for NTLMSSP based (including secure RPC) servers" and "Minimal session security for NTLM SSP based (including secure RPC) clients", do not make the use of SSP mandatory, because we can disable it for example with the help of the linux program "responder" and the "—lm" or "—disable-ess" key.

I will be very grateful for your help!

Thank you!

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-01-28*

Hi,

Please check this process over here and you can deploy via the GPO make sure all the settings are enabled as per the article and legacy clients will be impacted so if you have any old OS it will be impacted so please test out before you implement - https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-minimum-session-security-for-ntlm-ssp-based-including-secure-rpc-servers

Hope this helps.

JS

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
