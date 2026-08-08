---
title: "Migrate ADFS and ADFS Proxy from On Prem to Windows Server 2019 Azure IAAS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/733160/migrate-adfs-and-adfs-proxy-from-on-prem-to-window
question_id: 733160
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Migrate ADFS and ADFS Proxy from On Prem to Windows Server 2019 Azure IAAS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/733160/migrate-adfs-and-adfs-proxy-from-on-prem-to-window (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Please help me with the steps to Migrate ADFS and ADFS Proxy from On Prem to Windows Server 2019 Azure IAAS?  

Thanks  

Ram Ch

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-14*

This is documented here:    

Deploying Active Directory Federation Services in Azure https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/how-to-connect-fed-azure-adfs    

You will essentially add a new node in Azure IaaS and if your objective is to remove AD FS entirely from on-premises datacenters, the only difference with the published documentation aforementionned is that you would then move the primary roles to the machine in Azure and then procede to remove the on-prem nodes.    

Note that if you are using AD FS for Azure AD integration, the recommendation is to move away from AD FS and use cloud-based authentication. If that's you're case, we can also discuss this here.
