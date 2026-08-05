---
title: "Exchange 2016 CU 20 High CPU"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/350261/exchange-2016-cu-20-high-cpu
question_id: 350261
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 CU 20 High CPU

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/350261/exchange-2016-cu-20-high-cpu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I did a search but had trouble narrowing down to my specific so, hopefully, this is not a repost.  

Running Exchange 2016 Std virtualized in WS2016 Std environment.  Installed CU20 fine.  Rebooted.  Now Exchange services takes 30 minutes to load and, usually, not everything starts.  After waiting, I tend to need to manually start Frontend Transport and a few other required services.  

Also, two other issues have propped up.  After a while (not set time period), a CMD process pops up and uses 80-90%+ CPU and 4-6GB or memory.  This grinds Exchange down to a halt.  I log in and run Task Manager.  When it comes to, I terminate that CMD process and everything is fine again.  

The other issue is that I can no longer install any Microsoft Updates after CU20.  It downloads and installs then I get the "reverting back" after a few reboots.  

None of the old WS2012 Std / Exchange 2013 Std setups are affected.  All the WS2016 Std/Exchange 2016 Std setups experience the same issue.  

Any suggestions?  

Thanks in advance,  

Hedwig Poon

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-09*

Spoke too soon.  One site just spiked CPU.    

    

Also, these events are shown:    

    

    

    

I've attached a renamed EVTX file as a .log so I can upload it. 86061-21-04-08-eventsevtx.log    

Lastly, after terminating the CMD process, I see these in the event viewer (looks OWA related).    

    

Regards,    

Hedwig

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-09*

Hi Eric,  

Thanks for responding.  

-  No set time period.  It has started to happen on the 2016 sites shortly after CU20.  It happens once every 1-2 days.  Very random too.  If I don't stop it, it will just soak up CPU cycles and bog Exchange down to the point that all local Outlook say they've been disconnected.  

-  Other WS2016 would be the Hyper-V host and the Hyper-V guest for A/D.  Those can run Microsoft Updates fine.  The problem sites are all Hyper-V guest with Windows Server 2016 Std and Exchange 2016 Std (domain joined).  

I checked the event viewer but I couldn't find any specific error listing that coincided with the CMD process.  It had lots of error launching Exchange services but eventually they launch.  

I've read somewhere some people were having W3WP error.  Sometimes, I pop in via OWA to see if it's still working (quick response).  If the just spins, I figured it's got that CMD process again.  I wonder if OWA is causing it.  

Hedwig
