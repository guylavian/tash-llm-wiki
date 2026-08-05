---
title: "Active Directory domain names can’t be resolved warning in Windows Server Essentials 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1294433/active-directory-domain-names-can-t-be-resolved-wa
question_id: 1294433
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory domain names can’t be resolved warning in Windows Server Essentials 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1294433/active-directory-domain-names-can-t-be-resolved-wa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I get the warning below in Windows Server Essentials 2016. (The adapter already points to the server address.) Any suggestions would be appreciated.

Everything still works! Thanks:

"Active Directory domain names can’t be resolved Alert details: Windows Server Essentials cannot resolve Active Directory domain names using the current DNS settings."

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-31*

I haven't seen the error again for a couple of days.  Maybe there was an update?  I plan on rebooting the server and seeing if the error shows up then.  If it does, I will try your troubleshooting ideas.  Thanks.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-30*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`	(run on PDC emulator)  

`repadmin /showrepl >C:\repl.txt`	(run on any domain controller)   

`ipconfig /all > C:\%computername%.txt`	(run on EVERY domain controller)   

`ipconfig /all > C:\problemworkstation.txt`	(run on problem pc)   

Also check the domain controller System and Replication (DFS or FRS) event logs for errors since last boot. Post the Event Source and Event IDs of any found. (no evtx files)   

then put `unzipped` text files up on OneDrive and share a link.
