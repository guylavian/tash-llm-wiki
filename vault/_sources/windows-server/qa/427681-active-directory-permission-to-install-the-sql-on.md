---
title: "Active Directory permission to install the SQL on Windows cluster."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/427681/active-directory-permission-to-install-the-sql-on
question_id: 427681
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-server-high-availability-clustering-high-availability"]
answer_author_roles: ["Q&A User"]
---
# Active Directory permission to install the SQL on Windows cluster.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/427681/active-directory-permission-to-install-the-sql-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,  What AD permission will require to install the SQL on Windows cluster?   I have created three normal AD account in AD. One for Windows cluster install ; 2nd is service account for sql and 3rd is sql server network name.   Do I need to give any specific permission please suggest.  

Windows Cluster installation.   

 cluinstall ==>   For Windows failover cluster installation. .  

SQL Installation.   

Srv.sql==> Service account for sql.  

sqlvirtualname ===>sql server network name

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-12*

I am using single account for cluster and sql installation. And, one account for sql service

1) User is domain user and have domain admin rights.  

2) user is added in all the local administrative group.

Account which I am using for sql services, added that account also in local administrative group.

only i am facing issue while installing sql

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-09*

Hello,    

 To install a windows server failover cluster, You'd better use a domain administrator account, or make sure that the account has administrator rights on all servers that you want to add as failover cluster nodes.    

https://learn.microsoft.com/en-us/windows-server/failover-clustering/create-failover-cluster#verify-the-prerequisites    

The service account of sql server failover cluster instance can be a domain account or managed service account. It is recommended to always run SQL Server services by using the lowest possible user rights.    

https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-windows-service-accounts-and-permissions?view=sql-server-ver15    

sql server virtual  network name -- A computer object (Active Directory computer account) for the SQL Server network resource name will be created when installing the sql server failover cluster.
