---
title: "Exchange Online Outbound Connector - If I want to use two smart hosts, how are they used?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2237000/exchange-online-outbound-connector-if-i-want-to-us
question_id: 2237000
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online Outbound Connector - If I want to use two smart hosts, how are they used?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2237000/exchange-online-outbound-connector-if-i-want-to-us (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all, 

we do have Exchange Online in a hybrid scenario with the standard Outbound Connector created by the hybrid connection wizard. 

In the outbound connector is one smart host to deliver mails to the local Exchange server.

If I add a second smart host to the configuration, how is this smart host used?  

In round robin mode or as a failover?

Thanks for your help in advance! 

Best Regards,  

Marc

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-21*

Hello, @Marc Müllenbach

Welcome to the Microsoft Q&A platform!

In an Exchange Online hybrid scenario, if you configure multiple smart hosts in the outbound connector, they are used in a round robin fashion by default. This means that Exchange Online will distribute outbound emails evenly across all the configured smart hosts.

If you want to implement failover (where one smart host is used primarily and the others are used only if the primary one fails), you will need to set up more sophisticated load balancing and failover mechanisms outside of the standard Exchange Online configuration options. You might achieve this using a load balancer or by configuring DNS with multiple MX records with different priorities, but Exchange Online itself will use round robin for multiple smart hosts specified directly in the outbound connector.

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
