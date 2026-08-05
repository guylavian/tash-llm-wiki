---
title: "Core infrastructure documentation — pages 1601-1640"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1601-1640
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1601-1640
family: sccm
documentKind: "doc"
abstract: "Upgrade to Windows Server 2016, 2019, 2022, or 2025 Use the steps in this section for any of the upgrade scenarios listed above. ） Important Upgrade software update points (SUPs) from the top-level site downward. Older WSUS versions can synchronize from newer WSUS versions, but"
---

# Core infrastructure documentation — pages 1601-1640

<!-- p.1601 -->

Upgrade to Windows Server 2016, 2019, 2022, or 2025
Use the steps in this section for any of the upgrade scenarios listed above.

  ） Important

  Upgrade software update points (SUPs) from the top-level site downward. Older WSUS
  versions can synchronize from newer WSUS versions, but newer WSUS versions can't
  synchronize from older WSUS versions. If you have multiple SUPs in the same site, use this
  order:

     1. If the site server doesn't host a SUP, upgrade the site server only after you upgrade all
        other SUPs in the hierarchy.
     2. If the site server hosts a SUP, upgrade all SUPs as quickly as possible. Synchronization
        fails for any SUP in the site that isn't running the same version as the SUP on the site
        server.

Before upgrade

     (Windows Server 2012 or Windows Server 2012 R2 only): Remove the System Center
     Endpoint Protection (SCEP) client. Windows Server now has Windows Defender built in,
     which replaces the SCEP client. The presence of the SCEP client can prevent an upgrade to
     Windows Server.

     (Windows Server 2012 or Windows Server 2012 R2 only): Install the latest Cumulative Update
     and uninstall Windows Management Framework 5.1 before attempting the upgrade.

     Remove the WSUS role from the server if it's installed. You may keep the SUSDB and
     reattach it once WSUS is reinstalled. This includes removing and reinstalling the WSUS
     Administrative Tools on the CAS or Primary Site Server if the Software Update Point (SUP) is
     remote.

     If you're upgrading the OS of the site server, make sure file-based replication is healthy for
     the site. Check all inboxes for a backlog on both sending and receiving sites. If there are lots
     of stuck or pending replication jobs, wait until they clear out.
        On the sending site, review sender.log.
        On the receiving site, review despooler log.

After upgrade

<!-- p.1602 -->

     Make sure Windows Defender is enabled, set for automatic start, and running.

     Make sure the following Configuration Manager services are running:
        SMS_EXECUTIVE
        SMS_SITE_COMPONENT_MANAGER

     Make sure the Windows Process Activation and WWW/W3svc services are enabled and set
     for automatic start. The upgrade process disables these services, so make sure they're
     running for the following site system roles:
        Site server
        Management point

     Make sure each server that hosts a site system role continues to meet all prerequisites. For
     example, you might need to reinstall BITS, WSUS, or configure specific settings for IIS.

     After restoring any missing prerequisites, restart the server one more time to make sure
     services are started and operational.

     If you're upgrading the central administration site server or the primary site server, then run
     a site reset.

     If you're upgrading a secondary site server, then recover the secondary site.

     If the WSUS server is remote from the Site Server, the Windows Server Update Services
     Tools must be removed and reinstalled.

        Remove the Windows Server Update Services Tools

          Windows Command Prompt

          Uninstall-WindowsFeature -Name       UpdateServices-RSAT

        Install the Windows Server Update Services Tools

          Windows Command Prompt

          Install-WindowsFeature -Name       UpdateServices-RSAT

Known issue for remote Configuration Manager consoles

After you upgrade the site server, or an instance of the SMS Provider, you can't connect with the
Configuration Manager console. To work around this problem, manually restore permissions for

<!-- p.1603 -->

the SMS Admins group in WMI. Permissions must be set on the site server, and on each remote
server that hosts an instance of the SMS Provider:

   1. On the applicable servers, open the Microsoft Management Console (MMC) and add the
     snap-in for WMI Control, and then select Local computer.

   2. In the MMC, open the Properties of WMI Control (Local) and select the Security tab.

   3. Expand the tree below Root, select the SMS node, and then choose Security. Make sure the
     SMS Admins group has the following permissions:

           Enable Account

           Remote Enable

   4. On the Security tab below the SMS node, select the site_<sitecode> node, and then
     choose Security. Make sure the SMS Admins group has the following permissions:

           Execute Methods

           Provider Write

           Enable Account

           Remote Enable

   5. Save the permissions to restore access for the Configuration Manager console.

Known issue for remote site systems

After completing the After Upgrade section above, if you upgraded a central administration site,
primary site, secondary site, or distribution point there may be data missing from the following
registry location:

Key: HKLM\SYSTEM\CurrentControlSet\Control\SecurePipeServers\Winreg\AllowedPaths

Value: Machine

     For a central administration site, primary site, or secondary site the data in the REG_Multi_SZ
     'Machine' registry value should include: Software\Microsoft\SMS

     For a distribution point, the data in the REG_Multi_SZ 'Machine' registry value should
     include: Software\Microsoft\SMS\DP

<!-- p.1604 -->

If the data is missing from the value after you upgrade Windows on the server, manually add the
one(s) that correspond to the role(s) installed on the system. Otherwise site system roles can have
issues uploading files to the site server inboxes. Distribution Points may have issues with Content
Distribution, Distribution Point Configuration, or general functionality.

Upgrade the OS of clients
Configuration Manager supports an in-place upgrade of the OS for Configuration Manager
clients in the following situations:

     If Configuration Manager supports the resulting service pack level, it supports in-place
     upgrade to a later Windows service pack.

     In-place upgrade of Windows from a supported version to Windows 10 or later. For more
     information, see Upgrade Windows to the latest version.

     Build-to-build servicing upgrades of Windows 10 or later. For more information, see
     Manage Windows as a service.

Upgrade SQL Server
Configuration Manager supports an in-place upgrade of SQL Server on the site database server.

For information about the versions of SQL Server that Configuration Manager supports, see
Support for SQL Server versions.

Upgrade the service pack version of SQL Server
If Configuration Manager still supports the resulting SQL Server service pack level, it supports the
in-place upgrade of SQL Server to a later service pack.

When you have more than one Configuration Manager site in a hierarchy, each site can run a
different service pack version of SQL Server. There's no limitation to the order in which sites
upgrade the service pack version of SQL Server.

  ） Important

  If you use BitLocker management in Configuration Manager, and you encrypt recovery data
  in the database, before you upgrade SQL Server, make sure the certificate is for a supported
  version. For example, certificates created with SQL Server 2014 or earlier aren't compatible

<!-- p.1605 -->

  with SQL Server 2016 or later. For more information, see Manage the encryption certificate
  on SQL Server upgrade.

Upgrade to a new version of SQL Server
Configuration Manager supports the in-place upgrade of SQL Server to the following versions:

     SQL Server 2022
     SQL Server 2019
     SQL Server 2017
     SQL Server 2016
     SQL Server 2014

This support includes the upgrade of SQL Server Express to a newer version of SQL Server Express
at secondary sites.

When you upgrade the version of SQL Server that hosts the site database, you must upgrade the
SQL Server version that's used at sites in the following order:

   1. Upgrade SQL Server at the central administration site first

   2. Upgrade secondary sites before you upgrade a secondary site's parent primary site

   3. Upgrade parent primary sites last. These sites include both child primary sites that report to
     a central administration site, and stand-alone primary sites that are the top-level site of a
     hierarchy.

When you upgrade a site database from an earlier version of SQL Server, the database keeps its
existing cardinality estimation level, if it's at the minimum allowed for that instance of SQL Server.
If you upgrade SQL Server with a database at a compatibility level lower than the allowed level, it
automatically sets the database to the lowest compatibility level allowed by SQL Server. For more
information, see Supported SQL Server versions: Database compatibility level.

For more information about upgrading SQL Server, see the following SQL Server articles:

     Upgrade to SQL Server 2022

     Upgrade to SQL Server 2019

     Upgrade to SQL Server 2017

     Upgrade to SQL Server 2016

<!-- p.1606 -->

To upgrade SQL Server on the site database server
  1. Stop all Configuration Manager services at the site

  2. Upgrade SQL Server to a supported version

  3. Restart the Configuration Manager services

 ７ Note

 When you change the SQL Server edition in use at the central administration site from
 Standard to either a Datacenter or Enterprise, the database partition doesn't change. This
 database partition limits the number of clients the hierarchy supports.

Last updated on 05/27/2026

<!-- p.1607 -->

Updates and servicing for Configuration
Manager
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

Configuration Manager uses an in-console service method called Updates and
Servicing. This in-console method makes it easy to find and install recommended
updates for your Configuration Manager infrastructure. In-console servicing is
supplemented by out-of-band updates such as hotfixes. The out-of-band updates are
intended for customers who need to resolve issues that might be specific to their
environment.

   Tip

  The terms upgrade, update, and install are used to describe three separate concepts
  in Configuration Manager. For more information about how each term is used, see
  About upgrade, update, and install.

Baseline and update versions
Use the latest baseline version when you install a new site in a new hierarchy.

      After upgrading to Configuration Manager current branch, don't use baseline
      versions to stay current. Instead, only use in-console updates to update to the
      newest version.

      Periodically, another baseline version is released. When you use the latest baseline
      version to install a new hierarchy, you avoid installing an outdated or unsupported
      version of Configuration Manager, followed by another update to your
      infrastructure.

After you install a baseline version, later versions of Configuration Manager are available
as in-console updates. Use these updates to update your infrastructure to the latest
version of Configuration Manager.

      You install in-console updates to update the version of your top-level site.

      Updates you install at the central administration site (CAS) automatically install at
      child primary sites. Control this timing by using a service window at the primary

<!-- p.1608 -->

     site. For more information, see Service Windows.

     Manually update secondary sites to a new update version from within the console.

When you install an update, the update stores installation files for that version on the
site server in a folder named CD.Latest. For more information about these files, see The
CD.Latest folder.

     Use the files in the CD. Latest folder during site recovery. Also, when your hierarchy
     no longer runs a baseline version, use these files to install other sites.

     You can't use installation files from CD. Latest to install the first site of a new
     hierarchy.

Version details
Some updates for Configuration Manager are available as both an in-console update
version for existing infrastructure, and as a new baseline version.

Supported versions

The following supported versions * , of Configuration Manager are currently available as
a baseline, an update, or both:

                                                                               ﾉ   Expand table

 Version       Availability date     Support end date       Baseline     In-console update

 2409          December 4, 2024      June 4, 2026           No           Yes
 (5.00.9132)

 2403          April 22, 2024        October 22, 2025       YesNote 1    Yes
 (5.00.9128)

 2309          October 9, 2023       April 9, 2025          No           Yes
 (5.00.9122)

  ７ Note

  The Availability date in this table is when the early update ring was released.
  Baseline media will be available on the VLSC soon after the update is globally
  available.

<!-- p.1609 -->

Note 1: How to get baseline media

The baseline media is available as part of the following releases on the Volume License
Service Center    (VLSC):

      Microsoft Configmgr (current branch)

      System Center Datacenter
      System Center Standard

For example, search the VLSC for Microsoft Configmgr (current branch) . Find the
baseline media in the list of files, and download for that release.

  ７ Note

  The search string may be different on other media sites. For example, on the Visual
  Studio Subscriptions Portal     , search for Microsoft Configuration Manager .

  ７ Note

  * Supported Versions in Configuration Manager: In the context of Configuration

  Manager, the term supported encompasses both engineering and assisted technical
  support. While no further engineering development will occur for the versions in
  question, users will not have access to phone or online assisted technical support
  for these versions. However, Technical Support will assist with upgrading to a
  supported version of Configuration Manager. Users will resume their regular
  assisted technical support once Configuration Manager is upgraded to a supported
  version."

Historical versions

The following table lists historical versions of Configuration Manager current branch that
are out of support:

                                                                           ﾉ     Expand table

 Version               Availability date   Support end date     Baseline   In-console
                                                                           update

 2303                  April 10, 2023      October 10, 2024     Yes        Yes
 (5.00.9106)

<!-- p.1610 -->

Version       Availability date   Support end date    Baseline   In-console
                                                                 update

2211          December 5, 2022    June 5, 2024        No         Yes
(5.00.9096)

2207          August 12, 2022     February 12, 2024   No         Yes
(5.00.9088)

2203          April 6, 2022       October 6, 2023     Yes        Yes
(5.00.9078)

2111          December 1, 2021    June 1, 2023        No         Yes
(5.00.9068)

2107          August 2, 2021      February 2, 2023    No         Yes
(5.00.9058)

2103          April 19, 2021      October 19, 2022    Yes        Yes
(5.00.9049)

2010          November 30,        May 30, 2022        No         Yes
(5.00.9040)   2020

2006          August 11, 2020     February 11, 2022   No         Yes
(5.00.9012)

2002          April 1, 2020       October 1, 2021     Yes        Yes
(5.00.8968)

1910          November 29,        May 29, 2021        No         Yes
(5.00.8913)   2019

1906          July 26, 2019       January 26, 2021    No         Yes
(5.00.8853)

1902          March 27, 2019      September 27,       Yes        Yes
(5.00.8790)                       2020

1810          November 27,        December 1, 2020    No         Yes
(5.00.8740)   2018

1806          July 31, 2018       January 31, 2020    No         Yes
(5.00.8692)

1802          March 22, 2018      September 22,       Yes        Yes
(5.00.8634)                       2019

1710          November 20,        May 20, 2019        No         Yes
(5.00.8577)   2017

<!-- p.1611 -->

 Version              Availability date   Support end date    Baseline   In-console
                                                                         update

 1706                 July 31, 2017       July 31, 2018       No         Yes
 (5.00.8540)

 1702                 March 27, 2017      March 27, 2018      Yes        Yes
 (5.00.8498)

 1610                 November 18,        November 18,        No         Yes
 (5.00.8458)          2016                2017

 1606 with            October 12, 2016    October 12, 2017    Yes        No
 KB3186654
 (5.00.8412.1307)

 1606                 July 22, 2016       July 22, 2017       No         Yes
 (5.00.8412.1000)

 1602                 March 11, 2016      March 11, 2017      No         Yes
 (5.00.8355)

 1511                 December 8, 2015    December 8, 2016    Yes        No
 (5.00.8325)

How to check the version
To check the version of your Configuration Manager site, in the console go to About
Configuration Manager at the top-left corner of the console. This dialog displays the
site and console versions.

  ７ Note

  The console version is slightly different from the site version. The minor version of
  the console corresponds to the Configuration Manager release version. For
  example, in Configuration Manager version 2303 the initial site version is
  5.0.9122.1000, and the initial console version is 5.9122.1082.1700. The build (1082)
  and revision (1700) numbers may change with future hotfixes.

In-console updates and servicing
When you use a production-ready installation of Configuration Manager current branch,
most updates are available using the Updates and Servicing channel. This method
identifies, downloads, and makes available the updates that apply to your current

<!-- p.1612 -->

infrastructure version and configuration. It includes only updates that Microsoft
recommends for all customers.

These updates include:

     New versions, like version 2303, 2309, or 2403.

     Updates that include new features for your current version.

     Hotfixes for your version of Configuration Manager and that all customers should
     install.

        ７ Note

        In-console hotfixes have supersedence relationships. For more information,
        see Supersedence for in-console hotfixes.

The in-console updates deliver increased stability and resolve common issues. They
replace the update types seen for previous product versions such as service packs,
cumulative updates, hotfixes that are applicable to all customers, and the extension for
Microsoft Intune.

The in-console updates can apply to one or more of the following systems:

     Primary and CAS servers

     Site system roles and site system servers

     Instances of the SMS Provider

     Configuration Manager consoles

     Configuration Manager clients

Configuration Manager discovers new updates for you. Synchronize your Configuration
Manager service connection point with the Microsoft cloud service, noting the following
behaviors:

     When your service connection point is in online mode, your site synchronizes with
     Microsoft every day. It automatically identifies new updates that apply to your
     infrastructure. To download updates and redistributable files, the computer that
     hosts the service connection point site system role uses the System context to
     access the following internet locations: go.microsoft.com and
     download.microsoft.com . For more information about other locations used by the

     service connection point, see Internet access requirements.

<!-- p.1613 -->

     When your service connection point is in offline mode, use the service connection
     tool to manually sync with the Microsoft cloud. For more information, see Use the
     service connection tool.

     In-console updates replace the need to independently locate and install individual
     updates, service packs, and new features.

     Install only the in-console updates you choose. When installing some updates, you
     can select individual features to enable and use. For more information, see Enable
     optional features from updates.

When you install an in-console update, the following process occurs:

     It automatically runs a prerequisite check. You can also manually run this check
     before starting the installation.

     It installs at the top-level site in your environment. This site is the CAS if there's
     one. In a hierarchy, the update automatically installs at primary sites. Control when
     each primary site server is allowed to update by using Service windows for site
     servers.

     After a site server updates, all affected site system roles automatically update.
     These roles include instances of the SMS Provider. After the site installs the update,
     Configuration Manager consoles also prompt the console user to update the
     console.

     If an update includes the Configuration Manager client, you're offered the option
     to test the update in pre-production, or to apply the update to all clients
     immediately.

     After a primary site is updated, secondary sites don't automatically update. Instead,
     you must manually start the secondary site update.

  ７ Note

  The Configuration Manager current branch, the long-term servicing branch, and the
  technical preview branch are different releases. Updates that apply for one branch
  aren't available as in-console updates for the other branches. For more information
  about available branches, see Which branch of Configuration Manager should I
  use?.

Supersedence for in-console hotfixes

<!-- p.1614 -->

In-console hotfixes have supersedence relationships. When Microsoft publishes a new
Configuration Manager hotfix, the console doesn't display any hotfixes that are
superseded by this new hotfix. This new behavior helps you better determine which
hotfixes to install.

Supersedence example
There are three hotfixes available: Hotfix-A, Hotfix-B, and Hotfix-C. Hotfix-A is
superseded by Hotfix-B, and Hotfix-B is superseded by Hotfix-C.

                                                                                 ﾉ   Expand table

 Hotfix-A              Hotfix-B        Hotfix-C        In-console view

 Not installed         Not installed   Not installed   Show all three hotfixes

 Installed             Installed       Not installed   Hotfix-B shows as installed
                                                       Hotfix-C shows as ready to install

 Not installed         Not installed   Installed       Hotfix-C shows as installed

Out-of-band hotfixes
Some hotfixes release with limited availability to address specific issues. Other hotfixes
are applicable to all customers but can't install using the in-console method. These fixes
are delivered out-of-band and not discovered from the Microsoft cloud service.

Typically, when you're seeking to fix or address a problem with your deployment of
Configuration Manager, you can learn about out-of-band hotfixes from Microsoft
customer support services, a Microsoft support knowledge base article, or the
Configuration Manager team blog          .

Install these fixes manually, using one of the following two methods:

Update Registration Tool
This tool manually imports the hotfix into your Configuration Manager console. Then
install the update as you would in-console updates that are discovered automatically.

This method is used for hotfixes that use the following file name structure: <Product>-
<product version>-<KB article ID>-ConfigMgr.Update.exe

For more information, see Use the update registration tool to import hotfixes.

<!-- p.1615 -->

Hotfix Installer
Use this tool to manually install a hotfix that can't be installed using the in-console
method.

This method is used for fixes that use the following file name structure: <Product>-
<product version>-<KB article ID>-<platform>-<language>.exe

For more information, see Use the hotfix installer to install updates.

Next steps
The following articles can help you understand how to find and install the different
update types for Configuration Manager:

     Install in-console updates

     Use the service connection tool

     Use the update registration tool to import hotfixes

     Use the hotfix installer to install updates

For more information about the technical preview branch, see Technical preview.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1616 -->

Prepare to install in-console updates for
Configuration Manager
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

Configuration Manager synchronizes with the Microsoft cloud service to get updates.
Use the steps in this article to prepare your environment.

Get available updates
The site only downloads updates that apply to your infrastructure and version. This
synchronization can be automatic or manual, depending on how you configure the
service connection point for your hierarchy:

      In online mode, the service connection point automatically connects to the
      Microsoft cloud service and downloads applicable updates.

      By default, Configuration Manager checks for new updates every 24 hours.
      Manually check for updates in the Configuration Manager console. Go to the
      Administration workspace, select the Updates and Servicing node, and choose
      Check for Updates in the ribbon.

      In offline mode, the service connection point doesn't connect to the Microsoft
      cloud service. To download and then import available updates, use the Service
      Connection Tool.

  ７ Note

  If necessary, import out-of-band fixes into your console. To do so, use the update
  registration tool. These out-of-band fixes supplement the updates you get when
  you synchronize with the Microsoft cloud service.

After updates synchronize, view them in the Configuration Manager console. Go to the
Administration workspace and select the Updates and Servicing node.

      Updates you haven't installed display as Available.

      Updates you've installed display as Installed. Only the most recently installed
      update is shown. To view previously installed updates, select History in the ribbon.

<!-- p.1617 -->

Before you configure the service connection point, understand and plan for its use. The
following uses might affect how you configure this site system role:

     The site uses the service connection point to upload usage information about your
     site. This information helps the Microsoft cloud service identify the updates that
     are available for the current version of your infrastructure. For more information,
     see Diagnostics and usage data.

To better understand what happens when updates are downloaded, see the following
flowcharts:

     Flowchart - Download updates

     Flowchart - Update replication

Permissions
To view updates in the console, a user must have a role-based administration security
role that includes the security class Update packages. This class grants access to view
and manage updates in the Configuration Manager console.

About the Update packages class
By default, the Update packages class (SMS_CM_Updatepackages) is part of the
following built-in security roles with the listed permissions:

     Full Administrator with Modify and Read permissions:

        A user with this security role and access to the All security scope can view and
        install updates. The user can also enable features during the installation, and
        enable individual features after the site updates.

        A user with this security role and access to the Default security scope can view
        and install updates. The user can also enable features during the installation,
        and view features after the site updates. But this user can't enable the features
        after the site updates.

     Read-only Analyst with Read permissions:
        A user with this security role and access to the Default scope can view updates
        but not install them. This user can also view features after the site updates, but
        can't enable them.

Permissions required for updates and servicing

<!-- p.1618 -->

     Use an account to which you assign a security role that includes the Update
     packages class with both Modify and Read permissions.

     Assign the account to the Default scope.

Permissions to only view updates
     Use an account to which you assign a security role that includes the Update
     packages class with only the Read permission.

     Assign the account to the Default scope.

Permissions required to enable features after the site
updates
     Use an account to which you assign a security role that includes the Update
     packages class with both Modify and Read permissions.

     Assign the account to the All scope.

Before you install an in-console update
Review the following steps before you install an update from within the Configuration
Manager console.

Step 1: Review the update checklist
Review the applicable update checklist for actions to take before you start the update:

     Checklist for installing update 2409

     Checklist for installing update 2403

     Checklist for installing update 2309

     Checklist for installing update 2303

Step 2: Run the prerequisite checker before installing an
update
Before you install an update, run the prerequisite checks for that update. If you run the
checks before installing an update:

<!-- p.1619 -->

     The site replicates update files to other sites before installing the update.

     When you choose to install the update, the prerequisite check automatically runs
     again.

  ７ Note

  When you start a prerequisite check and then view the status, the Installation
  phase appears to be active. However, the site isn't actually installing the update. To
  run the prerequisite check, the update process extracts the package from the
  content library. It then puts the package into a staging folder where it can access
  the current prerequisite checks. When you install an update, this same process runs.
  This behavior is why the Installation phase shows as In progress. Only the Extract
  Update package step is shown in the Installation category.

Later, when you install the update, you can configure the update to ignore prerequisite
check warnings.

Process to run the prerequisite checker before installing an update
   1. In the Configuration Manager console, go to the Administration workspace, and
     select the Updates and Servicing node.

   2. Select the update package for which you want to run the prerequisite check.

   3. Select Run prerequisite check in the ribbon.

     When you run the prerequisite check, content for the update replicates to child
     sites. View the distmgr.log on the site server to confirm that content replicates
     successfully.

   4. To view the results of the prerequisite check:

      a. In the Configuration Manager console, go to the Monitoring workspace.

     b. Select the Updates and Servicing Status node and look for the prerequisite
        status.

      c. For more information, see the ConfigMgrPrereq.log on the site server.

Next steps
Now that you've prepared the environment, you're ready to install the updates.

<!-- p.1620 -->

  Install in-console updates

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1621 -->

Install in-console updates for
Configuration Manager
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

This article describes how to install updates from within the Configuration Manager
console. Before you start, make sure to Prepare to install in-console updates.

When you're ready to install updates from within the Configuration Manager console,
begin with the top-level site of your hierarchy. This site is either the central
administration site (CAS) or a standalone primary site.

Install the update outside of normal business hours for each site to minimize the effect
on business operations. The update installation might include actions like reinstalling
site components and site system roles.

      Child primary sites automatically start the update after the CAS completes
      installation of the update. This process is by default and recommended. To control
      when a primary site installs updates, use Service windows for site servers.

      After the primary parent site update is complete, manually update secondary sites
      from within the Configuration Manager console. Automatic update of secondary
      site servers isn't supported.

      When you use a Configuration Manager console after the site is updated, you're
      prompted to update the console.

      After the site server successfully completes installation of an update, it
      automatically updates all applicable site system roles. However, all distribution
      points don't reinstall and go offline to update at the same time. Instead, the site
      server uses the site's content distribution settings to distribute the update to a
      subset of distribution points at a time. The result is that only some distribution
      points go offline to install the update. Distribution points that haven't begun to
      update or that have completed the update remain online and able to provide
      content to clients.

Start the install
At the top-level site of your hierarchy, in the Configuration Manager console, go to the
Administration workspace, and select the Updates and Servicing node. Select an

<!-- p.1622 -->

update with the state of Available, and then choose Install Update Pack in the ribbon.

  ７ Note

  Your user account requires permissions to install updates. For more information,
  see Permissions for in-console updates.

Start the update installation at a secondary site
After the parent primary site updates, update the secondary site from within the
Configuration Manager console.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node. Select the secondary site
     you want to update, and then choose Upgrade in the ribbon.

   2. Select Yes to start the update of the secondary site.

To monitor the update installation on a secondary site, select the secondary site, and
choose Show Install Status in the ribbon. Also add the Version column to the Sites node
so that you can view the version of each secondary site.

The status in the console may not refresh or it might show that the update failed. After a
secondary site successfully updates, use the Retry installation option. This option
doesn't reinstall the update for a secondary site that successfully installed the update,
but forces the console to update the status.

Install process

1. When the update installation starts
You're presented with the Updates Wizard that displays a list of the product areas that
the update applies to.

     On the General page of the wizard, configure Prerequisite warnings as necessary:

        Prerequisite errors always stop the update installation. Fix errors before you can
        successfully retry the update installation. For more information, see Retry
        installation of a failed update.

        Prerequisite warnings can also stop the update installation. Fix warnings before
        you retry the update installation. For more information, see Retry installation of

<!-- p.1623 -->

        a failed update.

        Ignore any prerequisite check warnings and install this update regardless of
        missing requirements: Set a condition for the update installation to ignore
        prerequisite warnings. This option allows the update installation to continue. If
        you don't select this option, the update installation stops on a warning. Unless
        you've previously run the prerequisite check and fixed prerequisite warnings for
        a site, don't use this option.

        In both the Administration and Monitoring workspaces, the Updates and
        Servicing node includes a button on the ribbon named Ignore prerequisite
        warnings. This button becomes available when an update package fails to
        complete installation because of prerequisite check warnings. For example, you
        install an update without using the option to ignore prerequisite warnings (from
        within the Updates Wizard). The update installation stops with a state of
        prerequisite warning but no errors. Later, you select Ignore prerequisite
        warnings in the ribbon. This action triggers an automatic continuation of that
        update installation, which ignores prerequisite warnings. When you use this
        option, the update installation automatically continues after a few minutes.

     When an update applies to the Configuration Manager client, choose to test the
     client update with a limited set of clients. For more information, see How to test
     client upgrades in a pre-production collection.

     Starting in Configuration Manager 2107, sites that aren't already onboarded to
     Microsoft Endpoint Manager will be prompted to optionally cloud attach as part of
     the upgrade wizard. Environments are considered cloud attached if at least one of
     the following features are already enabled:
        Tenant attach
        Co-management
        Endpoint analytics

     If you don't wish to onboard, clear both of the Enable Microsoft Intune admin
     center and Enable automatic client enrollment for co-management options.

2. During the update installation
As part of the update installation, Configuration Manager does the following actions:

     Reinstalls any affected components, like site system roles or the Configuration
     Manager console.

<!-- p.1624 -->

     Manages updates to clients based on the selections that you made for client
     piloting, and for automatic client upgrades.

     Site system servers generally don't need to restart as part of the update. If a role
     uses .NET, and the package updates that prerequisite component, then the site
     system may restart. For more information, see Site and site system prerequisites.

   Tip

  When you install Configuration Manager updates, the site also updates the
  CD.Latest folder. For more information, see The CD.Latest folder.

3. Monitor the progress of updates as they install
Use the following steps to monitor progress:

     In the Configuration Manager console, go to the Administration workspace, and
     select the Updates and Servicing node. This node shows the installation status for
     all update packages.

     In the Configuration Manager console, go to the Monitoring workspace, and select
     the Updates and Servicing Status node. This node shows the installation status of
     only the current update package that the site is installing.

     The update installation is divided into several phases for easier monitoring. For
     each of the following phases, more details in the installation status include which
     log file to view for more information:

        Download: This phase applies only to the top-level site with the service
        connection point.

        Replication

        Prerequisites Check

        Installation

        Post Installation: For more information, see post installation tasks.

     View the CMUpdate.log file in <ConfigMgr_Installation_Directory>\Logs on the
     site server.

  ７ Note

<!-- p.1625 -->

  During the Installation phase, you can see the state of the Upgrade ConfigMgr
  database task.

        If the database upgrade is blocked, then you'll be given the warning In
        progress, needs attention.
           The cmupdate.log will log the program name and sessionid from SQL
           Server that is blocking the database upgrade.
        When the database upgrade is no longer blocked, the status will be reset to In
        progress or Complete.
           When the database upgrade is blocked, a check is done every 5 minutes to
           see if it's still blocked.

4. When the update installation completes
After the first site update completes installation:

     Child primary sites install the update automatically. No further action is required.

     Manually update secondary sites from within the Configuration Manager console.
     For more information, see start the update installation at a secondary site.

     Until all sites in your hierarchy update to the new version, your hierarchy operates
     in a mixed version mode. For more information, see Interoperability between
     different versions.

5. Update Configuration Manager consoles
After a CAS or primary site updates, each Configuration Manager console that connects
to the site must also update. You're prompted to update a console:

     When you open the console

     When you go to a new node in an open console

Update the console right away after the site updates.

After the console update completes, verify the console and site versions are correct. Go
to About Configuration Manager at the top-left corner of the console.

  ７ Note

<!-- p.1626 -->

   The console version is slightly different from the site version. The minor version of
   the console corresponds to the Configuration Manager release version. For
   example, in Configuration Manager version 2303 the initial site version is
   5.0.9122.1000, and the initial console version is 5.9122.1082.1700. The build (1082)
   and revision (1700) numbers may change with future hotfixes.

Next steps
Continue reading about what happens after the site updates, or what to do if the update
fails.

  After the site updates

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1627 -->

After the site updates
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

After you install an in-console update for Configuration Manager, the site does
additional processing in the background. There are also additional steps that you may
need to take after the update is complete. If something goes wrong, use the steps
below to help troubleshoot and retry the update.

Post-installation tasks
When a site installs an update, there are several tasks that can't start until after the
update completes installation on the site server. This list includes the post-installation
tasks that are critical for site and hierarchy operations. Because they're critical, they're
actively monitored. Other tasks that aren't directly monitored include the reinstallation
of site system roles. To view the status of the critical post-installation tasks, select the
Post Installation task while monitoring the update installation for a site.

Not all tasks complete immediately. Some tasks don't start until each site completes
installation of the update. New functionality you might expect can be delayed until
these tasks complete. Turning on new features doesn't start until all sites complete
update installation, so new features might not be visible for some time.

The post installation tasks include:

      Installing SMS_EXECUTIVE service
         Critical service that runs on the site server.
         Reinstallation of this service should complete quickly.

      Installing SMS_DATABASE_NOTIFICATION_MONITOR component
         Critical site component thread of SMS_EXECUTIVE service.
         Reinstallation of this service should complete quickly.

      Installing SMS_HIERARCHY_MANAGER component

         Critical site component that runs on the site server.

         Responsible for reinstalling roles on site system servers. Status for individual site
         system role reinstallation doesn't display.

         Reinstallation of this service should complete quickly.

<!-- p.1628 -->

          ７ Note

          Some Configuration Manager site roles share the client framework. For
          example, the management point and pull distribution point. When these
          roles update, the client version on these servers updates at the same time.
          For more information, see How to upgrade clients.

     Installing SMS_REPLICATION_CONFIGURATION_MONITOR component
        Critical site component that runs on the site server.
        Reinstallation of this service should complete quickly.

     Installing SMS_POLICY_PROVIDER component
        Critical site component that runs only on primary sites.
        Reinstallation of this service should complete quickly.

     Monitoring replication initialization
        This task only displays at the CAS and child primary sites.
        Dependent on the SMS_REPLICATION_CONFIGURATION_MONITOR.
        Should complete quickly.

     Updating Configuration Manager Client Preproduction Package
        This task displays even when client preproduction (also called client piloting)
        isn't enabled for use.
        Doesn't start until all sites in the hierarchy finish installing the update.

     Updating Client folder on Site Server
        This task doesn't display if you use the client in preproduction.
        Should complete quickly.

     Updating Configuration Manager Client Package
        This task doesn't display if you use the client in preproduction.
        Finishes only after all sites install the update.

     Turning on Features
        This task displays only at the top-tier site of the hierarchy.
        Doesn't start until all sites in the hierarchy finish installing the update.
        Individual features aren't displayed.

Retry installation of a failed update
When an update fails to install, review the in-console feedback to identify resolutions for
warnings and errors. For more details, view the ConfigMgrPrereq.log on the site server.

<!-- p.1629 -->

Before you retry the installation of an update, you must fix errors, and should fix
warnings.

   Tip

  If an update has problems downloading or replicating, use the update reset tool.

When you're ready to retry the installation of an update, select the failed update, and
then choose an applicable option. The update installation retry behavior depends on the
node where you start the retry, and the retry option that you use.

Retry installation for the hierarchy
Retry the installation of an update for the entire hierarchy when that update is in one of
the following states:

     Prerequisite checks passed with one or more warnings, and the option to ignore
     prerequisite check warnings wasn't set in the Update Wizard. (The update's value
     for Ignore Prereq Warning in the Updates and Servicing node is No.)

     Prerequisite failed

     Installation failed

     Replication of the content to the site failed

Go to the Administration workspace and select the Updates and Servicing node. Select
the update, and then choose one of the following options:

     Retry: When you Retry from Updates and Servicing, the update install starts again
     and automatically ignores prerequisite warnings. If content replication previously
     failed, content for the update replicates again.

     Ignore prerequisite warnings: If the update install stops because of a warning, you
     can then choose Ignore prerequisite warnings. This action allows the installation
     of the update to continue after a few minutes, and uses the option to ignore
     prerequisite warnings.

Retry installation for the site
Retry the installation of an update at a specific site when that update is in one of the
following states:

<!-- p.1630 -->

     Prerequisite checks passed with one or more warnings, and the option to ignore
     prerequisite check warnings wasn't set in the Update Wizard. (The updates value
     for Ignore Prereq Warning in the Updates and Servicing node is No.)

     Prerequisite failed

     Installation failed

Go to the Monitoring workspace, and select the Site Servicing Status node. Select the
update, and then choose one of the following options:

     Retry: When you Retry from Site Servicing Status, you restart the installation of
     the update at only that site. Unlike running Retry from the Updates and Servicing
     node, this retry doesn't ignore prerequisite warnings.

     Ignore prerequisite warnings: If the update install stops because of a warning, you
     can then select Ignore prerequisite warnings. This action allows the installation of
     the update to continue after a few minutes, and uses the option to ignore
     prerequisite warnings.

Report setup and upgrade failures to Microsoft
Starting in Configuration Manager version 2010, if the setup or update process fails to
complete successfully, you can report the error directly to Microsoft. If a failure occurs,
the Report update error to Microsoft button is enabled. When you use the button, an
interactive wizard opens allowing you to provide more information to us. When running
setup from the media rather than the console, you'll also be given the Report update
error to Microsoft option if setup fails.

  ） Important

  For business-impacting issues, contact Microsoft support        to open a new support
  request. Reporting setup and upgrade failures from the console is for providing
  product feedback on setup errors you may have encountered. Reporting an error
  doesn't generate a support request.

To report upgrade failures to Microsoft:

   1. In the Configuration Manager console, go to Administration > Overview >
     Updates and Servicing.

   2. Select an update then select Report update error to Microsoft in the ribbon.

<!-- p.1631 -->

                                                                                       

   3. Before you submit the feedback, you'll be given options to:

            Attach other files

            Provide your email address if you're willing to be contacted about the error.

   4. When you submit feedback, you'll be given a transaction ID for the feedback. A
      status message is also generated with this information.

            Message ID 53900 is a successful submission.

            Message ID 53901 is a failed submission.

After a site installs an update
After the site updates, review the post-update checklist for the applicable version:

      Post-update checklist for version 2409

      Post-update checklist for version 2403

      Post-update checklist for version 2309

      Post-update checklist for version 2303

Next steps
Some updates include optional features, which you can enable during or after
installation.

  Optional features

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1632 -->

Optional features in Configuration
Manager
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

When an update includes one or more optional features, you can enable those features
in your hierarchy. Enable features when the update installs, or return to the console later
to enable the optional features.

To view available features and their status, in the console go to the Administration
workspace, expand Updates and Servicing, and select the Features node. To enable a
feature, select it in the list, and then select Turn on in the ribbon.

Your user account requires permissions to view and enable optional features. For more
information, see Permissions for in-console updates.

When a feature isn't optional, it's automatically available for use. It doesn't appear in the
Features node.

  ） Important

  In a multi-site hierarchy, enable optional or pre-release features only from the
  central administration site (CAS). This behavior makes sure there are no conflicts
  across the hierarchy.

When you enable a new feature or pre-release feature, the Configuration Manager
hierarchy manager (HMAN) must process the change before that feature becomes
available. Processing of the change is often immediate. Depending on the HMAN
processing cycle, it can take up to 30 minutes to complete. After the change is
processed, restart the console before you can use the feature.

When new cloud-based features are available in the Microsoft Intune admin center, or
other attached cloud services for your on-premises Configuration Manager installation,
you can opt in to these new features in the Configuration Manager console.

List of optional features
The following features are optional in the latest version of Configuration Manager:

      Remove the central administration site

<!-- p.1633 -->

     BitLocker management
     Application groups

   Tip

  For more information on features that require consent to enable, see pre-release
  features.

  For more information on features that are only available in the technical preview
  branch, see Technical Preview.

Next steps
The current branch includes pre-release features for early testing in a production
environment. For more information, see pre-release features.

For answers to common questions, see In-console updates FAQ.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1634 -->

In-console updates FAQ

Why don't I see certain updates in my console?
If you can't find a specific update in your console after a successful sync with the Microsoft cloud
service, this behavior might be because of one of the following reasons:

      The update requires a configuration that your infrastructure doesn't use, or your current
      product version doesn't fulfill a prerequisite for receiving the update.

      If you think you have the required configurations and prerequisites for a missing update,
      confirm the service connection point is in online mode. Then, use the Check for Updates
      option in the Updates and Servicing node to force a check. If your service connection point
      is in offline mode, use the service connection tool to manually sync with the cloud service.

      Your account lacks the correct role-based administration permissions to view updates in the
      Configuration Manager console. For more information, see Permissions to manage updates.

Why did the current branch name change with
version 2103?
To better align with other releases within Microsoft Endpoint Manager, starting in the year 2021
the current branch version names will be 2103, 2107, and 2111. They will still release every four
months, and release at the same time of the year.

 Last updated on 01/29/2026

<!-- p.1635 -->

Update reset tool
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Beginning with version 1706, Configuration Manager primary sites, and central
administration sites include the Configuration Manager Update Reset Tool,
CMUpdateReset.exe. Use the tool to fix issues when in-console updates have problems
downloading or replicating. The tool is found in the \cd.latest\SMSSETUP\TOOLS folder
of the site server.

You can use this tool with any version of the current branch that remains in support.

Use this tool when an in-console update has not yet installed and is in a failed state. A
failed state means that the update download is in progress but stuck or taking an
excessively long time. A long time is considered to be hours longer than your historical
expectations for update packages of similar size. It can also be a failure to replicate the
update to child primary sites.

When you run the tool, it runs against the update that you specify. By default, the tool
does not delete successfully installed or downloaded updates.

Prerequisites
The account you use to run the tool requires the following permissions:

      Read and Write permissions to the site database of the central administration site
      and to each primary site in your hierarchy. To set these permissions, you can add
      the user account as a member of the db_datawriter and db_datareader fixed
      database roles on the Configuration Manager database of each site. The tool does
      not interact with secondary sites.
      Local Administrator on the top-level site of your hierarchy.
      Local Administrator on the computer that hosts the service connection point.

You need the GUID of the update package that you want to reset. To get the GUID:

   1. In the console, go to Administration > Updates and Servicing.
   2. In the display pane, right-click the heading of one of the columns (like State), then
      select Package Guid to add that column to the display.
   3. The column now shows the update package GUID.

   Tip

<!-- p.1636 -->

  To copy the GUID, select the row for the update package you want to reset, and
  then use CTRL+C to copy that row. If you paste your copied selection into a text
  editor, you can then copy only the GUID for use as a command-line parameter
  when you run the tool.

Run the tool
The tool must be run on the top-level site of the hierarchy.

When you run the tool, use command-line parameters to specify:

     The SQL Server at the top-tier site of the hierarchy.
     The site database name at the top-tier site.
     The GUID of the update package you want to reset.

Based on the status of the update, the tool identifies the additional servers it needs to
access.

If the update package is in a post download state, the tool does not clean up the
package. As an option, you can force the removal of a successfully downloaded update
by using the force delete parameter (See command-line parameters later in this topic).

After the tool runs:

     If a package was deleted, restart the SMS_Executive service at the top-tier site.
     Then, check for updates so you can download the package again.
     If a package was not deleted, you do not need to take any action. The update
     reinitializes and then restarts replication or installation.

Command-line parameters:

                                                                                 ﾉ     Expand table

 Parameter                         Description

 -S <FQDN of the SQL Server of     Required
 your top-tier site>               Specify the FQDN of the SQL Server that hosts the site
                                   database for the top-tier site of your hierarchy.

 -D <Database name>                Required
                                   Specify the name of the database at the top-tier site.

 -P <Package GUID>                 Required
                                   Specify the GUID for the update package you want to reset.

<!-- p.1637 -->

 Parameter                         Description

 -I <SQL Server instance name>     Optional
                                   Identify the instance of SQL Server that hosts the site
                                   database.

 -FDELETE                          Optional
                                   Force deletion of a successfully downloaded update package.

Examples:
In a typical scenario, you want to reset an update that has download problems. Your SQL
Servers FQDN is server1.fabrikam.com, the site database is CM_XYZ, and the package
GUID is 61F16B3C-F1F6-4F9F-8647-2A524B0C802C. You run: CMUpdateReset.exe -S
server1.fabrikam.com -D CM_XYZ -P 61F16B3C-F1F6-4F9F-8647-2A524B0C802C

In a more extreme scenario, you want to force deletion of problematic update package.
Your SQL Servers FQDN is server1.fabrikam.com, the site database is CM_XYZ, and the
package GUID is 61F16B3C-F1F6-4F9F-8647-2A524B0C802C. You run:
CMUpdateReset.exe -FDELETE -S server1.fabrikam.com -D CM_XYZ -P 61F16B3C-F1F6-
4F9F-8647-2A524B0C802C

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1638 -->

Test the database upgrade when
installing an update
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If necessary, you can run a test database upgrade before you install an in-console
update for the current branch of Configuration Manager.

  ） Important

  The test upgrade is no longer a required or recommend step for most sites.

  If your database is suspect, or is modified by customizations not explicitly
  supported by Configuration Manager, continue to use this process.

Do I need to run a test upgrade?
The deprecation of this upgrade test is made possible because of changes that are
introduced with Configuration Manager current branch. These changes simplify the
process and speed by which setup can update a production environment to a newer
version. This redesign was done to help you stay current with less risk, and less
operational overhead when installing each new update.

The changes are to how updates install, including logic that automatically rolls back a
failed update without the need to run a site recovery. These changes enable the use of
the console to manage update installations, and include an option to retry installation of
a failed update.

   Tip

  When you upgrade to Configuration Manager current branch from an older
  product, like System Center 2012 Configuration Manager, test database upgrades
  remain a recommended step.

If you still plan to test the upgrade of a site database when you install an in-console
update, the following information supplements the guidance on installing an in-console
update.

<!-- p.1639 -->

Prepare to run a test database upgrade
To run the upgrade test, use the Configuration Manager Setup from the CD.Latest
folder. Use the same version of the source files as the version of Configuration Manager
to which you're updating.

For example, to test the database update for version YYMM:

     You need at least one site on version YYMM from which you can get that CD.Latest
     folder.

     If you don't have a site that runs the required version, consider installing a site in a
     lab environment. Then update that site to the new version. This process creates the
     CD.Latest folder with the correct version of source files.

The upgrade test runs against a backup of your site database that you restore to a
separate instance of SQL Server. After the test upgrade completes, discard the upgraded
database. It can't be used by a Configuration Manager site.

Run the test upgrade
   1. Use Configuration Manager Setup and the source files from the CD.Latest folder of
     a site that runs the version that you plan to update to.

   2. Copy the CD.Latest folder to a location on the SQL Server instance that you'll use
     to run the test database upgrade.

   3. Create a backup of the site database that you want to test upgrade. Then restore a
     copy of that database to an instance of SQL Server that doesn't host a
     Configuration Manager site. The SQL Server instance needs to be the same edition
     of SQL Server as your site database. For more information, see Quickstart: Backup
     and restore a SQL Server database on-premises.

   4. After you restore the database copy, run Setup from the CD.Latest folder. When
     you run Setup, use the /TESTDBUPGRADE command-line option. If the SQL Server
     instance that hosts the database copy isn't the default instance, provide the
     command-line options to identify the instance that hosts the site database copy.

     For example, you have a site database with the database name CM_ABC . You restore
     a copy of this site database to a supported instance of SQL Server with the
     instance name DBTest . To test an upgrade of this copy of the site database, use the
     following command line: setup.exe /TESTDBUPGRADE DBtest\CM_ABC

<!-- p.1640 -->

     You can find Setup.exe in the following location on the source media for
     Configuration Manager: SMSSETUP\BIN\X64

   5. On the instance of SQL Server where you run the upgrade test, monitor the
     ConfigMgrSetup.log in the root of the system drive for progress and success.

     If the test upgrade fails, fix any issues related to the site database upgrade failure.
     Then, create a new backup of the site database and retest the upgrade of the new
     copy of the database.

Next steps
After the test database update completes successfully, discard the updated database. It
can't be used by a Configuration Manager site. You can then return to your active site
and begin the update installation.

If an update install fails, you shouldn't need to recover the site. Instead, you can retry
the update installation from within the console.

Feedback
Was this page helpful?      Yes    No

Provide product feedback
