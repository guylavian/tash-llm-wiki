---
title: "outlook exchange authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2068631/outlook-exchange-authentication
question_id: 2068631
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# outlook exchange authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2068631/outlook-exchange-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I can access the owa page and login without any problems.

I can also log in via iOS Mail exchange account and Samsung Mail/Gmail application with the same credentials.

As you can see, web and mail logins are successful, and requests are reaching the server.

Issue only occurs with the Outlook mobile app, where it shows an error before the request reaches the Exchange server.

USB debug log:
    "2024-09-11 16:56:51.863 510-3040  BufferQueueProducer     surfaceflinger
    E  [com.microsoft.office.outlook/com.microsoft.office.outlook.ui.onboarding.oauth.OAuthActivity$_14166#0] disconnect: not connected (req=1)"

Mobile outlook app error shown on UI: "an error occurred during authentication"

I also configured an exchange proxy, and I do not see any requests coming to the server backend.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-13*

What provides the modern authentication and conditional access requirements for Outlook? If there's anything I need to add or change, I will adjust my server accordingly.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-13*

Hi, @İsmail Can ÜNSAL

The Outlook mobile app can help you complete two-step verification, also known as multi-factor authentication, which helps you access your account more securely.

As far as I know, Outlook has requirements that include Conditional Access policies, Modern Authentication, and more, in addition to authenticating users.

Unfortunately, based on the USB debug log you provide, the Exchange Server tag cannot provide a more professional guide.

At the same time, the Outlook tag currently focuses on the Outlook desktop client, considering that your problem only appears on the mobile side, it is recommended that you post your problem here dedicated forum for Outlook for Mobile for more professional technical support.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
