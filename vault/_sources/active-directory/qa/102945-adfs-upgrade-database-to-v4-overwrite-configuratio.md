---
title: "ADFS upgrade database to v4 overwrite configuration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/102945/adfs-upgrade-database-to-v4-overwrite-configuratio
question_id: 102945
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "sql-server-other-l1"]
---
# ADFS upgrade database to v4 overwrite configuration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/102945/adfs-upgrade-database-to-v4-overwrite-configuratio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I am attempting an upgrade of the ADFS database, after replacing the servers with new Windows 2016 servers.  

I have used the script to create the database (new database), as the account I am using does not have permission to create databases (trying to replicate what is in production).  

When running the Invoke-AdfsFarmBehaviorLevelRaise I get the following error.  

Invoke-AdfsFarmBehaviorLevelRaise : An AD FS configuration database with the same name already exists; specify that the existing database is to be   

overwritten.  

I can see nothing in the powershell command 'invoke-xxx' to force an overwrite of the database.  

I read that you can specify -OverwriteConfiguration, but this just gives me an error this command doesnt exist.  

Any help would be appreciated.  

Thanks  

Matt

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-23*

Hi @Matthew Riddler  ,    

Please check the following articles if help:    

Upgrade AD FS 3.0 to Windows Server 2016/2019    

https://www.starwindsoftware.com/blog/upgrade-ad-fs-3-0-to-windows-server-20162019    

Update AD FS 2012 R2 to AD FS 2016    

https://xanderbikbergen.com/2019/02/19/update-ad-fs-2012-r2-to-ad-fs-2016/    

Or waiting for ADFS experts give some useful suggestion.    

Best regards,    

Cris    

If the answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
