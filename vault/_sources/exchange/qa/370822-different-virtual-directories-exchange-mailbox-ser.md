---
title: "Different virtual directories exchange mailbox server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/370822/different-virtual-directories-exchange-mailbox-ser
question_id: 370822
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-development-iis"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Different virtual directories exchange mailbox server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/370822/different-virtual-directories-exchange-mailbox-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,  

We are in exchange design phase , and we suggested to define different virtual directory than those published on the iis default  website  .  

Why that ? For example to disable owa and ecp on the default website and to be enabled on the new custom virtual directory over the new iis website on the same mailbox  server to can restrict more access for such services .  

My question is this approach supported by Microsoft,  and valid technically or not ??

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-25*

It's greate article but they mentioned another article how to work over 2016 ,and 2019  

https://techcommunity.microsoft.com/t5/exchange-team-blog/monitoring-exchange-using-multiple-owa-ecp-virtual-directories/ba-p/697122

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-25*

Ok, this is the only supported method to do this. From reading the comments, it does not work for Exchange 2016 ( which means 2019 as well)  

https://techcommunity.microsoft.com/t5/exchange-team-blog/configuring-multiple-owa-ecp-virtual-directories-on-the-exchange/ba-p/611217  

Honestly, I would not do this.  

instead, I would create separate FQDN namespaces and leave everything as the default, then have users connect to the FQDN that applies to them with separate Exchange Servers.
