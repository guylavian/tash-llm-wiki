---
title: "Exchange Hybrid: OWA Redirection Not Working for a Migrated User (On-Premises to Exchange Online)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2247687/exchange-hybrid-owa-redirection-not-working-for-a
question_id: 2247687
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Hybrid: OWA Redirection Not Working for a Migrated User (On-Premises to Exchange Online)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2247687/exchange-hybrid-owa-redirection-not-working-for-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Expertise, 

We are running a hybrid Exchange setup, with Exchange 2019 on-premises and Exchange Online (Office 365). After migrating a few users to Office 365, most of them are able to log into the on-premises OWA page and are correctly redirected to their cloud mailbox. But the affected user can login directly from exchange online. However, one specific user is experiencing issues:

Issue:

-  When the affected user tries to log in to the on-premises OWA (e.g., https://mail.domain.com/owa), they receive an error message stating that the email address or password is incorrect.

-  For other migrated users, when they attempt to log in via the on-premises OWA page, they are presented with the redirection URL and are successfully redirected to Office 365 OWA after clicking the link.

-  This specific user is not being redirected to the Office 365 OWA and is encountering the login error.

-  Additionally, the affected user is repeatedly prompted for their Outlook password, even though the credentials are correct.

Configuration:

-  The hybrid environment was set up using the Hybrid Configuration Wizard (HCW), and mail flow is functioning correctly.

-  The user's mailbox was migrated from Exchange On-Premises to Exchange Online.

-  Other migrated users have no issues with OWA redirection and can access their mailboxes on Office 365 without problems.

-  The TargetOWAURL setting in the Organization Relationship was checked, and it currently pointed.

Waiting for your response. 

Thank you.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-24*

Hi Dipto Adhikary,

Thank you for posting your question in the Microsoft Q&A forum.

We noticed that there is a post with the same issue description, and we have provided some suggestions. Please help to check if these suggestions are useful in your organization: Exchange Hybrid: OWA Redirection Not Working for a Migrated User (On-Premises to Exchange Online) - Microsoft Q&A 

Please also check if you have enabled Microsoft Entra password writeback to on-premises environment, and if the affected user changed password from M365 directly. Otherwise, the on-prem AD account may have the different password with account in Microsoft Entra.

For your reference:

Enable Microsoft Entra password writeback - Microsoft Entra ID | Microsoft Learn 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
