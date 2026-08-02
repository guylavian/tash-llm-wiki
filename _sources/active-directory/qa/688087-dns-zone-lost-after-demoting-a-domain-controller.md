---
title: "DNS zone lost after demoting a domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/688087/dns-zone-lost-after-demoting-a-domain-controller
question_id: 688087
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_affiliations: ["Mvp"]
---
# DNS zone lost after demoting a domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/688087/dns-zone-lost-after-demoting-a-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have demoted a local domain controller and keep the server as member server.  

Local machines are not able to resolve DNS query, we want avoid servers contacting a remote domain controller for DNS queries.  

What's the best solution ?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-08*

I'd check the DHCP server hands out the correct addresses of other remaining local domain controllers. Then clients may need to do ipconfig /release, ipconfig /renew  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
