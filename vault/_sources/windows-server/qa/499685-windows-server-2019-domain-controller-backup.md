---
title: "Windows Server 2019 Domain Controller backup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/499685/windows-server-2019-domain-controller-backup
question_id: 499685
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# Windows Server 2019 Domain Controller backup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/499685/windows-server-2019-domain-controller-backup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi guys,   

I setup the AD at AWS Cloud EC2  

primary and secondary AD is running.   

how I can backup and restore the AD? I try AWS snapshot is not the best way to backup using snapshot.   

thanks.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-08-03*

You may use Windows Server Backup feature to do that.    

Take a look at:    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-forest-recovery-backing-up-a-full-server
