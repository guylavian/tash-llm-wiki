---
title: "Active Directory custom application partition replication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185376/active-directory-custom-application-partition-repl
question_id: 2185376
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active Directory custom application partition replication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185376/active-directory-custom-application-partition-repl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

According to article: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/create-apply-custom-application-directory-partition I have created custom application partition, by default it is not replicated to any domain controller. Is there any way to mark it as "Enlisted Auto Domain" to start replication with all DCs? I would like to avoid to run multiple commands to add other DC to store directory partition replica (also in the future when I promote new ones)

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-02*

Hi WojtekW_MCS,

Thank you for posting in the Microsoft Community Forums.

Performance and Replication Needs: Ensure that replicating custom application partitions to all domain controllers is compatible with your replication needs and performance requirements. This may not be best practice for large data sets that change frequently.

Network bandwidth: Replicating data consumes network bandwidth, especially in large domains. Evaluate the impact this may have on your network environment.

Security: Ensure that all domain controllers are compliant with your security policy and that communication between them is encrypted and secure.

While it is not possible to directly mark a custom application partition as an “Enlisted Auto Domain”, you can automate the process of joining each domain controller to replication by writing a script. This ensures that when new domain controllers are added in the future, the replication configuration is updated accordingly.

Best regards

Neuvi
