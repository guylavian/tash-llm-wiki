---
title: "active directory sites and services"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/513056/active-directory-sites-and-services
question_id: 513056
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# active directory sites and services

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/513056/active-directory-sites-and-services (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have primary domain controller in my head office and so i am planning another additional domain controller in remote branch for DR.

so, what is the best practice to create the active directory sites.

1) should I create a new site or it should be better in default site.

please explain.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-13*

When you add another DC in a domain (same site or another site), the replication is configured during the DCPromo step.  

After that, replication is enabled and will occur depending on your configuration.  

hth

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-13*

It depends...  

Does your bandwidth between the 2 sites is really fast ?  

Keep in mind that putting the 2 sites location within the same AD Site means that a user could be authenticated by "any" domain controller in this site.  If the link between the 2 sites is not very good, you may experience some issues during logon / GPO application / DFS Access  

If it's for DR, i would create another site just to be sure that the DR site is completely independant.  

hth
