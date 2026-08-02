---
title: "Azure Active Directory connect with on prem ADFS caused Office.com account to not be able to login"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/892434/azure-active-directory-connect-with-on-prem-adfs-c
question_id: 892434
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Azure Active Directory connect with on prem ADFS caused Office.com account to not be able to login

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/892434/azure-active-directory-connect-with-on-prem-adfs-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Microsoft Partner Network with Azure credits and Azure AD. I recently got Azure AD Connect up and syncing with my on prem DC. I thought I'd try ADFS out as well and fully underestimated how bad I could screw things up. After fully implementing ADFS I realized externally I couldn't hit my 443 page but even internally in my LAN I could hit the landing page but couldn't login to office.com. I removed my ADFS role on my server and got it disabled in Azure AD connect. However I still have SSO enabled and Pass-Through authentication which I believe is why I still can't login to office.com with my licensed account using my custom domain name. Before messing around with ADFS I had sso through Go Daddy using this custom domain. I'd like to get back to just the AD sync working with Azure AD connect. Any tips would be much appreciated.

## Answers

_No answers on this thread._
