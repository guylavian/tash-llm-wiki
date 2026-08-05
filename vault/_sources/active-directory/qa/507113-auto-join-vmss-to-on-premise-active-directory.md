---
title: "Auto join VMSS to on-premise active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/507113/auto-join-vmss-to-on-premise-active-directory
question_id: 507113
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-virtual-machines", "azure-vm-scalesets", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Auto join VMSS to on-premise active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/507113/auto-join-vmss-to-on-premise-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have S2S VPN to Azure and DC on Azure  

Manual adding VM's to on-premise domain is OK  

But I need to add VMSS VM's to on-premise AD automatically  

I already try JsonADDomainExtension extension but it's not working.  

I think it's only for Azure AD, not local AD  

Any other options?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-08-16*

Problem solved  

It's working now with JsonADDomainExtension  

There was a problem with the image  

Creating new image solve the problem

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-08-10*

Hi Asaf, thanks for the post.  

do you mean add to on-prem AD as domain join during build process of VM or after creating the VM.
