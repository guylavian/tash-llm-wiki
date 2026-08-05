---
title: "DNS Servers (Domain Controllers) behind load balancer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1643235/dns-servers-domain-controllers-behind-load-balance
question_id: 1643235
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# DNS Servers (Domain Controllers) behind load balancer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1643235/dns-servers-domain-controllers-behind-load-balance (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we have 3 R/W domain controllers in US location (DNS servers) - one of them is set as preferred DNS server on literally all other servers causing overload of that DNS server reported by SCOM:  

Alert: Windows DNS 2016 and 1709+ - Server Query Overload

This raised the question of potentially placing these 3 DNS servers behind load balancer (ok, alternate solution would be to set this server as preferred DNS server on 1/3 of servers, and other 2 on the remaining 2/3 of servers respectively) - I am not aware of any solution for this provided by Microsoft so want to double check what options are on the table.

Finally, I have heard many times having DNS Servers behind LB is not the best idea.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-08*

Hello,

 

Thank you for posting in Q&A forum.

To resolve this high workload issue, you can try to configure other 2 DNS servers as primary DNS server. If you are worried about that these 2 servers are not able to resolve part of domain names, can add another one as DNS forwarder for these two.

For Microsoft Official Load Balancing resolution, please kindly refer to below link:

https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/app-lb

Hope this answer can help you well.

 

Best regards，

Jill Zhou
