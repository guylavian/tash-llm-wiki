---
title: "Exchange Server 2016 CU18"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/193973/exchange-server-2016-cu18
question_id: 193973
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Server 2016 CU18

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/193973/exchange-server-2016-cu18 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I currently have Exchange Server 2016 CU14 build 15.1.1847.3 installed. I would like to install the Exchange Server 2016 CU18 to upgrade the existing exchange server installation.  Based on what I am reading, I believe I can go directly from CU14 to CU18.  Is this correct?    

I also wanted to confirm that installing the updated CU version, that this doesn’t change any configuration or settings in the exchange server environment.  Since this is the full version of exchange that comes with the cumulative updates I just wanted to be sure that existing settings would remain unchanged from an administrative perspective.  

Thanks,  

Roger

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2020-12-10*

Yes you can do that, go straight to CU18    

Follow this and break out each step even if you are single domain/AD forest    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019    

Then follow:    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/install-cumulative-updates?view=exchserver-2019    

NOTE:    

Any customized Exchange or Internet Information Server (IIS) settings that you made in Exchange XML application configuration files on the Exchange server (for example, web.config files or the EdgeTransport.exe.config file) will be overwritten when you install an Exchange CU. Be sure save this information so you can easily re-apply the settings after the install. After you install the Exchange CU, you need to re-configure these settings.
