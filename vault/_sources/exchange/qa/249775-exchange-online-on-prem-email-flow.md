---
title: "Exchange Online + On Prem email flow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/249775/exchange-online-on-prem-email-flow
question_id: 249775
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
---
# Exchange Online + On Prem email flow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/249775/exchange-online-on-prem-email-flow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a hybrid Online/On Prem configuration and I migrated our first account from on prem to online.  Everything appears ok other than it can not receive emails from external domains.  It can send/receive internal emails and it can send to external.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-29*

@Daniel Kaliel      

550-Relaying from    

Does there exist any email filter tool, smart host or email proxy tool in your organization? In a hybrid environment, there can only exist Edge server between Exchange on-premise and Exchange online.    

So, if there exist such tool, please remove it from your organization, then remove exiting connectors(Send connectors on Exchange on-premises and Connectors on Exchange online) and rerun HCW to create new connector to routing emails in your organization.    

About the mail flow security, you could use EOP(Contained in Exchange online) to filter emails for your organization.    

By the way, make sure all need ports are opened in your organization: Exchange Online    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
