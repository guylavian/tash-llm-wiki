---
title: "2019 Domain Controller NIC configuration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/920061/2019-domain-controller-nic-configuration
question_id: 920061
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# 2019 Domain Controller NIC configuration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/920061/2019-domain-controller-nic-configuration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Its been a while since I've done new DCs. Is there any changes I need to put in place for a DC NIC?    

Like registerdns in DNS client settings or remove certain NIC protocols that aren't needed?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-07-15*

You should be fine to leave it checked on connection properties as long as there isn't a rouge (router?) that happens to have an enabled IPv6 DHCP server on the network.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-15*

What about disabling ipv6 on the nics on all the new 2019 DCs? we don't use ipv6    

we typically disabled ipv6 on our existing 2012r2 DCs.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-07-08*

I'd leave the protocols stock, then generally speaking add the domain controllers own static ip address plus the loopback (127.0.0.1) listed for DNS    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
