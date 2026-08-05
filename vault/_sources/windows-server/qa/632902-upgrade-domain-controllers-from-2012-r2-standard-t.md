---
title: "Upgrade Domain Controllers from 2012 R2 STANDARD TO 2019 Datacenter on a Hyper V Host Server 2016 Standard"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/632902/upgrade-domain-controllers-from-2012-r2-standard-t
question_id: 632902
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Upgrade Domain Controllers from 2012 R2 STANDARD TO 2019 Datacenter on a Hyper V Host Server 2016 Standard

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/632902/upgrade-domain-controllers-from-2012-r2-standard-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I do have 2 Domain Controllers Windows Server 2012 R2 Standard in a Hyper V host 2016 Standard. I would like to Upgrade Domain controllers to 2019 Datacenter Edition. I am migrating the Master Domain Controller to a Physical Server and the other will be replicating this Physical one.   

So my Question is Whether I can upgrade these to Domain controllers from 2012 standard edition to Windows Server 2019 Datacenter edition without any issues?  

Any recommendations. Please help  

Thank you   

Ramach

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-18*

Not much to go on (lacking the rest of details) but if it was because of a backup process then it would have been normal.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-18*

Attached is the error. But it has been rectified immediately by the event 5004. What do you think ? Is this DC is good to go for an upgrade ?     

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-18*

I have done the dcdiag on one of the GC Domain Controller. This is the only part i got errors, rest of them were all passed

Doing primary tests

Testing server: Default-First-Site-Name\DC02  

Starting test: Advertising  

......................... DC02 passed test Advertising  

Starting test: FrsEvent  

......................... DC02 passed test FrsEvent  

Starting test: DFSREvent  

There are warning or error events within the last 24 hours after the SYSVOL has been shared. F  

replication problems may cause Group Policy problems.  

......................... DC02 passed test DFSREvent  

Starting test: SysVolCheck

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-18*

Should not be any issues.    

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
