---
title: "need suggestion with Exchange legacy token"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2283005/need-suggestion-with-exchange-legacy-token
question_id: 2283005
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# need suggestion with Exchange legacy token

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2283005/need-suggestion-with-exchange-legacy-token (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,

It's bit confusing to check the Exchange legacy token related things for me and need some advice on same 

I run the below command 

Get-AuthenticationPolicy -AllowLegacyExchangeTokens

Got this result with one blocked and two allowed

When I try to use Get-App with allowed (starting with 4723 and 88fe) ID's I'm not getting any results

For blocked one i got the result as Phish alert (Third party application), Please suggest what i need to check and do further on this.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-06-11*

Hi, see:

https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/faq-nested-app-auth-outlook-legacy-tokens#what-do-i-do-for-add-ins-i-cant-identify

Essentially disable them and see who complains.

It's possible after running `Get-AuthenticationPolicy` there could be some custom add-ins that you can't identify the owner. For those add-ins you may need to perform a scream test. We recommend that administrators perform a scream test before June 2025 to determine if there are any remaining add-ins that will break when legacy tokens are turned off in June. This will give you time to reach out to publishers of any affected add-ins to address breaking issues before the June deadline.
