---
title: "How can a shared exchange mailbox be added to mail clients (not outlook) when 2FA is activated?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1290079/how-can-a-shared-exchange-mailbox-be-added-to-mail
question_id: 1290079
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How can a shared exchange mailbox be added to mail clients (not outlook) when 2FA is activated?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1290079/how-can-a-shared-exchange-mailbox-be-added-to-mail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello together

We have migrated to Microsoft and have a number of shared mailboxes in addition to personal mail accounts. Now we want to set up these shared mailboxes in different mail clients (we have bring your own device). On the internet I see various instructions that simply add the account as IMAP/SMTP, but that doesn't work because we use a 2 factor authentication. 

Does anyone have a solution to this problem?

Thank you and best regards

Sandro

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-05-24*

You cannot add a shared mailbox directly in Outlook, as they do not have credentials. Well technically you can, but that's against the terms of use.

Instead, you should delegate access to a user (or group of users) via Full Access permissions. That way, the user can use his own credentials, including any MFA-related challenges, to configure the shared mailbox in Outlook. If you need detailed instructions, here's a sample article: https://www.michev.info/blog/post/3567/how-to-add-a-shared-mailbox-as-additional-account-in-outlook-2022-version
