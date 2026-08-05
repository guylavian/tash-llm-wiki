---
title: "Server 2003 dcdiag reports: \"Warning :There is less than 9% available RIDs in the current pool\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/437421/server-2003-dcdiag-reports-warning-there-is-less-t
question_id: 437421
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Server 2003 dcdiag reports: "Warning :There is less than 9% available RIDs in the current pool"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/437421/server-2003-dcdiag-reports-warning-there-is-less-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Upon an investigation carried out for some entirely other purpose, the following message came up when running on our Server 2003 R2 (soon to be decommissioned) that holds the PDC roles of our AD:

Starting test: RidManager  

* Available RID Pool for the Domain is 3106 to 1073741823  

* mysrv.mydomain is the RID Master  

* DsBind with RID Master was successful  

* rIDAllocationPool is 2606 to 3105  

* rIDPreviousAllocationPool is 1606 to 2105  

* rIDNextRID: 2061  

* Warning :There is less than 9% available RIDs in the current pool  

......................... MYSRV passed test RidManager

Now, if I understand correctly, there is no issue of exhaustion here: the current pool is at 3106 and there are a billion RIDs to work with. Since the warning came up I thought that the counting was downwards to zero and got freaked up. But reading around it seems that it is counting up to 1073741823. Therefore, can I presume that all is well? And, if so, why did this warning came up (and cut 10 years from my life)?

## Answers

_No answers on this thread._
