---
title: "Exchange Server 2013 CU22 | Meeting issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/198210/exchange-server-2013-cu22-meeting-issue
question_id: 198210
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange Server 2013 CU22 | Meeting issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/198210/exchange-server-2013-cu22-meeting-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Expert,  

We have a user A who has a delegated permission on mailbox B.  

When User A sends a meeting from mailbox B's calendar to Mailbox C.  

It shows Organizer name as Mailbox C for same meeting where mailbox is only attendee. It should have been shown as organizer name as Mailbox B.  

It happens randomly.  

Any help would be appreciated

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-17*

Can we diagnose how active sync could create this issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-15*

Hi @Nitin Bhutani   ,    

Will this issue occur when user B sends a meeting invitation directly?    

-  Please try to log in to your mailbox on OWA and check whether the organizer of the meeting is displayed properly.    

-  Does user C use a mobile device to synchronize calendars through Exchange ActiveSync?    

According to the known issues released by Microsoft, when a user synchronize their iOS or Android device by using Exchange ActiveSync, they may unexpectedly become the organizer for a meeting to which they were invited.    

You can find the description of the issue in issue 1.2 in the article：Current issues with Microsoft Exchange ActiveSync and third-party devices    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
