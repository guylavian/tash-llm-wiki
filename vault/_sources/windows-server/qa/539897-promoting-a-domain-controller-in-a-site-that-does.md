---
title: "Promoting a domain controller in a site that does not see the master RID"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/539897/promoting-a-domain-controller-in-a-site-that-does
question_id: 539897
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Promoting a domain controller in a site that does not see the master RID

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/539897/promoting-a-domain-controller-in-a-site-that-does (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The company I am working for has multiple sites in China, US and NL.  Because there are problems establishing site-to-site connections with CN, we only have one MPLS connection between CN and US ant a site-to-site VPN between US and NL. The master domain controller was installed in CN and I created another one in US without problems. Now I am trying to set one in NL. The NL site is not seeing the CN site, so it is not seeing the RID master. When I try to promote the server in NL as a DC it is failing for this reason.  

Is there anything I can do to bypass this issue?  

All the the servers are 2019.  

Thanks,  

Mugurel

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-04*

I was afraid that is the case, just trying to see if there is any workaround. With the current setup, the RID Master is not going to be visible in NL :-(  

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-04*

Might check the logs for details  

-  %systemroot%\debug\dcpromo.log  

-  Event viewer\Windows logs\System  

-  Event viewer\Windows logs\Application  

-  Event viewer\Applications and services logs\Directory Service  

-  Event viewer\Applications and services logs\File Replication Service  

-  Event viewer\Applications and services logs\DFS Replication  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
