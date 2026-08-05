---
title: "Problems with Exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/334699/problems-with-exchange-2013
question_id: 334699
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Problems with Exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/334699/problems-with-exchange-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi folks, I know that, this is an old story, but I have one problematic Exchange Server 2013 SP1.   

This server is pre CU5, and I can not upgrade to CU23. Even if a make restart to this server, I have very big problems, making it to work. As long as it up and running, we can not eve breath on it.   

I can not even start any migration to Exchange 2016/2019, until I have at least CU18. It have around 500 mailboxes and successful backup on mailboxes (with DPM 2016) and probably System state. It can not run Bare metal backup.   

I can not avoid this issue, so I have to do something, so I was thinking about two scenarios:   

Scenario 1:   

-  I think to install new Server 2012 R2 with Exchange 2013 SP1 CU23 (to highest update). To create new Databases and start live migrating mailboxes to new server. I'm not planning to crate DAG.   

-  While I'm migrating the mailboxes, can those two Exchange server communicate which other?   

-  Do I need to create some send/receive connector between them?  

-  What about the mailboxes migrated on the new Exchange, are the users will be able to send and receive mails?   

-  What about Outlooks, are going to be able to automatically find there mailboxes, on second Exchange?   

After migrating all mailboxes, I will redirect mail traffic to second Exchange and dismantle first one.   

Than, after I have working Exchange, I will proceed with upgrade to Exchange 2019.   

Scenario 2:   

-  To install new Server 2012 R2,  

-  To disable network adapter on existing Exchange 2013,  

-  To install Exchange 2013 CU23 in restore/repair mode, on new Server 2012 R2,  

-  To create same disk and partition, as the existing one and restore DB from backup   

-  What if this doesn't work? Can I simply shut down new Exchange and re-enable network adapter on old one?   

-  It will crate a problems to entire Domain infrastructure?   

This will crate unknown downtime...   

Please if any has experience with this kind of situation?   

Best regards,   

Aleksandar

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-30*

Thank you joyceshen-MSFT.
