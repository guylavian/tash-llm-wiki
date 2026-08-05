---
title: "Exchange online powershell loging issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1019086/exchange-online-powershell-loging-issue
question_id: 1019086
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange online powershell loging issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1019086/exchange-online-powershell-loging-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I`m tring to login to exchange online powershell module using Connect-ExchangeOnline. but im getting the below error. i reinstall the module, but it same.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-23*

@Dhanushka Pannipitiya       

You can also try to install PowerShell 7, then install Exchange Online Management module and connect to Exchange online again.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-22*

What happens if you just enter Connect-ExchangeOnline without the userprincipalname switch?
