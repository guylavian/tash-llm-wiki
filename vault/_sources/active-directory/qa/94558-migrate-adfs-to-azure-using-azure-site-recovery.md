---
title: "Migrate ADFS to Azure using Azure Site Recovery"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/94558/migrate-adfs-to-azure-using-azure-site-recovery
question_id: 94558
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-site-recovery", "microsoft-security-security-active-directory-federation-services"]
---
# Migrate ADFS to Azure using Azure Site Recovery

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/94558/migrate-adfs-to-azure-using-azure-site-recovery (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am searching for documentation detailing the steps required to migrate ADFS on prem to Azure VMs within an existing AAD tenant.  I am not finding a lot of information in my google searches on this topic.  Can someone here assist?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-15*

Hello @jpcapone   , happy to help!    

I recommend exploring Azure Migrate feature for your migration scenario?     

Azure Site Recovery is best used for these 2 disaster recovery scenarios:    

-   On-prem machines to Azure    

-   Azure VMs across Azure Regions.    

Also noticed you are moving ADFS servers so sharing this useful reference that touches on how to move your claims/adfs aware apps to the cloud. this may be another feasible option over ADFS migration to Azure.  Hope this helps.    

    

Dont hesitate to ping if you have any followup questions.    

Here are some helpful references to get you started.
