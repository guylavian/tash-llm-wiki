---
title: "Windows 2008 Active Directory 3 Servers, Domain unavailable when one of them goes down."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1196331/windows-2008-active-directory-3-servers-domain-una
question_id: 1196331
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Windows 2008 Active Directory 3 Servers, Domain unavailable when one of them goes down.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1196331/windows-2008-active-directory-3-servers-domain-una (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an old Windows 2008 AD with 3 DCs.   DC1 used to hold all the rolls, I moved them to DC3 a long time ago.  I am running into an issue where if DC1 is offline neither DC2 or DC3 can open the active directory users and computers.  I get the error that it does not exist or cannot be connected.    Also if I run a "netdom query fsmo"  it returns saying either that the RDC server can't be reached or that it can't connect to anything.  

Any ideas , tools would be much appreciated.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2023-04-05*

Please run;

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`	(run on PDC emulator)
`repadmin /showrepl >C:\repl.txt`	(run on any domain controller)
`ipconfig /all > C:\%computername%.txt`	(run on EVERY domain controller)
`ipconfig /all > C:\problemworkstation.txt`	(run on problem pc)

Also check the domain controller System and Replication (DFS or FRS) event logs for errors since last boot. Post the Event Source and Event IDs of any found. (no evtx files)

then put `unzipped` text files up on OneDrive and share a link.
