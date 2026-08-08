---
title: "AppLocker GPOs marked as applied but Rules are not enforced"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3191063/applocker-gpos-marked-as-applied-but-rules-are-not
question_id: 3191063
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 12
qa_tags: []
---
# AppLocker GPOs marked as applied but Rules are not enforced

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3191063/applocker-gpos-marked-as-applied-but-rules-are-not (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Community,

We have been experiencing a problem with AppLocker GPOs in a Windows 10 Environment.

The Domain functionality level is: Server 2012R2

Domain Controllers are running: Windows Server 2016

Workstations are running: Windows 10 Enterprise Build 17134

We have 2 GPOs; one containing DLL AppLocker Rules and one containing EXE, Script, Appx etc.. Rules.

When running a gpupdate /force on an affected workstation and getting the gpresult the GPOs appear to be applied and are marked as winning however the contents of C:\Windows\system32\Applocker files are not being updated and recent rules added to both GPOs
 are not being applied. i.e. a new application which has been whitelisted will not run for the user albeit being specified in the applied GPO.

Can someone please shed some light into this issue? 

Help is highly appreciated!

Kind regards,

Jason

## Answer (community) — community member

*upvotes: 0 · updated: 2019-02-04*

Hi Jason

My name is Sarah Kong and I am an independent adviser that is here to try and help you with your issue.

Unfortunately you are in the wrong forum.

You need to post your question in the server technet forum.

See link below.

Have a great day!

https://social.technet.microsoft.com/Forums/Win...
