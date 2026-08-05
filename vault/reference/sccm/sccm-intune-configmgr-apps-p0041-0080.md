---
title: "App management documentation — pages 41-80"
type: reference
domain: sccm
slug: sccm-intune-configmgr-apps-p0041-0080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-apps-p0041-0080
family: sccm
documentKind: "doc"
abstract: "A localized application name is required for each language version that you set up. User categories: Choose Edit to specify application categories in the selected language. Users of Software Center use these categories to help filter and sort the applications. ７ Note User catego"
---

# App management documentation — pages 41-80

<!-- p.41 -->

  A localized application name is required for each language version that
  you set up.

User categories: Choose Edit to specify application categories in the selected
language. Users of Software Center use these categories to help filter and
sort the applications.

  ７ Note

  User categories for device-targeted application deployments show as
  filters in Software Center. These deployments can be either available or
  required.
  Renaming or deleting a category doesn't automatically apply to apps
  with this category. These changes apply on the next revision of the app.
  To work around this issue for rename or delete:
     First clear the checkbox for the category on any app that references it.
     Then apply that change, which revises the app.
        Instead of the rename action, next create a new category with the
        new name, and add the new category to the relevant apps.
        You can delete the category after you revise the apps.

User documentation: Specify the location of a file from which Software
Center users can get more information about this application. This location is
a website address, or a network path and file name. Make sure that users
have access to this location.

Link text: Specify the text that appears in place of "Additional information"
when user documentation is specified.

Privacy URL: Specify a website address to the privacy statement for the
application.

Localized description: Enter a description for this application in the selected
language.

Keywords: Enter a list of keywords in the selected language. These keywords
help Software Center users search for the application.

Icon: Select Browse to select an icon for this application. If you don't specify
an icon, Configuration Manager uses a default icon. Icons can have pixel
dimensions of up to 512x512.

<!-- p.42 -->

   4. On the Deployment Types page of the Create Application wizard, choose Add to
     create a new deployment type. For more information, see Create deployment types
     for the application.

   5. Choose Next, review the application information on the Summary page, and then
     finish the Create Application wizard.

The new application now appears in the Applications node of the Configuration
Manager console.

Create deployment types for the application
If you automatically detect application information, you may not need to finish some of
the steps in this section.

  ７ Note

  When you view the properties of an existing deployment type, the following
  sections correspond to tabs of the deployment type properties window:

        Content
        Task Sequence
        Detection Method
        User Experience
        Requirements
        Return Codes
        Dependencies

  For information on the Install Behavior tab on the properties of a deployment type,
  see Check for running executable files.

Start the Create Deployment Type wizard
There are three ways to start the Create Deployment Type wizard:

     In the Applications node: In the Configuration Manager console, go to the
     Software Library workspace, expand Application Management, and select the
     Applications node. Select an application, and then select Create Deployment Type
     in the ribbon.

<!-- p.43 -->

     When creating an application: When you Manually specify application information
     in the Create Application wizard, select Add on the Deployment Types page.

     From application properties: Select an existing application in the Applications
     node and select Properties. Switch to the Deployment Types tab, and select Add.

Then use one of the following procedures to automatically identify or manually specify
deployment type information.

Automatically identify deployment type information
   1. On the General page of the Create Deployment Type wizard:

     a. Select the application installation file Type to detect the deployment type
        information.

     b. Select Automatically identify information about this deployment type from
        installation files.

      c. In the Location box, specify the application installation file that you want to use
        to detect the deployment type information. This location is either a network
        path ( \\server\share\filename ) or a store link. You must have access to the
        network path and any subfolders that include application content.

   2. On the Import Information page of the Create Deployment Type wizard, review
     the information, and then select Next. If necessary, select Previous to go back and
     fix any errors.

   3. On the General Information page of the Create Deployment Type wizard, specify
     the following information:

       ７ Note

       Some of the deployment type information might already be present if it was
       read from the application installation files. Additionally, the displayed options
       might differ, depending on the deployment type that you're creating.

           General Information about the deployment type:

              The Name is required

              Administrator comments to further describe it

              Languages that are available for it

<!-- p.44 -->

           Installation program: Specify the installation program and any properties
           that you require to install the deployment type.

           Install behavior: Select one of the three options for how Configuration
           Manager installs this deployment type. For more information on these
           options, see User Experience.

           Use an automatic VPN connection (if configured): If you've deployed a VPN
           profile to the device on which the user launches the app, connect the VPN
           when the app starts. This option is only for Windows 8.1 and Windows Phone
           8.1. On Windows Phone 8.1 devices, if you deploy more than one VPN profile
           to the device, automatic VPN connections aren't supported. For more
           information, see VPN profiles.

   4. Choose Next, and then continue to Deployment type Content options.

Manually specify the deployment type information
   1. On the General page of the Create Deployment Type wizard, in the Type drop-
     down list, choose the application installation file type for this deployment type.

   2. Select Manually specify the deployment type information, and then select Next.

   3. On the General Information page of the Create Deployment Type wizard, specify a
     Name for the deployment type. Optionally specify Administrator comments,
     select the Languages for this deployment type, and then select Next.

   4. Continue to Deployment type Content options.

Deployment type Content options
On the Content page, specify the following information:

  ７ Note

  When you view the properties of an existing deployment type, some of these
  options appear on the Content tab and some on the Programs tab.

     Content location: Specify the location of the content for this deployment type, or
     select Browse to choose the deployment type content folder.

       ） Important

<!-- p.45 -->

  The System account of the site server computer must have permissions to the
  specified content location.

  Persist content in the client cache: The Configuration Manager client
  indefinitely keeps in its cache the deployment type content. The client persists
  the content even if the app is already installed. This option is useful with some
  deployments, like Windows Installer–based software. Windows Installer needs a
  local copy of the source content for applying updates. This option reduces the
  available cache space. If you select this option, it might cause a large
  deployment to fail at a later point if the cache doesn't have sufficient available
  space.

      Tip

     This option persists the specific version of content that the client installs. If
     you update the content for this app, the client doesn't automatically cache
     this content again. Once an action happens that requires the new content,
     the client downloads the new content version.

Installation program: Specify the name of the installation program and any
required installation parameters.
  Installation start in: Optionally specify the folder that has the installation
  program for the deployment type. This folder can be an absolute path on the
  client or a path to the distribution point folder that has the installation files.

Uninstall program: Optionally specify the name of the uninstall program and any
required parameters.
  Uninstall start in: Optionally specify the folder that has the uninstall program
  for the deployment type. This folder can be an absolute path on the client. It
  can also be a relative path on a distribution point of the folder with the
  package.

Repair program: For Windows Installer and Script Installer deployment types,
optionally specify the name of the repair program and any required parameters.
  Repair start in: Optionally specify the folder that has the repair program for the
  deployment type. This folder can be an absolute path on the client. It can also
  be a relative path on a distribution point of the folder with the package.

Run installation and uninstall program as 32-bit process on 64-bit clients: Use
the 32-bit file and registry locations on Windows-based computers to run the
installation program for the deployment type.

<!-- p.46 -->

Deployment type properties Content options
When you view the properties of a deployment type, the following options appear only
on the Content tab:

     Uninstall content settings:

        Same as install content: If the install and uninstall content are the same, select
        this option. This option is the default.

        No uninstall content: If your application doesn't need content for uninstall,
        select this option.

        Different from install content: If the uninstall content is different from the
        install content, select this option.
           Uninstall content location: Specify the network path to the content that's
           used to uninstall the application.

     Allow clients to use distribution points from the default site boundary group:
     Specify if clients should download and install the software from a distribution point
     in the site default boundary group when the content isn't available from a
     distribution point in the current or neighbor boundary groups.

     Deployment options: Specify if clients should download the application when they
     use a distribution point from a neighbor or the default site boundary groups.

  ７ Note

  Windows BranchCache is always enabled on clients. If the distribution point
  supports BranchCache, clients use it. For more information, see BranchCache.

Deployment type Task Sequence options
For more information on the task sequence deployment type, see Task sequence
deployment type.

On the Task Sequence page, specify the following information:

     Install task sequence: Select a task sequence that runs the installation process for
     this app.

     Uninstall task sequence (optional): Select a task sequence that removes this app.

<!-- p.47 -->

   Tip

  If your task sequence doesn't appear in the list, double-check that it doesn't include
  any OS deployment or OS upgrade steps. Also confirm that it isn't marked as a
  high-impact task sequence. For more information, review the prerequisites for the
  Task sequence deployment type.

Deployment type Detection Method options
This procedure sets up a detection method that indicates the presence of the
deployment type. In other words, whether the Windows device already has the
application installed. Use one of the two following methods to create a detection
method:

     Configure rules to detect the presence of this deployment type
     Use a custom script to detect the presence of this deployment type

Configure rules to detect the presence of this deployment type

   1. On the Detection Method page, the option to Configure rules to detect the
     presence of this deployment type is selected by default. Select Add Clause.

   2. In the Detection Rule dialog box, select a Setting type to detect the presence of
     the deployment type:

          File System: Detect whether a specified file or folder exists on a device. This
          detection indicates that the application is installed. Specify the following
          additional details:

             Type: Select whether it's a file or folder.

             Path (Required): Enter or browse to the local path on the device that
             includes the file or folder. For example, C:\Program Files . You can't specify
             a shared network path. If you select Browse, browse the local file system
             or connect to a representative client to browse.

             File or folder name (Required): Specify the specific file or folder name to
             detect in the above path. If the client detects this file or folder on the
             device, it considers the application as installed on the device.

             This file or folder is associated with a 32-bit application on 64-bit
             systems: The client first checks 32-bit file locations for the specified file or

<!-- p.48 -->

             folder. If the file or folder isn't found, the client then searches 64-bit
             locations.

          Registry: Detect whether a specified registry key or registry value exists on a
          client device. This detection indicates that the application is installed. Specify
          the following additional details:

             Hive (Required): Choose a registry hive from the drop-down list. For
             example, HKEY_LOCAL_MACHINE .

             Key (Required): Specify the registry key to search in the above hive. For
             example, SOFTWARE\Microsoft\Office .

             Value (Optional): Enter a specific value to detect in the above key. If you
             want the client to detect the (Default) value, enable the option to Use
             (Default) registry key value for detection. When you enter a value or
             enable this option, you're required to select a Data Type.

             This registry key is associated with a 32-bit application on 64-bit
             systems: Select this option to first check 32-bit registry locations for the
             specified registry key. If the registry key isn't found, the client searches 64-
             bit locations.

          Windows Installer: Detect whether a specified Windows Installer file exists on
          a client device. This detection indicates that the application is installed.
          Specify the MSI Product code to detect on the client. If you select Browse,
          choose the MSI file from which to read the product code.

  3. At the bottom of the Detection Rule window, specify whether the item must exist
     or satisfy a rule. For example, if you detect with a file, the following option is
     selected by default: The file system setting must exist on the target system to
     indicate presence of this application. Select the other option to create a rule for
     detection based on file or folder properties. These properties include Date
     Modified, Date Created, Version, or Size. These rule criteria are different for each
     setting type.

  4. Select OK to close the Detection Rule dialog box.

When you create more than one detection method for a deployment type, you can
group clauses together to create more complex logic.

Group detection clauses (optional)

  1. Create three or more detection method clauses on a deployment type.

<!-- p.49 -->

   2. Select two or more consecutive clauses, and then select Group. You'll see the
     parentheses added to the associated columns, which show where the group starts
     and ends.

     Example:

                                                                          ﾉ   Expand table

      Connector                    (       Clause                                     )

                                           MSI Product Code

      Or                           (       file1.text exists

      And                                  file2.txt exists                           )

   3. To remove the group, select the grouped clauses, and then select Ungroup.

Continue to the next section on using a custom script as a detection method. Or skip to
the User Experience options for the deployment type.

Use a custom script to check for the presence of a deployment type
   1. On the Detection Method page, select the Use a custom script to detect the
     presence of this deployment type box. Then select Edit.

   2. In the Script Editor dialog box, select a Script type to detect the deployment type:
     PowerShell, VBScript, or JScript.

       ７ Note

       When a Windows PowerShell script runs as a app detection method, the
       Configuration Manager client calls PowerShell with the -NoProfile parameter.
       This option starts PowerShell without profiles. A PowerShell profile is a script
       that runs when PowerShell starts.

   3. In the Script contents box, enter the script that you want to use, or paste in the
     contents of an existing script. Choose Open to browse to an existing saved script.
     Select Clear to remove the text in the Script contents field. If necessary, enable the
     option to Run script as 32-bit process on 64-bit clients.

       ７ Note

<!-- p.50 -->

         The maximum size for a script is 32 KB.

   4. Select OK to save the script and close the Script Editor dialog box. Back on the
     Create Deployment Type wizard, the Script Type and Script Length fields update
     with details about your script.

About custom script detection methods

Configuration Manager checks the results from the script. It reads the values written by
the script to the standard output (STDOUT) stream, the standard error (STDERR) stream,
and the exit code. If the script exits with a non-zero value, the script fails, and the
application detection status is Unknown. If the exit code is zero, and STDOUT has data,
the application detection status is Installed.

   Tip

  When writing a detection script, if you return a zero exit code but don't return
  output (data in STDOUT), the application will not be detected as installed. For more
  information, see the following examples.

Use the following tables to check whether an application is installed from the output
from a script:

Zero exit code

                                                                             ﾉ   Expand table

 STDOUT           STDERR           Script result       Application detection state

 Empty            Empty            Success             Not installed

 Empty            Not empty        Failure             Unknown

 Not empty        Empty            Success             Installed

 Not empty        Not empty        Success             Installed

Non-zero exit code

                                                                             ﾉ   Expand table

<!-- p.51 -->

 STDOUT           STDERR            Script result       Application detection state

 Empty            Empty             Failure             Unknown

 Empty            Not empty         Failure             Unknown

 Not empty        Empty             Failure             Unknown

 Not empty        Not empty         Failure             Unknown

Examples

Use the following PowerShell/VBScript examples to write your own application detection
scripts:

Example 1: The script returns an exit code that's not zero. This code indicates the script
failed to run successfully. In this case, the application detection state is unknown.

  PowerShell

  Exit 1

  VBScript

  WScript.Quit(1)

Example 2: The script returns an exit code of zero, but the value of STDERR isn't empty.
This result indicates the script failed to run successfully. In this case, the application
detection state is unknown.

  PowerShell

  Write-Error "Script failed"
  Exit 0

  VBScript

  WScript.StdErr.Write "Script failed"
  WScript.Quit(0)

Example 3: The script returns an exit code of zero, which indicates it ran successfully.
However, the value for STDOUT is empty, which indicates the application isn't installed.

  PowerShell

<!-- p.52 -->

  Exit 0

  VBScript

  WScript.Quit(0)

Example 4: The script returns an exit code of zero, which indicates it ran successfully.
The value for STDOUT isn't empty, which indicates the application is installed.

  PowerShell

  Write-Host "The application is installed"
  Exit 0

  VBScript

  WScript.StdOut.Write "The application is installed"
  WScript.Quit(0)

Example 5: The script returns an exit code of zero, which indicates it ran successfully.
The values for STDOUT and STDERR aren't empty, which indicates the application is
installed.

  PowerShell

  Write-Host "The application is installed"
  Write-Error "Completed"
  Exit 0

  VBScript

  WScript.StdOut.Write "The application is installed"
  WScript.StdErr.Write "Completed"
  WScript.Quit(0)

Deployment type User Experience options
These settings specify how the client installs the application on devices, and what the
user sees.

On the User Experience page, specify the following information:

<!-- p.53 -->

Installation behavior: In the drop-down list, select one of the following options:

  Install for user: The client only installs the application for the user to whom you
  deploy the application.

  Install for system: The client installs the application only once. It's available to
  all users.

  Install for system if resource is device; otherwise, install for user: If you deploy
  the application to a device, the client installs it for all users. If you deploy the
  application to a user, the client only installs it for that user.

Logon requirement: Select one of the following options:

  Only when a user is logged on

  Whether or not a user is logged on

  Only when no user is logged on

     ７ Note

     This option defaults to Only when a user is logged on. If you select Install
     for user in the Installation behavior drop-down list, you can't change this
     option.

Installation program visibility: Specify the mode in which the deployment type
runs on client devices. Select one of the following options:

  Maximized: The deployment type runs maximized on client devices. Users see
  all installation activity.

  Normal: The deployment type runs in the normal mode based on system and
  program defaults. This mode is the default.

  Minimized: The deployment type runs minimized on client devices. Users might
  see the installation activity in the notification area or taskbar.

  Hidden: The deployment type runs hidden on client devices. Users see no
  installation activity.

Allow users to view and interact with the program installation: Specify whether a
user can interact with the deployment type installation to set up the installation
options.

<!-- p.54 -->

   If you selected the Install for user option in the Installation behavior drop-down
   list, this option is enabled by default.

     ） Important

     When you select the Install for system behavior, this setting is optional. This
     change is primarily to allow an end user to interact with the installation during
     a task sequence. For example, to run a setup process that prompts the end
     user for various options. Some application installers can't have user prompts
     silenced, or the installation process may require specific configuration values
     only known to the user.

     Installing in system context and allowing users to interact with the installation
     isn't a secure configuration. For more information, see security and privacy
     for application management.

   Maximum allowed run time (minutes): Specify the maximum time in minutes that
   you expect the deployment type to run on the client computer. Specify this setting
   as a whole number greater than zero. The default value is 120 minutes (two hours).

   Use this value for the following actions:

      To monitor the results from the deployment type.

      To check whether a deployment type is installed when you define maintenance
      windows on client devices. When a maintenance window is in place, a
      deployment type only starts if enough time is available in the maintenance
      window to accommodate the Maximum Allowed Run Time setting.

        ） Important

        A conflict might occur if the Maximum allowed run time is longer than the
        scheduled maintenance window. If the user sets the maximum run time to
        a period greater than the length of any available maintenance window, that
        deployment type doesn't run.

   Estimated installation time (minutes): Specify the estimated installation time of
   the deployment type. Users see this time in Software Center.

Deployment type properties User Experience options

<!-- p.55 -->

When you view the properties of a deployment type, the following options appear only
on the User Experience tab:

Enforce specific post-installation behavior. Select one of the following options:

     Determine behavior based on return codes: Handle reboots based on the codes
     configured on the Return Codes tab. Software Center displays Might Require a
     Reboot. If a user is signed in during the install, they're prompted depending on the
     deployment's User Experience configuration.

     No specific action: No reboot required after installation. Software Center reports
     that no reboot is required.

     The software install program might force a device restart: Configuration Manager
     doesn't control or initiate a reboot, but the actual installation might do so without
     warning. Use this setting to prevent Configuration Manager from reporting
     installation failure when the installer initiates a reboot. Software Center displays
     Might Require a Reboot.

     Configuration Manager client will force a mandatory device restart:
     Configuration Manager forces a device reboot after successful installation.
     Software Center reports that a reboot is required. If a user is signed in during the
     install, they're prompted depending on the deployment's User Experience
     configuration.

Deployment type Requirements
Configuration Manager verifies these requirements on devices before installing the
deployment type. Use requirements to further refine and control the devices or users
that receive this application. For example, if you deploy the application to a user
collection, specify the app's hardware requirements here.

   1. On the Requirements page, select Add to open the Create Requirement dialog
     box.

   2. In the Category drop-down list, select whether this requirement is for a Device or
     a User.

     Select Custom to use a previously created global condition. When you select
     Custom, you can also choose Create to create a new global condition. For more
     about global conditions, see How to create global conditions.

        ） Important

<!-- p.56 -->

          If you deploy the application to a device collection, the client ignores any
          requirement of the category User and the condition Primary Device.

   3. In the Condition drop-down list, select the condition to assess whether the user or
     device meets the installation requirements. The contents of this list vary depending
     on the selected category.

   4. In the Operator drop-down list, select the operator to use. This operator compares
     the selected condition to the specified value. It assesses whether the user or device
     meets the installation requirement. The available operators vary depending on the
     selected condition. When using the One Of operator, the Values field has validation
     that you have to enter one entry per row.

          ７ Note

          The available requirements differ depending on the device type that the
          deployment type uses.

   5. In the Value box, specify the values to use for comparison. These values, along with
     the selected condition and operator, evaluate whether the user or device meets
     the installation requirements. The available values vary depending on the selected
     condition and the selected operator.

   6. Choose OK to save the requirement and close the Create Requirement dialog box.

Deployment type Dependencies
Dependencies define one or more deployment types from another application that the
client must install before it installs this deployment type.

  ） Important

  In some cases, a deployment type is dependent on a deployment type that also has
  dependencies. The maximum number of supported dependencies in the chain is
  five.

   1. On the Dependencies page, select Add.

   2. In the Add Dependency window, enter the Dependency group name. This name
     refers to this group of application dependencies.

<!-- p.57 -->

   3. In the Add Dependency window, select Add.

   4. In the Specify Required Application window, select an available application and at
     least one of its deployment types to use as a dependency.

         Tip

        Select View to display the properties of the selected application or
        deployment type.

   5. Select OK to close the Specify Required Application window.

   6. If you want the client to automatically install the dependent application, select
     Auto Install next to the dependency.

        ７ Note

        You don't need to deploy a dependent application for the client to
        automatically install it.

   7. If you add more than one dependency, use the Increase Priority and Decrease
     Priority buttons. These actions change the order in which the client evaluates each
     dependency.

   8. Select OK to close the Add Dependency window.

Deployment type Return Codes

  ７ Note

  This page isn't in the Create Deployment Type wizard. It's only a tab on the
  properties of an existing deployment type.

Specify return codes to control behaviors after the deployment type completes. For
example, signal that a restart is required, the installation is complete.

   1. On the Return Codes tab of the deployment type properties window, select Add.

   2. In the Add Return Code window, specify the Return Code Value that you expect
     from this deployment type. This value is any positive or negative integer between
      -2147483648 and 2147483647 .

<!-- p.58 -->

     3. Select a Code Type from the drop-down list. This setting defines how
       Configuration Manager interprets the specified return code from this deployment
       type. The available types vary based on the deployment type technology.

            Success (no reboot): The deployment type successfully installed, and no
            reboot is necessary.

            Failure (no reboot): The deployment type failed to install.

            Hard Reboot: The deployment type successfully installed, but requires the
            device to restart. Nothing else can be installed until the device restarts.

            Soft Reboot: The deployment type successfully installed, but requests the
            device to restart. Other installations can occur before the device restarts.

            Fast Retry: Another installation is already in progress on the device. The client
            retries every two hours, for a total of 10 times.

     4. Optionally, enter a Name and Description for this return code.

     5. Select OK to close the Add Return Code window.

Example: non-zero success

You're deploying an application that returns an exit code of 1 when it successfully
installs. By default, Configuration Manager detects this non-zero return code as a failure.
Specify the Return Code Value of 1 , and select the Code Type of Success (no reboot).
Now Configuration Manager interprets that return code as a success for this
deployment type.

Default return codes
When you create some deployment types, Configuration Manager automatically adds
the following return codes that are common to that technology:

Windows Installer (*.msi file)

                                                                            ﾉ   Expand table

 Value                     Code Type

 0                         Success (no reboot)

 1707                      Success (no reboot)

<!-- p.59 -->

 Value                    Code Type

 3010                     Soft Reboot

 1641                     Hard Reboot

 1618                     Fast Retry

Script Installer

                                                                       ﾉ   Expand table

 Value                    Code Type

 0                        Success (no reboot)

 1641                     Hard Reboot

 3010                     Soft Reboot

 1618                     Fast Retry

Windows app package (*.appx, *.appxbundle, *.msix,
*.msixbundle)

                                                                       ﾉ   Expand table

 Value                                 Code Type

 15605                                 Fast Retry

 15618                                 Fast Retry

Additional options for App-V deployment
types
Configure additional options that are unique to deployment types for virtual
applications (App-V).

App-V deployment type Content options
     1. In the Configuration Manager console, go to the Software Library workspace,
       expand Application Management, and select the Applications node.

<!-- p.60 -->

  2. Select an application with an App-V deployment type, and select Properties.

  3. In the application properties, switch to the Deployment Types tab. Select the App-
     V deployment type, and select Edit.

  4. In the deployment type properties, switch to the Content tab. Configure the
     following options as necessary:

          Persist content in the client cache: The Configuration Manager client won't
          delete from its cache the content for this deployment type.

          Load content into App-V cache before launch: Before the application starts,
          the Configuration Manager client loads into the App-V cache all content for
          this deployment type. The client doesn't pin the content in the cache. It
          deletes the content as necessary.

  5. Select OK to close the deployment type properties. Then select OK to close the
     application properties.

App-V deployment type Publishing options
  1. In the Configuration Manager console, go to the Software Library workspace,
     expand Application Management, and select the Applications node.

  2. Select an application with an App-V deployment type, and select Properties.

  3. In the application properties, switch to the Deployment Types tab. Select the App-
     V deployment type, and select Edit.

  4. In the deployment type properties, switch to the Publishing tab. Select the items in
     the virtual application that you want to publish.

  5. Select OK to close the deployment type properties. Then select OK to close the
     application properties.

Import an application
Use the following procedure to import an application into Configuration Manager:

  1. In the Configuration Manager console, go to the Software Library workspace,
     expand Application Management, and select the Applications node.

  2. In the ribbon, on the Home tab and the Create group, select Import Application.

<!-- p.61 -->

   3. On the General page of the Import Application Wizard, specify the network path to
      the File to import. For example, \\server\share\file.zip . This file is a valid
      compressed archive (ZIP format) of an exported Configuration Manager
      application.

   4. On the File Content page, select the action to take if this application is a duplicate
      of an existing application. Create a new application, or ignore the duplicate and
      add a new revision to the existing application.

   5. On the Summary page, review the actions, and then finish the wizard.

The new application appears in the Applications node.

   Tip

  The Windows PowerShell cmdlet Import-CMApplication has the same function as
  this procedure. For more information, see Import-CMApplication.

For more information about how to export an application, see Management tasks for
applications.

Supported deployment types
Configuration Manager supports the following deployment types for applications:

                                                                                ﾉ   Expand table

 Deployment type name         Description

 Windows Installer (*.msi     A Windows Installer file ( .msi ).
 file)

 Windows app package          Windows app package files ( .appx or .msix ) or Windows app
 (*.appx, *.appxbundle,       bundle packages ( .appxbundle or .msixbundle ).
 *.msix, *.msixbundle)

 Windows app package (in      Specify a link to the app in the Windows Store, or browse the store
 the Windows Store)           to select the app.Note 1

 Script Installer             Specify a script or program that runs on Windows clients to install
                              content or to do an action. Use this deployment type for setup.exe
                              installers or script wrappers.

 Microsoft Application        A Microsoft App-V v4 manifest.
 Virtualization 4

<!-- p.62 -->

 Deployment type name        Description

 Microsoft Application       A Microsoft App-V v5 package file.
 Virtualization 5

 Windows Phone app           A Windows Phone app package file.
 package (*.xap file)

 Windows Phone app           Specify a link to the app in the Windows Store.
 package (in the Windows
 Phone Store)

 macOS X                     For macOS computers running the Configuration Manager client.
                             Create a .cmmac file with the CMAppUtil tool.

 Web Application             Specify a link to a web application. This deployment type installs a
                             shortcut to the web application on the user's device.

 Windows Installer through   Create and deploy Windows Installer-based apps to Windows
 MDM (*.msi)                 devices using on-premises mobile device management (MDM). For
                             more information, see Deploy Windows Installer apps to MDM-
                             enrolled Windows devices.

 Task sequence               Install or uninstall complex applications using task sequences. For
                             more information, see Task sequence deployment type.

  ７ Note

  The Configuration Manager console may display other deployment types, but they
  are for platforms that are no longer supported. For more information, see What
  happened to hybrid?.

Note 1: Windows app package (in the Windows Store)
To deploy the app as a link to the Windows Store, configure the group policy Turn off
the Store application. Set this policy to Disabled or Not configured. If you enable this
setting, clients can't connect to the Windows Store to download and install applications.

Windows clients always evaluate deployment types that use a link to a store before
other deployment types. Then the client evaluates deployment types by priority.

   Tip

  Some store links may cause the following error in the Create Application Wizard:
  "Invalid Application link". For example, some store Featured Apps may cause this

<!-- p.63 -->

  error. You can still select Next on the General page of the wizard. Configuration
  Manager successfully creates the app, and you can successfully deploy it.

Next steps
After creating an application in Configuration Manager, the next step is to deploy the
application.

Create a group of applications that you can send to a user or device collection as a
single deployment. For more information, see Create application groups.

For more information about creating applications on different OS platforms, see the
following articles:

     Create Windows applications
     Create Mac applications
     Create Windows Embedded applications

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.64 -->

Create Mac computer applications with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in January 2022, this feature of Configuration Manager is deprecated. For
  more information, see Mac computers.

Keep the following considerations in mind when you create and deploy applications for
Mac computers.

  ） Important

  The procedures in this topic cover information about deploying applications to Mac
  computers on which you installed the Configuration Manager client. Mac
  computers that you enrolled with Microsoft Intune do not support application
  deployment.

General considerations
You can use Configuration Manager to deploy applications to Mac computers that run
the Configuration Manager Mac client. The steps to deploy software to Mac computers
are similar to the steps to deploy software to Windows computers. However, before you
create and deploy applications for Mac computers that are managed by Configuration
Manager, consider the following:

      Before you can deploy Mac application packages to Mac computers, you must use
      the CMAppUtil tool on a Mac computer to convert these applications into a
      format that can be read by Configuration Manager.

      Configuration Manager does not support the deployment of Mac applications to
      users. Instead, these deployments must be made to a device. Similarly, for Mac
      application deployments, Configuration Manager does not support the Pre-deploy
      software to the user's primary device option on the Deployment Settings page of
      the Deploy Software Wizard.

<!-- p.65 -->

     Mac applications support simulated deployments.

     You cannot deploy applications to Mac computers that have a purpose of
     Available.

     The option to send wake-up packets when you deploy software is not supported
     for Mac computers.

     Mac computers do not support Background Intelligent Transfer Service (BITS) for
     downloading application content. If an application download fails, it is restarted
     from the beginning.

     Configuration Manager does not support global conditions when you create
     deployment types for Mac computers.

Steps to create and deploy an application
The following table provides the steps, details, and information for creating and
deploying applications for Mac computers.

                                                                                  ﾉ    Expand table

 Step                             Details

 Step 1: Prepare Mac              Before you can create Configuration Manager applications from
 applications for Configuration   Mac software packages, you must use the CMAppUtil tool on a
 Manager                          Mac computer to convert the Mac software into a Configuration
                                  Manager.cmmac file.

 Step 2: Create a Configuration   Use the Create Application Wizard to create an application for
 Manager application that         the Mac software.
 contains the Mac software

 Step 3: Create a deployment      This step is required only if you did not automatically import this
 type for the Mac application     information from the application.

 Step 4: Deploy the Mac           Use the Deploy Software Wizard to deploy the application to
 application                      Mac computers.

 Step 5: Monitor the              Monitor the success of application deployments to Mac
 deployment of the Mac            computers.
 application

Supplemental procedures to create and deploy
applications for Mac computers

<!-- p.66 -->

Use the following procedures to create and deploy applications for Mac computers that
are managed by Configuration Manager.

Step 1: Prepare Mac applications for Configuration
Manager
The process for creating and deploying Configuration Manager applications to Mac
computers is similar to the deployment process for Windows computers. However,
before you create Configuration Manager applications that contain Mac deployment
types, you must prepare the applications by using the CMAppUtil tool. This tool is
downloaded with the Mac client installation files. The CMAppUtil tool can gather
information about the application, which includes detection data from the following
Mac packages:

     Apple disk image (.dmg)

     Meta package file (.mpkg)

     macOS X installer package (.pkg)

     macOS X application (.app)

After it gathers application information, the CMAppUtil then creates a file with the
extension .cmmac. This file contains the installation files for the Mac software and
information about detection methods that can be used to evaluate whether the
application is already installed. CMAppUtil can also process .dmg files that contain
multiple Mac applications and create different deployment types for each application.

   1. Copy the Mac software installation package to the folder on the Mac computer
     where you extracted the contents of the macclient.dmg file that you downloaded
     from the Microsoft Download Center.

   2. On the same Mac computer, open a terminal window and navigate to the folder
     where you extracted the contents of the macclient.dmg file.

   3. Navigate to the Tools folder and type the following command-line command:

     ./CMAppUtil <properties>

     For example, say you want to convert the contents of an Apple disk image file
     named MySoftware.dmg that's stored in the user's desktop folder into a cmmac
     file in the same folder. You also want to create cmmac files for all applications that
     are found in the disk image file. To do this, use the following command line:

<!-- p.67 -->

     ./CMApputil –c /Users/ <User Name> /Desktop/MySoftware.dmg -o /Users/
     <User Name> /Desktop -a

       ７ Note

       The application name can't be more than 128 characters.

     To configure options for CMAppUtil, use the command-line properties in the
     following table:

                                                                                   ﾉ   Expand table

      Property    More information

      -h          Displays the available command-line properties.

      -r          Outputs the detection.xml of the provided .cmmac file to stdout. The output
                  contains the detection parameters and the version of CMAppUtil that was used
                  to create the .cmmac file.

      -c          Specifies the source file to be converted.

      -o          Specifies the output path in conjunction with the –c property.

      -a          Automatically creates .cmmac files in conjunction with the –c property for all
                  applications and packages in the disk image file.

      -s          Skips generating the detection.xml if no detection parameters are found and
                  forces the creation of the .cmmac file without the detection.xml file.

      -v          Displays more detailed output from the CMAppUtil tool together with
                  diagnostic information.

  4. Ensure that the .cmmac file has been created in the output folder that you
     specified.

Create a Configuration Manager application that contains
the Mac software
Use the following procedure to help you create an application for Mac computers that
are managed by Configuration Manager.

  1. In the Configuration Manager console, choose Software Library > Application
     Management > Applications.

  2. On the Home tab, in the Create group, choose Create Application.

<!-- p.68 -->

3. On the General page of the Create Application Wizard, select Automatically
  detect information about this application from installation files.

    ７ Note

    If you want to specify information about the application yourself, select
    Manually specify the application information. For more information about
    how to manually specify the information, see How to create applications with
    Configuration Manager.

4. In the Type drop-down list, select Mac OS X.

5. In the Location field, specify the UNC path in the form \\<server>\<share>\
  <filename> to the Mac application installation file (.cmmac file) that will detect
  application information. Alternatively, choose Browse to browse to and specify the
  installation file location.

    ７ Note

    You must have access to the UNC path that contains the application.

6. Choose Next.

7. On the Import Information page of the Create Application Wizard, review the
  information that was imported. If necessary, you can choose Previous to go back
  and correct any errors. Choose Next to proceed.

8. On the General Information page of the Create Application Wizard, specify
  information about the application such as the application name, comments,
  version, and an optional reference to help you reference the application in the
  Configuration Manager console.

    ７ Note

    Some of the application information might already be on this page if it was
    previously obtained from the application installation files.

9. Choose Next, review the application information on the Summary page, and then
  complete the Create Application Wizard.

<!-- p.69 -->

 10. The new application is displayed in the Applications node of the Configuration
     Manager console.

Step 3: Create a deployment type for the Mac application
Use the following procedure to help you create a deployment type for Mac computers
that are managed by Configuration Manager.

  ７ Note

  If you automatically imported information about the application in the Create
  Application Wizard, a deployment type for the application might already have
  been created.

  1. In the Configuration Manager console, choose Software Library > Application
     Management > Applications.

  2. Select an application. Then, on the Home tab, in the Application group, choose
     Create Deployment Type to create a new deployment type for this application.

       ７ Note

       You can also start the Create Deployment Type Wizard from the Create
       Application Wizard and from the Deployment Types tab of the <application
       name> Properties dialog box.

  3. On the General page of the Create Deployment Type Wizard, in the Type drop-
     down list, select Mac OS X.

  4. In the Location field, specify the UNC path in the form \\<server>\<share>\
     <filename> to the application installation file (.cmmac file). Alternatively, choose
     Browse to browse to and specify the installation file location.

       ７ Note

       You must have access to the UNC path that contains the application.

  5. Choose Next.

  6. On the Import Information page of the Create Deployment Type Wizard, review
     the information that was imported. If necessary, choose Previous to go back and

<!-- p.70 -->

   correct any errors. Choose Next to continue.

 7. On the General Information page of the Create Deployment Type Wizard, specify
   information about the application such as the application name, comments, and
   the languages in which the deployment type is available.

      ７ Note

      Some of the deployment type information might already be on this page if it
      was previously obtained from the application installation files.

 8. Choose Next.

 9. On the Requirements page of the Create Deployment Type Wizard, you can
   specify the conditions that must be met before the deployment type can be
   installed on Mac computers.

10. Choose Add to open the Create Requirement dialog box and add a new
   requirement.

      ７ Note

      You can also add new requirements on the Requirements tab of the
      <deployment type name> Properties dialog box.

11. From the Category drop-down list, select that this requirement is for a device.

12. From the Condition drop-down list, select the condition that you want to use to
   assess whether the Mac computer meets the installation requirements. The
   contents of this list varies depending on the category that you select.

13. From the Operator drop-down list, choose the operator to use to compare the
   selected condition to the specified value to assess whether the user or device
   meets the installation requirements. The available operators vary depending on the
   selected condition.

14. In the Value field, specify the values to use with the selected condition and
   operator to assess whether the user or device meets in the installation
   requirement. The available values vary depending on the condition and operator
   that you select.

15. Choose OK to save the requirement rule and exit the Create Requirement dialog
   box.

<!-- p.71 -->

 16. On the Requirements page of the Create Deployment Type Wizard, choose Next.

 17. On the Summary page of the Create Deployment Type Wizard, review the actions
     for the wizard to take. If necessary, choose Previous to go back and change
     deployment type settings. Choose Next to create the deployment type.

 18. After the Progress page finishes, review the actions that have been taken, and then
     choose Close to complete the Create Deployment Type Wizard.

 19. If you started this wizard from the Create Application Wizard, you will return to
     the Deployment Types page.

Deploy the Mac application
The steps to deploy an application to Mac computers are the same as the steps to
deploy an application to Windows computers, except for the following differences:

     The deployment of applications to users is not supported.

     Deployments that have a purpose of Available are not supported.

     The Pre-deploy software to the user's primary device option on the Deployment
     Settings page of the Deploy Software Wizard is not supported.

     Because Mac computers do not support Software Center, the setting User
     notifications on the User Experience page of the Deploy Software Wizard is
     ignored.

     The option to send wake-up packets when you deploy software is not supported
     for Mac computers.

  ７ Note

  You can build a collection that contains only Mac computers. To do so, create a
  collection that uses a query rule and use the example WQL query in the How to
  create queries topic.

For more information, see Deploy applications.

Step 5: Monitor the deployment of the Mac application
You can use the same process to monitor application deployments to Mac computers as
you would to monitor application deployments to Windows computers.

<!-- p.72 -->

For more information, see Monitor applications.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.73 -->

Create Windows applications in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

In addition to the other Configuration Manager requirements and procedures for
creating an application, also take the following considerations into account when you
create and deploy applications for Windows devices.

General considerations
Configuration Manager supports the deployment of Windows app package ( .appx ) and
app bundle ( .appxbundle ) formats.

When you create an application in the Configuration Manager console, select the
application installation file Type as Windows app package (*.appx, *.appxbundle,
*.msix, *.msixbundle). For more information on creating apps in general, see Create
applications. For more information on the MSIX format, see Support for MSIX format.

  ７ Note

  To take advantage of new Configuration Manager features, first update clients to
  the latest version. While new functionality appears in the Configuration Manager
  console when you update the site and console, the complete scenario isn't
  functional until the client version is also the latest.

Provision Windows app packages for all users
on a device
Provision an application with a Windows app package for all users on the device. One
common example of this scenario is provisioning an app from the Microsoft Store for
Business and Education, like Minecraft: Education Edition, to all devices used by students
in a school. Previously, Configuration Manager only supported installing these
applications per user. After signing in to a new device, a student would have to wait to
access an app. Now when the app is provisioned to the device for all users, they can be
productive more quickly.

<!-- p.74 -->

  ） Important

  Be careful with installing, provisioning, and updating different versions of the same
  Windows app package on a device, which may cause unexpected results. This
  behavior may occur when using Configuration Manager to provision the app, but
  then allowing users to update the app from the Microsoft Store. For more
  information, see the next step guidance when you Manage apps from the
  Microsoft Store for Business.

When deploying offline apps to Windows devices with the Configuration Manager
client, don't allow users to update applications external to Configuration Manager
deployments. Control of updates to offline apps is especially important in multi-user
environments such as classrooms. For more information, see Manage apps from the
Microsoft Store for Business and Education with Configuration Manager.

Configuration Manager supports app provisioning on all supported versions of
Windows 10 and later.

To configure a Windows app deployment type for this feature, enable the option to
Provision this application for all users on the device. For more information, see Create
applications.

  ７ Note

  If you need to uninstall a provisioned application from devices to which users have
  already signed on, you need to create two uninstall deployments. Target the first
  uninstall deployment to a device collection that contains the devices. Target the
  second uninstall deployment to a user collection that contains the users who have
  already signed on to devices with the provisioned application. When uninstalling a
  provisioned app on a device, Windows currently doesn't uninstall that app for users
  as well.

Support for MSIX format
Configuration Manager supports the Windows app package ( .msix ) and app bundle
( .msixbundle ) formats. Supported versions of Windows 10 and later support these
formats.

     For an overview of MSIX, see A closer look at MSIX.

<!-- p.75 -->

     For how to create a new MSIX app, see MSIX support introduced in Insider Build
     17682    .

Convert applications to MSIX
Convert your existing Windows Installer (.msi) applications to the MSIX format.

Prerequisites for MSIX
     A reference device running Windows 10 version 1809 or later

     Sign in to Windows on this device as a user with local administrative rights

     Install the following apps on this device:

        Configuration Manager console

        Install the MSIX Packaging Tool     from the Microsoft Store

        Install the MSIX packaging tool driver

Don't install any other apps or services on this device. It's your reference system.

Process to convert applications to MSIX format

   1. Elevate the Configuration Manager console, go to the Software Library workspace,
     expand Application Management, and select the Applications node.

   2. Select an application that has a Windows Installer ( .msi ) deployment type.

        ７ Note

        You need to be able to access the application's source content from the
        reference device.

        The application's name can't have any special characters. Configuration
        Manager uses the app name as the name of the output file.

        Don't install this application on the reference device in advance.

   3. Select Convert to .MSIX in the ribbon.

When the wizard completes, the MSIX Packaging Tool creates an MSIX file in the
location you specified in the wizard. During this process, Configuration Manager silently

<!-- p.76 -->

installs the application on the reference device.

If the process fails, the summary page points to the log file with more information. If
there's an error about capturing user state, sign out of Windows. Signing in again may
resolve this issue.

To use this MSIX app, you first need to digitally sign it so that clients trust it. For more
information on this process, see the following articles:

     MSIX - The MSIX Packaging Tool - signing the MSIX package
     How to sign an app package using SignTool

After signing the app, create a new deployment type on the application in Configuration
Manager. For more information, see Create deployment types for the application.

Task sequence deployment type

  ７ Note

  In this version of Configuration Manager, the task sequence deployment type is a
  pre-release feature. To enable it, see Pre-release features.

You can install complex applications using task sequences via the application model.
Add a task sequence deployment type to an app either to install or uninstall the app.
This deployment type provides the following behaviors:

     Display the app task sequence with an icon in Software Center. An icon makes it
     easier for users to find and identify the app task sequence.

     Define additional metadata for the app task sequence, including localized
     information

     Starting in version 2010, deploy an app task sequence to a user collection

You can only add a non-OS deployment task sequence as a deployment type on an app.
High-impact, OS deployment, or OS upgrade task sequences aren't supported. A user-
targeted deployment still runs in the context of the local System account.

When you add this deployment type to an app, configure its properties on the Task
Sequence page. For more information, see Deployment type Task Sequence options.

Starting in version 2006, use the following Windows PowerShell cmdlets to add and
configure a task sequence deployment type:

<!-- p.77 -->

     Add-CMTaskSequenceDeploymentType
     Set-CMTaskSequenceDeploymentType

  ７ Note

  Consider the following scenario:

       An application has a task sequence deployment type.
       It's deployed as available.
       A device has maintenance windows defined.
       A user on the device runs the deployment in Software Center outside of a
       maintenance window.

  Configuration Manager honors the user's intent to install the application, even
  though there's no available maintenance window. In version 2107 and earlier, when
  the task sequence ran, the Restart Computer step would fail because of the
  maintenance window.

  Starting in version 2111, this step now ignores maintenance windows only when the
  task sequence is run as an app deployment type.

Prerequisites for a task sequence deployment type
Create a custom task sequence:

     Use only non-OS deployment steps, for example: Install Package, Run Command
     Line, or Run PowerShell Script. For more information including the full list of
     supported steps, see Create a task sequence for non-OS deployments.

     On the task sequence properties, User Notification tab, don't select the option for
     a high-impact task sequence.

When you create the application, to add a task sequence deployment type, your user
account needs permission to read task sequences. Use one of the following options to
configure these permissions:

     Add the app administrator's user account to the built-in Read-Only Analyst role.
     This role allows them to view all Configuration Manager objects.

     Copy the built-in Application Administrator role to create a custom role. Add the
     Read permission on the Task Sequence Package object.

<!-- p.78 -->

Known issues for a task sequence deployment type
     Don't use the Install Application step in this task sequence. Use the Install Package
     step to install apps.

     In version 2006 and earlier, you can't yet deploy an app task sequence to a user
     collection. This issue was resolved in version 2010.

Support for Universal Windows Platform (UWP)
apps
Windows 10 or later devices don't require a sideloading key to install line-of-business
apps. To enable sideloading on Windows, however, the registry key
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Appx\AllowAllTrustedApps

must have a value of 1.

If you don't configure this registry key, Configuration Manager automatically sets this
value to 1 the first time you deploy an app to the device. If you've set this value to 0,
Configuration Manager can't automatically change the value, and your line-of-business
app deployment fails.

Digitally sign UWP line-of-business apps. Use a code-signing certificate that's trusted on
each device to which you deploy the app. Use certificates from your organization's PKI,
or purchase a certificate from a third-party provider whose public root certificate is
already trusted by Windows.

To sign mobile app packages, use the following table to determine the type of code-
signing certificate to use:

                                                                           ﾉ   Expand table

 Package                                                            Symantec   Non-
                                                                               Symantec

 Universal .appx packages on Windows 10 Mobile devices              Yes        Yes

 .xap packages                                                      Yes        No

 .appx packages built for Windows Phone 8.1 to install on Windows   Yes        No
 10 Mobile devices

<!-- p.79 -->

Deploy Windows Installer apps to MDM-
enrolled Windows 10 devices
The Windows Installer through MDM (*.msi) deployment type lets you create and
deploy Windows Installer-based apps to MDM-enrolled devices running Windows 10 or
later.

When you use this deployment type, consider the following points:

         Only upload a single file with the MSI extension.

         Configuration Manager uses the file's product code and product version for app
         detection.

         Windows uses the app's default restart behavior. Configuration Manager doesn't
         control the app restart behavior.

         Per-user MSI packages are installed for a single user.

         Per-machine MSI packages are installed for all users of the device.

         Configuration Manager supports app updates. The MSI product code of each
         version must be the same.

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.80 -->

Create Windows Embedded applications
with Configuration Manager
Article • 01/12/2024

Applies to: Configuration Manager (current branch)

In addition to the other Configuration Manager requirements and procedures for
creating an application, you must also take the following considerations into account
when you create and deploy applications for Windows Embedded devices.

General considerations
      When you deploy applications to Windows Embedded devices that are enabled for
      write filtering, you can specify whether to disable the write filter on the device
      during the app deployment. You can then choose to restart the write filter after the
      app deployment. If the write filter isn't disabled, the software is deployed to a
      temporary overlay. This means that unless another deployment forces changes to
      persist, the software will no longer be installed when the device restarts.

      When you deploy an application to a Windows Embedded device, make sure that
      the device is a member of a collection that has a configured maintenance window.
      This lets you manage when the write filter is disabled and enabled, and when the
      device restarts.

      The setting that controls the write filter behavior is a check box named Commit
      changes at deadline or during a maintenance window (requires restarts).

Tips for deploying applications
Use required applications rather than available applications for Windows Embedded
devices that have write filters enabled. Because users can't install apps from Software
Center on a Windows Embedded device that has write filters enabled, always deploy
applications with a deployment purpose of required rather than available to these
devices. Typically, this isn't a problem because computers that run a Windows
Embedded operating system often run a single application that must run in the same
way for multiple users. Because of this, these devices are highly managed and locked
down by the IT department. Required applications are well-suited to this scenario.

However, if users do run more than one application on embedded devices when write
filters are enabled, educate these users about the following limitations:
