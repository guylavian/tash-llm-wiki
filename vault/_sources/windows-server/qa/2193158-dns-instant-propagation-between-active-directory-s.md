---
title: "DNS Instant propagation between Active Directory Servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193158/dns-instant-propagation-between-active-directory-s
question_id: 2193158
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-network-connectivity-file-sharing"]
---
# DNS Instant propagation between Active Directory Servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193158/dns-instant-propagation-between-active-directory-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Microsoft Support,

We are experiencing a problem with the propagation between AD servers in the same site not being instantaneous. I have set "Use Notify" to 0 in order to achieve instant propagation of DNS records. However, despite this configuration, DNS records still take approximately 10 minutes to propagate. 

Please provide guidance on this matter.

Thank you,

Vahhab

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-14*

Hello,

It is important to note that even with the "Use Notify" setting set to 0, there may still be a delay in DNS record propagation due to various factors such as network latency, DNS caching, and replication intervals.

To troubleshoot this issue, you can try the following steps:

-  Check the replication interval between the AD servers. You can use the "repadmin /showrepl" command to view the replication status and interval.

-  Check the DNS caching settings on the client machines. If the DNS cache is not cleared frequently, it may cause delays in DNS record propagation. You can use the "ipconfig /flushdns" command to clear the DNS cache.

-  Check the network latency between the AD servers. High network latency can cause delays in DNS record propagation. You can use the "ping" command to test the network latency.

-  Check the DNS server logs for any errors or warnings related to DNS record propagation.

Best Regards,

Hania Lian
