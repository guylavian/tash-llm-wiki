---
title: "Deleting SCP on Exchange servers...Need Help Please"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/429870/deleting-scp-on-exchange-servers-need-help-please
question_id: 429870
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Deleting SCP on Exchange servers...Need Help Please

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/429870/deleting-scp-on-exchange-servers-need-help-please (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi There,   

We have been running Ex2010, Ex2016 & Office 365 Hybrid Environment for two year... Now I am trying to remove ex2010 server. So I will start with deleting the old SCP points.   

Now I can see on SCP on two servers:  

On Exchange 2016 server:  

It has two SCP connectors: ex2010 and ex2016.  

On Exchange 2010 server:  

It has only one SCP connectors ex2010 .  

If I want to decommission Exchange 2010 server and delete SCP for Ex2010 only for now .  

Should I run this command only on Exchange server 2010:  

set-ClientAccessServer -identity EX2010 -AutoDiscoverServiceInternalUri $null  

?  

Or I have to run:  

set-ClientAccessService -identity EX01 -AutoDiscoverServiceInternalUri $null  

on Exchange 2016 server?  

Thanks a lot,  

ML

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-01*

So how do I find out if we have CAS Array? We only have one Ex2010 server.  

Thanks  

ML

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-11*

Hi @Namless Shelter   ,    

Good day!    

Based on my knowledge, the SCP is used to locate the Autodiscover service, and it stays in AD which means you could run it on both servers that have joined the domain.    

May I suppose the identity, EX2010 and EX01 are the same server? If so you could run either or them.    

And you can delete the SCP with ADSI EDIT:    

    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
