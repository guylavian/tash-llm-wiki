---
title: "Switching my Active Directory to B2C Tenant in Azure Portal prompts for Approving Sign-In Request."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5100446/switching-my-active-directory-to-b2c-tenant-in-azu
question_id: 5100446
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Switching my Active Directory to B2C Tenant in Azure Portal prompts for Approving Sign-In Request.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5100446/switching-my-active-directory-to-b2c-tenant-in-azu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I setup Azure B2C tenant in Azure Portal. At that time it must have prompted me to setup the account with Microsoft Authenticator which setup a different account in Authenticator with some "ext" text referring to external account to Azure B2C. 

I do not have any MFA setup for my work account in my based Azure AD Tenant.   

I accidentally deleted that account from my mobile phone. Now, I am locked out of my account. 

I asked another guy in Azure B2C who had admin access to revoke MFA, and force registration of MFA, but it is not affecting my account. I even asked my based Azure AD admin to reset the MFA and revoke MFA in base tenant. But, switching directory still prompts
 for "Approve Sign in Request" screen mentioning that "We have sent the request to your mobile device. Please open Authenticator App to respond." 

Is there any way to disable this MFA prompt. 

I have observed that if i use my work account to login to other identity provider, it is asking for MFA even if it is not setup for your account.

Did anyone faced similar issue? How to overcome this issue?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2020-12-08*

Hi Rizwan,

I'm Independent Advisor not Microsoft employee or support person. I have deep enough Windows knowledge and you may trust me. It's a pleasure for me to help others and I'll do all my best to help you.

You are talking about corporate environment. It is more effective to ask such questions at Q&A forum    https://docs.microsoft.com/en-us/answers/index.... 

It is oriented to admins and corporate users, and this forum - to home users so local experts may have no corresponding knowledge, sorry.
