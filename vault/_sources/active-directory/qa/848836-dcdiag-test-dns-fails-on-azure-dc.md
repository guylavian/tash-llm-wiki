---
title: "DCdiag:test:dns fails on azure DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/848836/dcdiag-test-dns-fails-on-azure-dc
question_id: 848836
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# DCdiag:test:dns fails on azure DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/848836/dcdiag-test-dns-fails-on-azure-dc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings, I have to admit, I am definitely a rookie when it comes to Azure and could use some help. Can anyone guide me in the right direction to resolve these errors? I had a consultant set these up for me and have no idea where to look or how to troubleshoot. I tried googling it but the sheer amount of information that come back makes my head spin. I believe 8.8.8.8 is google and 168.63.129.16 is azure but not sure how to go about fixing the issue. thanks

Error:  

Missing SRV record at DNS server 8.8.8.8:  

_kerberos._tcp.Azure-USEast2._sites.dc._msdcs.mydomain

```
Error:
                 Missing SRV record at DNS server 8.8.8.8:
                 _ldap._tcp.Azure-USEast2._sites.dc._msdcs.mydomain

                 Error:
                 Missing SRV record at DNS server 8.8.8.8:
                 _kerberos._tcp.Azure-USEast2._sites.mydomain

                 Error:
                 Missing SRV record at DNS server 8.8.8.8:
                 _ldap._tcp.gc._msdcs.mydomain

                 Warning:
                 Missing A record at DNS server 8.8.8.8:
                 gc._msdcs.mydomain

                 Error:
                 Missing SRV record at DNS server 8.8.8.8:
                 _gc._tcp.Azure-USEast2._sites.mydomain

                 Error:
                 Missing SRV record at DNS server 8.8.8.8:
                 _ldap._tcp.Azure-USEast2._sites.gc._msdcs.mydomain

           Error: Record registrations cannot be found for all the network adapters

     Summary of test results for DNS servers used by the above domain controllers:

        DNS server: 8.8.8.8 ()
           2 test failure on this DNS server
           Name resolution is not functional. _ldap._tcp.mydomain. failed on the DNS server 8.8.8.8

        DNS server: 168.63.129.16 ()
           1 test failure on this DNS server
           Name resolution is not functional. _ldap._tcp.mydomain. failed on the DNS server 168.63.129.16

     Summary of DNS test results:

                                        Auth Basc Forw Del  Dyn  RReg Ext
        _________________________________________________________________
        Domain: mydomain
           az-eastus2-dc01              PASS WARN PASS PASS PASS FAIL n/a

     ......................... Mydomain failed test DNS
```

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-05-13*

I'd check that your domain controller has own static ip address listed for DNS and no others such as router or public DNS    

https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances#name-resolution-that-uses-your-own-dns-server    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-01*

why are your using google DNS on your DC?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-06-01*

In addition to what @Anonymous   mentioned, here are some additional considerations when Deploy AD DS in an Azure virtual network also guidance on How to verify that SRV DNS records have been created for a domain controller. Hope this helps.
