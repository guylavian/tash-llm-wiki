---
title: "Removing Visual C++ 2012 for Exchange 2016/2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1662335/removing-visual-c-2012-for-exchange-2016-2019
question_id: 1662335
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Removing Visual C++ 2012 for Exchange 2016/2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1662335/removing-visual-c-2012-for-exchange-2016-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How can we remove Visual C++ 2012, which is out of support but required for Exchange 2016/2019, and still run Exchange? We are mandated to remove all unsupported software from our systems within 14 days, including C++ 2012. Thank you.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-03*

Hi,

Since Visual C++ 2012 is one of the prerequisites for installing Exchange 2016/2019, also Exchange 2016/2019 includes some components that depend on Visual C++ 2012 at runtime. In other words, Exchange 2019 may require a specific version of Visual C++ 2012 to ensure proper operation of its services. Therefore, Visual C++ 2012 cannot be removed. if it is removed, it may cause Exchange to be broken.
