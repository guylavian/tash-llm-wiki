---
title: "Exchange Server Update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/346397/exchange-server-update
question_id: 346397
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Exchange Server Update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/346397/exchange-server-update (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

The system is Windows Server 2008 R2 and i am trying to patch the server with KB5000848

The update fails to install both from windows update and i have tried to install it directly from Microsoft catalog.

I am getting the error with Code 8024200D

The troubleshooting i have made is :

1) Run Dism

2) Run sfc

3)Stoping services regarding windows update, renaming windowsdistribution folder and windowsupdate log file

I would need some assitance on this,

Thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-12*

Just as my previous post said, install the latest SSU KB4566425.    

Then, install KB500087 from here:    

Description of the security update for Microsoft Exchange Server 2019, 2016, and 2013: March 2, 2021 (KB5000871)    

https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-march-2-2021-kb5000871-9800a6bb-0a21-4ee7-b9da-fa85b3e1d23b     

-------------------------------------------------------------------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-12*

Hello,  

the exchange is 2013 version 15.0.1367.3 and i want to patch it with KB5000871 for the exchange.   

Is there any prerequisite to do so ?  

Thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-08*

Please install the latest SSU KB4566425, then restart computer and manually install KB5000848 again.    

https://support.microsoft.com/en-us/topic/servicing-stack-update-for-windows-8-1-rt-8-1-and-server-2012-r2-july-14-2020-1fd14b21-927c-087f-a7d2-a587e89ac4d4    

If still no help, follow the guide to Reset Windows Update components manually    

https://learn.microsoft.com/en-us/windows/deployment/update/windows-update-resources#reset-windows-update-components-manually    

-------------------------------------------------------------------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-07*

Hello the OS is Windows Server 2012 R2 my mistake

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-07*

March 9, 2021—KB5000848 (Monthly Rollup) is applied to Windows 8.1 and Windows Server 2012 R2, if your server OS is Windows Server 2008 R2, this KB cannot be installed.    

Windows Server 2008 R2 Standard is end of support on 1/14/2020.    

-------------------------------------------------------------------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
