---
title: "\"Access is denied\" for repadmin on Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1165611/access-is-denied-for-repadmin-on-domain-controller
question_id: 1165611
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# "Access is denied" for repadmin on Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1165611/access-is-denied-for-repadmin-on-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

When we attempt to run repadmin to check domain replication on a Domain Controller (Windows Server 2016), we get a pop up message saying "The application cannot run on your PC.  To find a version for your PC, check with the software publisher".

Then it returns back to command prompt with "Access is denied".

Is there anything wrong ?

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-01-31*

Doesn't sound good for that one but you could run it from another domain controller.
