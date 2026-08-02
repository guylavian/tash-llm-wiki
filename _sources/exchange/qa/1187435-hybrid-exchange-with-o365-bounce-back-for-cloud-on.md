---
title: "Hybrid Exchange with O365 Bounce back for Cloud only mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187435/hybrid-exchange-with-o365-bounce-back-for-cloud-on
question_id: 1187435
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Hybrid Exchange with O365 Bounce back for Cloud only mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187435/hybrid-exchange-with-o365-bounce-back-for-cloud-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

Currently, our exchange is in hybrid with O365, and what we've discovered is that if we create a cloud only mailbox, when an internal application/printer using our on-prem exchange as the smtp relay is sent to the cloud only mailbox, it gets bounced back because the user's mailbox doesn't exist on the on-prem exchange. To get around this we have to create the user's mailbox through the on-prem exchange console. However, we'd like to avoid creating exchange on-prem mailboxes, and just create cloud only accounts.  Is there a way we can get the exchange on-prem to relay mail to O365 without failing because the user's mailbox doesn't exists on the exchange on-prem. Ideally, going forward we'd like to create cloud only mailboxes due integrations we've implemented, and have the exchange on-prem just be the smtp realy to those accounts without checking if the mailbox exists on the exchange on-prem, until we can remove the hybrid. 

Any advice would be appreciated

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-07*

Hi, send the messages from the applications/printers to the mailbox's onmicrosoft.com email address instead. 

The on-prem Exch Server will route through the hybrid connector to 365 since that email address wont exist on-prem.
