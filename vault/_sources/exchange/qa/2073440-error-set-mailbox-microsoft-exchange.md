---
title: "Error set mailbox microsoft exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2073440/error-set-mailbox-microsoft-exchange
question_id: 2073440
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Error set mailbox microsoft exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2073440/error-set-mailbox-microsoft-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have function to update mailbox, the form have recipient type and email address. If I update these 2 fields at the same time, I get error Ex0D6BFD. Microsoft.Exchange.Data.DataValidationException|There are multiple primary SMTP addresses. Please ensure there is only one primary address for each address type.

I debug c# code and cmdlet syntax is valid.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-19*

Hello, @Solomon Tran,

Welcome to the Microsoft Q&A platform!

Based on your description, I understand that you receive the error “Ex0D6BFD. Microsoft.Exchange.Data.DataValidationException|There are multiple primary SMTP addresses. Please ensure there is only one primary address for each address type.” when you update the recipient type and email address of your mailbox at the same time.

If it is convenient for you, could you please provide a screenshot of the error you got, and we might be able to glean more information from it.

From the error code you have provided, this error usually occurs when a mailbox is assigned more than one primary SMTP address, which is not allowed. You can use the following command in PowerShell to check your SMTP address information (Primary SMTP address starts with SMTP:).

If you really do not have multiple primary SMTP addresses set up, regarding your reference to “update these 2 fields at the same time”, what operations exactly did you make? Your reply will help to solve your problem as soon as possible, so I hope you can get back to me in your free time.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
