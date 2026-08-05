---
title: "ADFS Single Sign On with ReactJS (Frontend) /.Net Core Web API (Backend)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/284235/adfs-single-sign-on-with-reactjs-frontend-net-core
question_id: 284235
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-aspnet-core-other-l1", "microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Single Sign On with ReactJS (Frontend) /.Net Core Web API (Backend)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/284235/adfs-single-sign-on-with-reactjs-frontend-net-core (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are having react app as frontend application and .NET Core Web API as Back end application. Our client requirement is to integrate ADFS SSO. Our Client is already having On-Premises ADFS running in their windows server 2016.  

After some googling I have following questions raised up in my mind.  

1.) Based on my analysis, ADFS is supporting following sign-in protocols (SAML 2.0, WS-Federation & OAuth). For our application setup(React/.NET Core Web API), which protocol, we should use?  

2.) Our client is asking us to use for SAML2.0. Is SAML 2.0 Protocol can be used for our application architecture (React/.NET Core Web API)?  

3.) To configure our application in On-Premises ADFS, I saw following options (Relying Party Trust and Application Groups). For our application architecture, which one should be used?  

Please help me with your thoughts. I am not able to take any concrete decision on the above questions since I am new to the ADFS SSO. Your help is much appreciated. Thanks in advance.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-02-23*

Only the dev/architect of the application would know what model would be the best fit.  

SAML2 is old school. That works, and that's supported by ADFS. But that's usually not a good fit for those multi tier apps. I mean, that's the very reason was OAuth2 was born.   

In general, for a modern multi-tiered application, OAuth2/OIDC seem to be a better option as it is very flexible for these scanario. But that depends if the frontend has to authenticate the end user, what type of access/auth between the frontend and the backend, etc...  

OAuth2 applications are created in ADFS through the Application Groups wizard.
