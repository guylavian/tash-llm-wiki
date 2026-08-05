---
title: "After P2Ving a DC dcdiag reports \"name unavailable\" for its own ip address"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/436129/after-p2ving-a-dc-dcdiag-reports-name-unavailable
question_id: 436129
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# After P2Ving a DC dcdiag reports "name unavailable" for its own ip address

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/436129/after-p2ving-a-dc-dcdiag-reports-name-unavailable (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are in the process of upgrading our Server 2003 R2 infrastructure to 2019. Just before trying to take the migrate path, we had to P2V the existing two DCs to ESXi, since we were afraid of the physical hardware failing.

Specifically we've offline P2V'ed srv2 having ip 192.168.1.13 (the other DC srv1 is at 192.168.1.12). DNS forwarders for this network were 172.30.47.4 and 172.30.47.5. We've run a couple of hiccups during the conversion, but essentially all went well. Replication works fine and dcdiag /test:dns /e /v as well as repadmin /replsum /bysrc /bydest /sort:Delta pass without issues.

We do have one question though. Running dcdiag shows a "name unavailable" next to the ip corresponding to srv2:

```
Summary of test results for DNS servers used by the above domain controllers:

    DNS server: 192.168.1.12 (srv1.domain.local.)
       All tests passed on this DNS server
       This is a valid DNS server 
       Name resolution is funtional. _ldap._tcp SRV record for the forest root domain is registered 
       Delegation to the domain _msdcs.domain.local. is operational

    DNS server: 192.168.1.13 ()
       All tests passed on this DNS server
       This is a valid DNS server 
       Name resolution is funtional. _ldap._tcp SRV record for the forest root domain is registered 

    DNS server: 172.30.47.4 ()
       All tests passed on this DNS server
       This is a valid DNS server 

    DNS server: 172.30.47.5 ()
       All tests passed on this DNS server
       This is a valid DNS server 

 Summary of DNS test results:

                                    Auth Basc Forw Del  Dyn  RReg Ext  
       ________________________________________________________________
    Domain: domain.local
       srv2                   PASS PASS PASS PASS PASS PASS n/a  
       srv1                        PASS PASS PASS PASS PASS PASS n/a  

 ......................... domain.local passed test DNS
```

Any idea on what to look for? If needed I can paste the entire dcdiag output.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-06-15*

On atlas I'd add server own static ip address (10.128.64.12) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service    

the unknown Node Type could be the netbt thing mentioned here https://www.itprotoday.com/compute-engines/jsi-tip-6538-ipconfig-all-show-node-type-unknown    

Warning :There is less than 9% available RIDs in the current pool    

https://learn.microsoft.com/en-us/archive/blogs/askds/managing-rid-pool-depletion    

On prometheus On atlas I'd add server own static ip address (10.128.64.13) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service    

same issue with the unknown Node Type    

As to the migration to Server 2019 this will need to be a two-step process with (suggested) Server 2016 intermediary     

-  The prerequisite before introducing the first 2016 domain controller: domain functional level needs to be 2003 or higher    

-  The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2016, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-15*

Thank you for your efforts to help! Here they are with srv1=atlas, srv2=prometheus (the one that got P2V):  

https://1drv.ms/u/s!AkrNXPx6e5M2v1W3pqS1W_qhYhDM?e=RUSgkC

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-15*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-15*

Thank you for your detailed information. from your advice it is clear that I should not try to p2v my other DC, srv1. However, having dcdiag fun without any issues is a prerequisite to continue.  

It is this context that I need help with. That is make sure that dcdiag reports back what it should (ie recognize the .13 ip as srv2).  

If I can provide outputs from specific commands to help you help me here, please let me know.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-15*

P2V should be the last resort and especially for domain controllers. The much simpler, safer, quicker method is to stand up a new one on the target host.    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2003, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
