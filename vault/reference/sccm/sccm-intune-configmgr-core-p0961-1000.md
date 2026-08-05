---
title: "Core infrastructure documentation — pages 961-1000"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0961-1000
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0961-1000
family: sccm
documentKind: "doc"
abstract: "ﾉ Expand table Key name Required Comment ProductID Yes SiteCode Yes Use the same site code that it used before the failure. SiteName No SMSInstallDir Yes SDKServer Yes Use the same server that hosted this role before the failure. PrerequisiteComp Yes PrerequisitePath Yes AdminCo"
---

# Core infrastructure documentation — pages 961-1000

<!-- p.961 -->

                                                                                   ﾉ   Expand table

 Key name             Required      Comment

 ProductID            Yes

 SiteCode             Yes           Use the same site code that it used before the failure.

 SiteName             No

 SMSInstallDir        Yes

 SDKServer            Yes           Use the same server that hosted this role before the failure.

 PrerequisiteComp     Yes

 PrerequisitePath     Yes

 AdminConsole         Yes*          * Only required when ServerRecoveryOptions is 1 or 2 .

 JoinCEIP             Yes

SQLConfigOptions section for site recovery

Many of the keys in the SQLConfigOptions section are also required for site recovery. For
more information, see SQLConfigOptions section for site install. The following table
summarizes the keys in the SQLConfigOptions section for site recovery:

                                                                                   ﾉ   Expand table

 Key name           Required     Comment

 SQLServerName      Yes          Use the same server that hosted the site database before the
                                 failure.

 DatabaseName       Yes          Use the same database name that was used before the failure.

 SQLSSBPort         Yes          Use the same port that was used before the failure.

 SQLDataFilePath    No

 SQLLogFilePath     No

CloudConnectorOptions section for site recovery

Many of the keys in the CloudConnectorOptions section are also required for site
recovery. For more information, see CloudConnectorOptions section for site install. The

<!-- p.962 -->

following table summarizes the keys in the CloudConnectorOptions section for site
recovery:

                                                                                  ﾉ     Expand table

 Key name                   Required         Comment

 CloudConnector             Yes

 CloudConnectorServer       Yes*             * Only required when CloudConnector equals 1 .

 UseProxy                   Yes*             * Only required when CloudConnector equals 1 .

 ProxyName                  Yes*             * Only required when UseProxy equals 1 .

 ProxyPort                  Yes*             * Only required when UseProxy equals 1 .

HierarchyExpansionOption section for site recovery

Many of the keys in the HierarchyExpansionOption section are also required for site
recovery. For more information, see HierarchyExpansionOption section for site install.
The following table summarizes the keys in the HierarchyExpansionOption section for
site recovery:

                                                                                  ﾉ     Expand table

 Key name            Required      Comment

 CCARSiteServer      Yes*          * Only required if the primary site was attached to a CAS before
                                   the failure.

 CASRetryInterval    No

 WaitForCASTimeout   No

Examples

Example script to install a primary site
  ini

  [Identification]
  Action=InstallPrimarySite
  CDLatest=1

<!-- p.963 -->

  [Options]
  ProductID=Eval
  SiteCode=XYZ
  SiteName=Contoso eval site
  SMSInstallDir=D:\Program Files\Microsoft Configuration Manager
  SDKServer=cmsite.contoso.com
  PrerequisiteComp=0
  PrerequisitePath=C:\Sources\Redist
  AdminConsole=1
  JoinCEIP=0
  ManagementPoint=cmsite.contoso.com
  ManagementPointProtocol=HTTP
  DistributionPoint=cmsite.contoso.com
  DistributionPointProtocol=HTTP
  DistributionPointInstallIIS=1
  RoleCommunicationProtocol=HTTPorHTTPS
  ClientsUsePKICertificate=0
  MobileDeviceLanguage=0

  [SQLConfigOptions]
  SQLServerName=cmsql.contoso.com
  SQLServerPort=1433
  DatabaseName=CM_XYZ
  SQLSSBPort=4022
  SQLDataFilePath=E:\Program Files\Microsoft SQL
  Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\
  SQLLogFilePath=E:\Program Files\Microsoft SQL
  Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\

  [CloudConnectorOptions]
  CloudConnector=1
  CloudConnectorServer=cmsite.contoso.com
  UseProxy=0

  [SABranchOptions]
  SAActive=1
  CurrentBranch=1

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.964 -->

Install the Configuration Manager
console
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

Administrators use the Configuration Manager console to manage the Configuration
Manager environment. Each Configuration Manager console can connect to a central
administration site (CAS) or to a primary site. You can't connect a Configuration
Manager console to a secondary site.

The Configuration Manager console is always installed on the site server for the CAS or
a primary site. To install the console separate from site server installation, run the
standalone installer.

Prerequisites
      Supported OS versions for Configuration Manager consoles

      You have local Administrator rights on the target computer for the console.

      You have Read permissions to the location of the console installation files.

.NET version requirements
Starting in version 2403, the console requires Microsoft .NET Framework version 4.8. If
you install the console on other devices, make sure to update .NET. If the device doesn't
already have it, the console setup doesn't install this prerequisite.

Starting in version 2107, the console requires Microsoft .NET Framework version 4.6.2,
but version 4.8 is recommended. If you install the console on other devices, make sure
to update .NET. If the device doesn't already have it, the console setup doesn't install
this prerequisite.

Starting in version 2103, the ConfigurationManager PowerShell module requires
Microsoft .NET version 4.7.2 or later.

  ７ Note

  .NET Framework version 4.6.2 is preinstalled with Windows Server 2016 and
  Windows 10 version 1607. Later versions of Windows are preinstalled with a later

<!-- p.965 -->

  version of the .NET Framework.

  .NET Framework version 4.8 isn't supported on some OS versions, such as Windows
  10 2015 LTSB.

  For more information, see .NET Framework system requirements.

Source paths
Decide which source path to use:

     ConsoleSetup folder in the installation path on the site server:
     \Tools\ConsoleSetup

     When you install a site server, it copies the console installation files and supported
     language packs for the site to the Tools\ConsoleSetup subfolder. Optionally, you
     can copy the ConsoleSetup folder to an alternate location to start the installation.
     When you update the site, it always keeps its local version up to date.

     Configuration Manager installation media: \SMSSETUP\BIN\I386

     Installing the Configuration Manager console from the installation media always
     installs the English version. This behavior happens even if the site server supports
     different languages, or the target computer's OS is set to a different language.

When possible, start the console installer from the ConsoleSetup folder rather than
from the source media.

  ） Important

  Don't install the console using the CD.Latest source files. It's an unsupported
  scenario, and may cause problems with the console installation. For more
  information, see The CD.Latest folder.

If you create a package for installing the console on other computers, make sure the
package includes the following files:

     ConsoleSetup.exe
     AdminConsole.msi
     ConfigMgr.AC_Extension.i386.cab
     ConfigMgr.AC_Extension.amd64.cab

<!-- p.966 -->

Use the Setup Wizard
  1. Browse to the source path, and open ConsoleSetup.exe.

       ） Important

       Always install the console by using ConsoleSetup.exe. Although you can
       install the Configuration Manager console by running AdminConsole.msi, this
       method doesn't run prerequisites or dependency checks. The installation
       might not install correctly.

  2. In the wizard, select Next.

  3. On the Site Server page, enter the fully qualified domain name (FQDN) of the site
     server to which the Configuration Manager console connects.

  4. On the Installation Folder page, enter the installation folder for the Configuration
     Manager console. The folder path can't include trailing spaces or Unicode
     characters.

  5. On the Ready to Install page, select Install.

Install from a command prompt

   Tip

  Installing the Configuration Manager console from a command prompt always
  installs the English version. This behavior happens even if the target computer's OS
  is set to a different language. To install the Configuration Manager console in a
  language other than English, use the Setup Wizard.

ConsoleSetup.exe command-line options

/q

Installs the Configuration Manager console unattended. The TargetDir and
DefaultSiteServerName options are required when you use this option.

/uninstall

<!-- p.967 -->

Uninstalls the Configuration Manager console. Specify this option first when you use it
with the /q option.

LangPackDir

Specifies the path to the folder that contains the language files. You can use Setup
Downloader to download the language files. If you don't use this option, Setup looks
for the language folder in the current folder. If the language folder isn't found, Setup
continues to install English only. For more information, see Setup Downloader.

TargetDir

Specifies the installation folder to install the Configuration Manager console. This option
is required when you use the /q option.

DefaultSiteServerName

Specifies the FQDN of the site server to which the console connects when it opens. This
option is required when you use the /q option.

Examples

Silent install
ConsoleSetup.exe /q "TargetDir=%ProgramFiles%\ConfigMgr Console"

DefaultSiteServerName=MyServer.Contoso.com

Silent install with language packs
ConsoleSetup.exe /q "TargetDir=C:\Program Files\ConfigMgr Console"

DefaultSiteServerName=MyServer.Contoso.com LangPackDir=C:\Downloads\ConfigMgr

Silent uninstall
ConsoleSetup.exe /uninstall /q

Postinstallation information

<!-- p.968 -->

The Configuration Manager console requires installation of the built-in WebView2
extension for certain features such as Community hub and dashboards. A notification to
install the extension is given to the console user when they open the console. For more
information see, the WebView2 console extension.

Next steps
An administrator sees objects in the console based on the permissions assigned to their
user account. For more information, see Fundamentals of role-based administration.

For more information on the fundamentals of navigating the Configuration Manager
console, see How to use the console.

If your environment uses a proxy server, this configuration may impact the functionality
of the console. For more information, see Proxy server support - Configuration Manager
console.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.969 -->

Upgrade an evaluation installation of
Configuration Manager to a full
installation
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If you installed Configuration Manager as an evaluation version, after 180 days the
Configuration Manager console becomes read-only. You then need to activate the
product from the Site Maintenance page in Setup. At any time before or after the 180-
day period, you can upgrade to a full installation.

  ７ Note

  When you connect a Configuration Manager console to an evaluation installation
  of Configuration Manager, the window title bar displays the number of days that
  remain until it expires. The number of days in the window title doesn't
  automatically refresh. It only updates when you make a new connection to a site.

You can upgrade the following sites that run an evaluation installation:

      Central administration site (CAS)
      Primary site

Configuration Manager doesn't consider secondary sites as evaluation installations. So
after you upgrade a primary parent site to a full installation, you don't need to modify a
secondary site.

Prerequisites
To upgrade an evaluation version to a licensed version, you need the following
requirements:

      A valid product license key to use during the upgrade.

      Administrator rights on the site server.

Process

<!-- p.970 -->

   1. On the site server, run .\BIN\X64\Setup.exe from the Configuration Manager
     installation folder. Use this copy of Setup because site maintenance options aren't
     available when you run Setup from source media.

   2. On the Before You Begin page, select Next.

   3. On the Getting Started page, select Perform site maintenance or reset the Site,
     and then select Next.

   4. On the Site Maintenance page, select Upgrade the evaluation edition to a
     licensed edition. Then enter a valid product key, and select Next.

   5. On the Microsoft Software License Terms page, read and accept the license terms,
     and then select Next.

   6. On the Configuration page, select Close to complete the wizard.

  ７ Note

  Until you reconnect the console to the site, the title bar might indicate that the site
  is still an evaluation version.

Next steps
Configure sites and hierarchies

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.971 -->

Upgrade to Configuration Manager
current branch
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in April 2022, this feature of Configuration Manager is deprecated. The
  baseline media for version 2203 is the last version of Configuration Manager
  current branch that will support upgrade from any version of System Center 2012
  Configuration Manager. Current branch version 2303 media will only support new
  installs of current branch.

Do an in-place upgrade to Configuration Manager current branch from a site and
hierarchy that runs System Center 2012 Configuration Manager. Before upgrading from
System Center 2012 Configuration Manager, you must prepare the sites. This
preparation requires you to remove specific configurations that can prevent a successful
upgrade. Then follow the upgrade sequence when more than a single site is involved.

   Tip

  When managing Configuration Manager site and hierarchy infrastructure, the terms
  upgrade, update, and install are used to describe three separate concepts. To learn
  how each term is used, see About upgrade, update, and install.

In-place upgrade paths
The following options are the currently supported in-place upgrade paths:

Upgrade to the latest current branch version
You can upgrade the following products to a fully licensed, baseline version of
Configuration Manager:

      System Center 2012 Configuration Manager with Service Pack 2
      System Center 2012 R2 Configuration Manager with Service Pack 1

<!-- p.972 -->

For more information, see Frequently asked questions for Configuration Manager
branches and licensing.

   Tip

  When you upgrade from a System Center 2012 Configuration Manager version to
  current branch, you might be able to streamline your upgrade process. For more
  information, see the following:

       Baseline and update versions
       The CD.Latest folder

If you previously installed Configuration Manager Evaluation version, you can use the
upgrade process to convert the site to the full version. For more information, see
Upgrade an evaluation installation of Configuration Manager to a full installation.

Unsupported paths
The following paths aren't supported:

     It's not supported to upgrade a technical preview branch to a fully licensed
     installation. A technical preview version can only upgrade to a later version of the
     technical preview.

     Migration from a technical preview to a fully licensed version isn't supported.

Upgrade checklists
The following checklists can help you plan a successful upgrade to Configuration
Manager.

Before you upgrade
Review these steps before you upgrade to Configuration Manager.

Review your System Center 2012 Configuration Manager
environment

Resolve issues as detailed in the following Microsoft Support article: Configuration
Manager clients reinstall every five hours because of a recurring retry task and may
cause an inadvertent client upgrade.

<!-- p.973 -->

Make sure your environment meets the supported configurations
     Review the server OS version in use to host site system roles:

        Some older operating systems supported by System Center 2012 Configuration
        Manager aren't supported by Configuration Manager current branch. Before the
        upgrade, remove site system roles on those OS versions. For more information,
        see Supported operating systems for site system servers.

        The prerequisite checker for Configuration Manager doesn't verify the
        prerequisites for site system roles on the site server or on remote site systems.
        For example, you need to manually verify that remote site systems have at least
        .NET version 4.6.2. For more information, see List of prerequisite checks for
        Configuration Manager.

     Review required prerequisites for each computer that hosts a site system role. For
     example, to deploy an OS, Configuration Manager uses the Windows Assessment
     and Deployment Kit (ADK). Before you run Setup, download and install the
     Windows ADK on the site server and on each computer that runs an instance of
     the SMS Provider.

For more information about supported platforms and prerequisite configurations, see
Supported configurations.

For more information about using the Windows ADK with Configuration Manager, see
Infrastructure requirements for OS deployment.

Review the site and hierarchy status and verify that there are no
unresolved issues

Before you upgrade a site, resolve all operational issues for the following components:

     Site server
     Site database server
     Site system roles on remote computers

A site upgrade can fail because of existing operational problems.

Install all applicable critical updates for operating systems on
computers that host the site, the site database server, and remote
site system roles

<!-- p.974 -->

Before you upgrade a site, install any critical software updates for each applicable site
system. If an update that you install requires a restart, restart the applicable computers
before you start the upgrade.

Uninstall the site system roles not supported by Configuration
Manager

The following site system roles are no longer used in Configuration Manager. Uninstall
them before you upgrade from System Center 2012 Configuration Manager:

     Out of Band Management point

     System Health Validator point

     Application catalog website point and web service point

Disable database replicas for management points at primary sites
Configuration Manager can't upgrade a primary site that has a database replica for
management points. Disable database replication before you:

     Create a backup of the site database to test the database upgrade

     Upgrade the production site to Configuration Manager current branch

For more information, see the following articles:

     System Center 2012 Configuration Manager: Configure database replicas for
     management points

     Configuration Manager, current branch: Database replicas for management points

Reconfigure software update points that use NLB
Configuration Manager can't upgrade a site that uses a Network Load Balancing (NLB)
cluster to host software update points.

If you use NLB clusters for software update points, use PowerShell to remove the NLB
cluster. (Beginning with System Center 2012 Configuration Manager SP1, there was no
option in the Configuration Manager console to configure an NLB cluster.)

Disable all site maintenance tasks at each site during its upgrade

<!-- p.975 -->

Before you upgrade to Configuration Manager, disable any site maintenance tasks that
might run during the time the upgrade process is active. This list includes but isn't
limited to the following tasks:

      Backup Site Server
      Delete Aged Client Operations
      Delete Aged Discovery Data

If a site database maintenance task runs during the upgrade process, the site upgrade
can fail.

Before you disable a task, record the schedule of the task so you can restore its
configuration after the site upgrade completes.

For more information about site maintenance tasks, see the following articles:

      System Center 2012 Configuration Manager: Planning for site operations

      Configuration Manager, current branch: Reference for maintenance tasks

Run setup prerequisite checker
Before you upgrade a site, run the Prerequisite Checker independently from setup to
validate that your site meets the prerequisites. Later, when you upgrade the site,
prerequisite checker runs again.

The independent prerequisite check evaluates the site for upgrade to both the current
branch and the long-term servicing branch (LTSB) of Configuration Manager. Because
some features aren't supported by the LTSB, you might see entries in the
ConfigMgrPrereq.log that are like the following examples:

      INFO: The site is a LTSB edition.

      Unsupported site system role 'Asset Intelligence synchronization point' for
      the LTSB edition; Error; Configuration Manager has detected that the 'Asset

      Intelligence synchronization point' is installed. Asset Intelligence is not
      supported on the LTSB edition. You must uninstall the Asset Intelligence

      synchronization point site system role before you can continue.

If you plan to upgrade to the current branch, errors for the LTSB edition can be safely
ignored. They only apply if you plan to upgrade to the LTSB.

Later, when you run Configuration Manager setup to do the upgrade, the prerequisite
check runs again. It evaluates your site based on the branch of Configuration Manager

<!-- p.976 -->

you choose to install (current branch, or LTSB). If you choose to upgrade to the current
branch, it doesn't run the check for features that aren't supported by the LTSB.

For more information, see the Prerequisite checker and List of prerequisite checks.

Download prerequisite files and redistributable files for
Configuration Manager

Use Setup Downloader to download prerequisite redistributable files, language packs,
and the latest product updates for Configuration Manager.

For information, see Setup Downloader.

Plan to manage server and client languages
When you upgrade a site, the site upgrade installs only the language pack versions you
select during the upgrade.

     Setup reviews the current language configuration of your site. It then identifies the
     language packs that are available in the folder where you store previously
     downloaded prerequisite files.

     You can affirm the selection of the current server and client language packs, or
     change the selections to add or remove support for languages.

     Only language packs that are available when you run Setup can be selected.

  ７ Note

  You can't use the language packs from System Center 2012 Configuration Manager
  to enable languages for a Configuration Manager current branch site.

For more information about language packs, see Language packs.

Review considerations for site upgrades

When you upgrade a site, some features and configurations reset to a default
configuration. To help you prepare for these and related changes, see Considerations for
upgrading.

<!-- p.977 -->

Create a backup of the site database at the central administration
site (CAS) and primary sites

Before you upgrade a site, back up the site database to make sure that you have a
successful backup to use for disaster recovery.

For more information, see Backup and recovery.

Back up a customized configuration.mof file
If you use a customized configuration.mof file to define data classes you use with
hardware inventory, create a backup of this file. After the upgrade, restore this file to
your site. For more information, see How to extend hardware inventory.

Test the database upgrade process on a copy of the most recent
site database backup
Before you upgrade a Configuration Manager CAS or primary site, test the site database
upgrade process on a copy of the site database.

     Test the site database upgrade process. When you upgrade a site, the site
     database might be modified.

     Although testing the database upgrade isn't required, it can identify problems for
     the upgrade before your production database is affected.

     A failed site database upgrade can render your site database inoperable and might
     require a site recovery to restore functionality.

     Although the site database is shared between sites in a hierarchy, plan to test the
     database at each applicable site before you upgrade that site.

     If you use database replicas for management points at a primary site, disable
     replication before you create the backup of the site database.

Configuration Manager doesn't support the backup of secondary sites, or the test
upgrade of a secondary site database.

It's not supported to run a test database upgrade on the production site database.
Doing so upgrades the site database and could render your site inoperable.

For more information, see Test the site database upgrade.

<!-- p.978 -->

Restart the site server and each computer that hosts a site system
role

Do this action to make sure there are no pending actions from a recent installation of
updates or from prerequisites.

Start the upgrade

Starting at the top-level site in the hierarchy, run Setup.exe from the Configuration
Manager source media.

After the top-level site upgrades, you can begin the upgrade of each child site.
Complete the upgrade of each site before you begin to upgrade the next site.

Until all sites in your hierarchy upgrade to Configuration Manager, your hierarchy
operates in a mixed version mode.

For information about how to run upgrade, see Upgrade sites.

After you upgrade
Review these steps after you upgrade to Configuration Manager.

Upgrade stand-alone Configuration Manager consoles

By default, when you upgrade a CAS or primary site, the installation also upgrades the
Configuration Manager console that's installed on the site server. Manually upgrade
each console that's installed on a computer other than the site server.

   Tip

  Close each open console before you start the upgrade.

For more information, see Install Configuration Manager consoles.

Reconfigure database replicas for management points at primary
sites
If you use database replicas for management points at primary sites, uninstall the
database replicas before you upgrade the site. After you upgrade a primary site,
reconfigure the database replica for management points.

<!-- p.979 -->

For more information, see Database replicas for management points.

Reconfigure any database maintenance tasks you disabled before
the upgrade

If you disabled database maintenance tasks at a site before the upgrade, reconfigure
those tasks at the site using the same settings that were in place before the upgrade.

Upgrade clients
After all your sites upgrade to Configuration Manager, plan to upgrade clients.

When you upgrade a client, the current client software is uninstalled and the new client
software version is installed. To upgrade clients, you can use any method that
Configuration Manager supports.

   Tip

  When you upgrade the top-level site of a hierarchy, the client installation package
  on each distribution point in the hierarchy is also updated. When you upgrade a
  primary site, the client upgrade package that's available from that primary site is
  updated.

For more information, see How to upgrade clients for Windows computers.

Considerations for upgrading

Automatic actions
When you upgrade to Configuration Manager, the following actions occur
automatically:

     A site reset. This action includes a reinstallation of all site system roles.

     If the site is the top-level site of a hierarchy, it updates the client installation
     package on each distribution point in the hierarchy. The site also updates the
     default boot images to use the new Windows PE version for the same version of
     the Windows ADK. However, the upgrade doesn't upgrade existing media for use
     with image deployment.

     If the site is a primary site, it updates the client upgrade package for that site.

<!-- p.980 -->

Manual actions after an upgrade
After you upgrade a site, make sure that you do the following actions:

     Make sure that clients assigned to each primary site upgrade and install the new
     client version.

     Upgrade each Configuration Manager console that connects to the site and that
     runs on a computer that's remote from the site server.

     At primary sites where you use database replicas for management points,
     reconfigure the database replicas.

     After the site upgrades, manually upgrade physical media like ISO files for CDs,
     DVDs, or USB flash drives. It also includes prestaged media provided to hardware
     vendors. The site upgrade updates the default boot images, it can't upgrade these
     media files or devices used external to Configuration Manager.

     Plan to update custom boot images when you don't require the older version of
     Windows PE.

Actions that affect configurations and settings
When a site upgrades to Configuration Manager, some configurations and settings
don't persist after the upgrade. Some configurations are set to a new default. The
following list includes some settings that don't persist or that change:

     Software Center: The following Software Center items are reset to their default
     values:

        Work information is reset to business hours from 5:00am to 10:00pm Monday
        to Friday.

        The value for Computer maintenance is set to Suspend Software Center
        activities when my computer is in presentation mode.

        The value for Remote control is set to the value in the client settings that are
        assigned to the computer.

     Software update summarization schedules: Custom summarization schedules for
     software updates or software update groups are reset to the default value of one
     hour. After the upgrade finishes, reset custom summarization values to the
     required frequency.

<!-- p.981 -->

Test the site database upgrade
This process only applies when you're upgrading a prior version like System Center 2012
Configuration Manager to Configuration Manager current branch.

Before you upgrade a site, test a copy of that site's database for the upgrade.

To test the database for an upgrade, you first restore a copy of the site database to an
instance of SQL Server that doesn't host a Configuration Manager site. The version of
SQL Server that you use to host the database copy must be a version of SQL Server that
Configuration Manager supports.

After you restore the site database, on the SQL Server computer, run Configuration
Manager Setup from the source media folder for Configuration Manager.

For more information including specific steps, see Test the database upgrade.

Upgrade sites
If you've completed the following tasks, you're ready to upgrade your Configuration
Manager site:

     Pre-upgrade configurations for your site
     Test the upgrade of the site database on a database copy
     Download prerequisite files and language packs for the version that you plan to
     install

When you upgrade a site in a hierarchy, you upgrade the top-level site of the hierarchy
first. This top-level site is either a CAS or a stand-alone primary site. After you complete
the upgrade of a CAS, you can upgrade child primary sites in any order you want. After
you upgrade a primary site, you can upgrade that site's secondary sites, or upgrade
other primary sites before you upgrade any secondary sites.

Before you upgrade a site, close the Configuration Manager console on the site server
until the upgrade successfully completes. Also close all remote consoles that run on
other computers. After the site upgrade completes successfully, you can reconnect the
console. Until you upgrade a console to the new version, that console can't display
some objects and information that are available in new version.

Upgrade a CAS or primary site
   1. Verify that the user who runs Setup has the following security rights:

<!-- p.982 -->

       Local Administrator rights on the site server

       If the site database server is remote from the site server, local Administrator
       rights on it

2. On the site server, run the following program from the Configuration Manager
  source media: .\SMSSETUP\BIN\X64\Setup.exe . This action starts the Configuration
  Manager Setup wizard.

3. Read the information on the Before You Begin page, and then select Next.

4. On the Getting Started page, select Upgrade this Configuration Manager site,
  and then select Next.

5. On the Product Key page:

  If you previously installed Configuration Manager Evaluation version, you can
  select Install the licensed edition of this product. Then enter your product key for
  the full installation of Configuration Manager. This action converts the site to the
  full version. For more information, see Upgrade an evaluation installation of
  Configuration Manager to a full installation.

  You can specify the Software Assurance expiration date of your licensing
  agreement. This date is a convenient reminder for you of that date. If you don't
  enter this value during setup, you can specify it later in the console.

    ７ Note

    Microsoft doesn't validate this expiration date, and doesn't use this date for
    license validation. It's a reminder to you of your expiration date. Configuration
    Manager periodically checks for new software updates offered online. To be
    eligible to install these updates, your license status should be current.

  For more information, see Licensing and branches.

6. On the Microsoft Software License Terms page, read and accept the license terms,
  and then select Next.

7. On the Prerequisite Licenses page, read and accept the license terms for the
  prerequisite software, and then select Next. Setup downloads and automatically
  installs the software on site systems or clients when it's required. Before you can
  continue to the next page, agree to all terms.

<!-- p.983 -->

 8. On the Prerequisite Downloads page, specify whether Setup downloads the latest
   content from the internet or uses previously downloaded files. This content
   includes prerequisite redistributable files, language packs, and the latest product
   updates. If you already used Setup Downloader, select Use previously downloaded
   files and specify the download folder. For more information, see Setup
   Downloader.

      ７ Note

      When you use previously downloaded files, verify that the path to the
      download folder contains the most recent version of the files.

 9. On the Server Language Selection page, view the list of languages that are
   currently installed for the site. Select other languages that are available at this site
   for the Configuration Manager console and for reports. You can also clear
   languages that you no longer want to support at this site. By default, English is
   selected and can't be removed.

      ） Important

      Each version of Configuration Manager can't use language packs from a prior
      version. To enable support for a language at a site that you upgrade, use the
      version of the language pack for the new version. For example, during
      upgrade from System Center 2012 Configuration Manager to Configuration
      Manager current branch, if the current branch version of a language pack isn't
      available with the prerequisite files you download, you can't install support for
      that language.

10. On the Client Language Selection page, view the list of languages that are
   currently installed for the site. Select other languages that are available at this site
   for client computers, or clear languages that you no longer want to support at this
   site. Specify whether to enable all client languages for mobile device clients, and
   then select Next. By default, English is selected and can't be removed.

11. On the Settings Summary page, review the configuration. When you're ready,
   select Next to start the Prerequisite Checker. This tool verifies server readiness for
   the upgrade of the site. For more information, see Prerequisite Checker.

12. On the Prerequisite Installation Check page, if there are no problems listed, select
   Next to upgrade the site and site system roles.

<!-- p.984 -->

     If the Prerequisite Checker finds a problem, select the item on the list for details
     about how to resolve it. Resolve all items in the list that have an Error status before
     you continue Setup. For items with a Warning status, resolve as many as possible
     in your environment. After you resolve the issues, select Run Check to restart
     prerequisite checking. For more detailed information, open the
     ConfigMgrPrereq.log file in the root of the system drive. The log file can contain
     additional information that's not displayed in the user interface. For a list of
     installation prerequisite rules and descriptions, see Prerequisite checks.

On the Upgrade page, Setup displays the overall progress status. When Setup
completes the core site server and site system installation, you can close the wizard. Site
configuration continues in the background.

Upgrade a secondary site
   1. Verify that the administrative user that runs Setup has the following security rights:

           Local Administrator rights on the secondary site server

           Infrastructure Administrator or Full Administrator security role on the
           parent primary site

           System administrator (SA) rights on the site database of the secondary site

   2. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and then select the Sites node.

   3. Select the secondary site that you want to upgrade. On the Home tab of the
     ribbon, in the Site group, select Upgrade.

   4. Select Yes to confirm the decision, and to start the upgrade of the secondary site.

The secondary site upgrade runs in the background. After the upgrade is complete,
confirm the status in the Configuration Manager console. Select the secondary site
server, then on the Home tab of the ribbon, in the Site group, select Show Install Status.

Post-upgrade tasks
After you upgrade a site, you might have to complete other tasks to finish the upgrade
or reconfigure the site. These tasks can include the following items:

     Upgrade Configuration Manager clients
     Upgrade Configuration Manager consoles

<!-- p.985 -->

     Re-enable database replicas for management points
     Restore settings for Configuration Manager functionality that you use and that
     doesn't persist after the upgrade

Next steps
Scenarios to streamline your installation of Configuration Manager current branch

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.986 -->

Scenarios to streamline your installation
of Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

With the release of update versions for Configuration Manager current branch, there are
new scenarios to streamline the install of a new hierarchy to an update version. You can
also use these techniques to upgrade from Microsoft System Center 2012 Configuration
Manager.

The following list is a summary of the two main scenarios:

      Install a new Configuration Manager current branch hierarchy that runs an update
      version.
         Install only the top-tier site with a baseline version. Then immediately install an
         update to bring that site current with the update version that you'll use. Then
         install others sites directly to that update version.
         This process skips the installation of other sites to a baseline level, and then
         updating them to the update version that you want to use.
         The process also skips the installation of clients to a baseline version, and then
         reinstalling them when you update to a later version.

      Upgrade a Microsoft System Center 2012 Configuration Manager infrastructure to
      an update version of Configuration Manager.
         Manually upgrade your central administration site (CAS) and each primary site
         to a baseline version before you install an update version.
         Don't upgrade secondary sites from Microsoft System Center 2012
         Configuration Manager until your primary sites run the update version that
         you'll use.
         Don't upgrade clients from Microsoft System Center 2012 Configuration
         Manager until your primary sites run the update version that you'll use.

Install a new hierarchy to an update version
   1. Install a top-level site for your new hierarchy by using the baseline media. You can
      use baseline media only to install the first site of a new hierarchy. For more
      information, see Use the Setup Wizard to install sites.

      After this step, your top-level site runs the baseline version.

<!-- p.987 -->

 2. Use in-console updates to update your top-level site to a later version. Before you
   install any child sites or clients, update your top-level site to the update version
   that you plan to use. For more information, see Updates for Configuration
   Manager.

   After this step, your top-level site runs the updated version.

 3. If you intend for the first site to be a CAS, next install new child primary sites. Use
   the installation media from the CD.Latest folder on the CAS server to install child
   primary sites. Use this source media to make sure that new child primary sites
   match the version of the CAS. For more information, see The CD.Latest folder for
   Configuration Manager.

 4. Add other site system roles on remote servers at the CAS and primary sites. This
   action makes sure that the site systems run the updated version. For more
   information, see Install site system roles.

 5. If you plan to have secondary sites, at each primary site, use the in-console option
   to install new secondary sites. Because you didn't install secondary sites while
   primary sites were at the baseline version, you don't need to update the secondary
   sites. Instead, you install new secondary sites that run the updated version. For
   more information, see Install a secondary site.

 6. Install new clients at the primary site. Because you didn't install clients while
   primary sites were at the baseline version, you don't need to update clients.
   Instead, install new clients that run the updated version. For more information, see
   Deploy clients.

 7. Install new consoles on remote computers. Because you didn't install consoles
   while primary sites were at the baseline version, you don't need to update
   consoles. Install them with the updated version. For more information, see Install
   consoles.

Upgrade to current branch
 1. Upgrade your top-level System Center 2012 Configuration Manager site to a
   baseline version of the current branch. Use source media for Configuration
   Manager current branch. You always upgrade the top-level site of a hierarchy first,
   and then upgrade child sites. For more information, see Upgrade to Configuration
   Manager.

   After this step, your top-level site runs the baseline version.

<!-- p.988 -->

 2. Upgrade each child primary site in your hierarchy to the same baseline version.
   When you upgrade from Microsoft System Center 2012 Configuration Manager,
   manually upgrade each primary site to a baseline version of the current branch.
   Don't upgrade secondary sites yet.

   After this step, each primary site runs the baseline version.

 3. Set service windows on child-primary sites. After you upgrade all of your primary
   sites to the baseline version, configure maintenance windows to control when
   those sites install infrastructure updates. For more information, see Service
   windows for site servers.

         Child primary sites automatically install the same updates that you install at a
         CAS.
         Secondary sties don't automatically install new versions. Update them
         manually from the console.

   After this step, child primary sites are ready to install updates during their service
   window.

 4. Install the update version at your top-level site. This action updates your top-level
   site to the updated version. After a CAS installs the update version, each child
   primary site automatically installs the same update during its service window. For
   more information, see Updates for Configuration Manager.

   After this step, your CAS and each primary site run the updated version.

 5. Upgrade secondary sites. After a primary site installs the update, use the in-
   console option to update secondary sites. This action upgrades secondary sites
   directly from System Center 2012 Configuration Manager to the same update
   version as the primary site. For more information about upgrading a secondary
   site, see Upgrade sites.

 6. Upgrade clients. This process upgrades clients directly from System Center 2012
   Configuration Manager to the update version that you installed at the primary site.
   For more information, see How to upgrade clients for Windows computers.

   After this step, run the updated version.

 7. Upgrade consoles on remote computers. This process upgrades clients directly
   from System Center 2012 Configuration Manager to the update version that you
   installed at the primary site. For more information, see Install consoles.

Next steps

<!-- p.989 -->

Configure sites and hierarchies

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.990 -->

Configure sites and hierarchies for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you install your first Configuration Manager site or add additional sites to your
hierarchy, use this checklist to ensure that you consider the most common
configurations that affect both sites and hierarchies.

The following configuration notes apply to most deployments:

      Some options build upon each other, such as Active Directory Forest Discovery,
      boundaries, and boundary groups.

      Several configurations have default values to use without configuration changes, at
      least to start.

      Other configurations, like boundary groups and distribution point groups, require
      you to configure them before using.

                                                                                    ﾉ   Expand table

 Action                  Details

 Configure role-based    Segregate administrative assignments to control which administrative
 administration          users can view and manage different objects and data in your
                         Configuration Manager environment.

                         Configurations for role-based administration are shared with all sites in a
                         hierarchy.

                         For more information, see Configure role-based administration.

 Publish site data to    Make it easy for clients to find services and efficiently use site resources.
 Active Directory
 Domain Services         First extend the Active Directory schema. Then individually configure
                         each site to publish site data

 Configure a service     Plan to install and configure the service connection point at the top-level
 connection point        site of your hierarchy. For more information, see About the service
                         connection point.

 Add site system roles   Install one or more additional site system roles for individual sites. For
                         more information, see Add site system roles.

<!-- p.991 -->

Action                   Details

Configure site           Specify boundaries that define network locations on your intranet that
boundaries and           can contain devices that you want to manage. Then configure boundary
boundary groups          groups so that clients at those network locations can find Configuration
                         Manager resources. For more information, see Define site boundaries
                         and boundary groups.

Configure distribution   Configure logical groups of distribution points to make managing
point groups             deployments easier. For more information, see Manage distribution point
                         groups.

Run discovery            Run discovery to find resources on your network, including network
                         infrastructure, devices, and users.

                         For more information, see Run discovery.

Add redundancy and       Install additional SMS Providers and Configuration Manager consoles to
capacity for             expand capacity for administrators to manage your infrastructure:
administrators
                         Install additional SMS providers to provide redundancy for console and
                         API connections to the site. For more information, see Manage the SMS
                         Provider.

                         Install additional Configuration Manager consoles to provide access to
                         additional administrative users. For more information, see Install
                         Configuration Manager consoles.

Configure site           Configure site components at each site to modify the behavior of site
components               system roles and site status reporting. For more information, see Site
                         components.

Create custom            Using information that the site discovers about devices and users, create
collections              custom collections of objects to simplify future management tasks. For
                         more information, see How to create collections.

Configure settings to    Configure settings at a site to warn administrators when they create a
manage high-risk         high-risk deployment. For more information, see Settings to manage
deployments              high-risk deployments.

Configure database       Configure a database replica to reduce the processor load that's placed
replicas for             on the site database server by management points as they service
management points        requests from clients. For more information, see Database replicas for
                         management points.

Configure a SQL          Configure availability groups as high-availability and disaster-recovery
Server Always On         solutions for hosting the site database at primary sites and the central
availability group       administration site. For more information, see Prepare to use a SQL
                         Server Always On availability group with Configuration Manager.

<!-- p.992 -->

 Action                    Details

 Modify replication        See Data transfers between sites to learn about the following subjects:
 between sites
                           Configure file-based replication between secondary sites

                           Configure database replication links

                           Configure distributed views

 Configure site servers    Starting in version 1806, configure a site server in passive mode for each
 in passive mode           primary site and the central administration site. This feature provides a
                           highly available site server. For more information, see Site server high
                           availability.

Feedback
Was this page helpful?      Yes            No

Provide product feedback

<!-- p.993 -->

Add site system roles for Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Each Configuration Manager site supports multiple site system roles. Each role extends
the functionality and capacity of your site to provide services to the site and to manage
devices and users. Each site system role on a site system server must be from the same
site.

Configuration Manager doesn't support site system roles for multiple sites on a single
site system server.

    Tip

   If you're not familiar with the basics for site system roles or the difference between
   the site server, site system servers, and site system roles, see Fundamentals of
   Configuration Manager.

The following articles detail procedures and related details for installing site system
roles:

         Install site system roles: Basic guidance about how to use the two in-console
         wizards to install new site system roles.

         Set up checklist for CMG: Set up a cloud management gateway (CMG) to manage
         clients on the internet.

         Install site system roles for on-premises mobile device management (MDM): Set up
         your site system roles to support managing modern devices by using
         Configuration Manager on-premises MDM.

         Configuration options for site system roles: Some site system roles support
         configurations that require more details than the user interface can explain.

         Remove a site system role: Guidance and procedures to remove roles from site
         system servers.

Feedback

<!-- p.994 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.995 -->

Install site system roles for Configuration
Manager
09/16/2025

Applies to: Configuration Manager (current branch)

There are two methods in the Configuration Manager console to install site system roles:

     Add Site System Roles: Add site system roles to an existing site system server in the site.

     Create Site System Server: Specify a new server as a site system server, and then install
     one or more roles. This method is the same as the Add Site System Roles, except for the
     first page. You first specify the name of the server and the site in which you want to install
     it.

   Tip

  A best practice for security and operational resilience is to keep site system roles separate
  from the site server, rather than colocate them on the same computer. When you install a
  role on a remote computer, Configuration Manager adds the computer account of the
  remote computer to a local group on the site server.

  When you install the site on a domain controller, the group on the site server is a domain
  group instead of a local group. In this case, the remote site system role doesn't
  immediately work. The site system server needs to restart, or you refresh the Kerberos
  ticket for the remote server's computer account. For more information, see Accounts
  used.

Before it installs the site system role, Configuration Manager checks the destination computer
to make sure it meets the prerequisites for the selected roles.

By default, when Configuration Manager installs a site system role, it installs files on the first
available NTFS-formatted disk drive that has the most available free disk space. To prevent
Configuration Manager from installing on specific drives, before you install the site system
server, create an empty file named NO_SMS_ON_DRIVE.SMS in the root of the drive.

Configuration Manager uses the site system installation account to install roles. You specify
this account when you install the role. By default, this account is the local system account of
the site server computer. You can specify a domain user account as the site system installation
account. For more information, see Accounts - Site system installation account.

<!-- p.996 -->

Install roles on an existing site system server
 1. In the Configuration Manager console, go to the Administration workspace. Expand Site
   Configuration, and select the Servers and Site System Roles node. Select the existing site
   system server on which you want to install new site system roles.

 2. In the ribbon, on the Home tab, in the Server group, select Add Site System Roles.

 3. On the General page, review the settings.

       Tip

      To access the site system role from the internet, make sure that you specify an
      internet fully qualified domain name (FQDN).

 4. On the Proxy page, if roles on this server require an internet proxy, then specify settings
   for a proxy server. For more information, see Proxy server support.

 5. On the System Role Selection page, select the site system roles that you want to add.

 6. Complete the wizard. Additional pages can appear for specific roles. For more
   information, see Configuration options for site system roles.

  Tip

 The Windows PowerShell cmdlet, New-CMSiteSystemServer, performs the same function
 as this procedure. For more information, see New-CMSiteSystemServer.

Install roles on a new site system server
 1. In the Configuration Manager console, go to the Administration workspace. Expand Site
   Configuration, and select the Servers and Site System Roles node.

 2. In the ribbon, on the Home tab, in the Create group, select Create Site System Server.

 3. On the General page, specify the general settings for the site system.

       Tip

      To access the new site system role from the internet, make sure that you specify an
      internet FQDN.

<!-- p.997 -->

 4. On the Proxy page, if roles on this server require an internet proxy, then specify settings
   for a proxy server. For more information, see Proxy server support.

 5. On the System Role Selection page, select the site system roles that you want to add.

 6. Complete the wizard. Additional pages can appear for specific roles. For more
   information, see Configuration options for site system roles.

  Tip

 The Windows PowerShell cmdlet, New-CMSiteSystemServer, performs the same function
 as this procedure. For more information, see New-CMSiteSystemServer.

Next steps
   Configuration options for site system roles

   Remove role

<!-- p.998 -->

Step-by-step example deployment of a
management point in an untrusted Active
Directory domain
Applies to: Configuration Manager (current branch)

This example shows how to install a Configuration Manager management point (MP) on a server
in an Active Directory domain that doesn't have a two-way trust with the domain that contains
the site server. This scenario is common when you need to extend management to a perimeter
network (DMZ), a partner domain, or another network segment that you don't fully trust.

Review your organization's network and Active Directory documentation for procedures and best
practices that apply to your environment. Use the steps in this article as a proof-of-concept
reference. For production guidance, see Communications across Active Directory forests.

  ７ Note

  This scenario applies to a site system connected to a primary site only. Secondary sites
  require a two-way domain trust between the secondary site's domain and the parent
  primary site's domain. Installing a secondary site in a domain without the required trust is
  not supported.

Test environment
The step-by-step instructions in this article use the following test environment:

     Trusted domain ( corp.contoso.com ): Contains the Configuration Manager primary site
     server ( SiteServer ) and the SQL Server site database ( SQLServer ). The site code is P01.

     Untrusted domain ( branch.fabrikam.com ): Contains the server that hosts the management
     point ( DMZ-MP ). No Active Directory trust exists between the two domains.

     Both domains use Windows Server DNS, and DNS conditional forwarders are configured in
     both directions so that each domain can resolve FQDNs in the other domain.

     You can sign in as a domain administrator in both domains to perform all procedures.

<!-- p.999 -->

Overview of the deployment steps
The following table summarizes this deployment and explains why each step is required.

                                                                                           ﾉ    Expand table

 Step   What you do                     Why it's required

 Step   Create service accounts in      The site system installation account and the MP database
 1      the untrusted domain            connection account must exist in the domain where the MP server
                                        resides, or as global accounts resolvable from both domains.

 Step   Grant SQL Server database       The MP database connection account must have the permissions to
 2      permissions                     read data in the site database so the management point can query
                                        client policy and inventory data.

 Step   Configure firewall rules        Normally, all network traffic between the MP and the site server and
 3                                      site database must be explicitly permitted through firewalls.

 Step   Install management point        Ensures that DMZ-MP has the Windows features and SQL connectivity
 4      prerequisites on the site       components required before Configuration Manager installs the
        system server                   role.

 Step   Install the management point    Creates the site system server object and installs the management
 5      role on DMZ-MP                  point role by using the accounts and settings prepared in earlier
                                        steps.

 Step   Verify the management point     Confirms that the management point is healthy and that clients in
 6      installation                    the untrusted forest can communicate with it.

Step 1: Create domain accounts
Use two dedicated user accounts. Configure both accounts with non-expiring passwords, and
don't grant unnecessary privileges.

                                                                                           ﾉ    Expand table

 Account                      Domain                    Purpose                Required permissions

 branch.fabrikam.com\svc-     Untrusted                 Site system            Member of the local
 cm-dmzmpinstall              ( branch.fabrikam.com )   installation account   Administrators group on
                                                        — the site server       DMZ-MP .
                                                        uses this account to
                                                        connect to DMZ-MP
                                                        and install the
                                                        management point
                                                        role.

<!-- p.1000 -->

Account                     Domain                 Purpose                  Required permissions

 corp.contoso.com\svc-cm-   Trusted                Management point         SQL Server login on
dmzmpdbconnect              ( corp.contoso.com )   connection account       SQLServer instance with the
                                                   — the management         smsdbrole_MP and
                                                   point uses this          smsdbrole_MPUserSvc roles
                                                   account to read and      assigned in the SQL database
                                                   write data to the site   of the site (granted in Step
                                                   database.                2).

To create the site system installation account in the
untrusted domain
  1. Sign in to a domain controller in branch.fabrikam.com using a domain administrator
     account.

  2. Open Active Directory Users and Computers.

  3. In the navigation pane, expand branch.fabrikam.com, right-click the Service Accounts
     organizational unit (OU), and then choose New > User.

        Tip

       If a dedicated Service Accounts OU doesn't exist, create one first or place the accounts
       in a suitable OU. Don't place service accounts in the default Users container in a
       production environment.

  4. Complete the New Object – User wizard with the following settings, and then choose
     Finish:

          First name: svc-cm-dmzmpinstall
          User logon name: svc-cm-dmzmpinstall
          Password: Use a strong, non-expiring password.
          Select Password never expires and clear User must change password at next logon.

  5. Close Active Directory Users and Computers.

To create the MP database connection account in the
trusted domain
  1. Sign in to a domain controller in corp.contoso.com using a domain administrator account.
