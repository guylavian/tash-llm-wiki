---
title: "Set-CsTeamsMeetingPolicy error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/504191/set-csteamsmeetingpolicy-error
question_id: 504191
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-teams-teams-business-other-l1", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Set-CsTeamsMeetingPolicy error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/504191/set-csteamsmeetingpolicy-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to Turn on meeting registration. After researching in the technical forum on how to get this functionality. I have run the following powershell command    

Install-Module -Name PowerShellGet -Force -AllowClobber    

Install-Module -Name MicrosoftTeams -Force -AllowClobber    

Connect-MicrosoftTeams    

Set-CsTeamsMeetingPolicy -AllowMeetingRegistration $True    

Then I got the error below. I just can't figure what to do next as I can't find any information on error.     

Any advice is appreciated.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-09-14*

You need to Add -Identity Global

The correct Command should be: Set-CsTeamsMeetingPolicy -Identity Global -AllowMeetingRegistration $True

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-08-06*

The latest versions of the Teams module include also the SfB cmdlets, part of which is Set-CsTeamsMeetingPolicy. The connection to SfB remote PowerShell should happen the first time you use a cmdlet, however it is known to fail. Try to open a new PowerShell window and connect again.
