---
title: "ADFS via Internet"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/22947/adfs-via-internet
question_id: 22947
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS via Internet

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/22947/adfs-via-internet (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Technet, hope you can help me moving forward.  

I have a WebApp Proxy with ADFS (V4) in place. Is it possible to use SSO via Internet: take my laptop (AD member) outside of the network, connect it via mobile phone to the Internet and access then a resources of the company. ADFS is then asking for credentials (login with username & password is working (manually entered)). Can I delegate my creds I used to sing in on the laptop to ADFS?  

Thanks for your input,  

Chris

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-04-16*

First of all, if the goal is to have SSO with Azure AD (and Office 365), you don't even need ADFS to make it work seamlessly from outside the organization. So if that's the case, let us know we'll explain!    

Then, you can use different authentication methods to log on to ADFS. For example, you could use certificate based authentication as a primary authentication method.    

Or, in the same spirit, you could use Azure MFA as a first factor for authentication too. And when you connect to ADFS, you will just have to accept the notification on your phone (no password involved).
