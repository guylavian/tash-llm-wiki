---
title: "Implement MFA for Active DIrectory sign on"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/418027/implement-mfa-for-active-directory-sign-on
question_id: 418027
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Implement MFA for Active DIrectory sign on

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/418027/implement-mfa-for-active-directory-sign-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi everyone,  

Hope you are all doing well.   

I just start to do research on this. We are considering turning on MFA for our Active DIrectory user sign on. We are not on Azure (except the fact that our email is thru Office 365). We are still running 2012 scheme and domain controllers (but will upgrade them all to 2016). 95% of the users are running windows 10.  

Do you know if Microsoft provide built-in MFA for domain sign on? Or I need to purchase a product to achieve it ? IF the answer is latter...do you have any good product you are using?  

Thank you for your help in advance.  

Takami Chiro

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-02*

Hello @Takami Chiro  ,    

Thank you for posting here.    

Here are the answers for your references.    

Q: Do you know if Microsoft provide built-in MFA for domain sign on? Or I need to purchase a product to achieve it ?    

A: Based on my knowledge, you are using on-premise Active Directory, there is no built-in MFA for domain sign on from Microsoft.    

Q: IF the answer is latter...do you have any good product you are using?    

A: Based on my knowledge, if you use Azure AD, Microsoft provide built-in MFA for domain sign on, for more information about Azure AD MFA, please refer to link below.    

Secure access to resources with multifactor authentication    

https://www.microsoft.com/en-us/security/business/identity-access-management/mfa-multi-factor-authentication    

And if you want to know more information about Microsoft Azure AD MFA, please open a new post by selecting Azure Active Directory tag or Azure-ad-multi-factor-authentication tag.    

And for on-premise Active Directory, if you want to know MFA, you can google in the internet and see if there is any third-part MFA.    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
