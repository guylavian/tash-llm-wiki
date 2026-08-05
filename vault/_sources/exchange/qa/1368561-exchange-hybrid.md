---
title: "exchange hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1368561/exchange-hybrid
question_id: 1368561
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# exchange hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1368561/exchange-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi team, im looking to setup exchange hybrid deployment, my question is that my exchange server currently is not exposed to the internet. i dont have public ips users only use it internally or through vpn.

my virtual directories are not published externally (owa, ews, autodiscover..)

can i acheive exchange hybrid configuration wizard if the above is my scenario by just opening needed ports? or no its mandatory to have a public IP and to have my virtual directories at least ews, autodisciver published on it?

thank u

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-14*

To set up an Exchange Hybrid deployment, you can achieve it without exposing your Exchange server to the internet or having public IP addresses. In your scenario, where users only access Exchange internally or through VPN, you can follow these steps:

Prepare Your Environment: Ensure that your on-premises Exchange server is up-to-date and meets the prerequisites for Exchange Hybrid deployment. This includes having the required service packs and cumulative updates installed.

Connectivity: You should have a reliable VPN connection for your users to access the on-premises Exchange server. This ensures secure communication without exposing your Exchange server to the public internet.

Virtual Directory Configuration: While it's common to publish virtual directories like OWA, EWS, and Autodiscover externally for Hybrid deployments, it's not mandatory if you are only serving internal or VPN-connected users. However, you should configure these virtual directories correctly for internal access.

Hybrid Configuration Wizard (HCW): You can run the Exchange Hybrid Configuration Wizard (HCW) from your on-premises Exchange server. The wizard will guide you through the necessary steps to configure hybrid connectivity with your Office 365 tenant.

Firewall and Port Configuration: Ensure that the required ports for Exchange (like HTTPS) are open on your firewall to allow communication between your on-premises Exchange server and Office 365. You'll need to establish outbound connections to Microsoft 365 services.

Public DNS: While you don't need public IP addresses, you will need to configure your public DNS records correctly for your domain to route email traffic to the Office 365 tenant.

In summary, you can set up an Exchange Hybrid deployment without exposing your Exchange server to the public internet. A VPN connection and proper internal configurations can suffice for secure communication. However, ensure that the required ports are open and DNS records are correctly configured for hybrid connectivity.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-14*

You would need a public IP, otherwise mailflow and OAuth between on-prem and EXo wont work. 

https://learn.microsoft.com/en-us/exchange/hybrid-deployment-prerequisites
