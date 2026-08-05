---
title: "Exchange hybrid reconfiguration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/231657/exchange-hybrid-reconfiguration
question_id: 231657
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange hybrid reconfiguration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/231657/exchange-hybrid-reconfiguration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

in your deployment we're using 4 exchange 2013 servers 1 edge 3 mailbox and symantec messaging gateway as a smart host, we also have office 365 and have hybrid configured, we want to decommission our edge server and use smg as a smart host between our exchange and office 365. is this a supported configuration or should we further adjust something else?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

@Archil Berikishvili      

As the information AndyDavid provided, except for Edge servers, other filtering tools are not supported between Exchange on-premises and Exchange Online.    

If you want to improve the security of your organization mail flow, you can use EOP as the incoming point, EOP will filter email for your organization. For more detailed information about mail flow in hybrid, you can have a look about this article.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-15*

Not Supported:    

https://learn.microsoft.com/en-us/exchange/transport-routing
