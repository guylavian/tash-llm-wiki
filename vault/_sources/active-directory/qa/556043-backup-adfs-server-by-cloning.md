---
title: "Backup ADFS server by Cloning"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/556043/backup-adfs-server-by-cloning
question_id: 556043
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Backup ADFS server by Cloning

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/556043/backup-adfs-server-by-cloning (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All,  

Is it safe to backup ADFS server by Cloning? So if the server crash I will switch on the cloning server.  

Regards,  

Nana Sutisna

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-09-20*

It might work. There are a lot of caveats though as some of the "clone" might not have the latest data for smart account lockout for example. Cloning isn't usually a supported way to do a proper restore though. You can keep it as a last resort if other ways are failing.    

An easy way to backup and restore ADFS is by using ADFS Rapid Restore. See here: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/ad-fs-rapid-restore-tool
