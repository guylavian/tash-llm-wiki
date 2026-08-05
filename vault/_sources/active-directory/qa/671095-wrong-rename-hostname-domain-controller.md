---
title: "Wrong rename hostname domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/671095/wrong-rename-hostname-domain-controller
question_id: 671095
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_affiliations: ["Mvp"]
---
# Wrong rename hostname domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/671095/wrong-rename-hostname-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello i'm Leonardo, i have big problem Whit 1 domain controller, i wrong rename hostname It, and i lose access to all user, the local administration is block, i was try   recovery or change hostname, i was success access to cmd from blocked login ( untilman.exe solution for recovery credential ) . any idea?    

Thanks for support    

-

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-22*

Hi @Leonardo Santorso       

The issue you are having is related to the solutions on this post:    

https://social.technet.microsoft.com/Forums/en-US/09f6599e-8ec3-4f4d-ba4e-ecaa55578080/renamed-dc-ad-broken?forum=winserverDS    

Basically using the NETDOM comand to rename Domain Controllers, instead of machine name changes or so, because NETDOM will change the SPN and DNS registration:    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc782761(v=ws.10)?redirectedfrom=MSDN    

Hope this helps with your query,    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-21*

Simplest solution may be to remove from network, seize roles (if necessary)    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

do cleanup to remove remnants    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

and stand up a new one for replacement.    

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new one, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
