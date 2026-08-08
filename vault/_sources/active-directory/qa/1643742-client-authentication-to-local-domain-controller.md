---
title: "Client authentication to local domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1643742/client-authentication-to-local-domain-controller
question_id: 1643742
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Client authentication to local domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1643742/client-authentication-to-local-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All, Request you to help me to address below issue. We have 4 domain controller 2 in local (primary and secondary) and 2 in Far site (primary and secondary). However, most of systems are not authenticating login from local domain controller and i want it should authenticate with local login.   Pls advise

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-05*

Hello Siddhesh Mayekar,

Thank you for posting in Q&A forum.

You can create more than one site and put local domain controllers to one site and put other domain controllers to other sites.  

Local site (corresponding to subnet1)  

DC1 and DC2  

Far site (corresponding to subnet2)

DC3 and DC4  

For example, if you want domain machines to be authenticated using DCs in local site, you can set the IP addresses of these machines using the IPs belongs to subnet1.  

For example:

https://theitbros.com/active-directory-sites-and-subnets/#:~:text=Open%20the%20AD%20Sites%20and%20Services%20snap-in%3B%20Expand,your%20DC%3B%20Click%20OK%20to%20start%20the%20transfer%3B

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-04-04*

You need to configure AD sites/subnets to reflect your network environment. Details at https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/creating-a-site-design and https://www.techcrafters.com/portal/en/kb/articles/setup-ad-sites-and-subnets#Creating_a_New_Site

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
