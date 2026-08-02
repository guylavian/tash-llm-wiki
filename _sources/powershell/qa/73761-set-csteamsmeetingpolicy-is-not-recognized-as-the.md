---
title: "'Set-CsTeamsMeetingPolicy' is not recognized as the name of a cmdlet"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/73761/set-csteamsmeetingpolicy-is-not-recognized-as-the
question_id: 73761
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# 'Set-CsTeamsMeetingPolicy' is not recognized as the name of a cmdlet

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/73761/set-csteamsmeetingpolicy-is-not-recognized-as-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I need to get the Teams Meeting participant list. I posted in the below forum    

https://social.technet.microsoft.com/Forums/en-US/1596142b-afba-431d-abdb-a8b6a1542b9f/how-to-capture-participant-list-in-a-meeting?forum=msteams    

I am getting the 'Set-CsTeamsMeetingPolicy' is not recognized as the name of a cmdlet    

    

I have installed Install-Module MicrosoftTeams module.    

Please help on how to execute Set-CsTeamsMeetingPolicy -AllowEngagementReport enabled

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-24*

During the meeting you can save the attendance list. After the meeting? Nope. At least not yet, but that's a limitation of Microsoft Teams, not PowerShell. Also, I don't now of a way to get the list during the meeting with PowerShell, but, again, that's a limitation of Microsoft Teams.  

get-teams-meeting-attendee-list  

33989875-view-or-export-a-list-of-users-who-attended-a-meet

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-24*

Hi Rich Matheisen,  

I need to send minutes of meeting with participants. There are 30 members join the meeting and I am unable to get all the attendees.    

Please let me know how to get the list of participant in a meeting in Teams.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-21*

Did you read the documentation for that module?  

The module you want is SkypeOnlineConnector.
