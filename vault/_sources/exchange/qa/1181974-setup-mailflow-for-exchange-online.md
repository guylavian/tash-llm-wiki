---
title: "Setup mailflow for Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181974/setup-mailflow-for-exchange-online
question_id: 1181974
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Setup mailflow for Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181974/setup-mailflow-for-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,

Greetings!

We had to setup mailflow for Exchange Online.

Domain                         Exchange Online

Contoso.Com               ******@contoso.com (Sender)

Contoso.Com               ******@contoso.com (Recipient)

Please suggest. Your quick help will be highly appreciated!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-20*

Hi,

Has the domain contoso.com been verified in your tenant and set as the default email domain?

If yes, you don't need to do any extra configuration if ******@contoso.com and ******@contoso.com are in the same tenant and their mailboxes are hosted by Exchange Online.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
