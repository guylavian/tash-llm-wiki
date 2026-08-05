---
title: "Domain controller recovery"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/882559/domain-controller-recovery
question_id: 882559
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Domain controller recovery

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/882559/domain-controller-recovery (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Yesterday I needed to restore a Windows Server 2019 Essentials domain controller without FSMO roles (single-level domain with 2 DCs). After recovery, I didn't find Log DFS Replication (Source: DFSR, Event ID: 4604) and I couldn't get to Active Directory using LDP (Error <0x51> - "Unable to open connection"). So I went through the logs again and found out the wrong thing. The restored controller took away one FSMO "Domain Naming Master" role shortly before the restore itself.    

I decided on the (second) main controller seized this role. My question is: Can I release the restored DC to the network and have it replicate? From the logs, I'm almost sure that the last backup (Windows Server Backup) of the restored controller had no FSMO roles.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-09*

In the end, it helped to get the controller into the network and replicate everything.
