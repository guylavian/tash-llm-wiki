---
title: "Automatic windows update GPO - Week of the Month"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/726592/automatic-windows-update-gpo-week-of-the-month
question_id: 726592
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Automatic windows update GPO - Week of the Month

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/726592/automatic-windows-update-gpo-week-of-the-month (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We have Automatic Windows update configured via GPO , which contains below settings    

    

I could see, servers are properly configured with settings in registry based on GPO configuration , still servers are getting rebooted in different timings also I want clarification on considering week of the month.    

Could please provide me explanation on how to calculate each week of the month(Windows update GPO) considering Feb 2022 as a month.    

First week of the month        Disabled     

Second week of the month   Disabled     

Third week of the month      Enabled     

Fourth week of the month    Disabled

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-08*

Hello,    

In the thread below you have good explanation on how it works, based on it you should consider a full week in your calculation so if we take feb22 we have 3 weeks in it    

https://learn.microsoft.com/en-us/answers/questions/144710/configure-automatic-updates-how-exactly-do-the-34w.html    

Regards,
