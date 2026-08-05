---
title: "Active Directory users migrations using ADMT"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/949577/active-directory-users-migrations-using-admt
question_id: 949577
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
---
# Active Directory users migrations using ADMT

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/949577/active-directory-users-migrations-using-admt (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

we have 2 sites in different region and both are different Forest.    

Now i want to migrate all users and computers to Site A from Site B.    

I am using ADMT and i try on lab environment its working fine but i have little concern regarding Trust between Forest. If any other options without creating  trust?    

And we can't use any 3rd party tool as well.    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-03*

I saw your check list but my question is still same.    

I don't want to Create trusts between Domains if any other solution are there?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-02*

Hi there,     

You can use the Active Directory Migration Checklist.    

During an AD DS greenfield installation and migration, system engineers need checklists to keep up with what they should be doing to stand up a new domain.  This checklist is a working checklist, one that has been created here for peer review and peer additions.    

Active Directory Migration Checklist     

https://social.technet.microsoft.com/wiki/contents/articles/43908.active-directory-migration-checklist.aspx    

I hope this information helps. If you have any questions please let me know and I will be glad to help you out.    

-------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--
