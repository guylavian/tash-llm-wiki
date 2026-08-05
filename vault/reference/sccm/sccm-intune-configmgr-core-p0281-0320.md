---
title: "Core infrastructure documentation — pages 281-320"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0281-0320
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0281-0320
family: sccm
documentKind: "doc"
abstract: "macOS Mojave (10.14) On-premises MDM ） Important Starting in November 2021, this feature of Configuration Manager is deprecated. Configuration Manager has built-in capabilities for managing mobile devices that are on- premises without installing client software. For more informa"
---

# Core infrastructure documentation — pages 281-320

<!-- p.281 -->

     macOS Mojave (10.14)

On-premises MDM

  ） Important

  Starting in November 2021, this feature of Configuration Manager is deprecated.

Configuration Manager has built-in capabilities for managing mobile devices that are on-
premises without installing client software. For more information, see Manage mobile devices
with on-premises infrastructure.

Supported operating systems
     Windows 10 Pro (x86, x64)

     Windows 10 Enterprise (x86, x64)

     Windows 10 IoT Enterprise (x86, x64) This version includes the long-term servicing channel
     (LTSC). For more information, see Overview of Windows 10 IoT Enterprise.

     Windows 10 Team for Surface Hub

Exchange Server connector
Configuration Manager supports limited management of devices that connect to your Exchange
Server, without installing the Configuration Manager client. For more information, see Manage
mobile devices with Configuration Manager and Exchange.

Supported versions of Exchange Server
     Exchange Online (Microsoft 365): This version includes Business Productivity Online
     Standard Suite

     Exchange Server 2016

     Exchange Server 2013

     Exchange Server 2010 SP1 or Exchange Server 2010 SP2

<!-- p.282 -->

Last updated on 05/27/2026

<!-- p.283 -->

Support for Windows 11 in Configuration
Manager
07/31/2025

Applies to: Configuration Manager (current branch)

Learn about the Windows 11 versions that Configuration Manager supports as a client.

For more information about support for the Windows Assessment and Deployment Kit (ADK)
for Windows 11, see Support for the Windows ADK.

  ７ Note

  You can continue to use Microsoft Endpoint Manager to manage devices running
  Windows 11 the same as with Windows 10. If another article doesn't explicitly reference
  Windows 11, assume that feature support for Windows 10 also includes Windows 11. This
  article lists some known issues.

Windows 11 versions
Configuration Manager attempts to provide support as a client for each new Windows 11
version soon after it becomes available. Because the products have separate development and
release schedules, the support that Configuration Manager provides depends on when each
becomes available.

A Configuration Manager version drops from the matrix after support for that version ends.
Similarly, Configuration Manager doesn't support Windows 11 versions when their support
lifecycle ends.

     The latest version of Configuration Manager current branch receives both security and
     critical updates, which can include fixes for Windows 11-specific features. When Microsoft
     releases a new version of Configuration Manager current branch, prior versions only
     receive security updates. For more information, see Support for Configuration Manager
     current branch versions.

        ７ Note

<!-- p.284 -->

         The best way to stay current with Windows 11 is to stay current with Configuration
         Manager. For more information, see Configuration Manager and Windows as a
         Service.

       This information supplements Supported operating systems for clients and devices.

The following table lists the versions of Windows 11 that you can use as a client with different
versions of Configuration Manager.

                                                                                ﾉ   Expand table

 Windows 11 version           ConfigMgr 2309         ConfigMgr 2403        ConfigMgr 2409

 24H2
 (10.0.26100)

 23H2
 (10.0.22631)

 22H2
 (10.0.22621)

For more information on Windows lifecycle, see the Windows lifecycle fact sheet and Windows
release information.

                                                                                ﾉ   Expand table

 Key

    = Supported

    = Not supported

Support notes
       Support for Windows 11 versions includes the following editions: Enterprise, Pro,
       Education, Pro Education, and Pro for Workstation.

       Windows 11 reports the Operating System property as Microsoft Windows NT Workstation
       10.0 , which is identical to Windows 10. To distinguish devices running Windows 11, use

       the Operating System Build device property for build number 10.0.22000 or later.

       OS deployment images and upgrade packages for Windows 11 show the image name as
       Windows 10. For more information, see Using deployment tools with Windows 11 images.

<!-- p.285 -->

     The last supported version of 32-bit WinPE is available in the WinPE add-on for Windows
     10, version 2004 (10.1.19041). Versions of the WinPE add-on for the ADK after the ADK
     for Windows 10, version 2004 (10.1.19041) no longer support 32-bit versions of Windows
     PE (WinPE). For more information, see Download and install the Windows ADK.

     Configuration Manager supports the use of older versions of Windows PE as boot images,
     but you can't customize them in the Configuration Manager console. For more
     information, see Customize boot images with Configuration Manager.

Windows 11 on ARM64
Configuration Manager version 2107 with the update rollup supports the client on Windows 11
ARM64 devices.

The All Windows 11 (ARM64) platform is available in the list of supported OS versions on
objects with requirement rules or applicability lists.

Starting in version 2403 OS deployment is supported for All Windows 11 (ARM64), you can
deploy a task sequence with a feature update to a Windows 11 on ARM64 device. For more
information, see Upgrade Windows to the latest version.

Support for Windows Insider
You can update and service Windows Insider builds. This ability is provided as a convenience to
our customers. While this functionality should work, its support is best effort. Configuration
Manager might not issue a hotfix for this functionality if it doesn't work.

To provide feedback on Windows Insider, use the Windows Feedback Hub.

Offline servicing
Due to changes in how Windows 11 updates are delivered through UUP patches, Offline
Servicing of Windows 11 images and update packages using Configuration Manager is no
longer supported. The recommended method to keep Windows 11 deployments up-to-date is
to acquire the latest patched Windows 11 ISO from Microsoft 365 admin center . Once the
updated Windows 11 ISO is obtained:

     Import the install.wim image from the ISO into the site for Operating System Images
     packages used in bare metal/refresh task sequences.
     Import the whole contents of the ISO into the site for Operating System Upgrade
     Packages used in-place upgrade task sequences.

<!-- p.286 -->

Known issues

Windows servicing dashboard
The Windows Servicing dashboard currently includes Windows 11 devices with the latest
version of Windows 10. It doesn't yet distinguish a version for Windows 11. For more
information on this dashboard, see Manage Windows as a service using Configuration
Manager.

Software Center notifications don't display during quiet
period
By default, Windows 11 enables focus assist for the first hour after a user signs on for the first
time. For more information, see Reaching the Desktop and the Quiet Period.

Software Center notifications are currently suppressed during this time. For more information,
see Turn Focus assist on or off in Windows     .

Pre-provisioning BitLocker during task sequence doesn't own
TPM
Applies to: Windows ADK for Windows 11 (version 10.1.22000)

When you use a Windows 11-based boot image with an OS deployment task sequence that
includes the Pre-provision BitLocker step, the step might fail. You'll see errors similar to the
following strings in the smsts.log:

     log

     'TakeOwnership' failed (2147942402)
     pTpm->TakeOwnership(sOwnerAuth), HRESULT=80070002
     Failed to take ownership of TPM. Ensure that Active Directory permissions are
     properly configured
     The system cannot find the file specified. (Error: 80070002; Source: Windows)
     Process completed with exit code 2147942402
     Failed to run the action: Pre-provision BitLocker. Error -2147024894

To work around this issue, add a Run Command Line step to the task sequence before the Pre-
provision BitLocker step. Run the following command:

reg.exe add HKLM\SOFTWARE\Policies\Microsoft\TPM /v OSManagedAuthLevel /t REG_DWORD /d 2
/f

<!-- p.287 -->

For more information on this registry key, see Change the TPM owner password. This work
around is only needed for ADK releases 10.1.22000. Later versions aren't affected.

Configuration Manager console with Windows Hello for
Business authentication
Applies to: Microsoft Entra joined devices

If you configure the authentication level for the site to require Windows Hello for Business
authentication, the Configuration Manager console on a Windows 11 device can't connect to
the site. The adminui.log file on the devices shows the following errors:

  log

  Description = "Current thread is not authenticated with the minimal allowed
  level.";
  ErrorCode = 2185761792;

Use one of the following options to work around this issue:

        Update the device to Windows 11 OS build 22000.282. For more information, see
        October 21, 2021—KB5006746 (OS Build 22000.282) Preview       .

        Install the console on a device running another version of Windows.

        Add users to the authentication exclusion list. For more information, see Configure SMS
        Provider authentication.

Next steps
Support for the Windows ADK

<!-- p.288 -->

Support for Windows 10 in Configuration
Manager
Applies to: Configuration Manager (current branch)

Learn about the Windows 10 versions that Configuration Manager supports as a client. For more
information about support for later versions of Windows, see Support for Windows 11.

For more information about support for the Windows Assessment and Deployment Kit (ADK) for
Windows 10, see Support for the Windows ADK.

   Tip

  Windows Server builds as a client are supported the same as the associated Windows 10
  version. For example, Windows Server 2016 is the same build version as Windows 10 LTSB
  2016, and Windows Server version 1803 is the same build version as Windows 10, version
  1803.

  For more information on Windows Server as a site system, see Supported operating
  systems for Configuration Manager site system servers.

Windows 10 versions
Configuration Manager attempts to provide support as a client for each new Windows 10 version
as soon as possible after it becomes available. Because the products have separate development
and release schedules, the support that Configuration Manager provides depends on when each
becomes available.

A Configuration Manager version drops from the matrix after support for that version ends.
Similarly, support for Windows 10 versions like the Enterprise 2015 LTSB or 1511 drops from the
matrix when they're removed from support.

     The latest version of Configuration Manager current branch receives both security and
     critical updates, which can include fixes for issues with Windows 10 versions. When
     Microsoft releases a new version of Configuration Manager current branch, prior versions
     only receive security updates. For more information, see Support for Configuration Manager
     current branch versions.

<!-- p.289 -->

           ７ Note

           The best way to stay current with Windows 10 is to stay current with Configuration
           Manager. For more information, see Configuration Manager and Windows as a
           Service.

       This information supplements Supported operating systems for clients and devices.

       If you use the long-term servicing branch of Configuration Manager, see Supported
       configurations for the long-term servicing branch.

The following table lists the versions of Windows 10 that you can use as a client with different
versions of Configuration Manager.

                                                                                   ﾉ    Expand table

 Windows 10 version               ConfigMgr       ConfigMgr        ConfigMgr        ConfigMgr
                                  2409            2503             2509             2603

 22H2                             ✅               ✅                ✅                ✅
 (10.0.19045) Extended Security
 Updates

All currently supported versions of Configuration Manager current branch support the following
Windows 10 LTSB/LTSC editions:

       Enterprise 2016 LTSB
       Enterprise LTSC 2019
       Enterprise LTSC 2021

For more information on Windows lifecycle, see the Windows lifecycle fact sheet and Windows 10
release information.

                                                                                   ﾉ    Expand table

 Key

 ✅ = Supported

 ❌ = Not supported

Support notes

<!-- p.290 -->

     Support for Windows 10 semi-annual channel versions includes the following editions:
     Enterprise, Pro, Education, Pro Education, and Pro for Workstation.

     OS deployment media shows the build number from the base version. For example,
      10.0.19041 . When Windows is installed, it applies an enablement package, which updates

     the build number to what's in the preceding table. You can use the revision ID to distinguish
     the media:

                                                                                    ﾉ   Expand table

       Media version                             Windows version

       10.0.19045.2130                           Windows 10, version 22H2

       10.0.19041.1288                           Windows 10, version 21H2

Windows 10 on ARM64
Configuration Manager supports the client on Windows 10 ARM64 devices.

The All Windows 10 (ARM64) platform is available in the list of supported OS versions on objects
with requirement rules or applicability lists.

  ７ Note

  If you previously selected the top-level Windows 10 platform, this action automatically
  selected both All Windows 10 (64-bit) and All Windows 10 (32-bit). If you want to add All
  Windows 10 (ARM64), manually select it in the list.

Starting in version 2403 OS deployment is supported for Windows 10 22H2 (ARM64), you can
deploy a task sequence with a feature update to a Windows 10 on ARM64 device. For more
information, see Deploy a feature update with a task sequence.

Support for Windows Insider
You can update and service Windows Insider builds. This ability is provided as a convenience to
our customers. While this functionality should work, the support for it is best effort. Configuration
Manager might not issue a hotfix for this functionality if it ceases to function.

To provide feedback on Windows Insider, use the Feedback Hub.

<!-- p.291 -->

Sysprep and Windows 10, version 20H2
If you manually customize a reference computer that runs Windows 10, version 20H2, and then
use capture media, Windows Sysprep fails with the following entry in the sysprep.log: Failed to
clean the package repository database: 0x80070005. This issue happens when you sign in to the

device and create a user profile.

To work around this issue, choose one of the following options:

      Use the default image file (install.wim) from the installation media. Use the task sequence to
      apply configurations at run time.

      Create a task sequence to capture an OS

      Remove appx packages for the signed-in user before you use capture media. For more
      information, see Sysprep fails after you remove or update Microsoft Store apps that include
      built-in Windows images.

      Manually run Sysprep, and then boot to the capture media to capture the image.

Next steps
Support for the Windows ADK

Support for Windows 11

 Last updated on 05/14/2026

<!-- p.292 -->

Support for the Windows ADK in
Configuration Manager
Applies to: Configuration Manager (current branch)

When you deploy operating systems with Configuration Manager, the Windows Assessment
and Deployment Kit (ADK) is a required external dependency. For more information, see the
following articles:

     Infrastructure requirements for OS deployment

     Download the Windows ADK

        ） Important
           Windows PE is a separate installer. Make sure to download both the Windows
           ADK and the Windows PE add-on for the ADK.
           ADK 10.1.26100.X (May 2024, Dec 2024) (10.1.26100.X) or newer is required to
           deploy Windows ARM64 operating systems on Configuration Manager 2403 or
           newer.

Windows ADK versions
The following table lists the versions of the Windows ADK that you can use with different
versions of Configuration Manager.

                                                                               ﾉ   Expand table

 Windows ADK version                         ConfigMgr 2409   ConfigMgr 2503   ConfigMgr 2509

 ADK 10.1.28000.1 (Updated Nov 2025)         ❌                ❌                ❌
 (10.1.28000.1)

 ADK 10.1.26100.2454 (Updated Dec 2024)      ✅                ✅                ✅
 (10.1.26100.X)

 ADK 10.1.26100.1 (May 2024)                 ✅                ✅                ✅
 (10.1.26100.1)

 ADK 10.1.25398.1 (updated September 2023)   ❌                ❌                ❌
 (10.1.25398.1)

 ADK for Windows 11, version 22H2            ✅                ✅                ✅
 (10.1.22621.1)

<!-- p.293 -->

Windows ADK version                            ConfigMgr 2409      ConfigMgr 2503     ConfigMgr 2509

ADK for Windows 11, version 21H1               ✅                   ✅                  ✅
(10.1.22000)

ADK for Windows Server 2022                    ✅                   ✅                  ✅
(10.1.20348)

ADK for Windows 10, version 2004               ❌                   ❌                  ❌
(10.1.19041) EOS

                                                                                      ﾉ      Expand table

Key

✅ = Supported
This table only shows Windows ADK supportability in relation to the version of Configuration Manager.
Microsoft recommends using the Windows ADK that matches the version of Windows you're deploying.
Use the latest Windows ADK version when deploying the latest Windows version. The latest Windows
ADK version might support deployment of older OS versions, such as Windows 10. For more information
on Windows ADK component supportability, see DISM supported platforms, USMT requirements, and
Choose the right ADK for your scenario.

   = Backward compatible
This combination isn't tested but should work. We'll document any known issues or caveats.

❌ = Not supported

Support notes
      ADK 10.1.25398.1 (updated September 2023) Windows PE boot images aren't supported
      for use with Configuration Manager due to known issues:

        VBScript doesn't work in WinPE.

        The Pre-provision BitLocker task doesn't work in WinPE.

        Devices with UFS storage, such as the Surface Go 4, don't work in WinPE.

        Instead use the ADK 10.1.26100.X (May 2024, Dec 2024) (10.1.26100.X) or newer where
        these issues are resolved.

      For information on applying the BlackLotus UEFI bootkit vulnerability          security updates
      to boot images from the ADKs before the ADK 10.1.26100.1 (May 2024, Dec 2024)
      (10.1.26100.1), see Customize Windows PE boot images. Boot images from the ADK
      10.1.26100.1 (May 2024, Dec 2024) (10.1.26100.1) and newer already have the BlackLotus

<!-- p.294 -->

       UEFI bootkit vulnerability security update applied to them. For this reason, it's
       recommended to use boot images from the ADK 10.1.26100.1 (May 2024, Dec 2024)
       (10.1.26100.X) or newer.

       Windows Server builds have the same Windows ADK requirement as the associated
       Windows client version. For example, Windows Server 2016 is the same build version as
       Windows 10 LTSB 2016.

       The last supported version of 32-bit WinPE is available in the WinPE add-on for Windows
       10, version 2004 (10.1.19041). Versions of the WinPE add-on for the ADK after the ADK
       for Windows 10, version 2004 (10.1.19041) no longer support 32-bit versions of Windows
       PE (WinPE). For more information, see Download and install the Windows ADK.

       Configuration Manager supports the use of older versions of Windows PE as boot images,
       but you can't customize them in the Configuration Manager console. For more
       information, see Customize boot images with Configuration Manager.

Known issues

Pre-provisioning BitLocker during task sequence doesn't own
TPM
Applies to: Windows ADK for Windows 11 (version 10.1.22000)

When you use a Windows 11-based boot image with an OS deployment task sequence that
includes the Pre-provision BitLocker step, the step might fail. You'll see errors similar to the
following strings in the smsts.log:

 log
 'TakeOwnership' failed (2147942402)
 pTpm->TakeOwnership(sOwnerAuth), HRESULT=80070002
 Failed to take ownership of TPM. Ensure that Active Directory permissions are
 properly configured
 The system cannot find the file specified. (Error: 80070002; Source: Windows)
 Process completed with exit code 2147942402
 Failed to run the action: Pre-provision BitLocker. Error -2147024894

To work around this issue, add a Run Command Line step to the task sequence before the Pre-
provision BitLocker step. Run the following command:

reg.exe add HKLM\SOFTWARE\Policies\Microsoft\TPM /v OSManagedAuthLevel /t REG_DWORD /d 2

/f

<!-- p.295 -->

For more information on this registry key, see Change the TPM owner password. This work
around is only needed for ADK releases 10.1.22000. Later versions aren't affected.

Next steps
Support for Windows 11

Support for Windows 10

Supported OS versions for clients

 Last updated on 12/09/2025

<!-- p.296 -->

Supported OS versions for
Configuration Manager consoles
Article • 12/19/2024

Applies to: Configuration Manager (current branch)

Configuration Manager supports the installation of the console on the following
Windows OS versions:

      Windows Server 2025: Standard, Datacenter (starting in version 2409)

      Windows Server 2022: Standard, Datacenter (starting in version 2107)

      Windows Server 2019: Standard, Datacenter

      Windows Server 2016: Standard, Datacenter

      Windows 11 (x64): Pro, Enterprise

      Windows 10 (x86, x64): Pro, Enterprise

For more information about the Configuration Manager console, see the following
articles:

      Install consoles

      Using the console

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.297 -->

Supported SQL Server versions for
Configuration Manager
Applies to: Configuration Manager (current branch)

Each Configuration Manager site requires a supported SQL Server version and configuration to
host the site database.

SQL Server instances and locations
Central administration site and primary sites
The site database must use a full installation of SQL Server.

SQL Server can be located on:

     The site server computer.
     A computer that is remote from the site server.

The following instances are supported:

     The default or named instance of SQL Server.

     Multiple instance configurations.

     A SQL Server Always On failover cluster instance. For more information, see Use a SQL
     Server Always On failover cluster instance for the site database.

     A SQL Server Always On availability group. For more information, see Prepare to use a SQL
     Server Always On availability group.

Secondary sites
The site database can use the default instance of a full installation of SQL Server or SQL Server
Express.

SQL Server must be located on the site server computer.

  ） Important

<!-- p.298 -->

  Upgrade SQL 2012 or 2014 Express, Standard, Enterprise edition to SQl 2016 or latest
  version. Visual C++ Redistributable need to be upgraded to latest version on Secondary site:
  Download Latest Microsoft Visual C++ Redistributable Version .

Limitations to support
The following configurations aren't supported:

     A failover cluster instance in a Network Load Balancing (NLB) cluster configuration

     A failover cluster instance on a Cluster Shared Volume (CSV)

     SQL Server database mirroring technology, and peer-to-peer replication

SQL Server transactional replication is supported only for replicating objects to management
points that are configured to use database replicas.

Supported versions of SQL Server
In a hierarchy with multiple sites, different sites can use different versions of SQL Server to host
the site database. So long as the following items are true:

     Configuration Manager supports the versions of SQL Server that you use.
     The SQL Server versions you use remain in support by Microsoft.
     SQL Server supports replication between the two versions of SQL Server. For more
     information, see SQL Server replication backward compatibility.

For SQL Server 2016 and prior, support for each SQL Server version and service pack follows the
Microsoft Lifecycle Policy. Support for a specific SQL Server service pack includes cumulative
updates unless they break backward compatibility to the base service pack version. Starting with
SQL Server 2017, service packs won't be released since it follows a modern servicing model. The
SQL Server team recommends ongoing, proactive installation of cumulative updates as they
become available.

Unless specified otherwise, the following versions of SQL Server are supported with all active
versions of Configuration Manager. If support for a new SQL Server version is added, the
Configuration Manager version that adds that support is noted. Similarly, if support is
deprecated, look for details about affected versions of Configuration Manager.

  ） Important

<!-- p.299 -->

 When you use SQL Server Standard for the database at the central administration site, you
 limit the total number of clients that a hierarchy can support. See Size and scale numbers.

Standard / Enterprise SQL Editions

                                                                                          ﾉ   Expand table

SQL            Minimum Required         Supported        Notes
Version        Update                   Site Types

SQL            RTM                      CAS, Primary,    Support added in version 2303. Support for SQL
Server                                  Secondary        2022 Compatibility Level (160) added in version
2022                                                     2603 . CU must be supported by SQL lifecycle.

SQL            Cumulative Update 5      CAS, Primary,    CU5 is the minimum requirement as it resolves an
Server         (CU5) or later           Secondary        issue with scalar UDF inlining. CU must be
2019                                                     supported by SQL lifecycle.

SQL            Cumulative Update 2      CAS, Primary,    CU must be supported by SQL lifecycle.
Server         (CU2) or later           Secondary
2017

SQL            Minimum Service Pack     CAS, Primary,
Server         supported by SQL 2016    Secondary
2016           lifecycle

SQL            Deprecated               CAS, Primary,    Deprecated in version 2409. SQL 2014 support
Server                                  Secondary        ended July 2024.
2014

Express Editions (Secondary Sites Only)

                                                                                          ﾉ   Expand table

SQL Version       Minimum Required          Supported       Notes
                  Update                    Site Types

SQL Server        RTM                       Secondary       Shipped with version 2509. Support for SQL
2022 Express                                                2022 Compatibility Level (160) added in
                                                            version 2603.

SQL Server        Cumulative Update 5       Secondary       CU5 is the minimum requirement as it resolves
2019 Express      (CU5) or later                            an issue with scalar UDF inlining. CU must be
                                                            supported by SQL lifecycle.

SQL Server        Cumulative Update 2       Secondary       CU must be supported by SQL lifecycle.

<!-- p.300 -->

 SQL Version    Minimum Required         Supported        Notes
                Update                   Site Types

 2017 Express   (CU2) or later

 SQL Server     Minimum Service Pack     Secondary
 2016 Express   supported by SQL 2016
                lifecycle

 SQL Server     Deprecated               Secondary        Deprecated in version 2409. SQL 2014 support
 2014 Express                                             ended July 2024.

Required configurations for SQL Server
The following configurations are required by all installations of SQL Server that you use for a site
database, including SQL Server Express. When Configuration Manager installs SQL Server Express
as part of a secondary site installation, it automatically creates these configurations.

SQL Server architecture version
Configuration Manager requires a 64-bit version of SQL Server to host the site database.

SQL Instance and Database collations
At each site, both the instance of SQL Server that's used for the site and the site database must
use the following collation: SQL_Latin1_General_CP1_CI_AS.

Configuration Manager supports two exceptions to this collation for the China GB18030
standard. For more information, see International support.

SQL Server features
Only the Database Engine Services feature is required for each site server.

Configuration Manager database replication doesn't require the SQL Server replication feature.
However, this SQL Server configuration is required when you use database replicas for
management points.

Windows authentication
Configuration Manager requires Windows authentication to validate connections to the
database.

<!-- p.301 -->

SQL Server instance
Use a dedicated instance of SQL Server for each site. The instance can be a named instance or
the default instance.

SQL Server memory
Reserve memory for SQL Server by using SQL Server Management Studio. Set the Minimum
server memory setting under Server Memory Options. For more information about how to
configure this setting, see SQL Server memory server configuration options.

     For a database server that you install on the same computer as the site server: Limit the
     memory for SQL Server to 50 to 80 percent of the available addressable system memory.

     For a dedicated database server that's remote from the site server: Limit the memory for
     SQL Server to 80 to 90 percent of the available addressable system memory.

     For a memory reserve for the buffer pool of each SQL Server instance in use:
         For a central administration site: Set a minimum of 8 GB.
         For a primary site: Set a minimum of 8 GB.
         For a secondary site: Set a minimum of 4 GB.

Other required SQL Server configurations
Configuration Manager sets the below SQL Server configurations during setup to function
correctly. They apply for both standalone primary site and hierarchy scenarios. Do not alter them
unless instructed by Microsoft support.

                                                                                     ﾉ    Expand table

 Display name             Canonical name    Required       More information link
                                            value

 CLR integration          clr enabled       True           Introduction to SQL Server CLR Integration.

 Allow Triggers to Fire   nested triggers   True           Configure the nested triggers server
 Others                                                    configuration option.

 Max Text Replication     max text repl     2147483647     Configure the max text repl size server
 Size                     size (B)                         configuration option.

Required SQL database configurations

<!-- p.302 -->

Database compatibility level
Configuration Manager requires that the compatibility level for the site database is no less than
the lowest supported SQL Server version for your Configuration Manager version.

When you upgrade a site database from an earlier version of SQL Server, the database keeps its
existing cardinality estimation level, if it's at the minimum allowed for that instance of SQL Server.
When you upgrade SQL Server with a database at a compatibility level lower than the allowed
level, it automatically sets the database to the lowest compatibility level allowed by SQL Server.

The following table identifies the recommended compatibility levels for Configuration Manager
site databases:

                                                                                    ﾉ   Expand table

 SQL Server version      Supported compatibility levels                       Recommended level

 SQL Server 2022         160 (since version 2603), 150, 140, 130, 120, 110    150

 SQL Server 2019         150, 140, 130, 120, 110                              150

 SQL Server 2017         140, 130, 120, 110                                   140

 SQL Server 2016         130, 120, 110                                        130

To identify the compatibility level in use for your site database, run the following SQL query on
the site database server:

 SQL

 SELECT name, compatibility_level FROM sys.databases

For more information on SQL Server compatibility levels and how to set them, see ALTER
DATABASE Compatibility Level (Transact-SQL).

Other required database configurations
Configuration Manager sets the below database configurations during setup to function
correctly. They apply for both standalone primary site and hierarchy scenarios - as well as for SQL
Always On configurations.

Do not alter them unless instructed by Microsoft support. The Support policies for manual
database changes article applies for database options.

<!-- p.303 -->

                                                                                      ﾉ    Expand table

 Display name               Canonical name             Required      More information link
                                                       value

 Database owner             owner_sid                  sa            ALTER AUTHORIZATION for
                                                                     databases

 Change tracking            CHANGE_TRACKING            True (ON)     Enable change tracking

 Recursive Triggers         RECURSIVE_TRIGGERS         True (ON)     Recursive Triggers
 Enabled

 Broker Enabled             ENABLE_BROKER              True (ON)     Activate Service Broker in a
                                                                     database

 Honor Broker Priority      HONOR_BROKER_PRIORITY      True (ON)     Enable conversation priorities

 Trustworthy                TRUSTWORTHY                True (ON)     TRUSTWORTHY database property

 Allow Snapshot Isolation   ALLOW_SNAPSHOT_ISOLATION   True (ON)     Snapshot Isolation in SQL Server

 Is Read Committed          READ_COMMITTED_SNAPSHOT    True (ON)     Set Transaction Isolation Level
 Snapshot On

 ANSI Nulls Enabled         ANSI_NULLS                 True (ON)     SET ANSI_NULLS

 ANSI Padding Enabled       ANSI_PADDING               True (ON)     SET ANSI_PADDING

 ANSI Warnings Enabled      ANSI_WARNINGS              True (ON)     SET ANSI_WARNINGS

 Arithmetic Abort Enabled   ARITHABORT                 True (ON)     SET ARITHABORT

 Concatenate Null Yields    CONCAT_NULL_YIELDS_NULL    True (ON)     SET CONCAT_NULL_YIELDS_NULL
 Null

 Quoted Identifiers         QUOTED_IDENTIFIER          True (ON)     SET QUOTED_IDENTIFIER
 Enabled

 Numeric Round-abort        NUMERIC_ROUNDABORT         False (OFF)   SET NUMERIC_ROUNDABORT

Optional configurations for SQL Server
The following configurations are optional for each database that uses a full SQL Server
installation.

SQL Server service
You can configure the SQL Server service to run using:

<!-- p.304 -->

     A low rights domain user account:
          This configuration is a best practice and might require you to manually register the
          service principal name (SPN) for the account.

     The local system account of the computer that runs SQL Server:
          Use the local system account to simplify the configuration process.
          When you use the local system account, Configuration Manager automatically registers
          the SPN for the SQL Server service.
          Using the local system account for the SQL Server service isn't a SQL Server best practice.

When the computer running SQL Server doesn't use its local system account to run the SQL
Server service, configure the SPN of the account that runs the SQL Server service in Active
Directory Domain Services. (When the system account is used, the SPN is automatically registered
for you.)

For information about SPNs for the site database, see Manage the SPN for the site database
server.

For information about how to change the account that is used by the SQL Server service, see
SCM Services - Change the service startup account.

SQL Extended Protection for Authentication
Starting from version 2409, Configuration Manager supports SQL extended protection for
authentication. It's a security feature that enhances protection against MITM attacks, making SQL
server more secure when connections are made using extended protection. These enhancements
collectively reduce the risk of unauthorized access and protect sensitive data managed by the
SQL Server database engine.

For more information, see Connect to the Database Engine Using Extended Protection.

SQL Server Reporting Services
SQL Server Reporting Services is required for installing a reporting services point that lets you run
reports. Configuration Manager supports the same versions of SQL Server for reporting as it does
for the site database.

For more information, see Prerequisites for reporting in Configuration Manager.

  ） Important

<!-- p.305 -->

  After you upgrade SQL Server from a previous version, you might see the following error:
  Report Builder Does Not Exist. To resolve this error, you must reinstall the reporting services
  point site system role.

Data warehouse service point
The data warehouse uses a separate database. You can host it on the site database server, or a
separate SQL Server. For more information, see The data warehouse service point for
Configuration Manager.

SQL Server ports
For communication to the SQL Server database engine and for intersite replication, you can use
the default SQL Server port configurations or specify custom ports:

     Intersite communications use the SQL Server Service Broker, which uses port TCP 4022 by
     default.

     Intrasite communications between the SQL Server database engine and various
     Configuration Manager site system roles use port TCP 1433 by default. The following site
     system roles communicate directly with the SQL Server database:
        Management point
        SMS Provider computer
        Reporting services point
        Site server

When a computer running SQL Server hosts a database from more than one site, each database
must use a separate instance of SQL Server. Also, each instance must be configured to use a
unique set of ports.

  ２ Warning

  Configuration Manager doesn't support dynamic ports. Because SQL Server named instances
  by default use dynamic ports for connections to the database engine, when you use a
  named instance, you must manually configure the static port that you want to use for
  intrasite communication.

If you have a firewall enabled on the computer that is running SQL Server, make sure that it's
configured to allow the ports that are being used by your deployment and at any locations on

<!-- p.306 -->

the network between computers that communicate with the SQL Server.

For an example of how to configure SQL Server to use a specific port, see Configure a server to
listen on a specific TCP port.

Upgrade options for SQL Server
If you need to upgrade your version of SQL Server, use one of the following methods, from easy
to more complex:

      Upgrade SQL Server in-place (recommended)

      Install a new version of SQL Server on a new computer, and then use the database move
      option of Configuration Manager setup to point your site server to the new SQL Server

      Use backup and recovery. Using backup and recovery for a SQL Server upgrade scenario is
      supported. You can ignore the SQL Server versioning requirement when reviewing
      Considerations before recovering a site.

 Last updated on 05/21/2026

<!-- p.307 -->

Support for Active Directory domains in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

All Configuration Manager site systems must be members of a supported Active
Directory domain. Configuration Manager client computers can be domain members or
workgroup members.

Requirements and limitations
      Domain membership also applies to site systems that support internet-based client
      management in a perimeter network. (These networks are also known as a DMZ,
      demilitarized zone, and screened subnet).

      It's not supported to change the following configurations for a computer that
      hosts a site system role:

         Domain membership, including if you remove a site system from the domain,
         and then rejoin the same domain.

         Domain name

         Computer name

      Before making these changes, uninstall the site system role. To make these
      changes to a site server, uninstall the site first. You can also consider creating a site
      server in passive mode to help manage this change on a site server.

      Configuration Manager supports domain and forest functional level of Windows
      Server 2008 R2 or later.

Disjoint namespace
You can install Configuration Manager site systems and clients in a domain that has a
disjoint namespace.

In a disjoint namespace, the primary DNS suffix of a computer doesn't match the Active
Directory DNS domain name of that computer. Another disjoint namespace scenario

<!-- p.308 -->

occurs if the NetBIOS domain name of a domain controller doesn't match the Active
Directory DNS domain name.

Disjoint scenarios
The following sections identify the supported scenarios for a disjoint namespace.

Scenario 1
The primary DNS suffix of the domain controller differs from the Active Directory DNS
domain name. Computers that are members of the domain can be either disjoint or not
disjoint.

The domain controller is disjoint in this scenario. Computers that are members of the
domain, such as site servers and computers, can have a primary DNS suffix that either
matches:

      The primary DNS suffix of the domain controller
      The Active Directory DNS domain name

Scenario 2
A member computer in an Active Directory domain is disjoint, even though the domain
controller isn't disjoint.

In this scenario, the primary DNS suffix of a site system differs from the Active Directory
DNS domain name. The primary DNS suffix of the domain controller is the same as the
Active Directory DNS domain name. Member computers that are Configuration
Manager clients can have a primary DNS suffix that either matches:

      The primary DNS suffix of the disjoint site system server
      The Active Directory DNS domain name

Configure disjoint namespace
To allow a computer to access domain controllers that are disjoint, change the msDS-
AllowedDNSSuffixes Active Directory attribute on the domain object container. Add
both DNS suffixes to the attribute.

To make sure that the DNS suffix search list contains all the DNS namespaces in the
organization, configure the search list for each computer in the disjoint domain. Include
the following suffixes in the list of namespaces:

<!-- p.309 -->

        The primary DNS suffix of the domain controller
        The DNS domain name
        Any additional namespaces for other servers that Configuration Manager might
        communicate with

You can use group policy to configure the Domain Name System (DNS) suffix search
list.

   ） Important

   When you reference a computer in Configuration Manager, enter the computer by
   using its primary DNS suffix. This suffix should match the fully qualified domain
   name that's registered as the dnsHostName attribute in the Active Directory
   domain and the service principal name that's associated with the system.

Single label domains
Configuration Manager supports site systems and clients in a single label domain when
the following criteria are met:

        Configure the single label domain in Active Directory Domain Services with a
        disjoint DNS namespace that has a valid top-level domain.

        For example: The single label domain of Contoso is configured to have a disjoint
        namespace in DNS of contoso.com. When you specify the DNS suffix in
        Configuration Manager for a computer in the Contoso domain, you specify
        "Contoso.com" and not "Contoso".

        The distributed component object model (DCOM) connections between site
        servers in the system context must be successful by using Kerberos authentication.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.310 -->

Support for Windows features and
networks in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article identifies Configuration Manager support for common Windows and
networking features.

BranchCache
Use Windows BranchCache with Configuration Manager when you enable it on
distribution points, and configure clients to use it in distributed cache mode.

Configure the BranchCache settings on a deployment type for applications, on the
deployment for a package, and for task sequences. BranchCache is enabled by default.

When the requirements for BranchCache are met, this feature enables clients in remote
locations to obtain content from local clients that have a current cache of the content.

For example, when the first BranchCache-enabled client requests content from a
distribution point that's configured as a BranchCache server, the client downloads and
caches the content. This content is then made available for clients on the same subnet
that requested this content.

These clients also cache the content. Other clients on the same subnet don't have to
download content from the distribution point. The content is distributed across multiple
clients for future transfers.

Requirements to support BranchCache with
Configuration Manager

Configure distribution points
Add the Windows BranchCache feature to the site system server that's configured as a
distribution point.

      Distribution points on servers that are configured to support BranchCache require
      no additional configuration.

<!-- p.311 -->

     You can't add Windows BranchCache to a content-enabled cloud management
     gateway. CMGs do support the download of content by clients that are configured
     for Windows BranchCache.

Configure clients
     The clients that can support BranchCache must be configured for BranchCache
     distributed cache mode.
     The OS setting for BITS client settings must be enabled to support BranchCache.

For information, see configure clients for BranchCache in the Windows documentation.

All Configuration Manager supported versions of Windows support BranchCache by
default.

For more information, see BranchCache for Windows in the Windows Server
documentation.

Computers in workgroups
Configuration Manager provides support for clients in workgroups.

     Configuration Manager supports moving a client from a workgroup to a domain or
     from a domain to a workgroup. For more information, see How to install
     Configuration Manager clients on workgroup computers.

  ７ Note

  Although clients in workgroups are supported, all site systems must be members of
  a supported Active Directory domain.

Data deduplication
Configuration Manager supports the use of data deduplication with distribution points
on Windows Server 2012 or later.

  ） Important

  The volume that hosts package source files can't be marked for data deduplication.
  This limitation is because data deduplication uses reparse points. Configuration

<!-- p.312 -->

  Manager doesn't support using a content source location with files stored on
  reparse points.

For more information, see the following posts:

     Configuration Manager distribution points and Windows Server 2012 data
     deduplication     on the Configuration Manager team blog

     Data deduplication overview in the Windows Server documentation

DirectAccess
Configuration Manager supports the DirectAccess feature for communication between
clients and site server systems.

     When all the requirements for DirectAccess are met, it enables Configuration
     Manager clients on the internet to communicate with their assigned site as if they
     were on the intranet.

     For server-initiated actions, such as remote control and client push installation, the
     initiating computer must be running IPv6. This protocol must be supported on all
     intervening networking devices.

Configuration Manager doesn't support the following functionality over DirectAccess:

     OS deployment

     Communication between Configuration Manager sites

     Communication between Configuration Manager site system servers within a site

Dual-boot computers
Configuration Manager can't manage more than one OS on a single computer. If there's
more than one OS on a computer to manage, adjust the site's discovery and client
installation methods to ensure that the Configuration Manager client is installed only on
the OS that has to be managed.

IPv6
In addition to Internet Protocol version 4 (IPv4), Configuration Manager supports
Internet Protocol version 6 (IPv6), with the following exceptions:

<!-- p.313 -->

                                                                               ﾉ   Expand table

 Function                    Exception to IPv6 support

 Cloud management            IPv4 is required to support Microsoft Azure and the cloud
 gateway                     management gateway.

 Network Discovery           IPv4 is required when you configure a DHCP server to search in
                             Network Discovery.

 OS deployment               Capturing or setting static IP addresses during the task sequence
                             requires IPv4.

 Wake-up proxy               IPv4 is required to support the client wake-up proxy packets.
 communication

Network Address Translation
Network Address Translation (NAT) isn't supported in Configuration Manager, unless the
site supports clients that are on the internet and the client detects that it's connected to
the internet. For more information about internet-based client management, see Plan
for managing internet-based clients.

Specialized storage technology
Configuration Manager works with any hardware that's certified on the Windows
Hardware Compatibility List for the version of the OS that the Configuration Manager
component is installed on.

Site server roles require NTFS, so that Configuration Manager can set directory and file
permissions. Configuration Manager assumes that it has complete ownership of a
logical drive. Site systems that run on separate computers can't share a logical partition
on any storage technology. However, each computer can use a separate logical partition
on the same physical partition of a shared storage device.

Support considerations
     Storage Area Network: A Storage Area Network (SAN) is supported when a
     supported Windows-based server is attached directly to the volume that's hosted
     by the SAN.

     Single Instance Storage: Configuration Manager doesn't support configuration of
     distribution point package and signature folders on a Single Instance Storage (SIS)-

<!-- p.314 -->

     enabled volume.

     Additionally, the cache of a Configuration Manager client isn't supported on a SIS-
     enabled volume.

     Removable disk drive: Configuration Manager doesn't support the installation of
     Configuration Manager site systems or clients on a removable disk drive.

Next steps
Support for virtualization environments with Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.315 -->

Support for virtualization environments
with Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager supports installing the client and site system roles on supported
operating systems that run as a virtual machine (VM) in certain virtualization
environments. This support exists even when the virtual host (virtualization environment)
isn't supported as a client or site server.

For example, you use Microsoft Hyper-V Server 2016 to host a VM that runs Windows
Server 2019. You can install the client or site system roles on the VM running Windows
Server 2019. You can't install the client on the host running Microsoft Hyper-V Server
2016.

Virtualization environments
        Windows Server 2022 (starting in version 2107)
        Windows Server 2019
        Windows Server 2016 Note 1
        Microsoft Hyper-V Server 2016 Note 1
        Windows Server 2012 R2
        Microsoft Hyper-V Server 2012
        Windows Server 2012

  ７ Note

  Configuration Manager doesn't support nested virtualization, which is new with
  Windows Server 2016.

Virtualization environment support
Each virtual computer needs the same or greater hardware and software requirements
that you would use for a physical Configuration Manager computer.

To validate that Configuration Manager supports your virtualization environment, use
the Server Virtualization Validation Program. It includes an online Virtualization Program

<!-- p.316 -->

Support Policy Wizard. For more information, see Windows Server Virtualization
Validation Program    .

Configuration Manager can't manage VMs if they're offline. The Configuration Manager
client on the host computer can't manage an offline VM image. For example, it can't
install software updates or collect hardware inventory.

In general, Configuration Manager gives no special consideration to VMs. For example,
if you stop a VM, and don't save its state, Configuration Manager might not determine if
it has to reinstall a software update.

To help with Configuration Manager client performance in virtual environments that
support multiple user sessions, it disables user policy by default. Starting in version
1910, you can enable user policy in this scenario. For more information, see About client
settings - Enable user policy for multiple user sessions.

Microsoft Azure VMs
Configuration Manager can run on infrastructure as a service (IaaS) VMs in Azure just as
it runs on-premises within your data center. Use Configuration Manager with Azure VMs
in the following scenarios:

     Scenario 1: Run Configuration Manager on an Azure VM. Use it to manage clients
     on other Azure VMs.

     Scenario 2: Run Configuration Manager on an Azure VM. Use it to manage clients
     that aren't running on Azure.

     Scenario 3: Run different Configuration Manager site system roles on Azure VMs.
     Run other roles in your on-premises data center, properly connected to Azure.

  ７ Note

  These scenarios also apply to IaaS VMs on Azure Stack Hub.

The same Configuration Manager requirements for networks, supported configurations,
and hardware requirements also apply to Azure VMs.

For more information, see Configuration Manager on Azure FAQ.

  ） Important

<!-- p.317 -->

  Configuration Manager sites and clients that run on Azure VMs are subject to the
  same license requirements as on-premises installations.

Azure Virtual Desktop
Azure Virtual Desktop is a desktop and app virtualization service that runs on Microsoft
Azure. Use Configuration Manager to manage these virtual devices running Windows in
Azure. For more information, see Supported operating systems for clients and devices.

Next steps
Manage Configuration Manager clients in a virtual desktop infrastructure (VDI)

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.318 -->

Size and scale numbers for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Each Configuration Manager deployment has a maximum number of sites, site system
roles, and devices that it can support. These numbers vary depending on your hierarchy
structure, what types and numbers of sites you use, and the site system roles that you
deploy. The information in this article can help you determine the number of site system
roles and sites that you need to support the devices you expect to manage.

For more information, see the following articles:

      Recommended hardware
      Supported operating systems for site system servers
      Supported operating systems for clients and devices
      Site and site system prerequisites

These support numbers are based on using the recommended hardware for
Configuration Manager. They're also based on the default settings for all available
Configuration Manager features. When you don't use the recommended hardware or
use more aggressive custom settings, the performance of site systems can degrade. The
site systems might not meet the stated levels of support. (An example of more
aggressive client settings is running hardware or software inventory more frequently
than the defaults of once every seven days.)

Site types

Central administration site
      A central administration site supports up to 25 child primary sites.

Primary site
      Each primary site supports up to 250 secondary sites.

      The number of secondary sites per primary site is based on continuously
      connected and reliable wide area network (WAN) connections. For locations that

<!-- p.319 -->

         have fewer than 500 clients, consider a distribution point instead of a secondary
         site.

         For information about the number of clients and devices that a primary site can
         support, see Client numbers for sites and hierarchies.

Secondary site
         Secondary sites don't support child sites.

Site system roles

Cloud management gateway
Unless otherwise noted, this guidance is the same for all deployment models and VM
sizes.

         You can install multiple instances of the cloud management gateway (CMG) at
         primary sites, or the central administration site (CAS).

             Tip

            In a hierarchy, create the CMG at the CAS.

         One CMG supports up to 16 virtual machine (VM) instances in the Azure cloud
         service.

         Simultaneous client connections per each CMG VM instance depend upon the
         deployment model and VM size. When the CMG is under high load with more than
         the supported number of clients, it still handles requests but there may be delay.

            Virtual machine scale-set (version 2107 and later)
                 Lab (B2s): 10
                 Standard (A2_v2): 6,000
                 Large (A4_v2): 10,000

                 ） Important

                 The Lab (B2s) size VM is only intended for lab testing and small proof-of-
                 concept environments. They aren't intended for production use with the
                 CMG. The B2s VMs are low cost and low performing. The Configuration

<!-- p.320 -->

           Manager technical preview branch only supports 10 clients, which is why
           this size supports that number of clients.

        Virtual machine scale set (version 2010 and 2103 for Cloud Service Provider
        (CSP) subscriptions): 2,000

        Cloud service (classic) (version 2111 and earlier): 6,000

           ） Important

           Starting in version 2203, the option to deploy a CMG as a cloud service
           (classic) is removed. All CMG deployments should use a virtual machine
           scale set. For more information, see Removed and deprecated features.

For more information, see CMG Performance and scale.

Cloud management gateway connection point
This guidance is the same for all deployment models and VM sizes.

     You can install multiple instances of the CMG connection point at primary sites.

     One CMG connection point can support a CMG with up to four VM instances. If the
     CMG has more than four VM instances, add a second CMG connection point for
     load balancing. A CMG with 16 VM instances should be linked with four CMG
     connection points.

  ７ Note

  When considering hardware requirements for the CMG connection point, see
  Recommended hardware for remote site system servers.

For more information, see CMG Performance and scale.

Distribution point
     Distribution points per site:

        Each primary and secondary site supports up to 250 distribution points.

        Each primary and secondary site supports up to 2000 additional distribution
        points that are configured as pull-distribution points. For example, a single
