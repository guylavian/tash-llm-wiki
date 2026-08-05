---
title: "I was looking for cloud Kerberos trust model there in pre requisite KB3534307 PATCH should be installed on the windows server 2106 is there so Just wanted to know that KB4534307 and KB3534307 are same or different?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1415326/i-was-looking-for-cloud-kerberos-trust-model-there
question_id: 1415326
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# I was looking for cloud Kerberos trust model there in pre requisite KB3534307 PATCH should be installed on the windows server 2106 is there so Just wanted to know that KB4534307 and KB3534307 are same or different?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1415326/i-was-looking-for-cloud-kerberos-trust-model-there (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I searched for KB3534307 it is showing me KB4534307 .

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-11-04*

What's the result of? 

```
(Get-HotFix | Sort-Object -Property InstalledOn)
```

KB4534307 == January 23, 2020-(OS Build 14393.3474) Updates are now cumulative which means the current monthly rollup contain new fixes plus all previous monthly rollups. So KB4534307 has been superseded by the newer updates and is no longer needed or required.   

--please don't forget to close up the thread here by marking answer if the reply is helpful--
