---
title: "ADFS Upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/725625/adfs-upgrade
question_id: 725625
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/725625/adfs-upgrade (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've upgraded and moved the DB from a 2012 SQL server to 2019 (retaining the same virtual pointer name), installed 2019 WAP server, uninstalled, then removed 2012 WAP server, installed 2019 ADFS server, and made the 2019 server the Primary server. When I attempt to upgrade (raise farm behavior) to 2019, I receive the error message shown below. I am a SQL SA on this server. What confuses me is the statement "Database upgrade could not be performed on localhost" (The SQL server is not local). I've generated the script to give to the DBA's to manually create the DB, but I'd really like to be able to do this as it was intended. Any help would be greatly appreciated

Invoke-AdfsFarmBehaviorLevelRaise : Database upgrade could not be performed on localhost. Error: Unable to connect to  

the database. You may not have permission to create the AD FS configuration database in the specified SQL server. You  

can do one of the following: (1) have the SQL administrator grant permissions to you to create the AD FS configuration  

database in the specified SQL server or (2) have the SQL administrator create the AD FS configuration database by  

running SQL scripts. Use the Export-ADFSDeploymentSQLScript to create the SQL scripts. After the SQL administrator  

runs the scripts, try the command again specifying that the database is to be overwritten.  

.  

At line:1 char:1  

-  Invoke-AdfsFarmBehaviorLevelRaise -Credential $cred  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : NotSpecified: (:) [Invoke-AdfsFarmBehaviorLevelRaise], RemoteException  

-  FullyQualifiedErrorId : DeploymentTask,Microsoft.IdentityServer.Deployment.Commands.InvokeUpgradeFarmBehaviorCom  

mand

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-07*

I was able to perform the upgrade by granting the service account SA priv's on the DB, then using the service account to perform the upgrade instead of my Domain Admin account
