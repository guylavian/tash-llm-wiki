---
title: "Exchange Hybrid Connector Wizard (Version?)- Exchange 2016 CU 15 to O365 Tenant"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/135412/exchange-hybrid-connector-wizard-version-exchange
question_id: 135412
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Exchange Hybrid Connector Wizard (Version?)- Exchange 2016 CU 15 to O365 Tenant

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/135412/exchange-hybrid-connector-wizard-version-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we're currently in the process of migrating to first a Hybrid Exchange 2016 to O365 tenant, and eventually making the cutover and decommissioning our on prem server. I setup AD Connect and changed UPN's, and users and group look good in the tenant.  Setup conditional access for further security.  Now I need to install the Hybrid connector wizard, but in doing research i'm a bit nervous.  

I'm currently running Exchange 2016 CU15 (December 2019 update), and current is CU18 (Sept 2020).  

MSFT always recommends the latest version in order to obtain a  supported environment.  It's very tough for us to take the single server offline and upgrade it, since it is downtime that they really don't want.  That  said, if it's a MUST, I guess we can.  

In reading about the current connector (they don't really have versions when I download them) it says you have to be running  CU18 (September 2020) since major updates were done to the connector.  Please see these 2 articles I found: 1.  https://techcommunity.microsoft.com/t5/exchange-team-blog/march-2020-significant-update-to-hybrid-configuration-wizard/ba-p/1238753  2. https://support.microsoft.com/en-us/help/4583653/september-2020-update-to-exchange-hybrid-configuration-wizard  

My question is - If I run the hybrid connector wizard from my current on prem Hybrid link, or from my O365 Hybrid link will it download the proper version that I need for my setup and work, OR - will it default to the latest downloadable version, and will I then run into issues using it since i'm at an older CU update?  

Just wondering if someone from MSFT with knowledge on this can please reply.  thanks!

## Answers

_No answers on this thread._
