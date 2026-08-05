---
title: "why i get kerberos ticket even from local user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/858499/why-i-get-kerberos-ticket-even-from-local-user
question_id: 858499
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# why i get kerberos ticket even from local user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/858499/why-i-get-kerberos-ticket-even-from-local-user (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

im joined windows 10 machine to domain, one day i logged as domain user,say john@keyman  .com. after few days i rebooted machine and logged as local administrator account, and still got john@keyman  .com ticket TGT     

i dont want this. im typing klist purge , ticket dissapearing but after few seconds it again getting and in klist i see this ticket again. also tried klist purge_bind but no success.     

why this happening? i think ticket refreshing on some interval but why it is doing this while i logged as local user and didnt logged in as john@keyman  .com after reboot?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-21*

Do you have any processes / services running under your domain ID?
