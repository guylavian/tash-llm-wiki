---
title: "Domain Controllers (Production - Non-Production Test environment)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2156006/domain-controllers-production-non-production-test
question_id: 2156006
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Domain Controllers (Production - Non-Production Test environment)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2156006/domain-controllers-production-non-production-test (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Microsoft Community,

I’m seeking some recommendations regarding the configuration of Domain Controllers for our production and non-production test environments.

Currently, both our production and non-production (test) environments are within the same forest. As our environment grows and the need for separation between production and non-production increases, we are evaluating our options for re-structuring this setup. Specifically, we would like to understand the best approach for isolating the non-production environment while still allowing for appropriate access between the two environments if needed.

Here are the options we are considering:

Creating a New Forest for Non-Production – We are considering creating a completely separate forest for non-production and establishing a forest trust between the production and non-production environments. Is this recommended, and are there any best practices for implementing forest trusts in this context?

Creating a New Tree or Child Domain in the Current Forest – Alternatively, we could create a new tree or child domain under the current forest. This would potentially provide easier management but might not offer as much isolation as a separate forest. What are the trade-offs here in terms of security, management, and scalability?

We would greatly appreciate any insights or recommendations from others who have dealt with similar scenarios or have expertise in managing domain environments with both production and non-production systems.

Thank you in advance for your help!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2025-02-25*

Hi @Ahmed Essam  

The test environment should be completely separate from production, in order to avoid impacting production during testing.

What I recommend is to install a new forest on a network completely separate from production and not to configure a trust relationship between the two environments.

Please don't forget to accept helpful answer
