---
title: "Upgrading Exchange Server2016 DAG (Wind SRV2016) to Exchange Server2019 (Wind SRV 2022)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1511651/upgrading-exchange-server2016-dag-wind-srv2016-to
question_id: 1511651
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Upgrading Exchange Server2016 DAG (Wind SRV2016) to Exchange Server2019 (Wind SRV 2022)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1511651/upgrading-exchange-server2016-dag-wind-srv2016-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,
We would like to Upgrade Exchange Server2016 DAG (Wind SRV2016) to Exchange Server2019 (Wind SRV 2022),
Can you please give me some recommendations and advice on this project? and is that possible to do it? and what is the issues I will face it?
Thanks in advanc

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-25*

Hello
Yes, it is possible to upgrade your Exchange Server 2016 DAG (on Windows Server 2016) to Exchange Server 2019 (on Windows Server 2022). Here are some recommendations and potential issues you might face during this process:
 
Recommendations:
 
Planning: Before starting the upgrade, it’s important to plan your migration process carefully. This includes understanding your current environment, determining the order of server upgrades, and planning for coexistence during the migration.
 
Preparation: Ensure that your environment meets the prerequisites for Exchange Server 2019. This includes hardware requirements, software requirements, and Active Directory preparation.
 
Installation: Install Exchange Server 2019 on a new server. You can use the Exchange Deployment Assistant as a guide.
 
Migration: Start the migration process. This typically involves moving mailboxes (or databases) from the old DAG to the new one.
 
Namespace and Load Balancing: Manage namespaces, load balancers, and clients during this transition. You can build a new 2019 DAG, configure it to use the same namespace/URLs, and then add these 2019 nodes to your current load balancers alongside the 2016 servers.
 
Potential Issues:
 
DAGs and Namespaces: One of the questions that often comes up is whether multiple DAGs can share the same namespace and load balancing topology. The answer is “yes”, but you need to carefully manage the transition to ensure minimal disruption.
 
Virtual Directory Settings: You need to go through the 2016 virtual directory settings and mirror them on the 2019 servers. Make sure you have any certificates installed on the 2019 server. You’ll have to update your send connectors to include your 2019 servers as necessary and mirror the 2016 receive connectors and their settings on your 2019 servers.
 
Lack of Resources: There are fewer resources available for migrating from Exchange Server 2016 to 2019 compared to older versions. However, the process is similar to previous migrations.
