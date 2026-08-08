---
title: "Active Directory Location Based Services"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198954/active-directory-location-based-services
question_id: 2198954
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# Active Directory Location Based Services

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198954/active-directory-location-based-services (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We're deploying AD servers in Azure datacenters all over the world and I need to be sure user endpoints utilize AD and DNS servers within their region. We have subnets assigned to sites in AD so that laptops in those regions are identified to the DC and DNS region. I am wondering if there are any other requirements to ensure endpoints use the correct regions servers.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-14*

Hello Mark Drucker1,  

Thank you for posting in Microsoft Community forum.  

Sites are divided by subnet segments. You can put DCs (DNS servers) you select to the corresponding sites.  

If all the domain devices of user endpoints belong to correct subnet segments, then the devices and users should find the correct DC and DNS region.

Creating a Site Design | Microsoft Learn

Designing the Site Topology | Microsoft Learn  

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
