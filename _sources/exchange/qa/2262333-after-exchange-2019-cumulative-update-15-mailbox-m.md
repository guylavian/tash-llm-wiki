---
title: "after exchange 2019 cumulative update 15, mailbox migration to exchange online stopped working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2262333/after-exchange-2019-cumulative-update-15-mailbox-m
question_id: 2262333
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# after exchange 2019 cumulative update 15, mailbox migration to exchange online stopped working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2262333/after-exchange-2019-cumulative-update-15-mailbox-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

after exchange 2019 cumulative update 15, mailbox migrations to exchange online stopped working. Does it have something to do with Extended Protection or whatever it's called? How can I make it work again?

It was working before, we were on CU12...

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-30*

Hi Braun, Thaddeus,

Thank you for posting your question in the Microsoft Q&A forum.

Extended Protection is enabled by default when installing Exchange Server 2019 CU14 or later, and there are some prerequisites or unsupported scenarios for Extended Protection. For example, Extended Protection can't be fully configured in a Modern Hybrid configuration (Exchange servers are published via a Hybrid Agent).

Currently, you can try to disable Extended protection temporarily to see if mailbox migration works again. This could help us to confirm if your issue is caused by Extended protection. Then you can check and meet all requirements before enabling extended protection again.

You can use a script and disable Extended protection for all Exchange servers:

.\ExchangeExtendedProtectionManagement.ps1 -DisableExtendedProtection

For more information about Extended protection and the script, please check:

Exchange Server support for Windows Extended Protection | Microsoft Learn

ExchangeExtendedProtectionManagement - Microsoft - CSS-Exchange

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
