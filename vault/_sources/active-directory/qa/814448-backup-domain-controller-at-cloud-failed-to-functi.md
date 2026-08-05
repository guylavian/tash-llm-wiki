---
title: "Backup Domain Controller at Cloud failed to function"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/814448/backup-domain-controller-at-cloud-failed-to-functi
question_id: 814448
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Backup Domain Controller at Cloud failed to function

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/814448/backup-domain-controller-at-cloud-failed-to-functi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All.  

I have a 2 VM in my local network, which serves as PDC and BDC. Also, I have installed and setup a BDC (using same OS which is Windows Server 2016) at VM in the Cloud (AWS), which serves at Disaster Recovery. I use IPSEC VPN from my local network to AWS. Both servers functioned properly and I can see the replication in all servers.  

Now, I would like to test the DR scenario. I turned OFF all Servers in my local network. I am assuming the BDC in the cloud will be functioned properly. but it's not. I can open DNS Manager and it showed my domain. but when I tried to open Active Directory Sites and Services and Active Directory Users and Computers, it failed with message :   

"Naming Information cannot be located because:  

The specified domain either does not exist or could not be contacted".  

Just additional notes:  

-  The BDC in the cloud can access internet and can access my local network (with the condition of both DC is turned off).  

-  When I ping my domain, it goes to the BDC in my local.  

-  When I nslookup to my domain (from my BDC in the cloud), it showed all three DCs, and default address : localhost  

-  If I turn ON the BDC in my local network, then the BDC in the cloud will be functioned properly. Also, the BDC in my local network is functioning properly. but this is not the scenario that I want.   

Any idea how to solve this?  

Thank you in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-16*

Hello.    

When your local DCs go down the site coverage must run and your cloud DC must take the responsibility of  local. I prefer to say it is DNS issues.  please check these possible issues in DNS server :    

The NS server IP and FQDN in your DNS server.     

Check the CNAME and it's GUID for each server.      

Try to create conditional forwarder in local DC with forest scope for cloud ( after that force to replicate).    

Additional causes :     

The date and time for both local and cloud server     

Firewall rules     

more information about ports :     

service-overview-and-network-port-requirements    

data-flow

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-04-16*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.
