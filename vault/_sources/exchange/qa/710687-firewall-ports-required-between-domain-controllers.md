---
title: "Firewall ports required between domain controllers and Exchange servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/710687/firewall-ports-required-between-domain-controllers
question_id: 710687
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Firewall ports required between domain controllers and Exchange servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/710687/firewall-ports-required-between-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a situation in the environment, Domain controllers are hosted by a vendor and their data center and Exchange servers are hosted by a different vendor in their data center.  We have a request from Exchange application team to open ANY to Any communication between domain controllers and Exchange servers. This request is being rejected by the Company Security and Firewall team. Can someone had this experience? and Can share the List of Firewall Ports required between DC and Exchange server communication?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-01-26*

Just to be clear, all ports must be open between Exch and the DCs to be supported:    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/network-ports?view=exchserver-2019

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-26*

I'd start with these ones.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts#windows-server-2008-and-later-versions    

and more are listed here.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
