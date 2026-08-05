---
title: "move adfs database back to adfs server from sql server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/605183/move-adfs-database-back-to-adfs-server-from-sql-se
question_id: 605183
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# move adfs database back to adfs server from sql server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/605183/move-adfs-database-back-to-adfs-server-from-sql-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Environment: two adfs web application proxy behind load balancer. Two backend ADFS 3.0 server. Each WAP points to a single ADFS server. ADFS server has the configuration and artifact databases on an alwayson group in a different SQL server.     

What I would like:     

Ideally, have the current two ADFS servers as primary and secondary with WID, meaning, move the database back to how it would be under wid condition.     

I looked at the rapid restore article below and it feels like one would have to run that, then install a brand new environment and then restore from what was exported out of the tool.     

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/ad-fs-rapid-restore-tool    

Would appreciate if anyone could provide a good guideline on how to go about doing that.     

Thanks!

## Answers

_No answers on this thread._
