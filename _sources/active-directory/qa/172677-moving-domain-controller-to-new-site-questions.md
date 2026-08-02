---
title: "Moving Domain Controller to New Site - Questions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/172677/moving-domain-controller-to-new-site-questions
question_id: 172677
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Moving Domain Controller to New Site - Questions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/172677/moving-domain-controller-to-new-site-questions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all. We have a domain AD site that has multiple domain controllers. We have recently started standing up DCs that are protected by Cisco ACI. We are now half ACI and half legacy that are not. We would like to start to force authentication in this AD site to just these ACI domain controllers. I thought standing up a new AD site and move these DCs here would force the authentication to the ACI DCs and give us time to decommission the legacy DCs since we don't know what the dependencies to these old DCs are.   

Would it work if I create a new AD site and move these DCs there and just not assign any subnets to this site? This way clients would not authenticate to these DCs by default. These DCs are in multiple different vlans. As we build this out we plan to fix and standardize AD. Can I move them without re-iping them as well?

## Answers

_No answers on this thread._
