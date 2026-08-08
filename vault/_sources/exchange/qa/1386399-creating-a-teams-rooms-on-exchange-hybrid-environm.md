---
title: "Creating a Teams Rooms on Exchange Hybrid environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1386399/creating-a-teams-rooms-on-exchange-hybrid-environm
question_id: 1386399
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-teams-teams-business-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Creating a Teams Rooms on Exchange Hybrid environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1386399/creating-a-teams-rooms-on-exchange-hybrid-environm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears

We need to implement "Teams Rooms" to be used with specific devices located in the Meeting rooms.

At the moment we have several internal room resources on our Exchange Server on-prem (Hybrod mode).

I noticed there's a way to create rooms on Exchange Online but I'd like users to add the Teams room to the meeting when booking the Meeting rooms where there is a specific Conference device.

What's the best solution?

1- Create the room on exchange on-prem, sync to cloud, assign Teams room license

2- Create the toom on cloud, assign Teams room license?

3- other solution?

Thanks!

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-10-10*

Hi @A Ska,

To me both methods should work for you.

While I would suggest directly creating the room mailboxes in Exchange Online (cloud).

Here is also a thread in the similar situation for your reference:

Best practice to create room mailbox in Exchange Hybrid setup

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-16*

Dears,

I finally manage to solve it, thanks for the suggestion @Kai Yao  !

This is what I've done:

-  Created a room on premise with our policy settings

-  Synced to cloud

-  Reset the Room user password

-  Enabled the account

-  Enabled the Teams cloud license on Admin 365

-  Logged in on the Tablet Device by using Room username and password

et voilà!

Thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-10*

Dears

I created the room on the on-prem exchange. After syncing to the cloud I enabled the Teams Room license.

How to configure the Room account on my device?

I obviously have no password for the Room as it is a Room resource.

Can you tell me how to configure the device and use it for the meetings?

Thank you
