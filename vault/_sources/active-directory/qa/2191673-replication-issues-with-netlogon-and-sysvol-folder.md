---
title: "Replication issues with netlogon and sysvol folders."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191673/replication-issues-with-netlogon-and-sysvol-folder
question_id: 2191673
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Replication issues with netlogon and sysvol folders.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191673/replication-issues-with-netlogon-and-sysvol-folder (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, during our server migration from a Windows Server 2016 to Windows Server 2022 the sysvol and netlogon folders haven't replicated. I am able to see them on the old Windows Server 2016 server. I am receiving an error in the event viewer 4012. I have copied and pasted the error below. 

The DFS Replication service stopped replication on the folder with the following local path: C:\windows\SYSVOL\domain. This server has been disconnected from other partners for 158 days, which is longer than the time allowed by the MaxOfflineTimeInDays parameter (60). DFS Replication considers the data in this folder to be stale, and this server will not replicate the folder until this error is corrected.  

To resume replication of this folder, use the DFS Management snap-in to remove this server from the replication group, and then add it back to the group. This causes the server to perform an initial synchronization task, which replaces the stale data with fresh data from other members of the replication group.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-23*

Hello Shannon Maddox,

Thank you for posting in Microsoft Community forum.

How many DCs are there in the domain now?

Please check the AD replication between the two DCs first. Run the commands below on PDC.

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt  

repadmin /showrepl * /csv >c:\repsum.csv

Please try the possible solution in the similar threads below.

Problems with DFSR SYSVOL, NETLOGON replication - Microsoft Q&A

DFS Replication issue with event ID 4012 (windows server 2016 - Microsoft Q&A

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
