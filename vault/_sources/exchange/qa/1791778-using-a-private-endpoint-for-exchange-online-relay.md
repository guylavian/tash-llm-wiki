---
title: "Using a private endpoint for Exchange Online Relay - GCC high"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1791778/using-a-private-endpoint-for-exchange-online-relay
question_id: 1791778
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-virtual-machines", "azure-virtual-network", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Using a private endpoint for Exchange Online Relay - GCC high

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1791778/using-a-private-endpoint-for-exchange-online-relay (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an online only configuration in Azure GCC high. We have virtual compute. 

We would like to setup an SMTP relay to be used for notifications as a trusted connection to exchange online. 

I understand the documentation here: https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-to-route-mail  

My question:  

Can I use a private connection as a connector in exchange online ? The goal is to not route the traffic publicly. 

Note: It does not appear that Email SMTP support through Azure Communication Services is supported in GCC High tenant (https://learn.microsoft.com/en-us/azure/communication-services/concepts/email/email-smtp-overview)

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-03*

Hi，@Rider, Justin

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, here are my suggestions:

In Exchange Online, follow the documentation to set up a connector, but when configuring the connector, you need to use the private IP address or internal DNS name of your internal relay server instead of the public address.

 

Regarding Azure question, it is separate from Exchange Online. In order to better solve your problem, I will add Azure tag to your problem.

Best
