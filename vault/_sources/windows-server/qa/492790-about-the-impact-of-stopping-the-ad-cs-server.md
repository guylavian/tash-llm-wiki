---
title: "About the impact of stopping the AD CS server."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/492790/about-the-impact-of-stopping-the-ad-cs-server
question_id: 492790
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# About the impact of stopping the AD CS server.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/492790/about-the-impact-of-stopping-the-ad-cs-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to migrate my AD CS server to another environment.  

There is only one AD CS server. (Enterprise CA)  

AD CS functionality is not on the AD server.  

(The AD server and AD CS server are separate environments. )  

The AD CS server will be stopped during the migration, so I would like to confirm the impact of that.  

Is it okay to recognize that client PCs and servers that already have the certificate installed will not be affected if the AD CS server is down?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-29*

Hello @QX0232176  ,    

Thank you so much for posting here.    

During the migration of CA, it is important to remove the CA role service from the source server after completing backup procedures and before installing the CA role service on the destination server. If you choose not to remove the CA role service from the source server before installing the CA role service on the destination server, it is important that you disable the Active Directory Certificate Services service (Certsvc) and shut down the source server before installing the CA role service on the destination server.    

I am not sure but based on my experience, there will be some impact if we do the migration during the working time. It is suggested that the migration should be done during the non-working time to reduce or avoid any impact.     

Reference: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee126140(v=ws.10)#BKMK_GrantPermsAIA    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
