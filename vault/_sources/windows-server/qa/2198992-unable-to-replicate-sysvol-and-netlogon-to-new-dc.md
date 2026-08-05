---
title: "Unable to replicate SYSVOL and NETLOGON to new DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198992/unable-to-replicate-sysvol-and-netlogon-to-new-dc
question_id: 2198992
fetched: 2026-07-25
answer_count: 16
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Unable to replicate SYSVOL and NETLOGON to new DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198992/unable-to-replicate-sysvol-and-netlogon-to-new-dc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm in the process of replacing a server 2016 DC with a 2022 DC. 

Things went smoothly until replication - DFS replication. I'm unable to replicate the SYSVOL and NETLOGON correctly. I don't see any inbound/outbound connections when checking replication on the new DC. SYSVOL & NETLOGON do not replicate to the new DC. I've migrated many DCs in my time, but never struggled like this. It seems impossible to get a hold of someone from Microsoft to help troubleshoot. 

DFS replication is enabled on both servers. I'm getting a strange error on the primary DC with the FISMO role. 

"The DFS Replication service stopped replication on the folder with the following local path: C:\Windows\SYSVOL\domain. This server has been disconnected from other partners for 491 days, which is longer than the time allowed by the MaxOfflineTimeInDays parameter (60). DFS Replication considers the data in this folder to be stale, and this server will not replicate the folder until this error is corrected.

To resume replication of this folder, use the DFS Management snap  in to remove this server from the replication group, and then add it back to the group. This causes the server to perform an initial synchronization task, which repl es the stale data with fresh data from other members of the replication group."

I've tried that, but no luck.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-06*

Gidtom

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-06*

This is the current output in Event Viewer: (DC01)

The replication mode on the connection to partner DC1 has changed. 

Additional Information: 

Previous Replication Mode: Obey Configured Schedule 

Current Replication Mode: Replicate Now 

Current Bandwidth Usage:  Full 

Duration, in minutes, for current mode: 15 

Connection ID: A76EA691-36AB-47A1-94FC-5CB4380D9108 

Replication Group ID: Domain System Volume

However, I still cannot see the Sysvol or Netlogon shares on the new DC, which is DC1.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-06*

In Active Directory Sites and Services, I do still see Azure listed there, with NTDS settings. 

Should I delete it?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-06*

Thanks for your reply. 

Yes, only 1 2016 DC, I did have a backup in Azure for a while, but removed it. 

I am not able to see the Sysvol or Netlogon shares on the new DC. 

I did change the Max Offline time setting as suggested. 

Output:

Repadmin: running command /showrepl against full DC localhost  

Default-First-Site-Name\DC01  

DSA Options: IS_GC   

Site Options: (none)  

DSA object GUID: f038dd09-b33a-4ca4-9b93-0876aa60af51  

DSA invocationID: f038dd09-b33a-4ca4-9b93-0876aa60af51  

==== INBOUND NEIGHBORS ======================================  

DC=Schenckfoods,DC=local  

```
Default-First-Site-Name\DC1 via RPC  

    DSA object GUID: 828c5106-55e9-4c78-89b6-c1c4c42adff0  

    Last attempt @ 2024-12-06 11:54:09 was successful.
```

CN=Configuration,DC=Schenckfoods,DC=local  

```
Default-First-Site-Name\DC1 via RPC  

    DSA object GUID: 828c5106-55e9-4c78-89b6-c1c4c42adff0  

    Last attempt @ 2024-12-06 11:54:09 was successful.
```

CN=Schema,CN=Configuration,DC=Schenckfoods,DC=local  

```
Default-First-Site-Name\DC1 via RPC  

    DSA object GUID: 828c5106-55e9-4c78-89b6-c1c4c42adff0  

    Last attempt @ 2024-12-06 11:54:09 was successful.
```

DC=DomainDnsZones,DC=Schenckfoods,DC=local  

```
Default-First-Site-Name\DC1 via RPC  

    DSA object GUID: 828c5106-55e9-4c78-89b6-c1c4c42adff0  

    Last attempt @ 2024-12-06 11:54:09 was successful.
```

DC=ForestDnsZones,DC=Schenckfoods,DC=local  

```
Default-First-Site-Name\DC1 via RPC  

    DSA object GUID: 828c5106-55e9-4c78-89b6-c1c4c42adff0  

    Last attempt @ 2024-12-06 11:54:09 was successful.
```

Replication Summary Start Time: 2024-12-06 12:09:43  

Beginning data collection for replication summary, this may take awhile:  

  .....  

Source DSA          largest delta    fails/total %%   error  

 DC01                      18m:33s    0 /   5    0    

 DC1                       15m:34s    0 /   5    0    

Destination DSA     largest delta    fails/total %%   error  

 DC01                      15m:34s    0 /   5    0    

 DC1                       18m:33s    0 /   5    0  

However, I was seeing this before. What I could not see was any inbound/outbound connections for replication. 

I made the change above to max days and rebooted the server. I'll report back. Thanks again!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-06*

Hello Jason Seibert2,  

Thank you for posting in Microsoft Community forum.

1.Please check if you can see SYSVOL and Netlogon share on new DC, please run the net share on the new DC to check. We should see SYSVOL and Netlogon are shared:

2.Do you have only one 2016 DC before you add this new 2022 DC in this domain?  

-  Please check the AD replication between DCs in the domain. Please run commands below on PDC.

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv

-  If all the results after running the commands are OK, it seems AD replication is OK.  

Then you can check the SYSVOL replication. 

Please try to change MaxOfflineTimeInDays from default value 60 to 492 days. For more information, please read two similar threads below.

Here are two similar threads for your reference.

Problems with DFSR SYSVOL, NETLOGON replication - Microsoft Q&A

DFS Replication issue with event ID 4012 (windows server 2016 - Microsoft Q&A

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
