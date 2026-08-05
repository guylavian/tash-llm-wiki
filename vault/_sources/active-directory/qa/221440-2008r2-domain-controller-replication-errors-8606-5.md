---
title: "2008R2 Domain Controller: Replication Errors: (8606), (5), (1256), (8446)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/221440/2008r2-domain-controller-replication-errors-8606-5
question_id: 221440
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["Mvp"]
---
# 2008R2 Domain Controller: Replication Errors: (8606), (5), (1256), (8446)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/221440/2008r2-domain-controller-replication-errors-8606-5 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I am facing these below errors when i ran the Repadmin /replsummary command on a 2008R2 Enterprize domain controller. Could someone please help me resolve these issues ?   

Destination DSA     largest delta    fails/total %%   error  

 ALBION           >60 days            2 /  24    8  (8606) Insufficient attributes were given to create an object. This object may not exist because it may have  

been deleted and already garbage collected.  

 CALEDONIA                 12m:36s    0 /  24    0  

 CAMBRIA                   16m:40s    0 /  17    0  

 GERMANIA                  22m:45s    0 /  12    0  

 GONDOR           >60 days           19 /  39   48  (5) Access is denied.  

 HIBERNIA                  22m:33s    0 /  17    0  

 MORDOR           >60 days           15 /  29   51  (1256) The remote system is not available. For information about network troubleshooting, see Windows Help.  

 SCYTHIA          >60 days            7 /  19   36  (8446) The replication operation failed to allocate memory.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-07*

These ones may help.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/replication-error-8446    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/replication-error-8606    

The ones that are greater than 60 days may have tombstoned. In that case the solution is to demote, reboot, promo it again.    

--please don't forget to Accept as answer if the reply is helpful--
