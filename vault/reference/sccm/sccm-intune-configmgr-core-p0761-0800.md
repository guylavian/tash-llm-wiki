---
title: "Core infrastructure documentation — pages 761-800"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0761-0800
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0761-0800
family: sccm
documentKind: "doc"
abstract: "Console improvements PowerShell release notes preview Next steps For more information, see the following articles: Evaluate Configuration Manager in a lab What's new in Configuration Manager incremental versions Introduction to Configuration Manager  Tip For more information on"
---

# Core infrastructure documentation — pages 761-800

<!-- p.761 -->

     Console improvements
     PowerShell release notes preview

Next steps
For more information, see the following articles:

     Evaluate Configuration Manager in a lab
     What's new in Configuration Manager incremental versions
     Introduction to Configuration Manager

   Tip

  For more information on current branch features that require consent to enable,
  see pre-release features.

  For more information on current branch features that you must enable first, see
  Enable optional features from updates.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.762 -->

Features in Configuration Manager technical
preview version 2411
Applies to: Configuration Manager (technical preview branch)

This article introduces the features that are available in the technical preview for Configuration
Manager, version 2411. Install this version to update and add new features to your technical
preview site. When you install a new technical preview site, this release is also available as a
baseline version.

Review the technical preview article before installing this update. That article familiarizes you with
the general requirements and limitations for using a technical preview, how to update between
versions, and how to provide feedback.

The following sections describe the new features to try out in this version:

Operating System support added for Windows 11 24H2
and Windows Server 2025
With this version of Configuration Manager, support is added for Windows 11 24H2 and
Windows Server 2025.

     Windows 11 24H2 & Windows Server 2025 are added to the product lifecycle dashboard
     and supported platform.
     Windows 11 24H2 & Windows Server 2025 client support is added.
     Boot image creation in CM on Windows Server 2025 now supports latest Windows ADK.
     Windows upgrade readiness dashboard now supports Windows 11 24H2 for upgrading
     clients.

  ７ Note

  Windows Server and Windows 11 24H2 do not support Firewall rules. This will result in a
  non-compliant status in the Configuration Manager applet.

Enhanced Security for CMG

<!-- p.763 -->

CMG Setup now uses managed identities and third party Server App to interact with CMG's
Azure storage account, instead of storage account keys.

     Hence storage account key access is disabled for new CMG setup.

     For sessions upgrading from earlier versions to 2411 tp, the CMG Enhance Security button
     is shown as enabled.

                                                                                          

     When the enhanced security option is selected, the VMSS OS Auto Upgrade feature is also
     activated. An extra panel appears, prompting the admin to provide maintenance window
     details. Azure uses this information to schedule upgrades whenever new OS images become
     available.

                                                                                          

<!-- p.764 -->

CMG Entra Application secret key renewal
The 'Renew Secret Key' feature now opens a dialog with four options for the validity period. This
update also prevents applications older than 800 days (approximately two years) from renewing
their secret keys. The same options are available when creating a new app.

                                                                                               

Sign in using tenant Global Administrator credentials and then click on the renew button.

  ） Important

  The Microsoft Entra Global Administrator role is a highly privileged role and should only be
  used when another role can't be used. This feature requires the Global Administrator role.
  For other features, Microsoft recommends using roles with the fewest permissions. To learn
  more, see Fundamentals of role-based administration for Configuration Manager.

SQL 2012 and 2014 support are deprecated
Starting with this version, Configuration Manager no longer supports SQL Server 2012 and 2014.
Upgrade to the latest SQL Server version or at least SQL Server 2016. If you don’t upgrade, CM

<!-- p.765 -->

upgrades are blocked, and you see an error during the prereq check.

Software metering support in Arm64 devices
The Configuration Manager now supports Software metering for Arm64 devices. Software
metering is used to monitor Windows PC desktop apps with a filename ending in .exe. For more
information, see Software metering in Configuration Manager.

Next steps
For more information about installing or updating the technical preview branch, see Technical
preview.

For more information about the different branches of Configuration Manager, see Which branch
of Configuration Manager should I use?.

Last updated on 01/29/2026

<!-- p.766 -->

Features in Configuration Manager technical
preview version 2405
Applies to: Configuration Manager (technical preview branch)

This article introduces the features that are available in the technical preview for Configuration
Manager, version 2405. Install this version to update and add new features to your technical
preview site. When you install a new technical preview site, this release is also available as a
baseline version.

Review the technical preview article before installing this update. That article familiarizes you with
the general requirements and limitations for using a technical preview, how to update between
versions, and how to provide feedback.

The following sections describe the new features to try out in this version:

Configuration Manager now supports SQL Extended
Protection for Authentication
Configuration Manager now supports SQL Extended Protection for Authentication. It's a security
feature that enhances protection against MITM attacks, making SQL Server more secure when
connections are made using Extended Protection. These enhancements collectively reduce the
risk of unauthorized access and protect sensitive data managed by the SQL Server Database
Engine.

For more information, see Connect to the Database Engine Using Extended Protection

BitLocker support in Arm devices
Configuration Manager now supports BitLocker Task Sequence steps for Arm devices. In BitLocker
Management, policies that include OS Drive encryption with a TPM protector and Fixed Drive
encryption with the Auto-Unlock option are supported on Arm devices.

Performance Enhancement of policy processing and
collection evaluation

<!-- p.767 -->

The performance of policy processing and collection evaluation has been enhanced. Previously,
blocking chains from sp_ProcessPolicyChanges, called by PolicyPv, would run for hours,
disrupting multiple workloads including collection management and policy processing.

Introducing Centralized Search - Desired
Workspace Selection
The centralized search box now enables the option to select the desired workspace for searching.
Users can easily refine their search results by selecting the desired workspace from the dropdown
menu.

                                                                                           

Known issues
Unable to import or connect to Powershell Configuration
Manager module via console
While importing or connecting to Configuration manager Powershell module via CM console
users get the following error message : PS C:\Build\AdminConsole\bin> Import-Module
.\ConfigurationManager.psd1 Import-Module : The module manifest

'C:\Build\AdminConsole\bin\ConfigurationManager.psd1' could not be processed because it is

not a valid Windows PowerShell restricted language file. Remove the elements that are not

permitted by the restricted language

<!-- p.768 -->

Configuration Manager console won't automatically update
If you update a technical preview site from version 2401 to a later version, the Configuration
Manager console fails to update. This problem is because of a known issue in the extension
installer.

Mitigation: To work around this issue, after you update the site from version 2401 to a later
version, manually uninstall the previous console and run ConsoleSetup.exe.

For more information, see Install the Configuration Manager console

Next steps
For more information about installing or updating the technical preview branch, see Technical
preview.

For more information about the different branches of Configuration Manager, see Which branch
of Configuration Manager should I use?.

 Last updated on 06/07/2024

<!-- p.769 -->

Features in Configuration Manager technical
preview version 2401
Applies to: Configuration Manager (technical preview branch)

This article introduces the features that are available in the technical preview for Configuration
Manager, version 2401. Install this version to update and add new features to your technical
preview site.

Review the technical preview article before installing this update. That article familiarizes you with
the general requirements and limitations for using a technical preview, how to update between
versions, and how to provide feedback.

The following sections describe the new features to try out in this version:

Automated diagnostic Dashboard for Software
Update Issues
A new dashboard is added to the console under monitoring workspace which shows the
diagnosis of the software update issues in your environment. You can fix software update issues
based on CM troubleshooting documentation.

Introducing Centralized Search box: Effortlessly Find
What You Need in the Console!

<!-- p.770 -->

Users can now use the global search box in CM console which streamlines the search experience
and centralizes access to information. This enhances the overall usability, productivity and
effectiveness of CM. Users no longer need to navigate through multiple nodes or sections/
folders to find information they require, saving valuable time and effort.

Microsoft Azure Active Directory rebranded to
Microsoft Entra ID
Starting Configuration Manager version 2403, Microsoft Azure Active Directory is renamed to
Microsoft Entra ID within Configuration Manager.

Enhancement in Deploying Software Packages with
Dynamic Variables
With the introduction of retry count in UI administrators while deploying the "Install Software
Package" via Dynamic variable with "Continue on error" unchecked to clients, won't be notified
with task sequence failures even if package versions on the distribution point are updated.

<!-- p.771 -->

Enabling Auto-Image Patching for CMG Virtual
Machine Scale Set
With this version of CM Configuration Manager Cloud Management Gateway (CMG) Virtual
Machine Scale introduces enabling of Auto-Image Patching for seamless and automated updates
to ensure your environment stays current and secure with this efficient solution.

Window 11 Readiness dashboard to support
Windows 23H2
With this version of Configuration Manager, the Windows 11 readiness dashboard will show
charts for Windows 23H2.

HTTPS or Enhanced HTTP should be enabled
for client communication from this version of
Configuration Manager
HTTP-only communication is deprecated, and support is removed from this version of
Configuration Manager. Please enable HTTPS or Enhanced HTTP for client communication.

<!-- p.772 -->

Upgrade to CM 2403 is blocked if CMG V1 is running as
a cloud service (classic)
The option to upgrade Configuration Manager 2403 is blocked if you're running cloud
management gateway V1 (CMG) as a cloud service (classic).All CMG deployments should use a
virtual machine scale set.

Windows Server 2012/2012 R2 operating system site
system roles aren't supported from this version of
Configuration Manager
Starting 2403, Windows Server 2012/2012 R2 operating system site system roles aren't supported
in any CB releases.

Improvements to Bitlocker

<!-- p.773 -->

This release includes the following improvements to Bitlocker:

      Based on your feedback, this feature ensures proper verification of key escrow and prevents
      message drops. We now validate whether the key is successfully escrowed to the database,
      and only on successful escrow we add the key protector.
      This feature prevents a potential data loss scenario where BitLocker is protecting the
      volumes with keys that are never backed up to the database, in any failures to escrow
      happens.

General known issues
Upgrading from TP 2311 to 2401 may encounter a prereq check failure if the Resource Access
slider is already in Intune. This regression is caused by the previous TP. To resolve this issue,
follow these steps:

      Move any other slider (Apps/Endpoint) to Configuration Manager (CM) or Intune.
      Choose to apply the changes and click 'Ok.'
      Proceed with upgrading the site to TP 2401.
      Once the upgrade is complete, you can revert the (Apps/Endpoint) slider back to its old
      settings."

Next steps
For more information about installing or updating the technical preview branch, see Technical
preview.

For more information about the different branches of Configuration Manager, see Which branch
of Configuration Manager should I use?.

 Last updated on 02/07/2024

<!-- p.774 -->

Features in Configuration Manager technical
preview version 2311
Applies to: Configuration Manager (technical preview branch)

This article introduces the features that are available in the technical preview for Configuration
Manager, version 2311. Install this version to update and add new features to your technical
preview site. When you install a new technical preview site, this release is also available as a
baseline version.

Review the technical preview article before installing this update. That article familiarizes you with
the general requirements and limitations for using a technical preview, how to update between
versions, and how to provide feedback.

The following sections describe the new features to try out in this version:

Folder support for Scripts node in Software Library
You can now organize scripts by using folders. This change allows for better categorization and
management of scripts. Full Administrator and Operations Administrator roles can manage the
folders.

New parameter SoftwareUpdateO365Language is
added to Save-CMSoftwareUpdate cmdlet

<!-- p.775 -->

A new parameter SoftwareUpdateO365Language is now added to PowerShell Save-
CMSoftwareUpdate cmdlet. Customers now don't have to check a specific language in the SUP
Properties (causing a metadata download for that language for all updates).

PowerShell Commandlet: Save-CMSoftwareUpdate – SoftwareUpdateO365Language <language name>
(<region name>)"

  ７ Note

  Languages need to be in O365 format to be consistent with Admin Console UI. E.g.
  "Hungarian (Hungary)".

Support for ARM64 Operating System Deployment
Configuration Manager operating system deployment support is now added on Windows 11
ARM64 devices. Currently Importing and customizing Arm64 boot images, Wipe and load Task
Sequence, Media creation Task sequence and WDS PXE for Arm64 is supported.

Resource access profiles and deployments will block
Configuration manager upgrade
Any configured Resource access profiles and associated deployments will block the Configuration
manager upgrade. Please consider deleting them and moving the co-management workload for
Resource Access (if co-managed) to Intune.

WildCard Support added in Defender Exploit Guard
policy for Controlled Folders
Defender Exploit Guards policy for Controlled Folder now accepts Regex in the file path for apps.

E.g. [C:\Folder\Subfolder\app?.exe] [C:\Folder1\Sub*Name]

Next steps
For more information about installing or updating the technical preview branch, see Technical
preview.

For more information about the different branches of Configuration Manager, see Which branch
of Configuration Manager should I use?.

<!-- p.776 -->

Last updated on 11/27/2023

<!-- p.777 -->

Migrate data between hierarchies in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use migration to transfer data from a supported source hierarchy to your Configuration
Manager (current branch) destination hierarchy. When you migrate data from a source
hierarchy:

      You access data from the site databases in the source infrastructure, and then
      transfer that data to your current environment.

      Migration doesn't change the data in the source hierarchy. Instead it discovers the
      data and stores a copy in the database of the destination hierarchy.

Consider the following points when you plan your migration strategy:

      You can migrate an existing Configuration Manager 2007 SP2 infrastructure to
      Configuration Manager (current branch).

      You can migrate some or all of the supported data from a source site.

      You can migrate the data from a single source site to several different sites in the
      destination hierarchy.

      You can move data from multiple source sites to a single site in the destination
      hierarchy.

The following video discusses and demonstrates two common migration scenarios. It
also includes options for including Microsoft Azure in migration plans.
https://www.youtube-nocookie.com/embed/6_0EwW-5b4E

Concepts
Configuration Manager uses the following concepts and terms during migration.

Source hierarchy

A hierarchy that runs a supported version of Configuration Manager and has data that
you want to migrate. When you set up migration, you identify the source hierarchy
when you specify the top-level site of a source hierarchy. After you specify a source

<!-- p.778 -->

hierarchy, the top-level site of the destination hierarchy gathers data from the database
of the designated source site to identify the data that you can migrate.

For more information, see Source hierarchies.

Source sites
The sites in the source hierarchy that have data that you can migrate to your destination
hierarchy.

For more information, see Source sites.

Destination hierarchy

A Configuration Manager (current branch) hierarchy where migration runs to import
data from a source hierarchy.

Data gathering
The ongoing process of identifying the information in a source hierarchy that you can
migrate to your destination hierarchy. Configuration Manager checks the source
hierarchy on a schedule. This process identifies any changes to information in the source
hierarchy that you previously migrated and that you might want to update in the
destination hierarchy.

For more information, see Data gathering.

Migration jobs
The process of configuring the specific objects to migrate, and then managing the
migration of those objects to the destination hierarchy.

For more information, see Planning a migration job strategy.

Client migration

The process of transferring information that clients use from the database of the source
site to the database of the destination hierarchy. This migration of data is then followed
by an upgrade of client software on devices to the client software version from the
destination hierarchy.

For more information, see Planning a client migration strategy.

<!-- p.779 -->

Shared distribution points
The distribution points from the source hierarchy that Configuration Manager shares
with the destination hierarchy during the migration period.

During the migration period, clients assigned to sites in the destination hierarchy can
get content from shared distribution points.

For more information, see Share distribution points between source and destination
hierarchies.

Monitoring migration

The process of monitoring migration activities. You monitor migration progress and
success from the Migration node in the Administration workspace.

For more information, see Planning to monitor migration activity.

Stop gathering data

The process of stopping data gathering from source sites. When you no longer have
data to migrate from a source hierarchy, or if you want to pause migration-related
activities, you can configure the destination hierarchy to stop gathering data from the
source hierarchy.

For more information, see Data gathering.

Clean up migration data
The process of finishing migration from a source hierarchy by removing information
about the migration from the destination hierarchies database.

For more information, see Planning to complete migration.

Typical workflow
To set up a workflow for migration:

   1. Specify a supported source hierarchy.

   2. Set up data gathering. Data gathering enables Configuration Manager to collect
     information about data that can migrate from the source hierarchy.

<!-- p.780 -->

     Configuration Manager automatically repeats the process to collect data on a
     simple schedule until you stop the data gathering process. By default, the data
     gathering process repeats every four hours so that Configuration Manager can
     identify changes to data in the source hierarchy. Data gathering is also necessary
     to share distribution points.

   3. Create migration jobs to migrate data between the source and destination
     hierarchy.

   4. You can stop the data gathering process at any time by using the Stop Gathering
     Data action. When you stop data gathering, Configuration Manager no longer
     identifies changes to data in the source hierarchy and can no longer share
     distribution points. Typically, you use this action when you no longer plan to
     migrate data or share distribution points from the source hierarchy.

   5. Optionally, after data gathering has stopped at all sites for the source hierarchy,
     you can clean up the migration data by using the Clean Up Migration Data action.
     This action deletes the historical data about migration from a source hierarchy
     from the database of the destination hierarchy.

After you migrate data, and you no longer need the source hierarchy to manage devices
in your environment, you can decommission that source hierarchy and infrastructure.

Scenarios
Configuration Manager supports the following migration scenarios:

     Migration from Configuration Manager 2007 hierarchies
     Migration from Configuration Manager 2012 or another Configuration Manager
     hierarchy

  ７ Note

  The expansion of a hierarchy that has a standalone site into a hierarchy that has a
  central administration site isn't categorized as a migration. For information about
  hierarchy expansion, see Expand a stand-alone primary site.

Migration from Configuration Manager 2007 hierarchies
When you use migration to migrate data from Configuration Manager 2007, you can
maintain your investment in your existing site infrastructure and gain the following

<!-- p.781 -->

benefits:

Site database improvements
The Configuration Manager (current branch) database supports full Unicode.

Database replication between sites
Replication in Configuration Manager (current branch) is based on Microsoft SQL Server.
This behavior improves the performance of site-to-site data transfer.

User-centric management

Users are the focus of management tasks in Configuration Manager (current branch).
For example, you can distribute software to a user even if you don't know the device
name for that user. Additionally, Configuration Manager gives users much more control
over what software is installed on their devices and when that software is installed.

Hierarchy simplification

Configuration Manager (current branch) lets you build a simpler site hierarchy. This
improvement is due to the introduction of the central administration site type and
changes to the behavior of primary and secondary sites. Configuration Manager (current
branch) uses less network bandwidth and requires fewer servers than previous versions.

Role-based administration

This central security model in Configuration Manager (current branch) offers hierarchy-
wide security and management that corresponds to your administrative and business
requirements.

  ７ Note

  Because of design changes that were first introduced in System Center 2012
  Configuration Manager, you can't upgrade Configuration Manager 2007 to
  Configuration Manager (current branch). In-place upgrade is supported from
  System Center 2012 Configuration Manager to Configuration Manager (current
  branch).

<!-- p.782 -->

Migration from Configuration Manager 2012 or another
Configuration Manager hierarchy
The process of migrating data from a System Center 2012 Configuration Manager or
Configuration Manager hierarchy is the same. This process includes migrating data from
multiple source hierarchies into a single destination hierarchy. You might use this
process when your company gets additional resources that are already managed by
Configuration Manager. Additionally, you can migrate data from a test environment to
your Configuration Manager production environment. This process lets you maintain
your investment in the Configuration Manager test environment.

See also
     Planning for migration to Configuration Manager

     Configuring source hierarchies and source sites for migration

     Operations for migration

     Security and privacy for migration

     Start using Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.783 -->

Plan for migration to Configuration
Manager current branch
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before you migrate data to a Configuration Manager current branch destination
hierarchy, make sure that you are familiar with sites and hierarchies in Configuration
Manager. For more about sites and hierarchies, see Fundamentals of Configuration
Manager.

Install a Configuration Manager current branch hierarchy to be the destination hierarchy
before you migrate data from a supported source hierarchy.

After you install the destination hierarchy, set up the management features and
functions that you want to use in your destination hierarchy before you start to migrate
data.

Additionally, you might have to plan for overlap between the source hierarchy and your
destination hierarchy. For example, you might set up the source hierarchy to use the
same network locations or boundaries as your destination hierarchy, and you then install
new clients to your destination hierarchy and use automatic site assignment. In this
scenario, because a newly installed Configuration Manager client can select a site to join
from either hierarchy, the client might incorrectly assign to your source hierarchy.
Therefore, plan to assign each new client in the destination hierarchy to a specific site in
that hierarchy instead of using automatic site assignment.

For more about site assignments, see Client site assignment considerations in
Interoperability between different versions of Configuration Manager.

Use the following articles to help you plan how to migrate a supported source hierarchy
to a Configuration Manager destination hierarchy:

        Prerequisites for migration

        Administrator checklists for migration planning

        Determine whether to migrate data to Configuration Manager current branch

        Plan a source hierarchy strategy

        Administrator checklists for migration planning

<!-- p.784 -->

     Plan a client migration strategy

     Plan a content deployment migration strategy

     Plan for the migration of Configuration Manager objects to Configuration Manager
     current branch

     Plan to monitor migration activity

     Plan to complete migration

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.785 -->

Prerequisites for migration in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To migrate from a supported source hierarchy, you must have access to each applicable
Configuration Manager source site, and permissions within the Configuration Manager
destination site to configure and run migration operations.

Use the information in the following sections to help you understand the versions of
Configuration Manager that are supported for migration, and the required
configurations.

      Versions of Configuration Manager that are supported for migration

      Source site languages that are supported for migration

      Required configurations for migration

Versions of Configuration Manager that are
supported for migration
You can migrate data from a source hierarchy that runs any of the following versions of
Configuration Manager:

      Configuration Manager 2007 SP2 (For the purpose of migration, Configuration
      Manager 2007 R2 or R3 on the source site are not a consideration. So long as the
      source site runs SP2, sites with either the R2 or R3 add-on installed are supported
      for migration to Configuration Manager current branch).

      System Center 2012 Configuration Manager SP2 or System Center 2012 R2
      Configuration Manager SP1.

         Tip

        In addition to migration, you can use an in-place upgrade of sites that run
        System Center 2012 Configuration Manager to Configuration Manager current
        branch.

<!-- p.786 -->

     A Configuration Manager hierarchy of the same or lesser version of Configuration
     Manager.

     For example, if you have a destination hierarchy that runs Configuration Manager
     current branch 1606, you could use migration to copy data from a source hierarchy
     that runs version 1606 or 1602. However you could not migrate data from a source
     hierarchy that runs 1610.

Source site languages that are supported for
migration
When you migrate data between Configuration Manager hierarchies, the data is stored
in the destination hierarchy in the language neutral format for Configuration Manager.
Because Configuration Manager 2007 does not store data in a language neutral format,
the migration process must convert objects to this format during migration from
Configuration Manager 2007. Therefore, only Configuration Manager 2007 source sites
that are installed with the following languages are supported for migration:

     English

     French

     German

     Japanese

     Korean

     Russian

     Simplified Chinese

     Traditional Chinese

When you migrate data from a System Center 2012 Configuration Manager or
Configuration Manager current branch hierarchy, there are no source site language
limitations. Objects in the source site database are already in a language neutral format.

Required configurations for migration
The following are required configurations for using migration and migration operations:

     To configure, run, and monitor migration in the Configuration Manager console:

<!-- p.787 -->

In the destination site, your account must be assigned the role-based
administration security role of Infrastructure Administrator. This security role
grants permissions to manage all migration operations, which includes the creation
of migration jobs, clean up, monitoring, and the action to share and upgrade
distribution points.

Data Gathering:

To enable the destination site to gather data, you must configure the following two
source site access accounts for use with each source site:

   Source Site Account: This account is used to access the SMS Provider of the
   source site.

      For a Configuration Manager 2007 SP2 source site, this account requires
      Read permission to all source site objects.

      For a System Center 2012 Configuration Manager or Configuration Manager
      current branch source site, this account requires Read permission to all
      source site objects, You grant this permission to the account by using role-
      based administration. For information about how to use role-based
      administration, see Fundamentals of role-based administration for
      Configuration Manager.

   Source Site Database Account: This account is used to access the SQL Server
   database of the source site and requires Connect, Execute, and Select
   permissions to the source site database.

You can configure these accounts when you configure a new source hierarchy, data
gathering for an additional source site, or when you reconfigure the credentials for
a source site. These accounts can use a domain user account, or you can specify
the computer account of the top-level site of the destination hierarchy.

  ） Important

  If you use the Configuration Manager computer account for either access
  account, ensure that this account is a member of the security group
  Distributed COM Users in the domain where the source site resides.

When gathering data, the following network protocols and ports are used:

   NetBIOS/SMB - 445 (TCP)

   RPC (WMI) - 135 (TCP & UDP)

<!-- p.788 -->

  Dynamic RPC. Dynamic ports use a range of port numbers that are defined by
  the OS version. These ports are also known as ephemeral ports. For more
  information about the default port ranges, see Service overview and network
  port requirements for Windows       .

  SQL Server - The TCP ports in use by both the source and destination site
  databases.

Migrate Software Updates:

Before you migrate software updates, you must configure the destination hierarchy
with a software update point. For more information, see Planning to migrate
software updates.

Share distribution points:

To successfully share any distribution points from a source site, at least one
primary site or the central administration site in the destination hierarchy must use
the same port numbers for client requests as the source site. For information about
client request ports, see How to configure client communication ports

For each source site, only the distribution points that are installed on site system
servers that are configured with a FQDN are shared.

In addition, to share a distribution point from a System Center 2012 Configuration
Manager or Configuration Manager current branch source site, the Source Site
Account (which accesses the SMS Provider for the source site server), must have
Modify permissions to the Site object on the source site. You grant this permission
to the account by using role-based administration. For information about how to
use role-based administration, see Fundamentals of role-based administration for
Configuration Manager.

Upgrade or reassign distribution points:

The Source Site Access Account configured to gather data from the SMS Provider
of the source site must have the following permissions:

  To upgrade a Configuration Manager 2007 distribution point, the account
  requires Read, Execute, and Delete permissions to the Site class on the
  Configuration Manager2007 site server to successfully remove the distribution
  point from the Configuration Manager2007 source site

  To reassign a System Center 2012 Configuration Manager or Configuration
  Manager current branch distribution point, the account must have Modify
  permission to the Site object on the source site. You grant this permission to the

<!-- p.789 -->

        account by using role-based administration. For information about how to use
        role-based administration, see Fundamentals of role-based administration for
        Configuration Manager.

        To successfully upgrade or reassign a distribution point to a new hierarchy, the
        ports that are configured for client requests at the site that manages the
        distribution point in the source hierarchy must match the ports that are
        configured for client requests at the destination site that will manage the
        distribution point. For information about client request ports, see How to
        configure client communication ports.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.790 -->

Administrator checklists for migration
planning in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the following administrator checklists to help you plan your migration strategy to
Configuration Manager current branch.

Administrator checklist for migration planning
Use the following checklist for pre-migration planning steps.

      Assess the current environment:

      Identify existing business requirements that are met by the source hierarchy and
      develop plans to continue to meet those requirements in the destination hierarchy.

      Review the functionality and changes that are available with the version of
      Configuration Manager that you use, and use this information to help you
      design your destination hierarchy:

      For more information, see Fundamentals of Configuration Manager and What's
      new.

      Determine the administrative security model to use for role-based
      administration:

      For more information, see Fundamentals of role-based administration for
      Configuration Manager.

      Assess your network and Active Directory topology: Review your existing domain
      structure and network topology and consider how this influences your hierarchy
      design and migration tasks.

      Finalize your destination hierarchy design:

      Decide upon the placement of a central administration site, primary sites,
      secondary sites, and content distribution options.

      Map your hierarchy to the computers that you will use for sites and site servers
      in the destination hierarchy:

<!-- p.791 -->

     Identify the computers that sites and site system servers will use in the destination
     hierarchy, and then ensure that they have sufficient capacity to meet existing and
     future operational requirements.

     Plan your object migration strategy:

     Plan to use the available migration jobs to migrate different objects, including site
     boundaries, collections, advertisements, and deployments. For more information,
     see Types of migration jobs in Planning a migration job strategy

     Configuration Manager migrates only the objects that you select. Any objects that
     are not migrated and that are required in the destination hierarchy must be re-
     created in the destination hierarchy.

     Objects that can migrate are displayed when you configure migration jobs.

     Plan your client migration strategy:

     Plan to migrate clients by using a controlled approach that limits the network
     bandwidth and server processing requirements when you migrate clients to the
     destination hierarchy. For more about planning a client migration strategy, see
     Planning a client migration strategy.

     Plan for inventory and compliance data:

     Configuration Manager does not support migrating hardware inventory, software
     inventory, or desired configuration management compliance data for software
     updates or clients.

     Instead, after the client migrates to its new site in the destination hierarchy and
     receives policy for these configurations, the client submits this information to its
     assigned site. This action populates the destination site database with current
     inventory and compliance data.

     Plan for the completion of migration from the source hierarchy:

     Decide when objects and clients will be migrated. After migration completes, you
     can plan to decommission the site servers in the source hierarchy.

Administrator checklist for hierarchy migration
Use the following checklist to help you plan a destination hierarchy before you start
migration.

     Identify the computers to use in the destination hierarchy:

<!-- p.792 -->

  Configuration Manager does not support an in-place upgrade from Configuration
  Manager 2007 infrastructure. Instead you use migration to move data from
  Configuration Manager 2007 to Configuration Manager current branch. This
  requires you to use a side-by-side deployment and install Configuration Manager
  on new computers.

  Similarly, when you migrate from another Configuration Manager hierarchy, you
  must install a new destination hierarchy that is a side-by-side deployment to your
  source hierarchy.

  Create your destination hierarchy:

  To prepare for migration, install and configure a Configuration Manager
  destination hierarchy that includes a primary site. For example:

    Install a central administration site and then install at least one child primary.

    Install a stand-alone primary if you do not plan to use a central administration
    site.

  If you want to migrate information that is related to software updates, configure
  a software update point in the destination hierarchy and synchronize software
  updates:

  You must configure and synchronize software updates in the destination hierarchy
  before you can migrate software updates information from the source hierarchy.

  Install and configure additional site system roles in the destination hierarchy:

  Configure additional site system roles and site systems that you require.

  Check operational functionality in the destination hierarchy:

  Check the following:

    If the destination hierarchy includes multiple sites, confirm that database
    replication is working between sites. Database replication is not applicable to
    stand-alone primary sites.

    Check that all installed site system roles are operational.

    Check that the Configuration Manager clients you install to the destination
    hierarchy can communicate successfully with their assigned site.

Administrator checklist for migration

<!-- p.793 -->

Use the following checklist to migrate data from the source hierarchy to the destination
hierarchy.

     Enable migration in the destination hierarchy:

     Configure a source hierarchy by specifying the top-level site of the source
     hierarchy. For more about specifying the source site, see Planning a source
     hierarchy strategy.

     When the source hierarchy runs Configuration Manager 2007 SP2, select and
     configure additional sites in the source hierarchy:

     For each additional site in the Configuration Manager 2007 SP2 source hierarchy
     that you want to collect data from, you must configure credentials for data
     gathering. When you configure each source site, the data-gathering process
     begins immediately and continues throughout the migration period until you stop
     data gathering for that site. Data gathering ensures that you can migrate objects
     from the source hierarchy that are updated or added after a previous data-
     gathering process.

        ７ Note

        When the source hierarchy runs System Center 2012 Configuration Manager
        or later, you do not need to configure additional source sites.

     Configure distribution point sharing:

     You can share distribution points between the two hierarchies to make content for
     objects that you migrate available to clients in the destination hierarchy. This
     ensures that the same content remains available for clients in both hierarchies and
     that you can maintain this content until you stop gathering data and finish the
     migration.

     For information about shared distribution points, see Share distribution points
     between source and destination hierarchies in Planning a content deployment
     migration strategy.

     Create and run migration jobs to migrate objects associated with the clients in
     the source hierarchy:

     Create migration jobs to migrate objects between hierarchies. The required
     configurations for each migration job can vary depending on what data the job
     migrates.

<!-- p.794 -->

For example, when you migrate content, regardless of the migration job you use,
you must assign a site in the destination hierarchy to own management of that
content. The assigned site will access the original source file location for the
content and is responsible for distributing that content to distribution points in the
destination hierarchy.

For more information, see Create and edit migration jobs for Configuration
Manager in Operations for migrating to Configuration Manager current branch.

Migrate clients to the destination hierarchy:

The process of migrating clients depends on your migration scenario:

   When you migrate clients that have a client version that is not the same as the
   destination hierarchy, you must upgrade the client software. Upgrade requires
   the removal of the current Configuration Manager client, followed by the
   installation of the new client version that matches the destination site.

   When you migrate clients that have a client version that matches the version of
   the destination hierarchy, the client does not upgrade or reinstall. Instead, the
   client reassigns to a primary site in the destination hierarchy.

When you migrate a client to the destination hierarchy, the client is associated with
its data that you previously migrated to that destination hierarchy.

For more information, see Planning a client migration strategy.

Upgrade or reassign shared distribution points:

When you no longer have to support clients in your source hierarchy, you can
upgrade shared distribution points from a Configuration Manager 2007 source
site, or reassign shared distribution points from a System Center 2012
Configuration Manager or Configuration Manager current branch source site.
When you upgrade or reassign a distribution point, the site system role transfers to
a primary site in the destination hierarchy and the distribution point is removed
from the source site in the source hierarchy. When you upgrade or reassign a
shared distribution point, the content remains on the distribution point computer
and you do not have to redeploy the content to new distribution points in the
destination hierarchy.

You can also upgrade a distribution point that is co-located on a Configuration
Manager 2007 secondary site server. This removes the secondary site and results in
only a distribution point in the destination hierarchy.

<!-- p.795 -->

     For information about shared distribution points, see Share distribution points
     between source and destination hierarchies in Planning a content deployment
     migration strategy.

     Finish migration:

     After you have migrated data and clients from all sites in the source hierarchy and
     you have upgraded applicable distribution points, you can finish migration. To
     finish migration you stop gathering data for each source site in the source
     hierarchy. You can then remove migration information that you do not need and
     decommission your source hierarchy infrastructure. For more information, see
     Planning to complete migration.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.796 -->

Determine whether to migrate data to
Configuration Manager current branch
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

In Configuration Manager current branch, migration provides a process for transferring
data and configurations that you've created from supported versions of Configuration
Manager to your new hierarchy. You can use this to:

      Combine multiple hierarchies into one.

      Move data and configurations from a lab deployment into your production
      deployment.

      Move data and configuration from a prior version of Configuration Manager, like
      Configuration Manager 2007, which has no upgrade path to Configuration
      Manager current branch, or from System Center 2012 Configuration Manager
      (which does support an upgrade path to Configuration Manager current branch).

With the exception of the distribution point site system role and the computers that
host distribution points, no infrastructure (which includes sites, site system roles, or
computers that host a site system role), migrates, transfers, or can be shared between
hierarchies.

Although you cannot migrate server infrastructure, you can migrate Configuration
Manager clients between hierarchies. Client migration involves migrating the data that
clients use from the source hierarchy to the destination hierarchy, and then installing or
reassigning the client software so that the client then reports to the new hierarchy.

After you install a client to the new hierarchy and the client submits its data, its unique
Configuration Manager ID helps Configuration Manager associate the data that you
previously migrated with each client computer.

The functionality that's provided by migration helps you maintain investments that you
have made in configurations and deployments while letting you take full advantage of
core changes in the product first (which was first introduced in System Center 2012
Configuration Manager and then continued in Configuration Manager). These changes
include a simplified Configuration Manager hierarchy that uses fewer sites and
resources, and the improved processing that comes from using native 64-bit code that
runs on 64-bit hardware.

<!-- p.797 -->

For information about the versions of Configuration Manager that migration supports,
see Prerequisites for migration.

Data that you can migrate to Configuration
Manager current branch
Migration can migrate most objects between supported Configuration Manager
hierarchies. The migrated instances of some objects from a supported version of
Configuration Manager 2007 must be modified to conform to the System Center 2012
Configuration Manager schema and object format.

These modifications don't affect the data in the source site database. Objects that are
migrated from a supported version of System Center 2012 Configuration Manager or
Configuration Manager current branch don't require modification.

The following are objects that can migrate based on the version of Configuration
Manager in the source hierarchy. Some objects, like queries, do not migrate. If you want
to continue to use these objects that do not migrate you must recreate them in the new
hierarchy. Other objects, including some client data, are automatically recreated in the
new hierarchy when you manage clients in that hierarchy.

Objects that you can migrate from System Center 2012
Configuration Manager or Configuration Manager
current branch
     Applications for System Center 2012 Configuration Manager and later versions

     App-V Virtual Environment from System Center 2012 Configuration Manager and
     later versions

     Asset Intelligence customizations

     Boundaries

     Collections: To migrate collections from a supported version of System Center 2012
     Configuration Manager or Configuration Manager current branch, you use an
     object migration job.

     Compliance settings:

        Configuration baselines

        Configuration items

<!-- p.798 -->

   Deployments

   Operating system deployment:

      Boot images

      Driver packages

      Drivers

      Images

      Packages

      Task sequences

   Search results: Saved search criteria

   Software updates:

      Deployments

      Deployment packages

      Templates

      Software update lists

   Software distribution packages

   Software metering rules

   Virtual application packages

Objects that you can migrate from Configuration
Manager 2007 SP2
   Advertisements

   Applications for System Center 2012 Configuration Manager and later versions

   App-V Virtual Environment from System Center 2012 Configuration Manager and
   later versions

   Asset Intelligence customizations

   Boundaries

<!-- p.799 -->

     Collections: You migrate collections from a supported version of Configuration
     Manager 2007 by using a collection migration job.

     Compliance settings (referred to as desired configuration management in
     Configuration Manager 2007):

        Configuration baselines

        Configuration items

     Operating system deployment:

        Boot images

        Driver packages

        Drivers

        Images

        Packages

        Task sequences

     Search results: Search folders

     Software updates:

        Deployments

        Deployment packages

        Templates

        Software update lists

     Software distribution packages

     Software metering rules

     Virtual application packages

Data that you can't migrate to Configuration
Manager current branch
You cannot migrate the following types of objects:

<!-- p.800 -->

     AMT client provisioning information

     Files on clients, including:

        Client inventory and history data

        Files in the client cache

     Queries

     Configuration Manager 2007 security rights and instances for the site and objects

     Configuration Manager 2007 reports from SQL Server Reporting Services

     Configuration Manager 2007 web reports

     System Center 2012 Configuration Manager and Configuration Manager current
     branch reports

     System Center 2012 Configuration Manager and Configuration Manager current
     branch role-based administration:

        Security roles

        Security scopes

Feedback
Was this page helpful?      Yes     No

Provide product feedback
