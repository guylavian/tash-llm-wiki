---
title: "DKIM Setup with O365 and Local Exchange Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1402961/dkim-setup-with-o365-and-local-exchange-hybrid
question_id: 1402961
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# DKIM Setup with O365 and Local Exchange Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1402961/dkim-setup-with-o365-and-local-exchange-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a hybrid environment with O365 and local exchange. O365 is used to send a majority of all OB emails and processes all IB emails and relaying. Our local Exchange server is used locally for and OB SMTP relay server that is used by our local applications/TMS to send 'bulk' emails. We are looking to setup DKIM. Since the Exchange server and O365 Exchange both send emails on behalf of the same domain what is the best practice for getting DKIM setup.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-10-24*

To leverage DKIM in 365 , then all the messages to external recipients will need to go through 365 as you prob already know.

To set that up:

https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dkim-configure?view=o365-worldwide

Essentially:

-  Configure DNS for the custom domains

-  Enable DKIM for the custom domain(s) you send from.

This linked doc explains it all
