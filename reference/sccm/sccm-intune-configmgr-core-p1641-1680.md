---
title: "Core infrastructure documentation — pages 1641-1680"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1641-1680
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1641-1680
family: sccm
documentKind: "doc"
abstract: "Flowchart - Download updates for Configuration Manager Article • 10/04/2022 Applies to: Configuration Manager (current branch) This data flow displays the process by which a site with an on-line service connection point downloads in-console updates. Feedback Was this page helpfu"
---

# Core infrastructure documentation — pages 1641-1680

<!-- p.1641 -->

Flowchart - Download updates for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This data flow displays the process by which a site with an on-line service connection
point downloads in-console updates.

<!-- p.1642 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1643 -->

Flowchart - Update replication for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

These data flows display the process by which an in-console update you select to install
replicates to additional sites. These flows also display the process of extracting the
update to run prerequisite checks and to install updates at a central administration site
and at primary sites.

<!-- p.1644 -->

<!-- p.1645 -->

<!-- p.1646 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1647 -->

Pre-release features in Configuration
Manager
Article • 04/11/2023

Applies to: Configuration Manager (current branch)

Pre-release features are features that are in the current branch for early testing in a
production environment. These features are fully supported, but still in active
development. They might receive changes until they move out of the pre-release
category.

Give consent
Before using pre-release features, give consent to use pre-release features. Giving
consent is a one-time action per hierarchy that you can't undo. Until you give consent,
you can't enable new pre-release features included with updates. After you turn on a
pre-release feature, you can't turn it off.

   1. In the Configuration Manager console, go to the Administration workspace,
      expand Site Configuration, and select the Sites node.

   2. In the ribbon, select Hierarchy Settings.

   3. On the General tab of Hierarchy Settings Properties, enable the option to Consent
      to use pre-release features.

Enable pre-release features
When you install an update that includes pre-release features, those features are visible
in the Updates and Servicing Wizard with the regular features included in the update.

If consent is given
In the Updates and Servicing Wizard, enable pre-release features. Select the pre-release
features as you would any other feature.

Optionally, wait to enable pre-release features later from the Features node under
Updates and Servicing in the Administration workspace. Select a feature, and then
select Turn on in the ribbon. Until you give consent, this option isn't available for use.

<!-- p.1648 -->

If you haven't given consent
In the Updates and Servicing Wizard, pre-release features are visible but you can't
enable them. After the update is installed, these features are visible in the Features
node. However, you can't enable them until you give consent.

  ） Important

  In a multi-site hierarchy, you can only enable optional or pre-release features from
  the central administration site. This behavior ensures there are no conflicts across
  the hierarchy.

  If you gave consent at a stand-alone primary site, and then expand the hierarchy by
  installing a new central administration site, you must give consent again at the
  central administration site.

When you enable a pre-release feature, the Configuration Manager hierarchy manager
(HMAN) must process the change before that feature becomes available. Processing of
the change is often immediate. Depending on the HMAN processing cycle, it can take
up to 30 minutes to complete. After the change is processed, restart the console before
using the feature.

List of pre-release features
                                                                          ﾉ      Expand table

 Feature                                          Added as pre-        Added as a full
                                                  release              feature

 Cloud management gateway with virtual machine    Version 2010         Version 2107
 scale set

 Orchestration groups                             Version 2002         Version 2111

 Task sequence deployment type                    Version 2002

 Task sequence debugger                           Version 1906         Version 2203

 Application groups                               Version 1906         Version 2111

   Tip

<!-- p.1649 -->

  For more information on non-pre-release features that you must enable first, see
  Enable optional features from updates.

  For more information on features that are only available in the technical preview
  branch, see Technical Preview.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1650 -->

Service windows for site servers
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To control when in-console updates can install, configure service windows. You can add
service windows at the central administration site (CAS) and primary sites. Each site can
have multiple service windows. The site determines when it can install an update by the
combination of all service windows that it has.

   Tip

  A service window is for a site server. A maintenance window is for a client. For more
  information, see How to use maintenance windows.

Default behavior
When you don't configure a service window:

      On your top-tier site, you choose when to start the update installation. The top-tier
      site is either the CAS or a stand-alone primary site.

      On a child primary site, the update automatically installs after it successfully
      completes at the CAS.

      On a secondary site, updates never start automatically. After the parent primary
      site updates, manually start the update from the console.

Behavior with a service window
When you create one or more service windows:

      On your top-tier site, you can't start the installation of any new update from the
      console until the time is in the service window. Even with a service window, the site
      still automatically downloads updates so they're ready to install.

      On a child primary site, an update from the CAS downloads to the primary site, but
      doesn't automatically start. You can't manually start the install of an update outside
      of a service window. When service windows no longer block update installation,
      the primary site automatically starts the update installation.

<!-- p.1651 -->

   Secondary sites don't support service windows, and don't automatically install
   updates. After the parent primary site updates, manually start the update from the
   console.

Configure a service window
 1. In the Configuration Manager console, go to the Administration workspace,
   expand Site Configuration, and select the Sites node.

 2. Select the site server where you want to configure a service window.

 3. In the ribbon, select Properties.

 4. Switch to the Service Windows tab.

 5. To add a new service window, select the new button (gold asterisk).

 6. In the Schedule window, specify a name to describe the service window. This name
   helps you identify the service window in the console.

 7. Configure the date, time, and recurrence pattern as necessary for this site.

<!-- p.1652 -->

After you create a service window, use the edit and delete buttons to make changes.

Next steps
Install in-console updates

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1653 -->

Use the service connection tool for
Configuration Manager
Article • 03/10/2025

Applies to: Configuration Manager (current branch)

Use the service connection tool when your service connection point is in offline mode.
You can also use it when your Configuration Manager site system servers aren't
connected to the internet. The tool can help you keep your site up to date with the
latest updates to Configuration Manager.

When you run the tool, it connects to the Configuration Manager cloud service, uploads
usage information for your hierarchy, and downloads updates. Uploading usage data is
necessary to enable the cloud service to provide the correct updates for your
environment.

Prerequisites
      The site has a service connection point, and you configure it for an Offline, on-
      demand connection.

      Run the tool from a command prompt as an administrator. There's no user
      interface.

      You run the tool from the service connection point and a computer that can
      connect to the internet. Each of these computers needs to have a x64-bit OS, and
      have the following components:

         Both the Visual C++ Redistributable x86 and x64 files. By default, Configuration
         Manager installs the x64 version on the computer that hosts the service
         connection point. This tool requires the Microsoft Visual C++ 2015-2019
         redistributable package (14.28.29914.0), or later, on the computer that you are
         running it from. To download this component, see Microsoft Visual C++
         Redistributable latest supported downloads.

           ７ Note

           If upgrading from an out of support version of Configuration Manager
           prior to 2107, the tool requires the Visual C++ 2013 redistributable
           package (12.0.40660.0), which is available from the same link.

<!-- p.1654 -->

       This tool requires .NET version 4.6.2, and version 4.8 is recommended. For more
       information, see Site and site system prerequisites.

       Starting in version 2309, this tool requires installation of the ODBC Driver 18 for
       SQL Server (x64). To download this component, see Download ODBC Driver for
       SQL Server.

    The account you use to run the tool needs the following permissions:

       Local administrator on the computer that hosts the service connection point

       Read permissions to the site database

    You need a method to transfer the files between the computer with internet access
    and the service connection point. For example, a USB drive with sufficient free
    space to store the files and updates.

Overview
  1. Prepare: Run the tool on the service connection point. It puts your usage data into
    a .cab file at the location you specify. Copy the data file to the computer with an
    internet connection.

  2. Connect: Run the tool on the computer with an internet connection. It uploads
    your usage data, and then downloads Configuration Manager updates. Copy the
    downloaded updates to the service connection point.

    You can upload multiple data files at one time, each from a different hierarchy. You
    can also specify a proxy server and a user for the proxy server.

  3. Import: Run the tool on the service connection point. It imports the updates, and
    adds them to your site. You can then view and install those updates in the
    Configuration Manager console.

Upload multiple data files
    Put all exported data files from separate hierarchies into the same folder. Give each
    file a unique name. If necessary, you can manually rename them.

    When you run the tool to upload data to Microsoft, you specify the folder that
    contains the data files.

    When you run the tool to import data, the tool only imports the data for that
    hierarchy.

<!-- p.1655 -->

Specify a proxy server
If the computer with an internet connection requires a proxy server, the tool supports a
basic proxy configuration. Use the optional parameters -proxyserveruri and -
proxyusername. For more information, see Command-line parameters.

Specify the type of updates to download
The tool supports options to control what files you download. By default, the tool
downloads only the latest available update that applies to the version of your site. It
doesn't download hotfixes.

To modify this behavior, use one of the following parameters to change what files it
downloads:

     -downloadall: Download all updates, including updates and hotfixes, whatever the
     version of your site.

     -downloadhotfix: Download all hotfixes whatever the version of your site.

     -downloadsiteversion: Downloads updates and hotfixes with a later version than
     the version of your site.

        ） Important

        Because of a known issue in Configuration Manager version 2002, the default
        behavior doesn't work as expected. Update to version 2006, or use the -
        downloadsiteversion parameter to download the necessary updates for
        version 2002.

For more information, see Command-line parameters.

   Tip

  The tool determines the version of your site from the data file. To verify the version,
  look in the .cab file for the text file named with the site version.

Use the tool
The service connection tool is in the Configuration Manager installation media at the
following path: SMSSETUP\TOOLS\ServiceConnectionTool\ServiceConnectionTool.exe .

<!-- p.1656 -->

Always use the service connection tool that matches the version of Configuration
Manager that you use. All of these files must be in the same folder for the service
connection tool to work.

Copy the ServiceConnectionTool folder with all of its contents to the computer with an
internet connection.

In this procedure, the command-line examples use the following file names and folder
locations. You don't need to use these paths and file names. You can use alternatives
that match your environment and preferences.

     The path to the Configuration Manager installation media source files on the
     service connection point: C:\Source

     The path to a USB drive where you store the data to transfer between computers:
     D:\USB\

     The name of the data file that you export from the site: UsageData.cab

     The name of the empty folder where the tool stores downloaded updates for
     Configuration Manager: UpdatePacks

Prepare
   1. On the computer that hosts the service connection point, open a command
     prompt as an administrator, and change directory to the tool location. For
     example:

     cd C:\Source\SMSSETUP\TOOLS\ServiceConnectionTool\

   2. Run the following command to prepare the data file:

     ServiceConnectionTool.exe -prepare -usagedatadest D:\USB\UsageData.cab

       ７ Note

       If you'll upload data files from more than one hierarchy at the same time, give
       each data file a unique name. If necessary, you can rename files later.

     The data in the file is based on the level of diagnostic and usage data that you
     configure for the site. For more information, see Overview of diagnostics and
     usage data. You can use the tool to export the data to a CSV file to view the
     contents. For more information, see -export.

<!-- p.1657 -->

 3. After the tool finishes exporting the usage data, copy the data file to a computer
   that has access to the internet.

Connect
 1. On the computer with internet access, open a command prompt as an
   administrator, and change directory to the tool location. This location is a copy of
   the entire ServiceConnectionTool folder. For example:

   cd D:\USB\ServiceConnectionTool\

 2. Run the following command to upload the data file and download the
   Configuration Manager updates:

   ServiceConnectionTool.exe -connect -usagedatasrc D:\USB -updatepackdest

   D:\USB\UpdatePacks

   For more examples, see Command line parameters.

     ７ Note

     When you run this command line, you might see the following error:

     Unhandled Exception: System.UnauthorizedAccessException: Access to the
     path
     'C:\Users\jqpublic\AppData\Local\Temp\extractmanifestcab\95F8A562.sql'
     is denied.

     You can safely ignore this error. Close the error window to continue.

 3. After the tool finishes downloading the updates, copy them to the service
   connection point.

Import
 1. On the computer that hosts the service connection point, open a command
   prompt as an administrator, and change directory to the tool location. For
   example:

   cd C:\Source\SMSSETUP\TOOLS\ServiceConnectionTool\

 2. Run the following command to import the updates:

<!-- p.1658 -->

      ServiceConnectionTool.exe -import -updatepacksrc D:\USB\UpdatePacks

   3. After the import completes, close the command prompt. It only imports updates
     for the applicable hierarchy.

   4. In the Configuration Manager console, go to the Administration workspace, and
     select the Updates and Servicing node. Imported updates are now available to
     install. For more information, see Install in-console updates.

Log files
     ServiceConnectionTool.log: Each time you run the service connection tool, it writes
     to this log file. The path of the log file is always the same location as the tool. This
     log file provides simple details about the tool usage based on the parameters you
     use. Each time you run the tool, the tool replaces any existing log file.

     ConfigMgrSetup.log: During the Connect phase, the tool writes to this log file at
     the root of the system drive. This log file provides more detailed information. For
     example, what files the tool downloads, and if the hash checks are successful.

Command-line parameters
This section lists in alphabetical order all of the available parameters for the service
connection tool.

-connect
Use during the Connect phase on the computer with internet access. It connects to the
Configuration Manager cloud service to upload the data file, and download updates.

It requires the following parameters:

     -usagedatasrc: The location of the data file to upload
     -updatepackdest: A path for the downloaded updates

You can also use the following optional parameters:

     -proxyserveruri: The FQDN of the proxy server
     -proxyusername: A user name for the proxy server
     -downloadall: Download everything, including updates and hotfixes, whatever the
     version of your site.
     -downloadhotfix: Download all hotfixes, whatever the version of your site.

<!-- p.1659 -->

     -downloadsiteversion: Download updates and hotfixes that have a later version
     than the version of your site.

Example of connect without a proxy server
ServiceConnectionTool.exe -connect -usagedatasrc D:\USB\ -updatepackdest

D:\USB\UpdatePacks

Example of connect with a proxy server
ServiceConnectionTool.exe -connect -usagedatasrc D:\USB\Usagedata.cab -

updatepackdest D:\USB\UpdatePacks -proxyserveruri itproxy.contoso.com -
proxyusername jqpublic

Example of connect to download only site version applicable
updates
ServiceConnectionTool.exe -connect -downloadsiteversion -usagedatasrc D:\USB -
updatepackdest D:\USB\UpdatePacks

-dest
A required parameter with the -export parameter to specify the path and file name of
the CSV file to export. For more information, see -export.

-downloadall
An optional parameter with the -connect parameter to download everything, including
updates and hotfixes, whatever the version of your site. For more information, see -
connect.

-downloadhotfix
An optional parameter with the -connect parameter to only download all hotfixes,
whatever the version of your site. For more information, see -connect.

-downloadsiteversion

<!-- p.1660 -->

An optional parameter with the -connect parameter to only download updates and
hotfixes that have a later version than the version of your site. For more information, see
-connect.

-export
Use during the Prepare phase to export usage data to a CSV file. Run it as an
administrator on the service connection point. This action lets you review the contents
of the usage data before you upload to Microsoft. It requires the -dest parameter to
specify the location of the CSV file.

Example of export
-export -dest D:\USB\usagedata.csv

-import
Use during the Import phase on the service connection point to import the updates to
the site. It requires the -updatepacksrc parameter to specify the location of the
downloaded updates.

Example of import
ServiceConnectionTool.exe -import -updatepacksrc D:\USB\UpdatePacks

-prepare
Use during the Prepare phase on the service connection point to export usage data
from the site. It requires the -usagedatadest parameter to specify the location of the
exported data file.

Example of prepare
ServiceConnectionTool.exe -prepare -usagedatadest D:\USB\UsageData.cab

-proxyserveruri
An optional parameter with the -connect parameter to specify the FQDN of your proxy
server. If your proxy requires a port other than 80 and you fail to specify it, or specify the

<!-- p.1661 -->

wrong port, the tool may fail and report with a CAB does not contain telemetry data.
error. For more information, see -connect.

-proxyusername
An optional parameter with the -connect parameter to specify the username to
authenticate with your proxy server. For more information, see -connect.

-updatepackdest
A required parameter with the -connect parameter to specify a path for the downloaded
updates. For more information, see -connect.

-updatepacksrc
A required parameter with the -import parameter to specify a path of the downloaded
updates. For more information, see -import.

-usagedatadest
A required parameter with the -prepare parameter to specify a path and file name of
the exported data file. For more information, see -prepare.

Next steps
Install in-console updates

How to view diagnostics and usage data

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1662 -->

Use the update registration tool to
import hotfixes
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Some updates for Configuration Manager aren't available from the Microsoft cloud
service and are only obtained out-of-band. An example is a limited release hotfix to
address a specific issue.

When you must install an out-of-band release, and the update or hotfix file name ends
with the extension update.exe, you use the update registration tool. This tool imports
the update to the Configuration Manager console. It enables you to extract and transfer
the update package to the site server, and register the update with the Configuration
Manager console.

If the hotfix file only has the .exe file extension (not update.exe), use the hotfix installer
to install the update.

  ７ Note

  This article provides general guidance about how to install hotfixes that update
  Configuration Manager. For details about a specific hotfix or update, refer to the
  corresponding hotfix article.

Prerequisites
      This tool only installs out-of-band updates that end with the full .update.exe file
      extension.

      It is self-contained with the individual updates that you get directly from Microsoft.

      The service connection point can be in either online or offline mode.

      Run it on the server with the service connection point site system role.

      Starting in version 2107, the service connection point requires .NET version 4.6.2,
      and version 4.8 is recommended. In version 2103 and earlier, this role requires .NET
      4.5.2 or later. For more information, Site and site system prerequisites.

<!-- p.1663 -->

     When you run the tool on the service connection point, the account that you use
     needs the following configurations:

        A local Administrator

        Write permissions to the following folder: <Configuration Manager installation
        directory>\EasySetupPayload\offline

Process
   1. On the computer that hosts the service connection point, open a command
     prompt with administrative privileges. Then change directories to the location that
     contains the update file. The update file name uses the following format:
      <Product>-<product version>-<KB article ID>-ConfigMgr.Update.exe

   2. Run the following command to start the update registration tool: <Product>-
     <product version>-<KB article ID>-ConfigMgr.Update.exe

     After the hotfix is registered, it appears as a new update in the console within 24
     hours. To accelerate this process: in the Configuration Manager console, go to
     Administration workspace, and select the Updates and Servicing node. In the
     ribbon, select Check for Updates.

     The update registration tool logs its actions to a .log file on the local computer.
     The log file has the same name as the hotfix file and is in the %SystemRoot%/Temp
     folder.

     After the update is registered, you can close the update registration tool.

   3. In the Configuration Manager console, go to the Administration workspace, and
     select the Updates and Servicing node. Hotfixes that you've imported are now
     available to install.

Next steps
Install in-console updates

Feedback
Was this page helpful?    Yes    No

<!-- p.1664 -->

Provide product feedback

<!-- p.1665 -->

Use the Hotfix Installer to install
updates for Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Some updates for Configuration Manager aren't available from the Microsoft cloud
service. These updates are available out-of-band. An example is a limited release hotfix
to address a specific issue.

When you need to install an update that you get from Microsoft:

      If the update has the simple file extension .exe: Use the hotfix installer that's
      included with that download. Install the update directly to the Configuration
      Manager site server.

      If the hotfix file has the .update.exe file extension: Use the update registration tool
      to import hotfixes to Configuration Manager.

Overview
Hotfixes for Configuration Manager are similar to updates for other Microsoft products,
such as SQL Server. They contain either one individual fix or a bundle, which is a rollup
of fixes.

      Individual updates include a single focused update for a specific version of
      Configuration Manager.
      Update bundles include multiple updates for a specific version of Configuration
      Manager.
      When an update is a bundle, you can't install individual updates from that bundle.

If you plan to create deployments to install updates on other computers, install the
update bundle on a central administration site (CAS) server or primary site server.

When you run the update bundle, the following process happens:

      It extracts the update files for each applicable component from the update bundle.

      Starts a wizard that guides you through a process to configure the updates and
      deployment options for the updates.

<!-- p.1666 -->

         After you complete the wizard, the updates in the bundle that apply to the site
         server are installed on the site server.

The wizard also creates deployments that you can use to install the updates on other
computers. Deploy the updates to other computers by using a supported deployment
method. For example, a software deployment package or System Center Updates
Publisher.

When the wizard runs, it creates a .cab file on the site server for use with Updates
Publisher. Optionally, you can configure the wizard to also create one or more packages
for software deployment. You can use these deployments to install updates on
components, such as clients or the Configuration Manager console. You can also install
updates manually on computers that don't run the Configuration Manager client.

You can update the following three groups in Configuration Manager:

         Configuration Manager server roles, which include:

            CAS

            Primary site

            Secondary site

            Remote SMS Provider

         Configuration Manager console

         Configuration Manager client

   ７ Note

   Updates for site system roles are installed as part of the update for site servers.
   They are serviced by the site component manager. This behavior includes updates
   for the site database and the cloud management gateway (CMG).

   Pull-distribution points are serviced by distribution manager instead of the site
   component manager.

Each update bundle for Configuration Manager is a self-extractable .exe file (SFX). This
file contains the files that are necessary to install the update on the applicable
components of Configuration Manager. Typically, the SFX file can contain the following
files:

<!-- p.1667 -->

                                                                                     ﾉ   Expand table

 File                               Details

 <Product version>-QFE-KB<KB        This file is the update. The command line for this file is
 article ID>-<platform>-            managed by Updatesetup.exe. For example: CM1511RTM-QFE-
 <language>.exe                     KB123456-X64-ENU.exe

 Updatesetup.exe                    This MSI wrapper manages the installation of the update
                                    bundle. When you run the update, Updatesetup.exe detects the
                                    display language of the computer where it runs. By default, the
                                    user interface for the update is in English. However, when the
                                    display language is supported, the user interface displays in the
                                    computer's local language.

 License_<language>.rtf             When applicable, each update contains one or more license files
                                    for supported languages.

 <Product&updatetype>-<product      When the update applies to the Configuration Manager console
 version>-<KB article ID>-          or clients, the update bundle includes separate Windows
 <platform>.msp                     Installer patch (.msp) files. For example: ConfigMgr1511-AdminUI-
                                    KB1234567-i386.msp for the console or ConfigMgr1511-client-
                                    KB1234567-x64.msp for the client.

By default, the update bundle logs its actions to a .log file on the site server. The log file
has the same name as the update bundle and is written to the %SystemRoot%/Temp folder.

When you run the update bundle, it extracts a file with the same name as the update
bundle to a temporary folder on the computer, and then runs Updatesetup.exe.
Updatesetup.exe starts the software update wizard.

As applicable to the scope of the update, the wizard creates a series of folders under the
Configuration Manager installation folder on the site server. The folder structure is
similar to the following example: \Hotfix\<KB Number>\<Update Type>\<Platform>

The following table provides details about the folders in the folder structure:

                                                                                     ﾉ   Expand table

 Folder           More information
 name

 <KB Number>      This folder is the ID number for this update bundle.

 <Update          This folder is the type of update for Configuration Manager. The wizard creates a
 type>            separate folder for each type of update in the bundle. They include the following
                  types:

<!-- p.1668 -->

 Folder          More information
 name

                 - Server: Includes updates to site servers, site database servers, and SMS Providers.
                 - Client: Includes updates to the Configuration Manager client.
                 - AdminConsole: Includes updates to the Configuration Manager console

                 The wizard also creates a folder named SCUP, which contains the .cab file for
                 Updates Publisher.

 <Platform>      This folder is platform-specific. It contains update files that are specific to a type of
                 processor. These folders include: x64 and I386.

How to install updates
To install updates, first install the update bundle on a site server. When you install an
update bundle, it starts an install wizard for that update. This wizard does the following
actions:

      Extracts the update files

      Helps you configure deployments

      Installs applicable updates on the server components of the local computer

After you install the update bundle on a site server, you can then update other
components for Configuration Manager. The following table describes update actions
for these various components:

                                                                                       ﾉ   Expand table

 Component             Instructions

 Site server           Deploy updates to a remote site server when you don't choose to install the
                       update bundle directly on that remote site server.

 Site database         For remote site servers, deploy server updates that include an update to the
                       site database if you don't install the update bundle directly on that remote
                       site server.

 Configuration         After initial installation of the Configuration Manager console, you can install
 Manager console       updates for the console on each computer that runs it. You can't modify the
                       console installation files to apply the updates during the initial installation of
                       the console.

 Remote SMS            Install updates for each instance of the SMS Provider that runs on a
 Provider              computer other than the site server where you installed the update bundle.

<!-- p.1669 -->

 Component           Instructions

 Configuration       After initial installation of the Configuration Manager client, you can install
 Manager clients     updates for the Configuration Manager client on each computer that runs
                     the client.

  ７ Note

  You can deploy updates only to computers that run the Configuration Manager
  client.

If you reinstall a client, Configuration Manager console, or SMS Provider, also reinstall
the updates for these components.

Update servers
Updates for servers can include updates for sites, the site database, and computers that
run an instance of the SMS Provider.

Update a site

To update a Configuration Manager site, you can install the update bundle directly on
the site server. You can also deploy the updates to a site server after you install the
update bundle on a different site.

When you install an update on a site server, the update installation process manages
other actions that are required to apply the update, such as updating site system roles.
The exception is the site database. The next section contains information about how to
update the site database.

Update a site database
To update the site database, the installation process runs a file named update.sql on the
site database. You can configure the update process to automatically update the site
database, or you can manually update the site database later.

Automatic update of the site database

When you install the update bundle on a site server, you can choose to automatically
update the site database when the server update is installed. This decision applies only

<!-- p.1670 -->

to the site server where you install the update bundle and doesn't apply to deployments
that are created to install the updates on remote site servers.

  ７ Note

  When you choose to automatically update the site database, the process updates a
  database regardless whether the database is located on the site server or on a
  remote computer.

  ） Important

  Before you update the site database, create a backup of the site database. You can't
  uninstall an update to the site database. For information about how to create a
  backup for Configuration Manager, see Backup and recovery for Configuration
  Manager.

Manual update of the site database

If you choose not to automatically update the site database when you install the update
bundle on the site server, the server update doesn't modify the database on the site
server where the update bundle runs. However, deployments that use the package that
is created for software deployment or that installs always update the site database.

  ２ Warning

  When the update includes updates to both the site server and the site database,
  the update isn't functional until the update is completed for both the site server
  and site database. Until the update is applied to the site database, the site is in an
  unsupported state.

   1. On the site server, stop the SMS_SITE_COMPONENT_MANAGER service. Then stop
     the SMS_EXECUTIVE service.

   2. Close the Configuration Manager console.

   3. Run the update script named update.sql on that site's database. For information
     about how to run a script to update a SQL Server database, see the documentation
     for the version of SQL Server that you use for your site database server.

         Tip

<!-- p.1671 -->

        When the update bundle installs, it extracts update.sql to the following
        location on the site server: \\<Server Name>\SMS_<Site Code>\Hotfix\<KB
        Number>\update.sql .

   4. Restart the services that you stopped in the previous step.

Update a computer that runs the SMS Provider

After you install an update bundle that includes updates for the SMS Provider, deploy
the update to each computer that runs the SMS Provider. The only exception is the
instance of the SMS Provider that was previously installed on the site server where you
install the update bundle. The local instance of the SMS Provider on the site server is
updated when you install the update bundle.

If you remove and then reinstall the SMS Provider on a computer, reinstall the update
for the SMS Provider on that computer.

Update clients
When you install an update that includes updates for the Configuration Manager client,
you can automatically upgrade clients with the update installation, or manually upgrade
clients at a later time. For more information about automatic client upgrade, see How to
upgrade clients for Windows computers.

You can deploy updates with Updates Publisher or a software deployment package. You
can also manually install the update on each client. For more information about how to
use deployments to install updates, see Deploy updates for Configuration Manager.

  ） Important

  When you install updates for clients and the update bundle includes updates for
  servers, install the server updates on the primary site to which the clients are
  assigned.

To manually install the client update, run Msiexec.exe on each Configuration Manager
client. Include the platform-specific client update MSP file in the command line. For
example, you can use the following command line for a client update:

msiexec.exe /p \\<ServerName>\SMS_<SiteCode>\Hotfix\<KB Number>\Client\<Platform>\
<msp> /L\*v <logfile> REINSTALLMODE=mous REINSTALL=ALL

<!-- p.1672 -->

Update Configuration Manager consoles
To update a Configuration Manager console, install the update on the computer that
runs the console.

  ） Important

  When you install updates for the Configuration Manager console, and the update
  bundle includes updates for servers, also install the server updates on the site that
  you use with the Configuration Manager console.

If the computer that you update runs the Configuration Manager client:

     You can use a deployment to install the update. For more information about how
     to use deployments to install updates, see Deploy updates for Configuration
     Manager.

     If you're signed in to the client computer, run the installation interactively.

To manually install the Configuration Manager console update, run Msiexec.exe. Include
the Configuration Manager console update MSP file in the command line. For example,
you can use the following command line to update a Configuration Manager console:

msiexec.exe /p \\<ServerName>\SMS_<SiteCode>\Hotfix\<KB Number>\AdminConsole\
<Platform>\<msp> /L\*v <logfile> REINSTALLMODE=mous REINSTALL=ALL

Deploy updates for Configuration Manager
After you install the update bundle on a site server, you can use one of the following
three methods to deploy updates to other computers.

Use Updates Publisher to install updates
When you install the update bundle on a site server, the installation Wizard creates a
catalog file for Updates Publisher. You can use this file to deploy the updates to
applicable computers. The wizard always creates this catalog, even when you select the
option Use package and program to deploy this update.

The catalog for Updates Publisher is named SCUPCatalog.cab. It's in the following
location on the computer where you ran the update bundle: \\
<ServerName>\SMS_<SiteCode>\Hotfix\<KB Number>\SCUP\SCUPCatalog.cab

<!-- p.1673 -->

  ） Important

  The SCUPCatalog.cab file is created by using paths that are specific to the site
  server where the update bundle is installed. It can't be used on other site servers.

After the wizard is finished, import the catalog to Updates Publisher. Then use software
updates to deploy the updates. For more information, see System Center Updates
Publisher.

Import the updates to Updates Publisher
   1. Start the Updates Publisher console and select Import.

   2. On the Import Type page of the Import Software Updates Catalog Wizard, select
     Specify the path to the catalog to import. Then specify the SCUPCatalog.cab file.

   3. Select Next, and then select Next again.

   4. In the Security Warning - Catalog Validation window, select Accept. Close the
     wizard after it's finished.

   5. Select the update that you want to deploy, and then select Publish.

   6. On the Publish Options page of the Publish Software Updates Wizard, select Full
     Content, and then select Next.

   7. Complete the wizard to publish the updates.

Use software deployment to install updates
When you install the update bundle on the site server of a primary site or CAS, you can
configure the installation Wizard to create update packages for software deployment.
Then deploy each package to a collection of computers that you want to update.

To create a software deployment package, on the Configure Software Update
Deployment page of the wizard, select each update package type that you want to
update. The available types can include servers, Configuration Manager consoles, and
clients. A separate package is created for each type of update that you select.

  ７ Note

  The package for servers contains updates for the following components:

<!-- p.1674 -->

         Site server
         SMS Provider
         Site database

Next, on the Configure Software Update Deployment Method page of the wizard,
select the option I will use software distribution.

After the wizard is finished, view the packages in the Configuration Manager console. Go
to the Packages node in the Software Library workspace. Use your standard process to
deploy software packages to Configuration Manager clients. When a package runs on a
client, it installs the updates to the applicable components of Configuration Manager on
the client computer.

For more information about how to deploy packages to Configuration Manager clients,
see Packages and programs.

Create collections for deploying updates to Configuration
Manager
You can deploy specific updates to applicable clients. The following information can help
you to create device collections for the different components for Configuration
Manager.

                                                                                   ﾉ   Expand table

 Component of               Instructions
 Configuration
 Manager

 CAS server                 Create a direct membership query and add the CAS server.

 All primary site servers   Create a direct membership query and add each primary site server.

 All secondary site         Create a direct membership query and add each secondary site server.
 servers

 All x86 clients            Create a collection with the following query criteria: Select * from
                            SMS_R_System inner join SMS_G_System_SYSTEM on
                            SMS_G_System_SYSTEM.ResourceID = SMS_R_System.ResourceId where
                            SMS_G_System_SYSTEM.SystemType = "X86-based PC"

 All x64 clients            Create a collection with the following query criteria: Select * from
                            SMS_R_System inner join SMS_G_System_SYSTEM on

<!-- p.1675 -->

 Component of               Instructions
 Configuration
 Manager

                            SMS_G_System_SYSTEM.ResourceID = SMS_R_System.ResourceId where
                            SMS_G_System_SYSTEM.SystemType = "X64-based PC"

 All computers that run     Create a direct membership query and add each computer.
 the Configuration
 Manager console

 Remote computers that      Create a direct membership query and add each computer.
 run an instance of the
 SMS Provider

  ７ Note

  To update a site database, deploy the update to the site server for that site.

For more information, see How to create collections.

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.1676 -->

Checklist for installing update 2603 for
Configuration Manager
Applies to: Configuration Manager (current branch)

When you use the current branch of Configuration Manager, you can install the in-console
update for version 2603 to update your hierarchy from a previous version.

To get the update for version 2603, you must use a service connection point at the top-level site
of your hierarchy. This site system role can be in online or offline mode. To download the update
when your service connection point is offline, use the service connection tool.

After your hierarchy downloads the update package from Microsoft, find it in the console. In the
Administration workspace, select the Updates and Servicing node.

     When the update is listed as Available, the update is ready to install. Before installing
     version 2603, review the following information about installing update 2603 and the pre-
     update checklist for configurations to make before starting the update.

     If the update displays as Downloading and doesn't change, review the hman.log and
     dmpdownloader.log for errors.

        The dmpdownloader.log can indicate that the dmpdownloader process is waiting for an
        interval before checking for updates. To restart the download of the update's
        redistribution files, restart the SMS_Executive service on the site server.

        Another common download issue occurs when proxy server settings prevent downloads
        from required internet endpoints.

For more information about installing updates, see In-console updates and servicing.

For more information about current branch versions, see Baseline and update versions.

About installing update 2603
Sites
Install update 2603 at the top-level site of your hierarchy. Start the installation from your central
administration site (CAS) or from your stand-alone primary site. After the update is installed at

<!-- p.1677 -->

the top-level site, child sites have the following update behavior:

     Child primary sites install the update automatically after the CAS finishes the installation of
     the update. You can use service windows to control when a site installs the update. For more
     information, see Service windows for site servers.

     Secondary sites are manually updated from within the Configuration Manager console after
     the primary parent site finishes the update installation. Automatic update of secondary site
     servers isn't supported.

Site system roles
When a site server installs the update, it automatically updates all of the site system roles. These
roles are on the site server or installed on remote servers. Before installing the update, make sure
that each site system server meets the current prerequisites for the new update version.

Configuration Manager consoles
The first time you use a Configuration Manager console after finishing the installation, you're
prompted to update that console. You can also run the Configuration Manager setup on the
computer that hosts the console, and choose the option to update the console. Install the update
to the console as soon as possible. For more information, see Install the Configuration Manager
console.

  ） Important

  When you install an update at the CAS, be aware of the following limitations and delays that
  exist until all child primary sites also complete the update installation:

        Client upgrades don't start, including automatic updates of clients and pre-production
        clients. Additionally, you can't promote pre-production clients to production until the
        last site completes the update installation. After the last site completes the update
        installation, client updates begin based on your configuration choices.
        New features you enable with the update aren't available. This behavior is to prevent
        the CAS replicating data related to that feature to a site that hasn't installed support
        for that feature yet. After all primary sites install the update, the feature is available for
        use.
        Replication links between the CAS and child primary sites display as not upgraded.
        This state displays in the update installation status as Completed with warning for

<!-- p.1678 -->

        monitoring replication initialization. In the Monitoring workspace of the console, this
        state displays as Link is being configured.

Early update ring
As of May 27, 2026, version 2603 is globally available for all customers to install.

Pre-update checklist
All sites run a supported version of Configuration Manager
Each site server in the hierarchy must run the same version of Configuration Manager before you
can start the installation. To update to version 2603, use version 2409 or later.

Review the status of your product licensing
You need an active Software Assurance (SA) agreement or equivalent subscription rights to install
this update. When you update the site, the Licensing page presents the option to confirm your
Software Assurance expiration date.

This value is optional. You can specify as a convenient reminder of your license expiration date.
This date is visible when you install future updates. You might have specified this value during a
previous setup or installation of an update. You can also specify this value in the Configuration
Manager console. In the Administration workspace, expand Site Configuration, and select Sites.
Select Hierarchy Settings in the ribbon, and switch to the Licensing tab.

For more information, see Licensing and branches.

Review Microsoft .NET versions
Configuration Manager now requires Microsoft .NET Framework version 4.8 for site servers,
specific site systems, and the console. Before you run setup to install or update the site, first
update .NET and restart the system. If possible in your environment, install the latest version of
.NET version 4.8 on all site systems.

This installation can put the site system server into a reboot pending state and report errors to
the Configuration Manager component status viewer. .NET applications on the server might
experience random failures until you restart the server.

For more information including how to manage restarts, see Site and site system prerequisites.

<!-- p.1679 -->

Review the version of the Windows ADK
The version of the Windows Assessment and Deployment Kit (ADK) should be supported for
Configuration Manager version 2603. For more information, see Support for the Windows ADK. If
you need to update the Windows ADK, do so before you begin the update of Configuration
Manager. This order makes sure the default boot images are automatically updated to the latest
version of Windows PE. Manually update any custom boot images after updating the site.

If you update the site before you update the Windows ADK, see Update distribution points with
the boot image.

Review SQL ODBC driver for CM
Starting with version 2309 and later, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a new site or
update an existing one.

Review the site and hierarchy status for unresolved issues
A site update can fail because of existing operational problems. Before you update a site, resolve
all operational issues for the following systems:

     The site server
     The site database server
     Remote site system roles on other servers

For more information, see Use the status system.

Review file and data replication between sites
Make sure that file and database replication between sites is operational and current. Delays or
backlogs in either can prevent a successful update.

Database replication

For database replication, to help resolve issues before you start the update, use the Replication
Link Analyzer (RLA). For more information, see Monitor database replication.

Use RLA to answer the following questions:

     Is replication per group in a good state?

<!-- p.1680 -->

     Are any links degraded?
     Are there any errors?

If there's a backlog, wait until it clears out. If the backlog is large, such as millions of records, then
the link is in a bad state. Before updating the site, solve the replication issue. If you need further
assistance, contact Microsoft Support.

File-based replication

For file-based replication, check all inboxes for a backlog on both sending and receiving sites. If
there are lots of stuck or pending replication jobs, wait until they clear out.

     On the sending site, review sender.log.
     On the receiving site, review despooler log.

Install all applicable critical Windows updates
Before you install an update for Configuration Manager, install any critical OS updates for each
applicable site system. These servers include the site server, site database server, and remote site
system roles. If an update that you install requires a restart, restart the applicable servers before
you start the upgrade.

Disable database replicas for management points at
primary sites
Configuration Manager can't successfully update a primary site that has a database replica for
management points enabled. Before you install an update for Configuration Manager, disable
database replication.

For more information, see Database replicas for management points.

Set SQL Server Always On availability groups to manual failover
If you use an availability group, make sure that the availability group is set to manual failover
before you start the update installation. After the site is updated, you can restore failover to be
automatic. For more information, see Prepare to use an availability group.

Disable site maintenance tasks at each site
Before you install the update, disable any site maintenance task that might run during the time
the update process is active. For example, but not limited to:
