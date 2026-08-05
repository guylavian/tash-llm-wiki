---
title: "Active Directory Domain referrals / domain realm mapping"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/553317/active-directory-domain-referrals-domain-realm-map
question_id: 553317
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory Domain referrals / domain realm mapping

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/553317/active-directory-domain-referrals-domain-realm-map (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I would like to ask that how active directory domain referral works.  

Concept "referral" comes from kerberos, refer to https://datatracker.ietf.org/doc/html/draft-ietf-krb-wg-kerberos-referrals-12#section-8  

I built up a cross-realm trusts between Windows AD and MIT Kdc5.  

In MIT Kdc, the way referral works is storing domain_realm mapping at KDC's krb5.conf. Refer to https://web.mit.edu/kerberos/krb5-1.12/doc/admin/realm_config.html  

When client query a server in another domain, KDC will tell client which domain that server is in, if that server host name match domain_realm mapping at KDC's krb5.conf.   

However, I don't know how that works at windows AD.   

1> How referral works at Windows AD  

2> How I can set domain realm mapping at windows AD.  

Thanks for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-15*

Hello @Dolcino       

Referrals are not a very easy task to explain, due to the length of their interaction with your domain.     

I would recommend the next readings to understand how domain referral works, and with information on how to manage them:    

https://learn.microsoft.com/en-us/windows/win32/ad/referrals    

https://techcommunity.microsoft.com/t5/azure-active-directory-identity/referral-chasing/ba-p/243177    

Hope this provides more information about what you want to achieve,    

Best regards,
