---
title: "PC joins domain but not listed in Active Directory, occasional login issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/983626/pc-joins-domain-but-not-listed-in-active-directory
question_id: 983626
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# PC joins domain but not listed in Active Directory, occasional login issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/983626/pc-joins-domain-but-not-listed-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently replaced a 2003 server with a 2019 (and have since decommissioned the old 2003 SBS server).    

Pretty static environment so it took awhile before I had to join a new PC to the domain. Having done so, it states the PC joins fine and generally allows the user to log in. However, some times the user cannot.    

I was looking into it and there is no entry in Active Directory for the PC.  Searched the whole tree. It isn't there.    

Test-ComputerSecureChannel shows True    

Setspn -1 <hostname> shows it is registered in the proper OU.     

Get-ADComputer shows "Cannot find an object with identity: <hostname>    

When I run a gpresult /r there is no CN= line under Computer.     

Also, I have unjoined and rejoined the domain. Renamed the PC (it didn't have an existing/old name in the first place, but figured I would do that anyway). No change.    

Obviously there is something broken or needs realigned on the DC or perhaps in Group Policy but I can't quite figure out what? Any advice? Thanks in advance.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-08-26*

Yes, I definitely had to do that migration.    

But you couldn't have done it without a two-step process. In order to do correctly there would have had to be a 2008, 2012 or 2016 domain controller added, migrate roles, demote 2003, FRS->DFSR migration, raise DFL to 2008, add 2019 domain controller.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-08-26*

Where are you looking? After the migration the old SBSComputers folder will no longer be used.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-08-26*

I'd check the system and DFS Replication logs as well as dcdiag results are clean.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-08-26*

So how did you move from 2003 to 2019? This should have required a two-step process since an FRS->DFSR migration would have been required before introducing a 2019 domain controller?    

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
