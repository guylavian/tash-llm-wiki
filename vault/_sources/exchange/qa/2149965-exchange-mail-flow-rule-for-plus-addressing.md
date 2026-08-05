---
title: "Exchange mail flow rule for plus addressing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2149965/exchange-mail-flow-rule-for-plus-addressing
question_id: 2149965
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange mail flow rule for plus addressing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2149965/exchange-mail-flow-rule-for-plus-addressing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm having trouble creating a rule that will catch all incoming + addressed messages.

Here's what I have so far:

-  Sender is NotInOrganization

-  Recipient address matches any of these text patterns: 

-  `username\+.*@domain\.com`

-  `^username\+.*@domain\.com$`

This does not catch email sent to ******@domain.com (or any other + label). What am I getting wrong in the regex?

Exchange also won't let me begin the string with a wildcard, so I can't use `.*\+.*@domain\.com` or `\+.*@domain\.com` catch all + addresses. This restriction doesn't make any sense at all. What's the point of a mail flow rule that requires you to predict the initial character of every email address? Surely, I'm missing something here.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-22*

Hi, @JayCarper-5747

After my testing, Exchange does have certain limitations, and it may not support all of the regex features you'd normally find in more flexible regex implementations. 

For some specific routing scenarios, you can follow this document to verify the availability of the plus address. Regular expressions in mail flow rules | Microsoft Learn

Plus addresses are not aliases configured on the mailbox, so they don't resolve to usernames in Outlook. This limitation causes the plus address to be not easily identified in the To or CC field of the message. 

To automatically identify and filter messages sent to plus addresses, it is recommended that you use inbox rules to take action on those messages.

Here is a PowerShell script to check the plus address for your reference. https://github.com/BohrenAn/GitHub_PowerShellScripts/blob/main/ExchangeOnline/CheckPlusEmailAddresses.ps1

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-01-21*

Check the header with a transport rule and see if that works.

Specifically the TO: field

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-21*

I have also tried 

-  Sender is NotInOrganization

-  Recipient address contains any of these words: '+'

This doesn't appear to do anything either.
