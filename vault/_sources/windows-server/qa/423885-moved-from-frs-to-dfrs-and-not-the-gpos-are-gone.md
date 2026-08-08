---
title: "Moved from FRS to DFRS and not the GPOs are gone"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/423885/moved-from-frs-to-dfrs-and-not-the-gpos-are-gone
question_id: 423885
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Moved from FRS to DFRS and not the GPOs are gone

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/423885/moved-from-frs-to-dfrs-and-not-the-gpos-are-gone (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So, I'm not a guru here, more of a tinkerer.  I'm learning on a home lab which has a Win2k12r2 and a Win2k16 server.  

I ran through the process of transitioning from FRS to DFRS using the "Quick" option outlined here:  

https://techcommunity.microsoft.com/t5/storage-at-microsoft/streamlined-migration-of-frs-to-dfsr-sysvol/ba-p/425405  

I was able to complete every step successfully.  I thought everything worked just fine.  Unfortunately, it did not.  

While the Sysvol share is visible under SYSVOL_DFSR, it's not populated with anything.  Furthermore, there is no NETLOGON directory.  I see my GPOs under the GPM console, but when I go to edit them, I get an error that says "Failed to open the Group Policy Object.  You might not have the appropriate rights."  The error then says the following under the details "The system cannot find the path specified."  I am however, able to create a new policy.  

Does someone mind helping me our here?  I don't know if the DFRS removes the need for a NETLOGON, which is why that folder doesn't exist.  I also don't know why nothing seems to have been copied over from SYSVOL to SYSVOL_DFSR.  Since the procedure deleted the SYSVOL folder, I can't check to compare the permissions, but from what I can tell, the permissions on SYSVOL_DFSR are there, so I'm going to assume that they're the right permissions?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-15*

Hello @Sameer Sheikh  ,

From the description:

4.Based on the description "I was able to complete every step successfully. I thought everything worked just fine. Unfortunately, it did not.", did you mean during the migration process from beginning to end, no errors were reported?

I had an issue with the global states not syncing between the DCs (1,2,3 etc). I followed some advice where someone suggested changing a registry value to D4 to fix the issue.

I do not quite understand "I had an issue with the global states not syncing between the DCs (1,2,3 etc). I followed some advice where someone suggested changing a registry value to D4 to fix the issue.", but it seems you do not migrate FSR to DFSR successfully.

Because it is the lab, I suggest you migrate FRS to DFSR again to see if you can set up a new lab.

Before you migrate FRS to DFSR, make sure:

AD replication is working fine.  

FSR replication is working fine, too.  

Any problems that arise during the migration process should be investigated and resolved as much as possible.

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-10*

I was able to solve the NETLOGON issue using the solution found here:  

https://serverfault.com/questions/844757/netlogon-share-missing-from-domain-server-2012-r2-dfsr

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-10*

Here's the latest DCDIAG:

```
Directory Server Diagnosis

Performing initial setup:

   Trying to find home server...

   Home Server = atlas-v2-dc

   * Identified AD Forest. 
   Done gathering initial info.

Doing initial required tests

   Testing server: Default-First-Site-Name\ATLAS-V2-DC

      Starting test: Connectivity

         ......................... ATLAS-V2-DC passed test Connectivity

Doing primary tests

   Testing server: Default-First-Site-Name\ATLAS-V2-DC

      Starting test: Advertising

         ......................... ATLAS-V2-DC passed test Advertising

      Starting test: CheckSecurityError

            [ATLAS-V2-DC] DsReplicaGetInfo(KCC_DS_CONNECT_FAILURES) failed with

            error 8453,

            [ATLAS-V2-DC] Unable to query the list of KCC connection failures.

            Continuing...

         [ATLAS-V2-DC] No security related replication errors were found on

         this DC!  To target the connection to a specific source DC use

         /ReplSource:.

         ......................... ATLAS-V2-DC passed test CheckSecurityError

      Starting test: CutoffServers

         ......................... ATLAS-V2-DC passed test CutoffServers

      Starting test: FrsEvent

         ......................... ATLAS-V2-DC passed test FrsEvent

      Starting test: DFSREvent

         There are warning or error events within the last 24 hours after the

         SYSVOL has been shared.  Failing SYSVOL replication problems may cause

         Group Policy problems. 
         ......................... ATLAS-V2-DC passed test DFSREvent

      Starting test: SysVolCheck

         ......................... ATLAS-V2-DC passed test SysVolCheck

      Starting test: FrsSysVol

         ......................... ATLAS-V2-DC passed test FrsSysVol

      Starting test: KccEvent

         A warning event occurred.  EventID: 0x80000B46

            Time Generated: 06/09/2021   13:12:22

            Event String:

            The security of this directory server can be significantly enhanced by configuring the server to reject SASL (Negotiate, Kerberos, NTLM, or Digest) LDAP binds that do not request signing (integrity verification) and LDAP simple binds that are performed on a clear text (non-SSL/TLS-encrypted) connection.  Even if no clients are using such binds, configuring the server to reject them will improve the security of this server. 

         A warning event occurred.  EventID: 0x80000BE1

            Time Generated: 06/09/2021   13:12:22

            Event String:

            The security of this directory server can be significantly enhanced by configuring the server to enforce  validation of Channel Binding Tokens received in LDAP bind requests sent over LDAPS connections. Even if  no clients are issuing LDAP bind requests over LDAPS, configuring the server to validate Channel Binding  Tokens will improve the security of this server. 

         A warning event occurred.  EventID: 0x8000082C

            Time Generated: 06/09/2021   13:13:22

            Event String: 

         A warning event occurred.  EventID: 0x80000B46

            Time Generated: 06/09/2021   13:21:08

            Event String:

            The security of this directory server can be significantly enhanced by configuring the server to reject SASL (Negotiate, Kerberos, NTLM, or Digest) LDAP binds that do not request signing (integrity verification) and LDAP simple binds that are performed on a clear text (non-SSL/TLS-encrypted) connection.  Even if no clients are using such binds, configuring the server to reject them will improve the security of this server. 

         A warning event occurred.  EventID: 0x80000BE1

            Time Generated: 06/09/2021   13:21:08

            Event String:

            The security of this directory server can be significantly enhanced by configuring the server to enforce  validation of Channel Binding Tokens received in LDAP bind requests sent over LDAPS connections. Even if  no clients are issuing LDAP bind requests over LDAPS, configuring the server to validate Channel Binding  Tokens will improve the security of this server. 

         A warning event occurred.  EventID: 0x8000082C

            Time Generated: 06/09/2021   13:22:09

            Event String: 

         ......................... ATLAS-V2-DC passed test KccEvent

      Starting test: KnowsOfRoleHolders

         ......................... ATLAS-V2-DC passed test KnowsOfRoleHolders

      Starting test: MachineAccount

         ......................... ATLAS-V2-DC passed test MachineAccount

      Starting test: NCSecDesc

         ......................... ATLAS-V2-DC passed test NCSecDesc

      Starting test: NetLogons

         Unable to connect to the NETLOGON share! (\\ATLAS-V2-DC\netlogon)

         [ATLAS-V2-DC] An net use or LsaPolicy operation failed with error 67,

         The network name cannot be found..

         ......................... ATLAS-V2-DC failed test NetLogons

      Starting test: ObjectsReplicated

         ......................... ATLAS-V2-DC passed test ObjectsReplicated

      Starting test: OutboundSecureChannels

         ** Did not run Outbound Secure Channels test because /testdomain: was

         not entered

         ......................... ATLAS-V2-DC passed test

         OutboundSecureChannels

      Starting test: Replications

         [Replications Check,ATLAS-V2-DC] A recent replication attempt failed:

            From ATLAS-V3-DC to ATLAS-V2-DC

            Naming Context: DC=ForestDnsZones,DC=abc123,DC=net

            The replication generated an error (8524):

            The DSA operation is unable to proceed because of a DNS lookup failure.

            The failure occurred at 2021-06-09 13:21:38.

            The last success occurred at 2021-06-09 13:18:25.

            1 failures have occurred since the last success.

            The guid-based DNS name

            6ee8724a-a33d-45b7-8551-95a8829391ba._msdcs.abc123.net

            is not registered on one or more DNS servers.

         [Replications Check,ATLAS-V2-DC] A recent replication attempt failed:

            From ATLAS-V3-DC to ATLAS-V2-DC

            Naming Context: DC=DomainDnsZones,DC=abc123,DC=net

            The replication generated an error (8524):

            The DSA operation is unable to proceed because of a DNS lookup failure.

            The failure occurred at 2021-06-09 13:21:38.

            The last success occurred at 2021-06-09 12:51:22.

            2 failures have occurred since the last success.

            The guid-based DNS name

            6ee8724a-a33d-45b7-8551-95a8829391ba._msdcs.abc123.net

            is not registered on one or more DNS servers.

         [Replications Check,ATLAS-V2-DC] A recent replication attempt failed:

            From ATLAS-V3-DC to ATLAS-V2-DC

            Naming Context: CN=Schema,CN=Configuration,DC=abc123,DC=net

            The replication generated an error (8524):

            The DSA operation is unable to proceed because of a DNS lookup failure.

            The failure occurred at 2021-06-09 13:21:38.

            The last success occurred at 2021-06-09 12:51:22.

            2 failures have occurred since the last success.

            The guid-based DNS name

            6ee8724a-a33d-45b7-8551-95a8829391ba._msdcs.abc123.net

            is not registered on one or more DNS servers.

         [Replications Check,ATLAS-V2-DC] A recent replication attempt failed:

            From ATLAS-V3-DC to ATLAS-V2-DC

            Naming Context: CN=Configuration,DC=abc123,DC=net

            The replication generated an error (8524):

            The DSA operation is unable to proceed because of a DNS lookup failure.

            The failure occurred at 2021-06-09 13:21:38.

            The last success occurred at 2021-06-09 12:51:22.

            2 failures have occurred since the last success.

            The guid-based DNS name

            6ee8724a-a33d-45b7-8551-95a8829391ba._msdcs.abc123.net

            is not registered on one or more DNS servers.

         ......................... ATLAS-V2-DC failed test Replications

      Starting test: RidManager

         ......................... ATLAS-V2-DC passed test RidManager

      Starting test: Services

            Could not open NTDS Service on ATLAS-V2-DC, error 0x5

            "Access is denied."

         ......................... ATLAS-V2-DC failed test Services

      Starting test: SystemLog

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   12:25:37

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x0000272C

            Time Generated: 06/09/2021   12:25:58

            Event String:

            DCOM was unable to communicate with the computer 1.0.0.1 using any of the configured protocols; requested by PID      368 (C:\Windows\system32\dcdiag.exe).

         An error event occurred.  EventID: 0x0000272C

            Time Generated: 06/09/2021   12:26:19

            Event String:

            DCOM was unable to communicate with the computer 1.1.1.1 using any of the configured protocols; requested by PID      368 (C:\Windows\system32\dcdiag.exe).

         An error event occurred.  EventID: 0x0000272C

            Time Generated: 06/09/2021   12:26:42

            Event String:

            DCOM was unable to communicate with the computer 84.200.69.80 using any of the configured protocols; requested by PID      368 (C:\Windows\system32\dcdiag.exe).

         An error event occurred.  EventID: 0x0000272C

            Time Generated: 06/09/2021   12:27:04

            Event String:

            DCOM was unable to communicate with the computer 84.200.70.40 using any of the configured protocols; requested by PID      368 (C:\Windows\system32\dcdiag.exe).

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   12:27:52

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{E19F8B53-6202-488C-A477-A93BE69B0C0B}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   12:30:38

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         A warning event occurred.  EventID: 0x000727A5

            Time Generated: 06/09/2021   12:35:05

            Event String:

            The WinRM service is not listening for WS-Management requests. 

         A warning event occurred.  EventID: 0x0000000B

            Time Generated: 06/09/2021   12:36:10

            Event String:

            Custom dynamic link libraries are being loaded for every application. The system administrator should review the list of libraries to ensure they are related to trusted applications. Please visit http://support.microsoft.com/kb/197571 for more information.

         A warning event occurred.  EventID: 0x00000079

            Time Generated: 06/09/2021   12:36:22

            Event String:

            The firewall exception to allow Internet Storage Name Server (iSNS) client functionality is not enabled. iSNS client functionality is not available.

         A warning event occurred.  EventID: 0x000003F6

            Time Generated: 06/09/2021   12:36:22

            Event String:

            Name resolution for the name _ldap._tcp.dc._msdcs.abc123.net. timed out after none of the configured DNS servers responded.

         A warning event occurred.  EventID: 0x800009CF

            Time Generated: 06/09/2021   12:36:29

            Event String:

            The server service was unable to recreate the share abc123_storage because the directory E:\abc123_storage no longer exists.  Please run "net share abc123_storage /delete" to delete the share, or recreate the directory E:\abc123_storage.

         A warning event occurred.  EventID: 0x800009CF

            Time Generated: 06/09/2021   12:36:29

            Event String:

            The server service was unable to recreate the share FD_4T-Videos$ because the directory E:\FD_4T-Videos$ no longer exists.  Please run "net share FD_4T-Videos$ /delete" to delete the share, or recreate the directory E:\FD_4T-Videos$.

         An error event occurred.  EventID: 0x0000166D

            Time Generated: 06/09/2021   12:36:32

            Event String:

            Netlogon could not register the ABC123 name for the following reason: 

         An error event occurred.  EventID: 0x0000164A

            Time Generated: 06/09/2021   12:36:32

            Event String:

            The Netlogon service could not create server share C:\Windows\SYSVOL_DFSR\sysvol\abc123.net\SCRIPTS.  The following error occurred: 

         An error event occurred.  EventID: 0xC00010E1

            Time Generated: 06/09/2021   12:36:32

            Event String:

            The name "ABC123      :1b" could not be registered on the interface with IP address 192.168.100.254. The computer with the IP address 192.168.100.246 did not allow the name to be claimed by this computer.

         A warning event occurred.  EventID: 0x00001796

            Time Generated: 06/09/2021   12:36:35

            Event String:

            Microsoft Windows Server has detected that NTLM authentication is presently being used between clients and this server. This event occurs once per boot of the server on the first time a client uses NTLM with this server.

         A warning event occurred.  EventID: 0x000727AA

            Time Generated: 06/09/2021   12:36:51

            Event String:

            The WinRM service failed to create the following SPNs: WSMAN/atlas-v2-dc.abc123.net; WSMAN/atlas-v2-dc. 

         An error event occurred.  EventID: 0xC0001B63

            Time Generated: 06/09/2021   12:36:50

            Event String:

            A timeout (30000 milliseconds) was reached while waiting for a transaction response from the WinTarget service.

         A warning event occurred.  EventID: 0x00002724

            Time Generated: 06/09/2021   12:36:52

            Event String:

            This computer has at least one dynamically assigned IPv6 address.For reliable DHCPv6 server operation, you should use only static IPv6 addresses.

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   12:37:04

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   12:37:26

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{E19F8B53-6202-488C-A477-A93BE69B0C0B}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0xC00010E1

            Time Generated: 06/09/2021   12:41:55

            Event String:

            The name "ABC123      :1b" could not be registered on the interface with IP address 192.168.100.254. The computer with the IP address 192.168.100.246 did not allow the name to be claimed by this computer.

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   12:42:05

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x0000042E

            Time Generated: 06/09/2021   12:45:52

            Event String:

            Iashlpr initialization failed: The DHCP service was unable to access path specified for the audit log.

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   12:47:05

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0xC00010E1

            Time Generated: 06/09/2021   12:51:57

            Event String:

            The name "ABC123      :1b" could not be registered on the interface with IP address 192.168.100.254. The computer with the IP address 192.168.100.246 did not allow the name to be claimed by this computer.

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   12:52:06

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   12:57:06

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   13:02:07

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x0000042E

            Time Generated: 06/09/2021   13:05:09

            Event String:

            Iashlpr initialization failed: The DHCP service was unable to access path specified for the audit log.

         An error event occurred.  EventID: 0x0000042E

            Time Generated: 06/09/2021   13:05:11

            Event String:

            Iashlpr initialization failed: The DHCP service was unable to access path specified for the audit log.

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   13:07:08

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x0000042E

            Time Generated: 06/09/2021   13:08:46

            Event String:

            Iashlpr initialization failed: The DHCP service was unable to access path specified for the audit log.

         An error event occurred.  EventID: 0x0000042E

            Time Generated: 06/09/2021   13:10:00

            Event String:

            Iashlpr initialization failed: The DHCP service was unable to access path specified for the audit log.

         An error event occurred.  EventID: 0x0000042E

            Time Generated: 06/09/2021   13:10:01

            Event String:

            Iashlpr initialization failed: The DHCP service was unable to access path specified for the audit log.

         A warning event occurred.  EventID: 0x0000000B

            Time Generated: 06/09/2021   13:12:10

            Event String:

            Custom dynamic link libraries are being loaded for every application. The system administrator should review the list of libraries to ensure they are related to trusted applications. Please visit http://support.microsoft.com/kb/197571 for more information.

         A warning event occurred.  EventID: 0x00000079

            Time Generated: 06/09/2021   13:12:20

            Event String:

            The firewall exception to allow Internet Storage Name Server (iSNS) client functionality is not enabled. iSNS client functionality is not available.

         A warning event occurred.  EventID: 0x000003F6

            Time Generated: 06/09/2021   13:12:20

            Event String:

            Name resolution for the name _ldap._tcp.dc._msdcs.abc123.net. timed out after none of the configured DNS servers responded.

         A warning event occurred.  EventID: 0x800009CF

            Time Generated: 06/09/2021   13:12:27

            Event String:

            The server service was unable to recreate the share abc123_storage because the directory E:\abc123_storage no longer exists.  Please run "net share abc123_storage /delete" to delete the share, or recreate the directory E:\abc123_storage.

         A warning event occurred.  EventID: 0x800009CF

            Time Generated: 06/09/2021   13:12:27

            Event String:

            The server service was unable to recreate the share FD_4T-Videos$ because the directory E:\FD_4T-Videos$ no longer exists.  Please run "net share FD_4T-Videos$ /delete" to delete the share, or recreate the directory E:\FD_4T-Videos$.

         An error event occurred.  EventID: 0x0000166D

            Time Generated: 06/09/2021   13:12:31

            Event String:

            Netlogon could not register the ABC123 name for the following reason: 

         An error event occurred.  EventID: 0x0000164A

            Time Generated: 06/09/2021   13:12:31

            Event String:

            The Netlogon service could not create server share C:\Windows\SYSVOL_DFSR\sysvol\abc123.net\SCRIPTS.  The following error occurred: 

         An error event occurred.  EventID: 0xC00010E1

            Time Generated: 06/09/2021   13:12:31

            Event String:

            The name "ABC123      :1b" could not be registered on the interface with IP address 192.168.100.254. The computer with the IP address 192.168.100.246 did not allow the name to be claimed by this computer.

         A warning event occurred.  EventID: 0x00001796

            Time Generated: 06/09/2021   13:12:45

            Event String:

            Microsoft Windows Server has detected that NTLM authentication is presently being used between clients and this server. This event occurs once per boot of the server on the first time a client uses NTLM with this server.

         A warning event occurred.  EventID: 0x000727AA

            Time Generated: 06/09/2021   13:12:47

            Event String:

            The WinRM service failed to create the following SPNs: WSMAN/atlas-v2-dc.abc123.net; WSMAN/atlas-v2-dc. 

         A warning event occurred.  EventID: 0x00002724

            Time Generated: 06/09/2021   13:12:49

            Event String:

            This computer has at least one dynamically assigned IPv6 address.For reliable DHCPv6 server operation, you should use only static IPv6 addresses.

         An error event occurred.  EventID: 0xC0001B63

            Time Generated: 06/09/2021   13:12:48

            Event String:

            A timeout (30000 milliseconds) was reached while waiting for a transaction response from the WinTarget service.

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   13:12:54

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   13:13:06

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{E19F8B53-6202-488C-A477-A93BE69B0C0B}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/09/2021   13:17:55

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0xC00010E1

            Time Generated: 06/09/2021   13:17:55

            Event String:

            The name "ABC123      :1b" could not be registered on the interface with IP address 192.168.100.254. The computer with the IP address 192.168.100.246 did not allow the name to be claimed by this computer.

         An error event occurred.  EventID: 0x80001778

            Time Generated: 06/09/2021   13:20:50

            Event String:

            The previous system shutdown at 1:20:03 PM on 6/9/2021 was unexpected.

         An error event occurred.  EventID: 0x400003E9

            Time Generated: 06/09/2021   13:20:50

            Event String:

            The computer has rebooted from a bugcheck.  The bugcheck was: 0x0000001a (0x0000000000041792, 0xfffff68043682330, 0x0008000000000000, 0x0000000000000000). A dump was saved in: C:\Windows\MEMORY.DMP. Report Id: 060921-7546-01.

         An error event occurred.  EventID: 0x00000029

            Time Generated: 06/09/2021   13:20:42

            Event String:

            The system has rebooted without cleanly shutting down first. This error could be caused if the system stopped responding, crashed, or lost power unexpectedly.

         A warning event occurred.  EventID: 0x0000000B

            Time Generated: 06/09/2021   13:20:56

            Event String:

            Custom dynamic link libraries are being loaded for every application. The system administrator should review the list of libraries to ensure they are related to trusted applications. Please visit http://support.microsoft.com/kb/197571 for more information.

         A warning event occurred.  EventID: 0x00000079

            Time Generated: 06/09/2021   13:21:08

            Event String:

            The firewall exception to allow Internet Storage Name Server (iSNS) client functionality is not enabled. iSNS client functionality is not available.

         A warning event occurred.  EventID: 0x000003F6

            Time Generated: 06/09/2021   13:21:08

            Event String:

            Name resolution for the name _ldap._tcp.dc._msdcs.abc123.net. timed out after none of the configured DNS servers responded.

         A warning event occurred.  EventID: 0x800009CF

            Time Generated: 06/09/2021   13:21:15

            Event String:

            The server service was unable to recreate the share abc123_storage because the directory E:\abc123_storage no longer exists.  Please run "net share abc123_storage /delete" to delete the share, or recreate the directory E:\abc123_storage.

         A warning event occurred.  EventID: 0x800009CF

            Time Generated: 06/09/2021   13:21:15

            Event String:

            The server service was unable to recreate the share FD_4T-Videos$ because the directory E:\FD_4T-Videos$ no longer exists.  Please run "net share FD_4T-Videos$ /delete" to delete the share, or recreate the directory E:\FD_4T-Videos$.

         An error event occurred.  EventID: 0x0000166D

            Time Generated: 06/09/2021   13:21:18

            Event String:

            Netlogon could not register the ABC123 name for the following reason: 

         An error event occurred.  EventID: 0x0000164A

            Time Generated: 06/09/2021   13:21:19

            Event String:

            The Netlogon service could not create server share C:\Windows\SYSVOL_DFSR\sysvol\abc123.net\SCRIPTS.  The following error occurred: 

         An error event occurred.  EventID: 0xC00010E1
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-09*

Thank you for both your responses and help. DSPatrick, I have that link open and am trying to make some sense out of it.

Daisy, here are the answers to your questions:

1.What is the forest functional level and domain functional level of your AD environment?

Windows2012r2Forest  

Windows2012R2Domain

2.How many Domain Controllers in your AD forest?

I have two: 1 x Win2k12r2 (primary), 1 x Win2k16 (secondary)

3.Please check if SYSVOL is FRS or DFSR by check the registry on all Domain Controllers.

The registry value is "3"

4.Based on the description "I was able to complete every step successfully. I thought everything worked just fine. Unfortunately, it did not.", did you mean during the migration process from beginning to end, no errors were reported?

I had an issue with the global states not syncing between the DCs (1,2,3 etc). I followed some advice where someone suggested changing a registry value to D4 to fix the issue.

Here's the output of dcdiag /c if you need it:

```
Directory Server Diagnosis

Performing initial setup:

   Trying to find home server...

   Home Server = atlas-v2-dc

   * Identified AD Forest. 
   Done gathering initial info.

Doing initial required tests

   Testing server: Default-First-Site-Name\ATLAS-V2-DC

      Starting test: Connectivity

         ......................... ATLAS-V2-DC passed test Connectivity

Doing primary tests

   Testing server: Default-First-Site-Name\ATLAS-V2-DC

      Starting test: Advertising

         ......................... ATLAS-V2-DC passed test Advertising

      Starting test: CheckSecurityError

         [ATLAS-V2-DC] No security related replication errors were found on

         this DC!  To target the connection to a specific source DC use

         /ReplSource:.

         ......................... ATLAS-V2-DC passed test CheckSecurityError

      Starting test: CutoffServers

         ......................... ATLAS-V2-DC passed test CutoffServers

      Starting test: FrsEvent

         ......................... ATLAS-V2-DC passed test FrsEvent

      Starting test: DFSREvent

         ......................... ATLAS-V2-DC passed test DFSREvent

      Starting test: SysVolCheck

         ......................... ATLAS-V2-DC passed test SysVolCheck

      Starting test: FrsSysVol

         ......................... ATLAS-V2-DC passed test FrsSysVol

      Starting test: KccEvent

         ......................... ATLAS-V2-DC passed test KccEvent

      Starting test: KnowsOfRoleHolders

         ......................... ATLAS-V2-DC passed test KnowsOfRoleHolders

      Starting test: MachineAccount

         ......................... ATLAS-V2-DC passed test MachineAccount

      Starting test: NCSecDesc

         ......................... ATLAS-V2-DC passed test NCSecDesc

      Starting test: NetLogons

         Unable to connect to the NETLOGON share! (\\ATLAS-V2-DC\netlogon)

         [ATLAS-V2-DC] An net use or LsaPolicy operation failed with error 67,

         The network name cannot be found..

         ......................... ATLAS-V2-DC failed test NetLogons

      Starting test: ObjectsReplicated

         ......................... ATLAS-V2-DC passed test ObjectsReplicated

      Starting test: OutboundSecureChannels

         ** Did not run Outbound Secure Channels test because /testdomain: was

         not entered

         ......................... ATLAS-V2-DC passed test

         OutboundSecureChannels

      Starting test: Replications

         ......................... ATLAS-V2-DC passed test Replications

      Starting test: RidManager

         ......................... ATLAS-V2-DC passed test RidManager

      Starting test: Services

         ......................... ATLAS-V2-DC passed test Services

      Starting test: SystemLog

         An error event occurred.  EventID: 0x0000042E

            Time Generated: 06/08/2021   16:52:27

            Event String:

            Iashlpr initialization failed: The DHCP service was unable to access path specified for the audit log.

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   16:52:43

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   16:57:44

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   17:02:45

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   17:07:46

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   17:12:46

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x0000042E

            Time Generated: 06/08/2021   17:14:11

            Event String:

            Iashlpr initialization failed: The DHCP service was unable to access path specified for the audit log.

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   17:17:47

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   17:22:48

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   17:27:49

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x0000042E

            Time Generated: 06/08/2021   17:32:28

            Event String:

            Iashlpr initialization failed: The DHCP service was unable to access path specified for the audit log.

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   17:32:49

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   17:37:50

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   17:42:51

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         An error event occurred.  EventID: 0x00000422

            Time Generated: 06/08/2021   17:47:52

            Event String:

            The processing of Group Policy failed. Windows attempted to read the file \\abc123.net\SysVol\abc123.net\Policies\{8C419E64-5BA7-45F8-8893-1A7919EBB906}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following: 

         ......................... ATLAS-V2-DC failed test SystemLog

      Starting test: Topology

         ......................... ATLAS-V2-DC passed test Topology

      Starting test: VerifyEnterpriseReferences

         ......................... ATLAS-V2-DC passed test

         VerifyEnterpriseReferences

      Starting test: VerifyReferences

         ......................... ATLAS-V2-DC passed test VerifyReferences

      Starting test: VerifyReplicas

         ......................... ATLAS-V2-DC passed test VerifyReplicas

      Starting test: DNS

         DNS Tests are running and not hung. Please wait a few minutes...

         ......................... ATLAS-V2-DC passed test DNS

   Running partition tests on : ForestDnsZones

      Starting test: CheckSDRefDom

         ......................... ForestDnsZones passed test CheckSDRefDom

      Starting test: CrossRefValidation

         ......................... ForestDnsZones passed test

         CrossRefValidation

   Running partition tests on : DomainDnsZones

      Starting test: CheckSDRefDom

         ......................... DomainDnsZones passed test CheckSDRefDom

      Starting test: CrossRefValidation

         ......................... DomainDnsZones passed test

         CrossRefValidation

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

   Running partition tests on : abc123

      Starting test: CheckSDRefDom

         ......................... abc123 passed test CheckSDRefDom

      Starting test: CrossRefValidation

         ......................... abc123 passed test CrossRefValidation

   Running enterprise tests on : abc123.net

      Starting test: DNS

         ......................... abc123.net passed test DNS

      Starting test: LocatorCheck

         ......................... abc123.net passed test LocatorCheck

      Starting test: FsmoCheck

         ......................... abc123.net passed test FsmoCheck

      Starting test: Intersite

         ......................... abc123.net passed test Intersite
```

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-07*

Hello @Sameer Sheikh  ,

Thank you for posting here.

To better understand your question, please confirm the following information at your convenience:

1.What is the forest functional level and domain functional level of your AD environment?  

Please run commands below to check

(Get-ADForest).ForestMode  

(Get-ADDomain).DomainMode

For example:  

2.How many Domain Controllers in your AD forest?  

Please run nltest /dclist:domain.com to check.

3.Please check if SYSVOL is FRS or DFSR by check the registry on all Domain Controllers.

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.

4.Based on the description "I was able to complete every step successfully. I thought everything worked just fine. Unfortunately, it did not.", did you mean during the migration process from beginning to end, no errors were reported?

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
