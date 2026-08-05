---
title: "Single Domain Controller Failing KB5007192 Every Day Since November"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/662267/single-domain-controller-failing-kb5007192-every-d
question_id: 662267
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Single Domain Controller Failing KB5007192 Every Day Since November

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/662267/single-domain-controller-failing-kb5007192-every-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,    

This one domain controller has been failing to install cumulative update KB5007192 for the past 30+ days.    

Can somebody please help me review the content of my windowsupdate.log log file that I just generated via Powershell and identify what could potentially be causing this?    

All other devices in the environment are updating with no issues.    

DC is on Windows Server 2016 Standard.    

This update literally tried to apply every single day, and fails every single day.    

From Windows Update Client in windows server:    

2021-11 Cumulative Update for Windows Server 2016 for x64-based Systems (KB5007192) - Error 0x800f081f    

From a patching audit done with Datto RMM:    

Same as SOAPCLIENT_SOAPFAULT - SOAP client failed because there was a SOAP fault for reasons of WU_E_PT_SOAP_* error codes    

Thanks,    

Jonathan157304-windowsupdate.log

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-12-14*

Simplest / safest solution may be to stand up a new one for replacement.    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2016, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-21*

Hi @Jonohue       

It may seem that some components of WUA are corrupted.     

First run Dism /Online /Cleanup-Image /RestoreHealth until  completed with no issues.     

Then  the following WU reset procedures: https://learn.microsoft.com/en-us/windows/deployment/update/windows-update-resources    

If that doesn't help I would do an in-place upgrade/reset using the latest ISO available, but be aware that doing this in a Domain Controller is risky. Please check this guide if proceeding that way:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers    

All in all, if the issue doesn't get resolved, instead of the inplace upgrade, it would be better to set up a secondary DC, move the FSMO roles after ensure that replication works ok, then deleting the old DC.    

Hope this helps with your query,    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-12-14*

Have you tried the client side script?  

https://www.ajtek.ca/wsus/client-machines-not-reporting-to-wsus-properly/
