---
title: "KB4602269 on Exchange Server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/318311/kb4602269-on-exchange-server-2016
question_id: 318311
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# KB4602269 on Exchange Server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/318311/kb4602269-on-exchange-server-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there ....   

I have an Exchange 16 on an SRV Std. 16 installed and patched to CU19 with the following updates (Like: KB5000871) .   

If i check the build number of that exchange i get:   

15.1.2167.2   

This website:   https://www.msxfaq.de/exchange/update/hafnium-exploit.htm  

Tells me that the fully patched version should be:   

15.1.2176.9   

Do i need to do anything else to get fully patched for haffnium ?  

THX

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-18*

Hi @BR0KK   ,    

It seems that the Update KB5000871 superseeds the update KB4602269    

Yes, and this is mentioned in the Security update replacement information of KB5000871:    

    

When it comes to verify the installation of the patches, as suggested by Andy, you can use the command he shared or run the HealthChecker script(Recommended). For more details, hopefully you can find the official link below helpful:    

Verify the installation of CUs & SUs    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
