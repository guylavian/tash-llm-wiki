---
title: "Install Exchange 2016 CU on Windows Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/298235/install-exchange-2016-cu-on-windows-server-2019
question_id: 298235
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Install Exchange 2016 CU on Windows Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/298235/install-exchange-2016-cu-on-windows-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,   

   I am stuck updating my Exchange Server CU 13 to the latest CU because the setup tells me that the Windows version is not compatible. I found myself in this situation upgrading Windows from 2016 to 2019.   

Is there any solution different by installing everything from scratch on a new machine?   

Thanks,  

Michele

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-03-04*

Hi @Michele   ,    

Installing Exchange 2016 on Windows 2019 is not supported.    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/system-requirements?view=exchserver-2016#supported-operating-systems-for-exchange-2016    

Please find the below reference for the pre-requisites for installing the latest Exchange 2016 CU in the windows 2016    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2016#exchange-2016-prerequisites-for-preparing-active-directory    

If the above suggestion helps, please click on "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-05*

Hi @Michele  ,    

As said by AshokM and also mentioned in the following official document, it's not supported to install Exchange 2016 on Windows server 2019. So you may have to keep using Windows 2016 for Exchange 2016 or considering upgrading to Exchange 2019 which can run with Windows server 2019:    

Exchange Server supportability matrix    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
