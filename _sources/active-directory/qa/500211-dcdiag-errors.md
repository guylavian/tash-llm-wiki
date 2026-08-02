---
title: "dcdiag errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/500211/dcdiag-errors
question_id: 500211
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# dcdiag errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/500211/dcdiag-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I'm trying to retire my DC (SOUTH-DC-2012) and I've also brought online a new 2019 DC (DSI-DC-2019). I ran a dcdiag and Im getting the follow errors:

Testing server: Default-First-Site-Name\DSI-DC-2019  

Starting test: Advertising  

Warning: DsGetDcName returned information for \SOUTH-DC-2012.DSI.local, when we were trying to reach  

DSI-DC-2019.  

SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE.  

......................... DSI-DC-2019 failed test Advertising

Starting test: DFSREvent  

There are warning or error events within the last 24 hours after the SYSVOL has been shared. Failing SYSVOL  

replication problems may cause Group Policy problems.  

......................... DSI-DC-2019 failed test DFSREvent

Starting test: NetLogons  

Unable to connect to the NETLOGON share! (\DSI-DC-2019\netlogon)  

[DSI-DC-2019] An net use or LsaPolicy operation failed with error 67, The network name cannot be found..  

......................... DSI-DC-2019 failed test NetLogons

Any suggestion or help for resolution would be greatly apprciated

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-08-04*

This one may help.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

also note; the two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
