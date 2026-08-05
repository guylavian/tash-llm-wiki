---
title: "Active Directory DNS Records have disappeared"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/760611/active-directory-dns-records-have-disappeared
question_id: 760611
fetched: 2026-07-25
answer_count: 15
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory DNS Records have disappeared

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/760611/active-directory-dns-records-have-disappeared (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We installed and configured our Active Directory about 3 months ago.  

AD DS and DNS roles installed on a server and then other computers joined. Everything was OK.  

However today after 3 months we tried to join a few more machines but because the DNS lookup for SVR record failed, I logged into the AD server to find out that all DNS records are gone. Nothing is left except the zone (mydomain.com) itself plus one SOA and one NS record. Everything else is wiped out.  

I'm the only one who has access to this server.  

I tried to solve this by removing DNS role and adding it again, to no avail.  

This is a crisis for us. Please assist.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-06*

@Anonymous       

The files you requested are here:    

https://1drv.ms/u/s!AnKo_BSti8xpiNFQohS-Wbyu4Ct1_Q?e=fToZ8Z    

Please note that we have one DC only and it's on the same server as AD and DNS.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-05*

Some possibilities here.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/dns-records-not-present    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-05*

@Anonymous       

Hello,    

Thanks. Looks like I panicked and posted this question without proper investigation.    

The zone file is still in `C:\Windows\System32\DNS` and it works fine and new machines were able to join the domain successfully BUT the DNS Manager GUI is empty and I don't see any of the records in it except for just one SOA and one NS record - both pointing to the server itself. Reloading the zone and restarting both DNS Server service and the server didn't solve this issue. The GUI is still empty.    

Now if you still need those files let me know and I'll provide them.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-05*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

then put `unzipped` text files up on OneDrive and share a link.
