---
title: "Azure Active Directory Connect sync mail users as contacts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194652/azure-active-directory-connect-sync-mail-users-as
question_id: 2194652
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Azure Active Directory Connect sync mail users as contacts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194652/azure-active-directory-connect-sync-mail-users-as (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a single Exchange Hybrid server connecting to 2 separate Office 365 tenants (Tenant A and Tenant B), with 2 AAD Connect servers connecting to each of the O365 tenants (AADCOnnect A and AADConnect B).

OU A is current,y syncing to Tenant A and OU B is syncing to tenant B.

Domain A is registered in Tenant A and Domain B is registered to Tenant B.

Cross-tenant sync is not available to sync users for the GAL because Tenant A is a commercial tenant and Tenant B is a GCC tenant.

I am trying to figure out a way to sync OU A to Tenant B and OU B to Tenant A that would allow me to populate the GAL for the other respective tenant. Is there a way to sync OU A to Tenant B and have those users show up as contacts instead of users? Is it possible to modify one of the syn rules to convert users in OU A so they sync to Tenant B as contacts?

The goal would be to have the OU A users show up in Tenant B with their email address as ******@domainA.com. the only way I can think of to do that would be to sync them as contacts because Domain A is registered to Tenant A and not Tenant B.

Unless there is a better way to accomplish this???

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-23*

Hello chabango,  

Greetings!  

No problem. Hope you can get some answers to your questions soon.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-23*

Thank you . posted in the azure active directory

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-23*

Hello chabango,  

Thank you for posting in Microsoft Community forum.  

From the description above, I understand your question is related to Azure AD.   

Since there are no engineers dedicated to Azure AD in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and select "Azure Active Directory" tag and any other Azure tag related to your products (because there are more Tags related to Azure when you type Azure key word).  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
