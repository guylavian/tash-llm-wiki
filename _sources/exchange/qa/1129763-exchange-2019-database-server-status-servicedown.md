---
title: "Exchange 2019 Database Server Status ServiceDown"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1129763/exchange-2019-database-server-status-servicedown
question_id: 1129763
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 Database Server Status ServiceDown

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1129763/exchange-2019-database-server-status-servicedown (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,    

Current infra:    

HQ:    

HQEMLAPP01 - Ex2019    

HQEMLAPP02 - Ex2019    

DRC:    

DRCEMLAPP01- Ex2019    

Exchange 2019 servers stretched between 2 datacenter, HQ and DRC.    

Issue:    

Sometime the status for Mailbox Database Copies shown as below.    

From DRC Exchange server:    

    

From HQ Exchange server:    

    

    

If result as above shown, we need to restart the Exchange server at DRC site to fix the issue.    

Is there any solution to this and what needs to be checked for. Is there any firewall blocking, WMI or any related finding.    

Since we need to frequently check the status for server at DRC and if the issue raised, then Mailbox Database replication will have issue until the server being restarted.    

Regards,    

Mohd

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-15*

Ensure that that the all ports are open between the data centers between the Exchange Servers and to all the domain controllers.    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/network-ports?view=exchserver-2019
