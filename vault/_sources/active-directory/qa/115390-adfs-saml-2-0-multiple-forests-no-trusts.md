---
title: "ADFS - SAML 2.0 - Multiple Forests - No Trusts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/115390/adfs-saml-2-0-multiple-forests-no-trusts
question_id: 115390
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
---
# ADFS - SAML 2.0 - Multiple Forests - No Trusts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/115390/adfs-saml-2-0-multiple-forests-no-trusts (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a weird scenario. There are many companies that are owned by one company. We are moving to a cloud based helpdesk system that supports SAML authentication for SSO. Ultimately all companies will be in a single forest, but for now each company has their own domain and Forest/Domain/External trusts will not be allowed. Can ADFS be set up such that each Forest has an ADFS server with a relaying party trust to "The Root Domain" and have the ADFS in "The Root Domain" have a relaying party trust using SAML to the SAML SP? Can SAML SP authentication requests be handled with this scenario for SSO?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-06*

You can have federation between domains or trusts but not both.  

If you have 2 top level domains with no trust like contoso.com and fabrikam.com they can each have an ADFS Server and be federated to each other. But if the 2 domains have a 2- way trust then only 1 ADFS Should be used as it is a client to AD and would use UPN suffix routing just like any other AD client would.  

--  

Please let us know if this answer was helpful to you. If so, please remember to mark it as the answer so that others in the community with similar questions can more easily find a solution.
