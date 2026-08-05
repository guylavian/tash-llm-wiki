---
title: "Best Practice DNS settings for a domain controller (VM) in Azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1504914/best-practice-dns-settings-for-a-domain-controller
question_id: 1504914
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-dns", "azure-virtual-network", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Best Practice DNS settings for a domain controller (VM) in Azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1504914/best-practice-dns-settings-for-a-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have extended our on-prem services to Azure, and we have multiple Azure VMs (2022 domain controllers) in different regions. (no networking issues at all)
Just wanted to know the best practices when it comes to DNS settings: 

1- Which option on the Azure side would be the best-> the "Inherit from Vnet" or "Custome DNS Servers" option? (NIC settings, the Azure side)

2- Should we leave the DNS settings as "Obtain DNS Server automatically" or we should enter the preferred DNS server addresses? (On the NIC, inside the Azure VM-2022 Server).

3- DNS forwarders-> is using 168.63.129.16 necessary? (if we are NOT planning to use private DNS features).

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-04*

Hey Sam,

1- Which option on the Azure side would be the best-> the "Inherit from Vnet" or "Custome DNS Servers" option? (NIC settings, the Azure side)

  Use the vNets custom DNS and enter in the DC/DNS servers in/closest to your vNet.

2- Should we leave the DNS settings as "Obtain DNS Server automatically" or we should enter the preferred DNS server addresses? (On the NIC, inside the Azure VM-2022 Server).

 Each DC/DNS server should still use 127.0.0.1 as its first entry once setup is complete.

3- DNS forwarders-> is using 168.63.129.16 necessary? (if we are NOT planning to use private DNS features).

 Set 168.63.129.16 as forwarder for each DNS server.
