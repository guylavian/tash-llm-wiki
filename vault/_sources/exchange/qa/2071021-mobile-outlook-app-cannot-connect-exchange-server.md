---
title: "Mobile Outlook App Cannot Connect Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2071021/mobile-outlook-app-cannot-connect-exchange-server
question_id: 2071021
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Mobile Outlook App Cannot Connect Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2071021/mobile-outlook-app-cannot-connect-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I can access the OWA page and log in without any issues. I can also log in using the iOS Mail Exchange account and the Samsung Mail/Gmail application with the same credentials.

As you can see, web and mail logins are successful, and requests are reaching the server.

The issue only occurs with the Outlook mobile app, which shows an error before the request reaches the Exchange server. Which SSL and TLS versions are supported by Outlook mobile app version 4.2435.1?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2024-09-17*

Hi, @İsmail Can ÜNSAL

As far as I know, Outlook mobile app version 4.2435.1 supports TLS 1.1 and TLS 1.2.

Support for older SSL versions (v2, v3) is generally deprecated due to security vulnerabilities.

More information can be found Azure support for TLS 1.0 and TLS 1.1 will end by October 31, 2024 - Microsoft Lifecycle | Microsoft Learn

Since Exchange Server tag focuses on Exchange and mail flow, we are unable to provide accurate and detailed guidance on the configuration of Outlook mobile app at this time.

You can continue to post your questions in the dedicated forum dedicated forum for Outlook for Mobile, there are more professional people here who can provide technical support.

Thank you for your understanding and support.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
