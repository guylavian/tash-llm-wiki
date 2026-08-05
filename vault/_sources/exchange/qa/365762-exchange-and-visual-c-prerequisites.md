---
title: "Exchange and Visual C++ prerequisites"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/365762/exchange-and-visual-c-prerequisites
question_id: 365762
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange and Visual C++ prerequisites

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/365762/exchange-and-visual-c-prerequisites (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

Looking at exchange 2016 prerequisites    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2016    

only visual c++ 2012 and 2013 are supported but I can see many exchange servers have a lots of visual c++ versions.    

e.g. I found this exchange 2013 server have many visual c++ versions    

    

And I found opinion about visual c++    

https://superuser.com/questions/173403/why-are-there-so-many-different-visual-c-redistributables/619114#619114    

But what about Exchange?    

e.g. I have windows 2016 server and this server already have visual c ++ 2015-2019 installed and now I need to install Exchange 2016 on this server.    

    

Is it OK to install visual c++ 2012 and 2013 on this server which is prerequisites and leave visual c++ 2015-2019?    

Any advice?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-25*

The correct version of the VC runtimes are essential for many things in Exchange, notably installations and CU upgrades where if you have the wrong version, can cause the install and CU updates to fail in some very interesting ways.  The best way I've found to insure the correct VC runtimes are installed is to run the Microsoft maintained HealthChecker PowerShell script.    

This is the Prerequisites info page for Exchange 2019
