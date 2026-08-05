---
title: "[Migrated from MSDN Exchange Dev] Meeting Rooms - Booking Buffer to avoid Conflicts with meeting over-runs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/144092/migrated-from-msdn-exchange-dev-meeting-rooms-book
question_id: 144092
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] Meeting Rooms - Booking Buffer to avoid Conflicts with meeting over-runs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/144092/migrated-from-msdn-exchange-dev-meeting-rooms-book (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange has been locked down and transitioned to Microsoft Q&A for support, we manually migrated this thread to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link] Meeting Rooms - Booking Buffer to avoid Conflicts with meeting over-runs   

[Original post]   

Does Exchange have the ability to add time buffers to a meeting room when booking time slots.  

I am trying to avoid conflicts, but moreover, I am trying to accommodate early arrivals / late finishes.  

As such, is it possible to add a buffer of 30 minutes to the front of the meeting for a room booking as well as add a 30 minute buffer at the end of the meeting.  

For example, a meeting is scheduled from 10:00 - 11:00 am, but the room booking is from 9:30 am - 11:30 am  

As such, the invitees time is only scheduled as busy for the hour, while the room booking is scheduled for 2 hours.  

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-29*

Hi Rob,    

Does Exchange have the ability to add time buffers to a meeting room when booking time slots.    

No. To the best of my knowledge, I am afraid it's not feasible to be realized with the built-in features available in Exchange.  As we can see in this document, room mailboxes do have some scheduling options, but there isn't a setting for the time buffer.    

After further research, I noticed that a similar suggest has been submitted in the UserVoice forum and I've added 3 votes for the idea. You could also vote for it or add your comments there to increase the chance that the idea gets noticed by the relevant product team:    

Add an option to enable meeting buffer time to the Booking Options section of Room Resource calendars to prevent back to back meetings.    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
