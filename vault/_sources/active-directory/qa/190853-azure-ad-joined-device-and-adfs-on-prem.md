---
title: "Azure AD Joined Device and ADFS (on-prem)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/190853/azure-ad-joined-device-and-adfs-on-prem
question_id: 190853
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Azure AD Joined Device and ADFS (on-prem)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/190853/azure-ad-joined-device-and-adfs-on-prem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey  

We have some Azure AD joined devices.   

We are able to access local shares using kerberos - but when using our local ADFS we are prompted for password. (from our local LAN)  

Is it possible to have SSO (like our domain joined machines when using ADFS)  

Thanks in advance.  

Mike

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-09*

There are many things to check. See here: https://learn.microsoft.com/en-us/answers/questions/173710/adfsiwa-integration.html    

But in your case, it might just be that the URL of your ADFS farm is not trusted by your browser. So make sure you push the URL of your ADFS farm as a trusted site or Intranet site (either locally in the browser or the local policy or through Intune).
