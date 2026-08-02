---
title: "MFA for onprem domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/266673/mfa-for-onprem-domain-controllers
question_id: 266673
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# MFA for onprem domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/266673/mfa-for-onprem-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible to have MFA integrated to onpremise AD?  

Like when they login using the domain admin account they will go through MFA.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-10-02*

Guys,   

I think today a solution is technically possible using FIDO2 keys and the old domain "SCRIL" feature.  

Also Remote Credential Guard and Protected Users are components required.  

Here all the details :  

https://techcommunity.microsoft.com/t5/security-compliance-and-identity/removing-onprem-domain-admins-passwords-with-azure-passwordless/m-p/2803878  

Please test yourself reporting feedbacks :) (I only tested in my lab , never in production so a running test might be appreciated ..)

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-25*

Hi. You can enable granular MFA on any/all on-premise AD users with a third party solution UserLock. 

More information here: [https://www.isdecisions.com/products/userlock/multi-factor-authentication-mfa-active-directory.htm

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-13*

Thanks for your answers guys. I'm sorry If I can mark only one as Answer.  

By the way, to help others who are also needing this, we are going to test Okta's service to apply MFA for on-prem DCs.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-10*

Hi,    

As of July 1, 2019, Microsoft no longer offers MFA Server for new deployments.     

New customers that want to require multi-factor authentication (MFA) during sign-in events should use cloud-based Azure AD Multi-Factor Authentication.    

For more information , you can refer to the following link:    

https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-mfaserver-nps-rdg    

https://learn.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa    

Best Regards,
