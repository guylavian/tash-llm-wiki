---
title: "Exchange on-prem stamping wrong build number onto message sent via Pickup folder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2110876/exchange-on-prem-stamping-wrong-build-number-onto
question_id: 2110876
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange on-prem stamping wrong build number onto message sent via Pickup folder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2110876/exchange-on-prem-stamping-wrong-build-number-onto (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange online is throttling then failing emails sent via Exchange 2016 pickup folder under the error {LED=550 5.7.230 Connecting Exchange server version is out-of-date; connection to Exchange Online blocked for 60 mins/hr.

Exchange 2016 server on-prem is fully up to date, doesn't appear on "Out-of-date connecting on-premises Exchange servers" & emails sent via traditional relay are being delivered to Exchange online without issue.

Anyone know how to resolve the issue where Exchange on-prem server is stamping wrong build number onto message sent via Pickup folder?

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2024-10-25*

We are aware of this problem, and it will be addressed in an upcoming update. EDIT: now released: https://techcommunity.microsoft.com/blog/exchange/released-november-2024-exchange-server-security-updates/4293125
