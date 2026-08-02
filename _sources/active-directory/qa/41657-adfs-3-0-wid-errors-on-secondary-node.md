---
title: "ADFS 3.0 WID Errors on Secondary node"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/41657/adfs-3-0-wid-errors-on-secondary-node
question_id: 41657
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS 3.0 WID Errors on Secondary node

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/41657/adfs-3-0-wid-errors-on-secondary-node (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm seeing hundreds of error on a secondary ADFS 3.0 node in the farm that indicate:     

An exception occurred while enqueueing a message in the target queue. Error: 15517, State: 1. Cannot execute as the database principal because the principal "dbo" does not exist, this type of principal cannot be impersonated, or you do not have permission.    

When I check the User Mapping on the domain service account used I see it is dbo on the AdfsArtifactStore and AdsfConfiguration databases.     

    

On the Schema properties permission for the AdfsArtifactStore DB I see db_genevaservice DB Role but there's nothing on the Schema properties permission for the AdfsConfiguration DB.     

There's very little information in reference to the Database Role db_genevaservice and asking a SQL DBA they say it must be a custom DB Role. I do find it referenced in articles for migrating from WID to SQL and they indicate that the service account needs to have this DB role on both databases.     

https://social.technet.microsoft.com/wiki/contents/articles/23563.windows-server-2012-r2-ad-fs-migrate-your-ad-fs-configuration-database-from-wid-to-sql-server.aspx    

Another article indicates that dropping the service account and adding it back as owner...    

https://social.technet.microsoft.com/Forums/windowsserver/en-US/e4cfb1e2-34b9-4cbb-815b-058138f5aa54/adfs-sync-server-loaded-with-event-id-28005-mssqlmicrosoftwid?forum=ADFS    

My service account is dbo so is the issue related to the Database Role db_genevaservice?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-23*

The service account is a normal domain user, not a managed service account. There were permission issues in WID on the secondary node. After working with Premier Support for a number of days we were able to gain access to the database. This didn't resolve the issues with the WID syncing to the secondary server. In the end I removed the ADFS and WID role from the server and reinstalled ADFS.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-24*

The error message points to owner problems. Please check who is the owner of both databases.  

Execute follow sql command:  

```
select name AS 'Database'
       , suser_sname(owner_sid) AS 'Creator'
 from sys.databases;

 GO
```

Independently what dou mean with domain service account. Do you use for the ad fs service a simple domain user account or a group managed service account (gMSA)?
