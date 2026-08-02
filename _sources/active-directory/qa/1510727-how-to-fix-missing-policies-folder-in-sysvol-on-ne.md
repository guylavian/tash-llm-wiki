---
title: "How to fix missing policies folder in SYSVOL on new domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1510727/how-to-fix-missing-policies-folder-in-sysvol-on-ne
question_id: 1510727
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to fix missing policies folder in SYSVOL on new domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1510727/how-to-fix-missing-policies-folder-in-sysvol-on-ne (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,
We've built a new domain controller on server 2019, our existing domain is on a server 2012 server and we are looking to migrate to the new domain controller but run into problems with replication. Firstly on the new server the SYSVOL and NetLogOn folders were missing I've managed to get those working ok but what's puzzling me in in the SYSVol folder there's no policies folder totally missing. Seems to be replicating ok as when you look at group policies on the new server and make sure the correct server is highlight I can see all the group policies. So not sure where these are being stored. Must have done something wrong initialising this server as even when we select new server as the GC we cannot shut the existing server down. Any ideas will be appreciated.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-24*

Hi @Anonymous  

To fix the issue of missing sysvol and netlogon folders you can start by launch a non-authoritative synchronization of DFSR sysvol replication as mentioned in the link below:

How to perform a non-authoritative synchronization of DFSR-replicated sysvol replication (like D2 for FRS)

If you still have the same issue, in this case you should demote and repromote impacted domain controller to force it to replicate correctly sysvol and netlogon folder.

Please don't forget to accept helpful answer
