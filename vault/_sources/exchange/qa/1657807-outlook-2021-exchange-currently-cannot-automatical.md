---
title: "Outlook 2021 Exchange currently cannot automatically delete copies of retained emails on the server."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1657807/outlook-2021-exchange-currently-cannot-automatical
question_id: 1657807
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Outlook 2021 Exchange currently cannot automatically delete copies of retained emails on the server.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1657807/outlook-2021-exchange-currently-cannot-automatical (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I previously used Outlook 2010 with an Exchange mailbox, where copies of received emails on the server would be automatically deleted after being downloaded by the client. However, after upgrading to Outlook 2021 (32-bit) while still using Exchange, the copies of emails on the server are not automatically deleted anymore. This has led to frequent server space shortages, preventing the reception of new emails.

Upon attempting to change email settings, I discovered that the option to "Keep copies of messages on the server" could not be found. Only "Exchange account settings" were available, as shown in the specific settings screenshot below. Please assist in resolving this issue.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-20*

The method you provided is to create a new account. However, I already have an account. I can't find the interface to set up this email account. When I enter the email change interface, I can only see Exchange email settings. I attempted to find the settings interface for the email type, but both POP3 and IMAP are shown as unavailable for configuration.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-19*

Hi Will Young,

I would like to confirm with you whether you have used POP3 to configure the automatic deletion of email copies. According to your screenshot, I suspect that after you upgraded to the Outlook 2021 version, it automatically defaulted to the Exchange account settings. What you said is "Keep copies of messages on the server" does not exist in Exchange-related configurations. It is recommended that you modify the configuration to POP3 in Outlook 2021 to solve this problem. For specific operations, please refer to the following link: How to set up POP3 in Outlook
