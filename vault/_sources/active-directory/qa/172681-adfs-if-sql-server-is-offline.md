---
title: "ADFS if SQL Server is Offline"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/172681/adfs-if-sql-server-is-offline
question_id: 172681
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "sql-server-other-l1"]
---
# ADFS if SQL Server is Offline

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/172681/adfs-if-sql-server-is-offline (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey everyone,  

I am building an ADFS and ADFS Proxy server off-site (but in the same farm) to accommodate SSO during a major network outage coming up, and will be configuring it for our current on-site SQL farm. We have plans to switch our DNS to point users to the new off-site servers during the outage.  

That being said, connectivity to our SQL farm will cease during this time.  

What are the ramifications of not having access to ADFSConfigurationV3 and ADFSArtifactStore during a window of about a day? Will ADFS be completely inoperable?  

I am not concerned about ADFS lockout, or any of those features; I just need ADFS SSO to work at a minimal level.  

TL;DR:  

What happens if ADFS has to stop talking to its SQL server for some time?

## Answers

_No answers on this thread._
