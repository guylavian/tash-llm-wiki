---
title: "Reusing Windows Server 2012 R2 ADFS server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/523361/reusing-windows-server-2012-r2-adfs-server
question_id: 523361
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Reusing Windows Server 2012 R2 ADFS server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/523361/reusing-windows-server-2012-r2-adfs-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have a SSO project with SAP and we wanted to use ADFS.  

I would like to inquire the best way on how to proceed:  

-  Use an existing ADFS server from a previous project. This server is used previously to provide SSO to a web application (Dealer Management System). This server is workng but project did not push through  

-  Install a new ADFS server  

If we proceed with option 1, can we just reconfigure ADFS or do we need to reinstall?  

If we proceed with option 2, is it possible to add a new ADFS server?  

Appreciate your feedback.  

Thanks and regards,

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-08-30*

ADFS (and any other IDP) are most of the time considered tier-0 or "control plane" security zone or level (cf: https://learn.microsoft.com/en-us/security/compass/privileged-access-access-model). So in theory you could re-use. But the reality is that you probably didn't consider the first deployment as a tier-0/control plane type of asset. Therefore, re-using might lead to service exposure as you don't necessarily know who has access or had access to the service, its dedicated account, etc. If that's the case, I would consider creating a new farm taking in consideration all security recommendation from the start: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/best-practices-securing-ad-fs.    

There is no limit on how many ADFS farm you can have in a forest. As long as they use different names and URL, you are good to go. The only thing that the farms of a forest share between them is the device registration configuration. But that's rarely use anyway.
