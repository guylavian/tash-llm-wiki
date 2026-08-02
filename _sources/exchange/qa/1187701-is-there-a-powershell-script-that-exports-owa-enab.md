---
title: "Is there a powershell script that exports OWA enabled mailboxes to CSV?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187701/is-there-a-powershell-script-that-exports-owa-enab
question_id: 1187701
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Is there a powershell script that exports OWA enabled mailboxes to CSV?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187701/is-there-a-powershell-script-that-exports-owa-enab (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When we onboard employees, all mailbox features are turned off by default via a short PS cmdlet. We discovered that there are some users where OWA (that should be disabled) is available and it should not be. I would like to compile a report of how many mailboxes that have OWA enabled, arranged in a table and exported as a CSV. Is this possible? If so, how can it be done?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-08*

Use the Get-CASMailbox to get the details about the protocols the mailbox is allowed to use.
