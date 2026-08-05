---
title: "Internet-bound Transport routing in Exchange hybrid !"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2076471/internet-bound-transport-routing-in-exchange-hybri
question_id: 2076471
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Internet-bound Transport routing in Exchange hybrid !

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2076471/internet-bound-transport-routing-in-exchange-hybri (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi folks,

I'm reading this KB

https://learn.microsoft.com/en-us/exchange/transport-routing

it says that:  Messages sent from on-premises recipients are always sent to directly to Internet recipients using DNS regardless of which of the above choices you select in the Hybrid Configuration wizard.

As i understand, there are 2 types of Send Connector Delivery: 

-  Directly via DNS query 

-  via Smart host

So my question is: What "directly to Internet" here?  In Hybrid Exchange Configuration, isn't it possible to configure the Internet-bound email send from on-Prems recipient via 3rd party SaaS solutions (using Smart host Send Connector) as below image?

Many appreciations for your clarifications and supports.

Mikel

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 2 · updated: 2024-09-23*

Hi，

Welcome to Microsoft Q&A community!

Yes, in a Hybrid Exchange Configuration, it is indeed possible to configure Internet-bound emails sent from on-premises recipients to route through a third-party SaaS solution using a Smart host Send Connector. This setup allows you to leverage the benefits of a Smart host, such as enhanced security, compliance, and additional processing, before the emails are sent to their final destination on the Internet.

Explanation of “Directly to Internet”:

When the Hybrid Configuration wizard mentions “directly to Internet,” it typically refers to sending emails using DNS to resolve recipient domains and deliver messages without any intermediary. However, you can override this default behavior by configuring a Smart host Send Connector.
