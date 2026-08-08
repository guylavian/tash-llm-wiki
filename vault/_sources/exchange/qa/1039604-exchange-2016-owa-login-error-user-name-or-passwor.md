---
title: "Exchange 2016 owa login error user name or password is wrong when password is expired"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1039604/exchange-2016-owa-login-error-user-name-or-passwor
question_id: 1039604
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Exchange 2016 owa login error user name or password is wrong when password is expired

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1039604/exchange-2016-owa-login-error-user-name-or-passwor (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange server 2016 owa:     

Password expired for a user. User tries to login to owa, but cannot login. "The user name or password you entered isn't correct. Try entering it again."    

Shouldn't Owa prompt the user that their password has expired and prompt them to change it?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-10*

Hi @shrvan   ,    

I tested in a test environment and when the user's owa password expired, entering the original password would jump to the change password page.    

    

You could check the following situations:    

-  Whether to set the user forbidden to change the password    

    

-  Check the minimum password change period    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
