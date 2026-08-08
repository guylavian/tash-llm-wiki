---
title: "Voting options don't work in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1183552/voting-options-dont-work-in-exchange-online
question_id: 1183552
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-hybrid-management", "office-exchange-online"]
---
# Voting options don't work in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1183552/voting-options-dont-work-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have a hybrid environment with users on both on-premise and migrated to Exchange Online, but we noticed that the voting options don't work in the migrated mailboxes e.g. my mailbox is migrated and when I received an e-mail from an on-premise mailbox with a vote component I didn't see anywhere the voting message giving the availability to choose a vote. I have tried setting the TNEFEnabled parameter to $true for our domain but that didn't give any result. I also tried setting the 'Use rich text' option from the Exchange Online Management Panel but that also didn't help.

Is there any other setting that might be braking this feature?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-24*

Hi @Popov ,

You need to set the rich text option in outlook, in addition you can also try to create a new remote domain and enable TNEF, refer to this case: Outlook 365 users on Exchange Online can not send voting buttons

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
