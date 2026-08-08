---
title: "[Migrated from MSDN Exchange Dev]  What happen when re-run prepare Schema in Exchange Installation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/197242/migrated-from-msdn-exchange-dev-what-happen-when-r
question_id: 197242
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# [Migrated from MSDN Exchange Dev]  What happen when re-run prepare Schema in Exchange Installation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/197242/migrated-from-msdn-exchange-dev-what-happen-when-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/2b6ef872-7017-4ef6-bca6-5d84cec500e7/what-happen-when-rerun-prepare-schema-in-exchange-installation?forum=exchangesvrdevelopment  

Hi all,  

Could you tell me what impact when I re-run prepare Schema in existing Exchange environment?  

In my case, I did run the first prepare schema in a domain child child1.domain.com but my exchange server is in child2.domain.com, then now I cant use disable mailbox function in UI and powershell as well. Im thinking about re-run prepare schema in domain.com (root), but dont know exactly the impact to existing environment.  

Please advice me, thanks in advance!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-14*

If the schema prepare failed you would have known it    

Sounds like you didnt run through all the steps, specifically PrepareAllDomains    

Run this from the root, each step:    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019    

```
Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema  
Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD  
Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAllDomains
```

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-14*

What error is reported when failing with disabling mailbox?     

You should run the command on root domain at first rather than on child domain.    

Re-running Prepare Schema might not solve the issue, just update your schema with the CU you specified.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-14*

Hi,    

Re-running the PrepareSchema with the current Exchange CU does not make any impact if it was run previously when the CU was installed.    

In this scenario, preapreschema needs to be run on the domain where the Schema master role is present. If domain.com is the parent and holds the schemamaster role, then PrepareSchema has to be run on a machine which is joined to domain.com and with the current Exchange CU iso. Schema change is forest-wide.    

You can check the current schema version before running     

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019    

Also, if Disable mailbox function is not working, can you try adding your account to "Recipient Management" & "organization management" role groups and check    

If the above suggestion helps, please click on "Accept Answer" and upvote it
