---
title: "Migrate from ADFS 2.0 to Azure Cloud Authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1061141/migrate-from-adfs-2-0-to-azure-cloud-authenticatio
question_id: 1061141
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Migrate from ADFS 2.0 to Azure Cloud Authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1061141/migrate-from-adfs-2-0-to-azure-cloud-authenticatio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi There,    

I'm looking for some guidance on we can migrate from the existing ADFS solution running on 2.0 on Server 2008 to cloud authentication. Please share any steps, blogs, posts or anything that will help. I have gone through the Microsoft document but it is not very clear. I will need help backing up existing config in case if we have to revert back, commands to decomm adfs and move all application authentication to cloud. I have used Azure stage roll out and its working as expected.    

Thanks    

Rish

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-11-12*

Are you trying to take and lift and shift the server to IaaS? or do you mean moving to Azure AD auth? I would start with https://learn.microsoft.com/en-us/azure/active-directory/hybrid/migrate-from-federation-to-cloud-authentication.     

What did you search for and found that was not clear?
