---
title: "Office 365 exchange url :https //outlook.office365.com/ews/exchange.asmx not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1039104/office-365-exchange-url-https-outlook-office365-co
question_id: 1039104
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Office 365 exchange url :https //outlook.office365.com/ews/exchange.asmx not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1039104/office-365-exchange-url-https-outlook-office365-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,    

We used office 365e xchnage service url to send email for an application.    

Now we observed emails are not being read and send using office365 exchange service url    

https //outlook.office365.com/ews/exchange.asmx .    

Please let us know what has been changed and let us know the steps to make it work    

Thanks    

Athulya

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-10*

@Athulya Pillai       

You could access this "https://aka.ms/DiagEnableBasicAuthinEXO" and run a diagnostic for your tenant. You will know whether basic auth was blocked:    

    

You can also temporarily enable it for your tenant. It will take about an hour for it to take effect:    

    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-07*

Sounds like you are using basic auth? Thats been disabled:    

https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online
