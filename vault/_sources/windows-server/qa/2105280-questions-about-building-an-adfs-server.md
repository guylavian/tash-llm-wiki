---
title: "Questions about building an ADFS server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2105280/questions-about-building-an-adfs-server
question_id: 2105280
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Questions about building an ADFS server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2105280/questions-about-building-an-adfs-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We need Wbexso for our in-house videoconferencing system, so we need to build an ADFS server. 

Can you tell me how much resources I need from the entire server when building ADFS servers? 

The number of employees in the company is approximately 1.5 million, and I think you will need an account up to twice as much as we need.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-18*

Hello

Thank you for posting in Q&A forum

Building an Active Directory Federation Services (ADFS) server for a company with around 1.5 million employees is quite an undertaking! Here are some general resource requirements you'll need to consider:

Hardware Requirements:

Processor Speed: At least 133 MHz for x86-based computers, but for a company of this size, you'll want much more powerful processors (e.g., multi-core CPUs).

RAM: Minimum of 256 MB for setup, but realistically, you'll need significantly more. For a company of this scale, several gigabytes of RAM per server would be more appropriate.

Disk Space: At least 10 GB for setup, but you'll need much more for logs, databases, and other operational needs. Multiple terabytes of storage would be advisable.

Network: High-speed, reliable network connections to handle the load.

Software Requirements:

Windows Server: Windows Server 2012 R2 or later.

Certificates: Publicly trusted SSL/TLS certificates for securing communications.

Database: A SQL Server for the configuration database, or Windows Internal Database (WID) for smaller setups, but SQL Server is recommended for larger environments.

Additional Considerations:

Load Balancing: You'll need load balancers to distribute the traffic among multiple ADFS servers to ensure high availability and performance.

Redundancy: Multiple ADFS servers in different data centers to provide failover capabilities.

Monitoring and Maintenance: Tools and processes to monitor the health of the servers and perform regular maintenance.

Best regards

Yanhong

=====================================

If the answer is helpful, please click "Accept answer" and upvote it
