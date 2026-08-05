---
title: "Exchange 2010 sp3 ru31 After I enabled outlook anywhere, I found that one machine didn't work"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/313294/exchange-2010-sp3-ru31-after-i-enabled-outlook-any
question_id: 313294
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2010 sp3 ru31 After I enabled outlook anywhere, I found that one machine didn't work

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/313294/exchange-2010-sp3-ru31-after-i-enabled-outlook-any (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI engineer  

```
After I enabled outlook anywhere, I found that one machine did not work and the other one was normal. I recently updated to ru31
```

We look forward to your reply.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-15*

Hi @超 邓  ,    

By "one machine didn't work", do you mean the user cannot add his account on that machine? Is there any error message?    

What's the detailed version of the Outlook client?    

Please compare if the Outlook version on problematic machine is the same as the normal machine. Also check if they are in the same network environment.    

Besides, you can try running the Outlook Connectivity test using the Microsoft Remote Connectivity Analyzer tool and see if there would be any clues.    

By the way, Exchange 2010 has hit End of Life as of October 13, 2020, so it's highly recommended to start planning migrating to Exchange 2016 or Microsoft 365.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
