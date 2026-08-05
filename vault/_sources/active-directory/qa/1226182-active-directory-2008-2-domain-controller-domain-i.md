---
title: "Active Directory 2008 2 Domain Controller.  Domain issues when none PDC shuts down Active Directory Domain Service."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1226182/active-directory-2008-2-domain-controller-domain-i
question_id: 1226182
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory 2008 2 Domain Controller.  Domain issues when none PDC shuts down Active Directory Domain Service.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1226182/active-directory-2008-2-domain-controller-domain-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have two domain controllers DC1 (holds all roles), and DC2.   When I shut down Active Directory Domain Service on DC2 I cannot open Domains and Users or run commands like "netdom query fsmo" from DC1.   What would cause this?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-04-12*

Please run;

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`	(run on PDC emulator)  

`repadmin /showrepl >C:\repl.txt`	(run on any domain controller)  

`ipconfig /all > C:\%computername%.txt`	(run on EVERY domain controller)  

Also check the domain controller System and Replication (DFS or FRS) event logs for errors since last boot. Post the Event Source and Event IDs of any found. (no evtx files)  

then put `unzipped` text files up on OneDrive and share a link.
