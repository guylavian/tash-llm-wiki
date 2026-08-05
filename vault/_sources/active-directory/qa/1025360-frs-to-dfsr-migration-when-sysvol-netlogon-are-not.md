---
title: "FRS-to-DFSr migration when sysvol/netlogon are not shared or replicated"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1025360/frs-to-dfsr-migration-when-sysvol-netlogon-are-not
question_id: 1025360
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# FRS-to-DFSr migration when sysvol/netlogon are not shared or replicated

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1025360/frs-to-dfsr-migration-when-sysvol-netlogon-are-not (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a unique situation (to me) with which I could use some assistance.    

I have a server environment with 4 domain controllers, general details below:    

DC01 = 2008 R2    

DC02 = 2012    

DC03 = 2016 Std.    

DC04 = 2016 Std.    

I am trying to add some new 2019 domain controllers but cannot due to the FRS warning during DCPROMO.    

The older DCs will be decommissioned and removed after new ones in place and domain functional level will be raised.    

Relevant information:    

-  DC02 is the primary FSMO holder and where the source SYSVOL and NETLOGON shares reside. SysvolReady parameter is set to (1).    

-  Domain is at 2008 R2 functional level.    

-  Replication is being done by FRS.    

-  All other domain controllers (DC01, DC03, DC04) do not have SYSVOL or NETLOGON shares present at all.  SysvolReady parameter is set to (0). <------I suspect this is the issue but wanted to confirm.    

Work Done so far:    

I have run replication tests which return no errors, but are only showing results for the DC I run it on.    

I also ran the FRSDIAG tool and the primary DC passes, but states it cannot communicate with the other DCs.    

I have confirmed all 4 DCs can see each other on the domain and there is no issues in ADUC or Sites and Services or Domains and Trusts.    

I have confirmed the SysvolReady registry value on each server located at 'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters' are in varied states (see above).    

My question is, in the current state, would it still be OK and relatively trouble-free to convert the domain to DFSR?    

Would that, in turn, help to create and sync the SYSVOL and NETLOGON shares across all DCs once converted?    

Should I be changing the SysvolReady registry entries and validating SYSVOL and NETLOGON are visible/replicated across all DCs prior to attempting conversion to DFSR?    

Any help/guidance would be appreciated and thanks in advance.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-09-27*

All other domain controllers (DC01, DC03, DC04) do not have SYSVOL or NETLOGON shares present at all    

How long has this been happening? If greater than tomebstone lifetime then you'll need to remove from network and seize roles to a healthy one (if needed)    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

then perform cleanup to remove them.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

then when domain health has been confirmed you can proceed.    

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019 or 2022, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
