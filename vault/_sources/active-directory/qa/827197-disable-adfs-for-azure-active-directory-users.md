---
title: "Disable ADFS for Azure Active directory users."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/827197/disable-adfs-for-azure-active-directory-users
question_id: 827197
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Disable ADFS for Azure Active directory users.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/827197/disable-adfs-for-azure-active-directory-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,    

Please let me know how to disable the ADFS for Azure Active Directory users.    

Azure ad account (UPN) : john.dave@Company portal   .com     

Your quick help will be much appreciated.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-04-28*

You could use the Staged Rollout feature: https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-staged-rollout    

You create a group, associate it with the feature (it is explained in the documentation I linked). And this user will use Azure AD for authentication without impacting the other users (which will still use AD FS). You need to make sure that this authentication can take place by also implementing the requirement for PHS or PTA. From the documentation:    

You have decided to move to either of two options:    

Option A - password hash synchronization (sync). For more information, see What is password hash sync    

Option B - pass-through authentication. For more information, see What is pass-through authentication
