---
title: "Exchange 2016 CU 20 failed to installation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/370329/exchange-2016-cu-20-failed-to-installation
question_id: 370329
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 CU 20 failed to installation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/370329/exchange-2016-cu-20-failed-to-installation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am to installed Exchange 2016 CU 20 and followed all MS recommendations however an installation is usually failed during this step (Step#3_ Management Console) and the winrm is impacted as I can not open exchange management shell for this server and the exchange search host control service is failed to start also and I noted the CU 20 is listed on programe file but when I rename an exchange setup log file and re-install it again its failed and I can not failover the database for this server unless skip the indexing , therefore any suggestions to remove this updates to complete the installation in a proper way....  

Thanks a lot.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-25*

Hi @Bebo Edward   ,    

Please provide the below information,    

-  Have you installed all the pre-requisites    

-  Is this a new installation?    

-  Have you prepared the Active directory with setup /prepareschema, setup /prepareAD switches - Any issues with this    

-  Please share the complete error message by covering your personal information    

Pre-requisites - https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2016    

Preparing Active directory - https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2016
