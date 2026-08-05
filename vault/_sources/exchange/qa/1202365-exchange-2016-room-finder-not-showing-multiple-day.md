---
title: "Exchange 2016 room finder  not showing multiple days meetings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1202365/exchange-2016-room-finder-not-showing-multiple-day
question_id: 1202365
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 room finder  not showing multiple days meetings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1202365/exchange-2016-room-finder-not-showing-multiple-day (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears
We're using Room finder to book meetings in Exchange 2016 Rooms.
In Outlook we cannot see resources when selecting multiple days; via OWA I'm able to do it.
In Outlook I can force the booking for multiple day by manually inserting the room in the resources.
The problem is that I cannot see in the Room Finder more days of availability (not over 1 day).

In my outlook I've workinghours 07-19
Thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-13*

Dears
After some reserch (I found nothing..) I noticed this information alert in the Room Finder:

This said I'd close the answer confirming that it's "by design". Thanks :-(

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-10*

What's the build version of your Office 365? Do you have a room list distribution group that was added to the room mailbox in it? Please try to connect to Exchange Online powershell and run the following cmdlets to view that:
`Get-DistributionGroup -RecipientTypeDetails RoomList`
`$roomgroups = Get-DistributionGroup -RecipientTypeDetails RoomList`
`foreach($roomgroup in $roomgroups){Get-DistributionGroupMember -Identity $roomgroup.Name}`
Besides, here is a similar thread about Room Finder. Please check if it's helpful to you: Room List and Room Finder not working

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-10*

Hi @ A Ska ,  

Do you want to book a room on a recurring basis?

If this is the case, you can refer to the following two scenarios to book in the Outlook client:

1.Select the meeting room, check the availability time in the room finder, and click Make Recurring to set up the loop;

2.Use the scheduling assistant to see the availability of available rooms, and then set up recurring meetings in Room Finder's recommended rooms. 

 

Here's a guide to using the Scheduling Assistant and Room Finder together:

Use the Scheduling Assistant and Room Finder for meetings in Outlook - Microsoft Support
 

Hope this helps! Moreover, if the above is not your scenario or I have misunderstood anything, please correct me and provide us with detailed information about the issue including the screenshot so that we can better understand to further assist you.

Your patience and cooperation are highly appreciated.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
