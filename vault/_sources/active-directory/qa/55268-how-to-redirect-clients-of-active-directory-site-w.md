---
title: "How to redirect clients of Active Directory site with RODC to another site when all RODC in site fail?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/55268/how-to-redirect-clients-of-active-directory-site-w
question_id: 55268
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# How to redirect clients of Active Directory site with RODC to another site when all RODC in site fail?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/55268/how-to-redirect-clients-of-active-directory-site-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!  

We have 3  sites: two central sites A and B with RWDC and remote site C with 1 RODC.  

What must we do to redirect clients of  site C with RODC to another site A (not to B) with RWDC when  RODC in this remote site fail? The access to site B is forbidden for security reasons.  

Thank you very much!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-31*

Hello,    

Thank you so much for posting here.    

When a user try to authenticate to an RODC, a check is performed to see if the password is cached on the RODC of the site. If the password is cached, the RODC will authenticate the user account locally. If the user’s password is not cached or RODC is not accessible, then the authentication request is forwarded to a writable Domain Controller which in turn authenticates the account and passes the authenticated request back.    

And if the RODC fails, the clients will find other DCs in other site. As mentioned, if site B is forbidden, it will find the DC in site A. Or if we would like to redirect the clients in site C to DC in site A, we could try to enable clients to locate the Next Closest Domain Controller. For more information about this, we could refer to:     

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/enabling-clients-to-locate-the-next-closest-domain-controller    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong
