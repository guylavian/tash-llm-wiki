---
title: "Exchange 2010 - 2016 hybrid setup PART2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/139350/exchange-2010-2016-hybrid-setup-part2
question_id: 139350
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange 2010 - 2016 hybrid setup PART2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/139350/exchange-2010-2016-hybrid-setup-part2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi ,  

i have a scenario where a customer is still running an Exchange2010 and they now want to migrate to Exchange online.  

There is no hybrid config yet.  

Can someone confirm my architecture :  

-  i install a new exchange 2016 next to the 2010 - mailboxes keep getting hosted on 2010  

-  i enable mrs endpoint proxy on the 2016 and load balance to the new 2016 server  

-  i run the hybrid config on this 2016 server  

-  i migrate the mailboxes that are hosted on ex2010 thru the ex2016 to O365  

Following the reply from AndyDavid which says this approach is ok BUT also states that you can still run the HCW on the Exchange2010, i came across this article from Steve Goodman  

https://practical365.com/exchange-server/why-you-shouldnt-install-an-exchange-hybrid-server/  

When i read the article - it states that it is better to run the exchange2010 in hybrid rather than installing the 2016 and run the HCW there.  

Installing the EXchange2016 will add additional steps & troubleshooting steps ...  

Can someone clarify ? i think both are possible , but still don't know what is the best approach ...   

kind regards,   

Filip

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-27*

Hi @Filip Soogen       

Yes, as Andy says, both two are supported ways.     

For the 1st way, upgrade Exchange 2010 hybrid to 2016 hybrid, detailed steps can be seen here: Step-by-Step: How to upgrade a Legacy Hybrid Exchange Server to 2016    

For the 2nd way, just follow the guide provided by Exchange deployment assistant, migrate your mailboxes to exchange 2016 first then deploy the hybrid ( mail migration advisor ).    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
