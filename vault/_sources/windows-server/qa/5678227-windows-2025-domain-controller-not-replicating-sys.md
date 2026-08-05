---
title: "Windows 2025 Domain Controller not replicating sysvol"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5678227/windows-2025-domain-controller-not-replicating-sys
question_id: 5678227
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# Windows 2025 Domain Controller not replicating sysvol

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5678227/windows-2025-domain-controller-not-replicating-sys (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have a 3 Windows Domain 2025 Domain Controllers.  They are called CORP-DC1, CORP-DC2, and DAL-DC1.  The CORP ones are at our corporate office and the DAL-DC1 is in a remote location that we have an always on VPN tunnel to with the 2 networks (CORP-192.168.10.x and DAL-192.168.6.x) open to all traffic in the VPN.  CORP-DC1 is primary and CORP-DC2 is replicating fine.  DAL-DC1 has never replicated since being promoted.  I have tried Forcing authoritative DFS replication, I have renamed the C:\System Volume Information\DFSR and let it rebuild the DB on DAL-DC1.  I forced DFSR to use Port 5722 on all 3 DCs and verified connectivity from all 3 to each other.  The Windows Firewall is turned off on all 3 DCs too.  All 3 servers are also DNS servers.  DNS is replicating fine to DAL-DC1.  The sysvol and netlogon shares are there (but empty) on DAL-DC1.  I am not sure what else to do.  Every time I force replication the same thing occurs.  

I get this on CORP-DC1 in the event viewer.

Event ID: 5004

The DFS Replication service successfully established an inbound connection with partner DAL-DC1 for replication group Domain System Volume. 

 Additional Information: 

Connection Address Used: DAL-DC1.corp.revdat.com 

Connection ID: E305FB2A-865F-4233-A923-E1D510A04DF5 

Replication Group ID: E24AFD63-7F20-42B9-8EAA-D3B2D84C1CA1

On DAL-DC1 I get these in the event viewer.   

The DFS Replication service successfully set up an RPC listener for incoming replication requests. 

 Additional Information: 

Port: 5722  

The DFS Replication service has detected that at least one connection is configured for replication group Domain System Volume. 

Additional Information: 

Replication Group ID: E24AFD63-7F20-42B9-8EAA-D3B2D84C1CA1 

Member ID: F636B636-C4BD-4368-AB3A-A893A49E2EC6

After about 3-5 minutes I get these on DAL-DC1.  

Event ID: 5002

The DFS Replication service encountered an error communicating with partner CORP-DC1 for replication group Domain System Volume.  

Partner DNS address: CORP-DC1.corp.revdat.com 

 Optional data if available: 

Partner WINS Address: CORP-DC1 

Partner IP Address: 192.168.10.8  

The service will retry the connection periodically. 

 Additional Information: 

Error: 1726 (The remote procedure call failed.) 

Connection ID: 6D37BFF2-278E-490C-BC8A-540DAFBEB589 

Replication Group ID: E24AFD63-7F20-42B9-8EAA-D3B2D84C1CA1

Event ID: 4612  

The DFS Replication service initialized SYSVOL at local path C:\WINDOWS\SYSVOL\domain and is waiting to perform initial replication. The replicated folder will remain in the initial synchronization state until it has replicated with its partner CORP-DC1.corp.revdat.com. If the server was in the process of being promoted to a domain controller, the domain controller will not advertise and function as a domain controller until this issue is resolved. This can occur if the specified partner is also in the initial synchronization state, or if sharing violations are encountered on this server or the sync partner. If this event occurred during the migration of SYSVOL from File Replication service (FRS) to DFS Replication, changes will not replicate out until this issue is resolved. This can cause the SYSVOL folder on this server to become out of sync with other domain controllers. 

Additional Information: 

Replicated Folder Name: SYSVOL Share 

Replicated Folder ID: B28F17AF-4462-4FAD-A4F0-B0B151406A8D 

Replication Group Name: Domain System Volume 

Replication Group ID: 6D37BFF2-278E-490C-BC8A-540DAFBEB589 

Member ID: F636B636-C4BD-4368-AB3A-A893A49E2EC6 

Read-Only: 0

Any ideas would be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-12-23*

It seems that you are experiencing issues with DFS replication for the SYSVOL share on your DAL-DC1 domain controller. Here are some troubleshooting steps you can take based on the information provided:

-  Check Active Directory Replication: Ensure that Active Directory replication is functioning correctly between all domain controllers. You can use the `Repadmin.exe` tool to verify the replication status and identify any potential issues.

-  Review Event Logs: Look for any relevant errors in the Event Viewer on both CORP-DC1 and DAL-DC1. Specifically, check for replication-related events that may provide more insight into the communication errors.

-  Verify DNS Configuration: Since DNS is critical for domain controller communication, ensure that all domain controllers are correctly configured in DNS and can resolve each other's names. You can use `nslookup` to verify name resolution.

-  Check Firewall and Network Settings: Although you mentioned that the Windows Firewall is turned off, double-check any other network devices (like routers or firewalls) that might be blocking RPC traffic on port 5722. Ensure that the VPN tunnel is stable and properly configured.

-  Force Replication: You can try forcing replication using the `DFSRDIAG` tool to see if that resolves the issue. Use the command `dfsrdiag pollad` on DAL-DC1 to force it to poll Active Directory for changes.

-  Review DFS Replication Health: Use the `dfsdiag` command to check the health of the DFS replication service. This can help identify if there are any issues with the DFS replication setup.

-  Check SYSVOL Share Status: Ensure that the SYSVOL share is properly configured and accessible. You can manually check the share using `net share` command to confirm that it is shared correctly.

-  Reinitialize DFS Replication: If all else fails, you may need to consider reinitializing the DFS replication for the SYSVOL folder on DAL-DC1. Be cautious with this step as it may lead to data loss if not done correctly. Make sure to back up any important data before proceeding.

By following these steps, you should be able to identify and resolve the replication issues with your DAL-DC1 domain controller.

References:

-  How to troubleshoot missing SYSVOL and Netlogon shares

-  Troubleshoot missing SYSVOL and NETLOGON shares on Windows domain controllers
