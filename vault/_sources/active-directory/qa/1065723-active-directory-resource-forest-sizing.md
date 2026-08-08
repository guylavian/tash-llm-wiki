---
title: "Active Directory Resource Forest sizing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1065723/active-directory-resource-forest-sizing
question_id: 1065723
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory Resource Forest sizing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1065723/active-directory-resource-forest-sizing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When sizing an Active Directory resource forest to host only member servers where users will reside in a separate Active Directory user forest, do the same sizing considerations of AD (for user objects) apply?    

AD User Forest - users.corp.com - contains 10,000 users.    

AD Resource Forest - resource.adatum.com contains 300 servers.    

Forest Trust will be implemented.    

Resource Forest will contain a small number of users (30) so the AD user database is small, however it will perform authentication and authorisation requests (via forest trust) for the 10,000 users to access servers. So, does the Resource Forest get sized for 30 users, or 10,000 users?

## Answers

_No answers on this thread._
