---
title: "Move/Upgrade 2012 R2 ADFS SQL database"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1188996/move-upgrade-2012-r2-adfs-sql-database
question_id: 1188996
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Move/Upgrade 2012 R2 ADFS SQL database

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1188996/move-upgrade-2012-r2-adfs-sql-database (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a single ADFS 2012 R2 server and single ADFS proxy server. The ADFS server is using a single SQL 2012 server. We would like to upgrade the SQL server to a later version.

-  What is the latest version of SQL that I can move to? The MS doc points to SQL 2014 - is this doc out of date? https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn554247(v=ws.11)?redirectedfrom=MSDN

-  Can I move to an Azure managed instance or Azure SQL database?

-  Once the databases are moved to a supported version of SQL, how do I update ADFS? 

-  Do I need to update the service broker? [http://the-techanic.blogspot.com/2015/02/migrating-your-adfs-2012-r2-sql.html]

-  How can I verify ADFS is working post move?

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-03-15*

What is the requirement to still keep using ADFS? We have a free workshop to help you migrate from ADSF to AAD. https://techcommunity.microsoft.com/t5/community-events-list/microsoft-workshops-how-to-successfully-migrate-away-from-ad-fs/m-p/3668480

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-13*

Hi Gary

Welcome to Q&A Forum; this is a great place to get support, answers, and tips.

Thank you for posting your query; I'll be more than glad to help you out.

I only can answer one part of your question:

From my understanding, ADFS only uses the database as a "data sink" without any usage of any special features. So I guess the sentence "For AD FS in Windows Server 2012 R2, you can use SQL Server 2008 and higher" should be correct.

So it should be possible to use a SQL Server 2022 as a data sink for ADFS.

I hope my answer is helpful to you,

Your

Bjoern Peters

If the reply was helpful, please upvote and/or accept it as an answer, as this helps others in the community with similar questions. Thanks!
