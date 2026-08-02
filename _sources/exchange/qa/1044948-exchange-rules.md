---
title: "Exchange Rules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1044948/exchange-rules
question_id: 1044948
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Rules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1044948/exchange-rules (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there a way, when someone sends a message between 19:30 and 07:30, that you can create a rule that pops up a message saying 'do you really need to send this' or something similar?    

I don't need to stop the email just prompt people to think before they send.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-17*

@Craig Williams      

About transport rule, it does not take effect until the message is sent. So, transport rule doesn't suitable for this one.    

About Viva Insights, it could generate a notification when user send email outside of working hours:    

    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-12*

Outlook does that now if you have the right versions:    

https://learn.microsoft.com/en-us/viva/insights/personal/use/mya-notifications
