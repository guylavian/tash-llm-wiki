---
title: "I can only see 60 public folders in Exchange public folder manager"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1330213/i-can-only-see-60-public-folders-in-exchange-publi
question_id: 1330213
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 4
qa_tags: ["office-exchange-online"]
---
# I can only see 60 public folders in Exchange public folder manager

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1330213/i-can-only-see-60-public-folders-in-exchange-publi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I can only see 60 public folders in Exchange public folder manager. If I search for one not in view it comes up with No public folders exist in this organization. The PF's are there, I can see them in Outlook and PowerShell. Started this week. Out 3rd party IT company also confirmed they can only see 60 so noting in out internal environment causing an issue.

Can any one else check this who uses PF's please?

## Answer (community) — community member

*upvotes: 2 · updated: 2023-07-19*

i reported this too, its being investigated as a widespread issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-07-21*

Created a ms ticket. I got this)) 

From: Mandeep S <[******@mail.support.microsoft.com]>  

Date: Thursday, 20 July 2023 22:04  

To:   

Subject: public folder not visible - TrackingID#2307190050003830

Hello Veli,

 

I checked with my resources and got the confirmation that this is known behavior in Office 365 now that we can see upto 60 Public folder mailboxes in GUI as per the latest update.

 

Thank you so much for choosing Microsoft.

Warm Regards,  

**** Office 365 Ambassador  

Working Hours : Monday - Friday | 9:30 AM (EST) -5:30 PM (EST)

## Answer (community) — community member

*upvotes: 0 · updated: 2023-07-20*

I raised a ticket last week and was directed to this thread to confirm that it's the same issue.

More than 60 folders? You only see 60 in the EAC but they still exist and work outside of the EAC. Worse still, I'm forced to use the EAC now since the old Exchange Powershell cmdlets that used to do what we need were deprecated and stopped working earlier this year. It's EAC or nothing now, and EAC is broken.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-07-19*

Same issue with my tenant as well. 

Has anyone got a resolution to this yet. 

I went ahead and reported it per the suggestion @Aholic Liang-MSFT
