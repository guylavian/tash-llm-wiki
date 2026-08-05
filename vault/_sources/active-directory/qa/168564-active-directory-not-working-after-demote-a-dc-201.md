---
title: "active directory not working after demote a dc 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/168564/active-directory-not-working-after-demote-a-dc-201
question_id: 168564
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# active directory not working after demote a dc 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/168564/active-directory-not-working-after-demote-a-dc-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a big problem!!!  

I have 2 Domain controllers on 2016 STD Servers. I transfer all the roles from DC1 to DC2 and i demote DC1. Now DC2 don't work correcly. Active directory tools don't work. Can you help me please???

DC1 => ARTHRO-DC1  

DC2 => ARTHRO-SQL

C:\Windows\system32>dcdiag

Directory Server Diagnosis

Performing initial setup:  

Trying to find home server...  

Home Server = arthro-sql  

* Identified AD Forest.  

Done gathering initial info.

Doing initial required tests

Testing server: Default-First-Site-Name\ARTHRO-SQL  

Starting test: Connectivity  

......................... ARTHRO-SQL passed test Connectivity

Doing primary tests

Testing server: Default-First-Site-Name\ARTHRO-SQL  

Starting test: Advertising  

Fatal Error:DsGetDcName (ARTHRO-SQL) call failed, error 1355  

The Locator could not find the server.  

......................... ARTHRO-SQL failed test Advertising  

Starting test: FrsEvent  

......................... ARTHRO-SQL passed test FrsEvent  

Starting test: DFSREvent  

There are warning or error events within the last 24 hours after the SYSVOL has been shared. Failing SYSVOL replication problems may cause Group Policy problems.  

......................... ARTHRO-SQL failed test DFSREvent  

Starting test: SysVolCheck  

......................... ARTHRO-SQL passed test SysVolCheck  

Starting test: KccEvent  

An error event occurred. EventID: 0xC0000466  

Time Generated: 11/19/2020 13:03:07  

Event String: Active Directory Domain Services was unable to establish a connection with the global catalog.  

A warning event occurred. EventID: 0x8000082C  

Time Generated: 11/19/2020 13:04:08  

Event String:  

......................... ARTHRO-SQL failed test KccEvent  

Starting test: KnowsOfRoleHolders  

......................... ARTHRO-SQL passed test KnowsOfRoleHolders  

Starting test: MachineAccount  

......................... ARTHRO-SQL passed test MachineAccount  

Starting test: NCSecDesc  

......................... ARTHRO-SQL passed test NCSecDesc  

Starting test: NetLogons  

Unable to connect to the NETLOGON share! (\ARTHRO-SQL\netlogon)  

[ARTHRO-SQL] An net use or LsaPolicy operation failed with error 67, The network name cannot be found..  

......................... ARTHRO-SQL failed test NetLogons  

Starting test: ObjectsReplicated  

......................... ARTHRO-SQL passed test ObjectsReplicated  

Starting test: Replications  

[Replications Check,ARTHRO-SQL] A recent replication attempt failed:  

From ARTHRO-DC1 to ARTHRO-SQL  

Naming Context: DC=DomainDnsZones,DC=arthromed,DC=local  

The replication generated an error (1256):  

The remote system is not available. For information about network troubleshooting, see Windows Help.  

The failure occurred at 2020-11-19 12:48:49.  

The last success occurred at 2020-11-18 15:59:13.  

23 failures have occurred since the last success.

C:\Windows\system32>repadmin /showrepl

Repadmin: running command /showrepl against full DC localhost  

Default-First-Site-Name\ARTHRO-SQL  

DSA Options: IS_GC  

Site Options: (none)  

DSA object GUID: 9d598d6a-4914-495b-932c-1a63c2a0baf4  

DSA invocationID: 96228654-fe48-4304-b9f0-272174e9e329

==== INBOUND NEIGHBORS ======================================

DC=arthromed,DC=local  

Default-First-Site-Name\ARTHRO-DC1 via RPC  

DSA object GUID: ddef38f7-946d-4c3d-b7e3-b9a40ae33482  

Last attempt @ 2020-11-19 12:48:49 failed, result 1722 (0x6ba):  

The RPC server is unavailable.  

23 consecutive failure(s).  

Last success @ 2020-11-18 15:59:22.

CN=Configuration,DC=arthromed,DC=local  

Default-First-Site-Name\ARTHRO-DC1 via RPC  

DSA object GUID: ddef38f7-946d-4c3d-b7e3-b9a40ae33482  

Last attempt @ 2020-11-19 12:49:32 failed, result 1722 (0x6ba):  

The RPC server is unavailable.  

23 consecutive failure(s).  

Last success @ 2020-11-18 15:59:13.

CN=Schema,CN=Configuration,DC=arthromed,DC=local  

Default-First-Site-Name\ARTHRO-DC1 via RPC  

DSA object GUID: ddef38f7-946d-4c3d-b7e3-b9a40ae33482  

Last attempt @ 2020-11-19 12:50:14 failed, result 1722 (0x6ba):  

The RPC server is unavailable.  

23 consecutive failure(s).  

Last success @ 2020-11-18 15:59:13.

DC=ForestDnsZones,DC=arthromed,DC=local  

Default-First-Site-Name\ARTHRO-DC1 via RPC  

DSA object GUID: ddef38f7-946d-4c3d-b7e3-b9a40ae33482  

Last attempt @ 2020-11-19 12:48:49 failed, result 1256 (0x4e8):  

The remote system is not available. For information about network troubleshooting, see Windows Help.  

23 consecutive failure(s).  

Last success @ 2020-11-18 15:59:13.

DC=DomainDnsZones,DC=arthromed,DC=local  

Default-First-Site-Name\ARTHRO-DC1 via RPC  

DSA object GUID: ddef38f7-946d-4c3d-b7e3-b9a40ae33482  

Last attempt @ 2020-11-19 12:48:49 failed, result 1256 (0x4e8):  

The remote system is not available. For information about network troubleshooting, see Windows Help.  

23 consecutive failure(s).  

Last success @ 2020-11-18 15:59:13.

Source: Default-First-Site-Name\ARTHRO-DC1  

******* 23 CONSECUTIVE FAILURES since 2020-11-18 15:59:22  

Last error: 1256 (0x4e8):  

The remote system is not available. For information about network troubleshooting, see Windows Help.

C:\Windows\system32>dcdiag /fix

Directory Server Diagnosis

Performing initial setup:  

Trying to find home server...  

Home Server = arthro-sql  

* Identified AD Forest.  

Done gathering initial info.

Doing initial required tests

Testing server: Default-First-Site-Name\ARTHRO-SQL  

Starting test: Connectivity  

......................... ARTHRO-SQL passed test Connectivity

Doing primary tests

Testing server: Default-First-Site-Name\ARTHRO-SQL  

Starting test: Advertising  

Fatal Error:DsGetDcName (ARTHRO-SQL) call failed, error 1355  

The Locator could not find the server.  

......................... ARTHRO-SQL failed test Advertising  

Starting test: FrsEvent  

......................... ARTHRO-SQL passed test FrsEvent  

Starting test: DFSREvent  

There are warning or error events within the last 24 hours after the SYSVOL has been shared. Failing SYSVOL replication problems may cause Group Policy problems.  

......................... ARTHRO-SQL failed test DFSREvent  

Starting test: SysVolCheck  

......................... ARTHRO-SQL passed test SysVolCheck  

Starting test: KccEvent  

A warning event occurred. EventID: 0x8000082C  

Time Generated: 11/19/2020 15:04:08  

Event String:  

......................... ARTHRO-SQL passed test KccEvent  

Starting test: KnowsOfRoleHolders  

......................... ARTHRO-SQL passed test KnowsOfRoleHolders  

Starting test: MachineAccount  

......................... ARTHRO-SQL passed test MachineAccount  

Starting test: NCSecDesc  

......................... ARTHRO-SQL passed test NCSecDesc  

Starting test: NetLogons  

Unable to connect to the NETLOGON share! (\ARTHRO-SQL\netlogon)  

[ARTHRO-SQL] An net use or LsaPolicy operation failed with error 67, The network name cannot be found..  

......................... ARTHRO-SQL failed test NetLogons  

Starting test: ObjectsReplicated  

......................... ARTHRO-SQL passed test ObjectsReplicated  

Starting test: Replications  

[Replications Check,ARTHRO-SQL] A recent replication attempt failed:  

From ARTHRO-DC1 to ARTHRO-SQL  

Naming Context: DC=DomainDnsZones,DC=arthromed,DC=local  

The replication generated an error (1256):  

The remote system is not available. For information about network troubleshooting, see Windows Help.  

The failure occurred at 2020-11-19 14:48:50.  

The last success occurred at 2020-11-18 15:59:13.  

25 failures have occurred since the last success.  

[ARTHRO-DC1] DsBindWithSpnEx() failed with error 1722,  

The RPC server is unavailable..  

[Replications Check,ARTHRO-SQL] A recent replication attempt failed:  

From ARTHRO-DC1 to ARTHRO-SQL  

Naming Context: DC=ForestDnsZones,DC=arthromed,DC=local  

The replication generated an error (1256):  

The remote system is not available. For information about network troubleshooting, see Windows Help.  

The failure occurred at 2020-11-19 14:48:50.  

The last success occurred at 2020-11-18 15:59:13.  

25 failures have occurred since the last success.  

[Replications Check,ARTHRO-SQL] A recent replication attempt failed:  

From ARTHRO-DC1 to ARTHRO-SQL  

Naming Context: CN=Schema,CN=Configuration,DC=arthromed,DC=local  

The replication generated an error (1722):  

The RPC server is unavailable.  

The failure occurred at 2020-11-19 14:49:32.  

The last success occurred at 2020-11-18 15:59:13.  

25 failures have occurred since the last success.  

The source remains down. Please check the machine.  

[Replications Check,ARTHRO-SQL] A recent replication attempt failed:  

From ARTHRO-DC1 to ARTHRO-SQL  

Naming Context: CN=Configuration,DC=arthromed,DC=local  

The replication generated an error (1722):  

The RPC server is unavailable.  

The failure occurred at 2020-11-19 14:48:50.  

The last success occurred at 2020-11-18 15:59:13.  

25 failures have occurred since the last success.  

The source remains down. Please check the machine.  

[Replications Check,ARTHRO-SQL] A recent replication attempt failed:  

From ARTHRO-DC1 to ARTHRO-SQL  

Naming Context: DC=arthromed,DC=local  

The replication generated an error (1722):  

The RPC server is unavailable.  

The failure occurred at 2020-11-19 14:50:14.  

The last success occurred at 2020-11-18 15:59:22.  

25 failures have occurred since the last success.  

The source remains down. Please check the machine.  

......................... ARTHRO-SQL failed test Replications  

Starting test: RidManager  

......................... ARTHRO-SQL passed test RidManager  

Starting test: Services  

......................... ARTHRO-SQL passed test Services  

Starting test: SystemLog  

An error event occurred. EventID: 0xC00038D6  

Time Generated: 11/19/2020 14:27:05  

Event String: The DFS Namespace service could not initialize cross forest trust information on this domain controller, but it will periodically retry the operation. The return code is in the record data.  

......................... ARTHRO-SQL failed test SystemLog  

Starting test: VerifyReferences  

......................... ARTHRO-SQL passed test VerifyReferences

Running partition tests on : DomainDnsZones  

Starting test: CheckSDRefDom  

......................... DomainDnsZones passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... DomainDnsZones passed test CrossRefValidation

Running partition tests on : ForestDnsZones  

Starting test: CheckSDRefDom  

......................... ForestDnsZones passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... ForestDnsZones passed test CrossRefValidation

Running partition tests on : Schema  

Starting test: CheckSDRefDom  

......................... Schema passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... Schema passed test CrossRefValidation

Running partition tests on : Configuration  

Starting test: CheckSDRefDom  

......................... Configuration passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... Configuration passed test CrossRefValidation

Running partition tests on : arthromed  

Starting test: CheckSDRefDom  

......................... arthromed passed test CheckSDRefDom  

Starting test: CrossRefValidation  

......................... arthromed passed test CrossRefValidation

Running enterprise tests on : arthromed.local  

Starting test: LocatorCheck  

Warning: DcGetDcName(GC_SERVER_REQUIRED) call failed, error 1355  

A Global Catalog Server could not be located - All GC's are down.  

Warning: DcGetDcName(TIME_SERVER) call failed, error 1355  

A Time Server could not be located.  

The server holding the PDC role is down.  

Warning: DcGetDcName(GOOD_TIME_SERVER_PREFERRED) call failed, error 1355  

A Good Time Server could not be located.  

Warning: DcGetDcName(KDC_REQUIRED) call failed, error 1355  

A KDC could not be located - All the KDCs are down.  

......................... arthromed.local failed test LocatorCheck  

Starting test: Intersite  

......................... arthromed.local passed test Intersite

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-19*

Log Name: Directory Service  

Source: Microsoft-Windows-ActiveDirectory_DomainService  

Date: 19/11/2020 4:04:08 μμ  

Event ID: 2092  

Task Category: Replication  

Level: Warning  

Keywords: Classic  

User: ANONYMOUS LOGON  

Computer: arthro-sql.arthromed.local  

Description:

This server is the owner of the following FSMO role, but does not consider it valid. For the partition which contains the FSMO, this server has not replicated successfully with any of its partners since this server has been restarted. Replication errors are preventing validation of this role.

Operations which require contacting a FSMO operation master will fail until this condition is corrected.

FSMO Role: DC=arthromed,DC=local

User Action:

-   Initial synchronization is the first early replications done by a system as it is starting. A failure to initially synchronize may explain why a FSMO role cannot be validated. This process is explained in KB article 305476.

-   This server has one or more replication partners, and replication is failing for all of these partners. Use the command repadmin /showrepl to display the replication errors. Correct the error in question. For example there maybe problems with IP connectivity, DNS name resolution, or security authentication that are preventing successful replication.

-   In the rare event that all replication partners are expected to be offline (for example, because of maintenance or disaster recovery), you can force the role to be validated. This can be done by using NTDSUTIL.EXE to seize the role to the same server. This may be done using the steps provided in KB articles 255504 and 324801 on http://support.microsoft.com.

The following operations may be impacted:  

Schema: You will no longer be able to modify the schema for this forest.  

Domain Naming: You will no longer be able to add or remove domains from this forest.  

PDC: You will no longer be able to perform primary domain controller operations, such as Group Policy updates and password resets for non-Active Directory Domain Services accounts.  

RID: You will not be able to allocation new security identifiers for new user accounts, computer accounts or security groups.  

Infrastructure: Cross-domain name references, such as universal group memberships, will not be updated properly if their target object is moved or renamed.  

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

<System>  

<Provider Name="Microsoft-Windows-ActiveDirectory_DomainService" Guid="{0e8478c5-3605-4e8c-8497-1e730c959516}" EventSourceName="NTDS General" />  

<EventID Qualifiers="32768">2092</EventID>  

<Version>0</Version>  

<Level>3</Level>  

<Task>5</Task>  

<Opcode>0</Opcode>  

<Keywords>0x8080000000000000</Keywords>  

<TimeCreated SystemTime="2020-11-19T14:04:08.069520600Z" />  

<EventRecordID>2181</EventRecordID>  

<Correlation />  

<Execution ProcessID="1404" ThreadID="13528" />  

<Channel>Directory Service</Channel>  

<Computer>arthro-sql.arthromed.local</Computer>  

<Security UserID="S-1-5-7" />  

</System>  

<EventData>  

<Data>DC=arthromed,DC=local</Data>  

</EventData>  

</Event>

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-19*

Log Name: Directory Service  

Source: Microsoft-Windows-ActiveDirectory_DomainService  

Date: 19/11/2020 4:03:07 μμ  

Event ID: 1126  

Task Category: Global Catalog  

Level: Error  

Keywords: Classic  

User: ANONYMOUS LOGON  

Computer: arthro-sql.arthromed.local  

Description:  

Active Directory Domain Services was unable to establish a connection with the global catalog.

Additional Data  

Error value:  

1355 The specified domain either does not exist or could not be contacted.  

Internal ID:  

3201395

User Action:  

Make sure a global catalog is available in the forest, and is reachable from this domain controller. You may use the nltest utility to diagnose this problem.  

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

<System>  

<Provider Name="Microsoft-Windows-ActiveDirectory_DomainService" Guid="{0e8478c5-3605-4e8c-8497-1e730c959516}" EventSourceName="NTDS General" />  

<EventID Qualifiers="49152">1126</EventID>  

<Version>0</Version>  

<Level>2</Level>  

<Task>18</Task>  

<Opcode>0</Opcode>  

<Keywords>0x8080000000000000</Keywords>  

<TimeCreated SystemTime="2020-11-19T14:03:07.599300000Z" />  

<EventRecordID>2180</EventRecordID>  

<Correlation />  

<Execution ProcessID="1404" ThreadID="13528" />  

<Channel>Directory Service</Channel>  

<Computer>arthro-sql.arthromed.local</Computer>  

<Security UserID="S-1-5-7" />  

</System>  

<EventData>  

<Data>3201395</Data>  

<Data>1355</Data>  

<Data>The specified domain either does not exist or could not be contacted.</Data>  

</EventData>  

</Event>

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-19*

can not understand what happened  

Might check the event logs for errors since last boot.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-19*

The DC1 is impossible to return.  

The roles are all in DC2 for many days....(netdom query fsmo)...i can not understand what happened so bad... :(

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-19*

Sounds like health was not good possibly before and certainly not after demotion. Might check the event logs for errors since last boot. May need to restore DC1 from a known good backup and start the migration over.  

--please don't forget to Accept as answer if the reply is helpful--
