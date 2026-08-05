---
title: "GPO settings for Office 2013 are not applying"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2719000/gpo-settings-for-office-2013-are-not-applying
question_id: 2719000
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# GPO settings for Office 2013 are not applying

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2719000/gpo-settings-for-office-2013-are-not-applying (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Win Server 2012 R2 machine with Office 2013 Pro Plus SP1 x64 installed for the purposes of RDS Remote webapps.  

I noticed as I was finalising the setup that when ever I try to open a file from a DFS propagated network share in an Office app, it
 fails stating that the file is corrupt/requires repair. This only happens via DFS - local and server file path work fine on the same files.   

To fix this I created a new GPO to add the DFS paths as Trusted Locations and enable Trusted locations on the network across Excel, Word,
 PowerPoint. However, the Office settings on the GPO will not apply to the machine - other settings in the same GPO will apply, just not the settings on Office apps. This is happening on a version of Office downloaded from MS Volume Licensing and I have updated
 to the latest Office 2013 ADMX files today. Is there any way to correct this issue?  

Enabling the settings on a per user level really isn't a suitable workaround in this case.   

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2016-07-21*

Worked out my mistake after further troubleshooting - Issue has now been resolved.   

Realised my glaring mistake after running gpresult. The GPO was not applied a t a user OU but rather machine. Made the switch and the
 settings are now corrected.
