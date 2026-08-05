---
title: "High availability for AD CS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/144716/high-availability-for-ad-cs
question_id: 144716
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# High availability for AD CS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/144716/high-availability-for-ad-cs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a two tier PKI (both VM) what is the best solution for HA. In case the servers goes down?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-10-30*

Hi,  

Just from the High availability for the PKI, using multiple CAs is good way to ensure that your infrastructure can support enterprise scalability.  

Such as one offline Root CA,with 2 issue CA in your environment.  

Also, one important thing, backup CA, to ensure that the server can be restored from the backup when it is down.  

For your reference:  

https://social.technet.microsoft.com/wiki/contents/articles/7421.active-directory-certificate-services-ad-cs-public-key-infrastructure-pki-design-guide.aspx#Plan_for_CA_Capacity_Performance_and_Scalability  

Best Regards,
