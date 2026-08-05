---
title: "Unable to send emails from OnPrem Exchange 2019 to external domains in Hybrid Setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1360981/unable-to-send-emails-from-onprem-exchange-2019-to
question_id: 1360981
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Unable to send emails from OnPrem Exchange 2019 to external domains in Hybrid Setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1360981/unable-to-send-emails-from-onprem-exchange-2019-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are Using a wildcard certificate (*.domain.com)

Unable to send emails from OnPrem Exchange 2019 to external domains in Hybrid Setup.

Verified certificate thumbprint on send connector, receive connectors and transport service.

Below is the error:

Outbound TLS authentication failed with error SubjectMismatch for Send connector Outbound to Office 365 - 84a08efe-69a3-4c36-8830-6673b4fab3a7. The TLS authentication mechanism is DomainValidation. Target is gmail.com.

Please advise.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-06*

-  Make sure there are no network devices between your on-prem org and Exchange Online that may be interfering

-  Is the inbound hybrid connector on the Exchange Online configured with the domain set on the cert?

https://learn.microsoft.com/en-us/exchange/certificate-requirements
