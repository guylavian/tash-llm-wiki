---
title: "connecting outlook on mobile to internal exchange server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/138018/connecting-outlook-on-mobile-to-internal-exchange
question_id: 138018
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# connecting outlook on mobile to internal exchange server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/138018/connecting-outlook-on-mobile-to-internal-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I can easily connect the outlook on pcs to my internal exchange server 2019 with both imap and mapi method.  

 but on mobile devices i encounter "timeout" and "can't reach server" problem !  

I tried all possible way with android gmail and outlook and ios mail and outlook but from these only gmail and ios mail work with imap method!  

the firewall on server is totally turned off and checked dns autodiscover and _autodiscover and i even scaned the open ports on server with same mobile devices and all corresponding port (25,143,443,993,587,465 ) are open!   

and even set internal and external addresses of owa autodiscover ecp mapi imap  the same but still gets timed out!!!  

plz help  

Tnx

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-26*

Hi @admin admin213   ,    

Is this your first time configuring Outlook on your mobile?    

Only one account have this issue or all have?    

-  I agree with ManuPhilip said that please make sure to configure the SSL certificate correctly.    

-  Please try to clean up the cached information in Outlook for IOS/Android, then uninstall and reinstall Outlook, and finally follow the specific steps in the following link to configure.    

For more information: Set up email in the Outlook for Android app and Set up the Office app and Outlook on iOS devices    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-10-25*

The best online tool to start troubleshooting the issue from Microsoft is here: exchange

You will find the actual issue (firewall, port, certificate etc.) from the detailed error message
