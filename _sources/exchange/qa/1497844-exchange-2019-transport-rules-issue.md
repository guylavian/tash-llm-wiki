---
title: "Exchange 2019 Transport Rules Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1497844/exchange-2019-transport-rules-issue
question_id: 1497844
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 Transport Rules Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1497844/exchange-2019-transport-rules-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
We have Exchange 2019 DAG with 4 servers, we have Transport rule as Warning banner (disclaimer)  for External users sending email to internal users. So once email received from external user internal users will receive it with warning banner.
Now the issue is application notification emails also coming with same warning even though sender is form organization and also from same network. to come up with this issue we have added exclusion with email and add those application sender email id to this list. 
But we dont have any Idea, how come those Internal Application emails coming with external warning banner.
Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-01-16*

If they are being sent from outside of Exchange, they are considered unauthenticated and external. 
They would only be considered authenticated if the application was itself authenticating to Exchange or you created a receive connector that treated messages sent through it as externally secure
https://learn.microsoft.com/en-us/exchange/receive-connector-authentication-mechanisms-exchange-2013-help
Be very careful however using this setting.
