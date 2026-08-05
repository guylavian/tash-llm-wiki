---
title: "Best Practice for ADFS High Availability"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2261818/best-practice-for-adfs-high-availability
question_id: 2261818
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Best Practice for ADFS High Availability

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2261818/best-practice-for-adfs-high-availability (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

I'm seeking guidance on the best practices for extending our ADFS environment to a DR (Disaster Recovery) site.

Here’s our current setup at HQ:

-  Two ADFS servers.

A Barracuda load balancer for high availability.

Microsoft Entra Connect is configured to use ADFS for authentication.

ADFS servers are using the default Windows Internal Database (WID).

We now plan to extend ADFS to our DR site to ensure service continuity in case of a failure at HQ.

My questions are:

Can we continue using WID for the DR extension, or do we need to move to a full SQL Server backend (e.g., SQL Always On) to support ADFS across multiple sites?

If WID is sufficient, what are the best practices to properly configure ADFS servers across primary and DR sites?

Are there any considerations for latency, replication, or failover between the HQ and DR ADFS servers when using WID?

Should the DR ADFS servers be added as additional federation servers in the existing farm, or is there a different recommended approach?

I appreciate any advice, experiences, or official documentation links that could guide us.

Thanks,

## Answers

_No answers on this thread._
