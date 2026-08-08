---
title: "The local domain controller could not connect with the following domain controller hosting the following directory partition to resolve distinguished names."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/67434/the-local-domain-controller-could-not-connect-with
question_id: 67434
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# The local domain controller could not connect with the following domain controller hosting the following directory partition to resolve distinguished names.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/67434/the-local-domain-controller-could-not-connect-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to setup a Active Directory and cant seem to find the solution on my own. The network also has a firewall, but I dont think that is the issue since the domain controller and AD are on the same machine.   

The local domain controller could not connect with the following domain controller hosting the following directory partition to resolve distinguished names.   

Domain controller:  

Directory partition:  

redacted.com   

Additional Data   

Error value:  

1355 The specified domain either does not exist or could not be contacted.   

Internal ID:  

3201395  

Windows IP Configuration  

   Host Name . . . . . . . . . . . . : Redacted   

   Primary Dns Suffix  . . . . . . . :  

   Node Type . . . . . . . . . . . . : Hybrid  

   IP Routing Enabled. . . . . . . . : No  

   WINS Proxy Enabled. . . . . . . . : No  

Ethernet adapter Ethernet 2:  

   Connection-specific DNS Suffix  . :  

   Description . . . . . . . . . . . : Intel(R) 82574L Gigabit Network Connection #2  

   Physical Address. . . . . . . . . : D0-50-99-C1-EB-DC  

   DHCP Enabled. . . . . . . . . . . : Yes  

   Autoconfiguration Enabled . . . . : Yes  

   Link-local IPv6 Address . . . . . : fe80::e571:7b1d:c7a9:445c%6(Preferred)  

   IPv4 Address. . . . . . . . . . . : 192.168.168.65(Preferred)  

   Subnet Mask . . . . . . . . . . . : 255.255.255.0  

   Lease Obtained. . . . . . . . . . : Friday, August 14, 2020 12:54:44 PM  

   Lease Expires . . . . . . . . . . : Saturday, August 15, 2020 1:03:01 PM  

   Default Gateway . . . . . . . . . : 192.168.168.168  

   DHCP Server . . . . . . . . . . . : 192.168.168.168  

   DHCPv6 IAID . . . . . . . . . . . : 265310361  

   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-22-94-F3-A7-D0-50-99-C1-EB-DC  

   DNS Servers . . . . . . . . . . . : 127.0.0.1  

   NetBIOS over Tcpip. . . . . . . . : Enabled  

Tunnel adapter isatap.{62CC7E69-5195-4C8B-9BE3-E02D07B12411}:  

   Media State . . . . . . . . . . . : Media disconnected  

   Connection-specific DNS Suffix  . :  

   Description . . . . . . . . . . . : Microsoft ISATAP Adapter  

   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0  

   DHCP Enabled. . . . . . . . . . . : No  

   Autoconfiguration Enabled . . . . : Yes  

Tunnel adapter Teredo Tunneling Pseudo-Interface:  

   Connection-specific DNS Suffix  . :  

   Description . . . . . . . . . . . : Teredo Tunneling Pseudo-Interface  

   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0  

   DHCP Enabled. . . . . . . . . . . : No  

   Autoconfiguration Enabled . . . . : Yes  

   IPv6 Address. . . . . . . . . . . : 2001:0:34f1:8072:c37:e1d1:b8f6:96ac(Preferred)  

   Link-local IPv6 Address . . . . . : fe80::c37:e1d1:b8f6:96ac%7(Preferred)  

   Default Gateway . . . . . . . . . : ::  

   DHCPv6 IAID . . . . . . . . . . . : 520093696  

   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-22-94-F3-A7-D0-50-99-C1-EB-DC  

   NetBIOS over Tcpip. . . . . . . . : Disabled

## Answer (community) — community member

*upvotes: 1 · updated: 2020-08-17*

Let's suppose that your Active Directory Domain Controller (and DNS Server) is a Windows Server 2016 machine and is responsible for the domain "wintips.local" and has the IP Address "192.168.1.10".  

At this example, the IP and the Preferred DNS address on the Primary Domain Controller (Server 2016) must be the same, e.g.  

Primary Domain Controller (Server 2016)  

Computer Name:	Server2k16  

Domain Name:	WINTIPS.LOCAL  

IP Address (Static):	192.168.1.10  

Subnet Mask:	255.255.255.0  

Default Gateway:	192.168.1.1  

Preferred DNS Server:	192.168.1.10  

Method 1. Set the Preferred DNS Server Address to match the Domain Controller's IP Address (on Client Workstation)  

To resolve the "Specified Domain Does Not Exist or Could Not Be Contacted" error, you have to set the Preferred DNS IP to point to Primary Domain Controller's IP address, on each client workstation that you want to join in the domain. To do that:  

-  Open Network and Sharing Center.  

-  Right click on Local Area Connection and click Properties.  

-  Double click on Internet Protocol TCP/IPv4.  

-  Change the Preferred DNS server address to match the Primary Domain Controller's IP Address (e.g. "192.168.1.10" in this example).  

-  Click OK twice and close all windows.  

6 Try to join the workstation in the Domain.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-08-14*

I'd also add the domain controller's own static ip address (192.168.168.168) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-08-14*

Hi,  

To get more details about the DC health on each domain controller you can run the following command `dcdiag`  

```
Dcdiag 
repadmin /showrepl
```

Check also the event viewer on each DC.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-14*

Please run;  

-  Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log  

-  repadmin /showrepl >C:\repl.txt  

-  ipconfig /all > C:\dc1.txt  

-  ipconfig /all > C:\dc2.txt  

-  (etc. as other DC's exist)  

then put unzipped text files up on OneDrive and share a link.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-14*

Added and executed the commands and restarted. I am going to post the current errors I do have from DNS and AD DS.

AD DS Errors: Let me know what I need to Expand.

```
6016    Warning DFSR    DFS Replication 8/14/2020 1:26:46 PM
1844    Warning Microsoft-Windows-ActiveDirectory_DomainService Directory Service   8/14/2020 1:22:00 PM
1202    Error   ADWS    Active Directory Web Services   8/14/2020 1:21:45 PM
1202    Error   DFSR    DFS Replication 8/14/2020 1:21:45 PM
4013    Warning Microsoft-Windows-DNS-Server-Service    DNS Server  8/14/2020 1:21:38 PM
414 Warning Microsoft-Windows-DNS-Server-Service    DNS Server  8/14/2020 1:21:33 PM
1220    Warning Microsoft-Windows-ActiveDirectory_DomainService Directory Service   8/14/2020 1:21:28 PM
3041    Warning Microsoft-Windows-ActiveDirectory_DomainService Directory Service   8/14/2020 1:21:26 PM
2886    Warning Microsoft-Windows-ActiveDirectory_DomainService Directory Service   8/14/2020 1:21:26 PM
1539    Warning Microsoft-Windows-ActiveDirectory_DomainService Directory Service   8/14/2020 1:21:15 PM
```

DNS Errors: Let me know what I need to Expand.

```
414 Warning Microsoft-Windows-DNS-Server-Service    DNS Server  8/14/2020 1:21:33 PM
   4013 Warning Microsoft-Windows-DNS-Server-Service    DNS Server  8/14/2020 1:21:38 PM
```
