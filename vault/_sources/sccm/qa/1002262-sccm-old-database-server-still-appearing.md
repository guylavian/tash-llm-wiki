---
title: "SCCM Old database server still appearing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1002262/sccm-old-database-server-still-appearing
question_id: 1002262
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
---
# SCCM Old database server still appearing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1002262/sccm-old-database-server-still-appearing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello dears,    

I have an SCCM ENV. It has two 'site systems', the primary site system (SCCM01) and the database server (OLDSQL).    

For maintenance reasons, I migrated the database onto a new server (NEWSQL). I went through the correct steps for moving this site, by following this link:    

https://www.anoopcnair.com/sccm-sql-server-database-migration-part-2/.    

The new database works as expected, however, the (OLDSQL) server still appears in the console in monitoring >> site component with critical status. How could I remove it from the console?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-11*

Hi Heba,    

Just go through this detailed article on removing and cleaning up SCCM after a migration - uninstall-sites-and-hierarchies    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
