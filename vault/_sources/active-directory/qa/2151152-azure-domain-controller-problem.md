---
title: "Azure / Domain Controller problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2151152/azure-domain-controller-problem
question_id: 2151152
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Azure / Domain Controller problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2151152/azure-domain-controller-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a strange problem and need help   

Case: Domain Controller DC with Windows 2012R Domain Controller DC1 with Windows 2022   

They are both in the same domain.   

When I turn off DC and only use DC1, users who connect via a VPN connection cannot access mapped drives.   

I have checked the VPN software and the configuration points to DC1 as the DNS server   

If I start DC again, users who connect via VPN have no problems and can access mapped drives   

I have tried to look in Azure to see if storage, for example, only responds to DC but I can't see that this is the case   

I need a hint

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-30*

HI Johnny,

You may need to provide more information. Below are some 'hints' you may find useful.

E.g.

What error message or symptoms are you getting when VPN users cannot connect to mapped drives?

Where is your VPN terminating inside your network? Is it terminating at a server inside your network/DMZ/etc. Is it using a gateway device? Is there a firewall or more between the VPN gateway and the network?

Have you looked in the event logs on the VPN client?

My guess is that you have a network related issue between your VPN entry point (gateway) and DC1. E.g. Firewall blocking authentication traffic to DC1. It would be interesting to know if other services are also affected.

I just noticed you referenced Azure. Are DC and DC1 both in Azure? Are you using Azure Point to Site VPN? Have you checked The netowrk config on the Azure VPN Gateway and all related (Network Security Groups (NSGs))? You may have NSGs related to Azure VPN gateway and Subnets and VMs. If I Recall Correctly Azure also has a network troubleshooting tool you could use if your license covers it.

Another option may be to get a network capture during the VPN connect and reproducing the problem and compare to a capture when DC is online. You may see what traffic is leaving the Client but not getting a response that may lead you to where to look next.

HTH
