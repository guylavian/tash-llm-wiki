---
title: "Exchange 2010 SP3 RU25 with Domain Controller 2019 + 2008 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/927882/exchange-2010-sp3-ru25-with-domain-controller-2019
question_id: 927882
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2010 SP3 RU25 with Domain Controller 2019 + 2008 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/927882/exchange-2010-sp3-ru25-with-domain-controller-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My existing environment have two Exchange 2010 SP3 RU25 with two domain controllers 2008 R2. The functional level is Windows Server 2008.    

I would like to add in Windows Server 2019 domain controller is the environment but as per Exchange supportability matrix 2019 is not supported for Exchange 2010. So if I just simply promoting one Windows Server 2019 as domain controller, transfer the FSMO role to it, and I keep one of the domain controller 2008 R2 running in the environment, will this cause issue and is it supported?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-07-15*

It may. Not supported usually means, "not tested with".     

So, in other words, you can do this, but if causes an issue, then you are kinda on your own. :)
