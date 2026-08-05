---
title: "Do I disable OWA if our mailbox is in Office 365 as part of the recommendation for the recent Exchange exploit?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/346753/do-i-disable-owa-if-our-mailbox-is-in-office-365-a
question_id: 346753
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Do I disable OWA if our mailbox is in Office 365 as part of the recommendation for the recent Exchange exploit?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/346753/do-i-disable-owa-if-our-mailbox-is-in-office-365-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

In response to the recent Exchange exploit, one of the recommendations is to, "Remove public access to Outlook Web Access (OWA) and Exchange Control Panel (ECP)." The vulnerability I am talking about is this https://techcommunity.microsoft.com/t5/exchange-team-blog/released-march-2021-exchange-server-security-updates/ba-p/2175901  

If we have an Exchange hybrid server on-prem, but the majority of our mailboxes are in the cloud (O365), do we still need to disable OWA for our users whose mailboxes are in the cloud?  

How do I disable OWA for the mailbox on-prem? We are using Exchanger server 2019 Standard.  

Thank you,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-07*

Thank you.  The server is fully patched.  I will look into blocking OWA in our firewall.
