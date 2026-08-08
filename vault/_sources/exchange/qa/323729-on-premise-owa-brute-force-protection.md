---
title: "On Premise OWA Brute force Protection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/323729/on-premise-owa-brute-force-protection
question_id: 323729
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# On Premise OWA Brute force Protection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/323729/on-premise-owa-brute-force-protection (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, please can someone advise if a owa captcha can be setup on exchange 2016, or the best way to lock out the user account after 4 incorrect logon attempts on owa (on prem) - cant see it in active directory? This has been brought more in to focus after the recent Microsoft exchange vulnerability with brute force attacks now more of a concern on owa / mobile active synch.  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-20*

Thanks Andy,  

Would we need to purchase the office 365 email / exchange package for this. Licensing is currently for on-prem. so don't want to go for a full online solution just yet.   

Or should we just use owa with vpn access. Owa is currently accessible externally on 443  

cheers  

Ash

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-20*

Not possible natively.     

Look at using ADFS with OWA:    

https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019    

and then setting the Extranet Smart Lockout to stop these:    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-ad-fs-extranet-smart-lockout-protection    

Really though, a Multi-Factor solution integrated with that is the best solution.    

You can leverage 3rd party MFA or use Azure:    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/hybrid-modern-auth-overview?view=o365-worldwide
