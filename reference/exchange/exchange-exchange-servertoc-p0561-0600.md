---
title: "Exchange Server — pages 561-600"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0561-0600
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0561-0600
family: exchange
documentKind: "doc"
abstract: "Error message when upgrading Cumulative Updates in Exchange Article • 04/30/2025 APPLIES TO: 2016 2019 Subscription Edition This article describes how to fix errors when you try to install or upgrade to a Cumulative Update using the setup of Exchange Server. Symptoms The symptom"
---

# Exchange Server — pages 561-600

<!-- p.561 -->

Error message when upgrading Cumulative
Updates in Exchange
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

This article describes how to fix errors when you try to install or upgrade to a Cumulative
Update using the setup of Exchange Server.

Symptoms
The symptom of a Cumulative Update upgrade failure is the AccessDenied error message.

Cause
The AccessDenied error message occurs when the built-in administrators don't have write
permissions for the CustomSD registry key when they try to record/log the event in the
application log.

After the Cumulative Update attempt fails, you might notice the following data in the setup log
immediately after the end of the Start-PreFileCopy task:

  text

  [12/05/2022 12:22:06.0909] [1] Ending processing Start-PreFileCopy
  [12/05/2022 12:22:06.0914] [0] The log file path for the language pack removal
  operation is set to 'C:\ExchangeSetupLogs'.
  [12/05/2022 12:22:06.0924] [0] [WARNING] Exception has been thrown by the target
  of an invocation.
  [12/05/2022 12:22:06.0939] [0] [WARNING] Cannot open log for source
  'MSExchangeSetup'. You may not have write access.
  [12/05/2022 12:22:06.0939] [0] [WARNING] Access is denied
  [12/05/2022 12:22:06.0939] [0] CurrentResult SetupLauncherHelper.loadassembly:444:
  1
  [12/05/2022 12:22:06.0939] [0] The Exchange Server setup operation didn't
  complete. More details can be found in ExchangeSetup.log located in the
  <SystemDrive>:\ExchangeSetupLogs folder.
  [12/05/2022 12:22:06.0939] [0] CurrentResult main.run:235: 1
  [12/05/2022 12:22:06.0939] [0] CurrentResult setupbase.maincore:396: 1
  [12/05/2022 12:22:06.0939] [0] End of Setup
  [12/05/2022 12:22:06.0939] [0] **********************************************

In a working scenario, you see the following lines in the setup log data after the Start-
PreFileCopy task:

<!-- p.562 -->

  text

  [04/21/2022 08:31:54.0092] [1] Ending processing Start-PreFileCopy
  [04/21/2022 08:31:54.0100] [0] The log file path for the language pack removal
  operation is set to 'C:\ExchangeSetupLogs'.
  [04/21/2022 08:31:54.0106] [0] **************
  [04/21/2022 08:31:54.0106] [0] Setup will run the task 'remove-InstalledLanguages'

Before removing and reinstalling languages, we need to log the event with ID:1000 with the
source Microsoft Exchange Setup.

  text

  Log Name:      Application
  Source:        MSExchangeSetup
  Date:          12/5/2022 11:33:03 AM
  Event ID:      1000
  Task Category: Microsoft Exchange Setup
  Level:         Information
  Keywords:      Classic
  User:          N/A
  Description: Exchange Setup (build 15.1.2507.6:Languages) was started.

The following test command in Windows PowerShell tries to record the event with ID:1000 in
the application log:

  PowerShell

  Write-EventLog -LogName Application -Source MSExchangeSetup -EntryType Information
  -EventId 1000 -Message "This is a test message"

If you're experiencing the issue, the command results in the AccessDenied error message as
shown in the following screenshot:

This result indicates an issue in accessing the application log to record the event ID:1000.

If you're experiencing the issue, verify the output of the CustomSD registry key by running the
following command in Windows PowerShell:

  PowerShell

<!-- p.563 -->

  Get-ItemProperty
  "Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Eventlog\Applicati
  on"

The output of this command is:

  PowerShell

  PrimaryModule       : Application
  DisplayNameFile     : C:\Windows\system32\wevtapi.dll
  DisplayNameID       : 256
  File                : C:\Windows\system32\winevt\Logs\Application.evtx
  MaxSize             : 209715200
  Retention           : 0
  RestrictGuestAccess : 1
  AutoBackupLogFiles : 0
  CustomSD            : O:BAG:SYD:(A;;0xf0005;;;SY)(**A;;0x5;;;BA**)(A;;0x1;;;S-1-5-
  32-573)(A;;0x1;;;S-1-5-21-3081388108-1913582122-755921781-506353)
  PSPath              :
  Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Se
  rvices\Eventlog\Application
  PSParentPath        : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\Sy
  stem\CurrentControlSet\Services\Eventlog
  PSChildName         : Application
  PSProvider          : Microsoft.PowerShell.Core\Registry

There are three distinct rights that pertain to event logs:

     Read: Corresponds to bit 1 in the Access rights field of the ACE String.
     Write: Corresponds to bit 2 in the Access rights field of the ACE String.
     Clear: Corresponds to bit 4 in the Access rights field of the ACE String.

If we attempt to read the access rights field of the ACE String (A;;0x5;;;BA) , these access
rights translate to:

     A: Allow
     BA: Built-in Admins
     0x5: Read + Clear

These results indicate that writing events in the application log isn't allowed, which is the cause
of the AccessDenied message.

Resolution
To fix the issue caused by the AccessDenied error message, do the following steps:

<!-- p.564 -->

1. Update the access rights from (A;;0x5;;;BA) to (A;;0x7;;;BA) in the following locations:

        HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\EventLog\System

        HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\EventLog\Application

  Updating the access right grants the required Write permission.

2. Restart the upgrade process.

<!-- p.565 -->

Exchange Server supportability matrix
APPLIES TO:      2016     2019      Subscription Edition

The Microsoft Exchange Server Supportability Matrix provides a central source of information
for Exchange admins to understand the supported configurations and versions of Exchange
Server.

Supported versions and builds
The following table lists the supported versions and builds of Exchange Server.

                                                                                   ﾉ   Expand table

 Version                                                              Build(s)

 Exchange Server SE                                                   RTM

  ２ Warning

  Exchange Server 2013 has reached end of support on April 11, 2023.

  Exchange Server 2016 and Exchange Server 2019 have reached end of support on
  October 14, 2025.

Supported operating systems
The following table lists the supported operating systems for Exchange Server and the
Exchange Management Tools role.
In-place upgrade of the server OS between major versions (for example, Windows Server 2022
to Windows Server 2025) with Exchange Server installed is not supported.

                                                                                   ﾉ   Expand table

 Version                          Operating Systems        Server           Installation Options
                                                           Edition

 Exchange Server SE               Windows Server 2025      Datacenter       Desktop Experience
                                  Windows Server 2022      Standard         Server Core
                                  Windows Server 2019                       (recommended)

<!-- p.566 -->

 Version                          Operating Systems       Server        Installation Options
                                                          Edition

 Exchange Server 2019             Windows Server 2025     Datacenter    Desktop Experience
                                  Windows Server 2022     Standard      Server Core
                                  Windows Server 2019                   (recommended)

 Exchange Server 2016             Windows Server 2016     Datacenter    Desktop Experience
                                  Windows Server 2012     Standard
                                  R2
                                  Windows Server 2012

 Exchange Server SE Management    Windows Server 2025     Datacenter    Desktop Experience
 Tools                            Windows Server 2022     Standard
                                  Windows Server 2019
                                  Windows 11
                                  Windows 10 (64-bit
                                  edition)

 Exchange Server 2019             Windows Server 2025     Datacenter    Desktop Experience
 Management Tools                 Windows Server 2022     Standard
                                  Windows Server 2019
                                  Windows 11
                                  Windows 10 (64-bit
                                  edition)

 Exchange Server 2016             Windows Server 2016     Datacenter    Desktop Experience
 Management Tools                 Windows Server 2012     Standard
                                  R2
                                  Windows Server 2012
                                  Windows 10 (64-bit
                                  edition)

  ２ Warning

  Windows Server 2012 and Windows Server 2012 R2 extended support has ended on
  October 10, 2023. These servers will no longer receive Windows Security Updates without
  an ESU. We strongly recommend migrating to a supported version as soon as possible!

Supported Active Directory environments
The following table lists the supported Active Directory environments for Exchange Server.
An Active Directory server refers to both writable Global Catalog (GC) servers and writable
Domain Controllers (DC). Read-only GCs and read-only DCs aren't supported.

<!-- p.567 -->

  ） Important

  For Exchange installations in environments where a Windows Server 2025 Active Directory
  domain controller holds the Schema Master FSMO role:

  Before you run any PrepareAD operations for Exchange, make sure the Windows Server
  2025 acting as the Schema Master has the November 2025         or later cumulative update
  installed. This update is required to prevent Active Directory replication issues .

                                                                                ﾉ   Expand table

 Version                       Active Directory servers         Forest Functional Levels

 Exchange Server SE            Windows Server 2025              Windows Server 2016
                               Windows Server 2022              Windows Server 2012 R2
                               Windows Server 2019
                               Windows Server 2016
                               Windows Server 2012 R2

 Exchange Server 2019          Windows Server 2025              Windows Server 2016
                               Windows Server 2022              Windows Server 2012 R2
                               Windows Server 2019
                               Windows Server 2016
                               Windows Server 2012 R2

 Exchange Server 2016          Windows Server 2022              Windows Server 2016
                               Windows Server 2019              Windows Server 2012 R2
                               Windows Server 2016              Windows Server 2012
                               Windows Server 2012 R2
                               Windows Server 2012

  ７ Note

  Support for Windows Server 2025 Active Directory servers was introduced with Exchange
  Server 2019 CU14 (2024H1).
  Support for Windows Server 2022 Active Directory servers was introduced with Exchange
  Server 2019 CU12 (2022H1) and Exchange Server 2016 CU23 (2022H1).

Supported Browsers for Outlook on the web
The following table lists the supported web browsers for use with Outlook on the web (OWA)
and Exchange Admin Center (EAC) in Exchange Server.

<!-- p.568 -->

Current release of Firefox/Chrome refers to the latest version or the immediately previous
version.

                                                                                 ﾉ   Expand table

 Version                       Browsers                          S/MIME Support

 Exchange Server SE OWA /      Microsoft Chromium Edge           Yes
 EAC                           Microsoft Chromium Edge (IE       Yes
                               Mode)                             Yes
                               Microsoft Edge                    No
                               Current release of Firefox        Yes
                               Current release of Chrome         No
                               Current release of Safari

 Exchange Server SE OWA        Microsoft Edge                    S/MIME is not available in light
 Light                         Current release of Safari         mode

 Exchange Server 2019 OWA /    Microsoft Chromium Edge           Yes
 EAC                           Microsoft Chromium Edge (IE       Yes
                               Mode)                             Yes
                               Microsoft Edge                    No
                               Current release of Firefox        Yes
                               Current release of Chrome         No
                               Current release of Safari

 Exchange Server 2019 OWA      Microsoft Edge                    S/MIME is not available in light
 Light                         Current release of Safari         mode

 Exchange Server 2016 OWA /    Microsoft Chromium Edge           No
 EAC                           Microsoft Chromium Edge (IE       Yes
                               Mode)                             No
                               Microsoft Edge                    No
                               Current release of Firefox        No
                               Current release of Chrome         No
                               Current release of Safari

 Exchange Server 2016 OWA      Microsoft Edge                    S/MIME is not available in light
 Light                         Current release of Firefox        mode
                               Current release of Chrome
                               Current release of Safari

Supported Email Clients
The following table lists the supported Microsoft email clients for Exchange Server.

                                                                                 ﾉ   Expand table

<!-- p.569 -->

 Version                             Clients

 Exchange Server SE                  Microsoft 365 Apps for enterprise
                                     Outlook 2024
                                     Outlook 2021
                                     Outlook 2019
                                     Outlook 2016
                                     Outlook for Mac (Microsoft 365, 2019)
                                     Outlook for iOS
                                     Outlook for Android

 Exchange Server 2019                Microsoft 365 Apps for enterprise
                                     Outlook 2024
                                     Outlook 2021
                                     Outlook 2019
                                     Outlook 2016
                                     Outlook for Mac (Microsoft 365, 2019)
                                     Outlook for iOS
                                     Outlook for Android

 Exchange Server 2016                Microsoft 365 Apps for enterprise
                                     Outlook 2024
                                     Outlook 2021
                                     Outlook 2019
                                     Outlook 2016
                                     Outlook for Mac (Microsoft 365, 2019)
                                     Outlook for iOS
                                     Outlook for Android

Additional Requirements and Information
Exchange Server also has supportability requirements for some of its prerequisites, namely
.NET Framework and Windows PowerShell.

.NET Framework
Releases of .NET Framework that aren't listed in the table below aren't supported on any
supported release of Exchange Server. These releases include minor and patch-level releases of
.NET Framework.

                                                                                   ﾉ   Expand table

 Version                            Windows                 .NET Framework

 Exchange Server SE                 Windows Server 2025     .NET Framework 4.8.1   (recommended)
                                    Windows Server 2022     or

<!-- p.570 -->

 Version                              Windows               .NET Framework

                                                            .NET Framework 4.8

 Exchange Server 2019 CU15 (2025H1)   Windows Server 2025   .NET Framework 4.8.1   (recommended)
 Exchange Server 2019 CU14 (2024H1)   Windows Server 2022   or
                                                            .NET Framework 4.8

 Exchange Server 2019 CU15 (2025H1)   Windows Server 2019   .NET Framework 4.8
 Exchange Server 2019 CU14 (2024H1)

 Exchange Server 2016 CU23            Any supported OS      .NET Framework 4.8

Windows PowerShell
Exchange Server SE, Exchange Server 2019 and Exchange Server 2016 support only the version
of PowerShell included in Windows Server. Exchange Server doesn't support the use of
Windows Management Framework (WMF) add-ons on any version of Windows PowerShell or
Windows. If there are other installed versions of Windows PowerShell or PowerShell Core that
support side-by-side operation, Exchange Server will use only the version that it requires.

For additional information, see the following resources:

      Exchange Server SE system requirements and prerequisites
      Exchange Server 2019 system requirements and prerequisites
      Exchange Server 2016 system requirements and prerequisites
      Exchange Server 2013 system requirements and prerequisites
      Exchange Server build numbers and release dates

 Last updated on 11/12/2025

<!-- p.571 -->

Exchange Server virtualization
Article • 04/30/2025

APPLIES TO:           2016   2019     Subscription Edition

You can deploy Exchange Server 2016 and Exchange Server 2019 in a virtualized environment.
This topic provides an overview of the scenarios that are supported for deploying Exchange on
a hardware virtualization software.

The following terms are used in this discussion on Exchange virtualization:

      Cold boot: When bringing a system from a power-off state into a clean start of the
      operating system, the action is a cold boot. No operating system state has been persisted
      in this case.

      Saved state: When a virtual machine is powered off, hypervisors typically have the ability
      to save the state of the virtual machine; so when the machine is powered back on, it
      returns to that saved state rather than going through a cold boot startup.

      Planned migration: When a system administrator initiates the move of a virtual machine
      from one hypervisor host to another, the action is a planned migration. The action could
      be a single migration, or a system administrator could configure an automation to move
      the virtual machine on a timed basis. A planned migration could also be the result of
      some other event that occurs in the system, other than a hardware or software failure.

      The key point of a planned migration is that the Exchange virtual machine is operating
      normally and needs to be relocated for some reason. This relocation can be done via
      technology (for example, Live Migration or vMotion). However, if the Exchange virtual
      machine or the hypervisor host where the virtual machine is located experiences some
      sort of a failure condition, the outcome isn't characterized as a planned migration.

Requirements for hardware virtualization
Microsoft supports Exchange 2016 and Exchange 2019 in production on a hardware
virtualization software only when all the following conditions are true:

      The hardware virtualization software is running one of the following:

         Any version of Windows Server with Hyper-V technology or Microsoft Hyper-V Server

         Any third-party hypervisor that has been validated under the Windows Server
         Virtualization Validation Program   .

<!-- p.572 -->

         ７ Note

         Deployment of Exchange 2016 or Exchange 2019 on Infrastructure-as-a-Service
         (IaaS) providers is supported if all supportability requirements are met. In the case
         of providers who are provisioning virtual machines, these requirements include
         ensuring that the hypervisor being used for Exchange virtual machines is fully
         supported, and that the infrastructure to be utilized by Exchange meets the
         performance requirements that were determined during the sizing process.
         Deployment on Microsoft Azure virtual machines is supported if all storage
         volumes used for Exchange databases and database transaction logs (including
         transport databases) are configured for Azure Premium Storage.

    The Exchange guest virtual machine has the following conditions:

       It's running Exchange 2016 or Exchange 2019.

       It's deployed on a supported version of Windows Server for Exchange.

For deployments of Exchange 2016 or Exchange 2019:

    All Exchange server roles are supported in a virtual machine.

    Exchange server virtual machines (including Exchange virtual machines that are part of a
    database availability group, or DAG) may be combined with host-based failover clustering
    and migration technology as long as the virtual machines are configured such that they
    won't save and restore state on disk when moved or taken offline. All failover activity
    occurring at the hypervisor level must result in a cold boot when the virtual machine is
    activated on the target node. All planned migration must either result in shutdown and
    cold boot or in an online migration that makes use of a technology like Hyper-V Live
    Migration. Hypervisor migration of virtual machines is supported by the hypervisor
    vendor; therefore, you must ensure that your hypervisor vendor has tested and supports
    migration of Exchange virtual machines. Microsoft supports Hyper-V Live Migration of
    these virtual machines.

    Only a management software (for example, antivirus software, backup software, or virtual
    machine management software) can be deployed on the physical host machine. No other
    server-based applications (for example, Exchange, SQL Server, Active Directory, or SAP)
    should be installed on the host machine. The host machine should be dedicated to
    running guest virtual machines.

    Some hypervisors include features for taking snapshots of virtual machines. Virtual
    machine snapshots capture the state of a virtual machine while it's running. This feature
    enables you to take multiple snapshots of a virtual machine and then revert the virtual

<!-- p.573 -->

  machine to any of the previous states by applying a snapshot to the virtual machine.
  However, virtual machine snapshots aren't application aware, and using them can have
  unintended and unexpected consequences for a server application that maintains state
  data, such as Exchange. As a result, making virtual machine snapshots of an Exchange
  guest virtual machine isn't supported.

  Many hardware virtualization products allow you to specify the number of virtual
  processors that should be allocated to each guest virtual machine. The virtual processors
  located in the guest virtual machine share a fixed number of physical processor cores in
  the physical system. Exchange supports a virtual processor-to-physical processor core
  ratio no greater than 2:1, although we recommend a ratio of 1:1. For example, a dual
  processor system using quad core processors contains a total of 8 physical processor
  cores in the host system. On a system with this configuration, don't allocate more than a
  total of 16 virtual processors to all guest virtual machines combined.

  When calculating the total number of virtual processors required by the host machine,
  you must also account for both I/O and operating system requirements. In most cases,
  the equivalent number of virtual processors required in the host operating system for a
  system hosting Exchange virtual machines is 2. This value should be used as a baseline for
  the host operating system virtual processor when calculating the overall ratio of physical
  cores to virtual processors. If performance monitoring of the host operating system
  indicates you're consuming more processor utilization than the equivalent of 2
  processors, you should reduce the count of virtual processors assigned to guest virtual
  machines accordingly and verify that the overall virtual processor-to-physical core ratio is
  no greater than 2:1.

  It's possible that guest virtual machines may be prevented from directly communicating
  with Fibre Channel or SCSI host bus adapters (HBAs) installed in the host machine. In this
  event, you must configure the adapters in the host machine's operating system and
  present the logical unit numbers (LUNs) to guest virtual machines as either a virtual disk
  or a pass-through disk.

  The only supported way to send emails to external domains from Azure compute
  resources is via an SMTP relay (also known as an SMTP smart host). The Azure compute
  resource sends the email to the SMTP relay, and then the SMTP relay provider delivers the
  email to the external domain. Microsoft Exchange Online Protection is one provider of an
  SMTP relay, but there are a number of third-party providers as well. For more information,
  see Troubleshoot outbound SMTP connectivity issues in Azure.

Host machine storage requirements

<!-- p.574 -->

The minimum disk space requirements for each host machine are described in the following
list:

        Host machines in some hardware virtualization applications may require storage space for
        an operating system and its components. Additional storage space is also required to
        support the operating system's paging file, management software, and crash recovery
        (dump) files.

        Some hypervisors maintain files on the host machine that are unique to each guest virtual
        machine. For example, in a Hyper-V environment, a temporary memory storage file (BIN
        file) is created and maintained for each guest machine. The size of each BIN file is equal
        to the amount of memory allocated to the guest machine. In addition, other files may also
        be created and maintained on the host machine for each guest machine.

        If your host machine is running Windows Server 2012 Hyper-V or Hyper-V 2012, and
        you're configuring a host-based failover cluster that will host Exchange Mailbox servers in
        a DAG, we recommend following the guidance in KB2872325            .

Exchange storage requirements
Requirements for storage connected to a virtualized Exchange server are as follows:

        Each Exchange guest machine must be allocated sufficient storage space on the host
        machine for the fixed disk that contains the guest's operating system, any temporary
        memory storage files in use, and related virtual machine files that are hosted on the host
        machine. In addition, for each Exchange guest machine, you must also allocate sufficient
        storage for the message queues and for the databases and log files on Mailbox servers.

        The storage used by the Exchange guest machine for storage of Exchange data (for
        example, mailbox databases and transport queues) can be virtual storage of a fixed size
        (for example, fixed virtual hard disks (VHD or VHDX) in a Hyper-V environment), dynamic
        virtual storage when using VHDX files with Hyper-V, SCSI pass-through storage, or
        Internet SCSI (iSCSI) storage. Pass-through storage is storage that's configured at the host
        level and dedicated to one guest machine. All storage used by an Exchange guest
        machine for storage of Exchange data must be block-level storage because Exchange
        doesn't support the use of network attached storage (NAS) volumes, other than in the
        SMB 3.0 scenario outlined later in this topic. Also, NAS storage that's presented to the
        guest as block-level storage via the hypervisor isn't supported.

        Fixed VHDs may be stored on SMB 3.0 files that are backed by block-level storage if the
        guest machine is running on Windows Server 2012 Hyper-V (or a later version of Hyper-
        V). The only supported usage of SMB 3.0 file shares is for storage of fixed VHDs. Such file

<!-- p.575 -->

     shares can't be used for direct storage of Exchange data. When using SMB 3.0 file shares
     to store fixed VHDs, the storage backing the file share should be configured for high
     availability to ensure the best possible availability of the Exchange service.

     Storage used by Exchange should be hosted in disk spindles that are separate from the
     storage that's hosting the guest virtual machine's operating system.

     Configuring iSCSI storage to use an iSCSI initiator inside an Exchange guest virtual
     machine is supported. However, there is reduced performance in this configuration if the
     network stack inside a virtual machine isn't full-featured (for example, not all virtual
     network stacks support jumbo frames).

Exchange memory requirements and
recommendations
Some hypervisors have the ability to oversubscribe/overcommit or dynamically adjust the
amount of memory available to a specific guest machine based on the perceived usage of
memory in the guest machine as compared to the needs of other guest machines managed by
the same hypervisor. This technology makes sense for workloads in which memory is needed
for brief periods of time and then can be surrendered for other uses. However, it doesn't make
sense for workloads that are designed to use memory on an ongoing basis. Exchange (like
many server applications with optimizations for performance that involve caching of data in
memory) is susceptible to poor system performance and an unacceptable client experience if it
doesn't have full control over the memory allocated to the physical or virtual machine on which
it's running. As a result, using dynamic memory or memory overcommit features for Exchange
isn't supported.

Host-based failover clustering and migration for
Exchange
The following are answers to some frequently asked questions about host-based failover
clustering and migration technology with Exchange DAGs:

     Does Microsoft support third-party migration technology?

     Microsoft can't make support statements for the integration of third-party hypervisor
     products using these technologies with Exchange, because these technologies aren't part
     of the Server Virtualization Validation Program (SVVP). The SVVP covers the other aspects
     of Microsoft support for third-party hypervisors. You need to ensure that your hypervisor
     vendor supports the combination of their migration and clustering technology with

<!-- p.576 -->

Exchange. If your hypervisor vendor supports their migration technology with Exchange,
Microsoft supports Exchange with their migration technology.

How does Microsoft define host-based failover clustering?

Host-based failover clustering refers to any technology that provides the automatic ability
to react to host-level failures and start affected virtual machines on alternate servers. Use
of this technology is supported given that, in a failure scenario, the virtual machine is
coming up from a cold boot on the alternate host. This technology helps to make sure
that the virtual machine never comes up from a saved state that's persisted on disk
because it will be stale relative to the rest of the DAG members.

What does Microsoft mean by migration support?

Migration technology refers to any technology that allows a planned move of a virtual
machine from one host machine to another host machine. This move could also be an
automated move that occurs as part of resource load balancing, but it isn't related to a
failure in the system. Migrations are supported as long as the virtual machines never
come up from a saved state that's persisted on disk. This means that technology that
moves a virtual machine by transporting the state and virtual machine memory over the
network with no perceived downtime is supported for use with Exchange. A third-party
hypervisor vendor must provide support for the migration technology, while Microsoft
provides support for Exchange when used in this configuration.

<!-- p.577 -->

Plan Exchange 2016 integration with
SharePoint and Skype for Business
Article • 04/30/2025

APPLIES TO:        2016      2019    Subscription Edition

Exchange 2016 integration with SharePoint Server 2016 and Skype for Business allow for
services that provide the ability to preserve, archive, and then quickly search email, documents,
and other content. Together, these enterprise applications make possible scenarios such as
eDiscovery and collaboration using site mailboxes to let your organization preserve important
data. Critical in most organizations these days is the ability to archive and then locate email
and documents as required to meet compliance and regulatory requirements. You can use
Exchange 2016 along with SharePoint 2016 and Skype for Business to:

      Archive Exchange mailboxes

      Archive Skype for Business content

      Preserve SharePoint Server 2016 documents and websites

      Search across stores using eDiscovery

      Authenticate seamlessly across servers

The eDiscovery Center introduced in SharePoint 2013 provides content identification,
preservation, collection, processing, and analysis. In an Exchange environment, eDiscovery lets
you archive content discovered across SharePoint Server 2016, Skype for Business,
andExchange. You can use the eDiscovery Center to create eDiscovery Case sites that are used
to organize in-place holds, queries, and exports for a specific case.

Exchange 2016, SharePoint Server 2016, and Skype for Business Server use the standard
protocol, Open Authorization (OAuth), for server-to-server authentication to provide the cross-
product functionality described here. Using the same protocol allows these applications to
seamlessly and securely authenticate to each other. The authorization method supports
authentication as an application by means of a linked account and user impersonation where
the access request is made in the user context. You can learn more about OAuth later in this
article in the Server-to-server authentication using OAuth section.

  ７ Note

  For enterprises that use Lync Server 2013, you can still make full use of the features
  described in this topic.

<!-- p.578 -->

Archive Skype for Business content in Exchange
2016
With Exchange 2016 and Lync Server 2013 deployed in an organization, you can configure
Skype for Business to archive instant message and on-line meeting content, including shared
presentations or documents in the user's Exchange 2016 mailbox. Archiving Skype for Business
data in Exchange 2016 allows you to apply retention policies to the data. Archived Skype for
Business content also surfaces in any eDiscovery searches. For more details about Skype for
Business archiving and how to deploy it, see the following topics:

     Planning for Archiving

     Deploying Archiving

Preserve documents in SharePoint Server 2016
You can create a query-based hold to preserve items that meet your specified criteria with an
In-Place Hold.

For example, Litigation Hold preserves until the hold is removed any deleted items as well as
original versions of modified items . You can optionally specify a hold duration that preserves a
mailbox item for the named duration period. If you specify a hold duration period, it's
calculated from the date a message is received or a mailbox item is created. For details, see
Create or remove an In-Place Hold.

For more details on eDiscovery see the following topics:

     In-Place eDiscovery in Exchange Server

     In-Place Hold and Litigation Hold in Exchange Server

     Configure eDiscovery in SharePoint Server

     What's new in eDiscovery in SharePoint Server

     Configure Exchange for SharePoint eDiscovery Center

Search across applications by using eDiscovery
SharePoint Server 2016 provides the eDiscovery Center to help you locate and then transfer
relevant content as needed to meet regulatory requirements. eDiscovery is the process of
finding, preserving, analyzing, and producing content in digital format required by litigation or
investigations. You can use eDiscovery across Exchange 2016, SharePoint Server 2016, and

<!-- p.579 -->

Skype for Business files. You can help protect content in-place that you've identified with
eDiscovery queries and then export the results into an offline format to hand off for legal
review. In-Place Hold in eDiscovery lets you:

      Protect content in-place and in real time at reduced storage costs, without affecting your
      users' daily work.

      Query to collect up-to-date, relevant content and statistics quickly answer questions.

      Export relevant content in an offline and portable format.

If your organization adheres to legal discovery requirements, that is, anything related to
organizational policy, compliance, or lawsuits, In-Place eDiscovery in Exchange Server 2016 can
help you perform discovery searches for relevant content within mailboxes. You can also use
In-Place eDiscovery in an Exchange hybrid environment to search on-premises and cloud-
based mailboxes in the same search.

When you configure server-to-server authentication betweenExchange 2016 and SharePoint
Server 2016 in on-premises deployments, administrators and compliance officers can use the
eDiscovery Center. For more information, see Configure Exchange for SharePoint eDiscovery
Center. In hybrid deployments, for more information see Using Oauth Authentication to
Support eDiscovery in an Exchange Hybrid Deployment

You can identify and reduce your data set by using keyword syntax, property restrictions, and
refinements. The query experience focuses on statistics for individual sources and query
fragments to help you make decisions about the content you're searching across. You can also
preview SharePoint 2016 and Exchange 2016 content to confirm that you have identified the
right set of results.

Server-to-server authentication using OAuth
The OAuth protocol is used by many web sites and web services to let clients access resources
without having to provide a username and password. An authorization server trusted by the
resource owner provides the client with an access token that grants access to a specific set of
resources for a specified period. Exchange 2016 allows other applications to use OAuth to
authenticate to Exchange. You'll need to configure the applications in Exchange as partner
applications.

There are two configuration objects used for OAuth andExchange 2016 partner applications:
AuthConfig and the partner application configuration.

      AuthConfig: Exchange 2016 Setup creates AuthConfig to publish the auth metadata. You
      only need to manage AuthConfig to provision a new certificate when the existing

<!-- p.580 -->

     certificate is close to expiration. When this happens, you can renew the existing certificate
     and configure the new certificate as the next certificate in the AuthConfig along with its
     effective date.

     Exchange 2016 Setup creates a self-signed certificate with the friendly name Microsoft
     Exchange Server Auth Certificate and replicates the certificate to all front-end servers in
     the Exchange organization. The certificate's thumbprint is specified in the authorization
     configuration for Exchange 2016, along with its service name, which is a well-known GUID
     that represents on-premises Exchange 2016. Exchange uses the authorization
     configuration to publish its auth metadata document.

     Partner applications: You enable partner applications by creating a partner application
     configuration to request access tokens from Exchange. Exchange 2016 provides the
      Configure-EnterprisePartnerApplication.ps1 script that lets you quickly and easily create

     partner application configurations and minimize configuration errors.

     When Exchange 2016 receives an access request from a partner application via Exchange
     Web Services (EWS), the following events take place.

        EWS parses the www-authenticate header of the https request that contains the access
        token signed by the calling server using its private key.

        The auth module validates the access token using the partner application
        configuration.

        The module then grants access to resources based on the RBAC permissions granted
        to the application. If the access token is on behalf of a user, the RBAC permissions
        granted to the user are checked.

        For example, if a user performs an eDiscovery search using the eDiscovery Center in
        SharePoint 2016, Exchange checks whether the user is a member of the Discovery
        Management role group or has the Mailbox Search role assigned and the mailboxes
        being searched are within the scope of the RBAC role assignment. For more details, see
        Permissions.

In on-premises deployments, Exchange 2016, SharePoint Server 2016, and Skype for Business
Server 2015 do not require an authorization server to issue tokens. Each application issues self-
signed tokens to access the resources provided by other applications. The application that
provides access to resources, for example Exchange 2016, trusts the self-signed tokens
presented by the calling application. Trust is established by creating a partner application
configuration for the calling application, which includes the calling application's ApplicationID,
certificate, and AuthMetadataUrl. Exchange 2016, SharePoint 2016, and Skype for Business
publish their auth metadata document in a well-known URL.

<!-- p.581 -->

Auth metadata URLs

                                                                                     ﾉ   Expand table

 Server                         AuthMetadataUrl

 Exchange 2016                   https://<serverfqdn>/autodiscover/metadata/json/1

 SharePoint Server 2016          https://<serverfqdn>/_layouts/15/metadata/json/1

 Skype for Business              https://<serverfqdn>/metadata/json/1

In hybrid deployments, you need to configure OAuth authorization protocol between your on-
premises Exchange 2016 and Exchange Online organizations. Hybrid deployments by default
continue to use the federation trust process.

Certain Exchange 2016 features are only fully available across your organization by using the
new OAuth protocol. For example, before you can use In-Place eDiscovery to search on-
premises and cloud-based mailboxes in an Exchange hybrid organization, you need to
configure OAuth authentication between your Exchange on-premises and Exchange Online
organizations. The Hybrid Configuration Wizard doesn't manage the OAuth authorization
connection. For more information, see Configure OAuth Authentication Between Exchange and
Exchange Online Organizations.

In online deployments, Exchange Online, SharePoint Online and Skype for Business Online
need to be configured for a modern authentication connection. Modern authentication brings
Active Directory Authentication Library (ADAL)-based sign in to Office 2013 Windows clients.
Office 2013 client applications sign in to the Microsoft 365 or Office 365 service to gain access
to Exchange Online, SharePoint Online, and Skype for Business Online. We recommend that
you enable Exchange Online for modern authentication when enabling modern authentication
for Skype for Business. Modern authentication is enabled by default in SharePoint Online. For
more information, see Enable or disable modern authentication for Outlook in Exchange
Online.

The per service default state of modern authentication is:

     Skype for Business Online - OFF by default

     Skype for Business Online - OFF by default

     SharePoint Online - ON by default.

  ） Important

<!-- p.582 -->

  The default Server Auth Certificate created by Exchange 2016 is valid for five years. You
  need to make sure that the authorization configuration includes a current certificate.

Manage SharePoint site mailboxes
In many organizations, information resides in two different stores: email in Exchange and
documents in SharePoint. There are two different interfaces to access these stores. This makes
for a disjointed user experience that impedes effective collaboration. Site mailboxes in
SharePoint let users collaborate effectively by bringing together Exchange emails and
SharePoint documents. For users, a site mailbox serves as a central filing cabinet, providing a
place to file project emails and documents that can only be accessed and edited by site
members. Site mailboxes are visible in Outlook 2016 to give users easy access to the email and
documents for the projects they care about. Additionally, the same set of content can be
accessed directly from the SharePoint site itself.

In a site mailbox, content is kept where it belongs. Exchange stores the email, providing users
with the same message view for email conversations that they use every day for their own
mailboxes. SharePoint stores the documents, which allows for document coauthoring and
versioning. Exchange synchronizes just enough metadata from SharePoint to create the
document view in Outlook (that is, document title, last modified date, last modified author, and
size).

You can provision and manage site mailboxes from SharePoint Server 2016. For more
information, including how to configure site mailboxes, see the following topics.

         Site Mailboxes

         Configure email integration for a SharePoint Server farm

Manage access to unified contact store
The unified contact store (UCS) feature provides a consistent contact experience across Office
products. This feature lets users store all contact information in their Exchange 2016 mailbox so
that the same contact information is available globally across Skype for Business, SharePoint,
Exchange, Outlook and Outlook on the web. When you deploy aSkype for Business Server and
publish the topology, UCS is enabled for all users by default and no additional action is
needed. For more information, see Configure Skype for Business Server to use the unified
contact store.

A user's contacts are automatically migrated to the Exchange 2016 server when the user:

<!-- p.583 -->

     Is assigned a user services policy that has UcsAllowed set to True.

     Was provisioned with an Exchange 2016 mailbox and has signed into the mailbox at least
     once.

     Logs in by using a Skype for Business rich client.

After you have installed SharePoint Server 2016 in an environment with Exchange 2016 and
you have configured server-to-server authentication between the two, users can initiate the
migration of existing contacts from SharePoint 2016 or Skype for Business Server 2015 to
Exchange 2016. For details, see Planning and Deploying Unified Contact Store.

Manage access to high-resolution user photos
The user photos feature lets you store high resolution user photos in Exchange 2016 that can
be accessed by client applications, including Outlook, Outlook on the web, SharePoint 2016,
Skype for Business, and mobile email clients. A low-resolution photo is also stored in Active
Directory. The cmdlet Set-UserPhoto stores a copy of a high resolution image in the user's
Exchange mailbox, and stores a 64x64 pixel copy of the photo as an image in the Active
Directory attribute thumbnailPhoto.

As with UCS, user photos allow your organization to maintain a consistent user profile photo
that can be consumed by client applications without requiring each application to have its own
user photos and different ways to add and manage them. Users can manage their own photos
by using Outlook on the web, SharePoint 2016 or Skype for Business. For detail about
managing photos on Outlook on the web, see Change your photo and account information in
Outlook on the web    .

<!-- p.584 -->

Exchange Server: Configure OAuth
authentication with SharePoint 2013 and
Lync 2013
07/23/2025

APPLIES TO:      2016      2019     Subscription Edition

Exchange 2016 supports partner applications such as SharePoint Server 2016 and Skype for
Business Server 2015 by using OAuth configuration with the script, Configure-
EnterpriseApplication.ps1 . You can automate the task using the script to more easily

configure authentication with partner applications and reduce configuration errors. The script
performs the following tasks:

   1. Configures an Enterprise partner application that self-issues OAuth tokens to successfully
     authenticate to Exchange.

   2. Assigns Role Based Access Control (RBAC) roles to the partner application to authorize it
     for calling specific Exchange Web Services APIs.

What do you need to know before you begin?
     Estimated time to complete: 5 minutes.

     The partner application needs to publish an authentication metadata document for
     Exchange 2016 to establish a direct trust to this application and accept authentication
     requests.

     Examples in this topic use the following default location of the \Scripts directory:
     C:\Program Files\Microsoft\Exchange Server\V15\Scripts .

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Partner applications - configure"
     entry in the Sharing and collaboration permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

<!-- p.585 -->

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Configure OAuth authentication with a partner
application
This procedure uses the Configure-EnterpriseApplication.ps1 script to configure OAuth
authentication with partner applications. Access to resources depends on the permissions
assigned to the partner application and/or the user it impersonates by using RBAC. After
configuring OAuth authentication from Exchange, the partner application can use Exchange
2016 resources.

   1. This example configures OAuth authentication for SharePoint 2016.

       Console

        Cd C:\Program Files\Microsoft\Exchange Server\V15\Scripts
        Configure-EnterprisePartnerApplication.ps1 -AuthMetaDataUrl
        https://sharepoint.contoso.com/_layouts/15/metadata/json/1 -ApplicationType
        SharePoint

   2. This example configures OAuth authentication for Skype for Business or Lync Server 2013.

       Console

        Cd C:\Program Files\Microsoft\Exchange Server\V15\Scripts
        Configure-EnterprisePartnerApplication.ps1 -AuthMetaDataUrl
        https://lync.contoso.com/metadata/json/1 -ApplicationType Lync

If Exchange 2016 also needs to access resources offered by the partner application, you must
also configure OAuth authentication in the partner application.

How do you know this worked?
To verify that you have successfully configured an enterprise partner application to
authenticate to Exchange 2016 , run the Get-PartnerApplication cmdlet in the Exchange
Management Shell to retrieve the configuration. You can also run the Test-OAuthConnectivity
cmdlet to test OAuth connectivity with a partner application for a user.

<!-- p.586 -->

Hybrid and on-premises deployments
  In hybrid deployments, you can use OAuth authentication between your on-premises
  Exchange 2016 organization and the Exchange Online organization. For more
  information, see Using Oauth Authentication to Support eDiscovery in an Exchange
  Hybrid Deployment.

  In on-premises deployments, you can configure server-to-server authentication between
  Exchange 2016 and SharePoint 2016 so administrators and compliance officers can search
  Exchange 2016 by using the SharePoint 2016 eDiscovery Center.. For more information,
  see Configure Exchange for SharePoint eDiscovery Center.

<!-- p.587 -->

Maintain the Exchange Server OAuth
certificate
Article • 04/18/2025

APPLIES TO:        2016     2019      Subscription Edition

General information
This documentation describes the required steps to rotate the Exchange Server Auth Certificate
without interrupting the Exchange service and before the current one expires.

   Tip

  You can also use the MonitorExchangeAuthCertificate          script. It performs the necessary
  steps of rotating the OAuth certificate automatically. It can also help you to replace the
  OAuth certificate if it has already expired.

The Auth Configuration and Auth Certificate are used by Microsoft Exchange server to enable
server-to-server authentication using the Open Authorization (OAuth) protocol standard. You
can find more information about it in the following article: Plan Exchange integration with
SharePoint and Skype for Business

The Auth Certificate is also used by several Exchange Server security features.

During the installation of the first Exchange server, the setup routine generates a self-signed
certificate with the friendly name Microsoft Exchange Server Auth Certificate , which is then
added to a new Auth Configuration. This certificate is automatically replicated to all front-end
servers in the Exchange organization. Exchange certificate servicelet performs the replication,
which is part of the MSExchangeServiceHost process. If you add more servers to your Exchange
organization, the servicelet takes care of replicating the certificate to all Exchange servers,
which were added to the organization.

The certificate, which is configured as current Auth Certificate can be queried by running the
following PowerShell (must be executed in Exchange Management Shell) query:

  PowerShell

  (Get-AuthConfig).CurrentCertificateThumbprint | Get-ExchangeCertificate | Format-
  List Subject, Thumbprint, NotAfter, NotBefore

<!-- p.588 -->

If the call fails with the following warning, it means that the current Auth Certificate is missing
on the server.

A special Rpc error occurs on server <Servername>: The certificate with thumbprint
<AuthCertificateThumbprint> was not found.

Follow the instructions mentioned in the "What are the steps to follow if the current certificate
has already expired or is missing" section to fix.

The certificate, which is configured as next Auth Certificate can be queried as followed:

  PowerShell

  (Get-AuthConfig).NextCertificateThumbprint | Get-ExchangeCertificate | Format-List
  Subject, Thumbprint, NotAfter, NotBefore

If the call fails with the same warning as for the current Auth Certificate, it means that the next
Auth Certificate isn't configured or is missing on the server.

Follow the instructions outlined in the "How to rotate the Exchange Server Auth Certificate" if
the current Auth Certificate is about to expire.

What are the steps to follow if the current
certificate has already expired or is missing?
In this case, it's required to immediately replace the old Auth Certificate with a new one. Follow
the instructions outlined in the resolutions section of the following support article: Can't sign in
to Outlook on the web or EAC if Exchange Server OAuth certificate is expired

How to rotate the Exchange Server Auth Certificate
It's important to replace the active Auth Certificate with a new one, before it expires. Doing so
ensures a smooth transition to a new certificate without interrupting the Exchange service. You
can follow the steps below to prepare and stage a new Auth Certificate.

  ） Important

  Please make sure that you have the latest Exchange Server Cumulative Update (CU)
  installed because it contains fixes that affect the corresponding Exchange feature.

   1. Generate a new Auth Certificate by running the following command:

<!-- p.589 -->

        PowerShell

        $newAuthCertificate = New-ExchangeCertificate -KeySize 2048 -
        PrivateKeyExportable $true -SubjectName "cn=Microsoft Exchange Server Auth
        Certificate" -FriendlyName "Microsoft Exchange Server Auth Certificate" -
        DomainName @()

   2. Don't overwrite the existing default SMTP certificate (Type 'N' and press enter):

        PowerShell

        Confirm
        Overwrite the existing default SMTP certificate?

        Current certificate: '<DefaultSMTPCertificateThumbprint>' (expires 12/30/2027
        2:39:08 PM)
        Replace it with certificate: '<NewCertificateThumbprint>' (expires 1/5/2028
        9:04:48 AM)
        [Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (default is "Y"): N

   3. Configure the Auth Certificate to become the new active one in 49 hours at the earliest:

        PowerShell

        Set-AuthConfig -NewCertificateThumbprint $newAuthCertificate.Thumbprint -
        NewCertificateEffectiveDate (Get-Date).AddHours(49)

Depending on the size of your Exchange organization it might take some time for the new
Auth Certificate to be deployed to all Exchange servers. Our recommendation is to plan for at
least 48 hours before the newly generated Auth Certificate becomes active. In large Exchange
environment it can take even longer.

A reference to the Auth Certificate is cached by the MSExchangeOWAAppPool and
MSExchangeECPAppPool application pool. You can recycle those application pools to refresh this

reference. You can do so by running the following commands from an elevated PowerShell
window:

  PowerShell

  Restart-WebAppPool MSExchangeOWAAppPool
  Restart-WebAppPool MSExchangeECPAppPool

The Exchange AuthAdmin servicelet, which is also a part of the MSExchangeServiceHost process,
is responsible for the final Auth Certificate publishing process. The servicelet is executed
immediately if the MSExchangeServiceHost service is restarted. Afterwards it's executed every 12

<!-- p.590 -->

hours and if it detects that the NewCertificateEffectiveDate is reached, it then publishes the
new Auth Certificate to make it the new active one.

To ensure that the AuthAdmin servicelet can start, you must enable the AuthAdminReadSession
when your Exchange Servers are installed in a child domain and the system mailbox is located
in the root domain. Otherwise, the AuthAdmin servicelet can't start. Run the following
PowerShell cmdlet if your Exchange servers are installed in the described constellation:

  PowerShell

  Set-OrganizationConfig -EnableAuthAdminReadSession:$true

You can query the last runtime of the AuthAdmin servicelet by running the following
PowerShell cmdlets:

  PowerShell

  [xml]$xml = Get-ExchangeDiagnosticInfo -Process "Microsoft.Exchange.ServiceHost"
  $xml.Diagnostics.Components.AnchorApplication.AnchorServiceComponents.CacheSchedul
  er.lastRunTime

Each run of the AuthAdmin servicelet is logged to the following directory:
<ExchangeInstallPath>\Logging\AuthAdminLogs

The servicelet generates a new event log entry when the rotation of the Auth Certificate is
successfully completed:

  text

  Log Name:      Application
  Source:        MSExchange AuthAdmin
  Date:          12/29/2022 5:56:13 AM
  Event ID:      2014
  Task Category: General
  Level:         Information
  Keywords:      Classic
  User:          N/A
  Description:   The current signing certificate for Exchange has been updated to
  certificate with thumbprint <NewExchangeCertificateThumbprint>.

Frequently asked questions
Question: Is it required to rerun the Hybrid Configuration Wizard (HCW) after the Auth
Certificate is replaced?

<!-- p.591 -->

Answer: Yes, we strongly recommend running the Hybrid Configuration Wizard (HCW) after the
active Auth Certificate is replaced.

Question: What should I do if the new Auth Certificate is missing on an Exchange server in a
different Active Directory (AD) site?

Answer: You can export the certificate by using the Export-ExchangeCertificate cmdlet and
import it via Import-ExchangeCertificate on a server in the other AD site. The certificate
servicelet takes care of the replication to the remaining Exchange servers located within the AD
site.

<!-- p.592 -->

Exchange Server post-installation tasks
07/01/2025

APPLIES TO:        2016       2019        Subscription Edition

Read the following topics to help you configure your new Exchange Server organization.

                                                                                                ﾉ   Expand table

 Topic                                  Description

 Enter your Exchange product key        Learn how to license your Exchange server.

 Configure mail flow and client         Learn how to configure mail flow to and from the Internet and
 access on Exchange servers             configure Exchange to accept client connections from the Internet.

 Verify Exchange Server installations   Learn how to verify that Exchange Server was installed successfully
                                        in your organization.

 Install the Exchange management        Learn how to install the Exchange Management Shell and Exchange
 tools                                  Toolbox on client workstations or other non-Exchange servers in
                                        your organization.

 Configure instant messaging            Learn how to configure instant messaging (IM) integration between
 integration with Outlook on the        Skype for Business Server and Outlook on the web (formerly known
 web in Exchange                        as Outlook Web App)

 Change the offline address book        Learn how to change the offline address book (OAB) generation
 generation schedule in Exchange        schedule on specific Exchange servers or for the whole organization

 Configure certificate based            Learn how to configure CBA in Exchange Server
 authentication in Exchange Server

 Edge Subscriptions                     Learn how to configure an EdgeSync Subscription between a new
                                        Edge Transport server in the perimeter network and the Exchange
                                        Mailbox servers in an internal Active Directory site.

If you've enabled the Scripting Agent in your Exchange organization, and you keep a
customized %ExchangeInstallPath%Bin\CmdletExtensionAgents\ScriptingAgentConfig.xml file on
all of your Mailbox servers, you need to copy that file to every new Mailbox server that you
deploy in your organization (the file isn't used on Edge Transport servers).

     The default value of %ExchangeInstallationPath% is %ProgramFiles%\Microsoft\Exchange
     Server\V15\ , but the actual value is wherever you installed Exchange on the server.

     The default name of the file on a new Exchange server is
      %ExchangeInstallPath%Bin\CmdletExtensionAgents\ScriptingAgentConfig.xml.sample . As

<!-- p.593 -->

     part of enabling the Scripting Agent in your organization, you need to rename this file to
     ScriptingAgentConfig.xml and customize it or replace it with your existing

     ScriptingAgentConfig.xml file.

For more information about the Scripting Agent in Exchange Server, see Scripting Agent.

<!-- p.594 -->

Enter your Exchange Server product key
07/01/2025

APPLIES TO:       2016      2019      Subscription Edition

A product key tells Exchange Server that you've purchased a Standard or Enterprise Edition
license. If the product key you purchased is for an Enterprise Edition license, it lets you mount
more than five databases per server in addition to everything that's available with a Standard
Edition license. If you want to read more about Exchange licensing, see Exchange Server
editions and versions.

If you don't enter a product key, your server is automatically licensed as a trial edition. The trial
edition functions just like an Exchange Standard Edition server and is helpful if you want to try
out Exchange before you buy it, or to run tests in a lab. The only difference is that you can only
use an Exchange server licensed as a trial edition for up to 180 days. If you want to keep using
the server beyond 180 days, you'll need to enter a product key or the Exchange admin center
(EAC) will start to show reminders that you need to enter a product key to license the server.

Note: If you want to install or activate Office, check out:

     Install Office

     Need help with your Office product key?

What do you need to know before you begin?
     Estimated time to complete this procedure: less than 5 minutes.

     To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
     Management Shell, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Product key" entry in the
     Exchange infrastructure and PowerShell permissions topic.

     After you license an Exchange Mailbox server, you need to restart the Microsoft Exchange
     Information Store service on the server after you enter the product key.

     You can upgrade from a Standard Edition license to an Enterprise Edition license. You
     can't downgrade from an Enterprise Edition license to a Standard Edition license without
     reinstalling Exchange.

<!-- p.595 -->

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online      , or Exchange Online Protection .

Use the EAC to enter the product key
 1. In the EAC. go to Servers > Servers, select the server you want to license, and then do
   either of the following steps:

         Click Edit    .

         In the details pane, click Enter Product Key. Note that this link is only available for
         unlicensed servers.

 2. The Exchange server properties window opens. On the General tab, do one of the
   following steps:

         License an unlicensed server: Enter the product key in the Enter a valid product key
         text boxes.

<!-- p.596 -->

           Change or upgrade the product key on a licensed server: Select Change product
           key and enter the product key in the Enter a valid product key text boxes. Note that
           you'll only see Change product key if the server is already licensed.

     When you're finished, click Save.

After you license a Mailbox server, do the following steps to restart the Microsoft Exchange
Information Store service:

   1. On the Exchange server, open the Windows Services console. For example:

           Run the command services.msc from the Run dialog, a Command Prompt window,
           or the Exchange Management Shell.

           Open Server Manager, and then click Tools > Services.

   2. In the list of services, right-click on Microsoft Exchange Information Store, and then click
     Restart.

Use the Exchange Management Shell to enter the
product key
To enter the product key in the Exchange Management Shell, use this syntax:

<!-- p.597 -->

  PowerShell

  Set-ExchangeServer <ServerName> -ProductKey <ProductKey>

Note that this command works to license an unlicensed server or to upgrade a licensed server
from a Standard Edition license to an Enterprise Edition license.

This example licenses the Exchange server named Mailbox01.

  PowerShell

  Set-ExchangeServer Mailbox01 -ProductKey 12345-12345-12345-12345-12345

For detailed syntax and parameter information, see Set-ExchangeServer.

After you license a Mailbox server, run the following command in the Exchange Management
Shell to restart the Microsoft Exchange Information Store service:

  PowerShell

  Restart-Service MSExchangeIS

How do you know this worked?
To verify that you've successfully licensed the Exchange server, do any of the following steps:

     In the EAC, go to Servers > Servers, and select the server you licensed. In the details
     pane, verify the Exchange edition value (Standard or Enterprise) and whether the value
     Licensed is present.

<!-- p.598 -->

In the Exchange Management Shell, replace <ServerName> with the name of the
Exchange server you licensed, and run the following command to verify the property
values:

  PowerShell

  Get-ExchangeServer <ServerName> | Format-List Name,Edition,*Trial*

In the Exchange Management Shell, run the following command to view the licensing
status of all Exchange servers in your organization:

  PowerShell

  Get-ExchangeServer | Format-Table -Auto Name,Edition,*Trial*

<!-- p.599 -->

Configure mail flow and client access on
Exchange servers
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

After you've installed Exchange Server 2016 or Exchange 2019 in your organization, you need
to configure Exchange for mail flow and client access. Without these additional steps, you
won't be able to send mail to the internet and external clients (for example, Microsoft Outlook,
and Exchange ActiveSync devices) won't be able to connect to your Exchange organization.

The steps in this topic assume a basic Exchange deployment with a single Active Directory site
and a single simple mail transport protocol (SMTP) namespace.

  ） Important

  This topic uses example values such as Mailbox01, contoso.com, mail.contoso.com, and
  172.16.10.11. Replace the example values with the server names, FQDNs, and IP addresses
  for your organization.

For additional management tasks related to mail flow and clients and devices, see Mail flow
and the transport pipeline and Clients and mobile.

What do you need to know before you begin?
      Estimated time to complete this task: 50 minutes

      You might receive certificate warnings when you connect to the Exchange admin center
      (EAC) website until you configure a secure sockets layer (SSL) certificate on the Mailbox
      server. You'll be shown how to do this later in this topic.

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

<!-- p.600 -->

Step 1: Create an internet Send connector
Before you can send mail to the internet, you need to create a Send connector on the Mailbox
server. For instructions, see Create a Send connector in Exchange Server to send mail to the
internet.

  ７ Note

  By default, a Receive connector named "Default Frontend <ServerName>_" is created
  when Exchange is installed. This Receive connector accepts anonymous SMTP connections
  from external servers. You don't need to do any additional configuration if this is the
  functionality you want. If you want to restrict inbound connections from external servers,
  modify the Default Frontend <Mailbox server> Receive connector on the Mailbox server.
  For more information, see Default Receive connectors created during setup.

Step 2: Add additional accepted domains
By default, Exchange uses the Active Directory domain where Setup /PrepareAD was run for
email addresses. If you want recipients to receive and send messages to and from another
domain, you need to add the domain as an accepted domain. For instructions, see Create
accepted domains and Configure Exchange to accept mail for multiple authoritative domains.

  ） Important

  To receive email from the internet for a domain, you need an MX resource record in your
  public DNS for that domain. Each MX record should resolve to the internet-facing server
  that receives email for your organization.

Step 3: Configure the default email address policy
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Email address policies" entry in the Email address and
address book permissions topic.

If you added an accepted domain in the previous step and you want that domain to be added
to every recipient in the organization, you need to update the default email address policy. For
instructions, see Modify email address policies and Apply email address policies to recipients.

  ７ Note
