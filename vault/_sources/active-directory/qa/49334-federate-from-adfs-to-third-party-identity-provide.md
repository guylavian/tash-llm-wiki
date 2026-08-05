---
title: "Federate from ADFS to Third Party Identity Provider"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/49334/federate-from-adfs-to-third-party-identity-provide
question_id: 49334
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Federate from ADFS to Third Party Identity Provider

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/49334/federate-from-adfs-to-third-party-identity-provide (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Have noticed that it is possible to federate from Azure AD to third party identity providers like Okta, Ping Identity via the Azure Portal (the customer does not want to use Azure AD)  

Is it possible to do the same via ADFS. Where when a client calls ADFS endpoint it would, in turn, call the relevant Identity Manager? If so is there a document or video highlighting the steps involved?  

Thanks in Advance,  

Scritz

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-20*

Yes, that is what I was referring to. I am not aware of any generic ADFS Documentation like that from Microsoft.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-19*

It was not whether we can set other IDP to point to ADFS (which is available in third-party IDP documentation like Okata), instead of whether ADFS can be configured to redirect to other IDP.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-19*

I would think you would need to consult the 3rd party support documents or their technical support to get this information.
