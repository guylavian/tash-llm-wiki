---
title: "Create a task scheduler via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/87291/create-a-task-scheduler-via-gpo
question_id: 87291
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Create a task scheduler via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/87291/create-a-task-scheduler-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need create a task scheduler, and this scheduler will periodically run a remote batch (use UNC Path). and I realize, only use SYSTEM account the GPO can be successfully pushed to client side.  But the remote batch can't run because privilege issue.  

I want to ask, have any way to fix this?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-07*

Hello,    

Thank you so much for posting here.    

As per the Scheduled Tasks GPO, we could choose the user account when running the task as shown below. We could kindly have a try.    

    

Besides, have we considered about script as shown below?     

    

Hope the information is helpful. For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
