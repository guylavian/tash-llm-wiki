---
title: "Exchange Server 2019 HA & DR Design | Need assistance in good planning"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2127320/exchange-server-2019-ha-dr-design-need-assistance
question_id: 2127320
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Server 2019 HA & DR Design | Need assistance in good planning

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2127320/exchange-server-2019-ha-dr-design-need-assistance (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,

I have been asked to setup a HA & DR of Exchange Server 2019 (In-House) with only Internal Clients connecting to it. There will be no Internet or external access. There are 2 Sites, A & B connected by Dark Fibre of 10G and though users are around 3000 but their usage is very minimum as it is only for internal purposes. They are keen to have HA & DR and in current setup I had setup HA with 3 servers.

I was reading about cross-site DAG and need little assistance in setting up the same. I need to design HA & DR so that if there is a site failure then automatically the DR should continue the work.

I thought Active-Active would be best because if anyone of the site fails, say Site A fails, the 40-50% of the users who would have their mailboxes on them would move to Site B.

-  Is it best to setup Active-Active or Active-Passive, benefits, safety, Administrator's Tasks in failover scenario?

-  Is it better to keep even nodes on each side with Witness Server (for Site A - Witness Server will be on B) & Alternate Witness Server?

-  I'm planning to keep a single URL as it does not matter where the user is, they mainly connect to their mailbox using web interface (owa) and some users use outlook.

-  Management's main idea is, if one site goes down the users should still be able to open their mailboxes.

If anyone has a sample design document with key configuration to keep in mind, if you can share it, please let me know,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-12-20*

Hi @Najeebulla Khan,

-  Active-Active DAG is recommended for true HA & DR, as it offers the best fault tolerance and failover capability.

-  Ensure the File Share Witness is in a third site to guarantee automatic failover and quorum.

-  Distribute your DAG nodes evenly across your sites, making sure they are equally capable of handling workloads.

-  Use DNS load balancing and a single URL for mailbox access to simplify user experience and management.

-  Treat all data centers as equal, ensuring HA is tested daily, and backup and restore strategies are in place.

This approach will ensure your Exchange Server 2019 setup is highly available, resilient, and able to recover quickly from site failures.

Even with a robust DAG in place, ensure you have a reliable backup strategy. Regular backups of Exchange Databases ensure that your data is protected and recoverable. Periodically test your Exchange server recovery plan to ensure that you can recover mailboxes and data quickly in case of any disaster.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-12-09*

If you want HA, then you need a 3rd Data Center and you put the File Share Witness there. Thats the only way to achieve automatic failover. Forget the primary and secondary witness stuff. Have one File Share Witness in the 3rd data center, its the ONLY way you can have true HA.

I would get DR idea out of your mind, instead treat all the servers and all the data centers as equal and any server can be the active server in any data center at any one time. That way you don't have to worry about testing DR, you test it everyday.

Follow the preferred architecture if possible:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/preferred-architecture-2019?view=exchserver-2019

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-09*

Hi @Najeebulla Khan，

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, you want to know about the HA & DR design of Exchange Server 2019, you can refer to the following suggestions:

-  Regarding the failover scenario, Active-Active or Active-Passive is better. Active-Active means that all nodes are active at the same time, which has the advantages of high scalability, parallel processing, and fault tolerance, while Active-Passive is simpler and has lower costs. If you want better failover, it is recommended that you use Active-Active, so that if one node fails, other nodes can take over the workload to avoid service interruption.

-  It is recommended that you keep the nodes evenly distributed across sites, because evenly distributed nodes can better balance the load and restore services faster when a failure occurs.

-  You can use a single URL to simplify access and system management, so that you can access the mailbox no matter which site you connect to.

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

Best,

Jeanne
