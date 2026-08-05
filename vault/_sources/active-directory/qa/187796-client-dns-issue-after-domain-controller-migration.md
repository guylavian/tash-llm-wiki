---
title: "Client DNS issue after Domain controller migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/187796/client-dns-issue-after-domain-controller-migration
question_id: 187796
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Client DNS issue after Domain controller migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/187796/client-dns-issue-after-domain-controller-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i had migrated from 2008 R2 Domain controller to 2016, all FSMO roles transferred to 2016 server. after migration existing clients machines not resolving new server DNS, it gives below error.

C:\Users\administrator.CLOUD>nslookup  

DNS request timed out.  

timeout was 2 seconds.  

Default Server: UnKnown  

Address: 192.168.201.11

new servers are able to resolve 2016 server DNS without any issue.

i did not demoted 2008 R2 domain due to DNS issue. i tried registering DNS manually but no luck

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-06*

Hi,    

The PTR you shared it in your last answer is for : 192.168.201.3    

    

Create new PTR for 192.168.201.11.    

Try to resolve a FQDN with local DNS suffix  :  `nslookup dc.cloud.local` to check if you get the same timeout    

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-06*

Hello Thmeur,  

PRT record is fine

C:\Users\administrator.CLOUD>nslookup google.com  

DNS request timed out.  

timeout was 2 seconds.  

Server: UnKnown  

Address: 192.168.201.11

DNS request timed out.  

timeout was 2 seconds.  

DNS request timed out.  

timeout was 2 seconds.  

DNS request timed out.  

timeout was 2 seconds.  

DNS request timed out.  

timeout was 2 seconds.  

*** Request to UnKnown timed-out

if i use my old domain IP it works fine, old domain 201.1 and new 201.11

C:\Users\administrator.CLOUD>nslookup  

Default Server: dc.cloud.local  

Address: 192.168.201.1

192.168.201.11

Server: dc.cloud.local  

Address: 192.168.201.1

Name: ad2016.cloud.local  

Address: 192.168.201.11

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-06*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-06*

Hi,    

Default Server: UnKnown this message means that there is no PTR entry (it's DNS entry to identify the server name by its IP addresse) for new DNS server. but the PTR dns entry is not required to let client send DNS requests to the server 192.168.201.11 .    

check if the client is able to resolve FQDN of any machine to test if it get answer from DNS server 192.168.201:    

nslookup domainName:    

    

Please don't forget to mark this reply as answer if it help you to fix your issue
