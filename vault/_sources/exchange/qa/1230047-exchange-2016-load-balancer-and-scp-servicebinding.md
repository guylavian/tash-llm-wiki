---
title: "Exchange 2016 Load balancer and SCP ServiceBindinginformation attribute in AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1230047/exchange-2016-load-balancer-and-scp-servicebinding
question_id: 1230047
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Load balancer and SCP ServiceBindinginformation attribute in AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1230047/exchange-2016-load-balancer-and-scp-servicebinding (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
We are installing a second on premises Exchange server, and will be using a DAG. A Kemp load balancer will be used for this configuration.  

Autodiscover will be mail.mydomain.com and will resolve to some IP address.  

Servers are ex1.mydomain.com and ex2.mydomain.com.  

I understand I need to change virtual directories like EWS, EAS, MAPI etc to point to mail.mydomain.com  

My question is regarding the existing SCP objects in AD with the serviceBindingInformation attribute.  

Should I change them using the Set-ClientAccessService cmdlet for both servers?  

How are they made to be proper/correct?  

Right now, ex1.mydomain.com already has one of its own when it was created, and once I install ex2.mydomain.com that will also create its own.  

So what will happen with MS Outlook clients?  

Will they be able to properly find the mail.mydomain.com load balancer?  

Thanks!****

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-04-13*

The autodiscover SCP  should be the same on all servers in the load balanced pool with a certificate with the subject name that matches that FQDN.
