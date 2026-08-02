---
title: "Youtrack with Outlook 365 (Microsoft Exchange Online)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2155379/youtrack-with-outlook-365-microsoft-exchange-onlin
question_id: 2155379
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Youtrack with Outlook 365 (Microsoft Exchange Online)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2155379/youtrack-with-outlook-365-microsoft-exchange-onlin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We are having trouble connecting YouTrack to Microsoft Outlook 365 to retrieve email. We keep getting the error:

```
MessagingException: The Microsoft Graph API failed to process the request to retrieve messages from the mail server
```

We have checked licenses, permissions, and Azure AD settings, but the issue persists. Could you please advise on how to resolve this?

This links also not helped:  

https://youtrack.jetbrains.com/issue/JT-86935/Mailbox-integration-with-MS-Exchange-fails

https://support.microsoft.com/en-us/office/mailbox-quota-exceeded-4b75b41f-dff8-4d53-9f44-cbca161618ce

Thank you.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-02-07*

As this is a third-party tool, you'll need to address the question to their support team. Judging by the error message, it's likely permissions/consent for the Graph API, but that's only a guess. Or it might be related to the mailbox itself, or anything really. The error message shown above is not one generated from Microsoft, but from the tool.
