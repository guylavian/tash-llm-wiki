---
title: "Exchange 2010 to 2016 Mailbox Moves - One user can no longer see Calendars"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/120971/exchange-2010-to-2016-mailbox-moves-one-user-can-n
question_id: 120971
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Volunteer Moderator"]
---
# Exchange 2010 to 2016 Mailbox Moves - One user can no longer see Calendars

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/120971/exchange-2010-to-2016-mailbox-moves-one-user-can-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So we've just finished moving all of our users to Exchange 2016 Databases. This has gone fine, except one particular user suddenly can no longer view other people's calendars. It's just this one user to our knowledge, and it doesn't matter who he tries to open, everyone's calendar says "No Connection".   

I checked Outlook Connection Status - All was good, even the connections to the calendars he was trying to open  

Recreated Outlook profile - same issue  

Cached mode vs. no cached mode - same issue  

Tried on a different machine - Same issue  

Tried on a different machine with Outlook 2019 (vs 2016) - Same issue  

Forced his machine to access Exchange CAS Server directly (vs through Kemp Load Balancer) - Same Issue.   

The Kicker - Tried using Outlook Web Access - this WORKS!  

Also, I can open his calendar no problem.   

Also, he can open ROOM mailbox calendars no problem.   

He can open shared mailboxes (Full mailbox contents) No problem.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-09*

Glad you have take such steps for troubleshooting, but still missed some, test the following scenarios and see the results:  

-  Remove the permissions and re-add permission in powershell for him, if you were using those calendar-specific permission, try full access this time.  

-  Restart Outlook in safe mode. Found a similar issue results from an add-in named "icloud for Outlook".  

-  Test Outlook autodiscover. Press ctrl and right click outlook icon, select "test Email autoconfiguration" and tick "use Autodiscover" for test.

Reference link: Outlook Shared Calendar shows no conenction - Resolution with screenshots  

No Connection error on Shared Calendar  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-15*

Thanks Eric,   

I'm almost at the point of doing a replacement of the mailbox.   

For the mailbox repair, there are many different options for corruption type. Do you know which would be most applicable?   

For the MFC MAPI where you suggested checking the permission on that folder, which folder did you mean exactly?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-09*

Thanks for the feed back. I did some investigation and here's what I learned.   

-  Outlook safe mode didn't help, I was hopeful it would, but it didn't.  

-  Autodiscover test seems healthy.  

-  This seems to be related to free busy only. I went and granted him Author permissions to my calendar, and it went from "No Connection" to suddenly seeing all my calendar items and details.  

When I removed the permissions (and cleared his cached OST file) he went back to seeing "No Connection" on my calendar. Default is granted access to my Free/Busy. So Granted him access to my Free/Busy specifically, but that didn't help.   

Free Busy info sharing seems to be working for everyone else in the company, at least everyone I've checked with.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-10-09*

Hi  

Compare permissions on a calendar to his calendar. I saw similar behavior with migrations from exchange 2010 to Exchange 2016 and had to go in and modify 1 or 2 users. cannot explain why it happened.
