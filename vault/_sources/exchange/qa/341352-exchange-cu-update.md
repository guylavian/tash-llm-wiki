---
title: "Exchange CU Update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/341352/exchange-cu-update
question_id: 341352
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange CU Update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/341352/exchange-cu-update (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi   

Updating an Exchange Server (its non internet facing hence doing it now)   

Exchange 2013 CU6 (hadnt been done since 2014)   

Its a mailbox only server in a hybrid 365 environment, there is no DAG etc  

Do i still need to put Exchange server into maintence mode or can I just update .Net Framework 4.7.2 and install CU23?  

Thanks, links appreciated with answers as well :)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-01*

Thanks Andy really appreciate the quick response super stuff  

I thought that CU23 was the security patch  

https://practical365.com/microsoft-issues-critical-security-updates-for-exchange-server/  

Two more queries I got a prerequisite for 4.7.2 .Net Framework is it better to just install 4.8 as you say?  

Also I was going to run setup.exe from the CU23 once extracted  

What happens if I don't run those steps as below? (Just looking to learn more about it I have done the below for a fresh Exchange install alright) :)   

Run each step separately:  

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema  

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD  

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAllDomains  

Also why no need for maintenance mode? Excellent stuff :)
