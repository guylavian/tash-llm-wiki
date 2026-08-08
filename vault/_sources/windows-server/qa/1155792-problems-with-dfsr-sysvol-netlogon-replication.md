---
title: "Problems with DFSR SYSVOL, NETLOGON replication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1155792/problems-with-dfsr-sysvol-netlogon-replication
question_id: 1155792
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["Mvp"]
---
# Problems with DFSR SYSVOL, NETLOGON replication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1155792/problems-with-dfsr-sysvol-netlogon-replication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,    

I am having 2 DCs Windows 2016 with DFSR replication type. I am having a dillemma. I do not know which of the DCs is at fault....    

DC-001 that holds FSMO roles throws the following errors:    

```
Starting test: FrsEvent  

     * The File Replication Service Event log test   
     Skip the test because the server is running DFSR.  

     ......................... DC-001 passed test FrsEvent
```

Starting test: DFSREvent    

```
The DFS Replication Event Log.   
     There are warning or error events within the last 24 hours after the SYSVOL has been shared.  Failing SYSVOL  

     replication problems may cause Group Policy problems.   
     A warning event occurred.  EventID: 0x80001396  

        Time Generated: 01/04/2023   20:34:34  

        Event String:  

        The DFS Replication service is stopping communication with partner DC-000 for replication group Domain System Volume due to an error. The service will retry the connection periodically.   

           

        Additional Information:   

        Error: 9033 (The request was cancelled by a shutdown)   

        Connection ID: D8098552-5382-4E6B-9107-4AA61EC2F9A0   

        Replication Group ID: 2A016BE6-ACDC-4A11-9B2A-8D96BC15495D  

     A warning event occurred.  EventID: 0x80001396  

        Time Generated: 01/04/2023   20:49:04  

        Event String:  

        The DFS Replication service is stopping communication with partner DC-000 for replication group Domain System Volume due to an error. The service will retry the connection periodically.   

           

        Additional Information:   

        Error: 9033 (The request was cancelled by a shutdown)   

        Connection ID: D8098552-5382-4E6B-9107-4AA61EC2F9A0   

        Replication Group ID: 2A016BE6-ACDC-4A11-9B2A-8D96BC15495D  

     An error event occurred.  EventID: 0xC000138A  

        Time Generated: 01/04/2023   20:49:38  

        Event String:  

        The DFS Replication service encountered an error communicating with partner DC-000 for replication group Domain System Volume.
```

======================================================================    

Second DC-000 is throwing another error:    

```
Starting test: FrsEvent  

     * The File Replication Service Event log test   
     Skip the test because the server is running DFSR.  

     ......................... DC-000 passed test FrsEvent  

  Starting test: DFSREvent  

     The DFS Replication Event Log.   
     There are warning or error events within the last 24 hours after the SYSVOL has been shared.  Failing SYSVOL  

     replication problems may cause Group Policy problems.   
     A warning event occurred.  EventID: 0x800008A5  

        Time Generated: 01/04/2023   20:34:41  

        Event String:  

        The DFS Replication service stopped replication on volume C:. This occurs when a DFSR JET database is not shut down cleanly and Auto Recovery is disabled. To resolve this issue, back up the files in the affected replicated folders, and then use the ResumeReplication WMI method to resume replication.   

           

        Additional Information:   

        Volume: C:   

        GUID: 14B12066-B2F6-11E4-93EB-806E6F6E6963   

           

        Recovery Steps   

        1. Back up the files in all replicated folders on the volume. Failure to do so may result in data loss due to unexpected conflict resolution during the recovery of the replicated folders.   

        2. To resume the replication for this volume, use the WMI method ResumeReplication of the DfsrVolumeConfig class. For example, from an elevated command prompt, type the following command:   

        wmic /namespace:\\root\microsoftdfs path dfsrVolumeConfig where volumeGuid="14B12066-B2F6-11E4-93EB-806E6F6E6963" call ResumeReplication   

           

        For more information, see http://support.microsoft.com/kb/2663685.  

     A warning event occurred.  EventID: 0x800008A5
```

==============================================================================================================================    

Please what to do .... I was thinking to demote one of them. I just do not know which on is at fault ?    

Thanks in advance,    

Andy

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2023-01-08*

Please run;    

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log` 	(run on PDC emulator)    

`repadmin /showrepl >C:\repl.txt` 					(run on any domain controller)    

`ipconfig /all > C:\%computername%.txt` 						(run on EVERY domain controller)    

Also check the domain controller System and Replication (DFS or FRS) event logs for errors since last boot. Post the Event Source and Event IDs of any found. (no evtx files)    

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-08*

Hi Patrik,    

Thank you for helping on this one.    

I changed MaxOfflineTimeInDays from default value 60 to 200 days. Restarted newly promoted domain controller and Replication picked it up. Everything is ok now,.    

Thanks for your help!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-08*

Patrick thank you for answering,    

Development:    

DC-001 is our primary (FSMO) DC.     

I decided to demote Dc-000 as domain controller.     

Reinstalled last domain controller in question. After promoting DC-000 the SYSvolS are not even created. There is no replication from our main DC-001 to DC-000.     

Finally I generated the logs as per your request:    

https://ourvolaris-my.sharepoint.com/:f:/g/personal/andy_baravi_portfolioplus_com/Eloz6Xuh3yFNqBYVJMh8Ro4BnklZ6hFGW0J1V9EosZ-7tA?e=QyZNaa
