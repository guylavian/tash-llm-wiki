---
title: "I have a Domain Controller with a Tombstone Lifetime that has exceeded. How do I bring it back online?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2079307/i-have-a-domain-controller-with-a-tombstone-lifeti
question_id: 2079307
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# I have a Domain Controller with a Tombstone Lifetime that has exceeded. How do I bring it back online?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2079307/i-have-a-domain-controller-with-a-tombstone-lifeti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Domain Controller with a Tombstone Lifetime that has exceeded. How do I bring it back online?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2024-09-26*

Hello,

The safest way to deal with a DC that has exceeded its tombstone lifetime is to demote it and promote a new DC.

If you demote a DC, perform metadata cleanup to ensure that all references to the old DC are removed from Active Directory.

Clean up AD DS server metadata | Microsoft Learn

Then once the cleanup has replicated you can join the DC back to the domain and promote it again.

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-09-25*

Restore it to an isolated network - and don't connect it to you production network

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
