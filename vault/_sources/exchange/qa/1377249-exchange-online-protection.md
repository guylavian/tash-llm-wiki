---
title: "Exchange Online Protection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1377249/exchange-online-protection
question_id: 1377249
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online Protection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1377249/exchange-online-protection (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We use Zix AppRiver for email security/filtering with Exchange Online.  AppRiver scans and let the emails through.  Quite a bit of these emails ends up in the Microsoft 365 Defender quarantine. The reason is "High Confidence Phish" and "Malware".  Now I am being asked if there is any way to disable the quarantine.  They want Zix to take care of the emails.  Don't think I can, and I do not want to if I could.    Quite a bit of these emails are legitimate.

Any suggestions on how to fix this issue?  Thanks for your help.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-27*

You can disable some of the protection and exclude users:

https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-phishing-policies-about?view=o365-worldwide#common-policy-settings
