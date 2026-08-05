---
title: "FSMO role transfer from Windows Server 2008R2 DC to Windows Server 2016."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161440/fsmo-role-transfer-from-windows-server-2008r2-dc-t
question_id: 1161440
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# FSMO role transfer from Windows Server 2008R2 DC to Windows Server 2016.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161440/fsmo-role-transfer-from-windows-server-2008r2-dc-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are in the process of upgrading our domain controller environment from Windows Server 2008R2 to Windows Server 2016. Our domain DFL/FFL level is 2008. We now plan to transfer FSMO role from WindowsServer2008R2DC node to WindowsServer2016. Needed checklist on what are the things we need to check and validate before transferring the FSMO role.

Also can we re-transfer the role back to Windows Server 2008R2 in case we identify any issue?

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2023-01-17*

Transferring roles to / from is not a problem.  

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2016, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.  

Also at some point either before or after (if not already done) I'd recommend migrating sysvol replication from older FRS technology to DFSR

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-01-17*

Hi,

Of course you can move fsmo roles temporarily to another domain controller without any impact.

Before moving fsmo roles check the domain controller and replication health. 

For the PDC role , you should move it to a domain controller able to communicate with all other DCs in same domain to ensure time synchronization and password reset.

please don’t forget to accept correct answer to close your thread
