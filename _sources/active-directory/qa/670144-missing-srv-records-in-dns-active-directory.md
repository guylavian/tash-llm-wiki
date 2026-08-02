---
title: "Missing SRV Records in DNS Active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/670144/missing-srv-records-in-dns-active-directory
question_id: 670144
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Missing SRV Records in DNS Active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/670144/missing-srv-records-in-dns-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to install exchange server 2016 in my environment.     

I have two domain controllers, AD1 and AD2. My domain is: contoso.com    

When i run `dcdiag /s:AD1 /test:dns` from the server that i want to install the exchange, i get an error below:    

`    

               TEST: Delegations (Del)  

                  Error: DNS server: ad1.contoso. IP:192.16.11.15 [Broken delegated domain contoso.com.contoso.com.]  

                  Error: DNS server: ad2.contoso. IP:192.16.11.12 [Broken delegated domain contoso.com.contoso.com.]  

```
TEST: Records registration (RReg)  
              Network Adapter [00000009] Intel(R) 82574L Gigabit Network Connection:  
                 Warning:  
                 Missing SRV record at DNS server 192.16.11.15:  
                 _ldap._tcp.contoso.com  

                 Warning:  
                 Missing SRV record at DNS server 192.16.11.15:  
                 _ldap._tcp.707686c3-aaf8-4ddf-9c65-0d43875614bc.domains._msdcs.contoso.com  

                 Warning:  
                 Missing SRV record at DNS server 192.16.11.15:  
                 _kerberos._contoso.com
```

`    

The error list is long, i just took a section of it,.    

There is no third-party anti-virus installed in the server, all tcp/udp ports 53, 389 etc btwn the server and both AD is open. The server is running `win server 2012 r2`    

I'm able to ping the AD from the server and vice versa.    

Both forest and domain functional level is `win server 2012 r2`    

The setup wizard is returning the following error:    

`    

Error:    

Setup encountered a problem while validating the state of Active Directory: Active Directory server  is not available. Error message: Active directory response: The LDAP server is unavailable.  See the Exchange setup log for more information on this error.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.AdInitErrorRule.aspx    

Error:    

This computer requires the Microsoft Unified Communications Managed API 4.0, Core Runtime 64-bit. Please install the software from http://go.microsoft.com/fwlink/?LinkId=260990.    

For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/readiness-checks?view=exchserver-2016    

Error:    

Either Active Directory doesn't exist, or it can't be contacted.    

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.CannotAccessAD.aspx    

`    

How can i resolve this issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-22*

Hello @Benard Mwanza       

It is highly possible that for a misconfiguration you have embedded a zone inside your zone.     

I would recommend to check in your DNS Forward Zone, inside the folders, if there is not the same Zone with a static IP DNS.     

For example, in one of my experiences, when I accessed the DNS management console, opened the Forward Zone and then the COM folder, I have found that some administrator had created the SAME domain there. I have no idea why, but this way all systems appeared with a double domain zone like contoso.com.contoso.com, instead just contoso.com.     

Hope this helps with your query,    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-12-21*

Hi @Benard Mwanza       

Do you have multiple AD sites in your organization?    

If yes, please either make sure the Schema master is in the same site as the Exchange server and rerun install, or manually prepare Schema/AD/Organization with another device in the same site as the Schema master.    

And it also seems you have some prerequisites (Unified Communications Managed API 4.0) not installed on the Exchange server.    

To get more detailed information, please download and run this script on the Exchange server to check the results: SetupAssist.ps1    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-20*

Some general info  

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/the-case-of-the-missing-srv-records/ba-p/255650  

If problems persist, then please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.
