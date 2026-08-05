---
title: "Domain controllers can't ping each other"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/944920/domain-controllers-cant-ping-each-other
question_id: 944920
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Domain controllers can't ping each other

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/944920/domain-controllers-cant-ping-each-other (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

Windows Server 2016 standard domain. I have a peculiar issue.     

I have two Windows Server 2016 domain controllers one of them (pdc) is a virtual machine (hyper-v) the other a physical machine. Somehow they have stopped seeing each other and neither can ping each other (request times out).    

Both dcs can be pinged from the host machine of hyper-v pdc. Both dcs can also be pinged from another machine on network. Both dcs can be remote desktoped into from other machines using the machine names of dcs.    

The pdc also has Essential role installed.    

What could be the reason for the two dcs not being able to ping each other?    

The ipconfig/all output for both dcs is below.    

Thanks    

Regards    

```
C:\Users\Administrator>ipconfig/all  
  
Windows IP Configuration  
  
   Host Name . . . . . . . . . . . . : PDC  
   Primary Dns Suffix  . . . . . . . : AD.MYDOMAIN.COM  
   Node Type . . . . . . . . . . . . : Hybrid  
   IP Routing Enabled. . . . . . . . : Yes  
   WINS Proxy Enabled. . . . . . . . : No  
   DNS Suffix Search List. . . . . . : AD.MYDOMAIN.COM  
  
Ethernet adapter Ethernet:  
  
   Connection-specific DNS Suffix  . :  
   Description . . . . . . . . . . . : Microsoft Hyper-V Network Adapter  
   Physical Address. . . . . . . . . : 00-15-5D-01-6A-00  
   DHCP Enabled. . . . . . . . . . . : No  
   Autoconfiguration Enabled . . . . : Yes  
   Link-local IPv6 Address . . . . . : fe80::a515:80b2:1c01:a982%9(Preferred)  
   IPv4 Address. . . . . . . . . . . : 192.168.1.100(Preferred)  
   Subnet Mask . . . . . . . . . . . : 255.255.255.0  
   Default Gateway . . . . . . . . . : 192.168.1.1  
   DHCPv6 IAID . . . . . . . . . . . : 50337117  
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-20-0C-37-F3-00-15-5D-01-6A-00  
   DNS Servers . . . . . . . . . . . : ::1  
                                       192.168.1.100  
                                       127.0.0.1  
   NetBIOS over Tcpip. . . . . . . . : Enabled  
  
PPP adapter RAS (Dial In) Interface:  
  
   Connection-specific DNS Suffix  . :  
   Description . . . . . . . . . . . : RAS (Dial In) Interface  
   Physical Address. . . . . . . . . :  
   DHCP Enabled. . . . . . . . . . . : No  
   Autoconfiguration Enabled . . . . : Yes  
   IPv4 Address. . . . . . . . . . . : 192.168.1.44(Preferred)  
   Subnet Mask . . . . . . . . . . . : 255.255.255.255  
   Default Gateway . . . . . . . . . :  
   NetBIOS over Tcpip. . . . . . . . : Enabled  
  
Tunnel adapter isatap.{BAF5DF81-A0C2-4DB1-B328-0AE37920F083}:  
  
   Media State . . . . . . . . . . . : Media disconnected  
   Connection-specific DNS Suffix  . :  
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter  
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0  
   DHCP Enabled. . . . . . . . . . . : No  
   Autoconfiguration Enabled . . . . : Yes  
  
Tunnel adapter isatap.{6E06F030-7526-11D2-BAF4-00600815A4BD}:  
  
   Media State . . . . . . . . . . . : Media disconnected  
   Connection-specific DNS Suffix  . :  
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter #2  
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0  
   DHCP Enabled. . . . . . . . . . . : No  
   Autoconfiguration Enabled . . . . : Yes  
  
 
  
  
  
C:\WINDOWS\system32>ipconfig/all  
  
Windows IP Configuration  
  
   Host Name . . . . . . . . . . . . : BDC  
   Primary Dns Suffix  . . . . . . . : AD.MYDOMAIN.COM  
   Node Type . . . . . . . . . . . . : Hybrid  
   IP Routing Enabled. . . . . . . . : No  
   WINS Proxy Enabled. . . . . . . . : No  
   DNS Suffix Search List. . . . . . : AD.MYDOMAIN.COM  
  
Ethernet adapter Ethernet:  
  
   Connection-specific DNS Suffix  . :  
   Description . . . . . . . . . . . : QLogic BCM5716C Gigabit Ethernet (NDIS VBD Client) #41  
   Physical Address. . . . . . . . . : D4-AE-52-6D-8F-D3  
   DHCP Enabled. . . . . . . . . . . : No  
   Autoconfiguration Enabled . . . . : Yes  
   IPv4 Address. . . . . . . . . . . : 192.168.1.39(Preferred)  
   Subnet Mask . . . . . . . . . . . : 255.255.255.0  
   Default Gateway . . . . . . . . . : 192.168.1.1  
   DNS Servers . . . . . . . . . . . : 192.168.1.100  
                                       192.168.1.39  
   Primary WINS Server . . . . . . . : 192.168.1.100  
   NetBIOS over Tcpip. . . . . . . . : Enabled  
  
Tunnel adapter isatap.{52C19ACD-7E97-4AD7-BF01-0757FB2E352D}:  
  
   Media State . . . . . . . . . . . : Media disconnected  
   Connection-specific DNS Suffix  . :  
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter  
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0  
   DHCP Enabled. . . . . . . . . . . : No  
   Autoconfiguration Enabled . . . . : Yes  
  
Tunnel adapter Teredo Tunneling Pseudo-Interface:  
  
   Media State . . . . . . . . . . . : Media disconnected  
   Connection-specific DNS Suffix  . :  
   Description . . . . . . . . . . . : Teredo Tunneling Pseudo-Interface  
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0  
   DHCP Enabled. . . . . . . . . . . : No  
   Autoconfiguration Enabled . . . . : Yes
```

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-29*

Hi    

It just started working o its own after a while. Not sure how.    

Thanks    

Regards
