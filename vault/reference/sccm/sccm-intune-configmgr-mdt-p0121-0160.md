---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 121-160"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0121-0160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0121-0160
family: sccm
documentKind: "doc"
abstract: "On this wizard Do this page Details - In Publisher, type publisher_name (where publisher_name is the name of the application's publisher). - In Application Name, type application_name (where application_name is the descriptive name of the application). - In Version, type version"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 121-160

<!-- p.121 -->

      On this wizard   Do this
      page

      Details          - In Publisher, type publisher_name (where publisher_name is the name
                       of the application's publisher).

                       - In Application Name, type application_name (where application_name
                       is the descriptive name of the application).

                       - In Version, type version (where version is the version of the
                       application).

                       - In Language, type language (where language is the language of the
                       application).

                       - Select Next.

      Summary          Select Next.

      Confirmation     Select Save Output to save the output of the wizard to a file, or select
                       View Script to view the Windows PowerShell scripts used to perform the
                       wizard tasks.

                       Select Finish.

     The New Application Wizard finishes. The application is added to the list of
     operating systems in the details pane of the Deployment Workbench.

View and Configure an Application in the Deployment Workbench

View the properties of applications beneath the Applications node in the Deployment
Workbench using the Properties actions as described in View Item Properties in the
Deployment Workbench. Configure an application in the Deployment Workbench by
performing the following steps in the Application Properties dialog box:

     Configure properties on the General tab as described in Configure the Application
     Properties General Tab.

     Configure properties on the Details tab as described in Configure the Application
     Properties Details Tab.

     Configure properties on the Dependencies tab as described in Configure the
     Application Properties Dependencies Tab.

     Configure the properties on the Office Products tab as described in Configure the
     Application Properties Office Products Tab.

<!-- p.122 -->

Configure the Application Properties General Tab

The application properties stored on the General tab are mostly configured when the
New Application Wizard runs. Update the application properties on the General tab
through the application_name Properties dialog box (where application_name is the
name of the application in the Deployment Workbench).

To configure the General tab for application properties

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Applications (where
     deployment_share is the name of the deployment share to which the application
     will be added).

  3. In the details pane, select application_name (where application_name is the name
     of the application to configure).

  4. In the Actions pane, select Properties.

     The application_name Properties dialog box opens (where application_name is the
     name of the application to configure).

  5. On the General tab, configure the settings listed in Table 40 based on the
     requirements of your organization, and then select OK.

     Table 40. Configuration Settings on the General Tab of
     Application Properties

                                                                               ﾉ   Expand table

      Setting                 Description

      Name                    Contains the name of the application displayed in the
                              Deployment Workbench. If Display name is not configured, this
                              value is also displayed in the Deployment Wizard.

      Comments                Provides information about the application.

      Display name            (Optional) Contains the name displayed in the Deployment
                              Wizard instead of the value in Name. If no value is specified, the
                              value in Name is displayed in the Deployment Wizard.

<!-- p.123 -->

Setting                    Description

Short name                 Contains the name of the folder in which the application resides.

Version                    Contains the version number of the application.

                           Enter the version number in this box; it is not validated against
                           the actual application version number but is provided for
                           informational purposes.

Publisher                  Contains the name of the application's publisher.

                           Enter the publisher in this box; it is not validated against the
                           actual application version number but is provided for
                           informational purposes.

Language                   Contains the language of the application.

                           Enter the language in this box; it is not validated against the
                           actual application language but is provided for informational
                           purposes.

Source directory           Configures the folder in which the source of the application files
                           resides.

Application GUID           Contains the GUID for the application.

Hide this application in   Select to control when this application appears in the
the Deployment             Deployment Wizard. If the check box is:
Wizard
                           - Selected, the Deployment Wizard will not display this
                           application.

                           - Cleared, the Deployment Wizard displays this application.

                           This check box is cleared by default.

                           This setting is also shown in the Hide column in the details pane
                           of the Deployment Workbench.

Enable this application    Select to control when this application is available to other
                           wizards and dialog boxes in the Deployment Workbench. If the
                           check box is:

                           - Selected, other wizards and dialog boxes in the Deployment
                           Workbench are able to select this application

                           - Cleared, other wizards and dialog boxes in the Deployment
                           Workbench are unable to select this application

<!-- p.124 -->

      Setting                  Description

                               This check box is selected by default.

     The application configuration settings are saved, and the modifications are
     displayed in the details pane of the Deployment Workbench.

Configure the Application Properties Details Tab

The application configuration settings stored on the Details tab are initially configured
when the New Application Wizard runs. Update the application properties on the Details
tab through the application_name Properties dialog box (where application_name is the
name of the application in the Deployment Workbench).

To configure the Details tab for application properties

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Applications (where
     deployment_share is the name of the deployment share to which the application
     will be added).

   3. In the details pane, select application_name (where application_name is the name
     of the application to configure).

   4. In the Actions pane, select Properties.

     The application_name Properties dialog box opens (where application_name is the
     name of the application to configure).

   5. On the Details tab, configure the settings listed in Table 41 based on the
     requirements of your organization, and then select OK.

     Table 41. Configuration Settings on the Details Tab of
     Application Properties

                                                                         ﾉ   Expand table

<!-- p.125 -->

    Setting       Description

    Application   Select to configure the application to install application dependencies but not the
    bundle        application. The other available option is Standard application.

    Standard      Select to configure the application to be a standard application that has source
    application   files, a command line, and other options listed on this tab. The other available
                  option is Application bundle.

    Quiet         Configures the command line to run for performing an unattended, or quiet,
    install       installation of the application. This text box is enabled only when you select the
    command       Standard application option.

    Working       Configures the working directory of the application and is enabled only when you
    directory     select Standard application.

    Uninstall     Configures the registry subkey
    registry      HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Uninstall,
    key name      used to determine whether the application is already installed on the target
                  computer. If MDT detects the presence of the subkey, it assumes that the
                  application is already installed and skips the installation of the application and any
                  dependencies. This text box is enabled only when you select Standard
                  application.

    Reboot the    Select to configure the MDT deployment process to restart the target computer
    computer      after installing this application. If the check box is:
    after
    installing    - Selected, the target computer restarts after installing the application
    this
    application   - Cleared, the target computer will not restart after installing the application

                  This check box is cleared by default.

    This can      Select to configure the application to run on any supported 32-bit or 64-bit
    run on any    Windows operating system. The other available option is This can run only on the
    platform      specified client platforms.

    This can      Select to configure the application to run on any supported 32-bit or 64-bit
    run only      Windows operating system. The other available option is This can run on any
    on the        platform.
    specified
    client
    platforms

   The application configuration settings are saved, and the modifications are
   displayed in the details pane of the Deployment Workbench.

Configure the Application Properties Dependencies Tab

<!-- p.126 -->

MDT checks the dependencies of an application before installing the application.
Similarly, MDT ensures that all application dependencies are installed before installing
the application.

  ７ Note

  Application dependencies are installed even if you do not select the dependencies
  separately from the application. Also, application dependencies override any rules
  defined in CustomSettings.ini or in the MDT DB.

When you define more than one application dependency, you can configure the order
in which the dependencies are installed, thereby ensuring that the dependencies are
installed in a specific order. Update the application properties on the Dependencies tab
through the application_name Properties dialog box (where application_name is the
name of the application in the Deployment Workbench).

To configure the Dependencies tab for application properties

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Applications (where
     deployment_share is the name of the deployment share to which you will add the
     application).

   3. In the details pane, select application_name (where application_name is the name
     of the application you are configuring).

   4. In the Actions pane, select Properties.

     The application_name Properties dialog box opens (where application_name is the
     name of the application to configure).

   5. On the Dependencies tab, configure the settings by performing one of the actions
     in Table 42 based on the requirements of your organization, and then select OK.

     Table 42. Actions on the Dependencies Tab of
     Application Properties

                                                                         ﾉ   Expand table

<!-- p.127 -->

      Action    Description

      Add       Adds a new application dependency to the list of dependencies using the Select
                an item dialog box. You can add any applications that already exist in the
                deployment share.

      Remove    Removes an application dependency from the list of dependencies.

      Up        Moves an application dependency higher in the sequence of installed
                dependencies.

                Application dependencies are installed from the top of the list to the bottom.

      Down      Moves an application dependency lower in the sequence of installed
                dependencies.

                Application dependencies are installed from the top of the list to the bottom.

     The application configuration settings are saved, and the modifications are
     displayed in the details pane of the Deployment Workbench.

Configure the Application Properties Office Products Tab

The application properties stored on the Office Products tab are mostly configured
when the New Application Wizard runs. Update the application properties on the Office
Products tab through the application_name Properties dialog box (where
application_name is the name of the application in the Deployment Workbench).

  ７ Note

  This tab is displayed when you create an application for Microsoft Office. For all
  other applications, this tab is not displayed.

To configure the Office Products tab for application properties

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Applications (where
     deployment_share is the name of the deployment share to which the application
     will be added).

<!-- p.128 -->

3. In the details pane, select application_name (where application_name is the name
  of the application to configure).

4. In the Actions pane, select Properties.

  The application_name Properties dialog box opens (where application_name is the
  name of the application to configure).

5. On the Office Products tab, configure the settings listed in Table 43 based on the
  requirements of your organization, and then select OK.

  Table 43. Configuration Settings on the Office
  Products Tab of Application Properties

                                                                              ﾉ   Expand table

   Setting         Description

   Office          Selects the Microsoft Office products to be installed.
   product to
   install

   Office          Use to select each language included in the source image.
   languages
                   By default, Microsoft Office Setup installs the same language as the target
                   operating system. Use these check boxes to force the installation of
                   specific language packs.

   Product key     Select to determine whether the Deployment Workbench configures the
                   Config.xml file for Microsoft Office Setup to provide a product key. If the
                   check box is:

                   - Selected, enter the product key in the associated box to automatically
                   configure the Config.xml file

                   - Cleared, the product key is provided during Microsoft Office Setup or in
                   a Windows Installer (MSP) configuration file

   Customer        Select to determine whether the Deployment Workbench configures the
   name            Config.xml for Microsoft Office Setup to provide the customer name. If the
                   check box is:

                   - Selected, enter the customer name in the associated box to automatically
                   configure the Config.xml file

                   - Cleared, the customer name is provided during Microsoft Office Setup or
                   in an MSP configuration file

<!-- p.129 -->

 Setting         Description

 Display level   Select to determine whether the Deployment Workbench configures
                 Config.xml for Microsoft Office Setup to configure the display level of the
                 setup process. If the check box is:

                 - Selected, select the display level in the associated box to automatically
                 configure the Config.xml file

                 - Cleared, the display level is provided during Microsoft Office Setup or in
                 an MSP configuration file

 Accept EULA     Select to determine whether the Deployment Workbench configures
                 Config.xml for Microsoft Office Setup to automatically accept the end user
                 license agreement (EULA) during the Setup process. If the check box is:

                 - Selected, the Config.xml file is configured to automatically accept the
                 EULA

                 - Cleared, EULA acceptance is provided during Microsoft Office Setup or in
                 an MSP configuration file

 Cache only      Select to determine whether the Deployment Workbench configures
                 Config.xml for Microsoft Office Setup to install the local installation source
                 (LIS) cache to the target computer during the setup process but not install
                 Microsoft Office. If the check box is:

                 - Selected, the Config.xml file is configured to copy the LIS cache during
                 Microsoft Office Setup but not install Microsoft Office products

                 - Cleared, the LIS cache is copied and Microsoft Office products are
                 installed during Microsoft Office Setup

 Always          Select to determine whether the Deployment Workbench configures
 suppress        Config.xml for Microsoft Office Setup to prevent restarting the target
 reboot          computer during the setup process. If the check box is:

                 - Selected, the Config.xml file is configured to prevent a restart of the
                 target computer during Microsoft Office Setup

                 - Cleared, the target computer can be restarted during Microsoft Office
                 Setup

 Add             Select to add Microsoft Office language packs.

 Edit            Select to modify the contents of the Config.xml file that the Deployment
 Config.xml      Workbench generates.

The application configuration settings are saved, and the modifications are
displayed in the details pane of the Deployment Workbench.

<!-- p.130 -->

Copy an Application in the Deployment Workbench
Copy and paste applications and folders beneath the Applications node in the
Deployment Workbench by using the Copy and Paste actions as described in Copy
Items in the Deployment Workbench.

Move an Application in the Deployment Workbench

Move applications and folders beneath the Applications node in the Deployment
Workbench by using the Cut and Paste actions as described in Move Items in the
Deployment Workbench.

Rename an Application in the Deployment Workbench
Rename applications and folders beneath the Applications node in the Deployment
Workbench by using the Rename action as described in Rename Items in the
Deployment Workbench.

Delete an Application from the Deployment Workbench
Delete applications and folders beneath the Applications node in the Deployment
Workbench using the Delete Selected Items Wizard as described in Delete Items from
the Deployment Workbench. The Delete Selected Items Wizard allows deletion of
individual applications or entire folder structures.

  ７ Note

  You should not delete an application when other applications are dependent on it.
  However, the Deployment Workbench does not enforce this recommendation.

Manage Folders for Applications in the Deployment Workbench

You can manage folders beneath the Applications node in the Deployment Workbench
to create hierarchical groupings of applications. For more information on:

     Managing folders, see Manage Folders in the Deployment Workbench

     Selection profiles, see Manage Selection Profiles

Enable or Disable an Application in the Deployment Workbench

<!-- p.131 -->

Control whether applications are available to other wizards and dialog boxes in the
Deployment Workbench by using the Enable this application check box on the General
tab of the application Properties dialog box.

   Tip

  To configure an application so that it can only be installed during a task sequence
  step, disable the application. Doing so allows the application to be installed during
  the task sequence but prevents the application from appearing in the list of
  available applications.

For more information on enabling or disabling applications in the Deployment
Workbench, see Configure the Application Properties General Tab.

Prevent an Application from Being Visible in the Deployment
Wizard

Prevent an application from being visible in the Deployment Wizard by selecting the
Hide this application in the Deployment Wizard check box on the General tab of the
application Properties dialog box, as described in Configure the Application Properties
General Tab.

  ７ Note

  The status of the Hide this application in the Deployment Wizard check box is
  shown in the Hide column in the details pane of the Application node.

Configure the Computer to Restart After Application Installation

Restart the target computer after installing an application by selecting the Restart the
computer after installing this application check box on the Details tab of the
application Properties dialog box. Selecting this check box causes the Deployment
Wizard to restart the target computer after installing the application, and then continue
with the next step in the task sequence.

  Ｕ Caution

  Do not allow the application to restart the target computer. MDT must control
  restarts, or the task sequence will fail. For example, use the command
  REBOOT=REALLYSUPPRESS to prevent some Windows Installer-based applications

<!-- p.132 -->

  from restarting. To prevent Microsoft Office from restarting the computer, add the
  property SETUP_REBOOT=NEVER to the Config.xml file or the MST file created by
  using the Office Customization Tool.

For more information on how to configure MDT to restart the target computer after
installing an application, see Configure the Application Properties Details Tab.

Customize Application Installation in Task Sequences
Adding applications in the Applications node in a deployment share through the
Deployment Workbench is the simplest method of deploying most applications. MDT
task sequences deploy applications by using the Install Application task sequence type.
Some of task sequence templates included in MDT have the Install Applications task
sequence step in the State Restore group, which is based on the Install Application task
sequence type.

The Install Application task sequence type allows for installation of one or more
applications in a single task sequence step using one of the configuration options listed
in Table 44.

Table 44. Configuration Settings on the Properties Tab of
the Install Application Task Sequence

                                                                                    ﾉ   Expand table

 Setting            Description

 Install multiple   Select to install one or more applications in a single task sequence step. This
 applications       configuration option allows installation of any applications that you:

                    - Select in the Deployment Wizard

                    - Specify in the Applications property in CustomSettings.ini or the MDT DB

                    - Specify in the MandatoryApplications property in CustomSettings.ini or the
                    MDT DB

                    You use the Success codes box in conjunction with this option to identify the
                    application installation return codes that indicate a successful application
                    deployment. The default values in this box are 0 and 3010 for the task sequence
                    step in the templates included in MDT.

                    This configuration option is the default selection for the Install Applications
                    task sequence step.

<!-- p.133 -->

 Setting          Description

                  For more information on the:

                  - Applications property, see the section, "Applications", in the MDT document
                  Toolkit Reference.

                  - MandatoryApplications property, see the section, "MandatoryApplications",
                  in the MDT document Toolkit Reference.

 Install single   Select to install one or more applications in a single task sequence step. You
 application      use the Application to install box in conjunction with this option to select the
                  application to install, including any application dependencies for the selected
                  application.

Customize the application-deployment process in the task sequences by:

      Configuring the existing Install Applications task sequence step in the State
      Restore group as described in Configure an Existing Install Applications Task
      Sequence Step

      Creating a new task sequence step based on the Install Application task sequence
      type as described in Create a New Task Sequence Step for Installing Applications

Configure an Existing Install Applications Task Sequence Step

Configure an existing Install Applications task sequence step by modifying the
configuration settings on the Properties tab of the task sequence step.

To configure an existing Install Applications task sequence step

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
      Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
      Workbench/Deployment Shares/deployment_share/Task Sequences (where
      deployment_share is the name of the deployment share to which the application
      will be added).

   3. In the details pane, select task_sequence (where task_sequence is the name of the
      task sequence to configure).

   4. In the Actions pane, select Properties.

<!-- p.134 -->

  The task_sequence Properties dialog box opens (where task_sequence is the name
  of the application to configure).

5. In the task_sequence Properties dialog box (where task_sequence is the name of
  the application you want to configure), select the Task Sequence tab.

6. In the hierarchy of the task sequence, go to State Restore/Install Applications.

7. On the Properties tab, configure the settings listed in Table 45 based on the
  requirements of your organization, and then select OK.

  Table 45. Configuration Settings on the Properties Tab
  of the Install Applications Task Sequence

                                                                               ﾉ    Expand table

   Setting            Description

   Name               Configures the name of the task sequence step displayed in the task
                      sequence hierarchy.

   Description        Configures the description text for the task sequence step.

   Install multiple   Select to configure the task sequence step to install any applications that
   applications       you:

                      - Select in the Deployment Wizard

                      - Specify in the Applications property in CustomSettings.ini or the MDT
                      DB

                      - Specify in the MandatoryApplications property in CustomSettings.ini
                      or the MDT DB

   Success codes      Configures the list of success codes for the application-installation
                      software. Each success code is separated by a space. This text box is only
                      enabled when you select the Install multiple applications option.

   Install a single   Configures the task sequence step to install only the application listed in
   application        the Application to install box.

   Application to     Configures the application to be installed when you select the Install a
   install            single application option. Select the application to install by selecting
                      Browse. This text box is enabled only when you select Install a single
                      application.

<!-- p.135 -->

     The updated task sequence appears in the details pane of the Deployment
     Workbench.

Create a New Task Sequence Step for Installing Applications

In most instances, the existing Install Applications task sequence step is sufficient for
installing applications to target computers. However, there are instances in which the
existing Install Applications task sequence step may not be sufficient for your
organization's requirements, or you may need to install an application at a different
sequence in the task sequence.

For example, the installation process for some device drivers is performed more like an
application installation than the typical installation process for a traditional device driver.
You can install these device drivers by creating a new task sequence step based on the
Install Application task sequence type.

   Tip

  Disable the existing Install Applications step in the task sequence, and add all
  applications manually using the task sequence controls. The benefits of this
  approach are that you can easily select and insert applications into the task
  sequence in any order necessary, simplifying management of a large number of
  applications.

To create a new task sequence step for installing applications

   1. Create a new task sequences step based on the Install Application type at the
     appropriate place in the task sequence hierarchy as described in Configure the
     Task Sequence Properties Task Sequence Tab.

   2. Configure the new task sequence step to deploy one or more applications as
     described in Configure an Existing Install Applications Task Sequence Step.

Configuring Packages in the Deployment Workbench
Packages in MDT are operating system software installed on the target computers and
stored in CAB or MSU files, such as security updates, service packs, feature packs, or
language packs. Manage the packages to be deployed to the reference and target
computers in your organization using the Deployment Workbench. You configure
packages in the Deployment Workbench in a deployment share's Packages node by:

<!-- p.136 -->

     Importing a new package as described in Import a New Package into the
     Deployment Workbench

     Modifying an existing package as described in Modify an Existing Package in the
     Deployment Workbench

     Copying a package as described in Copy a Package in the Deployment Workbench

     Moving a package as described in Move a Package in the Deployment Workbench

     Renaming a package as described in Rename a Package in the Deployment
     Workbench

     Deleting a package as described in Delete a Package from the Deployment
     Workbench

     Managing folders for packages as described in Manage Folders for Packages in the
     Deployment Workbench

     Enabling or disabling a package Enable or Disable a Package in the Deployment
     Workbench

     Preventing a package from being visible as described in Prevent a Package from
     Being Visible in the Deployment Wizard

     Customizing package installation as described in Customize Package Installation in
     Task Sequences

     In addtion to managing operating system packages in the Deployment
     Workbench, you can manage operating system packages using the MDT Windows
     PowerShell cmdlets. For more information on managing operating system
     packages using the MDT Windows PowerShell cmdlets, see the following sections
     beneath the section, "MDT Windows PowerShell Cmdlets", in the MDT document
     Toolkit Reference:

     Get-MDTDeploymentShareStatistics

     Import-MDTPackage

Import a New Package into the Deployment Workbench

Import packages into the Deployment Workbench by using the Import OS Packages
Wizard. Start the Import OS Packages Wizard using one of the following methods:

<!-- p.137 -->

    In the console tree, select the Packages node or a folder beneath the Packages
    node. Then, in the Actions pane, select Import OS Packages.

    In the console tree, select the Packages node or a folder beneath the Packages
    node. Then, from the Action menu, select Import OS Packages.

    In the console tree, select the Packages node or a folder beneath the Packages
    node, and then select Import OS Packages.

To import a new package

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
    Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
    Workbench/Deployment Shares/deployment_share/Packages (where
    deployment_share is the name of the deployment share to which you will add the
    application).

  3. In the Actions pane, select Import OS Packages.The Import OS Packages Wizard
    starts.

  4. Complete the Import OS Packages Wizard using the information in Table 46.

    Table 46. Information for Completing the Import OS
    Packages Wizard

                                                                               ﾉ   Expand table

     On this wizard   Do this
     page

     Specify          In Package source directory, type path (where path is the fully qualified
     Directory        path to the folder that contains the package you want to import), and
                      then select Next.

                      You can alternatively select Browse to find the folder on a local drive or
                      network shared folder.

     Summary          View the information in the Details box, and then select Next.

     Confirmation     You can select Save Output to save the output of the wizard to a file. You
                      can also select View Script to view the Windows PowerShell scripts used
                      to perform the wizard tasks.

<!-- p.138 -->

      On this wizard   Do this
      page

                       Select Finish.

     The Import OS Packages Wizard finishes. The package is added to the list of
     packages in the details pane of the Deployment Workbench.

Modify an Existing Package in the Deployment Workbench
Modify packages in the Packages node in the Deployment Workbench using the
Properties actions as described in View Item Properties in the Deployment Workbench.
The package properties are mostly configured when you run the Import OS Packages
Wizard. Update the package properties on the General tab through the package_name
Properties dialog box (where package_name is the name of the application in the
Deployment Workbench).

To modify an existing package

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Packages (where
     deployment_share is the name of the deployment share in which you will configure
     the package).

  3. In the details pane, select package_name (where package_name is the name of the
     package you want to configure).

  4. In the Actions pane, select Properties.

     The package_name Properties dialog box opens (where package_name is the
     name of the package you want to configure).

  5. On the General tab, configure the settings listed in Table 47 based on the
     requirements of your organization, and then select OK.

     Table 47. Configuration Settings on the General Tab of
     the Package Properties

<!-- p.139 -->

                                                                           ﾉ   Expand table

Setting                  Description

Name                     Contains the name of the package displayed in the Deployment
                         Workbench. If Display name is not configured, this value is also
                         displayed in the Deployment Wizard.

Comments                 Provides information about the package.

Display name             (Optional) Contains the name displayed in the Deployment
                         Wizard instead of the value in Name. If no value is specified, the
                         value in Name is displayed in the Deployment Wizard.

Type                     Type of package, which typically includes the following high-level
                         types of packages:

                         - Language packs

                         - Hotfix patches

                         - Feature packs

                         The package type in this text box is automatically determined by
                         the Deployment Workbench and cannot be modified.

Processor architecture   Target processor architecture for the package; it can be x86,
                         amd64, or ia64.

                         The processor architecture in this box is automatically determined
                         by the Deployment Workbench and cannot be modified.

Language                 Contains the language of the application.

                         The language in this box is automatically determined by the
                         Deployment Workbench and cannot be modified.

Keyword                  Used to identify the version of the language pack.

                         The keyword in this text box is automatically determined by the
                         Deployment Workbench and cannot be modified.

Public key token         Contains the public key token that MDT uses to updated the
                         unattended.xml file.

                         The public key token in this text box is automatically determined
                         by the Deployment Workbench and cannot be modified.

Version                  Contains the version number of the package.

<!-- p.140 -->

    Setting                 Description

                            The version number in this text box is automatically determined
                            by the Deployment Workbench and cannot be modified.

    Product name            Contains the name of the product for which the package is
                            intended.

                            The product name in this text box is automatically determined by
                            the Deployment Workbench and cannot be modified.

    Product version         Contains the version number of the product for which the
                            package is intended.

                            The product version number in this text box is automatically
                            determined by the Deployment Workbench and cannot be
                            modified.

    Package path            Contains the path of the package relative to the root of the
                            deployment share.

                            The path in this text box is automatically determined by the
                            Deployment Workbench and cannot be modified.

    Hide this package in    Select to control when this package appears in the Deployment
    the Deployment          Wizard. If the check box is:
    Wizard
                            - Selected, the Deployment Wizard will not display this package

                            - Cleared, the Deployment Wizard displays this package

                            The check box is cleared by default.

    Enable (approve) this   Select to control when this package is available to other wizards
    package                 and dialog boxes in the Deployment Workbench. If the check box
                            is:

                            - Selected, other wizards and dialog boxes in the Deployment
                            Workbench are able to select this package

                            - Cleared, other wizards and dialog boxes in the Deployment
                            Workbench are unable to select this package

                            The check box is selected by default.

   The package configuration settings are saved, and the modifications are displayed
   in the details pane of the Deployment Workbench.

Copy a Package in the Deployment Workbench

<!-- p.141 -->

You can copy and paste packages and folders beneath the Packages node in the
Deployment Workbench using the Copy and Paste actions as described in Copy Items in
the Deployment Workbench.

Move a Package in the Deployment Workbench
You can move packages and folders beneath the Packages node in the Deployment
Workbench using the Cut and Paste actions as described in Move Items in the
Deployment Workbench.

Rename a Package in the Deployment Workbench

You can rename packages and folders beneath the Packages node in the Deployment
Workbench using the Rename action as described in Rename Items in the Deployment
Workbench.

Delete a Package from the Deployment Workbench

You can delete packages and folders beneath the Applications node in the Deployment
Workbench using the Delete Selected Items Wizard as described in Delete Items from
the Deployment Workbench. The Delete Selected Items Wizard allows you to delete
individual package or entire folder structures.

Manage Folders for Packages in the Deployment Workbench

You can manage folders beneath the Packages node in the Deployment Workbench to
create hierarchical groupings of operating system packages. For more information on:

     Managing folders, see Manage Folders in the Deployment Workbench

     Selection profiles, see Manage Selection Profiles

Enable or Disable a Package in the Deployment Workbench

You can control whether packages are available to other wizards and dialog boxes in the
Deployment Workbench by selecting the Enable (approve) this package check box on
the General tab of the package Properties dialog box.

   Tip

<!-- p.142 -->

  If you want to configure a package so that it can only be installed during a task
  sequence step, disable the application. Doing so allows the package to be installed
  during the task sequence but prevents the application from appearing in the list of
  available package.

For more information on enabling or disabling packages in the Deployment Workbench,
see Configuring Packages in the Deployment Workbench.

Prevent a Package from Being Visible in the Deployment Wizard
You can prevent a package from being visible in the Deployment Wizard by selecting
the Hide this application in the Deployment Wizard check box on the General tab of
the application Properties dialog box. For more information on preventing packages
from appearing in the Deployment Wizard, see Configuring Packages in the Deployment
Workbench.

Customize Package Installation in Task Sequences

Adding packages in a deployment share's Packages node through the Deployment
Workbench is the simplest method for deploying most packages. MDT task sequences
deploy packages using the Install Updates Offline task sequence type. Some of task
sequence templates included in MDT have the Apply Patches task sequence step in the
Preinstall/Refresh onlygroup, which is based on the Install Updates Offline task
sequence type.

The Install Updates Offline task sequence type allows you to install one or more
packages in a single task sequence step using selection profiles, which allow one or
more packages to be selected and deployed as a unit. For more information managing
selection profiles, see Manage Selection Profiles.

Customize the package deployment process in your task sequences by:

     Configuring the existing Apply Patches task sequence step in the Preinstall group
     as described in Configure an Existing Apply Patches Task Sequence Step

     Creating a new task sequence step based on the Install Updates Offline task
     sequence type as described in Create a New Task Sequence Step for Installing
     Packages

     Adding language packs to task sequence steps as described in Add Language
     Packs to Task Sequence Steps

<!-- p.143 -->

Configure an Existing Apply Patches Task Sequence Step

You configure an existing Apply Patches task sequence step by modifying the
configuration settings on the Properties tab of the task sequence step.

To configure an existing Apply Patches task sequence step

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share to which you will add the
     application).

   3. In the details pane, select task_sequence (where task_sequence is the name of the
     task sequence you want to configure).

   4. In the Actions pane, select Properties.

     The task_sequence Properties dialog box opens (where task_sequence is the name
     of the application you want to configure).

   5. In the task_sequence Properties dialog box, select the Task Sequence tab (where
     task_sequence is the name of the application you want to configure).

   6. In the hierarchy of the task sequence, go to Preinstall/Apply Patches.

   7. On the Properties tab, configure the settings listed in Table 48 based on the
     requirements of your organization, and then select OK.

     Table 48. Configuration Settings on the Properties Tab
     of the Install Applications Task Sequence Step

                                                                                ﾉ   Expand table

      Setting        Description

      Name           Configures the name of the task sequence step displayed in the task
                     sequence hierarchy.

      Description    Configures the description text for the task sequence step.

      Selection      Used to select the selection profile that contains the updates you want to
      profile        deploy in this task sequence step. The selection profile can contain one or

<!-- p.144 -->

       Setting        Description

                      more packages to be deployed.

     The updated task sequence appears in the details pane of the Deployment
     Workbench.

Create a New Task Sequence Step for Installing Packages

In most instances, the existing Apply Patches task sequence step is sufficient for
installing packages to target computers. However, there are instances in which the
existing Apply Patches task sequence step may not be sufficient for your requirements
or you may need to install a package at a different place in the task sequence.

For example, the packages may need to be installed in a specific order or may have
dependencies, such as installing a service pack before installing hotfixes. First, create
folders and selection profiles for each grouping of packages that you wanted to install
separately. Then, install the groups of packages by creating a new task sequence step
for each group based on the Install Updates Offline-type task sequence step.

   Tip

  You can disable the existing Apply Patches step in the task sequence and add all
  packages manually using the task sequence controls. The benefit of this approach
  is that you easily select and insert packages into the task sequence in any order
  necessary. This simplifies management of a large number of packages.

To create a new task sequence step for installing packages

   1. Create a new task sequences step based on the Install Updates Offline type at the
     appropriate place in the task sequence hierarchy as described in Configure the
     Task Sequence Properties Task Sequence Tab.

   2. Configure the new task sequence step to deploy one or more packages by
     selecting the appropriate selection profile containing the packages to be installed
     as described in Configure an Existing Install Applications Task Sequence Step.

Add Language Packs to Task Sequence Steps

Language packs are one of the types of packages available in MDT and enable a
multilingual Windows environment. Windows is now language neutral, and all language
and locale resources are added to Windows through language packs (Lp.cab files). By

<!-- p.145 -->

adding one or more language packs to Windows those languages can be enabled when
installing the operating system. As a result, the same Windows image can be deployed
to regions with different language and locale settings, reducing development and
deployment time.

See the following references for additional information about language packs in
Windows:

     For instructions on installing language packs during deployment, see Running the
     Deployment Wizard.

     For the configuration properties for installing language packs automatically, see
     the MDT document Toolkit Reference.

     For more information about Windows language packs, see "Manage Language
     Packs for Windows" in the Windows ADK.

Configuring Device Drivers in the Deployment
Workbench
Integrate device drivers for the reference and target computers into Windows PE and
the target operating system unless these components are included in Windows PE or
the target operating system. The Deployment Workbench helps centralize and automate
device driver management and integration for LTI by providing a centralized repository
of device drivers, ensuring that the proper device drivers are deployed. The Deployment
Workbench also automates the injection of the appropriate device drivers into Windows
PE images that the Deployment Workbench generates. MDT supports different
strategies for device driver management. For more information about device driver
management strategies, see Managing Device Drivers.

Configure device drivers in the Deployment Workbench in a deployment share's Out-of-
Box node by:

     Importing device drivers as described in Import Device Drivers into the
     Deployment Workbench

     Modifying existing device drivers as described in Modify Existing Device Drivers in
     the Deployment Workbench

     Copying device drivers as described in Copy Device Drivers in the Deployment
     Workbench

     Moving device drivers as described in Move Device Drivers in the Deployment
     Workbench

<!-- p.146 -->

     Renaming device drivers as described in Rename Device Drivers in the Deployment
     Workbench

     Deleting device drivers as described in Delete Device Drivers from the Deployment
     Workbench

     Managing folders for device drivers as described in Manage Folders for Device
     Drivers in the Deployment Workbench

     Enabling or disabling device drivers as described in Enable or Disable Device
     Drivers in the Deployment Workbench

     Deploy specific device drivers to target computers for LTI deployments as
     described in Deploy Specific Device Drivers to Target Computers in LTI

     In addtion to managing device drivers in the Deployment Workbench, you can
     manage device drivers using the MDT Windows PowerShell cmdlets. For more
     information on managing device drivers using the MDT Windows PowerShell
     cmdlets, see the following sections beneath the section, "MDT Windows
     PowerShell Cmdlets", in the MDT document Toolkit Reference:

     Import-MDTDriver

     Get-MDTDeploymentShareStatistics

Import Device Drivers into the Deployment Workbench

Import device drivers into the Deployment Workbench using the Import Drivers Wizard.
Start the Import Drivers Wizard using one of the following methods:

     In the console tree, select the Out-of-Box Drivers node or a folder beneath the
     Out-of-Box Drivers node. Then, in the Actions pane, select Import Drivers.

     In the console tree, select the Out-of-Box Drivers node or a folder beneath the
     Out-of-Box Drivers node. Then, from the Action menu, select Import Drivers.

     In the console tree, select the Out-of-Box Drivers node or a folder beneath the
     Out-of-Box Drivers node, and then select Import Drivers.

To import device drivers

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

<!-- p.147 -->

2. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares/deployment_share/Out-of-box Drivers node
  (where deployment_share is the name of the deployment share to which you will
  add the device drivers) or a folder beneath that node.

3. In the Actions pane, select Import Drivers.

  The Import Driver Wizard starts.

4. Complete the Import Driver Wizard using the information in Table 49.

  Table 49. Information for Completing the Import
  Driver Wizard

                                                                             ﾉ    Expand table

   On this wizard   Do this
   page

   Specify          a. In Driver source directory, type path (where path is the fully qualified
   Directory        path to the folder that contains the device drivers you want to import).

                    You can alternatively select Browse to find the folder on a local drive or
                    network shared folder.

                    b. Select or clear the Import drivers even if they are duplicates of an
                    existing driver check box based on the requirements of your
                    organization.

                    If the check box is:

                    - Selected, the wizard will import the drivers even if the same drivers
                    already exist

                    - Cleared, the wizard will not import the drivers if the same drivers
                    already exist

                    In most instances, do not select this check box, as doing so increases the
                    size of the deployment share and makes driver management more
                    complex.

                    c. Select Next.

   Summary          Select Next.

   Confirmation     You can select Save Output to save the output of the wizard to a file. You
                    can also select View Script to view the Windows PowerShell scripts used

<!-- p.148 -->

      On this wizard       Do this
      page

                           to perform the wizard tasks.

                           Select Finish.

     The Import Drivers Wizard finishes. The device drivers are added to the list of
     device drivers in the details pane of the Deployment Workbench.

Modify Existing Device Drivers in the Deployment Workbench
Modify device drivers in the Out-of-Box Drivers node in the Deployment Workbench
using the Properties action as described in View Item Properties in the Deployment
Workbench. Configure device drivers in the Deployment Workbench by performing the
following steps in the device driver Properties dialog box:

   1. Configure properties on the General tab as described in Configure the Device
     Driver Properties General Tab.

   2. View properties on the Details tab as described in View the Device Driver
     Properties Details Tab.

Configure the Device Driver Properties General Tab

The device driver properties stored on the General tab are mostly configured when you
run the Import Device Drivers Wizard. Update the device driver properties on the
General tab through the driver_name Properties dialog box (where driver_name is the
name of the device driver in the Deployment Workbench).

To modify existing device drivers properties on the General tab

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Out-of-Box Drivers (where
     deployment_share is the name of the deployment share in which you will configure
     the device driver).

   3. In the details pane, select driver_name (where driver_name is the name of the
     device driver you want to configure).

   4. In the Actions pane, select Properties.

<!-- p.149 -->

  The driver_name Properties dialog box opens (where driver_name is the name of
  the device driver you want to configure).

5. On the General tab, configure the settings listed in Table 50 based on the
  requirements of your organization, and then select OK.

  Table 50. Configuration Settings on the General Tab of
  the Device Driver Properties

                                                                               ﾉ   Expand table

   Setting       Description

   Driver        Contains the name of the device driver displayed in the Deployment
   name          Workbench and the Deployment Wizard.

   Comments      Provides information about the device driver.

   Platforms:    Select to control whether this device driver is for 32-bit operating system. If
   x86           the check box is:

                 - Selected, the device driver is available for deployment to 32-bit operating
                 systems

                 - Cleared, the device driver is unavailable for deployment to 32-bit operating
                 systems

                 If the Deployment Workbench incorrectly detects the platforms that the
                 device driver supports, you can clear the platform selection. For example, if
                 the Deployment Workbench incorrectly detects 32-bit and 64-bit device
                 drivers, clear the x64 selection; the driver will then only be used for 32-bit
                 deployments.

   Platforms:    Select to control whether this device driver is for 64-bit operating system. If
   x64           the check box is:

                 - Selected, the device driver is available for deployment to 64-bit operating
                 systems

                 - Cleared, the device driver is unavailable for deployment to 64-bit operating
                 systems

                 If the Deployment Workbench incorrectly detects the platforms that the
                 device driver supports, you can clear the platform selection. For example, if
                 the Deployment Workbench incorrectly detects 32-bit and 64-bit device
                 drivers, clear the x64 selection; the driver will then only be used for 32-bit
                 deployments.

<!-- p.150 -->

      Setting       Description

      Enable this   Select to control whether this device driver is available to other wizards and
      driver        dialog boxes in the Deployment Workbench. If the check box is:

                    - Selected, the device driver is available to other wizards and dialog boxes in
                    the Deployment Workbench

                    - Cleared, the device driver is unavailable to other wizards and dialog boxes
                    in the Deployment Workbench

                    The check box is selected by default.

     The device driver configuration settings are saved, and the modifications are
     displayed in the details pane of the Deployment Workbench.

View the Device Driver Properties Details Tab

The device driver properties stored on the Details tab are configured when you run the
Import Device Drivers Wizard. All the information on the Details tab is read only and
cannot be modified. View the device driver properties on the Details tab through the
driver_name Properties dialog box (where driver_name is the name of the device driver
in the Deployment Workbench).

To view existing device drivers properties on the Details tab

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Out-of-Box Drivers (where
     deployment_share is the name of the deployment share in which you will configure
     the device driver).

   3. In the details pane, select driver_name (where driver_name is the name of the
     device driver you want to configure).

   4. In the Actions pane, select Properties.

     The driver_name Properties dialog box opens (where driver_name is the name of
     the device driver you want to configure).

   5. On the Details tab, view the settings listed in Table 51, and then select OK.

<!-- p.151 -->

     ７ Note

     The configuration settings on the Details tab are automatically determined by
     the Deployment Workbench and cannot be modified.

   Table 51. Configuration Settings on the Details Tab of
   the Device Driver Properties

                                                                               ﾉ   Expand table

    Setting          Description

    Manufacturer     Contains the name of the device driver manufacturer.

    Version          Contains the version number of the device driver.

    Driver date      Contains the date of the device driver.

    Driver type      Contains the class of the device driver, such as system or boot.
    (class)

    INF path         Contains the path to the device drive file relative to the root of the
                     deployment share.

    Supported OS     Contains a comma-separated list of the Windows operating system
    versions         versions that the device driver supports.

    Hash             Contains the encrypted hash of every file that is part of the driver
                     package.

    Supported PnP    Contains a list of the plug-and-play IDs that the device driver supports.
    IDs

    This driver is   Select to indicate whether the device driver is signed by the Windows
    WHQL signed      Hardware Quality Labs (WHQL). For device drivers that pass the WHQL
                     tests, Microsoft creates a digitally signed certification file that allows
                     installation on 64-bit versions of Windows and prevents 32-bit versions
                     of Windows from displaying a warning message that the driver has not
                     been certified by Microsoft.If the check box is:

                     - Selected, the device driver has been signed by the WHQL

                     - Cleared, the device driver has not been signed by the WHQL

Copy Device Drivers in the Deployment Workbench

<!-- p.152 -->

You can copy and paste device drivers and folders beneath the Out-of-Box Drivers node
in the Deployment Workbench using the Copy and Paste actions as described in Copy
Items in the Deployment Workbench.

Move Device Drivers in the Deployment Workbench
You can move device drivers and folders beneath the Out-of-Box Drivers node in the
Deployment Workbench using the Cut and Paste actions as described in Move Items in
the Deployment Workbench.

Rename Device Drivers in the Deployment Workbench

You can rename device drivers and folders beneath the Out-of-Box Drivers node in the
Deployment Workbench using the Rename action as described in Rename Items in the
Deployment Workbench.

Delete Device Drivers from the Deployment Workbench

You can delete device drivers and folders beneath the Out-of-Box Drivers node in the
Deployment Workbench using the Delete Selected Items Wizard as described in Delete
Items from the Deployment Workbench. The Delete Selected Items Wizard allows you to
delete individual packages or entire folder structures.

Manage Folders for Device Drivers in the Deployment Workbench

You can manage folders beneath the Out-of-Box Drivers node in the Deployment
Workbench to create hierarchical groupings of device drivers. For more information on:

     Managing folders, see Manage Folders in the Deployment Workbench

     Selection profiles, see Manage Selection Profiles

Enable or Disable Device Drivers in the Deployment Workbench

You can control whether device drivers are available to other wizards and dialog boxes
in the Deployment Workbench by selecting the Enable this driver check box on the
General tab of the device driver Properties dialog box.

  Ｕ Caution

<!-- p.153 -->

  If you disable a device driver, the driver is never installed.

For more information on enabling or disabling device drivers in the Deployment
Workbench, see Modify Existing Device Drivers in the Deployment Workbench.

Deploy Specific Device Drivers to Target Computers in LTI
By default, LTI deployments include all device drivers in Windows PE and deploy them to
the target computers. Then, the target operating system uses Plug-and-Play IDs to
identify the device drivers that are needed for the devices on the target computers.

To change this default behavior, configure the LTI deployment process to install specific
drivers to target computers as described in Control Device Driver Deployments for LTI.
For more information about strategies for device driver management, see Select the
Device Driver Management Strategy.

Configuring Task Sequences in the Deployment
Workbench
Task sequences in MDT contain the steps to be performed during LTI. Task sequences in
MDT use the same task sequence engine as Configuration Manager; however,
Configuration Manager is not required to perform LTI deployments. Use the
Deployment Workbench to manage the task sequences used to perform deployments to
the reference and target computers in your organization.

Configure task sequences in the Deployment Workbench in a deployment share's
Packages node by:

     Creating a new task sequence as described in Create a New Task Sequence in the
     Deployment Workbench

     Modifying an existing task sequence as described in Modify an Existing Task
     Sequence in the Deployment Workbench

     Copying task sequences as described in Copy Task Sequences in the Deployment
     Workbench

     Moving task sequences as described in Move Task Sequences in the Deployment
     Workbench

     Renaming task sequences as described in Rename Task Sequences in the
     Deployment Workbench

<!-- p.154 -->

     Deleting task sequences as described in Delete Task Sequences from the
     Deployment Workbench

     Managing folders for task sequences as described in Manage Folders for Task
     Sequences in the Deployment Workbench

     Enabling or disabling a task sequence as described in Enable or Disable a Task
     Sequence in the Deployment Workbench

     Preventing task sequences from being visible in the Deployment Wizard as
     described in Prevent a Task Sequence from Being Visible in the Deployment Wizard

     Modifying the unattended setup answer file for a task sequence as described in
     Modify the Unattended Setup Answer File Associated with the Task Sequence

     In addtion to managing task sequences in the Deployment Workbench, you can
     manage task sequences using the MDT Windows PowerShell cmdlets. For more
     information on managing task sequences using the MDT Windows PowerShell
     cmdlets, see the following sections beneath the section, "MDT Windows
     PowerShell Cmdlets", in the MDT document Toolkit Reference:

     Import-MDTTaskSequence

     Get-MDTDeploymentShareStatistics

Create a New Task Sequence in the Deployment Workbench

Using the New Task Sequence Wizard in the Deployment Workbench to create new task
sequences. Start the New task Sequence Wizard using one of the following methods:

     In the console tree, select the Task Sequences node or a folder beneath the Task
     Sequences node, and then, in the Actions pane, select New Task Sequence.

     In the console tree, select the Task Sequences node or a folder beneath the Task
     Sequences node, and then, from the Action menu, select New Task Sequence.

     In the console tree, select the Task Sequences node or a folder beneath the Task
     Sequences node, and then select New Task Sequence.

     MDT includes task sequence templates that you can use for common deployment
     scenarios. In many instances, you can use the templates without any modification
     to the task sequence. However, you can modify task sequences created from the
     templates to meet the requirements of your organization.

Table 52 lists the task sequence templates in MDT.

<!-- p.155 -->

                                                                                ﾉ   Expand table

Template               Description

Sysprep and Capture    Performs a Sysprep operation and captures an image of a reference
                       computer.

Standard Client Task   Creates the default task sequence for deploying operating system images
Sequence               to client computers, including desktop and portable computers

Standard Client        Backs up the system entirely, backs up the user state, and wipes the disk
Replace Task
Sequence

Custom Task            Creates a customized task sequence that does not install an operating
Sequence               system

Standard Server Task   Creates the default task sequence for deploying operating system images
Sequence               to server computers.

Litetouch OEM Task     Pre-loads operating systems images on computers in a staging
Sequence               environment prior to deploying the target computers in the production
                       environment (typically by a computer OEM).

Post OS Installation   Performs installation tasks after the operating system has been deployed
Task Sequence          to the target computer

Deploy to VHD          Deploys client operating system images to a virtual hard disk (VHD) file on
Client Task Sequence   the target computer

Deploy to VHD          Deploys server operating system images to a VHD file on the target
Server Task            computer
Sequence

 ７ Note

 Select the Litetouch OEM task sequence only when performing deployments using
 removable media-based deployments you create in the Media node in the
 Deployment Workbench. Although you can select the Litetouch OEM Task
 Sequence template from other deployment shares, the task sequence will not finish
 successfully.

To create a new task sequence

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
    Toolkit, and then select Deployment Workbench.

<!-- p.156 -->

2. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares/deployment_share/Task Sequences (where
  deployment_share is the name of the deployment share to which you will add the
  task sequence).

3. In the Actions pane, select New Task Sequence.

  The New Task Sequence Wizard starts.

4. Complete the New Task Sequence Wizard using the information in Table 53.

  Table 53. Information for Completing the New Task
  Sequence Wizard

                                                                                 ﾉ   Expand table

   On this          Do this
   wizard page

   General          - In Task sequence ID, type task_sequence_id (where task_sequence_id is a
   Settings         unique identifier for the task sequence you are creating).

                    Although you can change a task sequence's name and comments later,
                    you cannot change a task sequence's ID. Before creating task sequences,
                    create a naming scheme to use in creating task sequence IDs that will
                    provide meaningful information about each task sequence. An example
                    naming scheme is Version-Edition-Level-Label, where Version is the
                    operating system version (Win8, Win2012), Edition is the operating system
                    edition (Enterprise, Standard, Ultimate), Level is the service pack level (SP1,
                    SP2), and Label is a descriptive label that identifies the customizations.

                    - In Task sequence name, type task_sequence_name (where
                    task_sequence_name is a descriptive name for the task sequence you are
                    creating).

                    - In Task sequence comments, type task_sequence_comment (where
                    task_sequence_comment is text that describes the purpose or usage of the
                    task sequence).

                    - Select Next.

   Select           In The following task sequence templates are available. Select the one
   Template         you would like to use as a starting point, select task_sequence, and then
                    select Next.

   Select OS        In The following operating system images are available to be deployed
                    with this task sequence. Select one to use, select operating_system (where

<!-- p.157 -->

On this        Do this
wizard page

               operating_system is the operating system in the Operating Systems node in
               the Deployment Workbench that you want to deploy to the resource or
               target computer), and then select Next.

Specify        a. Select one of the following options based on the requirements of your
Product Key    organization:

               - Do not specify a product key at this time. Select this option when a
               product key is not required when deploying Windows; when the product
               key will be provided in the Deployment Wizard; or when using volume
               licenses that are activated using KMS.

               - Specify a multiple activation key (MAK) for activating this operating
               system. Select this option when deploying Windows using MAK product
               keys in the deployment. MAK product keys are used by Microsoft Volume
               Licensing customers.

               - Specify the product key for this operating system. Select this option
               when deploying retail product key.

               For more information about Volume Activation and product keys in MDT,
               see Volume Activation Overview.

               b. Select Next.

OS Settings    - In Full Name, type user_full_name (where user_full_name is the name of
               the user of the target computer).

               - In Organization, type organization_name (where organization_name is
               the name of the organization).

               - In Internet Explorer Home Page, type home_url (where home_url is the
               Uniform Resource Locator [URL] of the website to be the default site when
               starting Internet Explorer).

               - Select Next.

Admin          In Administrator Password and Please confirm Administrator Password,
Password       type password (where password is the password to be assigned to the
               built-in Administrator account on the reference or target computer), and
               then select Next.

Summary        Select Next.

Confirmation   Select Finish.

<!-- p.158 -->

     The New Task Sequence Wizard finishes. The package is added to the list of
     packages in the details pane of the Deployment Workbench.

Modify an Existing Task Sequence in the Deployment Workbench

Modify task sequences in the Task Sequences node in the Deployment Workbench using
the Properties actions as described in View Item Properties in the Deployment
Workbench. Configure task sequences in the Deployment Workbench by performing the
following steps in the task sequence Properties dialog box:

   1. Configure properties on the General tab as described in Configure the Task
     Sequence Properties General Tab.

   2. Configure properties on the Task Sequence tab as described in Configure the Task
     Sequence Properties Task Sequence Tab.

   3. Configure properties on the OS Info tab as described in Configure the Task
     Sequence Properties OS Info Tab.

Configure the Task Sequence Properties General Tab

The task sequence properties stored on the General tab are mostly configured when
you run the New Task Sequence Wizard. Update the task sequence properties on the
General tab through the task_sequence_name Properties dialog box (where
task_sequence_name is the name of the task sequence in the Deployment Workbench).

To modify existing task sequence properties on the General tab

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share in which you will configure
     the task sequence).

   3. In the details pane, select task_sequence_name (where task_sequence_name is the
     name of the task sequence you want to configure).

   4. In the Actions pane, select Properties.

     The task_sequence_name Properties dialog box opens (where task_sequence_name
     is the name of the task sequence you want to configure).

<!-- p.159 -->

5. On the General tab, configure the settings listed in Table 54 based on the
  requirements of your organization, and then select OK.

  Table 54. Configuration Settings on the General Tab of
  Task Sequence Properties

                                                                           ﾉ   Expand table

   Setting                 Description

   Task sequence ID        Contains the task sequence identifier that the New Task
                           Sequence Wizard provided.

                           The information in this text box is automatically generated by
                           Deployment Workbench and cannot be modified.

   Task sequence name      Contains the name of the task sequence displayed in the
                           Deployment Workbench and the Deployment Wizard.

   Comments                Provides information about the task sequence.

   Task sequence version   Contains the version number of the task sequence. You can type
                           any version number that is appropriate for your organization's
                           versioning standards.

   This can run on any     Select to configure the task sequence to run on any supported
   platform                32-bit or 64-bit Windows operating system. The other available
                           option is This can run only on the specified client platforms.

   This can run only on    Select to configure the task sequence to run on any supported
   the specified client    32-bit or 64-bit Windows operating system. The other available
   platforms               option is This can run only any platform.

   Hide this task          Select to control when this task sequence appears in the
   sequence in the         Deployment Wizard. If the check box is:
   Deployment Wizard
                           - Selected, the Deployment Wizard will not display this task
                           sequence

                           - Cleared, the Deployment Wizard displays this task sequence

                           This check box is cleared by default.

   Enable this task        Select to control when this task sequence is available to other
   sequence                wizards and dialog boxes in the Deployment Workbench. If the
                           check box is:

                           - Selected, other wizards and dialog boxes in the Deployment
                           Workbench can select this task sequence

<!-- p.160 -->

      Setting                 Description

                              - Cleared, other wizards and dialog boxes in the Deployment
                              Workbench cannot select this task sequence

                              This check box is selected by default.

     The task sequence configuration settings are saved, and the modifications are
     displayed in the details pane of the Deployment Workbench.

Configure the Task Sequence Properties Task Sequence Tab

The task sequence properties stored on the Task Sequence tab are mostly configured
when you run the New Task Sequence Wizard. However, you can update the task
sequence properties on the Task Sequence tab through the task_sequence_name
Properties dialog box (where task_sequence_name is the name of the task sequence in
the Deployment Workbench).

The Task Sequence tab contains areas and other controls that you use to:

     Configure steps and sequences as described in Configure the Task Sequence Steps
     and Step Sequence

     Configure step properties as described in Configure the Task Sequence Step
     Properties

     Configure step options as described in Configure the Task Sequence Step Options

Configure the Task Sequence Steps and Step Sequence

The Task Sequence tab contains a hierarchical representation of the task sequence steps
and their sequence. Task sequence steps are organized into a hierarchical folder
structure based on deployment phases.

You can organize one or more task sequence steps by creating a group. You can
organize multiple groups and task sequence steps to create a hierarchy of groups and
task sequence steps. You use task sequence step groups to control the processing of
one or more task sequence steps as a unit.

Configure the task sequence steps and step sequence by selecting one of the following
options from the menu bar at the top of the hierarchical representation:

     Add. Select to add a task sequence step group or step to the task sequence. The
     categories of task sequence steps that you can add are listed in Table 56 along
