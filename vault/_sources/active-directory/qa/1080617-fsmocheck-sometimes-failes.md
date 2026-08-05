---
title: "FSMOcheck sometimes failes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1080617/fsmocheck-sometimes-failes
question_id: 1080617
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# FSMOcheck sometimes failes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1080617/fsmocheck-sometimes-failes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How can I determine what is the cause why FSMOCheck sometimes fails?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-10*

If further assitance is needed then please run;    

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log` 	(run on PDC emulator)    

`repadmin /showrepl >C:\repl.txt` 					(run on any domain controller)    

`ipconfig /all > C:\dc1.txt` 						(run on domain controller 1)    

`ipconfig /all > C:\dc2.txt` 						(run on domain controller 2 if exists)    

`ipconfig /all > C:\dc3.txt` 						(run on domain controller 3 if exists)    

Also check the domain controller System and Replication (DFS or FRS) event logs for errors since last boot. Post the Event Source and Event IDs of any found    

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-10*

Hi @Janus Bariñan  ,    

adding my 2 cents:    

I suppose @Anonymous   meant "dcdiag /v", which you can run at the exact same time when the issue occurs. You can redirect the output to a file, is just easier to read:    

```
dcdiag /v > dcdiag.txt
```

If the issues are intermittent, they could be related to an underlying network issue for example. In this particular case you would see some RPC-related errors in the output (and most probably also in the event logs as DSPatrick mentioned).    

Hope this helps!    

Regards,    

Stoyan

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-08*

Not much to go on, might check the domain health, also check the event logs for clues.
