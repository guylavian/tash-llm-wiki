---
title: "One DC is pulling FSMO from an AD server that doesn't exist, other DC sees FSMO correctly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/556927/one-dc-is-pulling-fsmo-from-an-ad-server-that-does
question_id: 556927
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# One DC is pulling FSMO from an AD server that doesn't exist, other DC sees FSMO correctly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/556927/one-dc-is-pulling-fsmo-from-an-ad-server-that-does (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 DC, one onpremDC, one hostedDC. There was some previous work where an RDS server was made a DC and FSMO moved to it, then the hostedDC was made the DC & FSMO moved to it, then AD removed from the RDS server. However, the onpremDC still sees the RDSserver as holding all the FSMO (even though it is no longer an AD server). Each DC was only pointing to itself for DNS, so I fixed that, however "netdom query fsmo" from onpremDC still shows the RDSserver (that doesn't exist as an AD server now) as the holder. HostedDC shows itself as fsmo holder (which it should be). Obviously AD/dns/replication issues abound. Onprem will be going away soon anyways, so I was wondering should I put more time in trying to fix onpremDC (thought was it wouldn't take long to fix it, then it could be cleanly decommissioned)? I am not 100% sure AD is perfectly healthy with cloudDC (all clients are only pointing to cloudDC currently & "seem" to be working), otherwise, I would be tempted to just decom onpremDC and run through any metadata/cleanup needed to purge any reference to onpremDC & if there are any leftovers of RDS-DC. Eventually, I'll add a second hostedDC for the environment, but that is not currently scheduled. If I should fix onpremDC first, how do I tell it to pull the correct server as the fsmo role holder, assuming that is the big issue that needs to be fixed first? All server 2016.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-20*

Hello,  

Thank you for your question.  

I would like to suggest you to check below Troubleshooting steps.  

If netdom query still FSMP roles holing to RDS server then it could be due to Replication is not being completed or its still pending.  

I would suggest you to download Active Directory Replication Status Tool and Fix replication issues before removing old RDSserver .  

https://www.microsoft.com/en-in/download/details.aspx?id=30005  

Please also disable any firewall or Antivirus  program which may blocking to get AD synced between DCs.  

If the reply was helpful, please don’t forget to upvote or accept as answer.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-17*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.
