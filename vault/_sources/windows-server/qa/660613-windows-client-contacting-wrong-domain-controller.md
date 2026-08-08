---
title: "Windows client contacting wrong domain controller?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/660613/windows-client-contacting-wrong-domain-controller
question_id: 660613
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["Mvp"]
---
# Windows client contacting wrong domain controller?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/660613/windows-client-contacting-wrong-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 questions that I hope someone can answer some of.  

If you have look at our current Sites and Service (ADSS) configuration below.

1. When a client comming from network 123.123.140 (Domain1 network) and wants to join the Domain1  

(This subnet is not present in ADSS). Which domain controller is the client trying to contact?

I´m asking this question, because this happends when we deploying new client machines with SCCM.  

out of 10 are getting this error message:  

[DJOIN.EXE] Unattended Join: Calling DsGetDcName for test.domain.com.  

*Warning [DJOIN.EXE] Unattended Join: DsGetDcName failed: 0x54b, last error is 0x0, will retry in 10 seconds...  

Error [DJOIN.EXE] Unattended Join: NetJoinDomain failed error code is [135*5]*  

Error [DJOIN.EXE] Unattended Join: Unable to join; gdwError = 0x54b

Our theory is that these 2 out of 10 clients are contacting domain controller in Domain2 because of some strange reason.  

But we cant figure out why. Hope someone can contribute with som ideas that we not yet has thouht of.

2. Why cant I see all the subnets in ADSS, it looks like only 24 subnets are present?  

(Maybe there is some other intelligent solution that has replaced this solution with Sites and Services.  

Or am I looking att the wrong place?)

SITES  

-Subnets  

10.0.0.0/8  

10.12.3.0/16  

123.123.102.0/19  

123.123.103.0/21  

123.123.104.0/21  

123.123.105.0/22  

123.123.106.0/26  

...etc

Site1 (Domain1 (test.domain.com))  

-Servers  

-dc1  

-dc2  

-dc3  

-dc4

Site2 (Domain2(test2.domain.com))  

-Servers  

-dc5  

-dc6  

-dc7  

-dc8

Update 2021-12-12:  

Domain1(Site1) and Domain2(Site2) are in the same geograhical location  

Secondly, it applies to all models, and the same client usually works the second try.

Really appreciate your answer

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-12-12*

Read on here     

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/enabling-clients-to-locate-the-next-closest-domain-controller    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-17*

Hello @Bit-101       

This is very likely to a GPO that applies to those machines, which links them with that site for assignement or an SCCM policy applying for the same purpose as in (https://learn.microsoft.com/en-us/mem/configmgr/core/clients/deploy/assign-clients-to-a-site)    

Three options:    

a) check the machine for the next registry key: [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Mobile Client]    

If present delete the keys under it that predefines the assignement.    

REG delete "hklm\SOFTWARE\Microsoft\SMS\Mobile Client" /v GPRequestedSiteAssignmentCode /f    

REG delete "hklm\SOFTWARE\Microsoft\SMS\Mobile Client" /v GPSiteAssignmentRetryDuration(Hour) /f    

REG delete "hklm\SOFTWARE\Microsoft\SMS\Mobile Client" /v GPSiteAssignmentRetryInterval(Min) /f    

b) Check group policies applies using the command GPRESULT /H C:\temp\gpos.html and check what from the set is applicable    

c) Check the SCCM policies and boundaries applied to those specific computers that give you problems.    

Hope this helps with your query,    

------    

--If the reply is helpful, please Upvote and Accept as answer--
