---
title: "2 Domain Controllers on same Internal Network"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2247153/2-domain-controllers-on-same-internal-network
question_id: 2247153
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# 2 Domain Controllers on same Internal Network

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2247153/2-domain-controllers-on-same-internal-network (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 domain controllers DC1 with the IP address 192.168.10.10 and DC2 with the IP address 192.168.10.9 where DNS is installed on both of them

If I make a correction to the DC1 DNS configuration then I can see this correction on the DC2 DNS

The DHCP server delivers an IP address to the clients including dns servers DC1 and DC2

Everything works perfectly

But If I turn off DC1 due to an update then trouble starts

All clients Outlook loses connection to Mailbox until I restart DC1

This doesn't happen if I turn off DC2

I have tryed following commands:  

To set the StaticDomainControllers:  

Set-ExchangeServer -Identity Mailbox1 -StaticDomainControllers DC2.office.local,DC1.office.local

To set the StaticGlobalCatalogs:  

Set-ExchangeServer -Identity Mailbox1 -StaticGlobalCatalogs DC2.office.local,DC1.office.local

To set the StaticConfigDomainController  

Set-Exchangeserver Mailbox1 -StaticConfigDomainController DC2.office.local,DC1.office.local

Set-Exchangeserver Mailbox1 -StaticDomainControllers DC2.office.local -StaticGlobalCatalogs DC2.office.local -StaticConfigDomainController DC2.office.local

Set-AdServerSettings -ViewEntireForest $true -PreferredGlobalCatalog dc2.office.local

Set-AdServerSettings -ViewEntireForest $true

Set-ADServerSettings -PreferredServer dc2.office.local

When I check Application log on my Mailbox Event ID 2080 I get following result:  

Process Microsoft.Exchange.Directory.TopologyService.exe (PID=5652). Exchange Active Directory Provider has discovered the following servers with the following characteristics:       

In-site:  

DC2.office.local	CDG 1 7 7 1 0 1 1 7 1  

DC1.office.local	CDG 1 7 7 1 0 1 1 7 1       

Out-of-site:

Is it possible to configure On-Premise Exchange 2019 so that it can use both Domain Controllers depending on which one is on ?

A hint would be nice

Best Regards

John B

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-23*

I solved the problem myself by Manually Configuring DNS Lookups for Exchange Server :-)
