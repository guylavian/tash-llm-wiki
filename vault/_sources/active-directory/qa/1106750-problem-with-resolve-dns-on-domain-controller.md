---
title: "Problem with resolve DNS on Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1106750/problem-with-resolve-dns-on-domain-controller
question_id: 1106750
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_affiliations: ["Mvp"]
---
# Problem with resolve DNS on Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1106750/problem-with-resolve-dns-on-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

when I use DCDIAG /test:DNS and I have this problem    

```
PS C:\Users\Administrator> DCDIAG /test:DNS  
  
Directory Server Diagnosis  
  
Performing initial setup:  
   Trying to find home server...  
   Home Server = AD01  
   * Identified AD Forest.  
   Done gathering initial info.  
  
Doing initial required tests  
  
   Testing server: Default-First-Site-Name\AD01  
      Starting test: Connectivity  
         The host a57db1a0-89f2-4ea1-826b-1fc5f1992c0f._msdcs.domain.local could not be resolved to an IP address. Check  
         the DNS server, DHCP, server name, etc.  
         Got error while checking LDAP and RPC connectivity. Please check your firewall settings.  
         ......................... AD01 failed test Connectivity  
  
Doing primary tests  
  
   Testing server: Default-First-Site-Name\AD01  
  
      Starting test: DNS  
  
         DNS Tests are running and not hung. Please wait a few minutes...  
         ......................... AD01 passed test DNS  
  
   Running partition tests on : ForestDnsZones  
  
   Running partition tests on : DomainDnsZones  
  
   Running partition tests on : Schema  
  
   Running partition tests on : Configuration  
  
   Running partition tests on : domain  
  
   Running enterprise tests on : domain.local  
      Starting test: DNS  
         Test results for domain controllers:  
  
            DC: AD01.domain.local  
            Domain: domain.local  
  
  
               TEST: Basic (Basc)  
                  Error: No LDAP connectivity  
                  Warning: adapter [00000001] Intel(R) 82574L Gigabit Network Connection has invalid DNS server:  
                  8.8.8.8 ()  
                  Warning: adapter [00000001] Intel(R) 82574L Gigabit Network Connection has invalid DNS server:  
                  1.1.1.1 ()  
                  Error: all DNS servers are invalid  
                  No host records (A or AAAA) were found for this DC  
  
               TEST: Forwarders/Root hints (Forw)  
                  Error: All forwarders in the forwarder list are invalid.  
                  Error: Both root hints and forwarders are not configured or broken. Please make sure at least one of  
                  them works.  
  
               TEST: Dynamic update (Dyn)  
                  Warning: Failed to add the test record dcdiag-test-record in zone domain.local  
  
            TEST: Records registration (RReg)  
               Error: Record registrations cannot be found for all the network adapters  
  
         Summary of test results for DNS servers used by the above domain controllers:  
  
            DNS server: 1.1.1.1 ()  
               2 test failure on this DNS server  
               Name resolution is not functional. _ldap._tcp.domain.local. failed on the DNS server 1.1.1.1  
  
            DNS server: 8.8.8.8 ()  
               2 test failure on this DNS server  
               Name resolution is not functional. _ldap._tcp.domain.local. failed on the DNS server 8.8.8.8  
  
            DNS server: 192.112.36.4 (G.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.127.in-addr.arpa. failed on the DNS server 192.112.36.4  
            DNS server: 192.203.230.10 (E.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.127.in-addr.arpa. failed on the DNS server 192.203.230.10  
            DNS server: 2001:500:1::53 (H.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:1::53  
            DNS server: 2001:500:2::c (C.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:2::c  
            DNS server: 2001:500:2d::d (D.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:2d::d  
            DNS server: 2001:500:2f::f (F.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:2f::f  
            DNS server: 2001:500:84::b (B.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:84::b  
            DNS server: 2001:500:9f::42 (L.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:500:9f::42  
            DNS server: 2001:503:ba3e::2:30 (A.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:503:ba3e::2:30  
            DNS server: 2001:503:c27::2:30 (J.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:503:c27::2:30  
            DNS server: 2001:7fd::1 (K.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:7fd::1  
            DNS server: 2001:7fe::53 (I.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:7fe::53  
            DNS server: 2001:dc3::35 (M.ROOT-SERVERS.NET.)  
               1 test failure on this DNS server  
               PTR record query for the 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa failed on the DNS server 2001:dc3::35  
         Summary of DNS test results:  
  
                                            Auth Basc Forw Del  Dyn  RReg Ext  
            _________________________________________________________________  
            Domain: domain.local  
               AD01                         PASS FAIL FAIL PASS WARN FAIL n/a  
  
         ......................... domain.local failed test DNS
```

Have someone solution to it?

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-11-28*

Remove the public DNS. Domain controller and all members must use the static ip address of DC listed for DNS and no others such as router or public DNS.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
