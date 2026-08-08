---
title: "General Health status report for Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1090370/general-health-status-report-for-exchange-2019
question_id: 1090370
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# General Health status report for Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1090370/general-health-status-report-for-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Am looking for recommendation for a decent Exchange 2019 health report script.      

In our Exchange 2013 environment I used this script from Paul Cunningham however I don't believe this works for Exchange 2019...    

https://practical365.com/powershell-script-exchange-server-health-check-report/    

Thanks,    

Will

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-16*

Thanks everyone.      

It looks like someone else came up with a script mod that makes it work for Exchange 2019 as well:    

https://github.com/cunninghamp/Test-ExchangeServerHealth.ps1/pull/36/commits/7a8fc75e0ec3135649b1c7243c19550b7f156a52

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-16*

@WilliamW      

Microsoft provide a HealthChecker script for all version of Exchange server in this article. It will be useful to you:    

    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-15*

It says it works for "2016/2013/2010", so it should work for 2019. There isnt much difference between 2016 and 19
