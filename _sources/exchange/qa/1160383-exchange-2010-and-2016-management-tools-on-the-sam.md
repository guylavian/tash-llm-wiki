---
title: "Exchange 2010 and 2016 Management Tools on the same server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160383/exchange-2010-and-2016-management-tools-on-the-sam
question_id: 1160383
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2010 and 2016 Management Tools on the same server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160383/exchange-2010-and-2016-management-tools-on-the-sam (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Exchange 2010 and are migrating to Exchange 2016. During this time, I am needing to manage both 2010 and 2016 and would like to use the management tools on the same server. However, I am getting an error "Exchange Server 2016 can't be installed on a server that has an Exchange Server 2007 or Exchange Server 2010 role installed. For more information, visit http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.Exchange2013AnyOnExchange2010Server.aspx" when trying to install the 2016 management tools on a Windows server 2012 R2 that is used to manage our servers. This server is not used as any other Exchange roles. Is there any way to make this work?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-01-12*

Yea that wont work. :) 

You will need to install on a different server or a client machine:

[https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019
