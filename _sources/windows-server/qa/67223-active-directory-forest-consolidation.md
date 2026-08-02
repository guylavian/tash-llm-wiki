---
title: "Active Directory Forest Consolidation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/67223/active-directory-forest-consolidation
question_id: 67223
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Forest Consolidation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/67223/active-directory-forest-consolidation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Folks,  

A customer has multiple AD Forest for different business units, due to recent business restructuring they want to consolidate all IT services under single IT. For that, customer wants to have single new 2016 based AD forest with Exchange 2016 (all On-Premises environment).  

Currently customer has  2008 R2 based AD Infrastructure as following.  

IslandA.com with two child domains like City1.IslandA.com and City2.IslandB.com. Root Domain (IslandA.com holds Exchange 2010 and System center infrastructure too).  

IslandB.com with three child domains like City1.IslandB.com, City2.IslandB.com and City3.IslandB.com. Root Domain (IslandB.com holds Exchange 2010, System center infrastructure and some other applications like Oracel, Dynamics etc).  

Now, Customer wants to have new forest like Alpha.com based on Windows 2016 and all AD, Exchange infrastructure to be migrated under it.  

Customer has around 10,000 user based infrastructure spanning in 5 countries. I would like to request you please help me to design best approach for this  project. Some tips, third party tools and some design guidance would be appreciated. Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-22*

Thanks Daisy for answering Active Directory part. I will check on other forums for Exchange and Applications part. Thanks.
