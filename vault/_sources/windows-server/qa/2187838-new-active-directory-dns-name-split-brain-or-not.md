---
title: "New Active Directory DNS name - split-brain or not?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187838/new-active-directory-dns-name-split-brain-or-not
question_id: 2187838
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# New Active Directory DNS name - split-brain or not?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187838/new-active-directory-dns-name-split-brain-or-not (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I deploy a new specific Active Directory forest.

Based on latest recommandation, should I use split-brain DNS or not ?

Internal AD DNS name like mydomain.local and public DNS name mydomain.com.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-14*

Hello BernardPh,  

Thank you for your reply.

The latest recommendation for your query is to use the same DNS name in both zones for internal and external access to the website. This will simplify the configuration and management of the website and reduce the chances of errors or misconfigurations. However, you should ensure that the website is properly secured with SSL/TLS certificates and appropriate access controls to prevent unauthorized access.

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-13*

Hello,

Q: What is the latest recommendation you mentioned?

A: if a web site should be accessible for interal user and from internal, is it better to use the same DNS name in both zone, or is it better to use two differents DNS names (https://help.mysite.net for internals and https://help.mysite.com from internet ) ? 

Q: Why do you need to split the AD-integrated DNS?

A: I won't use AD integrated DNS for split-brain with Internet. I won't publish my AD server to Internet. If need, split-brain will be achive with two differents DNS system.

Thanks for your answer.

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-13*

Hello BernardPh,  

Thank you for your reply.  

My concern is about ressource (as web site) that may be accessible from inside the domain and from Internet. Does the two DNS zones (internal in AD and published on Internet) should be the same or it better to have different DNS zone name ?  

A: I think it is the same. Split-brain does not need to split "Internal AD DNS name like mydomain.local and public DNS name mydomain.com".  

You can know more information about split-brain from link below.  

Use DNS Policy for Split-Brain DNS Deployment | Microsoft Learn

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-10*

Thanks for your answer.

My concern is about ressource (as web site) that may be accessible from inside the domain and from Internet. Does the two DNS zones (internal in AD and published on Internet) should be the same or it better to have different DNS zone name ?

Kind Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-10*

Hello BernardPh,  

Thank you for posting in Microsoft Community forum.

If you install DNS role on one Domain Controller, it is an AD-integrated DNS.  

Active Directory-Integrated DNS Zones | Microsoft Learn  

What is the latest recommendation you mentioned?   

Why do you need to split the AD-integrated DNS?  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
