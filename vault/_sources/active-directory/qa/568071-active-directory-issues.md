---
title: "Active Directory Issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/568071/active-directory-issues
question_id: 568071
fetched: 2026-07-25
answer_count: 22
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory Issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/568071/active-directory-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Current Domain Environment:  

2 Domain Controllers running Server 2016 Standard. Both machines are hosted in VMWare on premise. Both machines have Active Directory Domain Services and DNS Server installed. One server is also running DHCP Server.  

1 member server running Server 2019 Datacenter hosting Active Directory Certificate Services and Network Policy Server using Radius as part of MFA for VPN users.  

GPO pushes certificates to computers in VPN group  

1 member server running Server 2019 Datacenter hosting Microsoft Exchange 2019.  

Several Server 2016 and Server 2019 servers hosting various applications and services.  

Domain Functional Level 2016

If either of the 2016 Domain Controller servers is restarted for ANY reason, it is usually not possible to log in to the server and Domain services and DHCP do not function. When the password for the user account is entered and the “submit” button or enter key is pressed, nothing happens. The cursor is either sent to the beginning of the password field or to the beginning of the username field. Changing users or retrying the logon does not change the behavior. The machine must be restarted several times before finally being able to logon.  

We tried adding 2 new domain controllers using Server 2019 Datacenter. Once it they were promoted to a domain controller, the console could not be logged onto. It would give the message or “Bad Username or Password”. If they was left running for a period of time and a computer on the network tried to authenticate a user account against this domain controller, the account would be denied with “Bad Username or Password”. The server could be connected to and managed with Server Manager or PowerShell. Remote Desktop sessions could not connect and were give the “Bad Username or Password” message. Server 2019 Domain controller was powered off to prevent valid user from being denied.

Running the AD Replication Status Tool, one of the 2019 DCs gives 2 errors for 2 of the other DCs. Replication Error 1256 and 1722. Running DCDIAG from one of the 2016 DCs, all tests pass except it shows "A recent replication atempt failed:" and it lists the 2 errors: 1256 & 1722

Obviously, something is broken and I have exhausted myself trying to track this down.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-27*

DC1 - It already has 127.0.0.1 in the list. Is this not sufficient?    

No, add the address and follow advice above    

We require higher time accuracy than can be achieved from the Windows time    

You can follow along here    

https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/configuring-systems-for-high-accuracy    

If I try to demote DC02 I get an Error    

The other option is to move roles off, remove from network and perform cleanup to remove remnants    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-27*

DC02 - Done  

DC1 - It already has 127.0.0.1 in the list.  Is this not sufficient?  

DC01 - Again, already has 127.0.0.1  

DSPatrick answered  

On DC02 I'd add the server's own static ip address (10.91.150.52) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service  

On DC1 I'd add the server's own static ip address (10.91.150.2) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service  

On DC01 I'd add the server's own static ip address (10.91.150.51) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service  

I see Error 5008 in the DFS Replication logs on every server:  

The DFS Replication service failed to communicate with partner DC1 for replication group Domain System Volume. This error can occur if the host is unreachable, or if the DFS Replication service is not running on the server.   

Partner DNS Address: DC1.morgan911.net   

Optional data if available:   

Partner WINS Address: DC1   

Partner IP Address: 10.91.150.2   

The service will retry the connection periodically.   

Additional Information:   

Error: 1722 (The RPC server is unavailable.)   

We run a 3rd party time sync software on our DCs and all of our domain servers and workstations.  We require higher time accuracy than can be achieved from the Windows time service.  

IPv6 disabled on DC02  

AD02 is currently the only authorized DHCP server on the network.  The goal is to have 2 and DC02 is supposed to eventually be the 2nd DHCP server.  DHCP server has been installed but not configured.  

If I try to demote DC02 I get an Error:    

Error validating Credentials:  Verification of user credential permissions failed.  Failed to examine the Active Directory forest.  The error was:  The operation cannot continue because the LDAP connect/bind operation failed:  Error 1326 (The user name or password is incorrect).

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-27*

On DC02 I'd add the server's own static ip address (10.91.150.52) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service  

On DC1 I'd add the server's own static ip address (10.91.150.2) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service  

On DC01 I'd add the server's own static ip address (10.91.150.51) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service  

DC1 not advertising  

DC01 not advertising  

DC02 not advertising  

On these three I'd do  

`w32tm /unregister`  

`net stop w32time`  

`w32tm /register`  

`net start w32time`  

`w32tm /config /syncfromflags:domhier /update`  

`net stop w32time`  

`net start w32time`  

then check  

`w32tm /query /source`  

`w32tm /query /configuration`  

On DC1 I'd check the DFS Replication event log for errors since last boot  

On DC01 I'd check the DFS Replication event log for errors since last boot  

On AD02 I'd check the DFS Replication event log for errors since last boot  

DC02 is still running FRS. There may have been a migration FRS->DFSR and this one did not complete. You could try demote, reboot, promo it again.  

DC02  This computer has at least one dynamically assigned IPv6 address. I'd turn off IPv6 on DHCP server unless it is configured correctly this will cause problems.  

DC02 has encountered another DHCP service on the network belonging to a directory service enterprise on which the local machine is not authorized. May be more than one DHCP server on network? Problematic  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-27*

Here is the link:  

https://1drv.ms/u/s!AqUWjGdph56LgQu267clVCyFl_SB?e=UmwZtc

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-27*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

`ipconfig /all > C:\dc4.txt`  

then put `unzipped` text files up on OneDrive and share a link.
