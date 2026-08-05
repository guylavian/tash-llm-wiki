---
title: "High occurrence of mailbox database copies with status of \"Passive failed and suspended\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1598491/high-occurrence-of-mailbox-database-copies-with-st
question_id: 1598491
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# High occurrence of mailbox database copies with status of "Passive failed and suspended"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1598491/high-occurrence-of-mailbox-database-copies-with-st (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have x2 Exchange 2016 servers with a DAG that consists of x4 mailbox databases.  We are experiencing a high frequency of 1 or 2 of the database copies showing as "Passive Failed and Suspended".  I usually click the Update option and it rebuilds/copies from the active server to the secondary.  This is not only tedious but is reflective of something not quite right.  I've looked through Exchange logs and can't pinpoint anything wrong.  Can someone give me an idea as to the possible cause or where to start looking?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-27*

Hello @Bill Clark,

Based on the information you've provided, there appears to be an issue with replicating mailbox databases between the two Exchange servers. This can be caused by a variety of factors, such as network connectivity issues, disk I/O issues, or even misconfiguration of the DAG itself.
To understand the root cause of the problem, you could run Test-ServiceHealth and Test-ReplicationHealth from the Exchange Management Shell (EMS). This will provide information that all required services are running. In addition, it could be a network connection issue between servers. You may want to check your network connectivity and make sure there are no firewall rules blocking replication traffic. When you have a mailbox database copy with a status of "Passive Failed and Pending", you might be able to try manually reseeding the problematic database copy.
More information for your reference:https://www.stellarinfo.com/article/reseed-a-failed-database-copy-in-exchange-server.php(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.) 

Hope the above information is helpful to you！

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
