---
title: "Converting Exchange2010 to 365 - Exchange patching questions."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/148648/converting-exchange2010-to-365-exchange-patching-q
question_id: 148648
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Converting Exchange2010 to 365 - Exchange patching questions.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/148648/converting-exchange2010-to-365-exchange-patching-q (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I 'm working with a company now that had the IT person leave unexpectedly. I have looked over the system and there are a number of updates I need to make.   I have begun replacing their old DCs so now I am moving on to Exchange.  They have Exchange 2010 SP1 RU3 running on Windows 2008r2.  They have 1 server running CAS and HUB roles and two servers running MBX rolls.  There is no DAG or load balancing so it seems a simple layout.  They want to move to Office 365 Exchange Online.  They have about 250 users so I think I need to do a full hybrid type conversion since they won't all be done the same weekend.  As I have begun research it looks like I need to first update the servers to the latest Exchange 2010 SP and Rollup which I think is SP3 RU30 before I can start moving to the cloud.  I hate messing with such old servers when the plan is for them to just stay up until the move is accomplished but it seems that is required.  

My initial questions:  

-  Is SP3 RU30 correct?  

-  Can I go straight to that patch level or do I need to do intermediate patching?  

-  Am I missing a more simple way of doing this?  

If you know of a better place for me to post this just let me know.  

As Always, Thanks for your help!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-03*

@EST_IT       

-  For running HCW, you just need to update to Exchange 2010 SP3, the latest version is not necessary, but better if install. You can have a look about this article: Office 365 Hybrid Configuration wizard for Exchange 2010:    

     

-  You need to update to Exchange 2010 SP3 first, then update to Exchange 2010 SP3 RU 30(If you want to use RU30).  As far as I know, update from Exchange 2010 SP1 to Exchange 2010 SP3 needs two KB which doesn't provided download now. If you encounter this problem during the installation process, you may need to open a case to Microsoft to obtain the installation package.     

-  For 250 users, the hybrid is the most suitable migration method.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
