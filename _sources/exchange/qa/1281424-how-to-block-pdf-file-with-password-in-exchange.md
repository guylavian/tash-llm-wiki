---
title: "How to Block pdf file with password in exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1281424/how-to-block-pdf-file-with-password-in-exchange
question_id: 1281424
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to Block pdf file with password in exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1281424/how-to-block-pdf-file-with-password-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have done to configure mail rules in exchange server to block any attachment with password, but i still able to receive pdf file with password

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-11*

Hi @evan,

I created and encrypted a pdf file in Word, and send a message with this pdf attachment.

The mail flow rule did block the message.

To me I suppose the cause may be with the pdf file's format, as according to this link: Use mail flow rules to inspect message attachments in Exchange Online

This condition matches messages with attachments that are protected by a password. Password detection only works for Office documents, .zip files, and .7z files.

Is this issue occurring to all encrypted pdf files?

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
