---
title: "Alter exchange meeting subject with powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1532178/alter-exchange-meeting-subject-with-powershell
question_id: 1532178
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Alter exchange meeting subject with powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1532178/alter-exchange-meeting-subject-with-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

we where utilizing the cmdlet  

`Set-CalendarProcessing -Identity "******@company.com" -AddOrginizerToSubject $true -DeleteSubject $true`
on one of our Meeting rooms, unfortunately this only affects new meetings created after the setting was changed.  

Now we have the request from our CEO to also alter the meeting subjects for meetings created before the setting was altered.  

I know there is no cmdlet like '`Set-CalendarItem`' or '`Set-MailboxItem`' available in Exchange Online,  

and the `Get-CalendarDiagnostics*` cmdlets only help with reading the existing items but not altering them.  

Therefore i'm asking if anyone found a workaround for this, or was able to create a script to 'touch' the objects in the calendar.  

Thanks for any input in advance.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-02-14*

Exchange Online PowerShell does not offer any item-level cmdlets, so you will not be able to do this. You can look at an API-based solution, either via the Graph API or EWS. Keep in mind that updating the item within the Room calendar will not update the corresponding items in either the organizer or attendee's calendars though.
