---
title: "Windows Server 2016 DNS LDAP connectivity issues after windows update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1531475/windows-server-2016-dns-ldap-connectivity-issues-a
question_id: 1531475
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Windows Server 2016 DNS LDAP connectivity issues after windows update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1531475/windows-server-2016-dns-ldap-connectivity-issues-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a small business with a single server acting as domain controller and VPN Server (single network interface).  

DHCP is served by load balancer (multi-WAN router).  

Server has a static ip address.  

Apparently after windows update we have multiple problems (authentication, sshd not able to authenticate with kerberus).  

I believe it has to do with AD or DNS or both or maybe Kerberus itself, which causes problems with DNS and AD.  

If I start DNS Manager as Administrator (built-in), I get Access Denied.  

If I start Active Directory Administrative Center, it closes with "unknown error".  

I can open AD users and Computers, browse them and even change settings for users.

Event Log shows following errors:

SERVER03
1655
Warning
Microsoft-Windows-ActiveDirectory_DomainService
Directory Service
2/13/2024 3:37:36 PM

SERVER03
1655
Warning
Microsoft-Windows-ActiveDirectory_DomainService
Directory Service
2/13/2024 3:37:36 PM

SERVER03
1126
Error
Microsoft-Windows-ActiveDirectory_DomainService
Directory Service
2/13/2024 3:37:36 PM

SERVER03
4000
Error
Microsoft-Windows-DNS-Server-Service
DNS Server
2/13/2024 3:35:34 PM

SERVER03
4007
Error
Microsoft-Windows-DNS-Server-Service
DNS Server
2/13/2024 3:10:08 PM

dcdiag /test:dns gives this error:  

Testing server: Default-First-Site-Name\SERVER03

```
Starting test: Connectivity
     * Active Directory LDAP Services Check
     The host be65bd94-0221-47fb-8e6b-321e0afd30ef._msdcs.future.int could
     not be resolved to an IP address. Check the DNS server, DHCP, server
     name, etc.
```

....

TEST: Basic (Basc)

```
Error: No LDAP connectivity
              Warning: adapter
              [00000017] Realtek Gaming 2.5GbE Family Controller has
              invalid DNS server: 8.8.8.8 ()
              Warning: adapter
              [00000017] Realtek Gaming 2.5GbE Family Controller has
              invalid DNS server: 127.0.0.1 (SERVER03)
              Error: all DNS servers are invalid
              No host records (A or AAAA) were found for this DC
              Warning: no DNS RPC connectivity (error or non Microsoft DNS server is running)
     
     Summary of test results for DNS servers used by the above domain
     controllers:
     
        DNS server: 192.168.0.6 (SERVER03)
           1 test failure on this DNS server
           Name resolution is not functional. _ldap._tcp.future.int. failed on the DNS server 192.168.0.6
           
        DNS server: 8.8.8.8 ()
           1 test failure on this DNS server
           Name resolution is not functional. _ldap._tcp.future.int. failed on the DNS server 8.8.8.8
           
     Summary of DNS test results:
     
                                        Auth Basc Forw Del  Dyn  RReg Ext
        _________________________________________________________________
        Domain: future.int
           SERVER03                     PASS FAIL n/a  n/a  n/a  n/a  n/a  
     
     ......................... future.int failed test DNS
```

Pinging server works: ping server03.future.int /4  

Pinging any of the donaims from the test above fails:  

PS C:\Users\Administrator> ping _ldap._tcp.future.int
Ping request could not find host _ldap._tcp.future.int. Please check the name and try again.
Best Practice Analyzer for DnsServer finds following errors:

-  RAS (Dial In) Interface does not have any DNS servers configured.

-  The interface RAS (Dial In) Interface is not configured to register its addresses in DNS.

-  The DNS server 127.0.0.1 on Ethernet 3 did not successfully resolve the name _ldap._tcp.gc._msdcs.future.int

-  The DNS server 127.0.0.1 on Ethernet 3 did not successfully resolve the name _kerberos._tcp.future.int.

-  The DNS server 127.0.0.1 on Ethernet 3 did not successfully resolve the name _ldap._tcp.future.int.

-  The DNS server 127.0.0.1 on Ethernet 3 did not successfully resolve the name _ldap._tcp.pdc._msdcs.future.int.

-  The DNS server 127.0.0.1 on Ethernet 3 did not successfully resolve the name for the start of authority (SOA) record of the zone hosting the computer's forest root domain name.

-  The DNS server 127.0.0.1 on Ethernet 3 did not successfully resolve the name for the start of authority (SOA) record of the zone hosting the computer's primary DNS domain name.  

I have tried restaring DNS and AD services.  

I have tried rebooting server.  

I have changed the password for krbtgt user as I tried to solve sshd issue.  

I have removed stored user credentials for the server in credential manager
I have added the credential for admin user again.

Any idea what else can I try?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-13*

All problems resolved by reverting Password change for Administrator.  

I have forgotten that we changed user password for our FUTURE\Administrator user.  

This was now try-anything-desperation-move to change the password back to what is was before.  

After that, all of the problem dissapeared.  

How can this be?  

Is there a method to change user password without messing up the entire system?
