---
title: "Replication between Primary Domain Controller and New Domain Controller Failing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1007195/replication-between-primary-domain-controller-and
question_id: 1007195
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# Replication between Primary Domain Controller and New Domain Controller Failing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1007195/replication-between-primary-domain-controller-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My Secondary domain controller stopped replicating to the PDC, i removed the SDC manually and performed a cleanup.    

I added a new SDC and it works for a day or two and stops replicating after a while.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-15*

Hello there,    

Do you get any Replication error code?    

The two most common causes of this problem include a loss of network connectivity or a DNS configuration error. Replication errors can also occur as a result of authentication errors or a situation when the domain controller lacks the hardware resources to keep pace with the current demand.    

The Repadmin tool and other diagnostic tools also provide information that can help you resolve replication failures.    

By default, Active Directory replication remote procedure calls (RPCs) occur dynamically over an available port through the RPC Endpoint Mapper (RPCSS) on port 135. Make sure that Windows Firewall with Advanced Security and other firewalls are configured properly to allow for replication.     

Here is a link that has some additional troubleshooting steps which you can try and see if helps in overcoming your issue Troubleshooting Active Directory Replication Problems https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/troubleshoot/troubleshooting-active-directory-replication-problems    

Troubleshoot common Active Directory replication errors https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/common-active-directory-replication-errors    

---------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-14*

Hi,    

Can you post output of the command dcdiag /e /v /q please?    

Check if time sync is in place    

Check if any network drops or network connectivity is in place always    

Check if any backups or snapshots are running when it breaks the replication    

Check all the AD services - is it DFSR or FRS?    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
