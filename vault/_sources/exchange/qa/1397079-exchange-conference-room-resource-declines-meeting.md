---
title: "Exchange Conference room resource declines meeting about 10 minutes after the meeting starts and is removed from the resource calendar allowing meetings to be booked over each other."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1397079/exchange-conference-room-resource-declines-meeting
question_id: 1397079
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 3
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange Conference room resource declines meeting about 10 minutes after the meeting starts and is removed from the resource calendar allowing meetings to be booked over each other.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1397079/exchange-conference-room-resource-declines-meeting (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are scheduling a conference room as the location for a meeting through my calendar with another user to test. The room accepts the meeting and then appears on both recipients calendars along with the rooms calendar. The issue we are experiencing is the meeting is from 1-2 at 1:10 the resource declines the meeting after it has already been accepted and started. This decline is causing issues where users think the room is free as the meting is removed from the resource after the decline message is sent out. We are using auto booking policy and there is not a user delegate over this room to allow/decline. Has anyone else faced this issue with a conference room resource?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-17*

I am having a similar issue at the moment, I have posted to the Microsoft Community forum - please see the link here - https://answers.microsoft.com/en-us/outlook_com/forum/outlk_win-outtop_classic-outsub_ofb/outlook-resource-calendar-shortening-to-10-minutes/78f009d6-3785-4e8e-b9af-7ded6107abba?rtAction=1729171761974  

I am wondering if the PostReservationMaxClaimTimeInMinutes - has anything to do with the issue.   

Kind regards,

Courtney.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-20*

Hi @Mike McCune,

Does this issue only occur on this specific room mailbox?

If yes can this issue be reproduced constantly?

If the issue can be reproduced constantly,

-  in the room mailbox (inbox or delete items folder) can you find any emails that update or cancel the meeting? 

-  have you configured the room mailbox on some meeting room devices?

-  please post the result of the cmdlet Get-CalendarProcessing -Identity "room mailbox" in Exchange Online Powershell

If possible I would suggest testing with another room mailbox and other users to see if the issue persists.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
