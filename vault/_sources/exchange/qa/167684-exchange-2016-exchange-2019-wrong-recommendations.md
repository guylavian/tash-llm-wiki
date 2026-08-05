---
title: "Exchange 2016 / Exchange 2019 wrong recommendations on Unified Communications Managed API"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/167684/exchange-2016-exchange-2019-wrong-recommendations
question_id: 167684
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 / Exchange 2019 wrong recommendations on Unified Communications Managed API

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/167684/exchange-2016-exchange-2019-wrong-recommendations (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Today I noticed something very weird. The official docs still links UCMA as a prerequisite for EX2016 and EX2019 on-premises. The linked version 4.0 is not even supported for later .net versions in compliance with Exchange Compat matrix and UCMA 4.0 is not supported on Windows Server 2012 R2, Windows Server 2016 or Windows Server 2019.    

The one that is supported is UCMA 6.0. Which is not mentioned in the docs or prerequisite checks.    

A customer Exchange 2016 was stuck on downloading updates via sconfig at KB3175339 (Sec fix for UCMA 4.0) which is listed in catalog but the download is no longer available.    

He is running Exchange Server 2016 CU 18 on Server 2016 LTSC. CU 18 or previous CUs never mentioned to check for the outdated version of UCMA 4.0, nor did Microsoft update them.    

Installing UCMA 6.0 was not an easy task though. Even when all named prerequisites are met the installer will quit after specifying the install path.     

Reason was found in the installer logs.    

The UCMA Setup tries to Install C++ Redist 2015-2019 x64 package version 14.12.x which is heavily outdated. Unfortunately the one that did the package for UCMA did a wrong hardcoded version check.    

So it required me uninstall UCMA 4.0 that's ok.    

But it also required me to uninstall C++ Redist 2015-2019 x64    

I would like to recommend anyone involved with packaging / assembling installers: never do hardcode version checks with version equal % but with equal or higher %, please.     

The current and secure version is C++ 2015-2019 Version 14.28.x    

2 Questions:    

why no one care to update the docs for UCMA 6.0 and actually reading the requirements on the download page     

why no one cared to update UCMA with Exchange CUs while it is a prereq for Exchange?    

UCMA 4.0 requirements    

    

UCMA 5.0 requirements    

    

UCMA 6.0 requirements

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-08*

Any news on this @Karl Wester-Ebbinghaus   ?    

Seems to me that Microsoft did not even take a look at this so far.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-09-04*

as the project has moved to a different repository the PR is now here  

https://github.com/microsoft/CSS-Exchange/issues/535

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-03-10*

C++ 2008 is officially out of support  

no need to be sorry. I am still waiting for a response from MSFT.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-08*

Sorry for all the messages.  

Got a reply on the GitHub of the HealthCheck script of last week Exchange vulnerabilities.  

They (Microsoft) will check internally with their Exchange team.  

https://github.com/dpaulson45/HealthChecker/issues/538

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-08*

Just spoke to Christian from Microsoft support which suggested me to install C++ 2008, since that the best and only solution for this issue.  

I have absolutely no clue why they would even consider saying anything like this.  

Will try it once more tommorow to see if I can talk to someone else on this matter.
