---
title: "Group Policy error in all clients \"LDAP Bind function call failed\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/912002/group-policy-error-in-all-clients-ldap-bind-functi
question_id: 912002
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Group Policy error in all clients "LDAP Bind function call failed"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/912002/group-policy-error-in-all-clients-ldap-bind-functi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Support,     

due to some reason we restored complete image base restore for Primary and Secondary Domain controller but after restoration exchange server working fine but we are facing below issue and need your expert advise appreciate for your advise.    

1- When we do GP update in both domain controller so its fine but when we do on any clients we are getting below error     

"Computer policy could not be updated successfully. The following errors were encountered:    

The processing of Group Policy failed because of lack of network connectivity to a domain controller. This may be a transient condition. A success message would be generated once the machine gets connected to the domain controller and Group Policy has successfully processed. If you do not see a success message for several hours, then contact your administrator.    

User Policy could not be updated successfully. The following errors were encountered:    

The processing of Group Policy failed. Windows could not authenticate to the Active Directory service on a domain controller. (LDAP Bind function call failed). Look in the details tab for error code and description.    

To diagnose the failure, review the event log or run GPRESULT /H GPReport.html from the command line to access information about Group Policy results.    

The processing of Group Policy failed. Windows could not authenticate to the Active Directory service on a domain controller. (LDAP Bind function call failed). Look in the details tab for error code and description.    

Event 1006"     

2- Also we are facing issue with DFS server we are unable to access share by namespace but by normal share is fine.    

we observe that FRS is trying to reach to DR domain controller which is off now. so how can we force FRS to connect with Primary domain controller     

Note: we have total 4 domain controller out of DR 2 domain controller we shutdown. only kept 2 PDC and ADC is up and running.    

Please advise..    

Your prompt reply will be highly appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-06*

Have you reviewed the following link on troubleshooting FRS replication issues? What OS are your DC's?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-04*

Dear Support,

Please do find the AD logs, please note that AWS-DC and DR-DC is shut. I just want to make up AD01 and AD02 and FRS and Group policy should work...Apprecaited for Your valubale support

Directory Server Diagnosis

Performing initial setup:

   Trying to find home server...

-  Verifying that the local machine ad01, is a Directory Server. 
   Home Server = ad01

-  Connecting to directory service on server ad01.

-  Identified AD Forest. 
   Collecting AD specific global data 

-  Collecting site info.

   Calling ldap_search_init_page(hld,CN=Sites,CN=Configuration,DC=contoso,DC=com,LDAP_SCOPE_SUBTREE,(objectCategory=ntDSSiteSettings),.......
   The previous call succeeded 
   Iterating through the sites 
   Looking at base site object: CN=NTDS Site Settings,CN=DR-Site,CN=Sites,CN=Configuration,DC=contoso,DC=com
   Getting ISTG and options for the site
   Looking at base site object: CN=NTDS Site Settings,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com
   Getting ISTG and options for the site
   Looking at base site object: CN=NTDS Site Settings,CN=AWS-Site,CN=Sites,CN=Configuration,DC=contoso,DC=com
   Getting ISTG and options for the site

-  Identifying all servers.

   Calling ldap_search_init_page(hld,CN=Sites,CN=Configuration,DC=contoso,DC=com,LDAP_SCOPE_SUBTREE,(objectClass=ntDSDsa),.......
   The previous call succeeded....
   The previous call succeeded
   Iterating through the list of servers 
   Getting information for the server CN=NTDS Settings,CN=DR-DC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com 
   objectGuid obtained
   InvocationID obtained
   dnsHostname obtained
   site info obtained
   All the info for the server collected
   Getting information for the server CN=NTDS Settings,CN=AD01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com 
   objectGuid obtained
   InvocationID obtained
   dnsHostname obtained
   site info obtained
   All the info for the server collected
   Getting information for the server CN=NTDS Settings,CN=AD02,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com 
   objectGuid obtained
   InvocationID obtained
   dnsHostname obtained
   site info obtained
   All the info for the server collected
   Getting information for the server CN=NTDS Settings,CN=AWS-DC,CN=Servers,CN=AWS-Site,CN=Sites,CN=Configuration,DC=contoso,DC=com 
   objectGuid obtained
   InvocationID obtained
   dnsHostname obtained
   site info obtained
   All the info for the server collected

-  Identifying all NC cross-refs.

   Ldap search capability attribute search failed on server DR-DC, return

   value = 81
   Got error while checking if the DC is using FRS or DFSR. Error:

   Win32 Error 81The VerifyReferences, FrsEvent and DfsrEvent tests might fail

   because of this error. 

   Ldap search capability attribute search failed on server AWS-DC,

   return value = 81
   Got error while checking if the DC is using FRS or DFSR. Error:

   Win32 Error 81The VerifyReferences, FrsEvent and DfsrEvent tests might fail

   because of this error. 

-  Found 4 DC(s). Testing 4 of them.

   Done gathering initial info.

Doing initial required tests

   Testing server: Default-First-Site-Name\DR-DC

```
Starting test: Connectivity

     * Active Directory LDAP Services Check
     Server DR-DC resolved to these IP addresses: 172.20.21.201, but

     none of the addresses could be reached (pinged). Please check the

     network.

     Error: 0x2b02 "Error due to lack of resources."

     This error more often means that the targeted server is shutdown or

     disconnected from the network.

     Got error while checking LDAP and RPC connectivity. Please check your

     firewall settings.

     ......................... DR-DC failed test Connectivity
```

   Testing server: Default-First-Site-Name\AD01

```
Starting test: Connectivity

     * Active Directory LDAP Services Check
     Determining IP4 connectivity 
     * Active Directory RPC Services Check
     ......................... AD01 passed test Connectivity
```

   Testing server: Default-First-Site-Name\AD02

```
Starting test: Connectivity

     * Active Directory LDAP Services Check
     Determining IP4 connectivity 
     * Active Directory RPC Services Check
     ......................... AD02 passed test Connectivity
```

   Testing server: AWS-Site\AWS-DC

```
Starting test: Connectivity

     * Active Directory LDAP Services Check
     Server AWS-DC resolved to these IP addresses: 172.40.3.26, but

     none of the addresses could be reached (pinged). Please check the

     network.

     Error: 0x2b02 "Error due to lack of resources."

     This error more often means that the targeted server is shutdown or

     disconnected from the network.

     Got error while checking LDAP and RPC connectivity. Please check your

     firewall settings.

     ......................... AWS-DC failed test Connectivity
```

Doing primary tests

   Testing server: Default-First-Site-Name\DR-DC

```
Skipping all tests, because server DR-DC is not responding to

  directory service requests.

  Test omitted by user request: Advertising

  Test omitted by user request: CheckSecurityError

  Test omitted by user request: CutoffServers

  Test omitted by user request: FrsEvent

  Test omitted by user request: DFSREvent

  Test omitted by user request: SysVolCheck

  Test omitted by user request: KccEvent

  Test omitted by user request: KnowsOfRoleHolders

  Test omitted by user request: MachineAccount

  Test omitted by user request: NCSecDesc

  Test omitted by user request: NetLogons

  Test omitted by user request: ObjectsReplicated

  Test omitted by user request: OutboundSecureChannels

  Test omitted by user request: Replications

  Test omitted by user request: RidManager

  Test omitted by user request: Services

  Test omitted by user request: SystemLog

  Test omitted by user request: Topology

  Test omitted by user request: VerifyEnterpriseReferences

  Test omitted by user request: VerifyReferences

  Test omitted by user request: VerifyReplicas
```

   Testing server: Default-First-Site-Name\AD01

```
Starting test: Advertising

     The DC AD01 is advertising itself as a DC and having a DS.
     The DC AD01 is advertising as an LDAP server
     The DC AD01 is advertising as having a writeable directory
     The DC AD01 is advertising as a Key Distribution Center
     The DC AD01 is advertising as a time server
     The DS AD01 is advertising as a GC.
     ......................... AD01 passed test Advertising

  Test omitted by user request: CheckSecurityError

  Test omitted by user request: CutoffServers

  Starting test: FrsEvent

     * The File Replication Service Event log test 
     There are warning or error events within the last 24 hours after the

     SYSVOL has been shared.  Failing SYSVOL replication problems may cause

     Group Policy problems. 
     A warning event occurred.  EventID: 0x800034C4

        Time Generated: 07/03/2022   22:13:34

        Event String:

        The File Replication Service is having trouble enabling replication from DR-DC to AD01 for c:\windows\sysvol\domain using the DNS name dr-DC.contoso.com. FRS will keep retrying. 

         Following are some of the reasons you would see this warning. 

         

         [1] FRS can not correctly resolve the DNS name dr-DC.contoso.com from this computer. 

         [2] FRS is not running on dr-DC.contoso.com. 

         [3] The topology information in the Active Directory Domain Services for this replica has not yet replicated to all the Domain Controllers. 

         

         This event log message will appear once per connection, After the problem is fixed you will see another event log message indicating that the connection has been established.

     A warning event occurred.  EventID: 0x800034C4

        Time Generated: 07/03/2022   23:54:33

        Event String:

        The File Replication Service is having trouble enabling replication from AWS-DC to AD01 for c:\windows\sysvol\domain using the DNS name AWS-DC.contoso.com. FRS will keep retrying. 

         Following are some of the reasons you would see this warning. 

         

         [1] FRS can not correctly resolve the DNS name AWS-DC.contoso.com from this computer. 

         [2] FRS is not running on AWS-DC.contoso.com. 

         [3] The topology information in the Active Directory Domain Services for this replica has not yet replicated to all the Domain Controllers. 

         

         This event log message will appear once per connection, After the problem is fixed you will see another event log message indicating that the connection has been established.

     ......................... AD01 passed test FrsEvent

  Starting test: DFSREvent

     The DFS Replication Event Log. 
     Skip the test because the server is running FRS.

     ......................... AD01 passed test DFSREvent

  Starting test: SysVolCheck

     * The File Replication Service SYSVOL ready test 
     File Replication Service's SYSVOL is ready 
     ......................... AD01 passed test SysVolCheck

  Starting test: KccEvent

     * The KCC Event log test
     Found no KCC errors in "Directory Service" Event log in the last 15 minutes.
     ......................... AD01 passed test KccEvent

  Starting test: KnowsOfRoleHolders

     Role Schema Owner = CN=NTDS Settings,CN=AD01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com
     Role Domain Owner = CN=NTDS Settings,CN=AD01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com
     Role PDC Owner = CN=NTDS Settings,CN=AD01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com
     Role Rid Owner = CN=NTDS Settings,CN=AD01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com
     Role Infrastructure Update Owner = CN=NTDS Settings,CN=AD01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com
     ......................... AD01 passed test KnowsOfRoleHolders

  Starting test: MachineAccount

     Checking machine account for DC AD01 on DC AD01.
     * SPN found :LDAP/ad01.contoso.com/contoso.com
     * SPN found :LDAP/ad01.contoso.com
     * SPN found :LDAP/AD01
     * SPN found :LDAP/ad01.contoso.com/contoso
     * SPN found :LDAP/0b98109f-cd33-4ef9-8117-f5fdf68545e5._msdcs.contoso.com
     * SPN found :E3514235-4B06-11D1-AB04-00C04FC2DCD2/0b98109f-cd33-4ef9-8117-f5fdf68545e5/contoso.com
     * SPN found :HOST/ad01.contoso.com/contoso.com
     * SPN found :HOST/ad01.contoso.com
     * SPN found :HOST/AD01
     * SPN found :HOST/ad01.contoso.com/contoso
     * SPN found :GC/ad01.contoso.com/contoso.com
     ......................... AD01 passed test MachineAccount

  Starting test: NCSecDesc

     * Security Permissions check for all NC's on DC AD01.
     * Security Permissions Check for

       DC=ForestDnsZones,DC=contoso,DC=com
        (NDNC,Version 3)
     * Security Permissions Check for

       DC=DomainDnsZones,DC=contoso,DC=com
        (NDNC,Version 3)
     * Security Permissions Check for

       CN=Schema,CN=Configuration,DC=contoso,DC=com
        (Schema,Version 3)
     * Security Permissions Check for

       CN=Configuration,DC=contoso,DC=com
        (Configuration,Version 3)
     * Security Permissions Check for

       DC=contoso,DC=com
        (Domain,Version 3)
     ......................... AD01 passed test NCSecDesc

  Starting test: NetLogons

     * Network Logons Privileges Check
     Verified share \\AD01\netlogon
     Verified share \\AD01\sysvol
     ......................... AD01 passed test NetLogons

  Starting test: ObjectsReplicated

     AD01 is in domain DC=contoso,DC=com
     Checking for CN=AD01,OU=Domain Controllers,DC=contoso,DC=com in domain DC=contoso,DC=com on 2 servers
        Object is up-to-date on all servers.
     Checking for CN=NTDS Settings,CN=AD01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com in domain CN=Configuration,DC=contoso,DC=com on 2 servers
        Object is up-to-date on all servers.
     ......................... AD01 passed test ObjectsReplicated

  Test omitted by user request: OutboundSecureChannels

  Starting test: Replications

     * Replications Check
     [Replications Check,AD01] A recent replication attempt failed:

        From DR-DC to AD01

        Naming Context: DC=ForestDnsZones,DC=contoso,DC=com

        The replication generated an error (1256):

        The remote system is not available. For information about network troubleshooting, see Windows Help.

        

        The failure occurred at 2022-07-04 10:52:33.

        The last success occurred at 2022-06-23 19:24:55.

        103 failures have occurred since the last success.

     [Replications Check,AD01] A recent replication attempt failed:

        From AWS-DC to AD01

        Naming Context: DC=ForestDnsZones,DC=contoso,DC=com

        The replication generated an error (1256):

        The remote system is not available. For information about network troubleshooting, see Windows Help.

        

        The failure occurred at 2022-07-04 11:22:33.

        The last success occurred at 2022-06-30 18:43:35.

        357 failures have occurred since the last success.

     [Replications Check,AD01] A recent replication attempt failed:

        From DR-DC to AD01

        Naming Context: DC=DomainDnsZones,DC=contoso,DC=com

        The replication generated an error (1256):

        The remote system is not available. For information about network troubleshooting, see Windows Help.

        

        The failure occurred at 2022-07-04 10:52:33.

        The last success occurred at 2022-06-23 18:59:39.

        103 failures have occurred since the last success.

     [Replications Check,AD01] A recent replication attempt failed:

        From AWS-DC to AD01

        Naming Context: DC=DomainDnsZones,DC=contoso,DC=com

        The replication generated an error (1256):

        The remote system is not available. For information about network troubleshooting, see Windows Help.

        

        The failure occurred at 2022-07-04 11:22:33.

        The last success occurred at 2022-06-30 18:43:35.

        357 failures have occurred since the last success.

     [Replications Check,AD01] A recent replication attempt failed:

        From DR-DC to AD01

        Naming Context: CN=Schema,CN=Configuration,DC=contoso,DC=com

        The replication generated an error (1722):

        The RPC server is unavailable.

        The failure occurred at 2022-07-04 10:53:57.

       The last success occurred at 2022-06-23 18:59:39.

        96 failures have occurred since the last success.

        The source remains down. Please check the machine.

     [Replications Check,AD01] A recent replication attempt failed:

        From AWS-DC to AD01

        Naming Context: CN=Schema,CN=Configuration,DC=contoso,DC=com

        The replication generated an error (1722):

        The RPC server is unavailable.

        The failure occurred at 2022-07-04 11:23:57.

        The last success occurred at 2022-06-30 18:43:35.

        357 failures have occurred since the last success.

        The source remains down. Please check the machine.

     [Replications Check,AD01] A recent replication attempt failed:

        From DR-DC to AD01

        Naming Context: CN=Configuration,DC=contoso,DC=com

        The replication generated an error (1722):

        The RPC server is unavailable.

        The failure occurred at 2022-07-04 10:53:15.

        The last success occurred at 2022-06-23 19:31:04.

        106 failures have occurred since the last success.

        The source remains down. Please check the machine.

     [Replications Check,AD01] A recent replication attempt failed:

        From AWS-DC to AD01

        Naming Context: CN=Configuration,DC=contoso,DC=com

        The replication generated an error (1722):

        The RPC server is unavailable.

        The failure occurred at 2022-07-04 11:23:15.

        The last success occurred at 2022-06-30 18:43:35.

        357 failures have occurred since the last success.

        The source remains down. Please check the machine.

     [Replications Check,AD01] A recent replication attempt failed:

        From DR-DC to AD01

        Naming Context: DC=contoso,DC=com

        The replication generated an error (1722):

        The RPC server is unavailable.

        The failure occurred at 2022-07-04 10:52:33.

        The last success occurred at 2022-06-23 19:43:14.

        255 failures have occurred since the last success.

        The source remains down. Please check the machine.

     [Replications Check,AD01] A recent replication attempt failed:

        From AWS-DC to AD01

        Naming Context: DC=contoso,DC=com

        The replication generated an error (1722):

        The RPC server is unavailable.

        The failure occurred at 2022-07-04 11:22:33.

        The last success occurred at 2022-06-30 18:43:34.

        357 failures have occurred since the last success.

        The source remains down. Please check the machine.

     ......................... AD01 failed test Replications

  Starting test: RidManager

     * Available RID Pool for the Domain is 14107 to 1073741823
     * ad01.contoso.com is the RID Master
    * DsBind with RID Master was successful
     * rIDAllocationPool is 13607 to 14106
     * rIDPreviousAllocationPool is 13607 to 14106
     * rIDNextRID: 13614
     ......................... AD01 passed test RidManager

  Starting test: Services

     * Checking Service: EventSystem
     * Checking Service: RpcSs
     * Checking Service: NTDS
     * Checking Service: DnsCache
     * Checking Service: NtFrs
     * Checking Service: IsmServ
     * Checking Service: kdc
     * Checking Service: SamSs
     * Checking Service: LanmanServer
     * Checking Service: LanmanWorkstation
     * Checking Service: w32time
     * Checking Service: NETLOGON
     ......................... AD01 passed test Services

  Starting test: SystemLog

     * The System Event log test
     An error event occurred.  EventID: 0x00002734

        Time Generated: 07/04/2022   10:56:34

        Event String:

        The server-side authentication level policy does not allow the user contoso\paloalto SID (S-1-5-21-3478182326-1166062991-1008443158-8314) from address 172.20.32.253 to activate DCOM server. Please raise the activation authentication level at least to RPC_C_AUTHN_LEVEL_PKT_INTEGRITY in client application.

     An error event occurred.  EventID: 0x00002734

        Time Generated: 07/04/2022   10:56:34

        Event String:

        The server-side authentication level policy does not allow the user contoso\paloalto SID (S-1-5-21-3478182326-1166062991-1008443158-8314) from address 172.20.32.253 to activate DCOM server. Please raise the activation authentication level at least to RPC_C_AUTHN_LEVEL_PKT_INTEGRITY in client application.

     An error event occurred.  EventID: 0x00002734

        Time Generated: 07/04/2022   10:56:50

        Event String:

       

     ......................... AD01 failed test SystemLog

  Test omitted by user request: Topology

  Test omitted by user request: VerifyEnterpriseReferences

  Starting test: VerifyReferences

     The system object reference (serverReference)

     CN=AD01,OU=Domain Controllers,DC=contoso,DC=com and backlink on

     CN=AD01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com

     are correct. 
     The system object reference (serverReferenceBL)

     CN=AD01,CN=Domain System Volume (SYSVOL share),CN=File Replication Service,CN=System,DC=contoso,DC=com

     and backlink on

     CN=NTDS Settings,CN=AD01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=com

     are correct. 
     The system object reference (frsComputerReferenceBL)

     CN=AD01,CN=Domain System Volume (SYSVOL share),CN=File Replication Service,CN=System,DC=contoso,DC=com

     and backlink on CN=AD01,OU=Domain Controllers,DC=contoso,DC=com

     are correct. 
     ......................... AD01 passed test VerifyReferences

  Test omitted by user request: VerifyReplicas
```

   Testing server: Default-First-Site-Name\AD02

```
Starting test: Advertising

     The DC AD02 is advertising itself as a DC and having a DS.
     The DC AD02 is advertising as an LDAP server
     The DC AD02 is advertising as having a writeable directory
     The DC AD02 is advertising as a Key Distribution Center
     The DC AD02 is advertising as a time server
     The DS AD02 is advertising as a GC.
     ......................... AD02 passed test Advertising

  Test omitted by user request: CheckSecurityError

  Test omitted by user request: CutoffServers

  Starting test: FrsEvent

     * The File Replication Service Event log test 
     There are warning or error events within the last 24 hours after the

     SYSVOL has been shared.  Failing SYSVOL replication problems may cause

     Group Policy problems. 
     A warning event occurred.  EventID: 0x800034C4

        Time Generated: 07/03/2022   23:05:31

        Event String:

        The File Replication Service is having trouble enabling replication from DR-DC to AD02 for c:\windows\sysvol\domain using the DNS name dr-DC.contoso.com. FRS will keep retrying. 

         Following are some of the reasons you would see this warning. 

         

         [1] FRS can not correctly resolve the DNS name dr-DC.contoso.com from this computer. 

         [2] FRS is not running on dr-DC.contoso.com. 

         [3] The topology information in the Active Directory Domain Services for this replica has not yet replicated to all the Domain Controllers. 

         

         This event log message will appear once per connection, After the problem is fixed you will see another event log message indicating that the connection has been established.

     ......................... AD02 passed test FrsEvent

  Starting test: DFSREvent

     The DFS Replication Event Log. 
     Skip the test because the server is running FRS.

     ......................... AD02 passed test DFSREvent

  Starting test: SysVolCheck

     * The File Replication Service SYSVOL ready test 
     File Replication Service's SYSVOL is ready 
     ......................... AD02 passed test SysVolCheck

  Starting test: KccEvent

     * The KCC Event log test
     A warning event occurred.  EventID: 0x8000061E

        Time Generated: 07/04/2022   11:15:52

        Event String:

        All directory servers in the following site that can replicate the directory partition over this transport are currently unavailable. 

         

        Site:

        CN=AWS-Site,CN=Sites,CN=Configuration,DC=contoso,DC=com 

        Directory partition:

        DC=contoso,DC=com 

        Transport:

        CN=IP,CN=Inter-Site Transports,CN=Sites,CN=Configuration,DC=contoso,DC=com

     An error event occurred.  EventID: 0xC000051F

        Time Generated: 07/04/2022   11:15:52

        Event String:

        The Knowledge Consistency Checker (KCC) has detected problems with the following directory partition. 

         

        Directory partition:

        DC=contoso,DC=com 

         

        There is insufficient site connectivity information for the KCC to create a spanning tree replication topology. Or, one or more directory servers with this directory partition are unable to replicate the directory partition information. This is probably due to inaccessible directory servers. 

         

        User Action 

        Perform one of the following actions: 

        - Publish sufficient site connectivity information so that the KCC can determine a route by which this directory partition can reach this site. This is the preferred option. 

        - Add a Connection object to a directory service that contains the directory partition in this site from a directory service that contains the same directory partition in another site. 

         

        If neither of the tasks correct this condition, see previous events logged by the KCC that identify the inaccessible directory servers.

     A warning event occurred.  EventID: 0x80000749

        Time Generated: 07/04/2022   11:15:52

        Event String:

        The Knowledge Consistency Checker (KCC) was unable to form a complete spanning tree network topology. As a result, the following list of sites cannot be reached from the local site. 

         

        Sites: 

        CN=AWS-Site,CN=Sites,CN=Configuration,DC=contoso,DC=com 

         
   
      

             

         

        

     A warning event occurred.  EventID: 0x8000061E

        Time Generated: 07/04/2022   11:15:52

        Event String:

        All directory servers in the following site that can replicate the directory partition over this transport are currently unavailable. 

         

        Site:

        CN=AWS-Site,CN=Sites,CN=Configuration,DC=contoso,DC=com 

        Directory partition:

        DC=ForestDnsZones,DC=contoso,DC=com 

        Transport:

        CN=IP,CN=Inter-Site Transports,CN=Sites,CN=Configuration,DC=contoso,DC=com

     An error event occurred.  EventID: 0xC000051F

        Time Generated: 07/04/2022   11:15:52

        Event String:

        The Knowledge Consistency Checker (KCC) has detected problems with the following directory partition. 

         

        Directory partition:

        DC=ForestDnsZones,DC=contoso,DC=com 

         

        There is insufficient site connectivity information for the KCC to create a spanning tree replication topology. Or, one or more directory servers with this directory partition are unable to replicate the directory partition information. This is probably due to inaccessible directory servers. 

         

        User Action 

        Perform one of the following actions: 

        - Publish sufficient site connectivity information so that the KCC can determine a route by which this directory partition can reach this site. This is the preferred option. 

        - Add a Connection object to a directory service that contains the directory partition in this site from a directory service that contains the same directory partition in another site. 

         

        If neither of the tasks correct this condition, see previous events logged by the KCC that identify the inaccessible directory servers.

     A warning event occurred.  EventID: 0x80000749

        Time Generated: 07/04/2022   11:15:52

        Event String:

        The Knowledge Consistency Checker (KCC) was unable to form a complete spanning tree network topology. As a result, the following list of sites cannot be reached from the local site. 

         

        Sites: 

        CN=AWS-Site,CN=Sites,CN=Configuration,DC=contoso,DC=com 

         

         

         

         

         

         

        

     A warning event occurred.  EventID: 0x8000061E

        Time Generated: 07/04/2022   11:15:52

        Event String:

        All directory servers in the following site that can replicate the directory partition over this transport are currently unavailable. 

         

        Site:

        CN=AWS-Site,CN=Sites,CN=Configuration,DC=contoso,DC=com 

        Directory partition:

        DC=DomainDnsZones,DC=contoso,DC=com 

        Transport:

        CN=IP,CN=Inter-Site Transports,CN=Sites,CN=Configuration,DC=contoso,DC=com

     An error event occurred.  EventID: 0xC000051F

        Time Generated: 07/04/2022   11:15:52

        Event String:

        The Knowledge Consistency Checker (KCC) has detected problems with the following directory partition. 

         

        Directory partition:

        DC=DomainDnsZones,DC=contoso,DC=com 

         

        There is insufficient site connectivity information for the KCC to create a spanning tree replication topology. Or, one or more directory servers with this directory partition are unable to replicate the directory partition information. This is probably due to inaccessible directory servers. 

         

        User Action 

        Perform one of the following actions: 

        - Publish sufficient site connectivity information so that the KCC can determine a route by which this directory partition can reach this site. This is the preferred option. 

        - Add a Connection object to a directory service that contains the directory partition in this site from a directory service that contains the same directory partition in another site. 

         

        If neither of the tasks correct this condition, see previous events logged by the KCC that identify the inaccessible directory servers.

     A warning event occurred.  EventID: 0x80000749

        Time Generated: 07/04/2022   11:15:52

        Event String:

        The Knowledge Consistency Checker (KCC) was unable to form a complete spanning tree network topology. As a result, the following list of sites cannot be reached from the local site. 

         

        Sites: 

        CN=AWS-Site,CN=Sites,CN=Configuration,DC=contoso,DC=com 

         

         

         

         

         

         

        

     A warning event occurred.  EventID: 0x8000061E

        Time Generated: 07/04/2022   11:15:52

        Event String:

        All directory servers in the following site that can replicate the directory partition over this transport are currently unavailable. 

         

        Site:

        CN=AWS-Site,CN=Sites,CN=Configuration,DC=contoso,DC=com 

        Directory partition:

        CN=Configuration,DC=contoso,DC=com 

        Transport:

        CN=IP,CN=Inter-Site Transports,CN=Sites,CN=Configuration,DC=contoso,DC=com

     An error event occurred.  EventID: 0xC000051F

        Time Generated: 07/04/2022   11:15:52

        Event String:

        The Knowledge Consistency Checker (KCC) has detected problems with the following directory partition. 

         

        Directory partition:

        CN=Configuration,DC=contoso,DC=com 

         

        There is insufficient site connectivity information for the KCC to create a spanning tree replication topology. Or, one or more directory servers with this directory partition are unable to replicate the directory partition information. This is probably due to inaccessible directory servers. 

         

        User Action 

        Perform one of the following actions: 

        - Publish sufficient site connectivity information so that the KCC can determine a route by which this directory
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-04*

Hi,@rr-4098       

Could you please share email id, or i need to paste here. please advise

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-03*

Was the image restore of the DC's authoritive or non-authoritive? Were the images from same date / time ? Please run an dcdiag /v /e/ > C:\<dcname>.txt on both DC's and upload the results.
