---
title: "'550 5.7.1 TRANSPORT.RULES.RejectMessage; the message was rejected by organization policy' in Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1651579/550-5-7-1-transport-rules-rejectmessage-the-messag
question_id: 1651579
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# '550 5.7.1 TRANSPORT.RULES.RejectMessage; the message was rejected by organization policy' in Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1651579/550-5-7-1-transport-rules-rejectmessage-the-messag (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,

It have 2 exchange system in my company. One is on-prem ex2019, and the other is ex2019 hybrid with exchange online.

When user receive a meeting request from external and forward this meeting to other external address:

-  On the exchange hybrid, the meeting request can forward and the sender is "user on behalf external sender".

-  But in on-prem ex2019, the email will reject with NDR "Your message wasn't delivered because the email admin for the organization 'xxx.xxx.com' created an email rule restriction. Please contact the email admin for that organization and ask them to remove or update the rule restriction."   '550 5.7.1 TRANSPORT.RULES.RejectMessage; the message was rejected by organization policy'

We don't have any rules in both exchange. Any configuration in ex2019 or EXO can control the external meeting can forward to external? Or this is the different between on-prem2019 and exchange online?

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-09*

Hi Chong,

The error message you describe as "550 5.7.1 Transport Rule RejectMessage; Message was rejected by organization policy" strongly indicates that there is some form of mail flow rule preventing the message from being transmitted. Since we received the NDR from the recipient, we could know that the message was delivered to recipients’ email system.  You can ask the forwarded recipient to execute ‘Get-MessageTrackingLog’ in the Exchange Management Shell to check why the message to be rejected.

In addition, I notice that this issue is with external message, You can create a new internal meeting request , and then forward it to the same recipient. This can help us isolate whether this issue is related to external message.
