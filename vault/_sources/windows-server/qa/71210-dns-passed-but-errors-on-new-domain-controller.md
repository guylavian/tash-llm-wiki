---
title: "DNS Passed But Errors on New Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/71210/dns-passed-but-errors-on-new-domain-controller
question_id: 71210
fetched: 2026-07-25
answer_count: 40
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# DNS Passed But Errors on New Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/71210/dns-passed-but-errors-on-new-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I had an old domain controller, that had been original for the domain, fail without opportunity for proper demotion. I cleaned up AD/DNS/etc... on remaining DC which is running Win Server 2008R2. Migrated DC/Domain to 2008R2 level and then promoted a new Win Server 2019 box as a second DC. Had to then resolve some DNS issues, but appear to have that sorted now and both DCs show proper info in DNS.  

My question is, when I run dcdiag /test:dns it comes back quick and short and pass on the original DC, but although passed on new DC, have a lot of extra entries that appear to be external queries that stated failed. Again, overall says passed DNS test, but wonder what the extra is..?

Directory Server Diagnosis

Performing initial setup:  

Trying to find home server...  

Home Server = DCAPCLD  

* Identified AD Forest.  

Done gathering initial info.

Doing initial required tests

Testing server: Default-First-Site-Name\DCAPCLD  

Starting test: Connectivity  

......................... DCAPCLD passed test Connectivity

Doing primary tests

Testing server: Default-First-Site-Name\DCAPCLD

```
Starting test: DNS

     DNS Tests are running and not hung. Please wait a few minutes...
     ......................... DCAPCLD passed test DNS
```

Running partition tests on : ForestDnsZones

Running partition tests on : DomainDnsZones

Running partition tests on : Schema

Running partition tests on : Configuration

Running partition tests on : presenceus

Running enterprise tests on : presenceus.org  

Starting test: DNS  

Summary of test results for DNS servers used by the above domain controllers:

```
DNS server: 128.63.2.53 (h.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.127.in-addr.arpa. failed on the DNS server 128.63.2.53
        DNS server: 128.8.10.90 (d.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.127.in-addr.arpa. failed on the DNS server 128.8.10.90
        DNS server: 128.9.0.107 (b.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.127.in-addr.arpa. failed on the DNS server 128.9.0.107
        DNS server: 198.32.64.12 (l.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.127.in-addr.arpa. failed on the DNS server 198.32.64.12
        DNS server: 2001:500:12::d0d (g.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:12::d0d
        DNS server: 2001:500:1::53 (h.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:1::53
        DNS server: 2001:500:200::b (b.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:200::b
        DNS server: 2001:500:2::c (c.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:2::c
        DNS server: 2001:500:2d::d (d.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:2d::d
        DNS server: 2001:500:2f::f (f.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:2f::f
        DNS server: 2001:500:9f::42 (l.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:9f::42
        DNS server: 2001:500:a8::e (e.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:a8::e
        DNS server: 2001:503:ba3e::2:30 (a.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:503:ba3e::2:30
        DNS server: 2001:503:c27::2:30 (j.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:503:c27::2:30
        DNS server: 2001:7fd::1 (k.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:7fd::1
        DNS server: 2001:7fe::53 (i.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:7fe::53
        DNS server: 2001:dc3::35 (m.root-servers.net.)
           1 test failure on this DNS server
           PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:dc3::35
     ......................... presenceus.org passed test DNS
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2020-08-20*

Hi,  

Thanks for posting in Q&A platform.  

As far as I know, it is safe to ignore the error if the DNS resolution works fine.  

"Dcdiag" tests the functionality of root hints by sending a reverse DNS lookup query for 1.0.0.127.in-addr.arpa (ipv4) and 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa (ipv6). These records exist on all Windows DNS servers (you may find it when you select the Advanced view in DNS management console). However, most root hints server (external DNS servers) does not have such reverse lookup zone which contains 1.0.0.127.in-addr.arpa and 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa or they do not perform recursive lookup. This is why the test failed.  

Hope my answer will help you.  

Please Accept answer if the reply is useful.  

Best Regards,  

Sunny

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-08-19*

There are no more endpoints available from the endpoint mapper  

means we have run out of dynamic ports. netstat -aon should confirm this. I'd try rebooting.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-08-19*

The existence of SYSVOL_DFSR is not an issue, its just an indication that is was migrated FRS->DFSR. Another thing to try is just do a non-authoritative synchronization  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo    

 on the new one since we're seeing;  

The DFS Replication service initialized SYSVOL at local path C:\Windows\SYSVOL\domain and is waiting to perform initial replication. The replicated folder will remain in the initial synchronization state until it has replicated with its partner  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-08-19*

Please run;  

-  Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log  

-  repadmin /showrepl >C:\repl.txt  

-  ipconfig /all > C:\dc1.txt  

-  ipconfig /all > C:\dc2.txt  

-  (etc. as other DC's exist)  

then put unzipped text files up on OneDrive and share a link.
