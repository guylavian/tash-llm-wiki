---
title: "Failed to create the GPO for the domain ad.server.local."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195649/failed-to-create-the-gpo-for-the-domain-ad-server
question_id: 2195649
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Failed to create the GPO for the domain ad.server.local.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195649/failed-to-create-the-gpo-for-the-domain-ad-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello! Im trying to install Active directory on my windows server 2022. It should be top notch and is fully updated, but I have now spendt countless hours trying to configure active directory in the active directory domain service configuration wizzard. I am trying to add a new forrest, next, next, next, next, but after i press install i get the error message:

The operation failed because:  

Failed to create the GPO for the domain ad.server.local. 

"The system cannot find the file specified."

The error seams to happen after the wizzard windows says Configuring NETLOGON.

I have looked online but I only found two instances of the same problem from many years ago. I have tried reset the database with the command:

esentutl /p systemroot\security\database\secedit.sdb

This server has almost no configuration before. I have installed a DNS server, but its not configured. I have set a static IP and a default DNS to 8.8.8.8. We have a Fortinet Firewall at the center also. 

From the event viever I can see these warnings and errors: 

This computer is configured as a member of a workgroup, not as a member of a domain. The Netlogon service does not need to run in this configuration.

W32time is unable to communicate with Netlogon Service. This failure prevents NTPClient from discovering and using domain peers, besides causing problems with correct W32time service state being advertised by Netlogon. This could be a temporary condition that resolves itself shortly. If this warning repeats over a considerable period of time, ensure the Netlogon service is running and is responsive and restart W32time service to reintiaize the overall state. The error was 0x80070700: An attempt was made to logon, but the network logon service was not started.

Active Directory Domain Services has detected and deleted some possibly corrupted indices as part of initialization.  

These deleted indices will be rebuilt.

NTDS (1496,D,50) NTDSA:  Out of date NLS sort version detected on the database 'C:\Windows\NTDS\ntds.dit' for Locale 'en-US', index sort version: (SortId=00000001-57ee-1e5c-00b4-d0000bb1e11e, Version=0006020F0006020F), current sort version: (SortId=00000001-57ee-1e5c-00b4-d0000bb1e11e, Version=0006040300060403).

NTDS (1496,D,50) NTDSA: Database 'C:\Windows\NTDS\ntds.dit': The secondary index 'INDEX_00000003' of table 'datatable' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.

NTDS (1496,D,50) NTDSA:  Out of date NLS sort version detected on the database 'C:\Windows\NTDS\ntds.dit' for Locale 'en-US', index sort version: (SortId=00000001-57ee-1e5c-00b4-d0000bb1e11e, Version=0006020F0006020F), current sort version: (SortId=00000001-57ee-1e5c-00b4-d0000bb1e11e, Version=0006040300060403).

The DFS Replication service failed to contact domain controller  to access configuration information. Replication is stopped. The service will try again during the next configuration polling cycle, which will occur in 60 minutes. This event can be caused by TCP/IP connectivity, firewall, Active Directory Domain Services, or DNS issues.  

Additional Information:  

Error: 1355 (The specified domain either does not exist or could not be contacted.)

The DNS server could not open socket for address 10.10.20.158.  

Verify that this is a valid IP address for the server computer.  If it is NOT valid use the Interfaces dialog under Server Properties in the DNS Manager to remove it from the list of IP interfaces.  Then stop and restart the DNS server. (If this was the only IP interface on this machine and the DNS server may not have started as a result of this error.  In that case remove the DNS\Parameters\ ListenAddress value in the services section of the registry and restart.)  

If this is a valid IP address for this machine, make sure that no other application (e.g. another DNS server) is running that would attempt to use the DNS port.  

For more information, see "DNS server log reference" in the online Help.

The DNS server could not bind a Transmission Control Protocol (TCP) socket to address 10.10.20.158. The event data is the error code.  An IP address of 0.0.0.0 can indicate a valid "any address" configuration in which all configured IP addresses on the computer are available for use.  

Restart the DNS server or reboot the computer.

The DNS server could not open socket for address 10.10.20.158.  

Verify that this is a valid IP address for the server computer.  If it is NOT valid use the Interfaces dialog under Server Properties in the DNS Manager to remove it from the list of IP interfaces.  Then stop and restart the DNS server. (If this was the only IP interface on this machine and the DNS server may not have started as a result of this error.  In that case remove the DNS\Parameters\ ListenAddress value in the services section of the registry and restart.)  

If this is a valid IP address for this machine, make sure that no other application (e.g. another DNS server) is running that would attempt to use the DNS port.  

For more information, see "DNS server log reference" in the online Help.

The DNS server could not bind a User Datagram Protocol (UDP) socket to 10.10.20.158. The event data is the error code. Restart the DNS server or reboot your computer.

The DNS server computer currently does not have a DNS domain name.  Its DNS name is a single-label host name with no domain (for example:  "host" rather than "host.microsoft.com").  

You might have forgotten to configure a primary DNS domain for the server computer.  

Because the DNS server has only a single-label name, all zones created will have default records (SOA and NS) created using only this single-label name for the server's host name.  This can lead to incorrect and failed referrals when clients and other DNS servers use these records to locate this server by name.  

To correct this problem:  

-  Click Start, and then click Control Panel. 

-  Open System and Maintenance , and then open System.  

-  Click Change Settings, and then click Change.  4) Click either Domain or Workgroup, and then type the name of the domain or  workgroup you want the computer to join; the domain or workgroup name will be used as your DNS domain name.  

-  When prompted, restart the computer. 

After the computer restarts, the DNS server will attempt to fix up default records, substituting the new DNS name of this server for the old single-label name.  However, you should review the zone's SOA and NS records to ensure that they now use the correct domain name of this server.

I have not doen anything after installing the DNS server. I tried adding a forward looking zone parent, but that did not help.

I have tried these solutions for the W32time service problem :

https://community.spiceworks.com/topic/1093067-time-service-warning

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/netlogon-service-not-start-event-2112-7024
https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/netlogon-service-not-start-automatically

I also see that the share C:\Windows\SYSVOL does not exit. I have also tried creating one, but still no luck

I am at a loss for what to do next, do anybody have any tips?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-12-04*

Hello Magnus Gjerstad，

Thank you for providing detailed error information. Based on the information you provided, I can see that you are experiencing multiple issues. Firstly, you need to fix the DNS server issue. Your DNS server is unable to open the socket at address 10.10.20.158, which may be caused by an invalid IP address or another application that is using a DNS port. You need to make sure that the IP address is valid and that no other applications are using the DNS port. You also need to check that the DNS server is configured correctly, including the primary DNS domain name and interface settings. If you have installed a DNS server but have not configured it, follow the instructions in the Microsoft documentation.

Next, you need to address the Active Directory domain service. You try to add a new forrest, but after installation you receive the error message "Unable to create GPO for domain ad.server.local. system could not find the specified file." This may be caused by a corrupted Active Directory database. You can try using the ntdsutil utility to rebuild the indexes and clean up the database. You can also try using the DCDiag tool to check the health of the domain controller and see if there are any other errors or warnings.

Finally, you need to resolve the issue with the W32time service. You have received the error message "W32time cannot communicate with the Netlogon service". This may be caused by the Netlogon service not starting correctly. You can try starting the Netlogon service manually and make sure it is running. You can also try restarting the W32time service to reinitialise the overall state.

In short, you need to address each of these issues individually to ensure that the Active Directory domain services are running properly. If you need more help, please refer to the Microsoft documentation or contact Microsoft Customer Support.

Best regards,

Qiuyang

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-06*

Hello Magnus Gjerstad，

Based on the information you have provided, it seems that there are multiple issues with your Active Directory installation. 

The first issue is that you are unable to create a domain controller. This could be due to a corrupted Active Directory database. You have already tried using the ntdsutil utility to rebuild the indexes and clean up the database, but it seems that the machine is not an Active Directory Domain Controller. This could be because the Active Directory Domain Services role is not installed on the server. 

To install the Active Directory Domain Services role, you can follow these steps:

-  Open Server Manager and click on Add Roles and Features.

-  Click Next until you reach the Server Roles page.

-  Select Active Directory Domain Services and click Next.

-  Click Next until you reach the Features page.

-  Click Install to install the role.

Once the role is installed, you can try creating the domain controller again.

The second issue is that the DFS Replication service failed to contact the domain controller to access configuration information. This could be due to TCP/IP connectivity, firewall, Active Directory Domain Services, or DNS issues. You can try the following steps to resolve this issue:

-  Check the TCP/IP connectivity between the servers.

-  Check the firewall settings to ensure that the necessary ports are open.

-  Check the DNS settings to ensure that the domain controller is correctly registered in DNS.

-  Check the Active Directory Domain Services to ensure that it is running correctly.

If the above steps do not resolve the issue, you can try resetting the DFS Replication service by following these steps:

-  Open a command prompt as an administrator.

-  Type "net stop dfsr" and press Enter.

-  Type "wmic /namespace:\root\microsoftdfs path dfsrVolumeConfig where volumeGuid="GUID" call Reset" and press Enter. Replace "GUID" with the GUID of the affected volume.

-  Type "net start dfsr" and press Enter.

I hope this helps you resolve the issues you are experiencing with your Active Directory installation.

Best regards,

Qiuyang

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-05*

Hello! Thanks for the reply!

Firsty I checked the DNS.  I ran "netstat -aon | findstr :53", but could not find any other services using that port. I tried pinging the Ip with port 

ComputerName     : 10.10.20.158 

RemoteAddress    : 10.10.20.158 

RemotePort       : 53 

InterfaceAlias   : Ethernet 

SourceAddress    : 10.10.20.30 

TcpTestSucceeded : True 

.  

"This may be caused by a corrupted Active Directory database. You can try using the ntdsutil utility to rebuild the indexes and clean up the database."

I tried this but I get the response : 

ntdsutil: activate instance ntds 

The machine is not an Active Directory Domain Controller

So it does not even create the domain controller when i get the error message :

Failed to create the GPO for the domain ad.server.local.

"The system cannot find the file specified."

I also cant find the NTDS folder on the server. When i try "net start ntds" i get: 

System error 1058 has occurred. 

The service cannot be started, either because it is disabled or because it has no enabled devices associated with it.

I think the issue is that i can even create the domain controller.

This is my settings when trying to configure the active directory:

Configure this server as the first Active Directory domain controller in a new forest. 

The new domain name is "ad.JOTUNSERVER.com". This is also the name of the new forest. 

The NetBIOS name of the domain: AD 

Forest Functional Level: Windows Server 2016 

Domain Functional Level: Windows Server 2016 

Additional Options: 

  Global catalog: Yes 

  DNS Server: Yes 

  Create DNS Delegation: No 

Database folder: C:\Windows\NTDS 

Log file folder: C:\Windows\NTDS 

SYSVOL folder: C:\Windows\SYSVOL 

The DNS Server service will be configured on this computer. 

This computer will be configured to use this DNS server as its preferred DNS server. 

The password of the new domain Administrator will be the same as the password of the local Administrator of this computer. 

(I have tried changing the domain name a few times)

The i get:

The operation failed because: 

Failed to create the GPO for the domain ad.JOTUNSERVER.com. 

"The system cannot find the file specified."

The events after this is as follwed: 

NTDS (1496,D,50) NTDSA:  Out of date NLS sort version detected on the database 'C:\Windows\NTDS\ntds.dit' for Locale 'en-US', index sort version: (SortId=00000001-57ee-1e5c-00b4-d0000bb1e11e, Version=0006020F0006020F), current sort version: (SortId=00000001-57ee-1e5c-00b4-d0000bb1e11e, Version=0006040300060403).

NTDS (1496,D,50) NTDSA: Database 'C:\Windows\NTDS\ntds.dit': The secondary index 'INDEX_00000003' of table 'datatable' is out of date with sorting libraries. If used in this state (i.e. not rebuilt), it may appear corrupt or get further corrupted. If there is no later event showing the index being rebuilt, then please defragment the database to rebuild the index.

NTDS (1496,D,50) NTDSA:  Out of date NLS sort version detected on the database 'C:\Windows\NTDS\ntds.dit' for Locale 'en-US', index sort version: (SortId=00000001-57ee-1e5c-00b4-d0000bb1e11e, Version=0006020F0006020F), current sort version: (SortId=00000001-57ee-1e5c-00b4-d0000bb1e11e, Version=0006040300060403).

Active Directory Domain Services has detected and deleted some possibly corrupted indices as part of initialization.  

These deleted indices will be rebuilt.

The DFS Replication service failed to contact domain controller  to access configuration information. Replication is stopped. The service will try again during the next configuration polling cycle, which will occur in 60 minutes. This event can be caused by TCP/IP connectivity, firewall, Active Directory Domain Services, or DNS issues.  

Additional Information:  

Error: 1355 (The specified domain either does not exist or could not be contacted.)

And after that i still get:

ntdsutil: activate instance ntds 

The machine is not an Active Directory Domain Controller

I see in server manager under AD DS that i can "Promote this server to a domain controller"  but the status of it is a red X. 

I also have a debug file from windows named DCPROMO. I uploaded it to pastebin. 

https://pastebin.com/0HLeRHsK

I also have a debug file named NetSetup.txt

https://pastebin.com/tumLGq4G

And a debug file named Dfsr00045.txt 
https://pastebin.com/byNCyf3u

Dfsr00046.txt
https://pastebin.com/LXC4inBG

DfsrAPI_010.txt
https://pastebin.com/HrmsraX6
DfsrAPI_011.txt
https://pastebin.com/CciYv2ea

DcPromoui.txt
https://pastebin.com/DdtTxdWL

I have tried to kleep it clean, but some of these debugs files might be overlapping as i have tried to configure the active directory domain a lot of times with different domains and such
