---
title: "What settings can be used in exchange online to control external calendar share permissions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2261806/what-settings-can-be-used-in-exchange-online-to-co
question_id: 2261806
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# What settings can be used in exchange online to control external calendar share permissions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2261806/what-settings-can-be-used-in-exchange-online-to-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have been reviewing Exchange online permissions that prevent sharing work resources with objects outside of ones 365 tenant.   

Let's say I have a user mailbox which has a calendar and I want to share it with my personal gmail account so I can use it in a third party app (I wouldn't do it this way it's just a hypothetical).   

If the user mailbox is allowed to share this calendar with an external address this could leak sensitive company information so I found you can disable this for all users by going to the admin center > org settings > services > calendar and unticking share with external.   

When testing this in a developer tenant before I change this setting it doesn't work regardless so I'm wondering if there is another setting/policy i.e DLP that could be restricting this?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-28*

For anyone going down this rabbit hole in future:  

Further testing shows this is the setting that does it and would enable it tenant wide. I ticked the box to allow it but it was getting unticked by our partner tool CIPP that manages these settings for each tenant we manage. Disabling this ensured the setting would stay either on or off.   

Allowing this for only one user where there is a business case can be done through a "sharing policy" in exchange.
