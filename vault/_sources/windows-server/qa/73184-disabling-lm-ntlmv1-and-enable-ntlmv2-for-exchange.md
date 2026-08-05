---
title: "Disabling LM / NTLMv1 and enable NTLMV2 for Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/73184/disabling-lm-ntlmv1-and-enable-ntlmv2-for-exchange
question_id: 73184
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Disabling LM / NTLMv1 and enable NTLMV2 for Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/73184/disabling-lm-ntlmv1-and-enable-ntlmv2-for-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,  

Disabling LM / NTLMv1 and enable NTLMV2 for Exchange 2016.  

Please confirm if compatibility checks have to be done for Outlook, workstation OS.  

Cheers  

Priya

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-25*

HI    

from below documents ,I think it is feasible.    

Exchange 2016 compatibility with Network security: LAN Manager authentication level" - NTLMV2 response only    

https://social.technet.microsoft.com/Forums/en-US/e5812087-e8bd-4db2-be2b-9b4650c5ebea/exchange-2016-compatibility-with-network-security-lan-manager-authentication-levelquot-ntlmv2?forum=Exch2016GD    

Network security: LAN Manager authentication level    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-lan-manager-authentication-level

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-08-23*

Hi,  

I confirm that Exchange 2016 and the last OS and outlook version don't need NTLMv1.  

Try to disable NTLMv1 and LM protocol from client mahine before disble them on domain controller.  

Please mark this reply this reply as answer if it help your to fix your issue

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-08-21*

Absolutely. This is not an Exchange issue as much as a Windows one.    

https://learn.microsoft.com/en-us/archive/blogs/miriamxyra/stop-using-lan-manager-and-ntlmv1    

Before making that change, you should gather auditing data and verify that nothing is using V1 and if so, then configure to use V2 if possible.    

https://learn.microsoft.com/en-us/archive/blogs/miriamxyra/stop-using-lan-manager-and-ntlmv1#further-resources-on-auditing-and-purging-old-authentication-protocols
