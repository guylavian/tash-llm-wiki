---
title: "ADFS Native Database Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/200650/adfs-native-database-migration
question_id: 200650
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Native Database Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/200650/adfs-native-database-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I would like to migrate our existing on prem ADFS SQL database's (AdfsArtifactStore and AdfsConfiguration) to Azure SQL Managed Instance (paas) so no cloud vm is required. Is this possible?  

If not, can I migrate them to to an Azure vm with SQL server on it? Can you confirm what SQL Server version is supported for this setup?  

Many thanks  

Jerome

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-17*

Azure SQL is not supported as a backend for ADFS.    

SQL doesn't offer a lot comparing to the local WID...    

-  A SQL backend is required for Token Replay Detection. But that is only for Claim Provider trusts else than Active Directory. So if you only have only Active Directory listed in the Claim Provider Trust section of the administrtive console, that's useless.     

-  A SQL backend is required to use the SAML Artifact Resolution profile of SAML2. This is very rare to use this SAML feature and most (if not almost all) applications in the markets are not using it.    

-  A SQL backend is required if you have more than 100 trusts.     

If you are not in these 3 cases, you should maybe condiser moving to WID. You can use the Rapid Restore PowerShell module to backup your environment and restore it into a WID environment.    

And/or you can also look at using Azure AD as an IDP then you don't have to manage any servers. But that's if you have an Azure AD directory.
