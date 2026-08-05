---
title: "ADFS 2016 Extranet Smart Lockout SQL Database Location?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/455188/adfs-2016-extranet-smart-lockout-sql-database-loca
question_id: 455188
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 2016 Extranet Smart Lockout SQL Database Location?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/455188/adfs-2016-extranet-smart-lockout-sql-database-loca (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We've got an ADFS v.4 farm with SQL backend and ExtranetLockoutMode = 'ADFSSmartLockoutEnforce'  

The feature seems to be working and we can successfully query for ESL activity via cmdlet Get-ADFSAccountActivity.  

We're interested to get ESL data based on other criteria besides per UPN.  For example, query all users with with X number of 'badpwdCountUnknown'.  Perhaps this data is available in the Azure portal, but we've yet to locate it so thought we might have some luck querying the [ArtifactStore].[AccountActivity] table.  

However, we are surprised to discover that we cannot locate this table, even when connecting to the SQL instance using the service account for which we had originally granted permission to create this table!  We've tried to view via the table via both SSMS and shell - essentially getting back "Invalid object name 'ArtifactStore.AccountActivity.'" from database [AdfsArtifactStore].  

Therefore:  

-  Can this data be had from the portal?  

-  Where else could the present data be returning [via the cmdlet] if not from an AccountActivity table??  

-  Are there any plans to expand the cmdlet's ability to gather info besides on a per UPN basis?  

Thanks for your time!  

DaveC

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-07-01*

The data is stored in the ArtifactStore.AccountActivity database.    

It is not documented, hence not supported to query it directly. It doesn't mean it won't work if you do it. But the data format is subject to change without particular notice.    

    

It is not written synchronously though. There is a timer component that write the stuff back to the DB. So the cmdLet might have more accurate data than the SQL direct lookup.    

I am not aware of any plans of extending the lookup feature to use something else.    

You could look for the failed log on events. It doesn't have the count (unless the account is actually locked out). But you would be able to measure things looking at the number of event per user.
