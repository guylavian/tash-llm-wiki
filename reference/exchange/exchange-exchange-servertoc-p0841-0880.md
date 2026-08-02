---
title: "Exchange Server — pages 841-880"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0841-0880
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0841-0880
family: exchange
documentKind: "doc"
abstract: "Windows component RPC-over-HTTP- proxy isn't installed on this computer [RPCOverHTTPproxyNotInstalled] Article • 09/16/2024 Microsoft Exchange Server Setup displayed this error because the RPC-over-HTTP-proxy Windows component isn't installed on the computer. You must install th"
---

# Exchange Server — pages 841-880

<!-- p.841 -->

Windows component RPC-over-HTTP-
proxy isn't installed on this computer
[RPCOverHTTPproxyNotInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the RPC-over-HTTP-proxy
Windows component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature RPC-over-HTTP-proxy

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.842 -->

Windows component Server-Gui-Mgmt-
Infra isn't installed on this computer
[ServerGuiMgmtInfraNotInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the Server-Gui-Mgmt-Infra
Windows component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature Server-Gui-Mgmt-Infra

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.843 -->

Windows component RSAT-ADDS-Tools
isn't installed on this computer
[RsatAddsToolsInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the RSAT-ADDS-Tools Windows
component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature RSAT-ADDS-Tools

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.844 -->

Windows component RSAT-Clustering isn't
installed on this computer
[RsatClusteringInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the RSAT-Clustering Windows
component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature RSAT-Clustering

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.845 -->

Windows component RSAT-Clustering-
Mgmt isn't installed on this computer
[RsatClusteringMgmtInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the RSAT-Clustering-Mgmt
Windows component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature RSAT-Clustering-Mgmt

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.846 -->

Windows component RSAT-Clustering-
PowerShell isn't installed on this computer
[RsatClusteringPowerShellInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the RSAT-Clustering-PowerShell
Windows component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature RSAT-Clustering-PowerShell

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.847 -->

No Exchange 2013 servers detected
[NoE15ServerWarning]
07/23/2025

Microsoft Exchange Server 2016 Setup displayed this warning because no Exchange Server
2013 server roles exist in the organization.

  Ｕ Caution

  If you continue with Exchange Server 2016 installation, you won't be able to add Exchange
  2013 servers to the organization at a future date.

Before deploying Exchange 2016, consider the following factors that may require you to deploy
Exchange 2013 servers prior to deploying Exchange 2016:

     Third-party or in-house developed applications: Applications developed for earlier
     versions of Exchange may not be compatible with Exchange 2016. You may need to
     maintain Exchange 2013 servers to support these applications.

     Coexistence or migration requirements: If you plan on migrating mailboxes into your
     organization, some solutions may require the use of Exchange 2013 servers.

If you decide that you need to deploy Exchange 2013 servers, you must do so before you
deploy Exchange 2016. Active Directory must be prepared for each Exchange version in the
following order:

   1. Exchange 2013
   2. Exchange 2016

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.848 -->

Running "dir" on a ReFS-formatted disk
could cause the computer to freeze
[Win2k12RefsUpdateNotInstalled]
07/23/2025

Microsoft Exchange Server 2016 Setup detects that the computer you're attempting to install
Exchange 2016 on doesn't have a recommended Windows update installed. We strongly
recommend that you install this Windows update before installing Exchange 2016 to avoid any
issues resolved by the update.

Computers running Windows Server 2012 and later support the Resilient File System (ReFS). An
issue exists that could cause computers to freeze when the "dir" command is run on disks
formatted with ReFS.

Download and install the 64-bit update from the following URL, and then select retry on the
Readiness Checks page.

  ７ Note

  If this update requires a reboot to complete installation, you'll need to exit Exchange 2016
  Setup, reboot, and then start Setup again.

Microsoft Knowledge Base article KB2894875, Windows 8-based or Windows Server 2012-
based computer freezes when you run the "dir" command on an ReFS volume          .

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.849 -->

A Windows Server 2012 update rollup isn't
installed
[Win2k12RollupUpdateNotInstalled]
07/23/2025

Microsoft Exchange Server 2016 Setup detects that the computer you're attempting to install
Exchange 2016 on doesn't have a recommended Windows update installed. We strongly
recommend that you install this Windows update before installing Exchange 2016 to avoid any
issues resolved by the update.

A Windows Server 2012 update rollup that resolves several issues, including issues that could
cause Resilient File System (ReFS)-formatted disks to perform unreliably, isn't installed.

Download and install the 64-bit update from the following URL, and then click retry on the
Readiness Checks page.

  ７ Note

  If this update requires a reboot to complete installation, you'll need to exit Exchange 2016
  Setup, reboot, and then start Setup again.

Microsoft Knowledge Base article KB2822241, Windows 8 and Windows Server 2012 update
rollup: April 2013   .

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.850 -->

Disks formatted as ReFS may not perform
reliably [Win2k12UrefsUpdateNotInstalled]
07/23/2025

Microsoft Exchange Server 2016 Setup has detected that the computer you're attempting to
install Exchange 2016 on doesn't have a recommended Windows update installed. We strongly
recommend that you install this Windows update before installing Exchange 2016 to avoid any
issues resolved by the update.

Computers running Windows Server 2012 and later support the Resilient File System (ReFS). An
issue in the Virtual Disk Service could cause disks formatted as ReFS to not perform reliably.
This could result in data corruption or data loss.

Download and install the 64-bit update from the following URL, and then click retry on the
Readiness Checks page.

  ７ Note

  If this update requires a reboot to complete installation, you'll need to exit Exchange 2016
  Setup, reboot, and then start Setup again.

Microsoft Knowledge Base article KB2884597, Virtual Disk Service or applications that use the
Virtual Disk Service crash or freeze in Windows Server 2012    .

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.851 -->

KB3206632 security update not installed
[Win2k16LSARollupUpdateNotInstalled]
07/23/2025

Microsoft Exchange Server 2016 Setup can't continue because the local computer requires a
software update. You need to install this update before Exchange 2016 Setup can continue.

Exchange 2016 Setup requires that the December 13, 2016 (KB3206632) security update is
installed on the computer before installation can continue.

Download and install the 64-bit update from the following URL, and then click retry on the
Readiness Checks page.

  ７ Note

  If this update requires a reboot to complete installation, you'll need to exit Exchange 2016
  Setup, reboot, and then start Setup again.

December 13, 2016 (KB3206632) security update

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.852 -->

Windows Server Core or Windows Nano
Server is installed [IsServerCoreInstalled]
07/23/2025

Microsoft Exchange Server 2016 Setup can't continue because it detected that the local
computer is running Windows Server Core or Windows Nano Server. Exchange 2016 requires
that Windows Server with Desktop Experience (Windows Server 2016) or Windows Server
with a GUI (Windows Server 2012 and 2012R2) is installed on the local computer. Before you
can install Exchange 2016, you need to do one of the following depending on the version of
Windows Server you have installed:

     Windows Server 2012 and Windows Server 2012 R2: Run the following command in
     Windows PowerShell:

       PowerShell

       Install-WindowsFeature Server-Gui-Mgmt-Infra, Server-Gui-Shell -Restart

     Windows Server 2016: Install Windows Server 2016 and choose the Desktop Experience
     installation option. If a computer is running Windows Server 2016 Core or Nano and you
     want to install Exchange 2016 on it, you'll need to reinstall the operating system and
     choose the Desktop Experience installation option.

For more information, see Exchange Server system requirements.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.853 -->

Exchange Server editions and versions
ﾃ   Summarize this article for me

APPLIES TO:         2016            2019   Subscription Edition

Exchange Server is available in two server editions:

     Enterprise Edition: Can scale up to 100 mounted databases per server.

     Standard Edition: Limited to five mounted databases per server.

A mounted database is a database that's in use (an active mailbox database that's mounted for
use by clients or a passive mailbox database that's mounted in recovery for log replication and
replay). While you can create more databases than the described limits, you can only mount
the maximum number of databases that are allowed by the edition of Exchange. Note that the
recovery database doesn't count towards these limits.

The server editions are defined by a product key. When you enter a valid product key, the
supported edition for the server is established. For more information, see Enter your Exchange
Server product key.

Notes:

     You can use a valid product key to move from the Trial Edition (evaluation version) of
     Exchange to either Standard Edition or Enterprise Edition. No loss of functionality occurs
     after the Trial Edition expires, so you can maintain lab, demo, training, and other non-
     production environments beyond 180 days without having to reinstall the Trial Edition of
     Exchange or entering a product key.

     You can use a valid product key to move from Standard Edition to Enterprise Edition.

     You can't use a valid product key to downgrade from Enterprise Edition to Standard
     Edition or revert to the Trial Edition. You can only do these types of downgrades by
     uninstalling Exchange, reinstalling Exchange, and entering the correct product key.

Exchange Server versions
For a list of Exchange Server versions and how to download and upgrade to the latest version
of Exchange, see the following topics:

     Exchange Server build numbers and release dates

     Install Exchange Mailbox servers using the Setup wizard

<!-- p.854 -->

     Upgrade Exchange to the latest Cumulative Update

Exchange Server license types
For more information about Exchange license types, see Exchange Licensing FAQs   .

Last updated on 02/13/2026

<!-- p.855 -->

Exchange Server language support
06/16/2025

APPLIES TO:       2016       2019    Subscription Edition

Exchange Server has enhanced language support for both servers and clients. This topic lists
the languages that are available for both servers and clients in Exchange Server.

Supported server languages for Exchange Server
     Chinese (Simplified)

     Chinese (Traditional)

     English

     French

     German

     Italian

     Japanese

     Korean

     Portuguese

     Russian

     Spanish

Supported client languages for Exchange Server
     Amharic

     Arabic

     Basque (Basque)

     Bengali (India)

     Bulgarian

     Catalan

<!-- p.856 -->

Chinese (Simplified)

Chinese (Traditional)

Croatian

Czech

Danish

Dutch

English

Estonian

Filipino (Philippines)

Finnish

French

Galician

German

Greek

Gujarati

Hebrew

Hindi

Hungarian

Icelandic

Indonesian

Italian

Japanese

Kannada

Kazakh

Kiswahili

<!-- p.857 -->

Korean

Latvian

Lithuanian

Malay (Brunei Darussalam)

Malay (Malaysia)

Malayalam

Marathi

Norwegian (Bokmål)

Norwegian (Nynorsk)

Oriya

Persian

Polish

Portuguese (Brazil)

Portuguese (Portugal)

Romanian

Russian

Serbian (Cyrillic, Serbia)

Serbian (Latin)

Slovak

Slovenian

Spanish

Swedish

Tamil

Telugu

Thai

<!-- p.858 -->

Turkish

Ukrainian

Urdu

Vietnamese

Welsh

<!-- p.859 -->

Exchange Server storage configuration
options
07/07/2025

APPLIES TO:          2016     2019        Subscription Edition

Understanding the storage options and requirements for Mailbox servers in Exchange Server is
an important part of your Mailbox server storage design solution.

Storage architectures
The following table describes supported storage architectures and provides best practice
guidance for each type of storage architecture where appropriate.

Supported storage architectures:

                                                                                           ﾉ      Expand table

 Storage                Description                                              Best practice
 architecture

 Direct-attached        DAS is a digital storage system directly attached to a   Not available.
 storage (DAS)          server or workstation, without a storage network in
                        between. For example, DAS transports include Serial
                        Attached Small Computer System Interface (SCSI)
                        and Serial Attached Advanced Technology
                        Attachment (ATA).

 Storage area           SAN is an architecture to attach remote computer         Don't share physical disks
 network (SAN):         storage devices (such as disk arrays and tape            backing up Exchange data
 Internet Small         libraries) to servers in such a way that the devices     with other applications.
 Computer System        appear as locally attached to the operating system       Use dedicated storage
 Interface (iSCSI)      (for example, block storage). iSCSI SANs encapsulate     networks.
                        SCSI commands within IP packets and use standard
                        networking infrastructure as the storage transport       Use multiple network paths
                        (for example, Ethernet).                                 for stand-alone
                                                                                 configurations.

 SAN: Fibre Channel     Fibre Channel SANs encapsulate SCSI commands             Don't share physical disks
                        within Fibre Channel packets and generally use           backing up Exchange data
                        specialized Fibre Channel networks as the storage        with other applications.
                        transport.                                               Use multiple Fibre Channel
                                                                                 network paths for stand-
                                                                                 alone configurations.

<!-- p.860 -->

 Storage                Description                                           Best practice
 architecture

                                                                              Follow storage vendor's
                                                                              best practices for tuning
                                                                              Fibre Channel host bus
                                                                              adapters (HBAs), for
                                                                              example, Queue Depth and
                                                                              Queue Target.

A network-attached storage (NAS) unit is a self-contained computer connected to a network,
with the sole purpose of supplying file-based data storage services to other devices on the
network. The operating system and other software on the NAS unit provide the functionality of
data storage, file systems, and access to files, and the management of these functions (for
example, file storage).

All storage used by Exchange for storage of Exchange data must be block-level storage
because Exchange Server doesn't support the use of NAS volumes, other than in the SMB 3.0
scenario outlined in the article Exchange Server virtualization. Also, in a virtualized
environment, NAS storage that's presented to the guest as block-level storage via the
hypervisor isn't supported.

Using storage tiers isn't recommended, as it could adversely affect system performance. For
this reason, don't allow the storage controller to automatically move the most accessed files to
"faster" storage.

Physical disk types
The following table provides a list of supported physical disk types and provides best practice
guidance for each physical disk type where appropriate.

Supported physical disk types:

                                                                                        ﾉ     Expand table

 Physical       Description                              Supported or best practice
 disk type

 Serial ATA     SATA is a serial interface for ATA and   Supported: 512-byte sector disks for Windows
 (SATA)         integrated device electronics (IDE)      Server 2008 and Windows Server 2008 R2. In
                disks. SATA disks are available in       addition, 512e disks are supported for Windows
                various form factors, speeds, and        Server 2008 R2 with the following:
                capacities.                                    The hotfix described in KB982018   .
                In general, choose SATA disks for             Windows Server 2008 R2 with Service Pack 1
                Exchange Server mailbox storage               (SP1) and Exchange Server 2010 SP1.

<!-- p.861 -->

Physical    Description                                 Supported or best practice
disk type

            when you have the following design          Exchange 2013 and later supports native 4
            requirements:                               kilobyte (KB) sector disks and 512e disks. Support
                                                        requires that all copies of a database reside on the
                  High capacity                         same physical disk type. For example, it isn't a
                  Moderate performance                  supported configuration to host one copy of a
                  Moderate power utilization            given database on a 512-byte sector disk and
                                                        another copy of that same database on a 512e
                                                        disk or 4K disk.

                                                        Best practice: Consider enterprise class SATA disks,
                                                        which generally have better heat, vibration, and
                                                        reliability characteristics.

Serial      Serial Attached SCSI is a serial            Supported: 512-byte sector disks for Windows
Attached    interface for SCSI disks. Serial Attached   Server 2008 and Windows Server 2008 R2. In
SCSI        SCSI disks are available in various form    addition, 512e disks are supported for Windows
            factors, speeds, and capacities.            Server 2008 R2 with the following:
            In general, choose Serial Attached                 The hotfix described in KB982018    .
            SCSI disks for Exchange Server                     Windows Server 2008 R2 SP1 and Exchange
            mailbox storage when you have the                  Server 2010 SP1.
            following design requirements:
                                                        Exchange 2013 and later supports native 4
                  Moderate capacity                     kilobyte (KB) sector disks and 512e disks. Support
                  High performance                      requires that all copies of a database are on the
                  Moderate power utilization            same physical disk type. For example, it is not a
                                                        supported configuration to host one copy of a
                                                        given database on a 512-byte sector disk and
                                                        another copy of that same database on a 512e
                                                        disk or 4K disk.

                                                        Best practice: Physical disk-write caching must be
                                                        disabled when used without a UPS.

Fibre       Fibre Channel is an electrical interface    Supported: 512-byte sector disks for Windows
Channel     used to connect disks to Fibre              Server 2008 and Windows Server 2008 R2. In
            Channel-based SANs. Fibre Channel           addition, 512e disks are supported for Windows
            disks are available in various speeds       Server 2008 R2 with the following:
            and capacities.                                   The hotfix described in KB982018 .
            In general, choose Fibre Channel disks            Windows Server 2008 R2 with Service Pack 1
            for Exchange Server mailbox storage                (SP1) and Exchange Server 2010 SP1.
            when you have the following design
            requirements:                               Exchange 2013 and later supports native 4
                                                        kilobyte (KB) sector disks and 512e disks. Support
                  Moderate capacity                     requires that all copies of a database are on the
                  High performance                      same physical disk type. For example, it isn't a
                  SAN connectivity                      supported configuration to host one copy of a
                                                        given database on a 512-byte sector disk and

<!-- p.862 -->

 Physical       Description                                Supported or best practice
 disk type

                                                           another copy of that same database on a 512e
                                                           disk or 4K disk.

                                                           Best practice: Physical disk-write caching must be
                                                           disabled when used without a UPS.

 Solid-state    An SSD is a data storage device that       Supported: 512-byte sector disks for Windows
 drive (SSD)    uses solid-state memory to store           Server 2008 and Windows Server 2008 R2. In
 (flash disk)   persistent data. An SSD emulates a         addition, 512e disks are supported for Windows
                hard disk drive interface. SSD disks are   Server 2008 R2 with the following:
                available in various speeds (different           The hotfix described in KB982018 .
                I/O performance capabilities) and                Windows Server 2008 R2 SP1 and Exchange
                capacities.                                      Server 2010 SP1.
                In general, choose SSD disks for
                Exchange Server mailbox storage            Exchange 2013 and later supports native 4
                when you have the following design         kilobyte (KB) sector disks and 512e disks when all
                requirements:                              copies of a database are on the same physical disk
                                                           type. For example, it isn't a supported
                      Low capacity                         configuration to host one copy of a given
                      High performance                     database on a 512-byte sector disk and another
                                                           copy of that same database on a 512e disk or 4K
                                                           disk.

                                                           Best practice: Physical disk-write caching must be
                                                           disabled when used without a UPS.

                                                           In general, Exchange Server Mailbox servers don't
                                                           require the performance characteristics of SSD
                                                           storage.

Factors to consider when choosing disk types
There are several trade-offs when choosing disk types for Exchange Server storage. The correct
disk is one that balances performance (both sequential and random) with capacity, reliability,
power utilization, and capital cost. The following table of supported physical disk types
provides information to help you when considering these factors.

From a performance perspective, using large, slower disks for Exchange storage is okay,
provided the disks can maintain an average read and write latency of 20 ms or less under load.

Factors in disk type choice:

                                                                                            ﾉ   Expand table

<!-- p.863 -->

Disk      Disk form    Interface or      Capacity    Random I/O      Sequential I/O   Power
speed     factor       transport                     performance     performance      utilization
(RPM)

5,400     2.5 inch     SATA              Average     Poor            Poor             Excellent

5,400     3.5 inch     SATA              Excellent   Poor            Poor             Above
                                                                                      average

7,200     2.5 inch     SATA              Average     Average         Average          Excellent

7,200     2.5 inch     Serial Attached   Average     Average         Above average    Excellent
                       SCSI

7,200     3.5 inch     SATA              Excellent   Average         Above average    Above
                                                                                      average

7,200     3.5 inch     Serial Attached   Excellent   Average         Above average    Above
                       SCSI                                                           average

7,200     3.5 inch     Fibre Channel     Excellent   Average         Above average    Average

10,000    2.5 inch     Serial Attached   Below       Excellent       Above average    Above
                       SCSI              average                                      average

10,000    3.5 inch     SATA              Average     Average         Above average    Above
                                                                                      average

10,000    3.5 inch     Serial Attached   Average     Above average   Above average    Below
                       SCSI                                                           average

10,000    3.5 inch     Fibre Channel     Average     Above average   Above average    Below
                                                                                      average

15,000    2.5 inch     Serial Attached   Poor        Excellent       Excellent        Average
                       SCSI

15,000    3.5 inch     Serial Attached   Average     Excellent       Excellent        Below
                       SCSI                                                           average

15,000    3.5 inch     Fibre Channel     Average     Excellent       Excellent        Poor

SSD: -=   Not          SATA, Serial      Poor        Excellent       Excellent        Excellent
          applicable   Attached SCSI,
                       Fibre Channel

Best practices for supported storage
configurations

<!-- p.864 -->

This section provides best practice information about supported disk and array controller
configurations. In addition to the commonly used Redundant Array of Independent Disks
(RAID), there's also just a bunch of disks (or drives), or JBOD, which refers to a collection of
hard disks that haven't been configured to act as a redundant array.

RAID is often used to both improve the performance characteristics of individual disks (by
striping data across several disks) and to provide protection from individual disk failures. With
the advancements in Exchange Server high availability, RAID isn't a required component for
Exchange Server storage design. However, RAID is still an essential component of Exchange
Server storage design for standalone servers and solutions that require storage fault tolerance.

Operating System, System, or Pagefile Volume
The recommended configuration for an operating system, system, or pagefile volume is to use
RAID technology to protect this data type. The recommended RAID configuration is either
RAID-1 or RAID-1/0, however all RAID types are supported.

Separated Mailbox Database and Log Volumes
If you're deploying a standalone Mailbox server role architecture, RAID technology is required
for the mailbox database and log volumes. The recommended RAID configuration for mailbox
volumes is RAID-1/0 (especially if you're using 5.4 K or 7.2 K disks); however all RAID types are
supported. For log volumes, RAID-1 or RAID-1/0 is the recommended RAID configuration.

When using RAID-5 or RAID-6 configurations for the operating system, pagefile, or Exchange
data volumes, note the following:

     RAID-5 configurations, including variations such as RAID-50 and RAID-51, should have no
     more than seven disks per array group and array controller high-priority scrubbing and
     surface scanning enabled.

     RAID-6 configurations should have array controller high-priority scrubbing and surface
     scanning enabled.

Although JBOD is supported in high availability architectures that have three or more highly
available database copies, because the log and mailbox database volumes are separated, JBOD
isn't recommended as a solution.

Mailbox Database and Log Volume Co-Location
Mailbox database and log volume co-location are not recommended in standalone
architectures. In high availability architectures, there are two possibilities for this scenario:

<!-- p.865 -->

   1. Single database per volume

   2. Multiple databases per volume

Single Database Per Volume
In an Exchange environment, a JBOD storage solution involves having both the database and
its associated logs stored on a single disk. To deploy a JBOD solution, you must deploy a
minimum of three highly available database copies. Using a single disk is a single point of
failure, because when the disk fails, the database copy residing on that disk is lost. Having a
minimum of three database copies ensures fault tolerance by having two additional copies if
one copy (or one disk) fails. However, placement of three highly available database copies, and
the use of lagged database copies, can affect storage design. The following table shows
guidelines for RAID or JBOD considerations.

RAID or JBOD Considerations:

                                                                                 ﾉ   Expand table

 Datacenter      Two highly       Three highly     Two or more        One        Two or more
 servers         available        available        highly available   lagged     lagged copies
                 copies (total)   copies (total)   copies per         copy       per datacenter
                                                   datacenter

 Primary         RAID             RAID or JBOD     RAID or JBOD       RAID       RAID or JBOD
 datacenter                       (2 copies)
 servers

 Secondary       RAID             RAID (1 copy)    RAID or JBOD       RAID       RAID or JBOD
 datacenter
 servers

To deploy on JBOD with the primary datacenter servers, you need three or more highly
available database copies within the DAG. If mixing lagged copies on the same server hosting
highly available database copies (for example, not using dedicated lagged database copy
servers), you need at least two lagged database copies.

For the secondary datacenter servers to use JBOD, you should have at least two highly
available database copies in the secondary datacenter. The loss of a copy in the secondary
datacenter won't result in requiring a reseed across the WAN or having a single point of failure
in the event the secondary datacenter is activated. If mixing lagged database copies on the
same server hosting highly available database copies (for example, not using dedicated lagged
database copy servers), you need at least two lagged database copies.

<!-- p.866 -->

For dedicated lagged database copy servers, you should have at least two lagged database
copies within a datacenter to use JBOD. Otherwise, the loss of disk results in the loss of the
lagged database copy, and the loss of the protection mechanism.

Multiple Databases Per Volume
Multiple databases per volume are a new JBOD scenario available in Exchange Server that
allows for active and passive copies (including lagged copies) to be mixed on a single disk,
enabling better disk utilization. However, to deploy lagged copies in this manner, automatic
lagged copy log file play down must be enabled. The following table shows guidelines for
JBOD considerations for multiple databases per volume.

JBOD Considerations:

                                                                                            ﾉ   Expand table

 Datacenter Servers                   3 or more copies (total)       Two or more copies per datacenter

 Primary datacenter servers           JBOD                           JBOD

 Secondary datacenter servers         N/A                            JBOD

The following table provides guidance about storage array configurations for Exchange Server.

Supported RAID types for the Exchange Server Mailbox server role:

                                                                                            ﾉ   Expand table

 RAID type     Description                   Supported or best practice

 Disk array    The stripe size is the per    Best practice: 256 KB or greater. Follow storage vendor best
 RAID          disk unit of data             practices.
 stripe size   distribution within a RAID
 (KB)          set. Stripe size is also
               referred to as block size.

 Storage       The cache settings are        Best practice: 100 percent write cache (battery or flash backed
 array         provided by a battery-        cache) for DAS storage controllers in either a RAID or JBOD
 cache         backed caching array          configuration. 75 percent write cache, 25 percent read cache
 settings      controller.                   (battery or flash backed cache) for other types of storage
                                             solutions such as SAN. If your SAN vendor has different best
                                             practices for cache configuration on their platform, follow the
                                             guidance of your SAN vendor.

 Physical      The settings for the          Supported: Physical disk write caching must be disabled when
 disk write    cache are on each             used without a UPS.

<!-- p.867 -->

 RAID type       Description                   Supported or best practice

 caching         individual disk.

The following table provides guidance about database and log file choices.

Database and log file choices for the Exchange Server Mailbox server role:

                                                                                             ﾉ   Expand table

 Database          Description                       Stand-alone: supported        High availability:
 and log file                                        or best practice              supported or best
 options                                                                           practice

 File              Database per log isolation        Best practice: For            Supported: Isolation of
 placement:        refers to placing the database    recoverability, move          logs and databases isn't
 database per      file and logs from the same       database (.edb) file and      required.
 log isolation     mailbox database on to            logs from the same
                   different volumes backed by       database to different
                   different physical disks.         volumes backed by
                                                     different physical disks.

 File              Database files per volume         Best practice: Based on       Supported: When using
 placement:        refer to how you distribute       your backup methodology.      JBOD, create a single
 database          database files within or across                                 volume with separate
 files per         disk volumes.                                                   directories for database(s)
 volume                                                                            and for log files.

 File              Log streams per volume refer      Best practice: Based on       Supported: When using
 placement:        to how you distribute             your backup methodology.      JBOD, create a single
 log streams       database log files within or                                    volume with separate
 per volume        across disk volumes.                                            directories for database(s)
                                                                                   and for log files.
                                                                                   Best practice: When using
                                                                                   JBOD, use multiple
                                                                                   databases per volume.

 Database          Database size refers to the       Supported: Approximately      Supported: Approximately
 size              disk database (.edb) file size.   16 terabytes.                 16 terabytes.
                                                     Best practice:                Best practice:

                                                           200 gigabytes (GB) or         2 terabytes or less.
                                                           less.                         Provision for 120
                                                           Provision for 120             percent of
                                                           percent of calculated         calculated maximum
                                                           maximum database              database size.
                                                           size.

<!-- p.868 -->

 Database        Description                         Stand-alone: supported           High availability:
 and log file                                        or best practice                 supported or best
 options                                                                              practice

 Log             Log truncation method is the        Best practice:                   Best practice:
 truncation      process for truncating and                Use backups for log              Enable circular
 method          deleting old database log                 truncation (for                  logging for
                 files. There are two                      example, circular                deployments that
                 mechanisms:                               logging disabled).               use Exchange native
                         Circular logging, in              Provision for three              data protection
                        which Exchange deletes             days of log                      features.
                        the logs.                          generation capacity.             Provision for three
                        Log truncation, which                                               days beyond replay
                        occurs after a                                                      lag setting of log
                        successful full or                                                  generation capacity.
                        incremental Volume
                        Shadow Copy Service
                        (VSS) backup.

The following table provides guidance about Windows disk types.

Windows disk types for the Exchange Server Mailbox server role:

                                                                                                 ﾉ   Expand table

 Windows        Description                                              Stand-alone:        High availability:
 disk type                                                               supported or        supported or
                                                                         best practice       best practice

 Basic disk     A disk initialized for basic storage is called a basic   Supported.          Supported.
                disk. A basic disk contains basic volumes, such as       Best practice:      Best practice: Use
                primary partitions, extended partitions, and             Use basic disks.    basic disks.
                logical drives.

 Dynamic        A disk initialized for dynamic storage is called a       Supported.          Supported.
 disk           dynamic disk. A dynamic disk contains dynamic
                volumes, such as simple volumes, spanned
                volumes, striped volumes, mirrored volumes, and
                RAID-5 volumes.

The following table provides guidance on volume configurations.

Volume configurations for the Exchange Server Mailbox server role:

                                                                                                 ﾉ   Expand table

<!-- p.869 -->

Volume            Description                            Stand-alone:               High availability:
configuration                                            supported or best          supported or best
                                                         practice                   practice

GUID partition    GPT is a disk architecture that        Supported.                 Supported.
table (GPT)       expands on the older master            Best practice: Use GPT     Best practice: Use GPT
                  boot record (MBR) partitioning         partitions.                partitions.
                  scheme. The maximum NTFS
                  formatted partition size is 256
                  terabytes.

MBR               An MBR, or partition sector, is        Supported.                 Supported.
                  the 512-byte boot sector that is
                  the first sector (LBA Sector 0) of a
                  partitioned data storage device
                  such as a hard disk. The
                  maximum NTFS formatted
                  partition size is 2 terabytes.

Partition         Partition alignment refers to          Supported: The             Supported: The
alignment         aligning partitions on sector          Windows Server 2008        Windows Server 2008
                  boundaries for optimal                 R2 and Windows             R2 and Windows
                  performance.                           Server 2012 default is 1   Server 2012 default is 1
                                                         megabyte (MB).             MB.

Volume path       Volume path refers to how a            Supported: Drive letter    Supported: Drive letter
                  volume is accessed.                    or mount point. Best       or mount point.
                                                         practice: Mount point      Best practice: Mount
                                                         host volume must be        point host volume
                                                         RAID enabled.              must be RAID-enabled.

File system       File system is a method for            Supported: NTFS and        Supported: NTFS and
                  storing and organizing computer        ReFS.                      ReFS.
                  files and the data they contain to
                  make it easy to find and access
                  the files.

NTFS              NTFS defragmentation is a              Supported.                 Supported.
defragmentation   process that reduces the amount        Best practice: Not         Best practice: Not
                  of fragmentation in Windows file       required and not           required and not
                  systems. It does this by physically    recommended. On            recommended. On
                  organizing the contents of the         Windows Server 2012,       Windows Server 2012,
                  disk to store the pieces of each       we also recommend          we also recommend
                  file close together and                disabling the automatic    disabling the automatic
                  contiguously.                          disk optimization and      disk optimization and
                                                         defragmentation            defragmentation
                                                         feature.                   feature.

NTFS allocation   NTFS allocation unit size              Supported: All             Supported: All
unit size         represents the smallest amount         allocation unit sizes.     allocation unit sizes.

<!-- p.870 -->

Volume              Description                            Stand-alone:               High availability:
configuration                                              supported or best          supported or best
                                                           practice                   practice

                    of disk space that can be              Best practice: 64 KB for   Best practice: 64 KB for
                    allocated to hold a file.              both .edb and log file     both .edb and log file
                                                           volumes.                   volumes.

NTFS                NTFS compression is the process        Supported: Not             Supported: Not
compression         of reducing the actual size of a       supported for              supported for
                    file stored on the hard disk.          Exchange database or       Exchange database or
                                                           log files.                 log files.

NTFS Encrypting     EFS enables users to encrypt           Supported: Not             Not supported for
File System (EFS)   individual files, folders, or entire   supported for              Exchange database or
                    data drives. Because EFS provides      Exchange database or       log files.
                    strong encryption through              log files.
                    industry-standard algorithms and
                    public key cryptography,
                    encrypted files are confidential
                    even if an attacker bypasses
                    system security.

Windows             Windows BitLocker is a data            Supported: All             Supported: All
BitLocker           protection feature in Windows          Exchange database and      Exchange database and
(volume             Server 2008. BitLocker protects        log files.                 log files. Windows
encryption)         against data theft or exposure on                                 failover clusters require
                    computers that are lost or stolen,                                Windows Server 2008
                    and it offers more secure data                                    R2 or Windows Server
                    deletion when computers are                                       2008 R2 SP1. Exchange
                    decommissioned.                                                   volumes with BitLocker
                                                                                      enabled are not
                                                                                      supported on Windows
                                                                                      failover clusters
                                                                                      running earlier versions
                                                                                      of Windows.
                                                                                      For more information
                                                                                      about Windows 7
                                                                                      BitLocker encryption,
                                                                                      see BitLocker Drive
                                                                                      Encryption in Windows
                                                                                      7: Frequently Asked
                                                                                      Questions.

Server Message      The Server Message Block (SMB)         Limited Support.           Limited Support.
Block (SMB) 3.0     protocol is a network file sharing     Supported scenario is a    Supported scenario is a
                    protocol (on top of TCP/IP or          hardware virtualized       hardware virtualized
                    other network protocols) that          deployment where the       deployment where the
                    allows applications on a               disks are hosted on        disks are hosted on
                    computer to access files and           VHDs on an SMB 3.0         VHDs on an SMB 3.0

<!-- p.871 -->

Volume           Description                          Stand-alone:                High availability:
configuration                                         supported or best           supported or best
                                                      practice                    practice

                 resources on a remote server. It     share. These VHDs are       share. These VHDs are
                 also allows applications to          presented to the host       presented to the host
                 communicate with any server          via a hypervisor. For       via a hypervisor. For
                 program that is set up to receive    more information, see       more information, see
                 an SMB client request. Windows       Exchange Server             Exchange Server
                 Server 2012 introduces the new       virtualization.             virtualization.
                 3.0 version of the SMB protocol
                 with the following features:
                       SMB Transparent failover
                       SMB Scaleout
                       SMB Multichannel
                       SMB Direct
                       SMB Encryption
                       VSS for SMB file shares
                       SMB Directory Leasing
                       SMB PowerShell

Storage Spaces   Storage Spaces is a new storage      Supported. Same             Supported. Same
                 solution that delivers               restrictions as for         restrictions as for
                 virtualization capabilities for      physical disk types         physical disk types
                 Windows Server 2012. Storage         outlined in this article.   outlined in this article.
                 Spaces allows you to organize
                 physical disks into storage pools,
                 which can be easily expanded by
                 adding disks. These disks can be
                 connected either through USB,
                 SATA, or SAS. It also uses virtual
                 disks (spaces), which behave just
                 like physical disks, with
                 associated powerful capabilities
                 such as thin provisioning, and
                 resiliency to failures of
                 underlying physical media. For
                 more information on Storage
                 Spaces, see Storage Spaces
                 Overview.

Resilient File   ReFS is a newly engineered file      Supported for volumes       Supported for volumes
System (ReFS)    system for Windows Server 2012       containing Exchange         containing Exchange
                 that is built on the foundations     database files, log files   database files, log files,
                 of NTFS. ReFS maintains high         and content indexing        and content indexing
                 degree of compatibility with         files, if the following     files, if the following
                 NTFS while providing enhanced        hotfix is installed:        hotfix is installed:
                 data verification and                Exchange Server 2013        Exchange Server 2013
                 autocorrection techniques and        databases become            databases become

<!-- p.872 -->

Volume            Description                          Stand-alone:               High availability:
configuration                                          supported or best          supported or best
                                                       practice                   practice

                  an integrated end-to-end             fragmented in              fragmented in
                  resiliency to corruptions            Windows Server             Windows Server
                  especially when used with the        2012     . Not supported   2012     . Not supported
                  storage spaces feature. For more     for volumes containing     for volumes containing
                  information on ReFS, see             Exchange binaries.         Exchange binaries.
                  Resilient File System (ReFS)
                  overview: Supported                  Best practice: Data        Best practice: Data
                  Deployments.                         integrity features must    integrity features must
                                                       be disabled for the        be disabled for the
                                                       Exchange database          Exchange database
                                                       (.edb) files or the        (.edb) files or the
                                                       volume that hosts          volume that hosts
                                                       these files. Integrity     these files. Integrity
                                                       features can be            features can be
                                                       enabled for volumes        enabled for volumes
                                                       containing the content     containing the content
                                                       index catalog, if the      index catalog, if the
                                                       volume doesn't contain     volume doesn't contain
                                                       any databases or log       any databases or log
                                                       files.                     files.

ReFS allocation   ReFS allocation unit size            Supported: All             Supported: All
unit size         represents the smallest amount       allocation unit sizes.     allocation unit sizes.
                  of disk space that can be            Best practice: 64 KB for   Best practice: 64 KB for
                  allocated to hold a file.            both .edb and log file     both .edb and log file
                                                       volumes.                   volumes.

Data De-          Data deduplication is a technique    OS Level: Not              OS Level: Not
Duplication       to optimize storage utilization.     Supported for              Supported for
                  It's a method of finding and         Exchange mailbox           Exchange mailbox
                  removing duplication within data     databases, transport       databases, transport
                  without compromising its fidelity    databases, or content      databases, or content
                  or integrity. The goal is to store   index files.               index files.
                  more data in less space by           Storage System Level:      Storage Level:
                  segmenting files into small          Supported, but falls       Supported, but falls
                  variable-sized chunks, identifying   within the Microsoft       within the Microsoft
                  duplicate chunks, and                third-party storage        third-party storage
                  maintaining a single copy of each    software solutions         software solutions
                  chunk. Data deduplication            support policy    .        support policy    .
                  technologies are typically
                  implemented one of two ways; at      Note: OS level dedupe      Note: OS level dedupe
                  the operating system level, or at    can be used for            can be used for
                  the storage system level and the     Exchange database          Exchange database
                  operating system are unaware of      files that are offline     files that are offline
                  it being used.                       (used as backups or        (used as backups or
                                                       archives).                 archives).

<!-- p.873 -->

<!-- p.874 -->

Network ports for clients and mail flow in
Exchange
Article • 05/09/2025

APPLIES TO:        2016     2019       Subscription Edition

This topic provides information about the network ports that are used by Exchange Server
2016 and Exchange Server 2019 for communication with email clients, internet mail servers,
and other services that are external to your local Exchange organization. Before we get into
that, understand the following ground rules:

      We don't support restricting or altering network traffic between internal Exchange servers,
      between internal Exchange servers and internal Lync or Skype for Business servers, or
      between internal Exchange servers and internal Active Directory domain controllers in any
      and all types of topologies. If you have firewalls or network devices that could potentially
      restrict or alter this kind of internal network traffic, you need to configure rules that allow
      free and unrestricted communication between these servers: rules that allow incoming
      and outgoing network traffic on any port (including random RPC ports) and any protocol
      that never alter bits on the wire.

      Edge Transport servers are almost always located in a perimeter network, so it's expected
      that you'll restrict network traffic between the Edge Transport server and the internet, and
      between the Edge Transport server and your internal Exchange organization. These
      network ports are described in this topic.

      It's expected that you'll restrict network traffic between external clients and services and
      your internal Exchange organization. It's also OK if you decide to restrict network traffic
      between internal clients and internal Exchange servers. These network ports are described
      in this topic.

Network ports required for clients and services
The network ports that are required for email clients to access mailboxes and other services in
the Exchange organization are described in the following diagram and table.

Notes:

      The destination for these clients and services is the Client Access services on a Mailbox
      server. In Exchange 2016 and Exchange 2019, Client Access (frontend) and backend
      services are installed together on the same Mailbox server. For more information, see
      Client Access protocol architecture.

<!-- p.875 -->

    Although the diagram shows clients and services from the internet, the concepts are the
    same for internal clients (for example, clients in an accounts forest accessing Exchange
    servers in a resource forest). Similarly, the table doesn't have a source column because
    the source could be any location that's external to the Exchange organization (for
    example, the internet or an accounts forest).

    Edge Transport servers have no involvement in the network traffic that's associated with
    these clients and services.

                                                                                  ﾉ   Expand table

Purpose                    Ports             Comments

Encrypted web              443/TCP (HTTPS)   For more information about these clients and services,
connections are used by                      see the following topics:
                                                   Autodiscover service in Exchange Server

<!-- p.876 -->

Purpose                       Ports             Comments

the following clients and                             Exchange ActiveSync
services:                                             EWS reference for Exchange
      Autodiscover service                            Offline address books in Exchange Server
      Exchange ActiveSync                             Outlook Anywhere
      Exchange Web                                    MAPI over HTTP in Exchange Server
      Services (EWS)
      Offline address book
      (OAB) distribution
      Outlook Anywhere
      (RPC over HTTP)
      Outlook MAPI over
      HTTP
      Outlook on the web
      (formerly known as
      Outlook Web App)

Unencrypted web               80/TCP (HTTP)     Whenever possible, we recommend using encrypted
connections are used by                         web connections on 443/TCP to help protect data and
the following clients and                       credentials. However, you may find that some services
services:                                       must be configured to use unencrypted web
      Internet calendar                         connections on 80/TCP to the Client Access services on
      publishing                                Mailbox servers.
      Outlook on the web                        For more information about these clients and services,
      (redirect to 443/TCP)                     see the following topics:
      Autodiscover
      (fallback when                                  Enable Internet Calendar Publishing
      443/TCP isn't                                   Autodiscover service in Exchange Server
      available)

IMAP4 clients                 143/TCP (IMAP),   IMAP4 is disabled by default. For more information, see
                              993/TCP (secure   POP3 and IMAP4 in Exchange Server.
                              IMAP)
                                                The IMAP4 service in the Client Access services on the
                                                Mailbox server proxies connections to the IMAP4
                                                Backend service on a Mailbox server.

POP3 clients                  110/TCP (POP3),   POP3 is disabled by default. For more information, see
                              995/TCP (secure   POP3 and IMAP4 in Exchange Server.
                              POP3)
                                                The POP3 service in the Client Access services on the
                                                Mailbox server proxies connections to the POP3
                                                Backend service on a Mailbox server.

SMTP clients                  587/TCP           The default Received connector named "Client
(authenticated)               (authenticated    Frontend <Server name>" in the Front End Transport
                              SMTP)             service listens for authenticated SMTP client
                                                submissions on port 587.

<!-- p.877 -->

 Purpose                   Ports             Comments

                                             Note: If you have email clients that are only able to
                                             submit authenticated SMTP email on port 25, you can
                                             modify the network adapter bindings of the client
                                             Receive connector to also listen for authenticated
                                             SMTP email submissions on port 25.

Network ports required for mail flow
How mail is delivered to and from your Exchange organization depends on your Exchange
topology. The most important factor is whether you have a subscribed Edge Transport server
deployed in your perimeter network.

Network ports required for mail flow (no Edge Transport
servers)
The network ports that are required for mail flow in an Exchange organization that has only
Mailbox servers are described in the following diagram and table.

<!-- p.878 -->

                                                                                   ﾉ   Expand table

Purpose        Ports           Source     Destination   Comments

Inbound mail   25/TCP (SMTP)   Internet   Mailbox       The default Receive connector named
                               (any)      server        "Default Frontend <Mailbox server name>"
                                                        in the Front End Transport service listens for
                                                        anonymous inbound SMTP mail on port 25.

                                                        Mail is relayed from the Front End
                                                        Transport service to the Transport service
                                                        on a Mailbox server using the implicit and
                                                        invisible intra-organization Send connector
                                                        that automatically routes mail between
                                                        Exchange servers in the same organization.
                                                        For more information, see Implicit Send
                                                        connectors.

<!-- p.879 -->

 Purpose            Ports             Source    Destination   Comments

 Outbound           25/TCP (SMTP)     Mailbox   Internet      By default, Exchange doesn't create any
 mail                                 server    (any)         Send connectors that allow you to send
                                                              mail to the internet. You have to create
                                                              Send connectors manually. For more
                                                              information, see Create a Send connector
                                                              to send mail to the internet.

 Outbound           25/TCP (SMTP)     Mailbox   Internet      Outbound mail is proxied through the
 mail (if                             server    (any)         Front End Transport service only when a
 proxied                                                      Send connector is configured with Proxy
 through the                                                  through Client Access server in the
 Front End                                                    Exchange admin center or -
 transport                                                    FrontEndProxyEnabled $true in the
 service)                                                     Exchange Management Shell.

                                                              In this case, the default Receive connector
                                                              named "Outbound Proxy Frontend
                                                              <Mailbox server name>" in the Front End
                                                              Transport service listens for outbound mail
                                                              from the Transport service on a Mailbox
                                                              server. For more information, see Configure
                                                              Send connectors to proxy outbound mail.

 DNS for name       53/UDP,53/TCP     Mailbox   DNS server    See the Name resolution section in this
 resolution of      (DNS)             server                  topic.
 the next mail
 hop (not
 pictured)

Network ports required for mail flow with Edge Transport
servers
A subscribed Edge Transport server that's installed in your perimeter network affects mail flow
in the following ways:

        Outbound mail from the Exchange organization never flows through the Front End
        Transport service on Mailbox servers. Mail always flows from the Transport service on a
        Mailbox server in the subscribed Active Directory site to the Edge Transport server
        (regardless of the version of Exchange on the Edge Transport server).

        Inbound mail flows from the Edge Transport server to a Mailbox server in the subscribed
        Active Directory site. Specifically:

           Mail from an Exchange 2013 or later Edge Transport server first arrives at the Front End
           Transport service before it flows to the Transport service on an Exchange 2016 or

<!-- p.880 -->

         Exchange 2019 Mailbox server.

         In Exchange 2016, mail from an Exchange 2010 Edge Transport server always delivers
         mail directly to the Transport service on an Exchange 2016 Mailbox server. Note that
         coexistence with Exchange 2010 isn't supported in Exchange 2019.

For more information, see Mail flow and the transport pipeline.

The network ports that are required for mail flow in Exchange organizations that have Edge
Transport servers are described in the following diagram and table.

                                                                                   ﾉ   Expand table

 Purpose              Ports           Source           Destination      Comments

 Inbound mail -       25/TCP (SMTP)   Internet (any)   Edge             The default Receive
 Internet to Edge                                      Transport        connector named "Default
 Transport server                                      server           internal Receive connector
                                                                        <Edge Transport server
                                                                        name>" on the Edge
                                                                        Transport server listens for
                                                                        anonymous SMTP mail on
                                                                        port 25.

 Inbound mail -       25/TCP (SMTP)   Edge Transport   Mailbox          The default Send connector
 Edge Transport                       server           servers in the   named "EdgeSync -
 server to internal                                    subscribed       Inbound to <Active
                                                                        Directory site name>" relays
