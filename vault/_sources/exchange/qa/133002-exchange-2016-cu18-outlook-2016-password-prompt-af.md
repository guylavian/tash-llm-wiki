---
title: "Exchange 2016 CU18 - Outlook 2016 password prompt after upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/133002/exchange-2016-cu18-outlook-2016-password-prompt-af
question_id: 133002
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 CU18 - Outlook 2016 password prompt after upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/133002/exchange-2016-cu18-outlook-2016-password-prompt-af (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On prem Exchange here  

Exchange 2016 CU14 + Outlook 2016 Users - Everything was ok   

Exchange 2016 CU18 + Outlook 2016 Users with Cached mode on - Outlook prompt for password and crash with chart.dll error file   

Exchange 2016 CU18 + O365 - Everything is ok  

I have done the following :  

-  Reboot PC  

-  Repair Office 2016  

-  Uninstall / Réinstall Office 2016  

-  Update Office 2016  

-  Tried disabling MAPI   

-  Tried a lot of registry add on.  

Removing Cached mode resolve the issue, but i would like to keep that on.  

Anything else i should check ?  

Nick

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-21*

Hi @Nicholas Terreault  ,    

Exchange 2016 CU18 + Outlook 2016 Users with Cached mode on - Outlook prompt for password and crash with chart.dll error file    

Does this occur to all Exchange 2016 CU18 + Outlook 2016 Users in your environment?     

When does the password prompt appear, at launch or when you are using Outlook?     

As regards to the chart.dll error, would you please remove any personal information involved such as email address or domain name etc and then share a screenshot of the error so that we can do further research on this?    

Besides, I did some research about Outlook 2016 and chart.dll error, according to the discussion under several relevant links, it seems that the error could be related to some third-party antivirus software. So if the affected users happen to have this kind of software installed, it's suggested to try temporarily disabling it and see if there would be any improvement.     

Reference: Outlook 2016 and chart.dll error (multiple PCs)    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
