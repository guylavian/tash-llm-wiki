---
title: "Active directory sub domains and group policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1139631/active-directory-sub-domains-and-group-policy
question_id: 1139631
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active directory sub domains and group policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1139631/active-directory-sub-domains-and-group-policy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we've created several sub-domains (political reasons, OUs would work fine but we're not allowed).  When we try to create domain GPOs for this sub-domain, we don't seem to have the option to do it.  My first thought was that the sub-domain might need to become a root domain, but before we go about this, I wanted to ask about why we don't have the option to simply create GPOs in the sub-domain.    

Thanks in advance!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-12-22*

Something here could help.    

https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/linking-gpos-to-active-directory-containers    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful-
