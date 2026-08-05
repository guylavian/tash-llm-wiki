---
title: "Problems with Domain Controller authentication over VPN"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1085225/problems-with-domain-controller-authentication-ove
question_id: 1085225
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Problems with Domain Controller authentication over VPN

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1085225/problems-with-domain-controller-authentication-ove (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'm trying to configure an SSTP VPN access to our office network.     

The network consists of:    

-  MikroTik Router (gateway, VPN tunnel)    

-  Windows Server 2019 Essentials (Domain Controller, DNS, File Server, SQL Server and several other roles) - yes, we only have 1 server, as we only have 3 employees    

I managed to get to a point where I can get access to the network, I can ping everything (hostname of the server as well) and I can even access the server via Remote Desktop using Admin credentials.    

However, I have problems with accessing various services of the server. Namely:    

-  Shared Files - When I click on a shared disk, I get this error: "The system cannot contact a domain controller to service the authentication request. Please try again later."    

-  Trying gpupdate /force via cmd: User Policy could not be updated successfully. The following errors were encountered: The processing of Group Policy failed. Windows attempted to read the file \company.com\SysVol\company.com\Policies{CFABC23E-DD6D-4314-A616-A900B203B7E8}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following:    

a) Name Resolution/Network Connectivity to the current domain controller.    

b) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller).    

c) The Distributed File System (DFS) client has been disabled.    

-  Trying to access a front end application connected to SQL Server: Connection failed: SQL State S1000. SQL Server Error: -2146892976. [Microsoft][ODBC Driver 17 for SQL Server]MAX_PROVS: The system cannot contact a domain controller to service the authentication request. Please try again later    

It is driving me nuts. I can browse through my files and looking at SQL Server via Remote Desktop, but at the same time, I can't access the resources directly from my client PC over the VPN.    

To state the obvious - everything works perfectly when I'm inside the LAN.    

I would greatly appreciate any tips as why this might be happening.    

Thanks a lot in advance.    

Tomas

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-11*

A VPN connection is a point-to point connection which emulates a single wire connection so the gateway doesn't really matter. Might also check the ports are flowing between networks.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts#windows-server-2008-and-later-versions    

https://www.microsoft.com/en-us/download/details.aspx?id=24009    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-11*

Might check that Use default gateway on remote network option is checked on VPN connection. Also check the connection uses the 2019 Essentials address listed for DNS.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
