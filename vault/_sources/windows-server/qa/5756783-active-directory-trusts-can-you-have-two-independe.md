---
title: "Active Directory - Trusts - can you have two independent trust records for each direction instead of one bidirectional record?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5756783/active-directory-trusts-can-you-have-two-independe
question_id: 5756783
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Active Directory - Trusts - can you have two independent trust records for each direction instead of one bidirectional record?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5756783/active-directory-trusts-can-you-have-two-independe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible to have the following setup via on-prem ad trusts:  

prod domain -> non-prod domain = domain-wide (incoming)   

+   

non-prod domain -> prod domain = selective (outgoing)  

as two seperate trust records?  

If they become one record i.e bidirectional then you can only selective either domain-wide or selective as an authentication type. I need one of each.  

I want prod to access all of non-prod but non-prod to only have selective access to prod.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-02-02*

You cannot configure asymmetric authentication types within a single bidirectional trust. If you set up a bidirectional trust, both directions must share either domain-wide or selective authentication. To achieve your requirement, you need two separate one-way trusts: prod → non-prod configured with domain-wide authentication, and non-prod → prod configured with selective authentication. This way, prod users can access all resources in non-prod, while non-prod users only gain access to specific prod resources where you grant “Allowed to Authenticate” permissions. Ensure DNS resolution and SID filtering are correctly configured, otherwise access will fail even with the trust in place.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-02-02*

In Active Directory, trust relationships can be configured to allow different types of access between domains. However, the specific scenario you described—having two independent trust records for each direction (one for domain-wide incoming and another for selective outgoing)—is not supported as you might expect.

When you create a trust relationship between two domains, it typically results in a bidirectional trust if both domains are configured to trust each other. In your case, if you establish a trust from the production domain to the non-production domain as domain-wide (incoming) and from the non-production domain to the production domain as selective (outgoing), these would generally be part of a single trust relationship rather than two separate records.

This means that you cannot have one trust configured as domain-wide and another as selective for the same domains in a way that they operate independently. The trust types must be consistent in their configuration. If you need different authentication types, you would typically have to manage this through a single trust relationship that encompasses both configurations, but it would not allow for distinct independent records as you desire.
