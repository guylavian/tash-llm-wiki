---
title: "SYSVOL no longer sync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/239668/sysvol-no-longer-sync
question_id: 239668
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# SYSVOL no longer sync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/239668/sysvol-no-longer-sync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I've got here a small domain with two Server 2019 DCs (Build 17763.1637)  

Since some Weeks there is no replication between the SYSVOL share.  

SFC /ScanNow	All fine  

DcDiag All fine  

Eventlog nothing special  

dfsdiag /TestDCs All fine  

dfsdiag /TestReferral /DFSPath:\mcr.local\SYSVOL /FULL All fine  

dfsrdiag ReplicationState reports 250 files not sync  

How can I fix this?  

RetoFelix

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-22*

Hi,  

As Dave said , you can check which DC can't replicated from the other, and try to operate a non-authoritative synchronization on the problematic DC.  

Before any changes , back up the SYSVOL folder for both the DCs.  

If there are any updates, welcome to share here!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-21*

Not much to go on but try the non-authoritative synchronization.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization    

--please don't forget to Accept as answer if the reply is helpful--
