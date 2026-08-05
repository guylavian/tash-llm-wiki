---
title: "Changing ADFS 3.0 service account (Server 2012 R2)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/20778/changing-adfs-3-0-service-account-server-2012-r2
question_id: 20778
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Changing ADFS 3.0 service account (Server 2012 R2)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/20778/changing-adfs-3-0-service-account-server-2012-r2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

There are many post on how to change the service account by using the following script:  

ADFS3.xChangeSvcAcct.ps1  

https://gallery.technet.microsoft.com/scriptcenter/Active-Directory-ddb67df0#content  

However, what I do not think is clear is how to proceed when you have an ADFS Web Proxy.  

The script talks about primary and secondaries. If I understand correctly, you first update on the secondary servers,  

and then you move to the primary.  

But does the ADFS Proxy is considered a secondary? If not, once I run the script on the primary server, how do I update  

the service account on the Proxy?  

Has anybody gone through this scenario?  

Thanks

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-03-31*

The Web Application Proxy (aka WAP, that's how we call the ADFS Proxy since Windows Server 2012 R2) does not leverage the ADFS service account at all.  

As a matter of fact, WAP don't even need to be domain joined. WAPs authenticate with the ADFS farm using TLS authentication (certificates are generated when you join the WAP to the farm and then roll-over on a regular basis).  

In other words, there is no action required on the WAPs when you change the service account of the ADFS farm.
