---
title: "SYSVOL Replication is not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194427/sysvol-replication-is-not-working
question_id: 2194427
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# SYSVOL Replication is not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194427/sysvol-replication-is-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have promoted new 2022 Domain Controllers on top of our current 2012 DCs wherein using a DFSR replication unfortunately we are unaware that SYSVOL replication is not taking place/working (so newly created or modified GPO is not replicating to other 2012 DC but created/modified AD objects are replicating properly... so when we promoted 2 new 2022 DCs, SYSVOL and NETLOGON are missing or not shared on 2022 DCs so technically 2012 DC SYSVOL is not replicating to both 2012 and 2022 DCs but AD object are replicating fine... Please advice on how to fix? do we need to enable DFS replication manually via enabling DFS management feature? or any fix we can apply?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-18*

Hi Xtrimcore,

Thank you for posting in the Microsoft Community Forums.

What are the details of the new 2022 domain controller that you said was promoted on top of the current 2012 domain controller? Is it a new 2022 domain controller added to the domain where the 2012 domain controller is located, or is it a 2022 server promoted to a domain controller after updating the 2012 server to a 2022 server? 

Did you perform a check on replication? Are there any errors reported in the event viewer? 

I will provide you with a reference to help you troubleshoot the error and resolve the issue. 

Troubleshoot missing SYSVOL and Netlogon shares for Distributed File System (DFS) Replication - Windows Server | Microsoft Learn

Best regards

Neuvi Jiang
