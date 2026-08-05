---
title: "Exchange system attendant error during room mailbox creation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/247120/exchange-system-attendant-error-during-room-mailbo
question_id: 247120
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange system attendant error during room mailbox creation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/247120/exchange-system-attendant-error-during-room-mailbo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi we have problem with error message when creating room mailbox on exchange 2016 with error   

"This mailbox was created successfully, but some properties weren't saved." "Cannot open mailbox <fullyDistinguishedName>/cn=Microsoft System Attendant."  

We have DAG deployed, where can i create homedb attribute for system attendant? We have 5 DAG databases. Can I go according to this article, it's for Exchange 2013  

http://www.networksteve.com/exchange/topic.php/Exchange_2013_-_Room_Mailbox_Creation/?TopicId=48581&Posts=0  

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-28*

Hi Eric we are on CU18 now, we have plan to go for CU19 next month, in the event log on these particular server i dint find event related to this problem, but it seems that room mailbox is working so will see next month after we update to CU19.  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-28*

Hi,     

The HomeDB is not set in my lab, but I never see this error.     

Does this issue happen on all your 5 servers? Can you find any related error in Eventlog?    

Which CU are you using? Try updaing to the latest CU19: Upgrade Exchange to the latest Cumulative Update    

Move the room mailbox to another database as a repair :    

```
New-MoveRequest -Identity '******@alpineskihouse.com' -TargetDatabase "DB01"
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
