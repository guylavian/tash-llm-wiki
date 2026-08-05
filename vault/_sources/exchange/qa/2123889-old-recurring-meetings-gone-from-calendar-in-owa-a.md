---
title: "Old recurring meetings gone from calendar in OWA and Team"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2123889/old-recurring-meetings-gone-from-calendar-in-owa-a
question_id: 2123889
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1", "office-teams-teams-business-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Old recurring meetings gone from calendar in OWA and Team

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2123889/old-recurring-meetings-gone-from-calendar-in-owa-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Old recurring meetings that were in my calendar are now gone when checking my calendar in OWA and Teams. I am not the organizer, everyone else sees the meeting in their calendar except me.

If I create a recurring meeting it shows up in my calendar.

The meetings aren't in the deleted items folder.

I have tried signing out, and reinstalling Office.

Please spare some assistance, thank you.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-28*

Hi @MichaelS  

Please try using CalCheck to check for calendar issues.  

The Calendar Checking Tool for Outlook (CalCheck) is a command-line program that checks the Microsoft Outlook calendar for problems. The tool opens an Outlook messaging profile to access the Outlook calendar. It performs various checks on general settings, such as permissions, free /busy publishing, delegate configuration, and automatic booking. Then, each item in the Outlook calendar folder is checked for known problems that can cause unexpected behavior, such as meetings that seem to be missing.  

To use CalCheck, the Outlook calendar must reside on a computer that is running Microsoft Exchange Server. The tool doesn't work with IMAP, POP3, or other non-Exchange email accounts.  

For how to download and use, please refer to Information about the Calendar Checking Tool for Outlook (CalCheck)  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
