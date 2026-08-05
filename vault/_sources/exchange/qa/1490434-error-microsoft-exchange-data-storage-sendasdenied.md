---
title: "Error: \"Microsoft.Exchange.Data.Storage.SendAsDeniedException: Can't send message.\" For mixed-use Outlook clients"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1490434/error-microsoft-exchange-data-storage-sendasdenied
question_id: 1490434
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator"]
---
# Error: "Microsoft.Exchange.Data.Storage.SendAsDeniedException: Can't send message." For mixed-use Outlook clients

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1490434/error-microsoft-exchange-data-storage-sendasdenied (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

One of our clients has outlook set up with one private Outlook.com account and two Office 365 mailboxes. When the outlook desktop application is set up with only the private account it works as expected, however after adding either one or both of the 365 mailboxes sending mails from the private outlook.com account always causes a bounce with error (Microsoft.Exchange.Data.Storage.SendAsDeniedException: Can't send message.).

Upon examining the sent mail I've noticed that either the Outlook application or the mailserver on outlook.com's end adds a strange alias to the mail, this doesn't seem to happen when operating outlook before adding the 365 mailboxes.  

This issue also persists when removing office through SARA and deleting appdata. And then re-installing office again.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-15*

Hi @Joris Slingerland  ,

I can understand that you've already tried methods like using SARA, deleting appdata and reinstalling Office, but Outlook profile is not changed in these steps.   

So, in case it's an issue with the current Outlook profile, I'd recommend trying to create a new Outlook profile, adding these accounts one after another and see if there would be any difference in the new profile. For detailed instructions on how to create and switch to new Outlook profile, hopefully you can find the link below helpful:  

Overview of Outlook e-mail profiles

If the error remains, I'd suggest creating another new Outlook profile and adding the 365 mailboxes first, then adding the outlook.com account along with them. This helps narrow down if it's the issue when outlook.com account is added as the primary account of the profile.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
