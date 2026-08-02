---
title: "Active Directory connection error Windows Server 2012 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2700121/active-directory-connection-error-windows-server-2
question_id: 2700121
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 6
qa_tags: []
---
# Active Directory connection error Windows Server 2012 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2700121/active-directory-connection-error-windows-server-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

This is my issue, I have two servers both running Windows Server 2012 R2 Datacenter I have setup AD-DS on one of them and let the setup configure the DNS settings, this server also has a DHCP server. On the server I want to connect to AD I have the DNS address
 pointing at my AD server which is 192.168.1.60 and it is also getting an IP address from the DHCP server. But it wont connect to Active Directory, when I try to ping the domain name which is yewman.email it tries pings an external IP (which is my public ip
 because I also have the actual domain yewman.email) how do I fix this?? This is the AD connection error:

Note: This information is intended for a network administrator.  If you are not your network's administrator, notify the administrator that you received this information, which has been recorded in the file C:\Windows\debug\dcdiag.txt.  

The following error occurred when DNS was queried for the service location (SRV) resource record used to locate an Active Directory Domain Controller (AD DC) for domain "yewman.email":  

The error was: "DNS name does not exist."  

(error code 0x0000232B RCODE_NAME_ERROR)  

The query was for the SRV record for _ldap._tcp.dc._msdcs.yewman.email  

Common causes of this error include the following:  

-  The DNS SRV records required to locate a AD DC for the domain are not registered in DNS. These records are registered with a DNS server automatically when a AD DC is added to a domain. They are updated by the AD DC at set intervals. This computer is configured
 to use DNS servers with the following IP addresses:  

192.168.1.60  

-  One or more of the following zones do not include delegation to its child zone:  

yewman.email  

email  

. (the root zone)

## Answers

_No answers on this thread._
