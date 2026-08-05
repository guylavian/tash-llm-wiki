---
title: "About the security alerts of Exchange 2016/2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/305461/about-the-security-alerts-of-exchange-2016-2019
question_id: 305461
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# About the security alerts of Exchange 2016/2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/305461/about-the-security-alerts-of-exchange-2016-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have our Exchange servers 2016 in CU15.   

I would like to know, if this version also in risk of those problems or not?  

Thank you in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-10*

thank you all for your support,  

i did find practical365 blog regarding installing cu to exchange 2016,  

just would like to know, if it would be the same steps for installing the cu19 patch?  

thank you in advance,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-10*

Agree with Andy, you need to upgrade to CU19 and install the patch.    

You can follow the blog to install the upgrade: https://practical365.com/exchange-server/installing-cumulative-updates-on-exchange-server-2016/    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-09*

Note you can now apply a CU15 specific patch. If you cant upgrade to CU19, then apply this patch in the short term to protect your servers and upgrade to CU19 as soon as possible  

https://www.microsoft.com/en-us/download/details.aspx?id=102789

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-09*

Yes, and even a couple more since CU15 has been out of support for a good while now (June 16, 2020) and other security updates have been released in the mean time as well.  

Update to CU19 as soon as possible and then apply the security updates.  

Once CU20 comes out, make a plan to update to remain supported; Only the last 2 CUs are supported, so once CU22 comes out, CU20 is no longer supported.
