---
title: "Hybrid Exchange - on-prem user needs to send mail to a 365-only address"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/236882/hybrid-exchange-on-prem-user-needs-to-send-mail-to
question_id: 236882
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-teams-teams-business-other-l1"]
---
# Hybrid Exchange - on-prem user needs to send mail to a 365-only address

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/236882/hybrid-exchange-on-prem-user-needs-to-send-mail-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hybrid Exchange (Full Hybrid Configuration, Classic Topology). 2 on-prem Exchange 2016 servers in a DAG. I'm just starting a pilot group of migration accounts.    

One thing I noticed: Microsoft Teams assigns an email address for the team. For example a Team named Test could have test@keyman  .com.    

With my current hybrid setup, I can invite an on-prem user to this Test Team because I can view the user's free/busy calendar information. However when the user responds to the invitation, the email comes back to them as undeliverable because the on-prem Exchange environment doesn't know about test@keyman  .com.    

While I'm sure one option would be for me to change the default SMTP address on the Test Team to be, say, the test@keyman  .onmicrosoft.com alias, I'd first like to know if this behavior is expected, or if the on-prem Exchange environment supposed to forward unknown @keyman  .com recipients across the migration endpoint. Ultimately I'd like to avoid using onmicrosoft.com aliases for these Teams if possible (especially since I'd want to go in and set them back to @keyman  .com after everyone is migrated).

## Answers

_No answers on this thread._
