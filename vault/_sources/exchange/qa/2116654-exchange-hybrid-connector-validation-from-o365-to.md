---
title: "Exchange Hybrid connector validation from o365 to on-prem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2116654/exchange-hybrid-connector-validation-from-o365-to
question_id: 2116654
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
---
# Exchange Hybrid connector validation from o365 to on-prem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2116654/exchange-hybrid-connector-validation-from-o365-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We recently setup Exchange Hybrid on Classic mode. Completed without errors.

During setup we ensure that the Transport Certificate is valid and we assigned our 3rd party cert.

We checked on IIS that "Default Front End" certificates are assigned with 3rd party cert.

IIS 'Exchange Back End' is using the private "Exchange Server" certificate.

When checking Exchange online connectors and validating the O365-Onprem connector, it errors with

"450 4.4.317 Cannot connect to remote server [Message=SubjectMismatch Expected Subject: ...... Thumbprint:######"

When troubleshooting and Checking the certificate thumbprint from the error message on the server.  Determined that the thumbprint belonged to the private certificate used in the 'Exchange Back End'

Not sure why it's presenting the wrong certificate and not the front-end certificate?

Normal email flow is still working.

Appreciate anyone's feedback.

## Answers

_No answers on this thread._
