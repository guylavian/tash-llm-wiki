---
title: "Migration to ADFS 2012 to 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/497833/migration-to-adfs-2012-to-2016
question_id: 497833
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Migration to ADFS 2012 to 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/497833/migration-to-adfs-2012-to-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Expert,  

I have to upgrade our ADFS from 2012R2 to 2016, may I know what is the steps to do this upgrade and what should I have to do avoid any issue?  

One more thing my AD is running on 2012R2, Shall i upgrade the AD first then the ADFS or what?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-08-02*

@Ibrahim hasan   Thanks for reaching out.     

For migrating to server 2016, you must ensure that the domain has been prepared or 2016 schema. so yes, upgrading AD would be the first thing.     

Before you can move to AD FS in Windows Server 2016 FBL, you must remove all of the Windows 2012 R2 nodes. You cannot just upgrade a Windows Server 2012 R2 OS to Windows Server 2016 and have it become a 2016 node. You will need to remove it and replace it with a new 2016 node.    

Here is our documented practice for upgrading to 2016 from 2012 :    

For SQL  database : https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/upgrading-to-ad-fs-in-windows-server-sql     

For WID  : https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/upgrading-to-ad-fs-in-windows-server     

-----------------------------------------------------------------------------------------------------    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
