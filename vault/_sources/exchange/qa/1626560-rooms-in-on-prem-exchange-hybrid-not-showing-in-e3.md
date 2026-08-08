---
title: "Rooms in on-prem Exchange Hybrid not showing in E365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1626560/rooms-in-on-prem-exchange-hybrid-not-showing-in-e3
question_id: 1626560
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Rooms in on-prem Exchange Hybrid not showing in E365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1626560/rooms-in-on-prem-exchange-hybrid-not-showing-in-e3 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are running a hybrid Exchange and are starting to move some test users to Exchange Online. The one thing we have noticed is that we do not see any of the conference rooms in Outlook from the Exchange Online users in Outlook desktop or Web. Any idea how to get them to show up? I have made sure that the room are in the AAD sync and they are visible in the portal under users. Any help would be great!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-09*

Update: I was able to get the Room Lists to show in Outlook and Outlook Web, but not Outlook Mobile or Teams, but I do see the Room Lists, just no rooms, so I am halfway there.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-08*

Unfortunately, we cannot migrate any room mailboxes at this time as we use a 3rd party to sync and schedule the meetings. We can only sync to E365 or on-prem, not both. So as a test, I did a search in the room finder for the room list and it did show up, and I also see all the meeting rooms under the list. So, it does appear that this is working, however I have to manually search for the room list. Is this normal? I was able to search from both Outlook and Webmail, however Outlook mobile only shows the room list, but no rooms listed. So something is still not working correctly but looks like I am halfway there.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-01*

I have already done this. I created the room list and added the individual rooms to each. They still do not show up.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-29*

No, you didn't need to migrate room mailboxes. Please check if you can get these rooms via running get-recipient in EXO PowerShell. And did the cloud users can see the on-premises mailboxes?

Please also check if the recipientTypeDetails of the room mailbox in on-premises is set to MailUser. Based on my experience, after directory synchronization occurs, the `recipientTypeDetails` property of on-premises room mailboxes is set to MailUser. If yes, please add on-premises mailboxes to an on-premises room list. To do this, open the Exchange Management Shell on the on-premises Exchange server,

New-DistributionGroup -Name <NameOfRoomList> -roomlist

Add-DistributionGroupMember <NameOfRoomList> -member <OnPremisesRoomMailbox>
Reference: https://learn.microsoft.com/en-US/exchange/troubleshoot/calendars/cannot-add-conference-rooms-to-meeting-in-owa

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-27*

I am not migrating the room account (Or do I need to?). The room is an on-prem account and needs to be accessible by the on-prem and E365 users.
