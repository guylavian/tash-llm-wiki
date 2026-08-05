---
title: "Exchange 2013 CU23 Installation Hierarcy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/284851/exchange-2013-cu23-installation-hierarcy
question_id: 284851
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 CU23 Installation Hierarcy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/284851/exchange-2013-cu23-installation-hierarcy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I am looking to install Exchange 2013 CU 23 rollup due to High vulnerability on it. Just for the clarity please guide from where should i start the CU installation. I have single forest multi domain environment. Exchange is installed on one of the child domain. DAG/MBX, CAS and Edge Server are on separate servers.   

Should i require to prepare Schema on schema master role holder?  

Should i require to prepare domain on each child domain?  

From which exchange role server should i start installation?  

what would be the suspected impact on existing environment if any?  

Anyone please guide in detail  

Thank you and regards.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-23*

What CU are you at now?    

You should start here:    

https://learn.microsoft.com/en-us/exchange/prepare-active-directory-and-domains-exchange-2013-help    

Run each step individually from the root , but no need to run on the DC that holds the schema master, but you can. I prefer a member server in the root domain    

```
Setup.exe /PrepareSchema /IAcceptExchangeServerLicenseTerms  
Setup.exe /PrepareAD /OrganizationName:"" /IAcceptExchangeServerLicenseTerms  
Setup.exe /PrepareAllDomains /IAcceptExchangeServerLicenseTerms
```

Exchange Installation Order and steps:    

https://practical365.com/exchange-server/exchange-2013-installing-cumulative-updates/    

Be sure to get an Exchange aware full backup of databases before proceeding
