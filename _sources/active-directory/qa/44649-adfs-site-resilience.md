---
title: "ADFS Site Resilience"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/44649/adfs-site-resilience
question_id: 44649
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS Site Resilience

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/44649/adfs-site-resilience (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

For a customer, we configured an ADFS farm, with 2 nodes, exposed the Interned with WAP.  

On each site, we have one ADFS Server and one WAP.  

We used DNS RoundRobin for federation services publication. We plan to use Load balancing.  

Each WAP server can contact each ADFS server.  

When the primary ADFS server is inaccessible, internal authentication works fine, but external authentication failed (through WAP).  

How can I build High Availibility?  

Thanks,  

Jean-Luc

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-22*

Look first in to the windows event log on the secondary AD FS server. Do you see entries from type error / warning at the timestamp you try the authentication?  

Does the authentication work over the secondary inside your trusted network (LAN) without WAP? So we can differentiate whether ADFS or WAP is the problem.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-22*

Hey,

How can I build High Availibility?

I think the problem is DNS Round Robin. Because it randomly reply on every request one ip address. But the dns protocol can not check, if the server or application behind the ip address ist online.

The only safe way for this is to implement a physikal or virtual load balancer in your enviroment. We setuped your szenario for few weeks with a high aviable Load Balancer. AD FS over WAP works in every failure scenario (eg. primary ad fs server ist down).

Regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-07-22*

hi,  

up!  

Any suggestion? Any reference documentation?  

Thanks,  

Jean-Luc
