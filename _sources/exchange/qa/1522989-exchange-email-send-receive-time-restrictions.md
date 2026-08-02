---
title: "Exchange Email - Send/Receive Time Restrictions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1522989/exchange-email-send-receive-time-restrictions
question_id: 1522989
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Email - Send/Receive Time Restrictions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1522989/exchange-email-send-receive-time-restrictions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

It there a way to restrict email send/receive times for a certain timeframe?  Example: Only allow send/receive during normal business hours.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-02-03*

You can use transport rules to cook up something that might work, but there are major downsides to such approach. Most importantly, any message that you reject will never be delivered (i.e. the sender server will not try to resend it say on Monday morning). Some organizations opt to include a disclaimer in the message, instead of blocking it outright. Moderation is also an option... but not realistic for any organization of size.

Another option is to block user's access to the service instead, i.e. set their account status to Blocked. Similarly, you can disable only access to Exchange Online, by means of configuring a CA policy, or toggling the protocol settings. This has the downside of causing annoying prompts from the various apps that users might have configured their accounts on.

Yet another alternative is to configure restrictions on the client side, but that assumes all the devices are managed. Outlook add-ins might also help.
