---
title: "Active Directory password reset Unlock users account ticked by default"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/764003/active-directory-password-reset-unlock-users-accou
question_id: 764003
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory password reset Unlock users account ticked by default

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/764003/active-directory-password-reset-unlock-users-accou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey, I have a strange issue with on-premise Active Directory.     

Whenever someone right clicks on a user in Active Directory, the "Unlock the user's account" check box is always ticked. Apparently this has been a problem for a while but due to some recently introduced software, its now causing problems.     

We see the box checked, regardless of the user account, when it was created, how it was created (copy of existing or brand new) this box is checked. Its also regardless of the OU the account is in, doesnt matter if its domain.local\Users or a custom nested OU structure so whatever is causing this seems to be coming from the root level of the domain.     

It happens on all Domain controllers, the domain functional level is 2016.     

Does anyone have any ideas why this may be happening?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-15*

Hello @Liam H       

In my experience this is  UI behavior by default that whenever user's account is locked out due to incorrect password then this check box "Unlock the user's account" check box will be enabled by default.    

I have just tested in my two different AD environment and this box was enabled when I try to right click of user whose account is locked.    

https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/locked-or-not-demystifying-the-ui-behavior-for-account-lockouts/ba-p/400245    

Hope this answers your question  :)    

Thank you.    

--    

--If the reply is helpful, please Upvote and Accept as answer--
