---
title: "Core infrastructure documentation — pages 201-240"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0201-0240
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0201-0240
family: sccm
documentKind: "doc"
abstract: " Configuration Manager does not support SQL Server 2012 and 2014 Starting with version 2409, Configuration Manager no longer supports SQL Server 2012 and 2014. Upgrade to the latest SQL Server version or at least SQL Server 2016. If you don't upgrade, CM upgrades are blocked, a"
---

# Core infrastructure documentation — pages 201-240

<!-- p.201 -->

                                                                                           

Configuration Manager does not support SQL Server 2012 and
2014
Starting with version 2409, Configuration Manager no longer supports SQL Server 2012 and
2014. Upgrade to the latest SQL Server version or at least SQL Server 2016. If you don't
upgrade, CM upgrades are blocked, and you see an error during the prereq check. For more
information, see Supported SQL Server versions for Configuration Manager.

Operating System support added for Windows 11 24H2 and
Windows Server 2025
With this version of Configuration Manager, support is added for Windows 11 24H2 and
Windows Server 2025.

     Windows 11 24H2 & Windows Server 2025 are added to the Product lifecycle dashboard
     and supported platform.
     Windows 11 24H2 & Windows Server 2025 client support is added.
     Boot image creation in CM on Windows Server 2025 now supports latest Windows ADK.
     Windows upgrade readiness dashboard now supports Windows 11 24H2 for upgrading
     clients.

  ７ Note

<!-- p.202 -->

  Windows Server and Windows 11 24H2 do not support Firewall Rules. This will result in a
  non-compliant status in the Configuration Manager applet.

Software metering support in Arm64 devices
The Configuration Manager now supports Software metering for Arm64 devices. Software
metering is used to monitor Windows PC desktop apps with a filename ending in .exe. For
more information, see Software metering in Configuration Manager.

OS deployment

BitLocker support in Arm64 devices
Configuration Manager now supports BitLocker task sequence steps for Arm64 devices. In
BitLocker Management, policies that include OS drive encryption with a TPM protector and
fixed drive encryption with the Auto-Unlock option are supported on Arm64 devices.

For more information, see Bitlocker Supported configurations.

Cloud-attached management

CMG Entra Application secret key renewal
The 'Renew Secret Key' feature now opens a dialog with four options for the validity period.
This update also prevents applications older than 800 days (approximately two years) from
renewing their secret keys. The same options are available when creating a new app.

<!-- p.203 -->

Sign in using the tenant Microsoft Entra Global Administrator credentials and then click on the
Renew button.

  ） Important

  The Microsoft Entra Global Administrator role is a highly privileged role and should only
  be used when another role can't be used. This feature requires the Global Administrator
  role. For other features, Microsoft recommends using roles with the fewest permissions. To
  learn more, see Fundamentals of role-based administration for Configuration Manager.

CMG Enhanced security option
CMG Setup now uses managed Identities and third-party Server App to interact with CMG's
Azure Storage account, instead of storage account keys.

     Hence storage account key access is disabled for new CMG setup.

     For sessions upgrading from earlier versions to 2409, the 'CMG enhanced security' button
     is shown as enabled.

<!-- p.204 -->

                                                                                             

Known Issues
     Upgrade SQL 2012 or 2014 Express, Standard, Enterprise edition to SQl 2016 or latest
     version. VC++ Redistributable Version need to be upgraded to latest version on
     Secondary sites. Download Latest Microsoft Visual C++ Redistributable Version       .

Other Updates

Performance Enhancement of policy processing and collection
evaluation
The performance of policy processing and collection evaluation has been enhanced. Previously,
blocking chains from sp_ProcessPolicyChanges, called by PolicyPv, would run for hours,
disrupting multiple workloads including collection management and policy processing.

Deprecated features
Learn about support changes before they're implemented in removed and deprecated items.

     MDT Integration with CM and Standalone is no longer supported with Configuration
     Manager deprecation first announced in December 2024 and planned end of support the
     first release after Oct 10, 2025. Customers should remove MDT Task sequence steps,
     followed by removing MDT integration, to avoid TS corruption and modification failures.

For more information, see Removed and deprecated features for Configuration Manager..

<!-- p.205 -->

Next steps
As of December 16, 2024, version 2409 is globally available for all customers to install.

  ７ Note

  For exisiting Fast ring current branch 2409 customers, you will see Slow ring upgrade
  package in console. Install 2409 Slow ring package to be in production current branch.

When you're ready to install this version, see Installing updates for Configuration Manager and
Checklist for installing update 2409.

   Tip

  To install a new site, use a baseline version of Configuration Manager.

  Learn more about:

         Installing new sites
         Baseline and update versions

For known significant issues, see the Release notes.

After you update a site, also review the Post-update checklist.

 Last updated on 02/24/2026

<!-- p.206 -->

What's new in version 2403 of
Configuration Manager current branch
Article • 05/02/2024

Applies to: Configuration Manager (current branch)

Update 2403 for Configuration Manager current branch is available as an in-console
update. Apply this update on sites that run version 2211 or later. When installing a new
site, it will also be available as a baseline version soon after global availability. This
article summarizes the changes and new features in Configuration Manager, version
2403.

Always review the latest checklist for installing this update. For more information, see
Checklist for installing update 2403. After you update a site, also review the Post-update
checklist.

To take full advantage of new Configuration Manager features, after you update the site,
also update clients to the latest version. While new functionality appears in the
Configuration Manager console when you update the site and console, the complete
scenario isn't functional until the client version is also the latest.

Site infrastructure

Microsoft Azure Active Directory rebranded to Microsoft
Entra ID
Starting Configuration Manager version 2403, Microsoft Azure Active Directory is
renamed to Microsoft Entra ID within Configuration Manager.

For more information, see New name for Azure Active Directory.

Automated diagnostic Dashboard for Software Update
Issues
A new dashboard is added to the console under monitoring workspace, which shows
the diagnosis of the software update issues in your environment this feature can easily
identify any issues related to software updates. You can fix software update issues based
on troubleshooting documentations.

<!-- p.207 -->

For more information, see Software update health dashboard.

Introducing centralized search box: Effortlessly find what
you need in the console!
Users can now use the global search box in CM console, which streamlines the search
experience and centralizes access to information. This feature enhances the overall
usability, productivity and effectiveness of CM. Users no longer need to navigate
through multiple nodes or sections/ folders to find information they require, saving
valuable time and effort.

<!-- p.208 -->

For more information, see Improvements to console search.

Added Folder support for Scripts node in Software
Library
You can now organize scripts by using folders. This change allows for better
categorization and management of scripts. Full Administrator and Operations
Administrator roles can manage the folders.

For more information, see Folder support for scripts.

HTTPS or Enhanced HTTP should be enabled for client
communication from this version of Configuration

<!-- p.209 -->

Manager
HTTP-only communication is deprecated, and support is removed from this version of
Configuration Manager. Enable HTTPS or Enhanced HTTP for client communication.

For more information, see Enable site system roles for HTTPS or Enhanced HTTP. and
Deprecated features

Windows Server 2012/2012 R2 operating system site
system roles are not supported from this version of
Configuration Manager
Starting 2403, Windows Server 2012/2012 R2 operating system site system roles aren't
supported in any CB releases. Clients with extended support (ESU) will continue to
support.

For more information, see Supported-operating-systems-for-site-system-servers.

Resource access profiles and deployments will block
Configuration manager upgrade
Any configured Resource access profiles and deployments block Configuration manager
upgrade. Consider deleting them and moving the co-management workload for
Resource Access (if co-managed) to Intune.

For more information, see FAQ and Resource access policies are no longer supported.

Software updates

New parameter SoftwareUpdateO365Language is added
to Save-CMSoftwareUpdate cmdlet
A new parameter SoftwareUpdateO365Language is now added to PowerShell Save-
CMSoftwareUpdate cmdlet. Customers now don't have to check a specific language in
the SUP Properties (causing a metadata download for that language for all updates).

PowerShell Commandlet: Save-CMSoftwareUpdate – SoftwareUpdateO365Language
<language name> (<region name>)"

  ７ Note

<!-- p.210 -->

  Languages need to be in O365 format to be consistent with Admin Console UI. E.g.
  "Hungarian (Hungary)".

OS deployment

Support for ARM 64 Operating System Deployment
Configuration Manager operating system deployment support is now added on
Windows 11 ARM 64 devices. Currently Importing and customizing Arm 64 boot images,
Wipe and load TS, Media creation TS, WDS PXE for Arm 64 and CMPivot is supported.

Enhancement in Deploying Software Packages with
Dynamic Variables
When deploying a Task Sequence for installing a software package using dynamic
variables, if the 'Continue on error' option is unchecked and the package is updated on
distribution points while the client is installing the Task Sequence, the installation
process fails due to version inconsistencies with the updated packages on the
distribution points. Previously, the only recourse was to reinstall the entire Task
Sequence from the software center.

<!-- p.211 -->

To address this issue, we've introduced a new feature allowing administrators to specify
the number of retries the system should attempt before marking the Task Sequence as
failed. This retry mechanism is activated only when the 'Continue on error' checkbox is
unchecked."

For more information, see Options for Install Application.

Cloud-attached management

Upgrade to CM 2403 is blocked if CMG V1 is running as a
cloud service (classic)
The option to upgrade Configuration Manager 2403 is blocked if you're running cloud
management gateway V1 (CMG) as a cloud service (classic). All CMG deployments
should use a virtual machine scale set.

For more information, see Check for a cloud management gateway (CMG) as a cloud
service (classic).

Deprecated features
Learn about support changes before they're implemented in removed and deprecated
items.

      System Center Update Publisher (SCUP) and integration with ConfigMgr planned
      end of support Jan 2024.

For more information, see Removed and deprecated features for Configuration
Manager..

<!-- p.212 -->

Other updates

Improvements to Bitlocker
This release includes the following improvements to Bitlocker:

     Starting in this release, this feature ensures proper verification of key escrow and
     prevents message drops. We now validate whether the key is successfully
     escrowed to the database, and only on successful escrow we add the key
     protector.
     This feature now prevents a potential data loss scenario where BitLocker is
     protecting the volumes with keys that are never backed up to the database, in any
     failures to escrow happens.

For more information on BitLocker management, see Deploy BitLocker management.
and Plan for BitLocker management..

     From this version of Configuration Manager, the Windows 11 readiness dashboard
     shows charts for Windows 23H2.
     Defender Exploit Guards policy for controlled folder now accepts regex in the file
     path for apps.
     For example, [C:\Folder\Subfolder\app?.exe] [C:\Folder1\Sub*Name]

Next steps
As of May 06, 2024, version 2403 is globally available for all customers to install.

  ７ Note

  For exisiting Fast ring current branch 2403 customers, you will see Slow ring
  upgrade package in console. Install 2403 Slow ring package to be in production
  current branch.

When you're ready to install this version, see Installing updates for Configuration
Manager and Checklist for installing update 2403.

   Tip

  To install a new site, use a baseline version of Configuration Manager.

  Learn more about:

<!-- p.213 -->

        Installing new sites
        Baseline and update versions

For known significant issues, see the Release notes.

After you update a site, also review the Post-update checklist.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.214 -->

What's new in version 2309 of
Configuration Manager current branch
Article • 11/15/2023

Applies to: Configuration Manager (current branch)

Update 2309 for Configuration Manager current branch is available as an in-console
update. Apply this update on sites that run version 2207 or later. This article summarizes
the changes and new features in Configuration Manager, version 2309.

Always review the latest checklist for installing this update. For more information, see
Checklist for installing update 2309. After you update a site, also review the Post-update
checklist.

To take full advantage of new Configuration Manager features, after you update the site,
also update clients to the latest version. While new functionality appears in the
Configuration Manager console when you update the site and console, the complete
scenario isn't functional until the client version is also the latest.

Site infrastructure

Introducing SQL ODBC driver support for Configuration
Manager
Starting with Configuration Manager 2309 release, Configuration Manager requires the
installation of the ODBC driver for SQL server 18.1.0 or later as a prerequisite. This
prerequisite is required when you create a new site or update an existing one and on all
remote roles.

  ） Important

  Microsoft ODBC Driver for SQL Server 18.1.0 or later needs to be installed on Site
  Servers and site system roles before upgrading to 2309 version. Do not uninstall
  SQL native client 11 until we call out in further communications. Configuration
  Manager doesn't manage the updates for the ODBC driver, ensure that this
  component is up to date.

For more information, see SQL ODBC driver for the site server

<!-- p.215 -->

Option to schedule scripts' runtime
Starting in Configuration Manager current branch version 2309, you can now schedule
scripts' runtime in UTC. The run Script Wizard now offers a scheduling option that
enables administrators to schedule the execution of scripts. It provides a convenient way
to automate the running of scripts on managed devices according to specified
schedules.

For more information, see Schedule scripts' runtime

External service notification Run details from Azure Logic
application
Starting in Configuration Manager current branch version 2309, when Azure Logic App
generates notifications related to specific events, CM can now capture and display these
notifications. This integration enables the monitoring of Azure Logic App notifications
directly within the MCM console, providing a centralized location for tracking critical
events, taking appropriate actions and maintains a high level of operational efficiency.

<!-- p.216 -->

For more information, see External service notification.

New Site Maintenance task “Delete Aged Task Execution
Status Messages” is now available on primary servers to
clean up data older than 30 days or configured number
of days
Starting in Configuration Manager current branch version 2309, you can now enable this
feature by utilizing the Site Maintenance Window or using PowerShell Commandlet. By
default, it has been set to run on Saturday and delete the data older than 30 days. It
does so by cleaning up [dbo].TaskExecutionStatus Table

<!-- p.217 -->

Example: PowerShell Commandlet: Set-CMSiteMaintenanceTask -Sitecode "XXX" -
MaintenanceTaskName "Delete Aged Task Execution Status Messages" -DaysOfWeek Friday

For more information, see Delete Aged Task Execution Status Messages.

Software updates

Update Orchestrator Service (USO) for Windows 11 22H2
or later with windows native reboot experience
In Configuration Manager current branch version 2309, when installing software updates
from Configuration Manager, administrators can now choose to use the native
Windows Update restart experience.To use this feature, client devices must be running
Windows build 22H2 or later. From the Computer Restart client device settings, ensure
that Windows is selected as the restart experience. Branding information is included in
the Windows restart notification for updates that require restart.

For more information, see Device restart notifications

Maintenance window creation using PS cmdlet
We've extended the Offset parameter for Maintenance windows.The cmdlet New-
CMMaintenanceWindow is used to create a maintenance window for a collection. Earlier
the Offset parameter could be set only between 0 and 4. Now it has been extended
between 0 to 7.

Example: PowerShell Commandlet: New-CMSchedule -Start (Get-Date) -DayOfWeek Monday
-WeekOrder Second -RecurCount 1 -OffSetDay 6

OS deployment

OSD preferred MP option for PXE boot scenario
Starting in Configuration Manager current branch version 2309, Preferred Management
Point (MP) option will now allow PXE clients to communicate to an initial lookup MP
and receive the list of MP(s) to be used for further communication. When the option is
enabled, it allows an MP to redirect the PXE client to another MP, based on the client
location in the site boundaries.

<!-- p.218 -->

For more information, see Install-and-configure-distribution-points

Enable Bitlocker through ProvisionTS
In Configuration Manager current branch version 2309, Escrowing recovery key to
Config Manager Database is now supported using ProvisionTS. ProvisionTS is the task
sequence that is executed at the time of provisioning. As a result device can escrow the
key to Config Manager Database instantly.

For more information, see Preprovision-bitlocker-in-windows-pe

Windows 11 Edition Upgrade using CM Policy settings
Starting in Configuration Manager current branch version 2309,administrator can now
create a policy using edition upgrade in Configuration Manager to update the Windows
11 edition.

<!-- p.219 -->

For more information, see Upgrade Windows devices to a new edition

Windows 11 Upgrade Readiness Dashboard
Starting in Configuration Manager current branch version 2309, administrators can use
this dashboard to devise their windows 11 upgrade strategy and discover the devices in
the organization, which are ready for Windows 11 Upgrade. This Dashboard also
provides a count by installed Feature update version and a view of all Windows devices
inside the organization. Administrators can create a collection of Windows 11 ready for
upgrading devices and roll out feature updates to them.

<!-- p.220 -->

                                                                                  

For more information, see Manage Windows 11 readiness dashboard

Cloud-attached management

New Cloud Management Gateway (CMG) creation via
Console
Starting in Configuration Manager current branch version 2309, we have enhanced
security of web (server) app for the creation of CMG. For new CMG creation, users can
select tenant and the app name using the Azure AD tenant name. After selecting tenant
and app name the sign-in button appears, follow rest of the process as per the setup
CMG.

<!-- p.221 -->

  ７ Note

  Pre-existing CMG customers must update their web server app by navigating to
  Azure Active Directory Tenants node --> select the tenant --> select the server app
  --> click on "update application settings".

For more information, see Configure Azure Active Directory for CMG

New Cloud Management Gateway (CMG) creation via
PowerShell
You can now create CMG web (server) app via PowerShell cmdlet, you need to specify
TenantID in the argument:

PowerShell Commandlet: Set-UpdateServerApplication – 'TenantID'

If you try to create the CMG before updating RedirectUrl, you get an error
"Your server Application needs to be updated".

<!-- p.222 -->

PowerShell command: Set-
UpdateServerApplication to update your App, and then try again to create CMG.

  ７ Note

  For new customers, before creating CMG, create Azure AD web server app and
  execute the new PowerShell commandlet script.

For more information, see New-CMCloudManagementGateway

Deprecated features
Learn about support changes before they're implemented in removed and deprecated
items.

     Configured resource access policies will block Configuration Manager 2403
     upgrade, remove existing policies and move the slider to Intune. Please action
     before January 2024, read the FAQ.

For more information, see Removed and deprecated features for Configuration
Manager.

Other updates
For more information on changes to the Windows PowerShell cmdlets for Configuration
Manager, see version 2309 release notes.

Next steps
As of November 1, 2023, version 2309 is globally available for all customers to install.

  ７ Note

  For exisiting Fast ring current branch 2309 customers, you will see Slow ring
  upgrade package in console. Install 2309 Slow ring package to be in production
  current branch.

When you're ready to install this version, see Installing updates for Configuration
Manager and Checklist for installing update 2309.

<!-- p.223 -->

   Tip

  To install a new site, use a baseline version of Configuration Manager.

  Learn more about:

        Installing new sites
        Baseline and update versions

For known significant issues, see the Release notes.

After you update a site, also review the Post-update checklist.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.224 -->

What's changed from System Center
2012 Configuration Manager
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

The current branch of Configuration Manager introduces important changes from
System Center 2012 Configuration Manager. This article identifies significant changes
and new capabilities found in the original baseline version 1511 of Configuration
Manager current branch. To learn about changes introduced in recent updates for
Configuration Manager, see What's new in Configuration Manager incremental versions.

  ７ Note

  Since October 2019, Configuration Manager is part of Microsoft Intune family of
  products. For more information, see Microsoft Configuration Manager FAQ.

The December 2015 release (version 1511) of Configuration Manager was the initial
release of the current Configuration Manager product from Microsoft. It's typically
referred to as Configuration Manager current branch. Current branch indicates this
version supports incremental updates to the product. It also provides a way to
distinguish between this release and previous releases of Configuration Manager.

Configuration Manager current branch:

      Doesn't use a year or product identifier in the product name, unlike past versions
      such as Configuration Manager 2007 or System Center 2012 Configuration
      Manager.

      Supports incremental, in-product updates, also called update versions. The initial
      release was version 1511. Later versions are released several times a year as in-
      console updates, like version 1910.

      Is installed using a baseline version. While 1511 was the original baseline version,
      new baseline versions are also released from time to time, like 2203. Baseline
      versions can be used to install a new Configuration Manager site and hierarchy, or
      to upgrade from a supported version of System Center 2012 Configuration
      Manager.

In-console updates

<!-- p.225 -->

Configuration Manager uses an in-console service method called Updates and
Servicing that makes it easy to locate and install recommended updates.

Some versions are only available as updates for existing sites from within the
Configuration Manager console. You can't use these updates to install a new
Configuration Manager site. For example, the 2111 update is only available from within
the Configuration Manager console. It's used to update a site that already runs a
supported version of Configuration Manager.

Periodically, an update version is also released as a new baseline version. For example,
update version 2203 is also a baseline. Use a baseline version to install a new site or
hierarchy. Don't start with an older baseline version like 2111, and upgrade your way to
the most current version. Always use the latest baseline.

For more information, see the following articles:

     Updates for Configuration Manager
     Baseline and update versions

Service connection point
Configuration Manager current branch includes a new site system role, the service
connection point:

     A point of contact for many cloud-enabled features

     Downloads updates for your site

     Uploads diagnostics and usage data about your site to the Microsoft cloud

This site system role supports both online and offline modes of operation. For more
information, see About the service connection point.

Diagnostics and usage data
Configuration Manager collects diagnostics and usage data about your sites and
infrastructure. This information is compiled and submitted to the Microsoft cloud service
by the service connection point. Configuration Manager requires this data to download
updates that are applicable for your environment. When you set up the service
connection point, you can specify both the level of data that it collects, and whether
automatically (online) or manually (offline) submits the data.

For more information, see Diagnostics and usage data.

<!-- p.226 -->

Deprecated functionality
Some features, like native Support for Intel Active Management Technology (AMT)
based-computers, are removed from the Configuration Manager console. Other
features, like Network Access Protection, are removed entirely. Additionally, some older
Microsoft products like Windows Vista, Windows Server 2008, and SQL Server 2008, are
no longer supported.

For a list of deprecated features, see Removed and deprecated items.

For details about supported products, operating systems, and configurations, see
Supported configurations.

Support for Intel Active Management Technology (AMT)
Configuration Manager current branch removes native support for AMT-based
computers from within the Configuration Manager console. AMT-based computers
remain fully managed when you use the Intel SCS Add-on for Microsoft Configuration
Manager      . The add-on provides you access to the latest capabilities to manage AMT,
while removing limitations introduced until Configuration Manager could incorporate
those changes.

The removal of integrated AMT for Configuration Manager includes out-of-band
management. The out-of-band management point site system role is no longer
available.

  ７ Note

  This change doesn't affect out-of-band management in System Center 2012
  Configuration Manager.

Changes in functionality
The following sections summarize some of the significant changes in feature areas
between System Center 2012 R2 Configuration Manager and the version 1511 version of
Configuration Manager current branch. For more information on more recent changes
in functionality, see What's new in incremental versions.

Client deployment

<!-- p.227 -->

Configuration Manager introduces a new feature for testing new versions of the
Configuration Manager client before upgrading the rest of site with the new software.
You can set up a pre-production collection in which to pilot a new client. Once you're
satisfied with the new client software in pre-production, you can promote the client to
automatically upgrade the rest of the site with the new version.

For more information on how to test clients, see How to test client upgrades in a pre-
production collection.

OS deployment
Be aware of the following changes to OS deployment:

     In the Create Task Sequence Wizard, a new task sequence type is available:
     Upgrade an operating system from upgrade package. It creates the steps to
     upgrade computers from an earlier version of Windows to Windows 10 or later. For
     more information, see Upgrade Windows to the latest version.

     Windows PE peer cache is now available when you deploy operating systems.
     Computers that run a task sequence to deploy an OS can use Windows PE peer
     cache to obtain content from a peer cache source, instead of downloading content
     from a distribution point. This behavior helps minimize WAN traffic in branch office
     scenarios where there's no local distribution point. For more information, see
     Prepare Windows PE peer cache to reduce WAN traffic.

     You can now view the state of Windows as a service in your environment. You can
     also create servicing plans to form deployment rings, and make sure that Windows
     10 or later computers are kept up to date when new builds are released.
     Additionally, you can view alerts when Windows clients are near the end of support
     for their build. For more information, see Manage Windows as a service.

Application management
Be aware of the following changes to application management:

     Configuration Manager lets you deploy Universal Windows Platform (UWP) apps
     for devices running Windows 10 and later. For more information, see Creating
     Windows applications.

     Software Center has a new, modern look. User-available apps that previously only
     appeared in the application catalog now appear in Software Center under the
     Applications tab. This behavior makes these deployments more discoverable, and
     makes it unnecessary for users to refer to the separate application catalog.

<!-- p.228 -->

     Additionally, a Silverlight-enabled browser is no longer required. For more
     information, see Plan for and configure application management.

     The new Windows Installer through MDM application type lets you create and
     deploy Windows Installer-based apps to enrolled PCs that run Windows 10 or later.
     For more information, see Creating Windows applications.

     In Configuration Manager 2012, to specify a link to an app in the Windows Store,
     you could either specify the link directly, or browse to a remote computer that had
     the app installed. In Configuration Manager current branch, you can still enter the
     link directly, but now, instead of browsing to a reference computer, you can
     browse the store for the app directly from the Configuration Manager console.

Software updates
Be aware of the following changes to software updates:

     Configuration Manager can now detect the difference between software update
     management methods for computers. Specifically, it can differentiate between a
     Windows computer that connects to Windows Update for Business (WUfB), and a
     computer connected to WSUS. The UseWUServer attribute is new, and specifies
     whether the computer is managed with WUfB. You can use this setting in a
     collection to remove these computers from software update management. For
     more information, see Integration with Windows Update for Business.

     You can now schedule and run the WSUS clean-up task from the Configuration
     Manager console. In Software Update Point Component properties, when you
     select to run the WSUS clean-up task, it runs at the next software updates
     synchronization. The expired software updates are set to a status of declined on
     the WSUS server, and the Windows Update Agent on computers no longer scans
     these software updates. For more information, see Schedule and run the WSUS
     clean up task.

Compliance settings
Be aware of the following changes to compliance settings:

     Configuration Manager improves the workflow for creating configuration items.
     Now, when you create a configuration item, and select supported platforms, only
     the settings relevant to that platform are available. See Get started with
     compliance settings.

<!-- p.229 -->

     The Create Configuration Item wizard now makes it easier to choose the
     configuration item type you want to create. Additionally, new and updated
     configuration items are available for:

        Windows 10 or later devices managed with the Configuration Manager client

        mac OS X devices managed with the Configuration Manager client

        Windows desktop and server computers managed with the Configuration
        Manager client

        Windows 8.1 and Windows 10 or later devices managed without the
        Configuration Manager client

     For more information, see How to create configuration items.

     Support for managing settings on macOS X computers that are managed without
     the Configuration Manager client.

On-premises mobile device management
You can now manage mobile devices by using on-premises Configuration Manager
infrastructure. All device and management data are handled on-premises, and isn't part
of Microsoft Intune or other cloud services. This type of device management doesn't
require client software. Configuration Manager manages devices with functionality that's
built into the device OS.

For more information, see Manage mobile devices with on-premises infrastructure.

Next steps
What's new in incremental versions

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.230 -->

Removed and deprecated items for
Configuration Manager
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

This article describes how to use the information about features, products, and
operating systems that are removed from support for Configuration Manager. Items
that are deprecated will be removed in a future update. These articles provide early
notice about future changes that might affect your use of Configuration Manager.

This information is subject to change with future releases, and might not include each
deprecated feature, product, or OS.

How to use this information
When a feature, product, or OS is first listed as deprecated, support for using it with
Configuration Manager is scheduled to be removed in a future update. This information
is provided to help you plan for alternatives to using that feature, product, or OS. When
the first version of Configuration Manager releases in which that support is removed,
this article is updated to indicate that specific version.

  ７ Note

  Unless noted otherwise, a feature, product, or OS that's deprecated in
  Configuration Manager typically continues to be fully supported, available, and
  usable.

When support is removed for a feature or OS, the feature or OS remains supported
when you use a previous version of Configuration Manager, as long as that version of
Configuration Manager remains in support. However, when you use a version of
Configuration Manager released after the date or version indicated, that version of
Configuration Manager doesn't provide support.

For example, if a feature was scheduled to have its support removed with the first
update released after September 2019, support for that feature would no longer be
included in update 1910, which released in November of 2019.

      With Update 1910, the feature is no longer supported.
      The article is updated to indicate support was removed with version 1910.

<!-- p.231 -->

However, if you continue to use an earlier version that supports the feature, like version
1906, you can continue to use that feature until the version you use drops out of
support.

See also
     Microsoft Support Lifecycle

     Support for current branch versions of Configuration Manager

Next steps
Items that are removed or deprecated are split between three categories:

     Removed and deprecated features

     Removed and deprecated items for site servers

     Removed and deprecated items for clients

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.232 -->

Removed and deprecated features for
Configuration Manager
Applies to: Configuration Manager (current branch)

This article lists the features that are deprecated or removed from support for Configuration
Manager. Deprecated features will be removed in a future update. These future changes might
affect your use of Configuration Manager.

This information is subject to change with future releases. It might not include each deprecated
Configuration Manager feature.

Deprecated features
The following features are deprecated. You can still use them now, but Microsoft plans to end
support in the future.

                                                                                         ﾉ   Expand table

 Feature                                                                   Deprecation       Planned end
                                                                           first             of support
                                                                           announced

 Microsoft Connected Cache (MCC) integration in Configuration Manager      June 2026         TBD
 will be deprecated in a future release of Configuration Manager. After
 deprecation, no further feature development or updates will be provided
 for Microsoft Connected Cache within Configuration Manager. Customers
 should begin transitioning to the standalone version of Microsoft
 Connected Cache to continue receiving ongoing improvements and
 support. For more information, see Microsoft Connected Cache.

 The MDT Integration with CM and Standalone is no longer supported         Dec 2024          The first
 with Configuration Manager. Customers should remove MDT TS steps,                           release after
 followed by removing MDT integration, to avoid TS corruption and                            Oct 10, 2025
 modification failures. More information on the MDT retirement here.

 Office 365 Client Management dashboard add-in support statement.          April 2024        The first
 For more information, see Office 365 Client Management dashboard.                           release after
                                                                                             April 1, 2025

 Windows Information Protection                                            July 2022         TBD

<!-- p.233 -->

Feature                                                                    Deprecation     Planned end
                                                                           first           of support
                                                                           announced

The site system roles for on-premises MDM and macOS clients:               January 2022    Mar 31, 2024
enrollment proxy point and enrollment point.

The Microsoft Store for Business and Education. For more information,      November        The first
see Manage apps from the Microsoft Store for Business and Education        2021            release after
with Configuration Manager.                                                                March 1,
                                                                                           2023

Asset intelligence. For more information, see Asset intelligence           November        The first
deprecation.                                                               2021            release after
                                                                                           November 1,
                                                                                           2022

On-premises MDM. For more information, see On-premises MDM in              November        The first
Configuration Manager.                                                     2021            release after
                                                                                           November 1,
                                                                                           2022

Azure Active Directory (Azure AD) Graph API and Azure AD Authentication    July 2021       June 30, 2022
Library (ADAL), which is used by Configuration Manager for some cloud-
attached scenarios. If you use cloud-attached features such as co-
management, tenant attach, or Microsoft Entra discovery, starting June
30, 2022, these features may not work correctly in Configuration Manager
version 2107 or earlier. Stay current with Configuration Manager to make
sure these features continue to work. For more information, see CMG
FAQ.

The BitLocker management implementation for the recovery service has       March 2021      The first
changed. The legacy MBAM-based service is replaced by the messaging                        release after
processing engine on the management point.                                                 Mar 2025

Older style of console extensions that haven't been approved in the        April 2021      TBDNote 1
Console Extension node, will no longer be supported. For more
information about new console extensions, see Manage console
extensions.

The implementation for sharing content from Azure has changed. Use a       February 2019   The first
content-enabled cloud management gateway. Starting in version 2107,                        release after
you can't create a traditional cloud distribution point.                                   October 5,
                                                                                           2022

Cloud management gateway and cloud distribution point deployments          November        The first
with Azure Service Manager using a management certificate. For more        2018            release after
information, see Plan for CMG.                                                             October 5,
                                                                                           2022

<!-- p.234 -->

Note 1: Support removed TBD
The specific timeframe is to be determined (TBD). Microsoft recommends that you change to the
new process or feature, but you can continue to use the deprecated process or feature for the
near future.

Unsupported and removed features
The following features are no longer supported. In some cases, they're no longer in the product.

                                                                                        ﾉ   Expand table

 Feature                                                              Deprecation    Support removed
                                                                      first
                                                                      announced

 System Center Update Publisher (SCUP) and integration with           October 2023   Jan 31, 2024
 ConfigMgr

 Sites that allow HTTP client communication. Configure the site for   March 2021     The first release
 HTTPS or Enhanced HTTP. For more information, see Enable the                        after April 1, 2024
 site for HTTPS-only or enhanced HTTP.

 Upgrade from any version of System Center 2012 Configuration         April 2022     Version 2303
 Manager to current branch. For more information, see Upgrade to
 Configuration Manager current branch

 The Configuration Manager client for macOS and Mac client            January 2022   December 31, 2022
 management. For more information, see Supported clients: Mac
 computers. Migrate management of macOS devices to Microsoft
 Intune. For more information, see Deployment guide: Manage
 macOS devices in Microsoft Intune.

 Community hub service and integration with ConfigMgr                 October 2022   The first release
                                                                                     after March 1, 2023

 The geographical view in the Site Hierarchy node of the              August 2020    The first release
 Monitoring workspace in the Configuration Manager console.                          after September
                                                                                     2023

 Desktop Analytics. For more information, see Windows                 November       November 30, 2022
 compatibility reports in Intune   .                                  2021

 The ability to deploy a cloud management gateway (CMG) as a          September      Version 2203
 cloud service (classic). All CMG deployments should use a virtual    2021
 machine scale set.

<!-- p.235 -->

Feature                                                                 Deprecation    Support removed
                                                                        first
                                                                        announced

Cloud management gateway (CMG) as a cloud service (classic). All                       Version 2403
CMG deployments should use a virtual machine scale set.

The following compliance settings for Company resource access:          March 2021     Version 2203
Certificate profiles, VPN profiles, Wi-Fi profiles, Windows Hello for
Business settings, and email profiles. This deprecation includes the
co-management resource access workload. Use Microsoft Intune to
deploy resource access profiles. For more information, see
Frequently asked questions about resource access deprecation.

Desktop Analytics data for Windows 7, Windows 8, and earlier            July 2021      January 31, 2022
versions of Windows 10 that don't support the Windows diagnostic
data processor configuration.

Third-party add-ons that use Microsoft .NET Framework version           September      Version 2111
4.6.1 or earlier, and rely on Configuration Manager libraries. Such     2021
add-ons need to use .NET 4.6.2 or later. For more information, see
External dependencies require .NET 4.6.2.

Log Analytics connector for Azure Monitor. This feature is called       November       Version 2107
the OMS Connector in the Azure Services node.                           2020

Microsoft Edge legacy browser profiles. For more information, see       March 2021     April 2021
New Microsoft Edge to replace Microsoft Edge Legacy with April's
Windows 10 Update Tuesday release

The collection evaluation viewer, which was integrated in version       November       Version 2103
2010.                                                                   2020

Desktop Analytics tile and page for Security Updates                    December       March 2021
                                                                        2020

Desktop Analytics option to View recent data for device                 May 2020       July 2020
enrollment and security updates. For more information, see Data
latency.

Windows Analytics and Upgrade Readiness integration. For more           October 14,    January 31, 2020
information, see KB 4521815: Windows Analytics retirement on            2019
January 31, 2020   .

Device health attestation assessment for Conditional Access             July 3, 2019   Version 1910
compliance policies For more information, see What happened to
hybrid MDM.

The Configuration Manager Company Portal app                            May 21, 2019   Version 1910

The application catalog, including both site system roles: the          May 21, 2019   Version 1910
application catalog website point and web service point. For more

<!-- p.236 -->

Feature                                                               Deprecation     Support removed
                                                                      first
                                                                      announced

information, see Remove the application catalog.

Certificate-based authentication with Windows Hello for Business      December        Version 1910
settings in Configuration Manager                                     2017
For more information, see Windows Hello for Business settings.

System Center Endpoint Protection for Mac and Linux                   October 2018    December 31, 2018
For more information, see End of support blog post .

On-premises Conditional Access                                        January 30,     September 1, 2019
For more information, see What happened to hybrid MDM.                2019

Hybrid mobile device management (MDM)                                 August 14,      September 1, 2019
For more information, see What happened to hybrid MDM.                2018

Starting with the 1902 Intune service release, expected at the end
of February 2019, new customers can't create a new hybrid
connection.

Security Content Automation Protocol (SCAP) extensions.               September       Version 1810
                                                                      2018

The Silverlight user experience for the application catalog website   August 11,      Version 1806
point is no longer supported. Users should use the new Software       2017
Center. For more information, see Configure Software Center.

The previous version of Software Center.                              December 13,    Version 1802
                                                                      2016
For more information about the new Software Center, see Plan for
and configure application management.

Management of Virtual Hard Disks (VHDs) with Configuration            January 6,      Version 1710
Manager.                                                              2017

This deprecation includes removal of options to create a new VHD
or manage a VHD using a task sequence, and the removal of the
Virtual Hard Disks node from the Configuration Manager console.

Existing VHDs are not deleted, but are no longer accessible from
within the Configuration Manager console.

Task sequences:                                                       November 18,    Version 1710
- Convert Disk to Dynamic                                             2016
- Install Deployment Tools

Upgrade Assessment Tool                                               September 12,   July 11, 2017
                                                                      2016
The Upgrade Assessment Tool depends on both Configuration

<!-- p.237 -->

 Feature                                                                Deprecation     Support removed
                                                                        first
                                                                        announced

 Manager and the Application Compatibility Toolkit (ACT) 6.x. The
 final version of ACT was shipped in the Windows 10 v1511 ADK. As
 there are no further updates to ACT, support for the Upgrade
 Assessment Tool is discontinued. Deprecation notice was added to
 the download page for UAT on September 12, 2016.

 Software update points with a network load balancing (NLB) cluster     February 27,    Version 1702
                                                                        2016

 Task sequences:                                                        June 20, 2016   Version 1606
 - OSDPreserveDriveLetter

 During an operating system deployment, by default, Windows
 Setup now determines the best drive letter to use (typically C:). If
 you want to specify a different drive to use, you can change the
 location in the Apply Operating System task sequence step. Go to
 the Select the location where you want to apply this operating
 system setting. Select Specific logical drive letter and choose the
 drive that you want to use.

 Network Access Protection (NAP) - as found in System Center 2012       July 10, 2015   Version 1511
 Configuration Manager

 Out of Band Management - as found in System Center 2012                October 16,     Version 1511
 Configuration Manager                                                  2015

 System Center Configuration Manager Management Pack - for              October 16,     Version 1511
 System Center Operations Manager is not available for download         2015

WINS
Windows Internet Name Service (WINS) is a legacy computer name registration and resolution
service. It's a deprecated service. You should replace WINS with Domain Name System (DNS). For
more information, see Windows Internet Name Service (WINS).

Out of Band Management
With Configuration Manager, native support for AMT-based computers from within the
Configuration Manager console has been removed.

     AMT-based computers remain fully managed when you use the Intel SCS Add-on for
     Configuration Manager . The add-on provides you access to the latest capabilities to

<!-- p.238 -->

     manage AMT, while removing limitations introduced until Configuration Manager could
     incorporate those changes.

     Out of Band Management in System Center 2012 Configuration Manager is not affected by
     this change.

Network Access Protection
Configuration Manager has removed support for Network Access Protection. The feature has
been deprecated in Windows Server 2012 R2, and is removed from Windows 10.

For network access protection alternatives, see the Deprecated functionality section of Network
Policy and Access Services Overview.

See also
     Removed and deprecated
     Microsoft Support Lifecycle
     Support for current branch versions of Configuration Manager

Last updated on 06/11/2026

<!-- p.239 -->

Removed and deprecated for
Configuration Manager site servers
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

This article describes products and operating systems that are removed from support for
Configuration Manager site servers, or will be removed in a future update (deprecated).
It provides early notice about future changes that might affect your use of Configuration
Manager.

This information may change in the future. It might not include each deprecated feature,
product, or OS.

Client OS
                                                                           ﾉ   Expand table

 Operating systems         Deprecation first announced              Support removed

 Windows 10 22H2           Oct 2021                                 Version 2509

Server OS
                                                                           ﾉ   Expand table

 Operating systems                    Deprecation first announced       Support removed

 Windows Server 2008 R2 with SP1      July 2015                         Version 1702

 Windows Server 2008 with SP2         July 2015                         Version 1511

SQL Server
                                                                           ﾉ   Expand table

 SQL Server versions    Deprecation first announced      Support removed

 Sql Server 2014        Oct 2024                         Version 2409

<!-- p.240 -->

 SQL Server versions       Deprecation first announced   Support removed

 SQL Server 2012           July 2021                     The first release after July 1, 2022

 SQL Server 2008 R2        July 2015                     Version 1702

 SQL Server 2008           July 2015                     Version 1511

If you need to upgrade your version of SQL Server, we recommend the following
methods, from easy to more complex:

   1. Upgrade SQL Server in-place (recommended).

   2. Install a new version of SQL Server on a new computer. Then to point your site
     server at the new SQL Server, use the database move option of Configuration
     Manager setup.

   3. Use backup and recovery.

  ７ Note

  Make sure to also upgrade versions of SQL Server Express at secondary sites.

Next steps
For more information, see the following articles:

     Removed and deprecated

     Microsoft Support Lifecycle

     Support for current branch versions of Configuration Manager

Feedback
Was this page helpful?      Yes        No

Provide product feedback
