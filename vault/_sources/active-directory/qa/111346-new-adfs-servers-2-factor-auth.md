---
title: "New ADFS Servers 2 factor auth"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/111346/new-adfs-servers-2-factor-auth
question_id: 111346
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# New ADFS Servers 2 factor auth

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/111346/new-adfs-servers-2-factor-auth (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I am wondering if anybody has come across this issue that I am having.    

I am in the process of upgrading ADFS from a 2012 r2 farm to a 2019 farm.    

The ADFS proxy servers have been replaced with server 2019 & these have been working fine for a week    

The issue that I come across is that when I replace the internal ADFS servers with server 2019 servers these go into a login loop.     

If I connect from a site where the conditional access policy does not apply the new ADFS servers work as expected.    

Me & my colleague believe that this is due to the azure authentication app not being able to be connected to, to supply 2fa.     

A conditional access policy has been applied requiring 2fa when not on a trusted network.    

I am guessing that there is something that needs to be configured on the new servers.     

This url may be what I am after, but it mentions configuring this on all ADFS servers. I dont want to break the existing 2012 R2 servers, as they are my fall back. I am not sure how the existing servers were configured to connect to Azure MFA, as the person who configured it left & there is no documentation    

configure-ad-fs-and-azure-mfa    

Is this the MFA Adapter?     

I do have 2 Radius servers setup, but not configured to allow 2fa to azure.    

Thanks    

Matt

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-22*

What's requiring you to stay on ADFS? We have workshops to help move off ADFS https://techcommunity.microsoft.com/t5/community-events-list/microsoft-workshops-how-to-successfully-migrate-away-from-ad-fs/m-p/3668480 & https://www.microsoft.com/en-us/security/business/identity-access/upgrade-adfs
