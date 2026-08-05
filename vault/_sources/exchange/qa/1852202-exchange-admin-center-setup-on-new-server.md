---
title: "Exchange Admin Center setup on new server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1852202/exchange-admin-center-setup-on-new-server
question_id: 1852202
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Admin Center setup on new server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1852202/exchange-admin-center-setup-on-new-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, my company currently has a hybrid environment between on-prem AD and Azure AD. Our mailboxes are stored in M365. 

I'm trying to configure a new URL for the on-prem EAC, but I cannot seem to figure out how to point the URL to the new server we have created. I tried looking through DNS and IIS, but cannot find exactly where the old URL is stored/pointing to. The EAC is accessible from the old server URL (i.e https://server.mydomain.com/ecp) but would like to make it accessible with the new server (i.e https://new-server.mydomain.com/ecp). We are looking to decommission the old Exchange server, and this EAC access set up is the last step before we can. 

Any help is appreciated, thank you!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-08-01*

By default the new server should have the URL set to itself already for ECP

https://learn.microsoft.com/en-us/powershell/module/exchange/set-ecpvirtualdirectory?view=exchange-ps

You just need to make sure that A record for the server is in your local DNS as well.
