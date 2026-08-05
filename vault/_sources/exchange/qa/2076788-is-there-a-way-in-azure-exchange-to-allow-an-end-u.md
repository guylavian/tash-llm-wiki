---
title: "Is there a way in Azure/Exchange to allow an end user to receive more external emails while still maintaining security."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2076788/is-there-a-way-in-azure-exchange-to-allow-an-end-u
question_id: 2076788
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-functions", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Is there a way in Azure/Exchange to allow an end user to receive more external emails while still maintaining security.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2076788/is-there-a-way-in-azure-exchange-to-allow-an-end-u (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an end user that works in a sort of community outreach role (far more external emails than the typical users) and many external emails that are inbound being blocked or quarantined. Once she receives an email from the external user I can whitelist it from there for future communications, but is there a way of allowing this user to receive more external emails without making her email account wide open to external threats.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-09-23*

You shouldnt be whitelisting those. Instead the user should be checking their quarantine and reporting any blocked as a false positive.  If that fails, then you as an admin can submit these

Thats the way to allow these and to better protect the account

https://learn.microsoft.com/en-us/defender-office-365/step-by-step-guides/how-to-handle-false-positives-in-microsoft-defender-for-office-365#handling-legitimate-emails-in-to-junk-folder-of-end-users
