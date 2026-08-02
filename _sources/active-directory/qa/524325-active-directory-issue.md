---
title: "Active Directory issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/524325/active-directory-issue
question_id: 524325
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/524325/active-directory-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I demoted a dc successfully and removed everything from sites and services and when I tried to re-promote it I get an error that states:  

The operation failed because:  

The path chosen for the system volume is not accessible.  Please either manually delete the contents of the path or choose another location for the system volume  

Will some please help.  Thank you in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-12-04*

This problem with access to SYSVOL.   

In my case, a new SYSVOL folder was created on which the Domain Admins group had no permissions, it was not possible to add this group, but there was a SYSVOL_old folder next to it, which had these permissions, I changed the names and the promotion was successful.  

DO NOT CHANGE - System Volume Information - it has nothing to do with it  

sysvol.png

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-24*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-23*

Hello @Heba Wagih   ,    

I would like to advise you if you have demoted DC and if there is nothing on that server then just reinstall windows and promote it again.    

If the reply was helpful, please don’t forget to upvote or accept as answer. Thanks, Prakash    

PRAKASH T

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-23*

Not much to go on but the user may not have permissions or file system corruption may be another possibility. If it were me I'd rebuild it from scratch.    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new one, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
