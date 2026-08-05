---
title: "Active Directory Certificate Services (AD CS) Failover Cluster Question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1134525/active-directory-certificate-services-ad-cs-failov
question_id: 1134525
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-high-availability-clustering-high-availability"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Certificate Services (AD CS) Failover Cluster Question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1134525/active-directory-certificate-services-ad-cs-failov (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We completed configuration of Windows 2022 Enterprise Subordinate CA in a 2-node Windows cluster.  Now we're looking at configuring a stretch cluster in our DR site.  We'd also like to prepare for future server OS upgrades by having a procedure to add a new cluster node.  The fact of installing the AD CS role on a new node means overwriting the database is the source of concern.  During the initial install, this isn't an issue, but the database is full of configuration changes and a few certificates for testing.    

Is the solution as simple as backing up the database prior to the install and then restoring afterwards?      

What about the shared registry location for the cluster service?  Should that be backed up and restored on the new node after the database restore?  Any chance that the new install will overwrite that registry key?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-21*

That link doesn't answer my question about adding new cluster nodes to an existing clustered Certificate Authority service.  The new node requires the role to be installed and that installation causes the database to be overwritten.  I suspect I'm looking for a graceful way of doing it, but the only answer is to backup and restore.  I don't like the idea of overwriting the database to add a new node.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-20*

Hi,    

Thank you for posting your query.    

Kindly follow the steps provided below to resolve your issue.    

Just from the High availability for the PKI, using multiple CAs is good way to ensure that your infrastructure can support enterprise scalability.    

Such as one offline Root CA,with 2 issue CA in your environment.    

Also, one important thing, backup CA, to ensure that the server can be restored from the backup when it is down.    

For your reference:    

https://social.technet.microsoft.com/wiki/contents/articles/7421.active-directory-certificate-services-ad-cs-public-key-infrastructure-pki-design-guide.aspx#Plan_for_CA_Capacity_Performance_and_Scalability     

Go to this link for your reference and other troubleshooting procedures https://learn.microsoft.com/answers/questions/144716/high-availability-for-ad-cs.html    

Do not hesitate to message us if you need further assistance.    

If the answer is helpful kindly click "Accept as Answer" and up vote it.
