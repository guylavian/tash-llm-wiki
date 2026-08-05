---
title: "Microsoft Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1279707/microsoft-exchange
question_id: 1279707
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Microsoft Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1279707/microsoft-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning,

I have some questions regarding the creation of emails with company domain through office 365 subscription.

To recap, I added the company domain in the admin page, I added all the employee email addresses. Now the addresses are backed to register.

The first step I did is create the address on Microsoft, delete it from register and create an alias on register with the address @onmicrosoft.com

In this way the new mail sends and receives messages but when it sends them, the recipient sees a question mark next to the recipient's name as if it were not certified.

To the other addresses that I have not yet migrated from register, they have both Microsoft and register mail, i.e. if they send from the Microsoft mail to a corporate address, the mail arrives only on the Microsoft one. How come two equal addresses coexist and they don't receive the same emails?

I hope I explained myself because it is difficult to describe correctly. If there is someone who can help me, I will explain the problems gradually.

Thank you

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-05-08*

Thats expected if you haven't set up SMTP authetication:

https://learn.microsoft.com/en-us/archive/blogs/tzink/showing-a-question-mark-in-the-sender-photo-when-a-message-is-not-authenticated

This doc walks through the steps to enable that:

https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dmarc-configure?view=o365-worldwide
