---
title: "what does the active directory attribute dSCorePropogationData measure?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2069486/what-does-the-active-directory-attribute-dscorepro
question_id: 2069486
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# what does the active directory attribute dSCorePropogationData measure?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2069486/what-does-the-active-directory-attribute-dscorepro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

what does the active directory attribute dSCorePropogationData measure?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2024-09-16*

Hello,

Thank you for posting in Q&A forum.

The `dSCorePropagationData` attribute in Active Directory is used internally by the Directory Service to track replication state information for objects within the directory. This attribute holds a sequence of timestamps that represent when certain actions were performed, such as when changes to the object were last propagated to other domain controllers. It's mainly utilized for internal processes and replication health monitoring rather than for direct use by administrators in day-to-day operations.

It's not typically an attribute that administrators need to interact with directly; rather, it serves as part of the internal housekeeping mechanisms of Active Directory.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
