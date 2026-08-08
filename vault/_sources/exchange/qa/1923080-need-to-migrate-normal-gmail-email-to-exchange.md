---
title: "Need to Migrate Normal Gmail Email to Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1923080/need-to-migrate-normal-gmail-email-to-exchange
question_id: 1923080
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Need to Migrate Normal Gmail Email to Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1923080/need-to-migrate-normal-gmail-email-to-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello there,

I’m encountering a problem with migrating my Gmail emails to Outlook. I have a Microsoft 365 Business Basic license. I've enabled IMAP on Gmail and attempted to create an app password in the security settings, but instead of the option for an app password, I only found a passkey setting. After these configurations, I proceeded to create a batch migration in the Exchange Admin Center by following the above steps. below

-  Log in to your Gmail account.

-  Go to Settings (usually represented by a gear icon) and select See all settings.

-  Navigate to the Forwarding and POP/IMAP tab.

-  Enable IMAP and save your changes.

-  Go to your Gmail account settings.

-  Look for the Security section.

-  Under  passkey and Security key configure the windows Hello.

Create a new IMAP migration batch:

-  Specify the Gmail server details (IMAP server address (imap.gmail.com),   Authentication – Basic, Encryption – SSL, Port – 993)).

-  Upload a CSV file with the list of email addresses, with corresponding username and password you want to migrate.(In password i have tried both way windows Hello and Gmail Password) but both ways failed.

-  Start the migration.

At last, the error state 

Data migrated:

Migration rate:

Error: ImapInvalidCredentialsException: The username or password for this account is incorrect. --> Imap server reported an error during LOGIN indicating that authentication failed: 'Invalid credentials (Failure)'.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-26*

Hi @kedar giri,

Welcome to the Microsoft Q&A platform!

Please understand that the tag “Microsoft Exchange Online” is for general questions related to Exchange Online. From the exchange side, please kindly check the steps in the guide to migrate your Gmail to O365 Migrate Google Workspace mailboxes to Microsoft 365 or Office 365 | Microsoft Learn.

However, based on my experience, the error could be that 2-Step Verification isn't enabled on your Google account.

-  Log in to your Google account.

-  Go to `Security` in your Google Account settings.

-  Under `Signing in to Google`, enable `2-Step Verification` and complete the setup.

Once 2-Step Verification is enabled, you should be able to create an app password.

-  Go to the `Security` section of your Google Account settings.

-  Under `Signing in to Google`, select `App passwords`.

-  Select the app and device you want to generate the app password for, and then generate the password.

Use this app password in the CSV file for your migration batch then you should be able to migrate successfully.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
