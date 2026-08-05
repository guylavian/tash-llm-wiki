---
title: "Uninstall Exchange on premise completely"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1022817/uninstall-exchange-on-premise-completely
question_id: 1022817
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Uninstall Exchange on premise completely

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1022817/uninstall-exchange-on-premise-completely (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

Previously my company used Exchange 2013 on premise (3 servers , 1 DAG)    

We recently migrated to Microsoft 365, the migration completed successfully , all of our mailboxes have been in the cloud.    

We removed 2 of 3 servers , DAG , mailbox databases ... keep only 1 server (stand alone) , 1 mailbox database.    

My question : Can we remove last Exchange server ? I'm worried it might delete Exchange attributes such as authOrig dLMemRejectPerms dLMemSubmitPerms msExchRequireAuthToSendTo etc

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-26*

I have read decommission-on-premises-exchange    

My case is scenario two , so I guess the answer is : No, I have to keep at least 1 exchange server on premise ?
