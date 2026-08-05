---
title: "2 Domain Controllers on the Same Network"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/313468/2-domain-controllers-on-the-same-network
question_id: 313468
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# 2 Domain Controllers on the Same Network

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/313468/2-domain-controllers-on-the-same-network (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How can two Domain Controllers both be Primary DNS Servers for the same Domain would there be any issues with this?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-15*

Hi,  

Did you mean some of the clients point to one DC1 as the Primary DNS Server while some clients point to another DC as the Primary DNS Server?  

Actually, In a larger environment, at least two domain controllers at each physical site should be DNS servers.  

This provides redundancy in the event that one DC goes offline unexpectedly. Note that domain-joined machines must be configured to use multiple DNS servers in order to take advantage of this.  

Based on my understanding , it would be ok to do this.  

Best Practices for DNS Configuration in an Active Directory Domain  

This response contains a third-party link. We provide this link for easy reference. Microsoft cannot guarantee the validity of any information and content in this link.  

Best Regards,
