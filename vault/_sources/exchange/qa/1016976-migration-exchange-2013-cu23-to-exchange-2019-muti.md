---
title: "Migration Exchange 2013 CU23 to Exchange 2019 (mutiple server)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1016976/migration-exchange-2013-cu23-to-exchange-2019-muti
question_id: 1016976
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Migration Exchange 2013 CU23 to Exchange 2019 (mutiple server)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1016976/migration-exchange-2013-cu23-to-exchange-2019-muti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello,     

I have a problem     

I have a site A with an exchange 2013 and a site B with another exchange 2013. The two servers communicate well together. But they each have different urls:    

autodiscover on site A (ex: siteA.contoso.com)    

another on autodiscover on site B (siteB.contoso.com)    

the same for the internal and external urls each site points to different urls    

ex site A:    

internal https://sitea.contoso.com/owa    

external https://sitea.contoso.com/owa    

for site B:    

internal https://siteB.contoso.com/owa    

external https://siteB.contoso.com/owa    

same for ecp, outlook anywhere, offline address book, activesync, ews..    

how can i migrate to my exchange 2019? Exchange 2019 will be on Site A and Site B users will communicate with Site A Exchange 2019.    

Can you help me?    

thank you in advance,

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-27*

hello,     

I've manage to migrate    

finally I pointed site B to the same URLs as site A    

I updated the DNS, autodiscover...    

and I migrated smoothly to Exchange 2019 full version    

this guide helped me:    

https://practical365.com/migrating-exchange-server-2016/    

thank you all,

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-21*

Follow the Exchange Deployment Guide    

https://learn.microsoft.com/en-us/exchange/exchange-deployment-assistant?view=exchserver-2019
