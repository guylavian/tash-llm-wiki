---
title: "Exchange DAG Setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2265195/exchange-dag-setup
question_id: 2265195
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange DAG Setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2265195/exchange-dag-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am using an Exchange 2016 hybrid environment and currently building an Exchange 2019 infrastructure in order to decommission my Exchange 2016 servers. As part of this, I want to create a Database Availability Group (DAG). Before creating the DAG, I’ve set up a File Share Witness (FSW).

I have provisioned a VM in Azure to serve as the file share witness—let’s call it exchfs01. On the C: drive, I created a folder named Witness, and within that, a subfolder named after the DAG (i.e., `C:\Witness\exchdag`). I shared the exchdag folder and granted Exchange Trusted Subsystem full access both in the sharing and security permissions. I also added Exchange Trusted Subsystem to the local administrators group on the VM.

From the Exchange Admin Center (EAC), I created the DAG with the following configuration:

DAG Name: exchdag

Witness Server: exchfs01.mydomain.com

Witness Directory: C:\Witness\exchdag

DAG IP Address: A static IP address that is not in use elsewhere

I have two Exchange 2019 servers, and I was able to successfully add both to the DAG. However, I’m facing the following issues:

On the Exchange servers, in Failover Cluster Manager, I’m unable to connect to the DAG or see the Exchange nodes.

-  How can I verify that my DAG is healthy?

-  Am I missing any configuration or steps?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-05-12*

You dont connect to the Cluster via that, Exchange just leverages cluster bits.

To verify DAG health:

https://learn.microsoft.com/en-us/exchange/high-availability/manage-ha/monitor-dags
