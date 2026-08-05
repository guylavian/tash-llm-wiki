---
title: "GPO WALL PAPER NO APPLYING"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/646263/gpo-wall-paper-no-applying
question_id: 646263
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# GPO WALL PAPER NO APPLYING

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/646263/gpo-wall-paper-no-applying (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI, I inherit a network Administrator position from a previous admin.  

 now i want to apply GPO wall paper but doesn't apply to the client. wall paper always shows black.  

i'm using sever 2012 and the clients are win10...  

any help will be appreciated

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-11-30*

Check event viewer for Group Policy errors.  

Also consider this method if you wish not to enforce the wallpaper to users and let them later change it - https://ccmexec.com/2015/08/replacing-default-wallpaper-in-windows-10-using-scriptmdtsccm/
