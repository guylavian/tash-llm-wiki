---
title: "Latency between domain controllers in the same AD Site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/302244/latency-between-domain-controllers-in-the-same-ad
question_id: 302244
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Latency between domain controllers in the same AD Site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/302244/latency-between-domain-controllers-in-the-same-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm planning to extend our AD to another datacenter and public clouds.  

What is the maximum allowed latency in milliseconds from an AD perspective (replication, queries, etc.) between Domain Controllers that belong to the same AD site so that I can keep them using the same AD site, and I will avoid at least the 15 minutes replication interval between ad sites

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-08*

Hi,    

Replication within a site occurs automatically on the basis of change notification. Intra-site replication begins when you make a directory update on a domain controller. By default, the source domain controller waits 15 seconds and then sends an update notification to its closest replication partner. If the source domain controller has more than one replication partner, subsequent notifications go out by default at 3 second intervals to each partner. After receiving notification of a change, a partner domain controller sends a directory update request to the source domain controller. The source domain controller responds to the request with a replication operation. The 3 second notification interval prevents the source domain controller from being overwhelmed with simultaneous update requests from its replication partners.    

If you want to Modify the Default Intra-Site Domain Controller Replication Interval, you can refer to the following link:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/modify-default-intra-site-dc-replication-interval    

Didn't find any information to clarify the max limit for the value.    

Best Regards,
