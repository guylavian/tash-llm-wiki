---
title: "Exchange Message Tracking Log Retention Period & Impact on Performance"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/109476/exchange-message-tracking-log-retention-period-imp
question_id: 109476
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Message Tracking Log Retention Period & Impact on Performance

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/109476/exchange-message-tracking-log-retention-period-imp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We have 2 X Exchange 2016 servers with message tracking log retention period of 90 days with max Log directory size of 4 GB. We are planning to increase this to 18 months. How this change impact the performance of Exchange, also will there be a delay in searching the logs?   

What about the option of keeping a backup of log files once in every 3 months and restore them to exchange log directory when ever required? If this is the optimal solution, then, after restoring the log files what are the steps that we need to take in order to search the log (Message tracking)  

Thanks in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-28*

By default  max age for a log file is 30 days, and the maximum size for a single file is 10 MB.     

Hence all message tracking logs in the default directory cannot exceed 1 GB.     

But if you need to keep logs more than that, you can use separate dedicated volume for that minimize performance issues.    

You can use Windows Powershell to analyze track data,    

Please refer for more details,    

https://practical365.com/exchange-server/speed-up-multi-server-message-tracking-log-searches-with-powershell-remoting/    

https://learn.microsoft.com/en-us/powershell/module/exchange/get-messagetrackinglog?view=exchange-ps
