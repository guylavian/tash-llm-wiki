---
title: "Install RSAT: Active Directory Domain Services and Lightweight Directory Services Tools"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2277836/install-rsat-active-directory-domain-services-and
question_id: 2277836
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Install RSAT: Active Directory Domain Services and Lightweight Directory Services Tools

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2277836/install-rsat-active-directory-domain-services-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to install "RSAT: Active Directory Domain Services and Lightweight Directory Services Tools." I followed instructions found on the web to go to Settings > Apps > Optional Features, then start typing "RSAT: Active ..." This is exactly what I did a year ago on a different computer and had no problem. Now, typing "RSAT: Active ..." all I get is "RSAT: Active Directory Certificate Services Tools." No domain services, no "RSAT: Group Policy Management Tools", which I'm also going to need.

They're run as dsa.msc and gpmc.msc, respectively.

How do I get these apps?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-25*

Just to try, I ran gpmc.msc and it worked. Likewise with dsa.msc. Perhaps they didn't show on Settings > Apps > Optional Features because they were already installed. I don't recall doing so, but maybe that cognitive decline is kicking in. I will save your answer though. Good for future reference.
