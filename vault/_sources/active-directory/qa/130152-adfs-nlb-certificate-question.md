---
title: "adfs nlb certificate question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/130152/adfs-nlb-certificate-question
question_id: 130152
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# adfs nlb certificate question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/130152/adfs-nlb-certificate-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I would just like to ask this question in setting up nlb for adfs regarding the certificate.  

How should the certificate be created? Like should adfs01 and adfs02 each have certificate issued to them by the root CA but with an additional entry in the SAN for the FQDN of the NLB cluster name?  

example:  

certificate SAN of adfs01  

DNS=adfs01.comp.com  

DNS=adfsnlb.comp.com  

certificate SAN of adfs02  

DNS=adfs02.comp.com  

DNS=adfsnlb.comp.com

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-18*

ADFS is agnostic of the load balancer situation/configuration.    

You need a certificate for the FQDN of your ADFS farm. You do not need the FQDN of the nodes. You can also use a wildcard certificate such as *.comp.com. Note that if you are considering using certificate authentication, you should also include certauth.comp.com in the SAN.
