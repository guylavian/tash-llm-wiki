---
title: "Event 5774 on a domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/77443/event-5774-on-a-domain-controller
question_id: 77443
fetched: 2026-07-25
answer_count: 13
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Event 5774 on a domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/77443/event-5774-on-a-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

A couple of days ago I was puzzled by the following event in my domain controller's System log:  

```
The dynamic registration of the DNS record 'gc._msdcs.mydomain.com. 600 IN A 10.1.1.2' failed on the following DNS server:  

**DNS server IP address: 81.211.90.x**
Returned Response Code (RCODE): 5 
Returned Status Code: 9017  

For computers and users to locate this domain controller, this record must be registered in DNS.  

USER ACTION  
Determine what might have caused this failure, resolve the problem, and initiate registration of the DNS records by the domain controller. To determine what might have caused this failure, run DCDiag.exe. To learn more about DCDiag.exe, see Help and Support Center. To initiate registration of the DNS records by this domain  controller, run 'nltest.exe /dsregdns' from the command prompt on the domain controller or restart Net Logon service. 
  Or, you can manually add this record to DNS, but it is not recommended.  

ADDITIONAL DATA 
Error Value: DNS bad key.
```

As far as I understand it my own domain controller (10.1.1.2) tried to register its srv record on some host on the internet (81.211.90.x**) - I just can't imagine what could have caused the domain controller (which is the FSMO holder itself!) to act as a dns client for some other DNS server???  

Thank you in advance,  

Michael

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-08-26*

I'd check domain controller should has own static ip address plus loopback listed for DNS and no others such as router or public DNS  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-27*

Hello Michael,  

Thank you so much for posting here.  

Have you checked the provided information? Hope they will be helpful to you.  

Here are some discussions about this issue. We could kindly have a check whether it helps.   

https://social.technet.microsoft.com/Forums/windowsserver/en-US/0507f7cc-c426-439b-a0c6-d36cda2dfee8/event-5774-netlogon?forum=winserverNIS  

Thanks again.  

Best regards,  

Hannah Xiong

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-08-26*

Hi,  

It seems a wrong DNS record mapped on external IP.  

Did you enable scavenging and only secure DNS update ?  

Don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-26*

Please run;  

-  Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log  

-  repadmin /showrepl >C:\repl.txt  

-  ipconfig /all > C:\dc1.txt  

-  ipconfig /all > C:\dc2.txt  

-  (etc. as other DC's exist)  

then put unzipped text files up on OneDrive and share a link.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-26*

Of course it's set only to its own ip!
