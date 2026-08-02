---
title: "SRV error joining Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/533059/srv-error-joining-active-directory
question_id: 533059
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# SRV error joining Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/533059/srv-error-joining-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am running AD 2008, which had been working until a few days ago. Suddenly some workstations cannot find resources.

I removed a single workstation and attempted to re-join, which displayed the following.

The following error occurred when DNS was queried for the service location (SRV) resource record used to locate an Active Dire

The error was: "DNS name does not exist."  

(error code 0x0000232B RCODE_NAME_ERROR)

The query was for the SRV record for _ldap._tcp.dc._msdcs.domain.com

Common causes of this error include the following:

-    The DNS SRV records required to locate a AD DC for the domain are not registered in DNS. These records are registered with a

192.168.1.9

-    One or more of the following zones do not include delegation to its child zone:

domain.com  

com  

. (the root zone)

This makes no sense to me given the following response from nslookup on the DC (192.168.1.9) itself.

C:\Users\Administrator>nslookup  

Default Server: fileserver.domain.com  

Address: 192.168.1.18

> set type=all  

> _ldap._tcp.dc._msdcs.domain.COM  

Server: fileserver.domain.com  

Address: 192.168.1.18

_ldap._tcp.dc._msdcs.domain.COM SRV service location:  

priority = 0  

weight = 100  

port = 389  

svr hostname = domaindc.domain.com  

_ldap._tcp.dc._msdcs.domain.COM SRV service location:  

priority = 0  

weight = 100  

port = 389  

svr hostname = fileserver.domain.com  

domaindc.domain.com internet address = 192.168.1.9  

fileserver.domain.com internet address = 192.168.1.18  

> EXIT  

Server: fileserver.domain.com  

Address: 192.168.1.18

Any ideas on where to start?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-30*

DFS Replication service has detected an NTFS change journal wrap. DFS Replication service was not running on this computer for an extended period of time. The DFS Replication service could not keep up with the rate of file changes on the volume. The service has automatically initiated the journal wrap recovery process.   

Hopefully it will recover. If not the simplest solution may be to move the roles off, demote, reboot, promo it again.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-30*

I do not think there is a rogue DHCP router.  

OneDrive  

I hope I followed your instructions accurately.   

Thanks for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-30*

OneDrive

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-30*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

then put `unzipped` text files up on OneDrive and share a link.
