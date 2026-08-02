---
title: "Exchange Server 2019 Access Rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1289957/exchange-server-2019-access-rule
question_id: 1289957
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange Server 2019 Access Rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1289957/exchange-server-2019-access-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

I've created the ECP blocking rule...

New-ClientAccessRule -Name "Block EAC" -Action DenyAccess -AnyOfProtocols ExchangeAdminCenter -ExceptAnyOfClientIPAddressesOrRanges 10.0.0.211 -Priority 2

...waited for >24 hours and tested it.

The result: EAC is still accessable from any ip - ???

Is there anything else I must check?

Thank you in advance,  

Michael

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-25*

Oh, sorry - it really did get blocked AFTER authentication - just didn't thought about it... Thank you all for your replies!

Regards,  

Michael
