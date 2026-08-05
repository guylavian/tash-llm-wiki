---
title: "Migrate ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/914866/migrate-adfs
question_id: 914866
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Migrate ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/914866/migrate-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a 2012 r2 ADFS farm with databases hosted on a backend SQL server. Many internal and third party applications are customized to use the environment so we will need to keep this around for some time.     

However, I want to get rid of hosting the sql databases in the backend. So, thinking of migrating to a fresh set of 2022 servers with primary and secondary. My questions are:    

-  Can I export the config of the current ADFS servers (with databases on backend sql server) and have it imported on the new primary/secondary farm?     

-  In primary and secondary architecture, does the requests get served by primary only or do both the primary and secondary serve the requests?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-07-12*

There is a way to do that.    

You can create a backup of your AD FS 2012 R2 farm using this: AD FS Rapid Restore (scenario 3: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/ad-fs-rapid-restore-tool#scenarios)    

Then restore it a chose WID.    

Then you can do a regular upgrade (which consist of adding 2022 servers to your existing 2012 R2 farm).
