---
title: "Exchange Mailbox/CAS Server Outbound 443 Requirement for Exchange Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2276475/exchange-mailbox-cas-server-outbound-443-requireme
question_id: 2276475
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Mailbox/CAS Server Outbound 443 Requirement for Exchange Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2276475/exchange-mailbox-cas-server-outbound-443-requireme (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Looking at the Hybrid Wizard Configuration Options and requirement for Exchange Modern Full setup (With Hybrid Agent). It seems like the CAS/Mailbox server still needs to have outbound 443 & 80 access to Exchange Online endpoints. 

https://learn.microsoft.com/en-us/exchange/hybrid-configuration-wizard-options

Just wondering, if my Exchange mailbox/CAS server doesn't have outbound internet access, can we still configure the Exchange hybrid with modern full topology? The hybrid configuration wizard and Hybrid agent will be running and installing on a separate server that has internet access.

If I do not need to care about the Free/Busy capability, I still need to have internet 443 access on my Exchange mailbox/CAS server to Exchange online?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-05-17*

I think you'll find a degraded experience. You can certainly try it, but why not just open those ports to Exchange Online to be supported? 

Free/Busy , Mail Tips , Autodiscover, EWS, all that stuff assume 443 is open to and from Exchange Online in hybrid mode.

This refers to the Hybrid agent but the principal is the same  

https://learn.microsoft.com/en-us/exchange/hybrid-deployment/hybrid-agent#port-and-protocol-requirements

Having said that, there is nothing that says you cant experiment and see what happens  :)

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-05-16*

Where are your mailboxes? on prem or all in ExO? If all in Exo, then you prob dont need Full, if you still have some on prem then you should open those ports.
