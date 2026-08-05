---
title: "GPO Script downloads to local PC but never runs - Can run manually"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1290791/gpo-script-downloads-to-local-pc-but-never-runs-ca
question_id: 1290791
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO Script downloads to local PC but never runs - Can run manually

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1290791/gpo-script-downloads-to-local-pc-but-never-runs-ca (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a startup script running via GPO on the domain server. It works on most PC's.   

The odd part is the Event Viewer, on a local PC with the issue, shows a GPOFileSystemPath . On this local system, I can access this folder. I can copy the script. I can run the scrip. It applies perfectly (even on non-admin account).    

I tried adding an argument "-ExecutionPolicy Unrestricted -FILE " which did not work.   

I tried putting the entire path in the script name. Nope.   

I've deleted and readded.   

I've checked on permissions. (Like I mentioned, the local PC with the issue can get to the folder with zero issues)  

I tried cussing it.   

I even talking nice to it.   

Any ideas? 

FYI:  Info from Event Viewer  

SupportInfo1 2008020256  

SupportInfo2 150  

ErrorCode 4294770688

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-25*

Hello there,

I would recommend you to deploy a Run Registry Key instead. You can still deploy that with Group Policy:

If you want to deploy this on a Computer (so that it applies to everyone logging in on the computer), then, in your GPO, go to Computer Configuration -> Preferences (not "Policies") -> Windows Settings -> Registry -> New Registry Item, and create a new REG_SZ value under the path shown in the documentation (HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run), give it a meaningful Value name, and set the Value data to be the path of the executable on the computer.

If you want to deploy this setting on a per-user basis, then use the same method but on User Configuration instead of Computer Configuration (and HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run instead of HKLM).

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer--
