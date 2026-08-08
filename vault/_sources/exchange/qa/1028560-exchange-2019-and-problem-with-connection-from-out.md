---
title: "Exchange 2019 and problem with connection from Outlook Mobile"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1028560/exchange-2019-and-problem-with-connection-from-out
question_id: 1028560
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 and problem with connection from Outlook Mobile

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1028560/exchange-2019-and-problem-with-connection-from-out (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I have got exchange on premise 2019 where I use to connect only ActiveSync.    

When I configure my Outlook on the computer it's working, but when I tried to configure Outlook Mobile on my mobile phone with these settings:    

e-mail: j.smith@Company portal   .com    

mail server: mail.contoso.com    

Domain\user_name: domain\jsmith    

Password:*******    

I've got an error:    

Login error    

The connection to your mail server has expired. Check your mail settings.    

How to resolve this problem? Is it the issue in exchange settings?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-03*

Verify all the Exchange Services are running and the autodiscover app pool is started. Restart the sevices if necessary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-03*

Someone? Somethink?
