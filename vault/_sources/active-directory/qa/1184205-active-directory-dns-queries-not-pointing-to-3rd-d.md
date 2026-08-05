---
title: "Active Directory DNS queries not pointing to 3rd DNS Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1184205/active-directory-dns-queries-not-pointing-to-3rd-d
question_id: 1184205
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory DNS queries not pointing to 3rd DNS Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1184205/active-directory-dns-queries-not-pointing-to-3rd-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an active directory domain services role plus DNS installed in a Windows Server 2016 STD in a VM of Hypver-V with the domain name of xyz.net, The Hypver-V is hosted in physical machine of DELL PowerEdge R750 and I have 2 other additional domain controllers also which secondary additional domain controller is in same network subnet with primary domain controller location head office, but the 3rd Additional domain controller is in our DR site which is in a different network different location, but they are all sync with each other and has no issue.

The problem is whenever we down the primary and secondary domain controller for testing which are in same network the DNS traffic/queries are not going automatically to 3rd additional domain controller which we have in our DR site its pointing to head office primary domain controller.

I did ipconfig/flushdns and ipconfig/registerdns and did a restart of the client PC also waited for 5 minutes, but still whenever I was tracert our domain xyz.net it was pointing to primary DNS.

How to point automatically my clients DNS queries to 3rd additional domain controller when my primary and secondary domain controllers are down.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-02-26*

Then if you did an 

```
ipconfig /all
```

on the problem member you should see it listed for DNS. Also check the required ports are open between sites.  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts#windows-server-2008-and-later-versions  

- 

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-02-25*

You can add the third (or more) domain controller / DNS server addresses to your DHCP server to hand out.  Then do an

```
ipconfig /renew
```

on the clients.

-

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-25*

Hi @John

You can add 3 DNS IP in IP settings client machine:

When the first DNS IP is not available the client PC will try to contact the second IP and if the second IP is not available the client PC will contact the 3rd IP.

Please don't forget to mark helpful answer as accepted
