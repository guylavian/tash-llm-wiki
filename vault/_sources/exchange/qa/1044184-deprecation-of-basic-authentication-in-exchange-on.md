---
title: "Deprecation of Basic Authentication in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1044184/deprecation-of-basic-authentication-in-exchange-on
question_id: 1044184
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Deprecation of Basic Authentication in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1044184/deprecation-of-basic-authentication-in-exchange-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

It appears Microsoft removed the ability to use Basic authentication in Exchange Online this past weekend for Exchange ActiveSync (EAS), POP, IMAP, Remote PowerShell, Exchange Web Services (EWS), Offline Address Book (OAB), Outlook for Windows, and Mac. This requires users to move from apps that use basic authentication to apps that use Modern authentication. Therefore, affected mobile users that uses their phone's native email app and are prompted with the “unable to sign in” or “enter password” message on their phone.  This requires them to re-authenticate their email account by removing and re-adding their account on their mobile devices. However, some users are still unable to sign in even after removing their account from their phone. The only solution is to reset their password in this case.     

I want to do why it works for some users to sign in after removing and re-adding their account on their phone, but some users would require admin to change their password on the domain in order to sign in their account on their phone?     

Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-13*

Did you check this article? - https://techcommunity.microsoft.com/t5/exchange-team-blog/basic-authentication-deprecation-in-exchange-online-september/ba-p/3609437
