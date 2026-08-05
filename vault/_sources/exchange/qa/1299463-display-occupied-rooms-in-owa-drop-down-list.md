---
title: "Display occupied rooms in OWA drop-down list"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1299463/display-occupied-rooms-in-owa-drop-down-list
question_id: 1299463
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
---
# Display occupied rooms in OWA drop-down list

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1299463/display-occupied-rooms-in-owa-drop-down-list (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I use Exchange 2016 (on promise), I have created room mailbox named Example. User is using OWA. In his calendar he wants to enter an event in the room Example, then on the Details page there is a drop-down list Add a location or a room . If the a room is free, it is listed in the drop-down list. If the room is occupied at the selected time, it does not appear in the drop-down list. If the same is done in Outlook, the room is displayed regardless of occupancy. 

I have setup

`Set-CalendarProcessing -Identity Example -AutomateProcessing Autoaccept -AllBookInPolicy $true -AllowConflicts $true`

without success :/

Next try was

 `-AllRequestOutOfPolicy $true`

but no change anyway.

Some suggestions?

Thank you.

mez

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-07*

Thanks for the clarification and the proposed solution.

mez
