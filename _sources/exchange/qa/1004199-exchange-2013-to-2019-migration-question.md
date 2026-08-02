---
title: "Exchange 2013 to 2019 migration question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1004199/exchange-2013-to-2019-migration-question
question_id: 1004199
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 to 2019 migration question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1004199/exchange-2013-to-2019-migration-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We are starting the migration to exchange 2019 from 2013.     

It looks like after we prepare AD Schema with  Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema    

we would need to prepare AD  using Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD /OrganizationName: “??????”    

So the question is what would we use for the organization name? Should it be idential to our org name of exchange 2013 or something different?    

Get-OrganizationConfig | select LegacyExchangeDN  on a 2013 server returns    

LegacyExchangeDN    

/o=Our Company    

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-12*

thank you!
