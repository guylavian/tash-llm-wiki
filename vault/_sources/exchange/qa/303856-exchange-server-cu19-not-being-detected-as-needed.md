---
title: "Exchange Server CU19 not being detected as needed by windows update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/303856/exchange-server-cu19-not-being-detected-as-needed
question_id: 303856
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Server CU19 not being detected as needed by windows update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/303856/exchange-server-cu19-not-being-detected-as-needed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 different environments running exchange server 2016.  

One of them Running on Server 2012R2  

the other running on Server 2019  

The 2012R2 servers has Exchange 2016 CU1 installed and the windows update does say that i am up to date  

The 2019 server has Exchange 2016 CU11 installed and the windows update does say that i am up to date  

Both server have checked "deliver other MS products updates with windows update" which is the case how the above CUs were delivered and installed too.  

Any ideas why according to Microsoft AUtomatic Update service i do not have to install the CUs?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-09*

Agree with Andy, both your servers need to update and the server running on window server 2019 has to be rebuilt.    

Keep your CU version up-to-date (or a bit later than newest) this time after you finish the updates.    

Be free to post any issues when updating.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-08*

Because:    

2016 CU1 is so old, ( 5 years!) that it probably cant detect the requirement    

You need to get to that CU19 plus the security patch.    

Update it manually -  immediately    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2016    

Run each step separately:    

    Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema  

    Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD   

    Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAllDomains  

Then install .net 4.8    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#microsoft-net-framework    

    

Then install CU19:    

CU19:    

https://www.microsoft.com/en-us/download/details.aspx?id=102532    

Then install the security patch:    

Critical Patch:    

https://www.microsoft.com/en-us/download/details.aspx?id=102772    

As for the other server, this is not supported:    

The 2019 server has Exchange 2016 CU11     

Exchange 2016 is not supported on Windows 2019. You will need to rebuild that server with a supported O/S    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#supported-operating-system-platforms
