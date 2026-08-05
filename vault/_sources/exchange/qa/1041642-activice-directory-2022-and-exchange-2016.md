---
title: "Activice Directory 2022 and Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1041642/activice-directory-2022-and-exchange-2016
question_id: 1041642
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Activice Directory 2022 and Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1041642/activice-directory-2022-and-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear experts,    

We are running Exchange 2016 CU23 on-prem and would like to go to Active Directory on Windows 2022 servers. I am checking and getting conflicting information  if this is supported or not.    

This article states that it is supported: https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2016    

This article does not have it listed as supported: https://learn.microsoft.com/en-us/exchange/plan-and-deploy/system-requirements?view=exchserver-2016     

Does anyone know whate the deal is here?    

Many tanks for you input!    

Regards,    

mrtro

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-19*

I have also recieved an answer from MS:    

"Checking the last time/date update for both links, you're completely the first one was updated in April 2022 and the second one in September 2022. The second article, the "Exchange Supportability Matrix" is the one that includes the correct information and it's the one that it's updated regularly as it includes the information for all Exchange versions. We will report this internally in order to fix the first link document."

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-10*

Thanks for the information JimmySalian-2011!    

Anyone out there that is running Windows 2022 as OS on their domain controllers?    

I am just trying to make absolutely sure before we go ahead with this.    

Regards,    

mrtro

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-10-10*

Hi,    

AFAIK, the article states that inplace upgrade of Windows 2019 with Exchange 2019 is not supported however the link reference states the Windows 2022 Standard and Datacenter is supported Domain Controller + OS. Also the article date is updated recently so I will follow that link and matrix as supported.    

    

    

Hope this helps.    

----    

Please don't forget to upvote and Accept as answer if the reply is helpful    

If this answer helped you please mark it as "Verified" so other users can reference it.
