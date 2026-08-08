---
title: "Exchange upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2260715/exchange-upgrade
question_id: 2260715
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2260715/exchange-upgrade (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am currently using an Exchange 2016 hybrid environment. We create users on-premises and then migrate them to Exchange Online. My Exchange 2016 servers are installed on Windows Server 2016, and I have three nodes in a Database Availability Group (DAG): Node1, Node2, and Node3.

I would like to upgrade to Exchange Server 2019 on Windows Server 2022 or 2025 and move to the subscription model. Since Microsoft does not support in-place upgrades from Exchange 2016 to Exchange 2019, I have reviewed the documentation and come up with the following plan. However, I still have some questions and would appreciate clarification and corrections where needed as i have never upgraded exchange earlier.

My Upgrade Plan:

1.Set up a new Windows Server 2022 or 2025 infrastructure with three nodes (Node4, Node5, Node6) and ensure the latest .NET Framework is installed.

-  Perform the Active Directory schema update.

-  Install Exchange Server 2019 with the latest Cumulative Update (CU).

-  Implement antivirus exclusions.

-  Move the arbitration mailboxes and update the URLs to point to the new servers. Question: Do "URLs" refer to the Exchange virtual directories, and is there a way to export them from Exchange 2016 and import into Exchange 2019?

-  Update provisioning scripts. Question: Does this refer to send/receive connectors, and is there a way to export them from Exchange 2016 and import into Exchange 2019?

-  Run the Hybrid Configuration Wizard (HCW) to configure the new Exchange servers.

-  Uninstall Exchange 2016.

My three Exchange 2016 servers are currently part of a Failover Cluster Manager setup using a fail share  witness. Question: At what stage should I add the new Exchange 2019 servers to the Failover Cluster Manager?

## Answers

_No answers on this thread._
