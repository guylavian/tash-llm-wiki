---
title: "How do I update GPOs?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/154271/how-do-i-update-gpos
question_id: 154271
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# How do I update GPOs?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/154271/how-do-i-update-gpos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone!  

  How do I update GPOs? I am migrating from w2k8r2 domain controllers to w2k19. Is there an update procedure or is it automatic? How it works? Does it occur when we raise the functional level of the domain?  

Hope I was clear enough.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-11-09*

Hi  

It's automatic in the migration as the SYSVOL volume where GPO are stored, will be synced with the newer server.  

Please keep in mind you might have to do a FRS to DFRS migration as older domain controller used to be in FRS. Windows Server 2019 does not support that replication methodology.  

It's a simple step to migrate, but it's worth to tell. See that site for more detailed step; https://techcommunity.microsoft.com/t5/storage-at-microsoft/streamlined-migration-of-frs-to-dfsr-sysvol/ba-p/425405  

Thanks
