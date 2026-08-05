---
title: "Exchange 2016 accepted domain type:internal relay"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/230762/exchange-2016-accepted-domain-type-internal-relay
question_id: 230762
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 accepted domain type:internal relay

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/230762/exchange-2016-accepted-domain-type-internal-relay (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,  

In exchange 2016 we have setup "accepted domains".  But later we created  Accepted domain with "*"  under domain type this one is "Internal relay".  

As far as I know having "accepted domain" with "*" makes exchange an "open relay" what is everything we don't want.   

Does "accepted domain" with "*"  Domain type "internal relay" makes exchange an open relay ?  

Thank you,  

Pero

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-01-14*

What it tells Exchange is that if the recipient can't be found, then send the message to another shared mail system that matches.    

HOWEVER, you should not have an accepted domain with a wildcard  unless its set for a subdomain like *.contoso.com     

You should only have accepted domains that represent the actual SMTP domains you accept for and if you are authoritative, then they should be set that way    

Why was one created for * ?    

https://learn.microsoft.com/en-us/exchange/mail-flow/accepted-domains/accepted-domains?view=exchserver-2019
