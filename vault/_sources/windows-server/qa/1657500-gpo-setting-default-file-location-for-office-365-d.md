---
title: "GPO setting default file location for Office 365 doesn't apply correct"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1657500/gpo-setting-default-file-location-for-office-365-d
question_id: 1657500
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO setting default file location for Office 365 doesn't apply correct

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1657500/gpo-setting-default-file-location-for-office-365-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I'm trying to setup Office 365 using Group Policies. The policies seems to be applied correctly (they can be located under HKEY_CURRENT_USER\Software\Policies\Microsoft\office\16.0...) But the policies regarding file locations all seems to be ignored. 

As an example, I have set 2 policies for Excel under "Microsoft Excel 2016/Excel Options/Save":

-  "Save Excel Files as" 

-  "Default file location"

The first applies correctly, while the second seems to be ignored. I have tried both with UNC network path, mappede network drive and a local folder. All with the same result: only folders typed in manually at "file/Options/Save/Defalut File Locations" have any effect.

Any help would be appreciated - thx

/Jesper

## Answers

_No answers on this thread._
