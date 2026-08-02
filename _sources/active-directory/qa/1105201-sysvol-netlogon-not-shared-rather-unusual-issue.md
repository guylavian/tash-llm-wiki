---
title: "Sysvol & Netlogon not shared - rather unusual issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1105201/sysvol-netlogon-not-shared-rather-unusual-issue
question_id: 1105201
fetched: 2026-07-25
answer_count: 12
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Sysvol & Netlogon not shared - rather unusual issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1105201/sysvol-netlogon-not-shared-rather-unusual-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all.    

We are facing a strange issue which was discovered recently, although I think it has been ongoing for sometime. Just that we didn't notice. No error was thrown up by the event manager.    

We have     

-  DC1 (Windows 2019)     

-  DC2 (Windows 2016)    

Both have been patched to the latest version.    

We attempted to promote DC2 server to a DC and everything was successful. However it seems that both sysvol and netlogon is missing on DC2.    

We did the usual - demote DC2 back to member and then promote it again. The issue still remains.    

DC1, the sysvol and netlogon shares can be seen and if we do an update on the group policy, it will be changed as well. Of course DC2 is still not showing anything.    

Any changes to the group policies done on DC1 will be reflected in DC2 and vice versa.    

We tested adding domain users on DC1 and it will be reflected in DC2 and vice versa as well.    

Here are the steps we did:    

-  repadmin /syncall -> everything is successful    

-  repdmin /showrepl on both DC1 & DC2 -> everything looks okay    

-  Did the both the non-authoritative and the authoritative synchronization for DFSR here: https://learn.microsoft.com/en-US/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization -> still no luck. When doing the steps, there was also no error.    

-  Checked the event logs again, there were no errors as well. However for DC1 & DC2, we never see a 4604 or a 4614 event for DFS Replication.    

 5. However when we do For /f %i IN ('dsquery server -o rdn') do @Echo   %i && @wmic /node:"%i" /namespace:\root\microsoftdfs path dfsrreplicatedfolderinfo WHERE replicatedfoldername='SYSVOL share' get replicationgroupname,replicatedfoldername,state -> it shows that DC1 as 'No Instance(s) available' while DC2 is at state 2.    

-  From here we troubleshoot and found that HKLM\System\CurrentControlSet\Services\DFSR\Parameters\StopReplicationOnAutoRecovery should be set to 0. However for our case, it is already 0.    

-  We checked, the DFSR service is running. The authoritative and non-authoritative synchronization steps had no errors.    

-  There looks like a solution which state to use this - wmic /namespace:\root\microsoftdfs path dfsrVolumeConfig where volumeGuid=" " call ResumeReplication -> However we do not have an error event that gives us the 'volumeGuid' that we need to run this.    

-  We did the DFS Replication Health Report -> Gave 2 warnings:-    

*One or more replicated folders are not replicating to this member because their memberships are disabled.      

  Affected replicated folders: SYSVOL Share     

  Description: The replicated folders listed above are not participating in replication because their memberships were manually disabled on this member. Event ID: 4114       

  Suggested action: If you want these replicated folders to participate in replication, enable the desired memberships using the DFS Management snap-in or the Dfsradmin.exe command-line tool.      

 Reference member returned no replicated folders.      

  Description: Backlog calculations cannot be performed because the reference member returned zero replicated folders.*      

Both seems to indicate us to use the authoritative and non-authoritative synchronization for DFRS method to resolve.    

So we are at our wits end now.    

Any help would be greatly appreciated.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-11-26*

ACESRV6 is multi-homed. Disable one of the adapters, a domain controller also cannot be DHCP assigned. Domain controller must have a static ip address and also list own static address for DNS on connection properties. After corrections then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service. I did not look at other files since this one is a showstopper. If problems persist then put up a new set of files to look at.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-26*

What's the current state in System and DFS Replication event logs? You commented some due to testing? Don't derail us, we only care about the active ones since last reboot. You could demote or otherwise just not even worry about DC2 until the problems are fixed with DC1 (2019)

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-26*

Hi,    

Just removed the multi-home adaptor. The DC1 itself now has one static IP address. And did the 3 steps as well. Restarted DC2 as well.    

But unfortunately the sysvol and netlogon still did not the appear. Not very sure what is causing the issue. But I think it is due to DC1.    

Wondering whether it is a good idea to demote and then promote DC1 in this case - as DC2 is still not yet properly configurated.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-26*

Hi,    

Thank you for your reply.    

---    

We are using DFSR and there does not seem to have any errors for the replication. Only warnings. And very likely because we were doing testing.    

Some errors were for the system. In the onedrive link.    

Again thank you for your help.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-26*

Please run;    

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log` 	(run on PDC emulator)    

`repadmin /showrepl >C:\repl.txt` 					(run on any domain controller)    

`ipconfig /all > C:\dc1.txt` 						(run on domain controller 1)    

`ipconfig /all > C:\dc2.txt` 						(run on domain controller 2 if exists)    

Also check the domain controller System and Replication (DFS or FRS) event logs for errors since last boot. Post the Event Source and Event IDs of any found. (no evtx files)    

then put `unzipped` text files up on OneDrive and share a link.
