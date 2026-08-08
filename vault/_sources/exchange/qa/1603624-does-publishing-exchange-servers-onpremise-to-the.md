---
title: "Does publishing Exchange Servers OnPremise to the Internet is still required for Hybrid Exchange organization with no OnPremise mailbox?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1603624/does-publishing-exchange-servers-onpremise-to-the
question_id: 1603624
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Does publishing Exchange Servers OnPremise to the Internet is still required for Hybrid Exchange organization with no OnPremise mailbox?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1603624/does-publishing-exchange-servers-onpremise-to-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Although all of my mailboxes have been migrated to Exchange Online, I continue to run Exchange Server 2016 in all of my company's data centres because removing it is not supported.

I discovered in my Firewall that the public IP address for my Exchange Servers is still NAT-ed into the private IP address.

Is it necessary to preserve this configuration, or may I disable NAT on all of my Exchange Servers to limit the attack surface?

Any assistance will be highly appreciated.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-02-29*

You allow the Exchange Online IPs with your firewall.
Note that if you are using the Exchange on-prem servers for management only and do not have any on-prem mailboxes or do not require any hybrid mail routing, you do not need to do this and you can remove the Public IP NAT as long as autdiscover for your domain points to office 365.

https://www.alitajran.com/autodiscover-url-exchange-hybrid/
