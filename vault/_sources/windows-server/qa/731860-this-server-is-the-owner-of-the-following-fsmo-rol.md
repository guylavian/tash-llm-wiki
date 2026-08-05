---
title: "This server is the owner of the following FSMO role, but does not consider it valid."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/731860/this-server-is-the-owner-of-the-following-fsmo-rol
question_id: 731860
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# This server is the owner of the following FSMO role, but does not consider it valid.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/731860/this-server-is-the-owner-of-the-following-fsmo-rol (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

we had an issue with a VM host, hosting one of our 2012R2 DCs.  

The host issues have now been resolved.  

This server is the owner of the following FSMO role, but does not consider it valid. For the partition which contains the FSMO, this server has not replicated successfully with any of its partners since the server was restarted.  

FSMO Role: Infrastructure.  

Now we get the above error on a primary DC (DC1) that had been down whilst the secondary (DC2) was up.  

As the host had issues (frequent reboots) over the last 3 months, I had expected the Dc may have passed the tombstone period, however couldnt see any errors related to it in event viewer.  

DC1 currently has all the FSMO roles.  

my instinct is telling me I need to seize the roles from DC1 to DC2. Also on DC1 to demote, remove from AD, wait for replication, rejoin and promote? i suspect this as i cannot join any new devices to the domain - the specified network name is no longer available

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-14*

DC1-TEST add server's own static address (10.77.33.5) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service.  

DC2-TEST add server's own static address (10.77.33.7) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service.  

no more endpoints available from the endpoint mapper  

replication appears to be blocked due to wrong firewall profiles other network issues.  

netstat -aon  

should show this result and a reboot may be needed to clear.  

 I'd check that both got the domain network profile, possibly restart the Network Location Awareness service.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-11*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.
