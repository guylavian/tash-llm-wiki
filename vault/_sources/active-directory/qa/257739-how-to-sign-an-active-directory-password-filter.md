---
title: "How to sign an Active Directory password filter"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/257739/how-to-sign-an-active-directory-password-filter
question_id: 257739
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to sign an Active Directory password filter

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/257739/how-to-sign-an-active-directory-password-filter (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a customer that is enabling protected mode on their domain controllers.  This is causing our password filter to fail to load.  I must be signed.  We have tried signing the code with the cross signing certificate ( our certificate is from digicert ).  I understand that cross signing is no longer supported.  The only option I have found is to submit a package to the Hardware Portal for signing.  All the docs related to that seem to be related to device drivers.  A password filter is just a kernel extension.  Do I need to use HLK to create a package to get it signed or is their a simpler way to do it for a password filter?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-04*

Hi,  

Welcome to share here!  

Regarding the password filter signing , i'm afraid i can't provide the professional advices.  

I would do more research about it .  

If it is urgent , i would suggest you contact Microsoft Customer Services and Support to get an efficient solution:  

https://support.microsoft.com/en-in/hub/4343728/support-for-business  

Thanks for your understanding !  

Best Regards,
