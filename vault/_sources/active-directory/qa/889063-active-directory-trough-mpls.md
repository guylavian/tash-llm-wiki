---
title: "Active directory trough MPLS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/889063/active-directory-trough-mpls
question_id: 889063
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active directory trough MPLS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/889063/active-directory-trough-mpls (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

I need to install 2 domain controllers on a central location, and the clients would have access to the dc trough a mpls network, do I need to be aware on some limitations? Does client to domain controller with mpls have any problems in terms of policy, logon etc?    

thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-14*

I'd just check that these ports are allowed to flow between networks.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts#windows-server-2008-and-later-versions    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
