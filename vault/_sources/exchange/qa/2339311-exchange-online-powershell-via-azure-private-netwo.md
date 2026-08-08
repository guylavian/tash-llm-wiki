---
title: "Exchange online PowerShell via Azure Private Network"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2339311/exchange-online-powershell-via-azure-private-netwo
question_id: 2339311
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange online PowerShell via Azure Private Network

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2339311/exchange-online-powershell-via-azure-private-netwo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello community,

We are currently working on enabling secure connectivity from an Azure virtual network (VNet) to Exchange Online using PowerShell, specifically the `Connect-ExchangeOnline` cmdlet. Our environment is locked down using Azure Private Endpoints and NSGs, and we need to whitelist the necessary hostnames or IPs to allow this command to execute successfully.

Scenario:

-  The PowerShell script is running from a Logic Apps in an Azure VNet.

-  Internet access is restricted; only specific hostnames/IPs are allowed via Azure Firewall rules.

-  We are using Azure Private DNS zones and Private Endpoints for other services.

-  We want to connect to Exchange Online via PowerShell using `Connect-ExchangeOnline`.

Request: Could someone please help identify:

-  The FQDNs or hostnames that need to be whitelisted to allow `Connect-ExchangeOnline` to work from a restricted Azure VNet?

Any guidance or references to official documentation would be greatly appreciated!

Thanks in advance.Hello community,

We are currently working on enabling secure connectivity from an Azure virtual network (VNet) to Exchange Online using PowerShell, specifically the `Connect-ExchangeOnline` cmdlet. Our environment is locked down using Azure Private Endpoints and NSGs, and we need to whitelist the necessary hostnames or IPs to allow this command to execute successfully.

Scenario:

-  The PowerShell script is running from a Logic Apps in an Azure VNet.

-  Internet access is restricted; only specific hostnames/IPs are allowed via Azure Firewall rules.

-  We are using Azure Private DNS zones and Private Endpoints for other services.

-  We want to connect to Exchange Online via PowerShell using `Connect-ExchangeOnline`.

Request: Could someone please help identify:

-  The FQDNs or hostnames that need to be whitelisted to allow `Connect-ExchangeOnline` to work from a restricted Azure VNet?

Any guidance or references to official documentation would be greatly appreciated!

Thanks in advance.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-07-07*

The endpoint you should allow is outlook.office365.com, assuming you are connecting to the "global" instance. Ports 80/443. Make sure to also handle authentication requests and certificate checks. That's all covered in the standard network guidance: https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide
