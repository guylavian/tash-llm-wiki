---
title: "Recent Exchange Calendar Sync Issues with iOS Devices, Exchange 2019 & 9646 Errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2225472/recent-exchange-calendar-sync-issues-with-ios-devi
question_id: 2225472
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Recent Exchange Calendar Sync Issues with iOS Devices, Exchange 2019 & 9646 Errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2225472/recent-exchange-calendar-sync-issues-with-ios-devi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Title:

Exchange Calendar Sync Failures for some users with ExchangeIS 9646 App Log Errors

Details:

We have ~ten or so users that have reported calendar sync issues using Exchange On-Prem, iOS Native Calendar and our MDM (Ivanti MobileIron) over the past three weeks or so. For specific reasons, we cannot have them use Microsoft Outlook for Mobile client instead of iOS Native Cal + Mail. We're in Exchange Hybrid Mode with Exchange 2019 and a recent CU.

Their calendars on their iPhones appear either mostly or completely blank with no recent items syncing. In addition, we've even observed recent items "disappearing" for these users, where an item will appear and then drop off the calendar without warning. Outlook Desktop is fine and showing their full Calendars with no issues on that side. In addition, when a user is experiencing the issue, additional enrolled iOS devices experience the issue, with the same blank calendars, indicating that it's not specific to their device.

For the users reporting the issue, we've observed 9646 errors similar to the below:

Log Name:      Application

Source:        MSExchangeIS

Date:          3/13/2025 12:00:19 PM

Event ID:      9646

Task Category: (6)

Level:         Error

Keywords:      Classic

User:          N/A

Computer:      LocalExchangeServer.OurDomain.com

Description:

Mapi session /o=OurDomain/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Recipients/cn=XXXX.XXXXXXX with client type WebServices exceeded the maximum of 16 objects of type Session.

The users' Calendars were a little on the high item count side, ranging from 3,000 to 16,000+ items. We've observed the following appears to resolve the issue at least temporarily:

-  Reduction of calendar items to the past year or so, often moving thousands of items out of the main calendar.

-  Moving the mailbox to another database.

#2 seems to be only a temp solution as we have at least one user report the issue returning about a week after the move, necessitating #1.

This has been effective for most users, but I have one user who I've moved their mailbox and reduced their items to only around 1,500 and he is still reporting the issue.

We have cases with Microsoft, Apple and Ivanti, but none of them seem to be getting anywhere so I'm posting this as a bit of a "hail mary". What's vexing about this issue is why did this suddenly appear now? The only changes in our environment are users upgrading to iOS 18.3.1 (which could be a factor), and we did upgrade our MobileIron Sentries as well about a month ago. MobileIron proxies Activesync traffic directly to Exchange and generally doesn't do much else in this equation, and haven't reported anything unusual on their end.  

Has anyone else experienced anything similar? Any ideas on how to figure out what's going on? One tech recommended a Fiddler trace but that isn't easy given there's no native iOS Fiddler client. Thanks......

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-25*

You may try to check below steps:

Immediate Mitigations:

-  Adjust Exchange Throttling Policies:

```
Set-ThrottlingPolicy -Identity DefaultThrottlingPolicy -EASMaxConcurrency 16 -EASPercentTimeInCAS 30 -EASPercentTimeInMailbox 30
```

   (Adjust values based on your environment)

-  Implement Calendar Sync Filters:

```
Set-ActiveSyncMailboxPolicy -Identity Default -CalendarSyncWindowLength 12
```

   This limits sync to 12 months of calendar items.

-  Clear ActiveSync Devices:   For affected users, try removing and re-adding the ActiveSync partnership:

```
Remove-MobileDevice -Identity 
```

Mote troubleshooting steps: 

-  Calendar Archiving:

-  Implement a policy to archive old calendar items automatically

-  Consider using Exchange Online Archiving if in hybrid mode

-  Alternative Sync Protocol:

-  Test with Outlook for iOS (though you mention this isn't preferred)

-  Consider implementing Modern Auth if not already in use

-  Exchange Updates:

-  Ensure you're on the latest Exchange 2019 CU and SU

-  Microsoft may have addressed similar issues in recent updates

User still experiencing issues after calendar reduction:

-  Check for:

-  Recurring meetings with many instances

-  Calendar permissions/delegation issues

-  Corrupted calendar items (try `New-MailboxRepairRequest`)

-  Create a new test calendar folder and verify if it syncs properly

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-17*

Hi @KM_MB  ，  

Welcome to the Microsoft Q&A platform!  

There have been some recent issues with the IOS client, consider clearing the history and adding Exchange back to the email account. Effective for your temporary program to scale back the number of items, it may also be related to resource constraints. You can refer to: https://learn.microsoft.com/en-us/exchange/architecture/mailbox-servers/managed-store/managed-store-limits?view=exchserver-2019

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
