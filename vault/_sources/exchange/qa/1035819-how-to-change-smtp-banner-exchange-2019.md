---
title: "How to change SMTP banner?  (Exchange 2019)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1035819/how-to-change-smtp-banner-exchange-2019
question_id: 1035819
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to change SMTP banner?  (Exchange 2019)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1035819/how-to-change-smtp-banner-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello! Please help me with a SMTP banner for Exchange 2019 - I already changed banner for 220 response but also need to change it after HELO command:    

    

How to change server name from mail.corp.company.com to mail.company.com? Thank you for support.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-05*

You know - something is wrong:

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-05*

```
Set-ReceiveConnector -Identity "Default FrontEnd MAIL"  -FQDN "mail.contoso.com"
```

Prob need to restart transport service after that

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-05*

Seems to me I changed SMTP banner only:    

    

Tell me please how to change FQDN - need to receive a real server name (mail.company.com)  in 250 response. It shows local server name at this moment.    

Just dont make this change if this is the default receive connector as mentioned above.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-05*

The only things you can change on a custom receive connector are the SMTP banner and the FQDN of the receive connectot?    

Have you done both?    

https://learn.microsoft.com/en-us/powershell/module/exchange/set-receiveconnector?view=exchange-ps
