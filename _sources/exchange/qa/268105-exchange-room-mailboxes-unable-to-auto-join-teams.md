---
title: "Exchange Room Mailboxes (unable to auto join Teams mettings)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/268105/exchange-room-mailboxes-unable-to-auto-join-teams
question_id: 268105
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-teams-teams-business-other-l1"]
---
# Exchange Room Mailboxes (unable to auto join Teams mettings)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/268105/exchange-room-mailboxes-unable-to-auto-join-teams (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good afternoon,    

Hoping to get some feedback with maybe an idea or to regarding the current issue we have.  It's more specific to Webex OBTP integration with Exchange and Teams, but  the issue we are seeing appears specific to the room mailboxes we are trying to resolve.  An example of what we are experiencing is listed below, but I think we might be close.  That said, here is our problem.    

Scenario with On-Prem Exchange/Teams/Webex(OBTP):    

-  I schedule a Teams meeting from my cube to room mailbox ABC    

-  I get up and go to room ABC and on the screen I see the OBTP Join button and push it    

-  The ABC room is able to join the Teams meeting, BUT is stuck in the lobby (doesn’t auto join)    

-  The ABC room has to be admitted by someone else already in the Teams meeting    

How can we get the room to auto join the meeting so when we click join it goes straight in and does not get stuck in the lobby (room mailboxes are On-Prem).  Was reviewing the following command and wanted to know if this might be related?  Ultimately how can we tell Exchange/Teams that this room is trusted and in the organization (it has the @keyman  .com like all other users)?    

Get-Mailbox ABC@keyman  .com | Fl room    

RoomMailboxAccountEnabled : False    

Thank you for any additional information you may provide.    

CWT

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-11*

Thanks EricYin,  

Understood.  Let me get more specific then focusing only on Room mailboxes.  I believe its possible that by running the parameter -EnableRoomMailboxAccount $true that the room may be able to join as an authenticated user since room mailbox accounts are disabled by default.  

Meaning, can I enable a room mailbox account in AD (set a password) and disable again after testing the results?  Does enabling/disabling the Room account in AD impact the room mailbox functionality and how others use/see it?  I'd like to test against one, but it is heavily used and cannot risk causing scheduling issues with it. Hope that makes sense.  

Thanks,  

CWT
