---
title: "Domain controller not successfully promoting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163361/domain-controller-not-successfully-promoting
question_id: 1163361
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Domain controller not successfully promoting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163361/domain-controller-not-successfully-promoting (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a client with a single 2012 domain controller.  Trying to add a 2022 domain controller to the domain, SYSVOL is never shared.  In the DFS Replication log, I have warning events 6016, 4614, and 6804.

```
Log Name:      DFS Replication
Source:        DFSR
Date:          1/22/2023 3:16:13 PM
Event ID:      6016
Task Category: None
Level:         Warning
Keywords:      Classic
User:          N/A
Computer:      CO-DC22-01.XXXX.local
Description:
The DFS Replication service failed to update configuration in Active Directory Domain Services. The service will retry this operation periodically. 
 
Additional Information: 
Object Category: msDFSR-LocalSettings 
Object DN: CN=DFSR-LocalSettings,CN=CO-DC22-01,OU=Domain Controllers,DC=XXXX,DC=local 
Error: 2 (The system cannot find the file specified.) 
Domain Controller: co-dc.XXXX.local 
Polling Cycle: 60
Event Xml:

  
    
    6016
    0
    3
    0
    0
    0x80000000000000
    
    18
    
    
    DFS Replication
    CO-DC22-01.XXXX.local
    
  
  
    msDFSR-LocalSettings
    CN=DFSR-LocalSettings,CN=CO-DC22-01,OU=Domain Controllers,DC=XXXX,DC=local
    2
    The system cannot find the file specified.
    co-dc.XXXX.local
    60
  

```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-24*

Thank you.  The answer was actually quite clear in DCDiag.

```
Starting test: DFSREvent
         The DFS Replication Event Log. 
         There are warning or error events within the last 24 hours after the
         SYSVOL has been shared.  Failing SYSVOL replication problems may cause
         Group Policy problems. 
         A warning event occurred.  EventID: 0x800008A5
            Time Generated: 01/23/2023   10:31:16
            Event String:
            The DFS Replication service stopped replication on volume C:. This occurs when a DFSR JET database is not shut down cleanly and Auto Recovery is disabled. To resolve this issue, back up the files in the affected replicated folders, and then use the ResumeReplication WMI method to resume replication. 
             
            Additional Information: 
            Volume: C: 
            GUID: 8DBE48AB-923E-11E3-93E7-806E6F6E6963 
             
            Recovery Steps 
            1. Back up the files in all replicated folders on the volume. Failure to do so may result in data loss due to unexpected conflict resolution during the recovery of the replicated folders. 
            2. To resume the replication for this volume, use the WMI method ResumeReplication of the DfsrVolumeConfig class. For example, from an elevated command prompt, type the following command: 
            wmic /namespace:\\root\microsoftdfs path dfsrVolumeConfig where volumeGuid="8DBE48AB-923E-11E3-93E7-806E6F6E6963" call ResumeReplication
```

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-23*

Hi @Ryan Wilderman  

Check if the  DFSR port is not blocked between the 2 domain controllers.

If it's not the case, you can try one of the following solutions to reinitialise DFSR replication:

-  Force authoritative or non-authoritative synchronization for DFSR-replicated sysvol replication: How to force authoritative and non-authoritative synchronization for DFSR-replicated sysvol replication

-  Demote impacted domain controller 2022 and repromote it again 

Please don't forget to mark helpful answer as accepted
