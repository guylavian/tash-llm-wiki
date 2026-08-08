---
title: "ADFS, two forests with no trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/967529/adfs-two-forests-with-no-trust
question_id: 967529
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS, two forests with no trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/967529/adfs-two-forests-with-no-trust (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am testing and ADFS config to accommodate a new company we are adding. They must remain separate, and we are not able to spin up a new Azure/ O365 tenant. I added multi-domain support to ADFS, added the second domain to adconnect and established DNS resolution between domains.    

The users in the new forest are synced to AzureAD, however when I try to log a user into the Azure Tenant via https://adfs.domain.com/adfs/ls/idpinitiatedsignon.aspx I get invalid username or password. The more detailed errors in the ADFS server event log are attached.    

I am not sure what else is required. This video tutorial shows my scenario and is what I have done, although it doesn't actually show a successful auth.    

What else is required for this scenario?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-08-29*

If you want to authenticate with AD FS and use the Active Directory Claim Provider Trust you need an trust. It's described here: https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-single-adfs-multitenant-federation    

Now, you don't have to federate the other users though. You don't have to use AD FS at all when it comes to Office 365 and Azure AD integration. Maybe we can help you moving away from it?
