---
title: "Microsoft exchange 365 IPs being blocked, how to use a dedicated IP for our organization."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1823803/microsoft-exchange-365-ips-being-blocked-how-to-us
question_id: 1823803
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Microsoft exchange 365 IPs being blocked, how to use a dedicated IP for our organization.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1823803/microsoft-exchange-365-ips-being-blocked-how-to-us (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I work for a college as an IT Admin, we've been using Microsoft 365, Entra, Exchange online, for students and staff, AD server is on-premise, everything else is with Microsoft 365. 

Some of Microsoft's IPs that are used with exchange online are blacklisted, so a lot of times a user has to resend the email a few times to get it through. Is there any way we can associate our dedicated IP that we have with our ISP with our Microsoft Exchange online account? 

Can we like deploy an edge transport and redirect emails from 365 through our on-premise edge transport, using connectors?

Any advice is greatly appreciated!

Thank you,

Raffy

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-07-18*

You can't there is a constantly growing number of IP address in Microsoft 365 (formerly Office 365), so they decided to create an RSS channel for that https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide because it is constantly growing, in applications and services...
