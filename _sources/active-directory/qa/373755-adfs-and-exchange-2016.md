---
title: "adfs and exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/373755/adfs-and-exchange-2016
question_id: 373755
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# adfs and exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/373755/adfs-and-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

exchange2016 access adfs2016 login  

If the exchange server and the adfs server want to communicate with each other, which ports need to be opened?  

For example, which ports will be requested for a login to exchange to adfs, and which ports will be requested for adfs to exchange, and will ad requests be involved in the middle? If so, which ports will be involved?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-27*

The Exchange Servers do not communicate with the ADFS servers.    

The clients need to be able to connect on port 443 (and port 49443 for cert auth)    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/best-practices-securing-ad-fs#wap-and-users    

Note only EAC and OWA support ADFS auth    

https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019
