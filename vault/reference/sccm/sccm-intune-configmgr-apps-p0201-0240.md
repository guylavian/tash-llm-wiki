---
title: "App management documentation — pages 201-240"
type: reference
domain: sccm
slug: sccm-intune-configmgr-apps-p0201-0240
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-apps-p0201-0240
family: sccm
documentKind: "doc"
abstract: "documentation. Feedback Was this page helpful?  Yes  No Provide product feedback Manage apps from the Microsoft Store for Business and Education with Configuration Manager Article • 04/11/2023 ） Important Starting in November 2021, this feature of Configuration Manager is depr"
---

# App management documentation — pages 201-240

<!-- p.201 -->

documentation.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.202 -->

Manage apps from the Microsoft Store
for Business and Education with
Configuration Manager
Article • 04/11/2023

  ） Important

  Starting in November 2021, this feature of Configuration Manager is deprecated.
  For more information, see Update to Intune integration with the Microsoft Store
  on Windows        .

The Microsoft Store for Business and Education is where you find and acquire Windows
apps for your organization. When you connect the store to Configuration Manager, you
then synchronize the list of apps you've acquired. View these apps in the Configuration
Manager console, and deploy them like you deploy any other app.

Online and offline apps
The Microsoft Store for Business and Education supports two types of app:

      Online: This license type requires users and devices to connect to the store to get
      an app and its license. Devices running Windows 10 or later should be Microsoft
      Entra joined or Microsoft Entra hybrid joined. They can also be Microsoft Entra
      registered.

      Offline: This type lets you cache apps and licenses to deploy directly within your
      on-premises network. Devices don't need to connect to the store or have a
      connection to the internet.

For more information, see the Microsoft Store for Business and Education overview.

Summary of capabilities
Configuration Manager supports managing Microsoft Store for Business and Education
apps on devices running Windows 10 or later with the Configuration Manager client.
Configuration Manager offers the following capabilities for online and offline apps:

                                                                         ﾉ   Expand table

<!-- p.203 -->

 Capability                                                    Offline apps   Online apps

 Synchronize app data to Configuration Manager                 Yes            Yes
 (synchronization occurs every 24 hours)

 Create Configuration Manager applications from store apps     Yes            Yes

 Support for free apps from the store                          Yes            Yes

 Support for paid apps from the store                          No             YesNote 1

 Support required deployments to user or device collections    Yes            Yes

 Support available deployments to user or device collections   Yes            Yes

 Support line-of-business apps from the store                  Yes            Yes

 Provision a store app for all users on a deviceNote 2         Yes            Yes

Note 1: Online licensed apps version requirement
To deploy online licensed apps to Windows devices with the Configuration Manager
client, they need to be running a supported version of Windows 10 or later.

Note 2: Provision Windows app packages for all users on a device
For more information, see Create Windows applications.

Deploying online apps using the Microsoft Store for
Business and Education to devices that run the
Configuration Manager client
Before deploying Microsoft Store for Business and Education apps to devices that run
the full Configuration Manager client, consider the following points:

     For full functionality, devices need to be running a supported version of Windows
     10 or later.

     Register or join devices to the same Microsoft Entra tenant where you registered
     the Microsoft Store for Business and Education as a management tool.

     When the local Administrator account signs in on the device, it can't access
     Microsoft Store for Business and Education apps.

<!-- p.204 -->

     Devices need a live internet connection to the Microsoft Store for Business and
     Education. For more information including proxy configuration, see Prerequisites.

Set up synchronization
When you synchronize the list of Microsoft Store for Business and Education apps that
your organization acquired, you see these apps in the Configuration Manager console.

Connect your Configuration Manager site to Microsoft Entra ID and the Microsoft Store
for Business and Education. For more information and details of this process, see
Configure Azure services. Create a connection to the Microsoft Store for Business
service.

Make sure the service connection point and targeted devices can access the cloud
service. For more information, see Prerequisites for Microsoft Store for Business and
Education - Proxy configuration.

Supplemental information and configuration
On the App page of the Azure Services Wizard, first configure the Azure environment
and Web app. Then read the More Information section at the bottom of the page. This
information includes the following other actions in the Microsoft Store for Business and
Education portal:

     Configure Configuration Manager as the store management tool. For more
     information, see Configure management provider.

     Enable support for offline licensed apps. For more information, see Distribute
     offline apps.

     Acquire at least one app. For more information, see Find and acquire apps.

On the Configurations page of the Azure Services Wizard, specify the following
information:

     Path to Microsoft Store for Business app content storage: Specify a shared
     network path, including a folder. For example, \\server\share\folder . When the
     site server syncs with the store, it caches content in this location. When you create
     an application in Configuration Manager, the site server copies the app content
     from this local cache to the site's content library.

     Selected languages: Select the languages to sync from the store and display to
     users in Software Center. For example, if the user configures Windows for German,

<!-- p.205 -->

     then Software Center shows German strings for the store app. This behavior
     requires that language to be synchronized, and to exist for the specific application.

     Default language: If the user's language is unavailable, select a default language
     to use.

  ７ Note

  Configuration Manager doesn't synchronize the app icon from the store. If you
  need an icon to display for this app in Software Center, manually add it in the app
  properties. For more information, see Manually specify application information.

Create and deploy the app
After synchronization, create and deploy the Microsoft Store for Business and Education
apps similar to any other Configuration Manager application.

   1. In the Software Library workspace of the Configuration Manager console, expand
     Application Management, then select the License Information for Store Apps
     node.

   2. Choose the app you want to deploy, then select Create Application in the ribbon.

The site creates a Configuration Manager application containing the Microsoft Store for
Business and Education app.

Then deploy and monitor this application as you would any other Configuration
Manager application. For more information, see the following articles:

     Deploy applications
     Monitor applications from the console

Manage the app
In the Software Library workspace, expand Application Management, then select the
License Information for Store Apps node.

For each store app you manage, view the following information about the app:

     App name
     App platform
     The number of licenses for the app that you own

<!-- p.206 -->

     The number of available licenses

After deploying online apps, any updates to that app come directly from the Microsoft
Store. Furthermore, Configuration Manager doesn't check version compliance of online
apps, just that Windows reports the app as installed.

When deploying offline apps to Windows devices with the Configuration Manager
client, don't allow users to update applications external to Configuration Manager
deployments. Control of updates to offline apps is especially important in multi-user
environments such as classrooms. One option to disable the Microsoft Store is by using
group policy.

After the Microsoft Store for Business and Education administrator acquires an offline
app, don't publish the app to users via the store. This configuration makes sure that
users can't install or update online. Users only receive offline app updates via
Configuration Manager.

Next steps
Troubleshoot the Microsoft Store for Business and Education integration with
Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.207 -->

Create App-V virtual environments in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

In a Microsoft Application Virtualization (App-V) virtual environment in Configuration
Manager, deployed virtual applications can share the same file system and registry on
client Windows PCs. Unlike standard virtual applications, these applications can share
data with each other. Virtual environments are created or modified on client PCs when
the application is installed or when clients next evaluate their installed applications. You
can order these applications so that when multiple applications try to modify a file
system or registry value, the application with the highest order takes priority.

  ） Important

  Do not rely on App-V virtual environments to provide security protection, such as
  from malware.

Use the following procedure to create an App-V virtual environment in Configuration
Manager.

Create an App-V virtual environment
   1. In the Configuration Manager console, choose Software Library > Application
      Management > App-V Virtual Environments.

   2. On the Home tab, in the Create group, choose Create Virtual Environment.

   3. In the Create Virtual Environment dialog box, enter the following information:

            Name. Enter a unique name for the virtual environment (maximum 128
            characters).

            Description. (Optional) Enter a description for the virtual environment.

   4. To add a new deployment type to the virtual environment, choose Add. You must
      add at least one deployment type.

   5. In the Add Applications dialog box, specify a Group name (maximum 128
      characters). You'll use this name to refer to the group of applications that you add

<!-- p.208 -->

     to the virtual environment.

   6. Choose Add, select the App-V 5 applications and deployment types that you want
     to add to the group, and then choose OK.

   7. In the Add Applications dialog box, you can select Increase Order or Decrease
     Order to set the application that takes priority if multiple applications attempt to
     modify file system or registry settings in the same virtual environment.

   8. To return to the Create Virtual Environment dialog box, choose OK.

   9. When you're done adding groups, choose OK to create the virtual environment.
     The new virtual environment is displayed in the App-V Virtual Environments node
     of the Configuration Manager console. You can monitor the status of your virtual
     environments by using the App-V Virtual Environment Status report.

        ７ Note

        The virtual environment is added or modified on client PCs when the
        application is installed or when the client next evaluates installed applications.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.209 -->

Import and export applications
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use Configuration Manager to import and export applications between two hierarchies.
For example, copy an application from a test environment to a production environment.

Export
   1. In the Configuration Manager console, select the Applications node. In the Create
      group of the ribbon, choose Export Application.

   2. On the General screen, enter a path to a new ZIP file to export into. Optionally,
      specify whether to export dependencies, supersedence relationships, conditions, and
      virtual environments, and content for the selected applications and dependencies.
      Enter any necessary administrator comments, and select Next.

   3. Verify the application and any dependencies are listed on the Related Objects
      page and select Next.

   4. On the Summary page, select Next.

   5. Once the process completes, it creates the ZIP file, and you can close the wizard.

  ） Important

  If you're going to copy this application to another environment, take both the ZIP
  file and the folder that accompanies it. The ZIP file must exist in the same directory
  as the created folder.

Import

  ７ Note

  You can only import applications from UNC paths, you can't directly import from
  your local disk.

   1. In the Configuration Manager console, select the Applications node. In the Create
      group of the ribbon, choose Import Application.

<!-- p.210 -->

   2. Choose the ZIP file that you'd like to import and select Next.

   3. The File Content window shows what happens when you import the application.
     Select Next.

   4. Review the summary screen and select Next.

   5. Close the wizard. The application is now available in the site.

   Tip

  Starting in version 2010, when you import an object in the Configuration Manager
  console, it now imports to the current folder. Previously, Configuration Manager
  always put imported objects in the root node.

Automation
If you want to automate the import and export of applications, use the following
PowerShell cmdlets:

     Import-CMApplication

     Export-CMApplication

Next steps
Deploy applications

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.211 -->

Revise and supersede applications in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Learn how to work with Configuration Manager application versions and how to
supersede applications with a new version.

Revisions
When you make revisions to an application or a deployment type, Configuration
Manager creates a new revision of the application. You can display the history of each
application revision. You can also view its properties, restore a previous revision of an
application, or delete an old revision.

Display the history of application revisions
   1. In the Configuration Manager console, go to the Software Library workspace,
      expand Application Management, and select the Applications node. Then choose
      the application that you want.

   2. On the Home tab of the ribbon, in the Application group, select Revision History.
      This action opens the Application Revision History window.

View an application revision
   1. In the Application Revision History window, select an application revision, and
      then select View.

   2. In the Properties dialog box, examine the properties of the selected application.

        ７ Note

        This view of application properties is read-only.

Restore an application revision

<!-- p.212 -->

   1. In the Application Revision History window, select an application revision, and
     then select Restore.

   2. Select Yes to restore the selected application revision.

Delete an application revision
   1. In the Application Revision History window, select an application revision, and
     then select Delete.

   2. Select Yes to confirm.

  ） Important

  You can only delete the current application revision after you retire the application
  and it has no references.

Supersedence
Application management in Configuration Manager lets you upgrade or replace existing
applications by using a supersedence relationship. When you supersede an application,
you specify a new deployment type to replace the deployment type of the superseded
application. You can also decide whether to upgrade or uninstall the superseded
application before the client installs the superseding application. It's best to limit
supersedence chains to five levels deep at a maximum.

  ） Important

  When you choose the option to uninstall the superseded deployment type, a
  deployment type can't be superseded by a deployment type that was deployed to
  a different type of collection. For example, a deployment type that was deployed to
  a device collection can't be superseded by a deployment type that was deployed to
  a user collection.

Decide whether to upgrade or replace an application
The type of supersedence depends on whether you select the Uninstall option:

     If you want to update to a newer version of the same application with the same
     application ID, don't select Uninstall.

<!-- p.213 -->

     If you want to change to a different application with a different application ID,
     select Uninstall. You need to remove the superseded version of the application.

Supersede dependent applications
In this example, main application refers to the app that you're deploying that has the
dependencies.

You can create a supersedence relationship that updates the dependent application to a
new version.

   1. Make sure that the new dependent application and the original dependent
     application are in the same dependency group of the main application.

   2. Create a supersedence relationship that supersedes the original dependent
     application with the new dependent application.

During new installations of the main application, the client installs the new dependent
application. Configuration Manager updates existing installations of the main
application with the new dependent application.

The end result is that all deployments of the main application use the new dependent
application.

Further considerations
     You can specify multiple supersedence relationships for dependent applications.
     Configuration Manager installs the highest dependent application in the
     supersedence chain.

     Deploy dependent applications to the device where the main application is
     installed. Otherwise Configuration Manager won't install the dependent
     application.

     For new installations of the main application, when you have multiple
     dependencies, the dependency order determines which version of the dependent
     application gets installed.

Specify a supersedence relationship
   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Application Management, and select the Applications node. Then choose
     the application that supersedes another application.

<!-- p.214 -->

 2. On the Home tab of the ribbon, in the Properties group, select Properties.

 3. Switch to the Supersedence tab, and select Add.

 4. For the Superseded Application, select Browse.

 5. Choose the application that you want to supersede, and then select OK.

 6. In the Specify Supersedence Relationship window, select the deployment type
   that replaces the deployment type of the superseded application.

     ７ Note

     By default, the new deployment type doesn't uninstall the deployment type of
     the superseded application. This scenario is commonly used when you want
     to deploy an upgrade to an existing application. To remove the existing
     deployment type before the new deployment type is installed, select
     Uninstall. If you decide to upgrade an application, make sure that you test
     this in a lab environment first.

 7. If you want users to still see in Software Center deployments for both applications,
   select the option to Allow users to see deployments for this application and all
   applications that it supersedes in Software Center.. With this option, you give
   users the choice to still install an older version of the app if needed. By default, this
   option isn't selected, so only the superseding application displays in Software
   Center. This option is only for available deployments to user collections.

 8. Select OK to save your changes and close the windows.

Display applications that supersede the current
application
 1. In the Configuration Manager console, go to the Software Library workspace,
   expand Application Management, and select the Applications node. Then choose
   the application that you want.

 2. On the Home tab of the ribbon, in the Properties group, select Properties.

 3. Switch to the References tab.

 4. For the Relationship type, choose Applications that supersede this application.

View supersedence relationships

<!-- p.215 -->

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Application Management, and select the Applications node. Then choose
     the application that you want.

   2. On the Home tab of the ribbon, in the Relationships group, select View
     relationships, and then select Supersedence.

This action shows a graphical diagram of the relationships of the selected application to
other applications. For the supersedence relationships, it shows applications that the
selected application supersedes, and applications that the selected application is
superseded by.

Manage supersedence with PowerShell
You can add, view, and remove supersedence relationships using the following
PowerShell cmdlets:

     Get-CMDeploymentTypeSupersedence
     Set-CMApplicationSupersedence

Next steps
Uninstall applications

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.216 -->

Uninstall applications with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Instead of needing to create a separate object to uninstall an application, you can
specify uninstall behaviors on the deployment type. Then create a separate deployment
with the action to uninstall. You can uninstall an application even if it wasn't previously
installed by Configuration Manager.

Behaviors and limitations
      To deploy an application with the Uninstall action, first delete any existing
      application deployments, simulated deployments, or task sequence deployments
      that include this application. Otherwise Configuration Manager may reinstall the
      application.

      Some application types don't support uninstallation.

      When you uninstall an application, Configuration Manager doesn't automatically
      uninstall dependencies.

      If you deploy to a user an application with the Uninstall action, and the application
      was installed for all users of the computer, the uninstall might fail if the user's
      account doesn't have permissions to uninstall the application.

      In version 2103 and earlier, if you remove a user or a device from a collection that
      has an application deployed to it, Configuration Manager doesn't automatically
      uninstall the application from the device.

         Tip

        Version 2107 and later supports Implicit uninstall.

      A deployment with the Uninstall action doesn't check requirement rules. If the
      application is installed on the target device, Configuration Manager uninstalls it.

Process

<!-- p.217 -->

When you create the application, select the option to Automatically identify
information about this deployment type from installation files. If the information is
available in the installation files, the uninstall command line is automatically added to
the deployment type properties.

For an existing application, use the following steps to configure its uninstall properties:

   1. In the Configuration Manager console, go to the Software Library workspace.
     Expand Application Management and select the Applications node.

   2. Select the application. In the details pane, switch to the Deployment Types tab.

   3. Select the deployment type. Then in the ribbon, on the Deployment Type tab,
     select Properties.

   4. Switch to the Content tab and configure the following settings:

           Uninstall content settings: Select an option for where Configuration Manager
           gets the content to uninstall the application:

              Same as install content: The install and uninstall content are the same.
              This option is the default.

              No uninstall content: Your application doesn't need content for uninstall.

              Different from install content: The uninstall content is different from the
              install content.

           Uninstall content location: If you select the third option for content settings,
           specify the network path to the content that's used to uninstall the
           application.

   5. Switch to the Programs tab and configure the following settings:

           Uninstall program: Specify the command line and any required parameters
           to uninstall the application.

           Uninstall start in: Optionally specify the folder that has the uninstall program
           for the deployment type. This folder can be an absolute path on the client. It
           can also be a relative path on a distribution point of the folder with the
           package.

           Run installation and uninstall program as 32-bit process on 64-bit clients:
           Use the 32-bit file and registry locations on Windows-based computers to
           run the uninstall program for the deployment type.

<!-- p.218 -->

Then deploy the application. On the Deployment Settings page of the wizard, select the
deployment action to Uninstall.

  ７ Note

  When you select a deployment action of Uninstall, the deployment purpose is
  automatically configured as Required.

Implicit uninstall
Many customers have lots of collections because for every application they need at least
two collections: one for install and another for uninstall. This practice adds overhead of
managing more collections, and can reduce site performance for collection evaluation.

Starting in version 2107, you can enable an application deployment to support implicit
uninstall. If a resource is in a collection, the application installs. Then when you remove
the resource from the collection, the application uninstalls.

Starting in version 2111, this behavior also supports application groups. When this
article refers to an application, it also applies to app groups.

  ７ Note

  In version 2111 and later, this behavior applies to deployments to device or user
  collections. In version 2107, this behavior only applies to deployments to device
  collections.

Starting in version 2203, if you deploy an application or app group to a user collection
that's based on a security group, and you enable implicit uninstall, changes to the
security group are now honored. When the site discovers the change in group
membership, Configuration Manager uninstalls the app for the user that you removed
from the security group.

Enable implicit uninstall
When you deploy the application to a collection, configure the following settings on the
Deployment Settings page:

     Action: Install

     Purpose: Required

<!-- p.219 -->

     Enable the following option: When a resource is no longer a member of the
     collection, uninstall the application

        Tip

       In version 2107, this option is named: Uninstall this application if the
       targeted object falls out of the collection

  ） Important

  Be careful with enabling this option on deployments to large query-based
  collections. Especially queries to external sources like Active Directory groups. An
  unexpected external change could automatically trigger a large number of devices
  to uninstall the application.

Implicit uninstall process
After you remove the resource from the collection, the following process happens:

     A background worker process runs on the site server every 10 minutes. This task
     keeps track of apps for which you've enabled this option. It then detects resources
     that you removed from the target collection. To help you troubleshoot this
     process, view the SMS_ImplicitUninstall.log file on the site server.

     The client needs to download policy. By default, the client policy polling interval
     client setting is 60 minutes. To accelerate this step, manually download policy.

     15 minutes after the client receives the updated policy, it uninstalls the app.

Depending upon the timing of those steps, the longest time period for the client to
uninstall the app is 85 minutes. If the first step happens immediately, and you manually
download policy on the device, the overall process is 15 minutes.

  ７ Note

       For this behavior, the site can process up to 1000 collection membership
       changes every 10 minutes.
       If the uninstall doesn't occur, it's likely that there's a conflicting install
       deployment of the same application, application group, or a different

<!-- p.220 -->

        application group with the same apps. Configuration Manager always honors
        an install deployment over an uninstall deployment.

Known issues
You configure an app's installation behavior to Install for system, and then deploy it to a
user collection. A device has multiple users who are both in the collection, and the app
installs on the device. If you then remove one user from the collection, the app is
uninstalled from the device for all users.

Next steps
How to manage collections

Monitor applications from the Configuration Manager console

Log file reference

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.221 -->

Create and run PowerShell scripts from
the Configuration Manager console
Article • 12/16/2024

Applies to: Configuration Manager (current branch)

Configuration Manager has an integrated ability to run PowerShell scripts. PowerShell
has the benefit of creating sophisticated, automated scripts that are understood and
shared with a larger community. The scripts simplify building custom tools to administer
software and let you accomplish mundane tasks quickly, allowing you to get large jobs
done more easily and more consistently.

  ７ Note

  In version 2006 and earlier, Configuration Manager doesn't enable this optional
  feature by default. You must enable this feature before using it. For more
  information, see Enable optional features from updates.

With this integration in Configuration Manager, you can use the Run Scripts functionality
to do the following things:

      Create and edit scripts for use with Configuration Manager.
      Manage script usage through roles and security scopes.
      Folder support for scripts.
      Run scripts on collections or individual on-premises managed Windows PCs.
      Schedule scripts' runtime in UTC on collections or individual on-premises managed
      Windows PCs.
      Get rapid aggregated script results from client devices.
      Monitor script execution and view reporting results from script output.

  ２ Warning

        Given the power of scripts, we remind you to be intentional and careful with
        their usage. We have built in additional safeguards to assist you; segregated
        roles and scopes. Be sure to validate the accuracy of scripts before running
        them and confirm they are from a trusted source, to prevent unintended
        script execution. Be mindful of extended characters or other obfuscation and
        educate yourself about securing scripts. Learn more about PowerShell script
        security

<!-- p.222 -->

        Certain anti-malware software may inadvertently trigger events against the
        Configuration Manager Run Scripts or CMPivot features. It is recommended to
        exclude %windir%\CCM\ScriptStore so that the anti-malware software permits
        those features to run without interference.

Prerequisites
     To run PowerShell scripts, the client must be running PowerShell version 3.0 or
     later. However, if a script you run contains functionality from a later version of
     PowerShell, the client on which you run the script must be running that version of
     PowerShell.
     Configuration Manager clients must be running the client from the 1706 release, or
     later in order to run scripts.
     To use scripts, you must be a member of the appropriate Configuration Manager
     security role.
     To import and author scripts - Your account must have Create permissions for SMS
     Scripts.
     To approve or deny scripts - Your account must have Approve permissions for SMS
     Scripts.
     To run scripts - Your account must have Run Script permissions for Collections.

For more information about Configuration Manager security roles:
Security scopes for run scripts
Security roles for run scripts
Fundamentals of role-based administration.

Limitations
Run Scripts currently supports:

     Scripting languages: PowerShell
     Parameter types: integer, string, and list.

  ２ Warning

  Be aware that when using parameters, it opens a surface area for potential
  PowerShell injection attack risk. There are various ways to mitigate and work
  around, such as using regular expressions to validate parameter input or using
  predefined parameters. Common best practice is not to include secrets in your

<!-- p.223 -->

  PowerShell scripts (no passwords, etc.). Learn more about PowerShell script
  security

Run Script authors and approvers
Run Scripts uses the concept of script authors and script approvers as separate roles for
implementation and execution of a script. Having the author and approver roles
separated allows an important process check for the powerful tool that Run Scripts is.
There's an additional script runners role that allows execution of scripts, but not creation
or approval of scripts. See Create security roles for scripts.

Scripts roles control
By default, users can't approve a script they've authored. Because scripts are powerful,
versatile, and potentially deployed to many devices, you can separate the roles between
the person that authors the script and the person that approves the script. These roles
give an additional level of security against running a script without oversight. You're able
to turn off secondary approval, for ease of testing.

Approve or Deny a script
Scripts must be approved, by the script approver role, before they can be run. To
approve a script:

   1. In the Configuration Manager console, click Software Library.
   2. In the Software Library workspace, click Scripts.
   3. In the Script list, choose the script you want to approve or deny and then, on the
     Home tab, in the Script group, click Approve/Deny.
   4. In the Approve or deny script dialog box, select Approve, or Deny for the script.
     Optionally, enter a comment about your decision. If you deny a script, it can't be

<!-- p.224 -->

     run on client devices.

   5. Complete the wizard. In the Script list, you see the Approval State column change
     depending on the action you took.

Allow users to approve their own scripts
This approval is primarily used for the testing phase of script development.

   1. In the Configuration Manager console, click Administration.
   2. In the Administration workspace, expand Site Configuration, and then click Sites.
   3. In the list of sites, choose your site and then, on the Home tab, in the Sites group,
     click Hierarchy Settings.
   4. On the General tab of the Hierarchy Settings Properties dialog box, clear the
     checkbox Script authors require additional script approver.

  ） Important

<!-- p.225 -->

  As a best practice, you shouldn't allow a script author to approve their own scripts.
  It should only be allowed in a lab setting. Carefully consider the potential impact of
  changing this setting in a production environment.

Security scopes
Run Scripts uses security scopes, an existing feature of Configuration Manager, to
control scripts authoring and execution through assigning tags that represent user
groups. For more information on using security scopes, see Configure role-based
administration for Configuration Manager.

Create security roles for scripts
The three security roles used for running scripts aren't created by default in
Configuration Manager. To create the script runners, script authors, and script approvers
roles, follow the outlined steps.

   1. In the Configuration Manager console, go to Administration >Security >Security
        Roles
   2. Right-click on a role and click Copy. The role you copy has permissions already
        assigned. Make sure you take only the permissions that you want.
   3. Give the custom role a Name and a Description.
   4. Assign the security role the permissions outlined below.

Security Role Permissions
Role Name: Script Runners

        Description: These permissions enable this role to only run scripts that were
        previously created and approved by other roles.
        Permissions: Ensure the following are set to Yes.

                                                                           ﾉ     Expand table

 Category                              Permission                        State

 Collection                            Run Script                        Yes

 Site                                  Read                              Yes

 SMS Scripts                           Read                              Yes

<!-- p.226 -->

Role Name: Script Authors

        Description: These permissions enable this role to author scripts, but they can't
        approve or run them.
        Permissions: Ensure the following permissions are set.

                                                                           ﾉ      Expand table

 Category                              Permission                         State

 Collection                            Run Script                         No

 Site                                  Read                               Yes

 SMS Scripts                           Create                             Yes

 SMS Scripts                           Read                               Yes

 SMS Scripts                           Delete                             Yes

 SMS Scripts                           Modify                             Yes

Role Name: Script Approvers

        Description: These permissions enable this role to approve scripts, but they can't
        create or run them.
        Permissions: Ensure the following permissions are set.

                                                                           ﾉ      Expand table

 Category                              Permission                         State

 Collection                            Run Script                         No

 Site                                  Read                               Yes

 SMS Scripts                           Read                               Yes

 SMS Scripts                           Approve                            Yes

 SMS Scripts                           Modify                             Yes

Example of SMS Scripts permissions for the script authors role

<!-- p.227 -->

Folder support for scripts
Starting in version 2403, you can organize scripts by using folders. This change allows
for better categorization and management of scripts.

Open the Configuration Manager console and go to the Software Library workspace.
From the ribbon or right-click menu, in the Scripts, select from the following options:

     Create Folder
     Delete Folder
     Rename Folder
     Move Folders
     Set Security Scopes

Create a script
   1. In the Configuration Manager console, click Software Library.
   2. In the Software Library workspace, click Scripts.
   3. On the Home tab, in the Create group, click Create Script.
   4. On the Script page of the Create Script wizard, configure the following settings:

           Script Name - Enter a name for the script. Although you can create multiple
           scripts with the same name, using duplicate names makes it harder for you to
           find the script you need in the Configuration Manager console.
           Script language - Currently, only PowerShell scripts are supported.
           Import - Import a PowerShell script into the console. The script is displayed
           in the Script field.

<!-- p.228 -->

           Clear - Removes the current script from the Script field.
           Script - Displays the currently imported script. You can edit the script in this
           field as necessary.
   5. Complete the wizard. The new script is displayed in the Script list with a status of
     Waiting for approval. Before you can run this script on client devices, you must
     approve it.

  ） Important

  Avoid scripting a device reboot or a restart of the Configuration Manager agent
  when using the Run Scripts feature. Doing so could lead to a continuous rebooting
  state. If needed, there are enhancements to the client notification feature that
  enable restarting devices. The pending restart column can help identify devices
  that need a restart.

Script parameters
Adding parameters to a script provides increased flexibility for your work. You can
include up to 10 parameters. The following outlines the Run Scripts feature's current
capability with script parameters for; String, Integer data types. Lists of preset values are
also available. If your script has unsupported data types, you get a warning.

In the Create Script dialog, click Script Parameters under Script.

Each of your script's parameters has its own dialog for adding further details and
validation. If there's a default parameter in the script, it will be enumerated in the
parameter UI and you can set it. Configuration Manager won't overwrite the default
value since it will never modify the script directly. You can think of this as "pre-
populated suggested values" are provided in the UI, but Configuration Manager doesn't
provide access to "default" values at run-time. This can be worked around by editing the
script to have the correct defaults.

  ） Important

  Parameter values can't contain a single quote.

  There is a known issue where parameter values that include or are enclosed in
  single quotes don't get passed to the script properly. When specifying default
  parameter values containing a space within a script, use double quotes instead.
  When specifying default parameter values during creation or execution of a Script,

<!-- p.229 -->

  surrounding the default value in either double or single quotes is not necessary
  regardless of whether the value contains a space or not.

Parameter validation
Each parameter in your script has a Script Parameter Properties dialog for you to add
validation for that parameter. After adding validation, you should get errors if you're
entering a value for a parameter that doesn't meet its validation.

Example: FirstName
In this example, you're able to set the properties of the string parameter, FirstName.

The validation section of the Script Parameter Properties dialog contains the following
fields for your use:

     Minimum Length - minimum number of characters of the FirstName field.
     Maximum Length- maximum number of characters of the FirstName field

<!-- p.230 -->

         RegEx - short for Regular Expression. For more information on using the Regular
         Expression, see the next section, Using Regular Expression validation.
         Custom Error - useful for adding your own custom error message that supersedes
         any system validation error messages.

Using Regular Expression validation

A regular expression is a compact form of programming for checking a string of
characters against an encoded validation. For example, you could check for the absence
of a capital alphabetic character in the FirstName field by placing [^A-Z] in the RegEx
field.

The regular expression processing for this dialog is supported by the .NET Framework.
For guidance on using regular expressions, see .NET Regular Expression and Regular
Expression Language.

Script examples
Here are a couple examples that illustrate scripts you might want to use with this
capability.

Create a new folder and file
This script creates a new folder and a file within the folder, given your naming input.

  PowerShell

   Param(
   [Parameter(Mandatory=$True)]
   [string]$FolderName,
   [Parameter(Mandatory=$True)]
   [string]$FileName
   )

   New-Item $FolderName -type directory
   New-Item $FileName -type file

Get OS Version
This script uses WMI to query the machine for its OS version.

  PowerShell

<!-- p.231 -->

  Write-Output (Get-WmiObject -Class Win32_operatingSystem).Caption

Edit or copy PowerShell scripts
You can Edit or Copy an existing PowerShell script used with the Run Scripts feature.
Instead of recreating a script that you need to change, now directly edit it. Both actions
use the same wizard experience as when you create a new script. When you edit or copy
a script, Configuration Manager doesn't persist the approval state.

   Tip

  Don't edit a script that's actively running on clients. They won't finish running the
  original script, and you may not get the intended results from these clients.

Edit a script
   1. Go to the Scripts node under the Software Library workspace.
   2. Select the script to edit, then click Edit in the ribbon.
   3. Change or reimport your script in the Script Details page.
   4. Click Next to view the Summary then Close when you're finished editing.

Copy a script
   1. Go to the Scripts node under the Software Library workspace.
   2. Select the script to copy, then click Copy in the ribbon.
   3. Rename the script in the Script name field and make any additional edits you may
     need.
   4. Click Next to view the Summary then Close when you're finished editing.

Run a script
After a script is approved, it can be run against a single device or a collection. Once
execution of your script begins, it's launched quickly through a high priority system that
times out in one hour. The results of the script are then returned using a state message
system.

To select a collection of targets for your script:

   1. In the Configuration Manager console, click Assets and Compliance.

<!-- p.232 -->

   2. In the Assets and Compliance workspace, click Device Collections.
   3. In the Device Collections list, click the collection of devices on which you want to
     run the script.
   4. Select a collection of your choice, click Run Script.
   5. On the Script page of the Run Script wizard, choose a script from the list. Only
     approved scripts are shown.
   6. Click Next, and then complete the wizard.

  ） Important

  If a script does not run, for example because a target device is turned off during the
  one hour time period, you must run it again.

Schedule scripts' runtime
Starting in Configuration Manager current branch version 2309, you can now schedule
scripts' runtime in UTC.

Schedule script execution on a collection:

   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, click Device Collections.

   3. In the Device Collections list, click the collection of devices on which you want to
     schedule the script.

   4. Select a collection of your choice, click Run Script.

   5. On the Scheduling page, Schedule the script to be run at checkbox and specify the
     Schedule Time in UTC.

   6. Verify the details that are displayed on the summary page.

   7. Click Next, and then complete the wizard.

<!-- p.233 -->

  ７ Note

  A max of twenty five scheduled scripts will be proccessed in every 5 minutes.

Target machine execution
The script is executed as the system or computer account on the targeted client(s). This
account has limited network access. Any access to remote systems and locations by the
script must be provisioned accordingly.

Script monitoring
After you have initiated running a script on a collection of devices, use the following
procedure to monitor the operation. You are able to monitor a script in real time as it
executes, and later return to the status and results for a given Run Script execution.
Script status data is cleaned up as part of the Delete Aged Client Operations
maintenance task or deletion of the script.

<!-- p.234 -->

1. In the Configuration Manager console, click Monitoring.

2. In the Monitoring workspace, click Script Status.

3. In the Script Status list, you view the results for each script you ran on client
  devices. A script exit code of 0 generally indicates that the script ran successfully.

<!-- p.235 -->

Schedule script Monitoring on a collection
 1. In the Configuration Manager console, click Monitoring.

 2. In the Monitoring workspace, click Scheduled Scripts node.

 3. A new row will be displayed in the list of Scheduled Scripts.

 4. Verify a new row has been displayed in the list of Scheduled Scripts. The state
   column should have the value Scheduled. The ClientOperationId column should
   be blank. Verify that the other columns like Script Name, Schedule Time etc. have
   appropriate values.

 5. After the Schedule Time, refresh the Scheduled Scripts node. The state column
   should have the value Successfully initiated client operation. The
   ClientOperationId column should have an integer value.

 6. In the Monitoring workspace, click Script Status node.Verify new row has been
   displayed in the list and the ClientOperationId is equal to the ClientOperationId
   from the Scheduled Scripts node.

 7. Click on View Status and ensure that the script output displays.

<!-- p.236 -->

Script output
Client's return script output using JSON formatting by piping the script's results to the
ConvertTo-Json cmdlet. The JSON format consistently returns readable script output. For
scripts that do not return objects as output, the ConvertTo-Json cmdlet converts the
output to a simple string that the client returns instead of JSON.

     Scripts that get an unknown result, or where the client was offline, won't show in
     the charts or data set.

     Avoid returning large script output since it's truncated to 4 KB.

     Convert an enum object to a string value in scripts so they're properly displayed in
     JSON formatting.

You can view detailed script output in raw or structured JSON format. This formatting
makes the output easier to read and analyze. If the script returns valid JSON-formatted
text or the output can be converted to JSON using the ConvertTo-Json PowerShell
cmdlet, then view the detailed output as either JSON Output or Raw Output. Otherwise
the only option is Script Output.

<!-- p.237 -->

Example: Script output is convertible to valid JSON
Command: $PSVersionTable.PSVersion

  Output

  Major      Minor   Build   Revision
  -----      -----   -----   --------
  5          1       16299   551

Example: Script output isn't valid JSON
Command: Write-Output (Get-WmiObject -Class Win32_OperatingSystem).Caption

  Output

  Microsoft Windows 10 Enterprise

Log files
     On the client, by default in C:\Windows\CCM\logs:
           Scripts.log
           CcmMessaging.log

     On the MP, by default in C:\SMS_CCM\Logs:
           MP_RelayMsgMgr.log

     On the site server, by default in C:\Program Files\Configuration Manager\Logs:
           SMS_Message_Processing_Engine.log

Automate with Windows PowerShell
You can use the following PowerShell cmdlets to automate some of these tasks:

     Approve-CMScript
     Deny-CMScript
     Get-CMScript
     Invoke-CMScript
     New-CMScript
     Remove-CMScript
     Set-CMScript

<!-- p.238 -->

See also
     Configure role-based administration for Configuration Manager
     Fundamentals of role-based administration

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.239 -->

Learn more about PowerShell script
security
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

It's the administrator's responsibility to validate proposed PowerShell and PowerShell
parameter usage in their environment. Here are some helpful resources to help educate
administrators about the power of PowerShell and potential risk surfaces. This guidance
is to help you mitigate potential risk surfaces and allow safe scripts to be used.

PowerShell Script Security
The Configuration Manager scripts feature lets you visually review and approve scripts.
Another administrator can request that their script is allowed. Administrators should be
aware PowerShell scripts can have obfuscated scripts. An obfuscated script could be
malicious and difficult to detect with visual inspection during the script approval
process. Visually review PowerShell scripts and use inspection tools to help detect
suspicious script issues. These tools can't always determine the PowerShell author's
intent, so it can bring attention to a suspicious script. However, the tools will require the
administrator to judge if it's malicious or intentional script syntax.

Recommendations
      Familiarize yourself with PowerShell security guidance using the various links
      referenced below.
      Sign your scripts: Another method for keeping scripts secure is by having them
      vetted and then signed, before importing them for usage.
      Don't store secrets (such as passwords) in PowerShell scripts and learn more about
      how to handle secrets.

General information about PowerShell security
This collection of links was chosen to give Configuration Manager administrators a
starting point for learning about PowerShell script security recommendations.

Defending Against PowerShell Attacks

Protecting Against Malicious Code Injection

<!-- p.240 -->

PowerShell - The Blue Team, discusses Deep Script block logging, Protected Event
Logging, Antimalware Scan Interface, and Secure Code Generation APIs

API for anti-malware scan interface

PowerShell parameters security
Passing parameters is a way to have flexibility with your scripts and defer decisions until
run time. It also opens up another risk surface.

The following list includes recommendations to prevent malicious parameters or script
injection:

     Only allow usage of pre-defined parameters.
     Use the regular expression feature, to validate parameters that are allowed.
         Example: If only a certain range of values are allowed, use a regular expression
         to check for only those characters or values that can make up the range.
         Validating parameters can help prevent users trying use certain characters that
         can be escaped, like quotes. There can be multiple types of quotes, so using
         regular expressions to validate which characters you've decided are permissible
         is often easier than trying to define all the inputs that not permissible.
     Use the PowerShell module "injection hunter"         in the PowerShell Gallery.
         There can be false positives, so look for intent when something is flagged as
         suspicious to determine if it's a real issue or not.
     Microsoft Visual Studio has a script analyzer, that can assist with checking
     PowerShell syntax.

The following video titled: "DEF CON 25 - Lee Holmes - Get $pwnd: Attacking Battle
Hardened Windows Server" gives an overview of the types of issues that you can secure
against (especially the section 12:20 to 17:50):
https://www.youtube-nocookie.com/embed/ahxMOAAani8

Environment recommendations
The following list includes general recommendations for PowerShell administrators:

     Deploy the latest version of PowerShell, such as version 5 or later, which is built
     into Windows 10 or later. You can also deploy the Windows Management
     Framework      .
     Enable, and collect PowerShell logs, optionally including Protected Event Logging.
     Incorporate these logs into your signatures, hunting, and incident response
     workflows.
