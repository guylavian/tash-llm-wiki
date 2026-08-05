---
title: "ADFS 4 and SharePoint 2016 with non-claims-aware applications ISSUES"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/292257/adfs-4-and-sharepoint-2016-with-non-claims-aware-a
question_id: 292257
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS 4 and SharePoint 2016 with non-claims-aware applications ISSUES

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/292257/adfs-4-and-sharepoint-2016-with-non-claims-aware-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have successfully deployed ADFS v4 + WAP (on-prem Windows server 2016)  and we are publishing SharePoint 2016, Skype for Business and also using ADFS as an IDP to access a quite few cloud based applications with SAML.    

Now, in order to have SharePoint 2016 working properly, we have published it as "non-claims-aware" and it is using Kerberos-Windows integrated authentication instead and we have NO issues.     

You probably are aware that if we publish SharePoint as a "Claims-aware" we will encounter issues with people picker, searches, etc. that don't work properly and in order to address some of these issues we need to deploy third party claims provider app: LDAPCP and MS clearly states "LDAPCP isn't a Microsoft product and isn't supported by Microsoft Support" -https://learn.microsoft.com/en-us/sharepoint/security-for-sharepoint-server/implement-saml-based-authentication-in-sharepoint-server. So, this configuration was a No go for our production environment.     

Moving forward to 2021, we need enhance security in our ADFS deployment so we are looking for different ways to protect our ADFS+WAP environment and so far the only way we found and it is published on MS site as well, is that we can replace the WAP role for 2 third party solutions:    

-  F5 BigAP (APM+LTM) or     

-  Citrix ADC (premium license),  both solutions will add load balancing, WAF, etc. .     

So far, this is looking great! BUT, here is our huge headache: Which of these 2 applications has still the option to keep using "non-claims-aware\Kerberos authentication" to publish applications???? or Does MS has another way/workaround to add all these security features (WAF, ddos protection, LB, etc.). into an ADFS+WAP farm.    

Thanks and I look forward to hearing from you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-26*

yes that's the way i use adfs based on server 2019 myself  

Marcel

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-25*

Hi  MarcelPalme-8257,  

Thanks for the update and are you aware if this vulnerability is present on Windows  server 2016 or 2019? that KB refers to W2012 R2 only.  

Mike

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-04*

Thanks for the reply Piaudonn!
