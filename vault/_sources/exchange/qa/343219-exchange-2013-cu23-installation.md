---
title: "Exchange 2013 CU23 Installation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/343219/exchange-2013-cu23-installation
question_id: 343219
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 CU23 Installation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/343219/exchange-2013-cu23-installation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys, had some great for an earlier question, getting the below error    

I have updated .Net Framework 4.8     

I have run and rebooted in between the following steps separately    

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema    

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD    

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAllDomains    

Anyone come across this lately and have a good fix for it found this below from Practical 365    

https://practical365.com/expired-certificates-cause-exchange-cumulative-updates-fail/

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-03*

Looking at this now   

https://supertechman.com.au/how-to-renew-an-expired-microsoft-exchange-server-auth-certificate/#:~:text=The%20Microsoft%20Exchange%20Server%20Auth%20Certificate%20has%20a,expired%20or%20is%20about%20to%20expire%2C%20dont%20stress.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-03*

Thanks Manu Philip, there are 3 certificates that have expired along with the Auth certificate.  

Would it work to renew in EAC? I am going to take snapshot and try that in the morning, (once backups are successful tonight)  

Any good links for this that you can recommend?  

Much appreciated :)
