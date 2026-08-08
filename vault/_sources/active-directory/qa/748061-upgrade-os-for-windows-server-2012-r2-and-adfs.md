---
title: "Upgrade OS for Windows Server 2012 R2 and ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/748061/upgrade-os-for-windows-server-2012-r2-and-adfs
question_id: 748061
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Upgrade OS for Windows Server 2012 R2 and ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/748061/upgrade-os-for-windows-server-2012-r2-and-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently running a single Windows Server 2012 R2 with ADFS.  

I would like to upgrade the OS to version 2019, which I assume (?) would upgrade ADFS to version 4.  

Is it as "simple" as performing an in-place upgrade?  

I read several articles on upgrading an ADFS farm, which requires additional servers - which I would rather not do.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-28*

In-place upgrade is actually never simple. I am not even sure if that's a working thing for AD FS (never heard of someone even trying it).   

Adding a Windows Server 2019 to an existing farm is actaully a good way to test things without breaking stuff. You can add the server to the farm following the procedure you seem to allude to, then you can configure the HOSTS file of your machine to make the AD FS FQDN point to the new server and test stuff. Without affecting anything else than your machine and the couple of other machines on which you'd like to do the test on. Once this is done, then you can get rid of the 2012 R2 server and update your DNS to make the FQDN of the farm point to the new server.  

Not only that's the way to go, that's the easiest way to go (since it requires nothing to be configured or changed on the existing farm) and the rollback is as easy too.
