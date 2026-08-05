---
title: "Only 1 out of 2 GPO deployed printers shows up"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/948572/only-1-out-of-2-gpo-deployed-printers-shows-up
question_id: 948572
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-print-jobs", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Only 1 out of 2 GPO deployed printers shows up

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/948572/only-1-out-of-2-gpo-deployed-printers-shows-up (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've deployed 2 printers via GPO. On a test laptop I can see both printers are being shared by the print server but only one printer has been automatically added.    

Both printers are using package-aware drivers, AFAIK, so there shouldn't be deployment issues. The time since the printers were deployed is now over a day so it's unlikely a DC/GPO replication issue. The print server is using Windows Server 2022 and the test laptop is using Windows 10.    

Any idea why only 1 out of 2 printers is being deployed correctly? Is there any way to "debug" this? I.e. some kind of log or something to check if there's a potential issue?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-15*

Check windows event viewer on your windows 10 laptop, it records any group policy failure and should be a good starting point. Report back your findings.
