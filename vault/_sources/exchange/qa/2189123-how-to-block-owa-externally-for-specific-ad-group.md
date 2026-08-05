---
title: "How to block OWA externally for specific AD Group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189123/how-to-block-owa-externally-for-specific-ad-group
question_id: 2189123
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# How to block OWA externally for specific AD Group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189123/how-to-block-owa-externally-for-specific-ad-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to share my experience configuring a special scenario to restrict OWA externally for specific AD group. (This is not to request help, it is to help others.)

Prerequisites: 

-  Configured Exchange Server to use ADFS authentication

-  Deployed ADFS and WAP

-  Use this Microsoft procedure as a reference: https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019

-  Within the AD, two different security groups have been created to control external access: 

-  One to allow OWA access from the Internet

-  

-  And another to Deny OWA access from the internet

-  

Once the rules have been created within the ADFS and WAP, an Access Control Policy rule is created.

-  

-  Which in turn consists of three different rules:

-  

-  

-  

- 

- 

-  

- 

Then you add the users you want to allow or deny access from the Internet by adding them to the different groups. For internal access, OWA works without adding the users to any AD group. 

It worked perfectly for me, thanks to the support of the Microsoft ADFS technician and a good friend!

Thank you so much, O.A.!

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-05*

Hello Runjie,

Your welcome!

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-24*

Hello 

Thank you for posting on the Microsoft Community. 

Thank you for sharing and for the expertise and literacy shown in this case. 

Regards  

Runjie Zhai
