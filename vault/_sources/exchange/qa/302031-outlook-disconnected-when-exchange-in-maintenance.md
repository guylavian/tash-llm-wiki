---
title: "Outlook disconnected when Exchange in Maintenance Mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/302031/outlook-disconnected-when-exchange-in-maintenance
question_id: 302031
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Outlook disconnected when Exchange in Maintenance Mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/302031/outlook-disconnected-when-exchange-in-maintenance (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Having some strange issues when we put our Exchange Servers in maintenance mode when doing a CU update. We have 4 Servers and 2 DAGS, when we put the primary server into maintenance mode, we get disconnected in Outlook. Everything else works fine, Webmail, E-Mail to phone, just not Outlook. Does anyone have any suggestions on what might be causing this? When I do a test in Outlook, it is pointing to the correct Internal/External URLS and the test comes back fine. It just will not connect to the Database on the failover server?  

Setup  

Exchange 2016   

4 Servers  

2DAGS  

Kemp Load Balancer  

Thanks,  

Gavin

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-06*

When you set to maint mode, do you also reboot the server after that to clear any connections?
