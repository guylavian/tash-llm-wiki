---
title: "HSTS on ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/102869/hsts-on-adfs
question_id: 102869
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# HSTS on ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/102869/hsts-on-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We're running ADFS on Windows Server 2019, with the appropriate headers enabled. Much like this prior question, we need to have ADFS return a header, showing HSTS enabled, rather than a 404, if the root is called -- i.e., https://adfs.url.com. HSTS shows as enabled for a valid endpoint, such as https://adfs.url.com/adfs/ls/IdpInitiatedSignon.aspx, but our vulnerability auditors insist on calling the root. Any ideas?

## Answer (community) — community member

*upvotes: 1 · updated: 2020-09-24*

I had the same issue/question for few weeks - Configure HSTS for AD FS    

There is no way to modify the behavior. Work as designed by microsoft.
