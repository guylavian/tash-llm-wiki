---
title: "App management documentation — pages 81-120"
type: reference
domain: sccm
slug: sccm-intune-configmgr-apps-p0081-0120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-apps-p0081-0120
family: sccm
documentKind: "doc"
abstract: "Users can't install required software from Software Center. Users can't change their business hours in the Options tab of Software Center. Users can't postpone the installation of a required application. In addition, low-rights users can't sign in during a maintenance period if"
---

# App management documentation — pages 81-120

<!-- p.81 -->

     Users can't install required software from Software Center.

     Users can't change their business hours in the Options tab of Software Center.

     Users can't postpone the installation of a required application.

In addition, low-rights users can't sign in during a maintenance period if Configuration
Manager is committing changes for software installations and updates. During this
period, users see a message informing them that the device is unavailable because it's
being serviced.

Do not deploy applications to Windows Embedded devices that have write filters
enabled if the applications require the user to accept the license terms. When write
filters are disabled so that Configuration Manager can install software on embedded
devices, low-rights users can't sign in to the device. If the installation requires the user
to accept the license terms, this won't be possible and the installation will fail. Make sure
that you don't deploy software to Windows Embedded devices if the installation
requires user interaction. You can use the Applicable Platforms list to filter these
operating systems.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.82 -->

How to create global conditions in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

In Configuration Manager, global conditions are rules that represent business or
technical conditions that you can use to specify how an application is provided and
deployed to client devices. Global conditions are accessed from the Requirements page
of the Create Deployment Type Wizard.

  ７ Note

  You can edit global conditions only from the site where they were created.

Use the following procedures to create Configuration Manager global conditions.

Provide basic information about the global
condition
Several different types of global conditions are available. Different options are
associated with the different global condition types. When you select a specific global
condition type, Configuration Manager shows the options that apply to your selection.

   1. In the Configuration Manager console, choose Software Library > Application
      Management > Global Conditions.

   2. On the Home tab, in the Create group, choose Create Global Condition.

   3. In the Create Global Condition dialog box, provide a name and an optional
      description for the global condition.

   4. In the Device type drop-down list, choose whether the global condition is for a
      Windows computer or a Windows Mobile device.

   5. In the Condition Type drop-down list, choose one of the following options:

            Setting – This option checks for the existence of one or more items on client
            devices. For example, you can check that a file, folder, or registry key value
            exists on a client device.

<!-- p.83 -->

           Expression – This option lets you to set up more complex rules to check if the
           condition is satisfied on client devices. For example, you can check if the
           physical memory on a computer is between 2 GB and 4 GB or if a mobile
           device uses touch screen input.

Set up rules for the global condition
The procedure to define the global condition rules is different depending on whether
you are configuring a setting or an expression. Use the applicable procedure here to set
up a setting or an expression for the global condition.

To set up a setting for the global condition
   1. In the Condition Type drop-down list, choose Setting.

   2. In the Setting type drop-down list, choose the item to use as the condition for
     which requirements will be checked. The following setting types and
     configurations are available.

           Active Directory query

             LDAP prefix - Specify a valid LDAP prefix to the Active Directory Domain
             Services query to assess compliance on client computers. You can use
             either LDAP:// or GC://.

             Distinguished name (DN) - Specify the distinguished name of the Active
             Directory Domain Services object that will be assessed for compliance on
             client computers.

             Search filter - Specify an optional LDAP filter to refine the results from the
             Active Directory Domain Services query to assess compliance on client
             computers.

             Search scope - Specify the search scope in Active Directory Domain
             Services:

                Base - Queries only the specified object.

                One Level - This option is not used in this version of Configuration
                Manager.

                Subtree - Queries the specified object and its complete subtree in the
                directory.

<!-- p.84 -->

  Property - Specify the property of the Active Directory Domain Services
  object that will be used to assess compliance on client computers.

  Query - Shows the LDAP query that is constructed from the entries in
  LDAP prefix, Distinguished name (DN), Search Filter if specified, and
  Property. This query will be used to assess compliance on client
  computers.

Assembly
  Assembly name - Specifies the name of the assembly object to search for.
  The name cannot be the same as any other assembly object of the same
  type, and the name must be registered in the Global Assembly Cache. The
  assembly name can be a maximum of 256 characters.

  ７ Note

  An assembly is a piece of code that can be shared between applications.
  Assemblies can have the .dll or .exe file name extension. The Global
  Assembly Cache is a folder named %systemroot%\assembly on client
  computers in which all shared assemblies are stored.

File system

  Type – From the drop-down list, choose whether you want to search for a
  File or a Folder.

  Path - Specify the path to the specified file or folder on client computers.
  You can specify system environment variables and the %USERPROFILE%
  environment variable in the path.

     ７ Note

     If you use the %USERPROFILE% environment variable in the Path or
     File or folder name fields, all user profiles on the client computer will
     be searched. This could result in the discovery of multiple instances of
     the file or folder.

  File or folder name - Specify the name of the file or folder object that will
  be searched for. You can specify system environment variables and the
  %USERPROFILE% environment variable in the file or folder name. You can
  also use the * and ? wildcards in the file name.

<!-- p.85 -->

     ７ Note

     If you specify a file or folder name and use wildcards, this might
     produce a high numbers of results. This could result in high resource
     use on the client computer and high network traffic when reporting
     results to Configuration Manager.

  Include subfolders – Enable this option if you also want to search any
  subfolders under the specified path.

  This file or folder is associated with a 64-bit application - Choose
  whether the 64-bit system file location (%windir%\system32) should be
  searched in addition to the 32-bit system file location
  (%windir%\syswow64) on Configuration Manager clients that run a 64-bit
  version of Windows.

     ７ Note

     If the same file or folder exists in both the 64-bit and 32-bit system
     file locations on the same 64-bit computer, multiple files will be
     discovered by the global condition.

  The File system setting type does not support specifying a UNC path to a
  network share in the Path field.

IIS metabase

  Metabase path - Specify a valid path to the IIS Metabase.

  Property ID - Specify the numeric property of the IIS Metabase setting.

Registry key

  Hive – From the drop-down list, choose the registry hive that you want to
  search in.

  Key - Specify the registry key name that you want to search for. The
  format used should be key\subkey.

  This registry key is associated with a 64-bit application - Specifies
  whether the 64-bit registry keys should be searched in addition to the 32-
  bit registry keys on clients that run a 64-bit version of Windows.

<!-- p.86 -->

     ７ Note

     If the same registry key exists in both the 64-bit and 32-bit registry
     locations on the same 64-bit computer, both registry keys will be
     discovered by the global condition.

Registry value

  Hive - From the drop-down list, select the registry hive that you want to
  search in.

  Key - Specify the registry key name that you want to search for. The
  format used should be key\subkey.

  Value – Specify the value that must be contained within the specified
  registry key.

  This registry key is associated with a 64-bit application - Specifies
  whether the 64-bit registry keys should be searched in addition to the 32-
  bit registry keys on clients that run a 64-bit version of Windows.

     ７ Note

     If the same registry key exists in both the 64-bit and 32-bit registry
     locations on the same 64-bit computer, both registry keys will be
     discovered by the global condition.

Script

  Discovery script – Choose Add to enter, or browse to the script to use.
  You can use Windows PowerShell, VBScript, or JScript scripts.

  Run scripts by using the logged on user credentials – If you enable this
  option, the script will run on client computers by using the credentials of
  the user who is signed in.

     ７ Note

     The value returned by the script will be used to assess the compliance
     of the global condition. For example, when you use VBScript, you
     could use the WScript.Echo Result command to return the Result
     variable value to the global condition.

<!-- p.87 -->

    If your script returns multiple values, these values must be on a single
    line and separated with a semi-colon. If each value is on a separate
    line, the evaluation will fail.

SQL query

  SQL Server instance – Choose whether you want the SQL query to run on
  the default instance, all instances, or a specified database instance name.

    ７ Note

    The instance name must refer to a local instance of SQL Server. To
    refer to a SQL Server Always On failover cluster instance or availability
    group, you should use a script setting.

  Database - Specify the name of the Microsoft SQL Server database for
  which the SQL query will be run.

  Column - Specify the column name returned by the Transact-SQL
  statement to use to assess the compliance of the global condition.

  Transact-SQL statement – Specify the full SQL query to use for the global
  condition. You can also choose Open to open an existing SQL query.

WQL query

  Namespace - Specify the WMI namespace that will be used to build a
  WQL query that will be assessed for compliance on client computers. The
  default value is Root\cimv2.

  Class - Specifies the WMI class that will be used to build a WQL query that
  will be assessed for compliance on client computers.

  Property - Specifies the WMI property that will be used to build a WQL
  query that will be assessed for compliance on client computers.

  WQL query WHERE clause - You can use the WQL query WHERE clause
  item to specify a WHERE clause to be applied to the specified namespace,
  class, and property on client computers.

XPath query

  Path - Specify the path to the XML file on client computers that will be
  used to assess compliance. Configuration Manager supports the use of all

<!-- p.88 -->

           Windows system environment variables and the %USERPROFILE% user
           variable in the path name.

           XML file name - Specify the file name that contains the XML query to use
           to assess compliance on client computers.

           Include subfolders - Enable this option if you also want to search any
           subfolders under the specified path.

           This file is associated with a 64-bit application - Choose whether the 64-
           bit system file location (%windir%\system32) should be searched in
           addition to the 32-bit system file location (%windir%\syswow64) on
           Configuration Manager clients that run a 64-bit version of Windows.

           XPath query - Specify a valid full XML path language (XPath) query to use
           to assess compliance on client computers.

           Namespaces - Opens the XML Namespaces dialog box to identify
           namespaces and prefixes to use during the XPath query.

 3. In the Data type drop-down list, choose the format in which data will be returned
   by the condition before it is used to check requirements.

     ７ Note

     The Data type drop-down list is not shown for all setting types.

 4. Set up further details about this setting below the Setting type drop-down list. The
   items you can set up will vary depending on the setting type you have selected.

 5. Choose OK to save the rule and to close the Create Global Condition dialog box.

Set up an expression for the global condition
 1. In the Condition Type drop-down list, choose Expression.

 2. Choose Add Clause to open the Add Clause dialog box.

 3. From the Select category drop-down list, select whether this expression is for a
   device or a user. Alternatively, select Custom to use a previously configured global
   condition.

 4. From the Select a condition drop-down list, select the condition to use to assess
   whether the user or device meets the rule requirements. The contents of this list

<!-- p.89 -->

     will vary depending on the selected category.

   5. From the Choose operator drop-down list, choose the operator that will be used
     to compare the selected condition to the specified value to assess whether the
     user or device meets the rule requirements. The available operators will vary
     depending on the selected condition.

   6. In the Value field, specify the values that will be used with the selected condition
     and operator to assess whether the user or device meets the rule requirements.
     The available values will vary depending on the selected condition and the
     selected operator.

   7. Choose OK to save the expression and to close the Add Clause dialog box.

   8. When you have finished adding clauses to the global condition, choose OK to
     close the Create Global Condition dialog box and to save the global condition.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.90 -->

Create application groups
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

Create a group of applications that you can send to a user or device collection as a
single deployment. The metadata you specify about the app group is seen in Software
Center as a single entity. You can order the apps in the group so that the client installs
them in a specific order.

   Tip

  This feature was first introduced in version 1906 as a pre-release feature. Beginning
  with version 2111, it's no longer a pre-release feature.

  This feature is optional in Configuration Manager, and enabled by default. For more
  information, see Enable optional features from updates.

Process
   1. In the Configuration Manager console, go to the Software Library workspace.
      Expand Application Management and select the Application Group node.

   2. In the Create group in the ribbon, select Create Application Group.

   3. On the General Information page, specify information about the app group.

   4. On the Software Center page, include information that shows in Software Center.

   5. On the Application Group page, select Add. Select one or more apps for this
      group. Reorder them using the Move Up and Move Down actions.

   6. Complete the wizard.

   Tip

  To manage app groups, you need permissions on the Application Groups object.
  The permissions for most administrative operations are the same as on
  applications.

<!-- p.91 -->

Deploy
Deploy the app group using the same process as for an application. For more
information, see Deploy applications. You can deploy an app group to device or user
collections. Starting in version 2111, when you deploy an app group as required to a
device or user collection, you can specify that it automatically uninstalls when the
resource is removed from the collection. For more information, see Implicit uninstall.

After you deploy the group:

     If you add a new app to the group, you have to separately distribute the new app
     content to distribution points.

     If you modify an app in the app group, redistribute the content.

To troubleshoot an app group deployment, use the following log files on the client:

     AppGroupHandler.log
     AppEnforce.log
     SettingsAgent.log

App approval
Starting in version 2111, you can use the following app approval behaviors:

     Deploy an app group to a user collection and require approval.
        A user can then request the app group in Software Center.
        You can approve or deny the user's request for the app group.

     Deploy an app group to a device collection and require approval. The deployment
     is suspended on the device until you trigger installation via automation. For
     example, use the Approve-CMApprovalRequest PowerShell cmdlet.

     From the Configuration Manager console, when you select a device, there's a new
     action in the Device group of the ribbon to Install Application Group. For more
     information, see Install applications for a device.

     When you enable tenant attach, you can view status and take actions on app
     groups from the Microsoft Intune admin center. For more information, see Install
     an application from the admin center.

Known issues

<!-- p.92 -->

     The following deployment options may not work: alerts, phased deployment,
     repair.
     You can't use application groups with the Install Application task sequence step.
     You can't export or import app groups.
     In version 2103 and earlier, don't include in the group any apps that require restart,
     or the group deployment may fail.
     In version 2107 and earlier, if you delete an app that's a part of an app group,
     you'll see the following warning when you next view the properties of the app
     group: "Unable to load information about all applications in the group." Make a
     small change to the app group and save it. For example, add a space to the
     Administrator comments. When you save the change, it removes the deleted app
     from the group. Starting in version 2111, you can't delete an app that's part of an
     app group.
     In most scenarios, user categories on the app group don't display as filters in
     Software Center. If the app group is deployed as available to a user collection, the
     categories display.

PowerShell
You can create and deploy app groups using Windows PowerShell. For more
information, see the following cmdlet articles:

     Get-CMApplicationGroup
     New-CMApplicationGroup
     Remove-CMApplicationGroup
     Set-CMApplicationGroup
     Get-CMApplicationGroupDeployment
     New-CMApplicationGroupDeployment
     Remove-CMApplicationGroupDeployment
     Set-CMApplicationGroupDeployment

Next steps
Deploy applications

Feedback
Was this page helpful?    Yes    No

<!-- p.93 -->

Provide product feedback

<!-- p.94 -->

Packages and programs in Configuration
Manager
Applies to: Configuration Manager (current branch)

Configuration Manager continues to support packages and programs that were used in
Configuration Manager 2007. A deployment that uses packages and programs might be more
suitable than an application when you deploy any of the following tools or scripts:

     Administrative tools that don't install an application on a computer
     "One-off" scripts that don't need to be continually monitored
     Scripts that run on a recurring schedule and can't use global evaluation

   Tip

  Consider using the Scripts feature in the Configuration Manager console. Scripts may be a
  better solution for some of the preceding scenarios instead of using packages and
  programs.

When you migrate packages from an earlier version of Configuration Manager, you can deploy
them in your Configuration Manager hierarchy. After migration is complete, the packages appear
in the Packages node in the Software Library workspace.

You can modify and deploy these packages in the same way you did by using software
distribution. The Import Package from Definition Wizard remains in Configuration Manager to
import legacy packages. Advertisements are converted to deployments when you migrate from
Configuration Manager 2007 to a Configuration Manager hierarchy.

  ７ Note

  Use Package Conversion Manager to convert packages and programs into Configuration
  Manager applications. Package Conversion Manager is integrated with Configuration
  Manager. For more information, see Package Conversion Manager.

Packages can use some new features of Configuration Manager, including distribution point
groups and monitoring. You can't deploy Microsoft Application Virtualization (App-V)

<!-- p.95 -->

applications with packages and programs in Configuration Manager. To distribute virtual
applications, create them as Configuration Manager applications. For more information, see
Deploy App-V virtual applications.

Create a package and program
Use the Create Package and Program wizard
   1. In the Configuration Manager console, go to the Software Library workspace, expand
     Application Management, and select the Packages node.

   2. In the Home tab of the ribbon, in the Create group, choose Create Package.

   3. On the Package page of the Create Package and Program Wizard, specify the following
     information:

          Name: Specify a name for the package with a maximum of 50 characters.

          Description: Specify a description for this package with a maximum of 128 characters.

          Manufacturer (optional): Specify a manufacturer name to help you identify the
          package in the Configuration Manager console. This name can be a maximum of 32
          characters.

          Language (optional): Specify the language version of the package with a maximum of
          32 characters.

          Version (optional): Specify a version number for the package with a maximum of 32
          characters.

          This package contains source files: This setting indicates whether the package
          requires source files to be present on client devices. By default, the wizard doesn't
          enable this option, and Configuration Manager doesn't use distribution points for the
          package. When you select this option, specify the package content to distribute to
          distribution points.

          Source folder: If the package contains source files, choose Browse to open the Set
          Source Folder dialog box, and then specify the location of the source files for the
          package.

             ７ Note

<!-- p.96 -->

             The computer account of the site server must have read access permissions to the
             source folder that you specify.

             Windows limits the source path to 256 characters or less. This limit applies to
             package source as well as applications. For more information, see Naming Files,
             Paths, and Namespaces.

           If you want to pre-cache content on a client, specify the Architecture and Language of
           the package. For more information, see Configure pre-cache content.

   4. On the Program Type page of the Create Package and Program Wizard, select the
     Standard program type for computers. Or you can skip this step and create a program later.

         Tip

        To create a new program for an existing package, first select the package. Then, in the
        Home tab, in the Package group, choose Create Program to open the Create Program
        Wizard.

        The Program for device type is a legacy option that only applies to mobile devices,
        which aren't currently managed by Configuration Manager.

Custom icons for packages

Starting in version 2203, add custom icons for packages. These icons appear in Software Center
when you deploy the package and program. Instead of a default icon, a custom icon can improve
the user experience to better identify the software.

On the General tab of package properties, in the section for the icon, select Browse. Select an
icon from the default shell library, or browse to another file in a local or network path.

     It supports the following file types:
        Programs ( .exe )
        Libraries ( .dll )
        Icons ( .ico )
        Images ( .png , .jpeg , .jpg )
     The file doesn't need to be on clients that you target with the deployment. Configuration
     Manager includes the image with the deployment policy.
     The maximum file size for an image is 256 KB.

<!-- p.97 -->

     Icons can have pixel dimensions of up to 512 x 512.

When clients receive the deployment policy, they'll display the icon in Software Center.

  ７ Note

  To take full advantage of new Configuration Manager features, after you update the site,
  also update clients to the latest version. While new functionality appears in the
  Configuration Manager console when you update the site and console, the complete
  scenario isn't functional until the client version is also the latest.

Create a program
   1. On the Program Type page of the Create Package and Program Wizard, choose Standard
     Program, and then choose Next.

   2. On the Standard Program page, specify the following information:

           Name: Specify a name for the program with a maximum of 50 characters.

             ７ Note

             The program name must be unique within a package. After you create a program,
             you can't modify its name.

           Command Line: Enter the command line to use to start this program, or choose
           Browse to browse to the file location.

           If you don't specify an extension for a file name, Configuration Manager attempts to
           use .com, .exe, and .bat as possible extensions.

           When the client runs the program, Configuration Manager searches for the file in the
           following locations:
              Within the package
              The local Windows folder
              The local %path%

           If it can't find the file, the program fails.

             ） Important

<!-- p.98 -->

  On a 64-bit client, the command line always runs as a 32-bit process in the
  WOW64 (Windows 32-bit On Windows 64-bit) subsystem. As a result, WOW64
  redirects the process's file system and registry access. For example, a script that
  writes files to %ProgramFiles% is redirected to %ProgramFiles(x86)% , and registry
  writes to HKEY_LOCAL_MACHINE\Software are redirected to
  HKEY_LOCAL_MACHINE\Software\WOW6432Node . To bypass file system redirection and

  run a 64-bit process, WOW64 recognizes %windir%\Sysnative as a special alias for
  %windir%\System32 . For example, to run the 64-bit version of cmd.exe , use the

  following command line: %windir%\Sysnative\cmd.exe . For more information, see
  File System Redirector and Registry Redirector.

Startup folder (optional): Specify the folder from which the program runs, up to 127
characters. This folder can be an absolute path on the client. It can also be a path
that's relative to the distribution point folder that contains the package.

Run: Specify the mode in which the program runs on client computers. Select one of
the following options:

  Normal: The program runs in the normal mode based on system and program
  defaults. This mode is the default.

  Minimized: The program runs minimized on client devices. Users might see
  installation activity in the notification area or on the taskbar.

  Maximized: The program runs maximized on client devices. Users see all installation
  activity.

  Hidden: The program runs hidden on client devices. Users don't see any installation
  activity.

Program can run: Specify whether the program runs only when a user is signed in,
only when no user is signed in, or regardless of whether a user is signed in to the
client computer.

Run mode: Specify whether the program runs with administrative permissions or with
the permissions of the user who's currently signed in.

Allow users to view and interact with the program installation: Use this setting, if
available, to specify whether to allow users to interact with the program installation.
This option is only available if the following conditions are met:

<!-- p.99 -->

          Program can run setting is Only when a user is logged on or Whether or not a
          user is logged on
          Run mode setting is to Run with administrative rights

       Drive mode: Specify information about how this program runs on the network. Choose
       one of the following options:

          Runs with UNC name: Specify that the program runs with a Universal Naming
          Convention (UNC) name. This setting is the default.

          Requires drive letter: Specify that the program requires a drive letter to fully qualify
          its location. For this setting, Configuration Manager can use any available drive
          letter on the client. This setting requires the deployment to use the Deployment
          option Run program from distribution point and the package's Data Access option
          enabled to Copy the content in this package to a package share on distribution
          points.

          Requires specific drive letter: Specify that the program requires a specific drive
          letter that you specify to fully qualify its location. For example, Z:. If the client is
          already using the specified drive letter, the program doesn't run. This setting
          requires the deployment to use the Deployment option Run program from
          distribution point and the package's Data Access option enabled to Copy the
          content in this package to a package share on distribution points.

       Reconnect to distribution point at log on: Indicate whether the client reconnects to
       the distribution point when the user signs in. By default, the wizard doesn't enable this
       option.

3. On the Requirements page of the Create Package and Program Wizard, specify the
  following information:

       Run another program first: Identify a package and program that runs before this
       package and program runs.

       Platform requirements: Select This program can run on any platform or This
       program can run only on specified platforms. Then choose the OS versions that
       clients must have to install this package and program.

         ７ Note

<!-- p.100 -->

          When you run a task sequence from boot media or PXE, Configuration Manager
          ignores this option. The task sequence runs as though the option This program
          can run on any platform is selected.

        Estimated disk space: Specify the amount of disk space that the program requires to
        run on the computer. The default setting is Unknown. If necessary, specify a whole
        number greater than or equal to zero. If you set a value, also select units for the value.

        Maximum allowed run time (minutes): Specify the maximum time that you expect the
        program to run on the client computer. The default value is 120 minutes. Only use
        whole numbers greater than zero.

          ） Important

          If the targeted computers to which you deploy this program have a maintenance
          window, a conflict could occur if the Maximum allowed run time is longer than
          the scheduled maintenance window. If you set the maximum run time to
          Unknown, the program starts to run during the maintenance window. It then
          continues to run as needed after the maintenance window is closed. If you set the
          maximum run time to a specific period that's greater than the length of any
          available maintenance window, then the client doesn't run the program.

        If you set this value to Unknown, Configuration Manager sets the maximum allowed
        run time as 12 hours (720 minutes).

          ７ Note

          If the program exceeds the maximum run time, Configuration Manager stops it if
          the following conditions are met:
             You enable the option to Run with administrative rights
             You don't enable the option to Allow users to view and interact with the
             program installation

Deploy packages and programs
 1. In the Configuration Manager console, go to the Software Library workspace, expand
   Application Management, and select the Packages node.

<!-- p.101 -->

2. Select the package that you want to deploy. In the Home tab of the ribbon, in the
  Deployment group, choose Deploy.

3. On the General page of the Deploy Software Wizard, specify the name of the package and
  program that you want to deploy. Select the collection to which you want to deploy the
  package and program, and any optional comments.

  To store the package content on the collection's default distribution point group, select the
  option to Use default distribution point groups associated to this collection. If you didn't
  associate this collection with a distribution point group, this option is unavailable.

4. On the Content page, choose Add. Select the distribution points or distribution point
  groups to which you want to distribute the content for this package and program.

5. On the Deployment Settings page, configure the following settings:

       Purpose: Choose one of the following options:

          Available: The user sees the published package and program in Software Center
          and can install it on demand.

          Required: The package and program is deployed automatically, according to the
          configured schedule. In Software Center, you can track its deployment status and
          install it before the deadline.

          ７ Note

          If multiple users are signed in to the device, package and task sequence
          deployments appear in Software Center for the user in the active console session.
          If no user is in the active console session, the deployments appear for the user
          with the lowest connected interactive session ID. To view the session ID and type
          for each signed-in user, open Task Manager, select the Users tab, right-click a
          column header, and enable ID and Session. The Session column shows the
          Console for a local sign-in or an RDP session name for a remote connection. For
          more information, see Remote Desktop Sessions.

       Send wake-up packets: If you set the deployment purpose to Required and select this
       option, the site first sends a wake-up packet to computers at the installation deadline
       time. Before you can use this option, configure computers for Wake On LAN. For more
       information, see How to configure Wake on LAN.

<!-- p.102 -->

       Allow clients on a metered Internet connection to download content after the
       installation deadline, which might incur additional costs

    ７ Note

    When you deploy a package and program, the option to Pre-deploy software to the
    user's primary device isn't available.

6. On the Scheduling page, configure when to deploy this package and program to client
  devices.

  The options on this page vary depending on whether you set the deployment action to
  Available or Required.

  For Required deployments, configure the rerun behavior for the program from the Rerun
  behavior drop-down menu. Choose from the following options:

                                                                                         ﾉ   Expand table

   Rerun behavior       Description

   Never rerun          The client won't rerun the program. This behavior happens even if the program
   deployed program     originally failed or if the program files are changed.

   Always rerun         The client always reruns the program when the deployment is scheduled. This
   program              behavior happens even if the program has already successfully run. It's useful
                        with recurring deployments when you update the program.

   Rerun if failed      The client reruns the program when the deployment is scheduled, only if it
   previous attempt     failed on the previous run attempt.

   Rerun if succeeded   The client reruns the program only if it previously ran successfully on the client.
   on previous          This behavior is useful with recurring deployments when you routinely update
   attempt              the program, and each update requires the previous update to be successfully
                        installed.

7. On the User Experience page, specify the following information:

       Allow users to run the program independently of assignments: Users can install this
       software from Software Center regardless of any scheduled installation time.

       Software installation: Allows the software to be installed outside of any configured
       maintenance windows.

<!-- p.103 -->

       System restart (if required to complete the installation): If the software installation
       requires a device restart to finish, allow this action to happen outside of any
       configured maintenance windows.

       Embedded devices: When you deploy packages and programs to Windows Embedded
       devices that are write-filter-enabled, you can specify that they install packages and
       programs on the temporary overlay and commit changes later. Alternately, commit the
       changes on the installation deadline or during a maintenance window. When you
       commit changes on the installation deadline or during a maintenance window, a
       restart is required, and the changes persist on the device.

          ７ Note

          When you deploy a package or program to a Windows Embedded device, make
          sure that the device is a member of a collection that has a configured
          maintenance window. For more information about how maintenance windows are
          used when you deploy packages and programs to Windows Embedded devices,
          see Creating Windows Embedded applications.

8. On the Distribution Points page, specify the following information:

       Deployment options: Specify the action that a client when it uses a distribution point
       in its current boundary group. Also select the action for the client when it uses a
       distribution point from a neighbor boundary group or the default site boundary
       group.

          ） Important

          If you configure the deployment option to Run program from distribution point,
          make sure to enable the option to Copy the content in this package to a
          package share on distribution points on the Data Access tab of the package
          properties. Otherwise the package is unavailable to run from distribution points.

       Allow clients to use distribution points from the default site boundary group: When
       this content isn't available from any distribution point in the current or neighbor
       boundary groups, enable this option to let them try distribution points in the site
       default boundary group.

<!-- p.104 -->

   9. Complete the wizard.

View the deployment in the Deployments node of the Monitoring workspace and in the details
pane of the package deployment tab when you select the deployment. For more information, see
Monitor packages and programs.

Monitor packages and programs
To monitor package and program deployments, use the same procedures that you use to
monitor applications as detailed in Monitor applications.

Packages and programs also include a number of built-in reports, which enable you to monitor
information about the deployment status of packages and programs. These reports have the
report category of Software Distribution - Packages and Programs and Software Distribution -
Package and Program Deployment Status.

For more information about how to configure reporting in Configuration Manager, see
Introduction to reporting.

Manage packages and programs
In the Software Library workspace, expand Application Management, and select the Packages
node. Select the package that you want to manage, and then choose a management task.

Create Prestage Content File
Opens the Create Prestaged Content File Wizard, to create a file that contains the package
content. Use this file to manually import the package to a remote distribution point. This action is
useful when you have low network bandwidth between the site server and the distribution point.

Create Program
Opens the Create Program Wizard, to create a new program for this package.

Export
Opens the Export Package Wizard, to export the selected package and its content to a file. Use
this file to import the file to another hierarchy.

Deploy

<!-- p.105 -->

Opens the Deploy Software Wizard, to deploy the selected package and program to a collection.
For more information, see Deploy packages and programs.

Distribute content
Opens the Distribute Content Wizard, to send the content for a package and program to
selected distribution points or distribution point groups.

Import
Opens the Import Package Wizard, to import a previously exported package from a .zip file.

   Tip

  When you import an object in the Configuration Manager console, it imports to the current
  folder. In earlier versions, Configuration Manager always put imported objects in the root
  node.

Update distribution points
Updates distribution points with the latest content for the selected package and program.

Next steps
      Scripts

      Package Conversion Manager

      Package definition files

 Last updated on 07/18/2026

<!-- p.106 -->

Package definition files
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Package definition files are scripts to help you automate the creation of Packages and
programs in Configuration Manager. They provide all of the information that
Configuration Manager needs to create a package and program, except for the location
of package source files.

About the package definition file format
Each package definition file is an ASCII or UTF-8 text file that uses the .ini file format. It
contains the following sections:

[PDF]
This section identifies the file as a package definition file. It contains the following
information:

      Version: Specify the version of the package definition file format that the file uses.
      This version corresponds to the version of Configuration Manager for which it was
      written. This entry is required.

[Package Definition]
Specify the properties of the package and program. It provides the following
information:

      Name: The name of the package, up to 50 characters.

      Version (optional): The version of the package, up to 32 characters.

      Icon (optional): The file that contains the icon to use for this package. If specified,
      this icon replaces the default package icon in the Configuration Manager console.

      Publisher: The publisher of the package, up to 32 characters.

      Language: The language version of the package, up to 32 characters.

      Comment (optional): A comment about the package, up to 127 characters.

<!-- p.107 -->

     ContainsNoFiles: This entry indicates if the package has any source files.

     Programs: The programs that you define for this package. Each program name
     corresponds to a [Program] section in this package definition file.

     Example:

     Programs=Typical, Custom, Uninstall

     MIFFileName: The name of the Management Information Format (MIF) file that
     contains the package status, up to 50 characters.

     MIFName: The name of the package for MIF matching, up to 50 characters.

     MIFVersion: The version number of the package for MIF matching, up to 32
     characters.

     MIFPublisher: The software publisher of the package for MIF matching, up to 32
     characters.

[Program]
Include a [Program] section for each program that you specify in the Programs entry in
the [Package Definition] section. This section defines each program. Each program
section provides the following information:

     Name: The name of the program, up to 50 characters. This entry must be unique
     within a package.

     Icon (optional): Specify the file that contains the icon to use for this program. This
     icon replaces the default program icon in the Configuration Manager console. The
     client also displays this icon when you deploy the program to a collection.

     Comment (optional): A comment about the program, up to 127 characters.

     CommandLine: Specify the command line for the program, up to 127 characters.
     The command is relative to the package source folder.

     StartIn: Specify the working folder for the program, up to 127 characters. This
     entry can be an absolute path on the client computer or a path that's relative to
     the package source folder.

     Run: Specify the program mode in which the program runs. You can specify
     Minimized, Maximized, or Hidden. If you don't include this entry, the program
     runs in normal mode.

<!-- p.108 -->

AfterRunning: Specify any special action that occurs after the program successfully
completes. Options available are SMSRestart, ProgramRestart, or SMSLogoff. If
you don't include this entry, the program doesn't run a special action.

EstimatedDiskSpace: Specify the amount of disk space that the software program
requires to run on the computer. The default value is Unknown. You can set the
value as a whole number greater than or equal to zero. If you specify a value, also
include the units for the value.

Example:

EstimatedDiskSpace=38MB

EstimatedRunTime: Specify the estimated duration in minutes that you expect the
program to run on the client computer. The default value is 120. You can set the
value as a whole number greater than zero, or Unknown.

Example:

EstimatedRunTime=25

SupportedClients: Specify the processors and operating systems on which this
program runs. Separate the platforms by commas. If you don't include this entry,
the client doesn't check supported platforms for this program.

SupportedClientMinVersionX, SupportedClientMaxVersionX: Specify the
beginning-to-ending range for version numbers for the operating systems that are
specified in the SupportedClients entry.

Example:

  INI

  SupportedClients=Win NT (I386),Win NT (IA64),Win NT (x64)
  Win NT (I386) MinVersion1=5.00.2195.4
  Win NT (I386) MaxVersion1=5.00.2195.4
  Win NT (I386) MinVersion2=5.10.2600.2
  Win NT (I386) MaxVersion2=5.10.2600.2
  Win NT (I386) MinVersion3=5.20.0000.0
  Win NT (I386) MaxVersion3=5.20.9999.9999
  Win NT (I386) MinVersion4=5.20.3790.0
  Win NT (I386) MaxVersion4=5.20.3790.2
  Win NT (I386) MinVersion5=6.00.0000.0
  Win NT (I386) MaxVersion5=6.00.9999.9999
  Win NT (IA64) MinVersion1=5.20.0000.0
  Win NT (IA64) MaxVersion1=5.20.9999.9999
  Win NT (x64) MinVersion1=5.20.0000.0
  Win NT (x64) MaxVersion1=5.20.9999.9999

<!-- p.109 -->

  Win NT (x64) MinVersion2=5.20.3790.0
  Win NT (x64) MaxVersion2=5.20.9999.9999
  Win NT (x64) MinVersion3=5.20.3790.0
  Win NT (x64) MaxVersion3=5.20.3790.2
  Win NT (x64) MinVersion4=6.00.0000.0
  Win NT (x64) MaxVersion4=6.00.9999.9999

AdditionalProgramRequirements (optional): Provide any other information or
requirements for client computers, up to 127 characters.

CanRunWhen: Specify the user status that the program requires to run on the
client computer. Available values are UserLoggedOn, NoUserLoggedOn, or
AnyUserStatus. The default value is UserLoggedOn.

UserInputRequired: Specify whether the program requires interaction with the
user. Available values are True or False. The default value is True. This entry is set to
False if CanRunWhen isn't set to UserLoggedOn.

AdminRightsRequired: Specify whether the program requires administrative
credentials on the computer to run. Available values are True or False. The default
value is False. This entry is set to True if CanRunWhen isn't set to UserLoggedOn.

UseInstallAccount: Specify whether the program uses the client software
installation account when it runs on client computers. By default, this value is False.
This value is also False if CanRunWhen is set to UserLoggedOn.

DriveLetterConnection: Specify whether the program requires a drive letter
connection to the package files on the distribution point. You can specify True or
False. The default value is False, which enables the program to use a Universal
Naming Convention (UNC) connection. When this value is set to True, the client
uses the next available drive letter, starting with Z: and proceeding backwards.

SpecifyDrive (optional): Specify a drive letter that the program requires to connect
to the package files on the distribution point. This setting forces the use of the
specified drive letter for client connections to distribution points.

ReconnectDriveAtLogon: Specify whether the computer reconnects to the
distribution point when the user signs in. Available values are True or False. The
default value is False.

DependentProgram: Specify a program in this package that must run before the
current program. This entry uses the format DependentProgram=<ProgramName> ,
where <ProgramName> is the Name entry for that program in the package definition
file. If there are no dependent programs, leave this entry empty.

<!-- p.110 -->

    Examples:

     DependentProgram=Admin

     DependentProgram=

    Assignment: Specify how the program is assigned to users. This value can be:
       FirstUser: Only the first user who signs in to the client runs the program
       EveryUser: Every user who signs in runs the program

    When CanRunWhen isn't set to UserLoggedOn, this entry is set to FirstUser.

    Disabled: Specify whether you can deploy this program to clients. Available values
    are True or False. The default value is False.

Use a package definition file
  1. In the Configuration Manager console, go to the Software Library workspace,
    expand Application Management, and select the Packages node.

  2. On the Home tab of the ribbon, in the Create group, choose Create Package from
    Definition.

  3. On the Package Definition page of the Create Package from Definition Wizard,
    choose an existing package definition file. To open a new package definition file,
    choose Browse. After you specify a new package definition file, select it from the
    Package definition list.

  4. On the Source Files page, specify information about any required source files for
    the package and program.

  5. If the package requires source files, on the Source Folder page, specify the
    location from where the site can get the source files.

  6. Complete the wizard.

See also
Packages and programs

Feedback

<!-- p.111 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.112 -->

Deploy applications with Configuration
Manager
Article • 12/16/2024

Applies to: Configuration Manager (current branch)

Create or simulate a deployment of an application to a device or user collection in
Configuration Manager. This deployment gives instructions to the Configuration
Manager client on how and when to install or uninstall the software.

Before you can deploy an application, create at least one deployment type for the
application. For more information, see Create deployment types for the application.

In some situations, consider another feature as a better solution:

      If you have several applications that you need to deploy together, instead of
      creating multiple deployments, create an application group. You can send the app
      group to a user or device collection as a single deployment. For more information,
      see Create application groups.

      For more complex deployments, first test it with a simulated deployment. This
      simulation tests the applicability of a deployment without installing or uninstalling
      the application. A simulated deployment evaluates the detection method,
      requirements, and dependencies for a deployment type and reports the results in
      the Deployments node of the Monitoring workspace. For more information, see
      Simulate application deployments.

        ７ Note

        You can only simulate the deployment of required applications, but not
        packages or software updates.

        On-prem MDM-enrolled devices don't support simulated deployments, user
        experience, or scheduling settings.

      Phased deployments allow you to orchestrate a coordinated, sequenced rollout of
      software based on customizable criteria and groups. For example, deploy the
      application to a pilot collection, and then automatically continue the rollout based
      on success criteria. For more information, see Create a phased deployment.

<!-- p.113 -->

Start the deployment wizard
   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Application Management, and select either the Applications or
     Application Groups node.

   2. Select an application or application group from the list to deploy. In the ribbon,
     select Deploy.

  ７ Note

  When you view the properties of an existing deployment, the following sections
  correspond to tabs of the deployment properties window:

       General
       Content
       Deployment Settings
       Scheduling
       User Experience
       Alerts

General information
On the General page of the Deploy Software wizard, specify the following information:

     Software: This value displays the application to deploy. Select Browse to choose a
     different application.

     Collection: Select Browse to choose the target collection for this application
     deployment.

     Use default distribution point groups associated to this collection: Store the
     application content on the collection's default distribution point group. If you
     haven't associated the selected collection with a distribution point group, this
     option is grayed out.

     Automatically distribute content for dependencies: If any of the deployment
     types in the application have dependencies, then the site also sends dependent
     application content to distribution points.

       ７ Note

<!-- p.114 -->

        If you update the dependent application after deploying the primary
        application, the site doesn't automatically distribute any new content for the
        dependency.

     Comments (optional): Optionally, enter a description for this deployment.

Content options
On the Content page, select Add to distribute the content for this application to a
distribution point or a distribution point group.

If you selected the option to Use default distribution points associated to this
collection on the General page, then this option is automatically populated. Only a
member of the Application Administrator security role can modify it.

If the application content is already distributed, then they appear here.

Deployment settings
On the Deployment Settings page, specify the following information:

     Action: From the drop-down list, choose whether this deployment is to Install or
     Uninstall the application.

        ７ Note

        If you create a deployment to Install an app and another deployment to
        Uninstall the same app on the same device, the Install deployment takes
        priority.

     You can't change the action of a deployment after you create it.

     Purpose: From the drop-down list, choose one of the following options:

        Available: The user sees the application in Software Center. They can install it on
        demand.

           ７ Note

           When you deploy apps as available to user collections, there are other
           requirements for some types of clients. For more information, see

<!-- p.115 -->

     Prerequisites to deploy user-available apps.

   Required: The client automatically installs the app according to the schedule
   that you set. If the application isn't hidden, a user can track its deployment
   status. They can also use Software Center to install the application before the
   deadline.

     ７ Note

     When you set the deployment action to Uninstall, the deployment purpose
     is automatically set to Required. You can't change this behavior.

Allow end users to attempt to repair this application: If you created the
application with a repair command line, enable this option. Users see an option in
Software Center to Repair the application.

Uninstall this application if the targeted object falls out of the collection: Starting
in version 2107, when you remove the device from the target collection,
Configuration Manager runs the uninstall program on that device. For more
information, see Implicit uninstall. This option is only available for device-targeted
deployments and when the deployment is Required.

Pre-deploy software to the user's primary device: If the deployment is to a user,
select this option to deploy the application to the user's primary device. This
setting doesn't require the user to sign in before the deployment runs. If the user
must interact with the installation, don't select this option. This option is only
available when the deployment is Required.

Send wake-up packets: If the deployment is Required, Configuration Manager
sends a wake-up packet to computers before the client runs the deployment. This
packet wakes the computers at the installation deadline time. Before using this
option, computers and networks must be configured for Wake On LAN. For more
information, see Plan how to wake up clients.

Allow clients on a metered Internet connection to download content after the
installation deadline, which might incur additional costs: This option is only
available for deployments with a purpose of Required.

Automatically upgrade any superseded versions of this application: The client
upgrades any superseded version of the application with the superseding
application.

<!-- p.116 -->

        ７ Note

        This option works regardless of administrator approval. If an administrator
        already approved the superseded version, they don't need to also approve the
        superseding version. Approval is only for new requests, not superseding
        upgrades.

        For Available install purpose, you can enable or disable this option.

Approval settings
The application approval behavior depends upon whether you enable the
recommended optional feature, Approve application requests for users per device.

     An administrator must approve a request for this application on the device: If
     you enable the optional feature, the administrator approves any user requests for
     the application before the user can install it on the requested device. If the
     administrator approves the request, the user is only able to install the application
     on that device. The user must submit another request to install the application on
     another device. This option is grayed out when the deployment purpose is
     Required, or when you deploy the application to a device collection.

     Require administrator approval if users request this application: If you don't
     enable the optional feature, the administrator approves any user requests for the
     application before the user can install it. This option is grayed out when the
     deployment purpose is Required, or when you deploy the application to a device
     collection.

For more information, see Approve applications.

Deployment properties: Deployment settings
When you view the properties of a deployment, if supported by the deployment type
technology, the following option appears on the Deployment Settings tab:

Automatically close any running executables you specified on the install behavior tab
of the deployment type properties dialog box. For more information, see check for
running executable files before installing an application.

Scheduling settings

<!-- p.117 -->

On the Scheduling page, set the time when this application is deployed or available to
client devices.

By default, Configuration Manager makes the deployment policy available to clients
right away. If you want to create the deployment, but not make it available to clients
until a later date, configure the option to Schedule the application to be available. Then
select the date and time, including whether that's based on UTC or the client's local
time.

If the deployment is Required, also specify the Installation deadline. By default this
deadline is as soon as possible.

For example, you need to deploy a new line-of-business application. All users need to
install it by a certain time, but you want to give them the option to opt in early. You also
need to make sure that the site has distributed the content to all distribution points. You
schedule the application to be available in five days from today. This schedule gives you
time to distribute the content and confirm its status. You then set the installation
deadline for one month from today. Users see the application in Software Center when
it's available in five days. If they do nothing, the client automatically installs the
application at the installation deadline.

If the application you're deploying supersedes another application, set the installation
deadline when users receive the new application. Set the Installation Deadline to
upgrade users with the superseded application.

Delay enforcement with a grace period
You might want to give users more time to install required applications beyond any
deadlines you set. This behavior is typically required when a computer is turned off for a
long time, and needs to install many applications. For example, when a user returns
from vacation, they have to wait for a long time as the client installs overdue
deployments. To help solve this problem, define an enforcement grace period.

        First, configure this grace period with the property Grace period for enforcement
        after deployment deadline (hours) in client settings. For more information, see the
        Computer agent group. Specify a value between 1 and 120 hours.

        On the Scheduling page of a required application deployment, enable the option
        to Delay enforcement of this deployment according to user preferences, up to
        the grace period defined in client settings. The enforcement grace period applies
        to all deployments with this option enabled and targeted to devices to which you
        also deployed the client setting.

<!-- p.118 -->

After the deadline, the client installs the application in the first non-business window,
which the user configured, up to this grace period. However, the user can still open
Software Center and install the application at any time. Once the grace period expires,
enforcement reverts to normal behavior for overdue deployments.

  ７ Note

  Most of the time, this feature addresses the scenario when the device is powered
  off while the user is out of the office. Technically, the grace period starts when the
  client gets policy after the deployment deadline. The same behavior happens if you
  stop the Configuration Manager client service (CcmExec), and then restart it at
  some time after the deployment deadline.

User experience settings
On the User Experience page, specify information about how users can interact with the
application installation.

     User notifications: Specify whether to display notification in Software Center at the
     configured available time. This setting also controls whether to notify users on the
     client computers. For available deployments, you can't select the option to Hide in
     Software Center and all notifications.
        When software changes are required, show a dialog window to the user
        instead of a toast notification: Select this option to change the user experience
        to be more intrusive. It only applies to required deployments. For more
        information, see User notifications.

     Software Installation and System restart: Only configure these settings for
     required deployments. They specify the behaviors when the deployment reaches
     the deadline outside of any defined maintenance windows. For more information
     about maintenance windows, see How to use maintenance windows.

<!-- p.119 -->

     Write filter handling for Windows Embedded devices: This setting controls the
     installation behavior on Windows Embedded devices that are enabled with a write
     filter. Choose the option to commit changes at the installation deadline or during a
     maintenance window. When you select this option, a restart is required and the
     changes persist on the device. Otherwise, the application is installed to the
     temporary overlay, and committed later.
        When you deploy a software update to a Windows Embedded device, make
        sure the device is a member of a collection that has a configured maintenance
        window. For more information about maintenance windows and Windows
        Embedded devices, see Create Windows Embedded applications.

Alerts
On the Alerts page, configure how Configuration Manager generates alerts for this
deployment. If you're also using System Center Operations Manager, configure its alerts
as well. You can only configure some alerts for required deployments.

Next steps
     Monitor applications
     Disable and delete application deployments
     Troubleshoot application deployments
     Common error codes for app installation
     Management tasks for applications
     Software Center user guide

  ７ Note

  This article used to include more sections, which have moved to the following
  articles:

        Delete a deployment
        User notifications for required deployments
        Check for running executable files
        Deploy user-available apps

Feedback

<!-- p.120 -->

Was this page helpful?      Yes    No

Provide product feedback
