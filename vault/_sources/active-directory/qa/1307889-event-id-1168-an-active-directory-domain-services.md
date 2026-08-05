---
title: "Event ID 1168 \"An Active Directory Domain Services error has occurred\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1307889/event-id-1168-an-active-directory-domain-services
question_id: 1307889
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Event ID 1168 "An Active Directory Domain Services error has occurred"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1307889/event-id-1168-an-active-directory-domain-services (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have reviewed the other 2 questions that are similar, but they don't have the same error values or internal ID. I am using a Windows Server 2012 edition, and my client has an employee that is unable to access a folder on the server. I was able to find a way for him to access it, but now there's some files missing inside and it won't allow access to open if typed in explorer window. Even says he can't copy files over to this folder, even though the permissions property has his profile on it, and the groups "everyone", and "domain users" on the same folder and files... This same employee makes changes to some files on there, and other users cannot see any changes he makes. I'm at a loss here on how to resolve this; are there any suggestions?  

Internal error: An Active Directory Domain Services error has occurred. 

Additional Data 

Error value (decimal):

-1023 

Error value (hex):

fffffc01 

Internal ID:

160207c9

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-06-17*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`	(run on PDC emulator)  

`repadmin /showrepl >C:\repl.txt`	(run on any domain controller)   

`ipconfig /all > C:\%computername%.txt`	(run on EVERY domain controller)   

`ipconfig /all > C:\problemworkstation.txt`	(run on problem pc)   

Also check the domain controller System and Replication (DFS or FRS) event logs for errors since last boot. Post the Event Source and Event IDs of any found. (no evtx files)   

then put `unzipped` text files up on OneDrive and share a link.
