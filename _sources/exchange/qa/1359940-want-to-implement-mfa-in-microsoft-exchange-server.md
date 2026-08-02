---
title: "Want to implement MFA in Microsoft Exchange Server on Premise 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1359940/want-to-implement-mfa-in-microsoft-exchange-server
question_id: 1359940
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-authenticator", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Want to implement MFA in Microsoft Exchange Server on Premise 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1359940/want-to-implement-mfa-in-microsoft-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to deploy 2FA or MFA for all the logins of the users hosted in my Microsoft Exchange Server. This server is the 2019 version and on-premise. I have checked and for my organization is impossible to deploy modern authentication because we have computers older than windows 11. So I have checked that one solution might be an hybrid modern authentication approach.

How should I do this? Should I buy licenses for each user in my Exchange Server? Can I do this without expending any money in licenses?

Thank you very much!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-05*

You need an Azure instance and AADConnect and Exchange Hybrid enabled:

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-05*

Well, you should already have the necessary licenses, there is no requirement to buy any specifically for HMA:

https://learn.microsoft.com/en-us/microsoft-365/enterprise/hybrid-modern-auth-overview?view=o365-worldwide#do-you-meet-modern-authentication-prerequisites
