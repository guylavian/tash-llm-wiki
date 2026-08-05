---
title: "Hybrid Exchange Server setup and Windows Extended Protection?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1035669/hybrid-exchange-server-setup-and-windows-extended
question_id: 1035669
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Hybrid Exchange Server setup and Windows Extended Protection?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1035669/hybrid-exchange-server-setup-and-windows-extended (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm currently running Exchange 2016 on-premise with Hybrid Setup to Exchange Online (AD DS --> Azure AD).    

Based on https://microsoft.github.io/CSS-Exchange/Security/Extended-Protection/    

How can I safely enable and secure the OnPremise Hybrid Exchange Server when the below script shows the warning:    

    

Thank you,

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2022-10-05*

Did you enable Modern Hybrid? If not and you are using classic Hybrid, then you are ok:    

Extended Protection does not work with hybrid servers using Modern Hybrid configuration    

Extended Protection cannot be enabled on Hybrid Servers which uses Modern Hybrid configuration. In Modern Hybrid configuration, Hybrid Server are published to Exchange Online via Hybrid Agent which proxies the Exchange Online call to Exchange Server.    

Enabling Extended Protection on Hybrid servers using Modern Hybrid configuration will lead to disruption of hybrid features like mailbox migrations and Free/Busy. Hence, it is important to identify all the Hybrid Servers in the organization published via Hybrid Agent and not enable Extended Protection specifically on these servers.    

https://learn.microsoft.com/en-us/exchange/hybrid-configuration-wizard-options
