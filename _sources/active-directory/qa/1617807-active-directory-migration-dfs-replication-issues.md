---
title: "Active Directory migration - DFS Replication Issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1617807/active-directory-migration-dfs-replication-issues
question_id: 1617807
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory migration - DFS Replication Issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1617807/active-directory-migration-dfs-replication-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

recently we have started with process of migration old domain controllers. I will try to explain the situation and steps I have already proceeded with.

Old DCs:

-  DC1 (main1): Windows Server 2012

-  DC2 (main2): Windows Server 2012 (FSMO roles)

Sysvol replication: DFSR

Newly added DCs:

-  DC3 (ad1): Windows Server 2022

-  DC4 (ad2): Windows Server 2022

Before promoting new DCs I have only checked status of synchronization repadmin /showrepl and dcdiag for DNS. Not the dcdiag against old DCs.

Note: We have only two testing group policy apllied in our domain.

After I have added new DCs, there were no SYSVOL and NETLOGON shares.

From dcdiag:  

-  Warning: DsGetDcName returned information for \MAIN2..., when we were trying to reach AD2.  SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE.

-  There are warning or error events within the last 24 hours after the SYSVOL has been shared.  Failing SYSVOL replication problems may cause Group Policy problems.

-  Unable to connect to the NETLOGON share! (\AD2\netlogon)  [AD2] An net use or LsaPolicy operation failed with error 67, The network name cannot be found..

In both DFS Replication Logs on new DCs was warning ID: 5014 

-  (The DFS Replication service is stopping communication with partner MAIN2/MAIN1 for replication group Domain System Volume due to an error).

So I have gone through this article: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares

And did force non-authotitative synchronization for DC3 and DC4. Unfortunately that did not help. 

Then I realized that I did not read the previous article properly and I found out that both old DC1 and DC2 had in DFS Replication logs (event ID 2213). 

This event was there for a long period of time. Every time, the backup with Windows Server Backup was made, it logged this ID 2213. 

So I have proceeded with recovery steps as it was stated in log. Firstly on DC2 (which holds FSMO roles). 

- wmic /namespace:\root\microsoftdfs path dfsrVolumeConfig where volumeGuid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" call ResumeReplication

Output returned value 0.

So I went check the logs and first there was warning Event ID 2212 and followed with Event ID 4012. 

-  This server has been disconnected from other partners for 650 days, which is longer than the time allowed by the MaxOfflineTimeInDays parameter (60).

After that I have tried to proceeded with recovery steps on DC1. 

- wmic /namespace:\root\microsoftdfs path dfsrVolumeConfig where volumeGuid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" call ResumeReplication

Checked the logs and ID 2012 was followed with ID 2214 (The DFS Replication service successfully recovered from an unexpected shutdown on volume C:.)

So I thought at least one SYSVOL recovered.

One SYSVOL recovered (main1), one disconected from partner for too long (main2), 2 new ones without SYSVOL and NETLOGON.

So I read through couple of articles and thought I should now proceed again with non-authotitative synchronization of DFSR-replicated SYSVOL.

So at the same time I have modified in ADSIEDIT the main2, ad1 and ad2 to be value  msDFSR-Enabled=FALSE.

Then forced replication on all three Domain Controllers with: repadmin /syncall /AeD

Then run: DFSRDIAG POLLAD

Change value back to msDFSR-Enabled=TRUE

Again forced on all three domain controllers replication: repadmin /syncall /AeD

Then run: DFSRDIAG POLLAD

On all three domain Controllers I saw in DFSR log: ID 4614 (The DFS Replication service initialized SYSVOL at local path C:\Windows\SYSVOL\domain and is waiting to perform initial replication), 

but after that, nothing happened. In article it says it should follow with ID 4604, but 4604 did not happened.

I have checked the DFSR Replication State and all 4 domain controllers are in state  2 = Initial Sync

I dont know what I can do now. Could someone please advice me, what should be next steps to make my new DC to have SYSVOL and NETLOGON? So I can then decomission old DCs?  

Thank you in advance for any advice.

Best Regards   

JU

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-26*

Hello guys,

finally resolved the issue.

Authoritatve restore for DC2 (FSMO) and non-authoritative restore for DC1.

This video https://www.youtube.com/watch?v=ja53C2Mz1EQ helped me a lot.

In official Microsoft documentation, the individual steps for authoritative restore are quite confusing.

So thank you all for any responses.

Best Regrads.

Jan Ulman

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-23*

Hi @Jan Ulman  

I already encountered sysvol and netlogon sharing issues after promoting the new domain controller. I fixed it via this registry key:

-  Login to your Domain Controller that’s having the issue

-  Open Regedit

-  Browse to: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters

-  Set SysVolReady from 0 to 1

-  Restart domain controller

Please don't forget to accept helpful answer

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-22*

Hello Daisy and community,

I have demoted new domain controllers DC3(ad1) Win2022 and DC4(ad2) Win2022 as you suggested.

I have checked SYSVOL type, and its DFSR. 

I have also run DCdiag on the old ones.

SYSVOL and NETLOGON is still not shared between DC1 (main1) and DC2 (main2).

I have checked the DFS Replication Event logs, and on both DC1 and DC2 there is still event warning: 5014

Followed by event ID: 5004

Replication state on both controllers is still 2 = initial Sync.

I have checked this article: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/distributed-file-system-replication-not-replicate-files

and checked the %systemroot%\debug\dfsr*.logs

DC2 (main2)

- 	[Error:1168(0x490) Config::RegReader::ReadSeedingSysVolConfigValues reg.h:453 7576 W Element not found.]

- 	[Error:1168(0x490) Config::RegReader::ReadSysVolConfigValues reg.cpp:1590 7576 W Element not found.]

- 	[Error:1168(0x490) Config::RegReader::ReadSysVolConfigValues reg.cpp:1460 7576 W Element not found.]

- 	[Error:9027(0x2343) InConnection::TransportEstablishSession inconnection.cpp:7701 7576 C A failure was reported by the remote partner]

- 	[Error:9027(0x2343) DownstreamTransport::EstablishSession downstreamtransport.cpp:4075 7576 C A failure was reported by the remote partner]

- 	[Error:9027(0x2343) DownstreamTransport::EstablishSession downstreamtransport.cpp:4054 7576 C A failure was reported by the remote partner]

- 	[Error:9051(0x235b) DownstreamTransport::EstablishSession downstreamtransport.cpp:4054 7576 C The content set is not ready]

DC1 (main1)

- 	[Error:1168(0x490) Config::RegReader::ReadSeedingSysVolConfigValues reg.h:453 3164 W Element not found.]

- 	[Error:1168(0x490) Config::RegReader::ReadSysVolConfigValues reg.cpp:1590 3164 W Element not found.]

- 	[Error:1168(0x490) Config::RegReader::ReadSysVolConfigValues reg.cpp:1460 3164 W Element not found.]

- 	[Error:9027(0x2343) InConnection::TransportEstablishSession inconnection.cpp:7701 3164 C A failure was reported by the remote partner]

- 	[Error:9027(0x2343) DownstreamTransport::EstablishSession downstreamtransport.cpp:4075 3164 C A failure was reported by the remote partner]

- 	[Error:9027(0x2343) DownstreamTransport::EstablishSession downstreamtransport.cpp:4054 3164 C A failure was reported by the remote partner]

- 	[Error:9051(0x235b) DownstreamTransport::EstablishSession downstreamtransport.cpp:4054 3164 C The content set is not ready]

Unfortunately both domain controllers have these errors in it.

We have experienced BSOD after update on the DC1(main1) several times in the past. Unfortunately we did not find the issue.

Before every update we had made full backup with windows server backup with full vss. Then created clone of the both DC1 and DC2.

After BSOD, we could not operate with DC1(main1) anymore, so we decided to use clone server for restore. Both DC1 and DC1 clone were disconected from network.

So we performed non-authoritative system state recovery on DC1(main1) clone, and after that we connected him to network.

Repadmin /showrepl and dcdiag on DNS looked good. 

dcdiag /v was probably not performed.

In the article above they recommend to contact Microsoft Support.

Has anybody experienced the same problem? 

What should we do? 

Thank you for any help.

Best Regards

Jan Ulman

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-18*

Hello Jan Ulman,  

Thank you for posting in Q&A forum.  

If you want to migrate the operating system of Domain Controller from 2012 to 2022, the minimum requirement to add one a domain controller of one of Windows Server 2022 is a Windows Server 2008 functional level. The domain also has to use DFS-R as the engine to replicate SYSVOL.  

Please ensure the functional level is at least Windows Server 2008.  

Here is my suggest for your reference:  

1.You can demote the newly added DCs if possible:

DC3 (ad1): Windows Server 2022 and DC4 (ad2): Windows Server 2022  

2.Try to check the AD replication between DC1 (main1): Windows Server 2012 and DC2 (main2): Windows Server 2012 (FSMO roles).  

3.Run Dcdiag /v on each DC to check the health of DC itself.  

4.Check if SYSVOL and Netlogon are shared.  

5.Check if SYSVOL type is DFSR.

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.

6.Check if SYSVOL replication works fine.  

If there is any issue about the six points, you can try to fix the issue.  

Ensure all the AD works fine, then you can add the new two DCs in this domain.

Note: You had better back up all domain controllers if there is no any recent backup about the old two DCs.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
