---
title: "Exchange 2016: How to exclude Exchange Server themselves from ADFS authentication on OWA and ECP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297064/exchange-2016-how-to-exclude-exchange-server-thems
question_id: 297064
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016: How to exclude Exchange Server themselves from ADFS authentication on OWA and ECP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297064/exchange-2016-how-to-exclude-exchange-server-thems (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We successfully  enabled ADFS authentication for OWA and ECP.  

While this is what we want for the clients, we now have the problem that the local ECP of any exchange server cant be authenticated anymore: https://localhost/ecp/?ExchClientVer=15 or https://servername/ecp/?ExchClientVer=15  

This leads to an ADFS error page because the cert is not valid.  

We have to fall back to https://owa.ist.ac.at/ecp/?ExchClientVer=15  

The problem with this is, for some tasks i need to know on which server I work. For instance to check if our OWA theme still works after a server upgrade.  

So i need to make https://localhost/ecp/?ExchClientVer=15 work again locally on the servers. How I can exclude these servers or the admin users from ADFS authentication? I can apply the authentication in ADFS to groups, but now they are applied to everyone and I would love if I dont have to mess with the groups but somehow could just exclude the servers in a way that does not affect the whole infrastructure.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-03*

There is no way to do that unless you disable ADFS auth on the virtual dirs of those servers.  

Alternatively, set the local hosts file on your workstation for owa.ist.ac.at to a specific server's IP Address and connect that way when you want to verify things.
