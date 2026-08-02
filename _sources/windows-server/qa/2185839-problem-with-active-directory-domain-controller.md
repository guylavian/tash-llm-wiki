---
title: "problem with active directory domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185839/problem-with-active-directory-domain-controller
question_id: 2185839
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# problem with active directory domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185839/problem-with-active-directory-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

No access to domain server

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-10*

Hello Jeff Toben,  

Thank you for your reply.  

So you only have one forest with single domain and single Domain Controller?  

Not sure if "cannot access domain the DC name" issue and "cannot join any pc to the domain" issue is caused by the same reason or not.  

What error message did you receive when you join PC to domain?  

1.You can check if all the ports that AD require are open or not .  

Active Directory and Active Directory Domain Services Port Requirements

https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd772723(v=ws.10)?redirectedfrom=MSDN

Active Directory Replication over Firewalls

https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727063(v=technet.10)?redirectedfrom=MSDN  

Especially, check the ports below.  

Application protocol
Protocol
Ports

Global Catalog Server
TCP
3269

Global Catalog Server
TCP
3268

LDAP Server
TCP
389

LDAP Server
UDP
389

LDAP SSL
TCP
636

RPC
TCP
135

RPC randomly allocated high TCP ports/ DCOM
TCP
1024 – 65535(windows server 2003/R2) <br><br>49152 – 65535(windows server 2008/R2 and later)

SMB
TCP
445

DNS
UDP
53

DNS
TCP
53

Kerberos
TCP
88

Kerberos
UDP
88

Kerberos Password V5
TCP
464

Kerberos Password V5
UDP
464

NTP/SNTP
UDP
123

NetBIOS Datagram Service
UDP
138

NetBIOS Datagram Service
TCP
139

2.Run DCdiag /v on the DC to check if there is any error.  

3.Run net share on DC to check if netlogon and sysvol is shared.  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-09*

Server can not be found but if I use the ip I can get to the server, also I can not join any pc to the domain. We have 1 domain server. We access the domain though mapped drives for years. I can ping the ip. I t seems like a dens problem. I can access domain with the ip but not with the pc name.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-09*

Hello Jeff Toben,  

Thank you for posting in Microsoft Community forum.  

1.What error message did you receive when "No access to domain server"?  

2.How many Domain Controllers are there in your domain?  

3.How did you access to domain server?  

4.Can you ping the domain name or IP of Domain Controller or FQDN of Domain Controller from your current machine?  

For example:  

ping domain.com (domain.com is your domain name)

ping 1.1.1.1(the IP is IP address of Domain Controller)  

ping DCname.domain.com (FQDN of Domain Controller)  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-06*

Since when this problem started?

Are you facing this issue with all endpoints?

Are you able to ping the Domain Controller?

Have you check log files?

Open command prompt as administrator and run the following command:

nltest /sc_reset:<domainname>

<domainname> is name of your domain.
