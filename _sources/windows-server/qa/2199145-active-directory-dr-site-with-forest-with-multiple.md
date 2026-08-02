---
title: "Active Directory DR site with forest with multiple subdomains"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199145/active-directory-dr-site-with-forest-with-multiple
question_id: 2199145
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Active Directory DR site with forest with multiple subdomains

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199145/active-directory-dr-site-with-forest-with-multiple (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My company is planning a DR site for our datacenter based on on VMware Site Recovery Manager.  

Our Active Directory infrastructure is a forest with 1 parent domain and 3 subdomains.  

The there are 3 subdomains, one for the Production servers, one for pre-production and one for testing.  

As an example  

SERVICE.local -> hosts all infrastrucutre servers  

PROD.service.local -> hosts production servers  

PREPROD.service.local -> hosts all pre-production servers  

TEST.service.local -> hosts all testing servers  

Our idea is to create a new AD site, and place 2 new DCs on this site, one for the SERVICE.local domain, and one for the PROD.service.local domain. We don't need to protect the pre-production and testing servers.  

Then, all the servers that we want to protect are then replicated to the DR site with VMware SRM.   

In case of Disaster, they will be switched to the DR site and continue working properly authenticating to the DCs in DR.  

For networking reasons that are beyond my control, the preproductione and testing networks (and so the corresponding DCs) are not able to communicate with the DCs in DR.  

Basically, this is waht we are planning.  

Waht I'm asking:  

-  is this a suitable and robust DR solution?  

-  do you see any potential problem for the preprod and testing DCs not communicating with the DCs in DR?  

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-22*

Hello, I reopen this thread of my own, since I am worried about potential issues in a failback situation.

In a DR scenario, only the SERVICE and PROD will be online at the DR site, while the PREPROD and TEST domains will be unavailable.

If the DR situation last for long time, what will happen to the PREPROD  and TEST domains when the main site is brought back online?

Are there any potential issues in such a situation?

Regards
