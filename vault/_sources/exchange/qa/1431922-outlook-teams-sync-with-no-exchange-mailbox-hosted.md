---
title: "Outlook & Teams Sync with no exchange mailbox hosted"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1431922/outlook-teams-sync-with-no-exchange-mailbox-hosted
question_id: 1431922
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online", "office-teams-teams-business-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Outlook & Teams Sync with no exchange mailbox hosted

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1431922/outlook-teams-sync-with-no-exchange-mailbox-hosted (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have outlook configure with no Exchange mailbox hosted.

this doesn't give me any possibility to share outlook calendar with teams calendar

so I did another profile in outlook leaving it to configure the 365 account  by Automatic procedure. this is perfectly  working with teams and sync calendar except for I can't receive any email from external caused by DNS configuration of my email provider 

 so I thought it could be possible to have both account with 365 and without 365

in the profile base that it's working with my email provider, I tried to add an Account with 365 exchange configuration, but it stop me caused by email  of both Account, "no exchange mailbox" and 365, have same Email address.

is there any possibility to have both into same profile?

or better it could be: is there any possibility to automatically sync calendar of both account?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-20*

Hello @Max Lorenzoni  ,

the synchronization of the Teams calendar with the Outlook calendar only works if this is the same account. In other words, if you also have your Exchange mail addresses with Microsoft. Teams then automatically retrieves the data from Outlook.

I assume that you now also have a hosted Exchange server from yourself or from another provider. This is not possible because Teams does not fetch the data locally from Outlook, but from your Microsoft account. You would have to migrate your Hosted Exchange Mail Server to Microsoft.

Enclosed you will find an overview of the Microsoft Exchange online plans: https://www.microsoft.com/en-us/microsoft-365/exchange/compare-microsoft-exchange-online-plans

If this is helpful, please accept the answer. Thank you.
