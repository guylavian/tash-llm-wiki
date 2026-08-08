---
title: "Upgrade win2012R2 domain controller to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/725316/upgrade-win2012r2-domain-controller-to-2019
question_id: 725316
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Upgrade win2012R2 domain controller to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/725316/upgrade-win2012r2-domain-controller-to-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have two R/W domain controllers MDC/ADC in HO and 9 RODC in different branches. All servers are having win2012R2 OS without any security updates and patches since 2017. Now we want to upgrade all the DC's to win 2019. First we want to updated two R/W domain controller in HO and later we will updated all the RODC one by one. I need sequence and procedure for this upgrade.  

Thanks in advance.  

BR,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-08*

want to use same IP's of existing DC's to new DC's, what steps it need to achieve this.    

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then move roles off, decommission demote first one, remove from network. Also perform cleanup if needed.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

Then stand up the new 2019 or 2022 (with existing name / address), patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can move on to next one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-08*

Hi DSPatrick,  

As i mention that existing win2012R2 domain controllers are not having any updates since 2017, so for upgrade these DC's doesn't need any service pack, hot fixes or Patches before upgrading it to win2019. And i want to use same IP's of existing DC's to new DC's, what steps it need to achieve this.  

Thanks.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-07*

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one and move on to next one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
