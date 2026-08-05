---
title: "Active Directory Failover"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1402949/active-directory-failover
question_id: 1402949
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory Failover

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1402949/active-directory-failover (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We recently, migrated/upgraded customers Active Directory 2012 to 2022. It seems to be successful as users and computers were replicated in the 2022 Active Directory. We tried to test if it would failover, but it didn't. Scenario of the testing below:

Setup:

2x DC (Primary and Secondary) in 1 Site; WS2022.

-  We plugged off the Network Cable of the Primary

-  We ping the domain, returns RTO.

-  We tried to login to a workstation, not able to authenticate.

-  We plugged the Network Cable back in the Primary

-  We ping the domain, was able to Ping the Primary

What i was expecting is even if the primary is down, when we ping the domain, the secondary IP should be pingable. And also, users should be able to authenticate since there is a secondary DC.

I wish we could get help immediately. Thank you in advanced!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-26*

As for the Replication Events:

SOURCE
EventID

DFSR
5002, 1202, 5008, 6104

For the System Events:

Source
EventID

NETLOGON
5722

Service Control Manager
7030

DistributedCOM
10028

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-10-26*

Hi @Kenelm Ulric Dogcio  

please make sure you you hide all the sensitive information from your log files. I just took a short look and you have put all your customer's log files publicly on the Internet. Those contain very important and sensitive IPs. I would encourage you to anonymize those or find another way of providing the data needed. 

(If the reply was helpful please don't forget to upvote or accept as answer, thank you)  

Regards,  

Stoyan

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-10-26*

-  Both WSUS and SATADC1 are multi-homed which will always cause no end to grief for active directory DNS.        

-  Each domain controller should have at a minimum its own static ip address plus the loopback (127.0.0.1) listed for DNS. So remove any of the other addresses. After corrections then do an ipconfig /flushdns, ipconfig /registerdns, and restart the netlogon service.

-  You didn't put up the file for the problem member but make sure it has the static addresses of both domain controllers listed for DNS and no others such as router or public DNS or the other unknown addresses the DCs have.       

-  I didn't look too much at the rest because above are showstoppers. If problems persist then put up a new set of files to look at.        

--please don't forget to close up the thread here by marking answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-26*

Hi Dave!

Just got back from the client. Here's the link for the log files.

https://gsiorg0-my.sharepoint.com/:f:/g/personal/ulric_d_gsiorg_ph/EtpowCKXwYdGhvvcLPzKjDEBTg13eaK764BNb_J1xMbwig?e=L94Md9

The DC that were having problems is the Secondary.

Thanks for your help!
