---
title: "A disconnected domain controller on a ship"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/953097/a-disconnected-domain-controller-on-a-ship
question_id: 953097
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# A disconnected domain controller on a ship

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/953097/a-disconnected-domain-controller-on-a-ship (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible to place a domain controller on a ship that will connect to the domain occasionally, but always within sixty days?    

If it is possible, what challenges will be experienced with the domain controller, and thus active directory?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-12*

Thanks Gary, you have confirmed what I suspected.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-03*

Hello    

Thank you for your question and reaching out. I can understand you are  having query  related  to Domain controller.    

You can place a domain controller offline , but it should be get Replicated or Synced with another Domain controller within 60 days to Tombstone lifetime and replication of deletions    

Reference :    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/information-lingering-objects    

---    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-08-03*

As long as it isn't disconnected from greater than tombstone lifetime. Also it is possible that this can result in a deleted objects being reintroduced into the directory.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
