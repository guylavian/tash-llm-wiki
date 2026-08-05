---
title: "Exchange 2016 on Prem / How can I add folders to all users from Powershell."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/385853/exchange-2016-on-prem-how-can-i-add-folders-to-all
question_id: 385853
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
---
# Exchange 2016 on Prem / How can I add folders to all users from Powershell.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/385853/exchange-2016-on-prem-how-can-i-add-folders-to-all (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We want to start a retention policy of 30 days move to one folder. example a folder called 30-days. At 60 days to another folder. Example 60-days and 90 days delete.  

I have the retention policy setup but i can not find a way to add the folders to all mailbox's every user for standardization.   

My CEO swears his last job did it this way and he wants us to do the same.  

Thanks in advance.  

Bryan.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-07*

Hi Eric,    

Does that mean it is possible in the cloud version of office?    

@Eric Yin-MSFT

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-07*

Hi,    

I'm afraid it's not realizable in on-premise Exchange.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-06*

Hi Alex, Thanks for the reply and the research I really do appreciate it.    

I have seen similar post but I have not been able to find the actual .ps1 file the link goes to a script repository but I have tried searching with no luck.    

@AlexC

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-06*

Hi Bryan,  

Your CEO is probably talking about the Managed Folders feature, which was replaced by Retention Tags and Policies in Exchange 2010.  

The only approach I see for you is leveraging EWS for automating adding a folder and applying a Tag via powershell.  

I found this for you:  

https://blogs.perficient.com/2016/03/23/office-365-script-to-recreate-managed-folders-functionality/  

I hope this helps you a bit further and calm your CEO... :)  

KR, Alex
