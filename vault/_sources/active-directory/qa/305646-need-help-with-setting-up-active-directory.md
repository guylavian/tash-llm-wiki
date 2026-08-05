---
title: "Need help with setting up active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/305646/need-help-with-setting-up-active-directory
question_id: 305646
fetched: 2026-07-25
answer_count: 15
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Need help with setting up active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/305646/need-help-with-setting-up-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I’m trying to setup a test domain at home to learn more about active directory. I have a vm setup win server 2019 and followed many guides on how to add a domain controller. Everything seems to be setup correctly, however when I try to add a Pc to a domain I get the following error. Any help would be appreciated The domain name "hometest" might be a NetBIOS domain name. If this is the case, verify that the domain name is properly registered with WINS. If you are certain that the name is not a NetBIOS domain name, then the following information can help you troubleshoot your DNS configuration. The following error occurred when DNS was queried for the service location (SRV) resource record used to locate an Active Directory Domain Controller (AD DC) for domain "hometest": The error was: "DNS server failure." (error code 0x0000232A RCODE_SERVER_FAILURE) The query was for the SRV record for _ldap._tcp.dc._msdcs.hometest Common causes of this error include the following: - The DNS servers used by this computer contain incorrect root hints. This computer is configured to use DNS servers with the following IP addresses: 192.168.25.1 - One or more of the following zones contains incorrect delegation: hometest . (the root zone)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-10*

Here is the link to the logs: https://1drv.ms/u/s!AtYNeAn3hQMVgg6etowYavZJxGzA?e=JZDm1d  

A little info about my setup  

ISP is comcast cable which is DHCP & comcast cable gateway.  

I have a netgear nighhawk R700 router  

Tried to setup both VM and another PC and same results.  

have server set to static ip 192.168.25.50  

When running the initial everything runs correctly. followed my guides on how to setup a domain controller. the issue seems when i want to join a pc to the domain is where i get the hang up on.   

if you need any further info i do my best to help, and thank you for helping me i am trying to learn this stuff.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-10*

Hi,  

For this situation, i would also suggest you check if the DC is healthy .  

You may try the command provided by DSPatric and check if there are any errors.  

If you have any updates, welcome to share here!  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-09*

What is problem member?  

the desktop machine  

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`netsh advfirewall monitor show currentprofile >C:\DC1profile.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

`netsh advfirewall monitor show currentprofile >C:\problemworkstationprofile.txt`  

`C:\Windows\debug\netsetup.log`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-09*

I’m running windows 2019 on an old laptop and same issues. I’m just trying to add a windows 10 pro desktop to my local domain.  

What is problem member?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-09*

What operating systems are involved? I'd check that the domain controller and problem member both have the static ip address of DC listed for DNS and no others such as router or public DNS.  

--please don't forget to Accept as answer if the reply is helpful--
