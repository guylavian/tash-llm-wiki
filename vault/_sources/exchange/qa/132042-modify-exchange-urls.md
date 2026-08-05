---
title: "Modify Exchange URLs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/132042/modify-exchange-urls
question_id: 132042
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Modify Exchange URLs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/132042/modify-exchange-urls (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We have modified the e-mail domain from @mycompany.com to @myorganization.com. The public URLs not yet changed, just added an SRV record for autodiscover for new domain. This weekend we are planning to change all internal and external URLs. Below are a few concerns  

a) _autodiscover._tcp.myorganization.com. 3600 IN SRV 0 0 443 autodiscover.mycompany.com. is the current Autodiscover SRV record. We saw this record is not working with many devices. So when we create a new CNAME autodiscover, will all the ActiveSync devices  & Outlook anywhere automatically works without any disconnection or do we need to manually re-configure all these devices?  

c) We use F5 load balancer in front of 2 X MB servers. When we modify below folder URLs to new mail.myorganization.com, how it affect end users  

OwaVirtualDirectory  

EcpVirtualDirectory  

OabVirtualDirectoryM  

MapiVirtualDirectory  

ActivesyncVirtualDirectory  

PowerShellVirtualDirectory  

WebservicesVirtualDirectory  

AutoDiscoverService

## Answers

_No answers on this thread._
