---
title: "How to connect on prem exchange to azure exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1046028/how-to-connect-on-prem-exchange-to-azure-exchange
question_id: 1046028
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-vpn-gateway", "office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to connect on prem exchange to azure exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1046028/how-to-connect-on-prem-exchange-to-azure-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I need some information about site to site VPN. I want to deploy two domain controllers and two exchange mailbox servers. I want to deploy one domain controller and one exchange server in my on premise hyper-v and another domain controller and exchange server in my azure. How can I configure it and how to I setup it. Also I want to know how to do I setup site to site vpn connection? Thanks in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-14*

Hello    

Thank you for your question and reaching out. I can understand you are  having  query  related to connect on prem exchange to azure exchange    

Azure VPN gateways provide cross-premises connectivity between customer premises and Azure.    

Prerequisites    

An Azure account with an active subscription. If you don't have one, create one for free.    

Make sure you have a compatible VPN device and someone who is able to configure it. For more information about compatible VPN devices and device configuration, see About VPN Devices.    

Verify that you have an externally facing public IPv4 address for your VPN device.    

If you're unfamiliar with the IP address ranges located in your on-premises network configuration, you need to coordinate with someone who can provide those details for you. When you create this configuration, you must specify the IP address range prefixes that Azure will route to your on-premises location. None of the subnets of your on-premises network can over lap with the virtual network subnets that you want to connect to.    

Below are some Reference article which should help you further.    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/connect-an-on-premises-network-to-a-microsoft-azure-virtual-network?view=o365-worldwide    

https://learn.microsoft.com/en-us/answers/questions/134975/how-to-join-to-on-premise-ad-dc.html    

------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-13*

You can follow:    

https://learn.microsoft.com/en-us/azure/vpn-gateway/tutorial-site-to-site-portal    

https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-create-site-to-site-rm-powershell
