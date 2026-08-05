---
title: "Update Exchange 2016 cu2 to cu19"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/313074/update-exchange-2016-cu2-to-cu19
question_id: 313074
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Update Exchange 2016 cu2 to cu19

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/313074/update-exchange-2016-cu2-to-cu19 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have recently inherited server 2012 running exchange 2016 on CU2. I will be updating it to CU19 and applying the emergency patch put out by Microsoft. I am trying to locate the easiest way to backup Exchange or Internet Information Server (IIS) settings. I will be following this write up. Any other pointers are helpful. https://learn.microsoft.com/en-us/exchange/plan-and-deploy/install-cumulative-updates?view=exchserver-2019

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-16*

anonymous userDavid     

Thank you so much for the direction. The update worked perfectly without any errors.     

Follow these steps, rebooting after EACH step and running from an ELEVATED PROMPT.    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2016    

Install .net 4.8    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#microsoft-net-framework    

Run each step separately:    

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema    

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD    

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAllDomains    

Then install CU19:    

CU19:    

https://www.microsoft.com/en-us/download/details.aspx?id=102532    

Then install the security patch:    

Critical Patch:    

https://www.microsoft.com/en-us/download/details.aspx?id=102772
