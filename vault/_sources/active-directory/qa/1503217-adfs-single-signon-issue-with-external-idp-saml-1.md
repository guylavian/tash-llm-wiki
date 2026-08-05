---
title: "ADFS Single signon issue with external idp - SAML 1.1 Assertion is missing ImmutableID of the user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1503217/adfs-single-signon-issue-with-external-idp-saml-1
question_id: 1503217
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Volunteer Moderator"]
---
# ADFS Single signon issue with external idp - SAML 1.1 Assertion is missing ImmutableID of the user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1503217/adfs-single-signon-issue-with-external-idp-saml-1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have office 365 + Onperm AD + ADFS for federation. 
I have configured Shibboleth as a second Claims provider (MFA enabled). When I tried to login to office 365, I get Windows AD and Shibboleth as options, when I click on Shibboleth, I get authenticated but finally I get the following error
SAML 1.1 Assertion is missing ImmutableID of the user
The IdP is providing the following 
IDPEmail = UPN
ImmutableID =ObjectGUID
adfssamaccountname = samaccountname
I understand that I have to create a rule in ADFS, but not sure what to create 
Claim rule? or Claim issuance policy or both? 
I would appreciate your expert knowledge in this regard. 
Thanks in advance

## Answer (community) — Volunteer Moderator

*upvotes: 1 · updated: 2024-01-23*

Hi @Dinesh Loganathan  

Your configurations seemed okay, without looking else to another trouble.

We just need few clarifications and some additional points to consider:

-  You need to create claims in the Claims Provider Trust (Shibboleth) based on the SAML attributes you receive from Shibboleth. These claims will map the incoming SAML attributes to ADFS claims.  Ensure that the claim types, formats, and values match the SAML attributes you provided.

-  Create Claim Issuance Policies in the Relying Party Trusts (for ClaimsXray and Office365) to specify how claims should be issued for these relying parties.   In each Claim Issuance Policy, you'll define rules that determine which claims are issued and how they are mapped or transformed.

-  For Office365, you mentioned an extra claim issuance policy for ImmutableID. Ensure that you are correctly mapping the ImmutableID claim to the corresponding attribute received from Shibboleth.

You are doing a great job, check those three above and conduct all the necessary test. You should be fine.

Success.
