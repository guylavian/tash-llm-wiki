---
title: "Known issues with Exchange servers and clients after enabling extended protection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1564024/known-issues-with-exchange-servers-and-clients-aft
question_id: 1564024
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Known issues with Exchange servers and clients after enabling extended protection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1564024/known-issues-with-exchange-servers-and-clients-aft (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Please summarize the known issues after enabling EP.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-22*

Enabling Extended Protection (EP) on Exchange servers provides significant security benefits against attacks like NTLM Relay and Ticket Replay, but there are some known issues to be aware of:

General issues:

-  Older clients (pre-Windows 10, Outlook 2016) may not support EP, resulting in connection failures. Before enabling EP, ensure that your clients are compatible.

-  Some existing Exchange configurations may need to be adjusted to work with EP. Microsoft provides detailed guidance on the necessary changes.

-  Certain management tools, particularly third-party ones, may be incompatible with EP and require updates or alternative solutions.

Specific issues:

-  In rare cases, enabling EP may disrupt Autodiscover functionality, affecting automatic client configuration.

-  Users of Outlook Web App (OWA) may encounter authentication issues if certain requirements are not met.

-  Some mobile devices, especially older models, may have difficulty connecting to Exchange with EP enabled. Prior to deployment, conduct thorough testing.

-  Third-party applications that rely on Exchange APIs may require changes or updates to function properly with EP.
