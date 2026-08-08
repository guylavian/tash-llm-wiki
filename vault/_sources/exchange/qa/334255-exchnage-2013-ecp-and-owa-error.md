---
title: "Exchnage 2013 ECP and OWA error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/334255/exchnage-2013-ecp-and-owa-error
question_id: 334255
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchnage 2013 ECP and OWA error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/334255/exchnage-2013-ecp-and-owa-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All   

I have been updating our exchange server with all the windows updates  so I can run the CU23 update,  

I have temp done the iis rewrite rules advised and stopped all external 443 access whilst we patch the server BUT  

I can no longer get in to ECP or OWA, PowerShell works ok as long as I run as admin.  

I get am error when going to OWA from the server or ECP from the server   

Server error in /owa application   

The length of the query string for this request exceeds the configuration maxquuerystringlenghth value  

I am currently on exchange 2013  CU18 running on a Server 2012R2 server with all the updates run  

I dont want to try run the CU23 update in case it kills exchange due to this error above but need to do this so we can migrate the exchange to Office 365  

any ideas please  

Thanks in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-28*

Also helpful might be to run dpaulson45's heathchecker.ps1 script or the tasks it performs.   It can help expose version issues with .Net and the VC runtimes as well as misconfigured host settings and general Exchange health issues.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-27*

thanks did not see that and thought updating it to 4.7.2 in advance would have been enough.  

done the upgrade to cu23 on our backup VM Host and after 6 hours of some errors i had to manually overcome  it finally did it and allows me in to exchange, will try it for real now .  

thanks for your input and fingers crossed

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-27*

thanks I will try this on our VM backup first, I have tried recreating the front end and backend virtual directories with no success  

I think this error started after i updated .net to 4.7.2   

with over 100 users i need to be partly confidant it wont kill exchange completely  

Rob

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-27*

Well, I think the other way around  :)     

I would be applying .net 4.8, then CU23 then the patch and see if it it works after that since this a .net issue    

If not, then setting the manual values in the web.config:    

https://learn.microsoft.com/en-us/dotnet/api/system.web.configuration.httpruntimesection.maxquerystringlength?redirectedfrom=MSDN&view=netframework-4.8#System_Web_Configuration_HttpRuntimeSection_MaxQueryStringLength    

Get a full backup of Exchange    

Just FYI, be sure to follow these steps to go from Cu18 to Cu23, rebooting after EACH step and running from an ELEVATED PROMPT.    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2013    

Run each step separately:    

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema    

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD    

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAllDomains    

Install .net 4.8    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#microsoft-net-framework    

Then install CU23:    

https://www.microsoft.com/en-us/download/details.aspx?id=58392    

Then install the security patch:    

Critical Patch:    

https://www.microsoft.com/en-us/download/details.aspx?id=102775

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-27*

No it’s not the rules as it was working after I applied them started after I did a round of server updates. Unfortunately there where a few security updates for exchange and 2012 so not sure which one killed it
