---
title: "Connect Exchange calendar and Office365 calendar"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1193768/connect-exchange-calendar-and-office365-calendar
question_id: 1193768
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Connect Exchange calendar and Office365 calendar

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1193768/connect-exchange-calendar-and-office365-calendar (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The following technical setup:

- 

-  E-mail runs via Hosted Exchange

- 

-  Microsoft 365 is used in parallel

The problem: When I receive an appointment or notification via Teams (i.e. Office 365), they do not appear in my Outlook calendar (and vice versa).

In the end, the same mail address always appears to the "outside" - but apparently two systems are addressed behind it, which leads to the problems.

How can this be synchronized or in general be solved?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-29*

Hi @ Its_winter_time ,

Just want to confirm that calendars for Teams in M365 need to be synchronized with mailbox calendars hosted in your on-premises Exchange server?

 

For cloud users, the Calendar section in Teams is connected to their Exchange Online (EXO) calendar.

For calendar access to work with on-premises mailboxes, users with on-premises mailboxes must be synchronized to Azure Active Directory. You need a hybrid deployment for on-premises Exchange Server to enable interaction with Microsoft Teams.

For more information, please refer to the following links:

Configuring Teams calendar access for Exchange on-premises mailboxes - Microsoft Community Hub

How Exchange and Microsoft Teams interact - Microsoft Teams | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
