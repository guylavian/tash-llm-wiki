---
title: "Opening mailbox in OWA changes language in full Outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1253596/opening-mailbox-in-owa-changes-language-in-full-ou
question_id: 1253596
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator"]
---
# Opening mailbox in OWA changes language in full Outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1253596/opening-mailbox-in-owa-changes-language-in-full-ou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,  

I noticed a strange thing regarding Outlook client (2016 version).
Until now, user was working with connected shared mailbox within his outlook, and names of all the folders (Inbox etc.) respected CZ regional settings (which are set on the shared mailbox, I checked it with Get-MailboxRegionalConfiguration cmdlet ).   

After the user opened that shared mailbox within OWA, the names of those native folders in Outlook all changed to English.  

Even though that shared mailbox itself has CZ regional settings.  

We have Exchange 2016/Exchange Online hybrid, all users have mailboxes hosted online, and this particular shared mailbox is hosted onpremise (not sure if this is relevant but just to make it clear).
Anyone ever encountered that? It doesnt make any sense to me.
Thank everyone for any hints,
Tomas

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-04-26*

Hi @T Crha ,  

Please try changing the regional settings of the affected mailbox to a different language via either OWA or the Set-MailboxRegionalConfiguration cmdlet, then change it back and see if the language of the folder names can revert back to CZ regional in Outlook accordingly.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-04-25*

Hi @T Crha  ,  

Based on my experience, the language of the default folders could be affected by:

-  the regional settings of the mailbox, which can be checked with Get-MailboxRegionalConfiguration cmdlet

-  the language of Outlook client

From your description, both the above have the CZ regional settings, right?  

Did the user make any changes on the language settings when opening the mailbox in OWA?  

Does this issue affect the user's own primary mailbox as well?  

For current situation, below are some suggestions for reference:

-  Check if the shared mailbox has been added in other Outlook clients where the display language is set as English.

-  Double check it in OWA and make sure the language of the shared mailbox is set correctly:  

   

-  Run the `Outlook.exe /ResetFolderNames` command to reset the default folder names. (Exit Outlook and then run "Outlook.exe /resetfoldernames".  

   Reference: Issues with default folders in Outlook.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
