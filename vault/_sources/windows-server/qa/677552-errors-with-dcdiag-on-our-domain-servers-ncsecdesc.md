---
title: "errors with dcdiag on our domain servers - ncsecdesc is failing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/677552/errors-with-dcdiag-on-our-domain-servers-ncsecdesc
question_id: 677552
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# errors with dcdiag on our domain servers - ncsecdesc is failing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/677552/errors-with-dcdiag-on-our-domain-servers-ncsecdesc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

ncsecdesc is failing  

Error: Domain\Enterprise Read-only domain controllers doesn't have replicating directory changes  

both domain servers are failing on this  

DC1 is a Windows 2012R2 server  

DC2 is a Windows 2019 server

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-19*

Hi all, just an update to this. I was able to work through this doc    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/replication-error-8453    

The first part under Top Solution was what fixed that issue.    

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-30*

Also try working through this one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/replication-error-8453    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-29*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-29*

I just read through the steps and now I think that this is over my head and don't want to create issues with everything.  

Anything else that I can test before I make any changes?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-28*

Might try a non authoritative synchronization  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
