---
title: "Domain controller IP Address has intermittent connection issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/156286/domain-controller-ip-address-has-intermittent-conn
question_id: 156286
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Domain controller IP Address has intermittent connection issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/156286/domain-controller-ip-address-has-intermittent-conn (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This domain controller has been running for three years. It is a standalone Windows Sever 2012R2. It is used for Active directory and file and print sharing.

It has been dropping packets for a couple of days. At first we felt it was the issue with the ISP, had them put new lines from the pole. Stopped for about 8 hours and started again. We tried several other diagnose and thought it was the ethernet card. The system has two ethernet cards.

-    Card 1 IP Address 192.168.1.2 -- Static Ping losing packets.

-    Card 2 No IP Address and disabled

-    Configured Card 2-- IP Address 192.168.1.3 and disabled Card 1

-    Connected the cable to it. The system stayed up and running for 24 hours.

-    Static Ping no loss of packets

-    Issue is the DNS server is on IP Address 192.168.1.2.

-    Tried to change the IP Addresses making Card 2-- 192.168.16.2 and it started dropping packet again.

-    Note: Each time I have disabled the card not being used.

-    Configure the original Card 1 IP Address 192.168.16.3 and put the ethernet cable back into it.

-    Have been receiving a static ping internally and externally without error.

-    Enable Card 2 --IP address 192.168.1.2 have no network wire in it

-    Issue I need the DNS so the server can see the workstations.

I have a couple of questions:

```
Is there away to forward 192.168.1.3?
Can I move the DNS to 192.168.1.3 on the domain controller? 
The only change on this network was an external IP Address change!
```

This is an emergency management system and I must keep it up and running. Can you point me in the right direction to get help. Your help is greatly appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-10*

I want to thank you for your help.  The issue was the router needed the firmware updated.   You helped me confirm this.  The server has been up and running all night without loosing the internet intermittently.   When I remove the public DNS Address from the network card I do loose my ability to connect to the server.  I need to go through a workstation and do remote desktop.    

Thank you again.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-09*

Police01 remove the public DNS (75.75.75.75) from connection properties, then do ipconfig /flushdns, ipconfig /registerdns, then restart the netlogon service. If problems persist then put up a new set of files to look at.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-09*

https://1drv.ms/u/s!Agucruy6CbKnj1KNfkUdUTqmQqnn?e=9u4jMs

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-09*

Multi-homing a domain controller will always cause no end to grief for active directory domain DNS. I'd disable the second NIC, then do ipconfig /flushdns, ipconfigregisterdns, restart the netlogon service.  

--please don't forget to Accept as answer if the reply is helpful--
