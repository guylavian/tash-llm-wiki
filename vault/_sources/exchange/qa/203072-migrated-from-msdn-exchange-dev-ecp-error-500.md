---
title: "[Migrated from MSDN Exchange Dev]ECP Error 500"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/203072/migrated-from-msdn-exchange-dev-ecp-error-500
question_id: 203072
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]ECP Error 500

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/203072/migrated-from-msdn-exchange-dev-ecp-error-500 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

ECP Error 500  

[Original post]  

I faced Error 500 in ECP while i can use OWA correctly.  

what should i do?  

"Unexpected Error.an Error occurred and your request couldn't be complete. please try again "

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-18*

Hi,  

Sorry I need to ask a few questions to get some more information.  

1.What version of Exchange are you running?  

2.Is it a fresh install? If not,what changes have been done recently before the problem appears?  

Here are some suggestions:  

1.Try recycling the MSExchangeECPAppPool in the IIS manager-->Application Pools  

2.Recreate the EAC virtual directory via running the following commands in EMS(Exchange Management Shell)  

```
Remove-EcpVirtualDirectory -Identity "Server01\ecp (Default Web site)"
New-EcpVirtualDirectory
```
