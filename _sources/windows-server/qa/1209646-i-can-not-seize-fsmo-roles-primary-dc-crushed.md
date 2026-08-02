---
title: "I can not seize FSMO roles. primary DC crushed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1209646/i-can-not-seize-fsmo-roles-primary-dc-crushed
question_id: 1209646
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# I can not seize FSMO roles. primary DC crushed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1209646/i-can-not-seize-fsmo-roles-primary-dc-crushed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I get this error when tryng to seize fsm roles: Primary DC crushed .

```
Move-ADDirectoryServerOperationMasterRole : Cannot find directory server with identity: 'd
At line:1 char:1
+ Move-ADDirectoryServerOperationMasterRole -Identity dc02.GladAfrica.local -Opera ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (dc02.GladAfrica.local:ADDirectoryServer) [M
   Role], ADIdentityNotFoundException
    + FullyQualifiedErrorId : ActiveDirectoryCmdlet:Microsoft.ActiveDirectory.Management.A
   icrosoft.ActiveDirectory.Management.Commands.MoveADDirectoryServerOperationMasterRole
```

2nd error on DNS MANAGER:
DC02	4015	Warning	Microsoft-Windows-DNS-Server-Service	DNS Server	2023-04-09 04:37:44 PM
The DNS server has encountered a critical error from the Active Directory. Check that the Active Directory is functioning properly. The extended error debug information (which may be empty) is "". The event data contains the error.
Please assist.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-04-10*

Do the 4015 errors repeat? Something here could help.  

https://support.hpe.com/hpesc/public/docDisplay?docId=c03366032&docLocale=en_US

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-04-09*

Please run;

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`	(run on PDC emulator)
`repadmin /showrepl >C:\repl.txt`	(run on any domain controller)
`ipconfig /all > C:\%computername%.txt`	(run on EVERY domain controller)
`ipconfig /all > C:\problemworkstation.txt`	(run on problem pc)

Also check the domain controller System and Replication (DFS or FRS) event logs for errors since last boot. Post the Event Source and Event IDs of any found. (no evtx files)

then put `unzipped` text files up on OneDrive and share a link.
