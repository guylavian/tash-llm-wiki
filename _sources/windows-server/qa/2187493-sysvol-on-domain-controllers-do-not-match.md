---
title: "SYSVOL on Domain Controllers do not Match"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187493/sysvol-on-domain-controllers-do-not-match
question_id: 2187493
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# SYSVOL on Domain Controllers do not Match

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187493/sysvol-on-domain-controllers-do-not-match (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have three DCs and the local SYSVOL directory on the three do not match. In GPM console there a few GPOs I click on and get a message popup that it could not be located. Here is my environment. 

All DCs are Server 2019, I'm running DFSR. All repladmin and dcdiag test come back fine, other than repladmin /replsummery shows errors in last 24 hours in the DFSR logs. But I always looked over that since the nightly backups log an error to pause the replication for backup. 

All DCs are GC, and run DNS. 

DC1: PDC and FSMO roles, has less directories in SYSVOL than DC2 and DC3; DNS Primary self, DNS secondary DC2

DC2: RID Master role, has same number of directories in SYSVOL as DC3; DNS primary self, DNS secondary DC1

DC3: has same number of directories in SYSVOL as DC2; DNS primary is self, DNS secondary is DC1

I created a folder in the the local SYSVOL directory on each DC. DC2 and DC3 immediately held the new folder from all other DCs. 

DC1 never received the new folder from DC2 or DC3. 

On DC1 the DFSR log show the nightly pause of replication when the backups run, and then this error. 

The DFS Replication service is stopping communication with partner DC2 for replication group Domain System Volume due to an error. The service will retry the connection periodically. Otherwise it's all normal replication log entries. 

Additional Information: 

Error: 9033 (The request was cancelled by a shutdown) 

Connection ID: D96D228F-6825-48FC-926B-4E8628BD3FE8 

Replication Group ID: 7062DE7B-C13B-49AD-99A1-5680D3DE69CF

I checked and all three have content freshness value set to 60. After reading through the few related, but not exactly same situation, posts and answers and suggestions, I'm not sure how to proceed. I do not want to make something worse than it already is. It's unclear if an authoritative replication or non authoritative replication should be run, and if so on which DC. Is there something further to look at and help determine what is causing this issue?

TYIA

## Answer (community) — community member

*upvotes: 1 · updated: 2024-10-30*

Thank you for all the suggestions. For the general network connectivity, firewalls etc, all is good. DC1 and DC2 are on the same network even. 

Even though I can look up the command dfsrdiag /testintegrity and see the parameters, typing it on my DCs gives me an "unrecognized parameter 'testintegrity'"  and lists all the known parameters for dfsrdiag  and none are that one. 

I also tried PowerShell Get-DfsReplicationGroup -groupname * and I get no return at all. Should I? Adding the -includesysvol does show me the domain replication entity. 

So without further input on those options to troubleshoot, it looks like I'm at the step of running an authoritative restore on DC2 or DC3. By backing up, is that with the built in Windows Backup utility, or just make a copy of the local SYSVOL directory?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-03*

This has been resolved. After looking at everything and trying to force sync commands it was not progressing. DFSRDIAG backlog was showing a long list of items not replicating between servers. The list combined with the sharing violation, ID4302 is the source, I checked open sessions. All the same sysvol items were listed with an open session that were backlogged. 

I rebooted first the authoritative DC. Waited a while, and checked the backlog for it, nothing was listed. Then rebooted the next DC, waited and check backlog. Finally third DC. Nothing was showing a backlog, or any errors in DFSR events. I was then able to create a folder on each DC and it instantly appear on all other DCs.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-03*

Okay, I ended up following the instructions here to do an authoritative restore, making DC2 the authoritative source. (for the record DC1 is the PDC emulator)  https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization

I ran this in a lab environment using restores of my DCs. It worked flawlessly, and when I made changes to any one of the DCs the other 2 updated. I went through the process in my prod environment and it did not clear things up.   

Now DC2 is pushing it's changes to DC1 and DC3 fine. But DC1 and DC3 are not pushing their changes to any other DC.   

Both DC1 and DC3 are now showing these in the DFSR event logs.   

Event ID 4302: The DFS Replication service has been repeatedly prevented from replicating a file due to consistent sharing violations encountered on the file. A local sharing violation occurs when the service fails to receive an updated file because the local file is currently in use.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-18*

Hi Gyan Gearon,

Thank you for posting in the Microsoft Community Forums.

Check the status of DFS replication:

On each DC, open the DFS Replication administration tool and check the status of the replication group.

Look for any warning or error messages, especially related to DC1.

Check network connectivity:

Ensure that the network connections between all DCs are healthy.

Use the ping and tracert commands to test connectivity between DCs.

Review DFS replication logs:

Drill down into the DFS replication logs, especially the entries related to error 9033.

Error 9033 usually indicates that a replication request was canceled for some reason (e.g., network connection down, firewall rule, DFSR service issue, etc.).

Check the firewall settings:

Make sure there are no firewall rules blocking DFS replication traffic between DCs.

DFS replication uses the RPC and SMB protocols, and you need to ensure that these ports are open in the firewall.

Check DFSR configuration:

Make sure that the DFSR configuration is consistent on all DCs.

Check the topology of the replication group to make sure it is correct.

Run the DFSR diagnostic tool:

Use the dfsrdiag command line tool to diagnose the problem.

dfsrdiag /testdfsintegrity can help you check the integrity of the SYSVOL folder.

dfsrdiag /testconnectivity can test connectivity between DCs.

Consider authoritative recovery:

If all else fails and you are sure that SYSVOL on DC2 or DC3 is up to date, you may consider running an authoritative recovery on DC2 or DC3.

However, before running an authoritative recovery, make sure that you have backed up all important GPO and SYSVOL data.

An authoritative recovery resets the replication state of the DFSR and forces the selected DC to be the authoritative source.

Avoid non-authoritative recovery:

Non-authoritative recovery is usually not recommended because it can lead to data loss or inconsistency.

Consider using non-authoritative recovery only when you are certain that there are no other options and you fully understand the possible risks and consequences.

Best regards

Neuvi
