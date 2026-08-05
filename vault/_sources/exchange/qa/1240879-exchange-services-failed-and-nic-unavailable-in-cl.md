---
title: "Exchange services failed and NIC unavailable in cluster after migrated to new VM host"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1240879/exchange-services-failed-and-nic-unavailable-in-cl
question_id: 1240879
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange services failed and NIC unavailable in cluster after migrated to new VM host

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1240879/exchange-services-failed-and-nic-unavailable-in-cl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,

I have to migrate 2 Exchange DAG servers to new VM Host. After migrated one of the node, that server cannot access EAC or EMS. 

In event log, it have 1564, 1228 and 5328 errors. Seem the node cannot access the witness server. Then I check in cluster manager, this node is down and it's NIC shown unavailable. 

However, the cluster validation report shows everything is healthy. And the server can access the witness server as normal. 
Any idea to resume the cluster node and exchange services?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-19*

Hi @ Chong ,  

Because you are migrating Exchange Server  using a third-party tool, we recommend that you consult their technical support for more information about the migration process.

For the usual approach, we recommend the following scenarios:

-  Join the new VM host to the domain and install the new Exchange server.

2. Add the new Exchange server to the DAG.

3. Move any active mailbox databases or database copies from the original DAG member to the new DAG  member.

4. Remove the original DAG member from the DAG, uninstall  Exchange from it, and retire the  VM host on which it runs.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
