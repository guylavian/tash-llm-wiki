---
title: "Exchange 2019 CU8 installation issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/301475/exchange-2019-cu8-installation-issues
question_id: 301475
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 CU8 installation issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/301475/exchange-2019-cu8-installation-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, We are on Exchange 2019 cu7. When trying to apply CU8 fails with following error …. "The upgrade patch cannot be installed by the windows installer service because the program to be upgraded may be missing, or the upgrade patch may update a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade patch." Appreciate any suggestions on troubleshooting this. Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-08*

Hi @Anantha Lakshman Chilakamarri      

Yes, according to the official link published by Microsoft, Released: March 2021 Exchange Server Security Updates    

Security updates are available for Exchange 2019 CU7 and CU8.     

Make sure you have Download Security Update For Exchange Server 2019 Cumulative Update 7 (KB5000871)    

You could also check below articles to get more information:     

Issues due to Exchange Server security updates    

FAQ for March 2021 Exchange Server Security Updates    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-07*

Thanks AndyDavid for the suggestion. This was about zero-day patching. CU7 was applied ok before trying to apply CU8.  

For zero-day security patch, is CU7 enough without CU8?  

Appreciate your time with the clarification.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-07*

The upgrade patch cannot be installed by the windows installer service because the program to be upgraded may be missing, or the upgrade patch may update a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade patch."   

That's the error message you would get if attempting to apply a security patch to the wrong version of Exchange. Is that what is being attempted here?  

Are you trying to install the zero-day security patch?   

If so, can I suggest that rather then trying to upgrade to CU8, you simply apply the patch now to CU7?  

https://www.microsoft.com/en-us/download/details.aspx?id=102771  

Get that applied immediately, then worry about upgrading to CU8.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-07*

Hi @Anantha Lakshman Chilakamarri   ,

Make sure to download the ISO again and check the below,

1.Check if all the required windows pre-requisites are installed .NET, VC++, etc

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2019#windows-server-2019-prerequisites-for-exchange-2019

2.Prepare active directory using the below commands,

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema  

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD  

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareDomain

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019#step-1-extend-the-active-directory-schema

3.Account is part of Exchange Organization Management role group, Schema Admins and Enterprise Admins groups.

If the above suggestion helps, please click on "Accept Answer" and upvote it.
