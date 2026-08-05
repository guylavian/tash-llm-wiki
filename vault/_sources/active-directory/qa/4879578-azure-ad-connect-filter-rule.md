---
title: "Azure AD connect filter rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4879578/azure-ad-connect-filter-rule
question_id: 4879578
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Azure AD connect filter rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4879578/azure-ad-connect-filter-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all

I am running the latest version of Azure AD connect. We have roughly 20,000 user objects that we do not need to sync to Azure AD, because they have no mail properties. I want to create a rule in Azure AD connect that filters these users out so they do not
 sync. Knowing that all objects that are mail enabled have a value for  the "MSexchangerecipientTypeDetails" attribute, i want to create a rule that says if AD attribute  "MSexchangerecipientTypeDetails" equals "Null" do not sync. 

I have seen a few examples on how to filter users based on custom attribute, but i am not able to use the same logic from these examples to build a rule that will do what i need. Any help is appreciated

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2016-03-05*

Hi SkipHofmann2670,

Generally, users can follow the steps in the link below to filter attributes:

Azure AD Connect sync: Configure Filtering

I understand that you have some special requirements. Given the situation, to better help you, we suggest you post a new thread in our
Azure forum for dedicated assistance.

Your understanding is highly appreciated.

Best Regards,  

Erick
