---
title: "how to connect O365 account using exchange online with MFA enable without login prompt in powershell?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1069717/how-to-connect-o365-account-using-exchange-online
question_id: 1069717
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# how to connect O365 account using exchange online with MFA enable without login prompt in powershell?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1069717/how-to-connect-o365-account-using-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want login to O365 account using exchange online     

o365 account has MFA enable    

want to login to account without adding credentials to login prompt.    

any suggestion will greatly appreciated    

Thanks,    

Pavan

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2022-10-31*

You cannot, that's the whole idea of having MFA - the login attempt must be interactive. Either ask your admins to exclude your account from the MFA requirements (bad practice), add a trusted IP/range so you don't get prompted (better practice) or configure the device as Azure AD Joined (best, as you can use PRT, which counts as MFA). If the idea is to run scripts automatically, use the method outlined here instead: https://learn.microsoft.com/en-us/powershell/exchange/app-only-auth-powershell-v2?view=exchange-ps
