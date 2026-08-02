---
title: "Opted out of Previews VIA GPEDIT.MSC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4297559/opted-out-of-previews-via-gpedit-msc
question_id: 4297559
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: []
---
# Opted out of Previews VIA GPEDIT.MSC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4297559/opted-out-of-previews-via-gpedit-msc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The person msgrogms on the locked thread that said this:

"Sadly as a Home user you do not have an option as I can tell.

Pro users can opt out of Preview Builds via Group Policy Editor.

Computer Configuration, Administrative Templates, Windows Components, Windows Updates, Windows Update for Business, Manage Preview Builds, Enable, Disable preview builds"

IS WRONG. I TRIED THIS ON MY WIN 10 PRO MACHINE AND RESTARTED AND DID A WINDOWS UPDATE AND THE PREVIEW CAME BACK. IT'S CALLED:

2022-11 Cumulative Update Preview for Windows 10 Version 22H2 for x64-based Systems (KB5020030)

IT CAME BACK SO DISABLING THIS FEATURE AND HITTING APPLY DID NOTHING JUST LIKE ON THE DISCUSSION CALLED: What is a cumulative update preview.

WE WILL NOT FIND A SOLUTION TO THIS.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-03*

Hi Choose,  

 I am Sumit here to assist you with this question.   

Simply editing a GPO rather than exiting correctly would put you into Beta Channel.  

But as your device might not be 11 compatible, it is fine.  

Optional updates are released for retail versions too, in the second half of the month. This is by design.  

The optional update is released as a mandatory update on the second Tuesday of the subsequent month.  

Hope that helps.
