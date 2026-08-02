---
title: "Exchange Online V2 module memory management issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/179366/exchange-online-v2-module-memory-management-issues
question_id: 179366
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange Online V2 module memory management issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/179366/exchange-online-v2-module-memory-management-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to migrate to Exchange Online V2 module(EXO V2) from EXO V1. However, when we connect using the Connect-ExchangeOnline cmdlet, we observe the memory utilization goes to around ~200MB for the process.   

We do this from C# code. However, doing the same from powershell.exe also gives us similar observation.  

Post connect, we call the Disconnect-ExchangeOnline. We were under the impression calling the Disconnect-ExchangeOnline cmdlet should release the resources\memory. However. we don't see this happening. The memory utilization does not change.   

Same connection establishing in V1 does not consume so much memory. For our solution we need to make continuous calls to O365 for different tenants.  Our observation has been over a period of time this memory utilization keeps adding up and we end up running out of memory.   

We tried to dispose the runspace, abort the thread etc. But unless the process is killed, the memory is not reclaimed.   

We needed some pointers for this memory utilization. How can be make the EXO V2 connect call release the memory it has reserved?

## Answers

_No answers on this thread._
