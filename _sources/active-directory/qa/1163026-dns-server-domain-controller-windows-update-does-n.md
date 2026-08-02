---
title: "DNS Server& Domain Controller:  Windows update does not work but forwarder can find IP address"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163026/dns-server-domain-controller-windows-update-does-n
question_id: 1163026
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# DNS Server& Domain Controller:  Windows update does not work but forwarder can find IP address

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163026/dns-server-domain-controller-windows-update-does-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a domain controller and secondary.  I have no issues with my domain.  

I can access nearly every internet website; however, Windows update does not work on one Windows 10 machine.  Using the diagnostics on that computer indicated that it not resolve the IP from the Windows domain name.  This was confirmed when using NSLOOKUP on the Windows 10 computer and other connected machines.

I can resolve the IP address if I point NSLOOKUP directly to the forwarder instead of the Windows DNS server.  This indicates that there is an issue with the Windows DNS Server.

I have run BPA on both domain controllers.  There are no issues.  I have checked the event logs on both domain controllers, there are no errors or warnings on either for the domain controller, applications or system (other than when I restarted one of the domain controllers).

Using NSLOOKUP on the primary domain controller, I have found that I can resolve "au.download.windowsupdate.com" when I "set norecurse".  I can also resolve any other external address such as "www.microsoft.com".  When I "set recurse", I can no longer resolve "au.download.windowsupdate.com" but I can resolve other external IP addresses.

Clearing the DNS caches on both domain controllers allows access to "au.download.windowsupdate.com" and all other internet addresses until the TTL is reached.  Once the TTL is reached "au.download.windowsupdate.com" is no longer resolvable but other internet IP addresses are.

My Unix DNS server resolves all internet addresses without any issues at all times.  I would like to simplify my setup and use my Windows DNS Servers.

Although I am testing using "au.download.windowsupdate.com", there are a number of other addresses that aren't resolved which has broken some programmes that need to access them.

I am at a loss as how to troubleshoot this issue.  My network is configured using IPv4.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-22*

I found the issue.

The Windows DNS server did not update the Trusted Root Anchors properly in order for DNSSEC to work.  As a result, some domains worked while others did not.  I was not able to find any log files or error messages that flagged this issue.  Once I manually updated the trusted root anchors, the IPs of the domains in question were able to be found by the Windows DNS Servers.  The only useful information regarding updating these I could find was on the www.icann.org website.

Thanks for your assistance Dave.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-01-22*

tried changing the DNS settings for each domain controller  

Ok, probably is not a showstopper but is not correct.

must be an issue with Windows DNS  

You could be right. Might try standing up a new one from testing or replacement.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-01-22*

DC is definitely having some replication issues connecting to DC2, may need to check the event logs for more details. Generally each domain controller should have its own static ip address listed for DNS plus the loopback. What you have may not be a showstopper but if it were me I'd fix it. As to the problem pc I'd just check that it only uses domain controller addresses only for DNS. Also if its a single pc bad actor then it may not be worth spending too much time on, rebuilding it may be more expedient.   

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-01-21*

Please run;

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`	(run on PDC emulator)  

`repadmin /showrepl >C:\repl.txt`	(run on any domain controller)  

`ipconfig /all > C:\%computername%.txt`	(run on EVERY domain controller)  

`ipconfig /all > C:\problemworkstation.txt`	(run on problem pc)  

Also check the domain controller System and Replication (DFS or FRS) event logs for errors since last boot. Post the Event Source and Event IDs of any found. (no evtx files)  

then put `unzipped` text files up on OneDrive and share a link.
