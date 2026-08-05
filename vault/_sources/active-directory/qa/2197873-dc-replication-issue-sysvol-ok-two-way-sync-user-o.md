---
title: "DC Replication issue-Sysvol=OK(two way sync), User objects are one way only!!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197873/dc-replication-issue-sysvol-ok-two-way-sync-user-o
question_id: 2197873
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# DC Replication issue-Sysvol=OK(two way sync), User objects are one way only!!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197873/dc-replication-issue-sysvol-ok-two-way-sync-user-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We noticed an odd behavior where some of our DCs(not all of them, around 100 sites, connected via satellite WAN over VPN, different subnets, one forest, one domain)show some interesting replication issues.

1- Sysvol replication is fine and we do have clean two-way sync.

2- Adding new objects to DCs appear only from source to destination(one-way sync)

We do have hub-spoke topology and the above sync happens from the hub to spoke.

repadmin /replsummary shows no errors on the hub side.

no obvious networking issues on either side.

Appreciate any hints.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-24*

Hello SamNa1,

Based on the information you provided, it appears that you are experiencing replication issues with user objects in Active Directory. Since you mentioned that there is no problem with Sysvol replication, the issue may be related to the replication of domain partitions. 

Here are some steps you can take to resolve the issue: 

-  Check the replication topology: Ensure that the replication topology is configured correctly and that all domain controllers are included in the replication scope. 

-  Check the replication status: Use the repadmin /replsummary command to check the replication status between domain controllers. Look for any errors or warnings that may indicate replication problems. 

-  Check the event log: Check the event log on the domain controller for any errors or warnings related to replication. 

-  Check network connectivity: Verify that there are no network connectivity issues between domain controllers. You can use tools like ping and Tracert to test connectivity. 

-  Check the firewall settings: Make sure the necessary ports are open on the firewall to allow replication traffic.

Best regards

Qiuyang
