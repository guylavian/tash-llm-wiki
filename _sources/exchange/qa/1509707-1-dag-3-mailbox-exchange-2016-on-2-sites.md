---
title: "1 DAG, 3 Mailbox Exchange 2016 on 2 sites"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1509707/1-dag-3-mailbox-exchange-2016-on-2-sites
question_id: 1509707
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-high-availability-clustering-high-availability", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# 1 DAG, 3 Mailbox Exchange 2016 on 2 sites

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1509707/1-dag-3-mailbox-exchange-2016-on-2-sites (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts, I have a question.
We have 2 sites, primary and DRP.
On Main site we have 2 DCs and 2 Exchange Servers   

On DRP Site we have 1 DC and 1 Exchange Server.
We have 1 DAG for the 3 Exchange Server.
The DAG is ip-less.
The network connectiviy between Sites is over VPN.  

OS: WS 2016 (updated to January 2024)
Exchange Server Datacenter 2016 CU 23 Nov 23SU.
On DAG Cluster we set :
(get-cluster).CrossSiteDelay = 4000 
(get-cluster).CrossSiteThreshold = 120    

https://techcommunity.microsoft.com/t5/failover-clustering/tuning-failover-cluster-network-thresholds/ba-p/371834
On Exchange´s servers on main site: DatabaseCopyAutoActivationPolicy IntrasiteOnly and DatabaseCopyActivationDisabledAndMoveNow $false    

On Exchange´s server on DRP site: DatabaseCopyAutoActivationPolicy blocked and DatabaseCopyActivationDisabledAndMoveNow $true  

https://techcommunity.microsoft.com/t5/failover-clustering/tuning-failover-cluster-network-thresholds/ba-p/371834
Now, the Database on DAG and replication is working fine , the Exchange Server on DRP Site have an issue:   

On ECP Database Availability Group show the Exchange Server on DRP is operational "NO", the other Exchange servers on main site is "YES"   

When we try to activate the database passive copy on DRP site, we can't do that and the issue is similar to split brain, however the Database replication on DAG is working fine "Passive Healthy" and is replicating.  

Since I have a DAG with 3 members (ODD) we don't use witness, do you know if we need to consider another thing?  

We need to have 3 servers on dag (1 active and 2 passive).
Any help is appreciated.
:-)

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-25*

Hello @Fernando Mendoza Ortiz  ，

have you tried putting it in maintenance mode at some point?

What I mean is, if you tried it in maintenance mode before, you might need to try taking it out of maintenance mode.

According to the error message you provided, the error message indicates that the product has been uninstalled, which indicates that the cluster software may not be installed or configured correctly. To resolve this issue, we recommend that you try uninstalling and reinstalling the FailoverClustering role. Alternatively, you could first turn off Windows Firewall (if it is on) and then try.

Hope the above is helpful to you :-)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
