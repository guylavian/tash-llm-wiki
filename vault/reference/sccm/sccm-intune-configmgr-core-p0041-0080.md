---
title: "Core infrastructure documentation — pages 41-80"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0041-0080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0041-0080
family: sccm
documentKind: "doc"
abstract: "feature is available only for \"User Available\" apps. Also, admins can make the Featured tab of Software Center as the default tab from Client Settings. If an app is marked as Featured and it's deployed to a User Collection as an Available app, it will show under the Featured piv"
---

# Core infrastructure documentation — pages 41-80

<!-- p.41 -->

feature is available only for "User Available" apps. Also, admins can make the Featured
tab of Software Center as the default tab from Client Settings.

If an app is marked as Featured and it's deployed to a User Collection as an Available
app, it will show under the Featured pivot in Software Center.

                                                                                     

Updates

                                                                                     

Select the Updates tab (1) to view and install software updates that your IT admin
deploys to this computer.

     All (2): Shows all updates that you can install

     Required (3): Your IT admin enforces these updates.

<!-- p.42 -->

      Sort by (4): Rearrange the list of updates. By default this list sorts by Application
      name: A to Z.

      Search (5): Still can't find what you're looking for? Enter keywords in the Search
      box to find it!

To install updates, select Install All (6).

To only install specific updates, select the icon to enter multi-select mode (7):    Check
the updates to install, and then select Install Selected.

Operating Systems

                                                                                        

Select the Operating Systems tab (1) to view and install versions of Windows that your
IT admin deploys to this computer.

      All (2): Shows all Windows versions that you can install

      Required (3): Your IT admin enforces these upgrades.

      Sort by (4): Rearrange the list of updates. By default this list sorts by Application
      name: A to Z.

      Search (5): Still can't find what you're looking for? Enter keywords in the Search
      box to find it!

Installation status
Select the Installation status tab to view the status of applications. You may see the
following states:

      Installed: Software Center already installed this application on this computer.

      Downloading: Software Center is downloading the software to install on this
      computer.

      Failed: Software Center wasn't able to install the software.

<!-- p.43 -->

     Scheduled to install after: Shows the date and time of the device's next
     maintenance window to install upcoming software. Maintenance windows are
     defined by your IT admin.

        The status can be seen in the All and the Upcoming tab.

        You can install before the maintenance window time by selecting the Install
        Now button.

Device compliance
Select the Device compliance tab to view the compliance status of this computer.

Select Check compliance to evaluate this device's settings against the security policies
defined by your IT admin.

Options
Select the Options tab to view additional settings for this computer.

Work information
Indicate the hours that you typically work. Your IT admin may schedule software
installations outside your business hours. Allow at least four hours each day for system
maintenance tasks. Your IT admin can still install critical applications and software
updates during business hours.

     Select the earliest and latest hours that you use this computer. By default these
     values are from 5:00 AM through 10:00 PM.

     Select the days of the week that you typically use this computer. By default
     Software Center only selects the weekdays.

Specify whether you regularly use this computer to do your work. Your administrator
might automatically install applications or make additional applications available to
primary computers. If the computer you're using is a primary computer, select I
regularly use this computer to do my work.

Power management
Your IT admin may set power management policies. These policies help your
organization conserve electricity when this computer isn't in use.

<!-- p.44 -->

To make this computer exempt from these policies, select Do not apply power settings
from my IT department to this computer. By default this setting is disabled and the
computer applies power settings.

Computer maintenance
Specify how Software Center applies changes to software before the deadline.

     Automatically install or uninstall required software and restart the computer
     only outside of the specified business hours: This setting is disabled by default.

     Suspend Software Center activities when my computer is in presentation mode:
     This setting is enabled by default.

  ７ Note

  These settings are designed to be managed by end users and do not impact
  deployment deadlines.

When instructed by your IT admin, select Sync Policy. This computer checks with the
servers for anything new, such as applications, software updates, or operating systems.

Remote Control
Specify remote access and remote control settings for your computer.

Use remote access settings from your IT department: By default, your IT department
defines the settings to remotely assist you. The other settings in this section show the
state of the settings that your IT department defines. To change any settings, first
disable this option.

     Level of remote access allowed
        Do not allow remote access: IT administrators can't remotely access this
        computer to assist you.
        View only: An IT administrator can only remotely view your screen.
        Full: An IT administrator can remotely control this computer. This setting is the
        default option.

     Allow remote control of this computer by administrators when I am away. This
     setting is Yes by default.

     When an administrator tries to control this computer remotely

<!-- p.45 -->

        Ask for permission each time: This setting is the default option.
        Do not ask for permission

     Show the following during remote control: These visual notifications are both
     enabled by default to let you know that an administrator is remotely accessing the
     device.
        Status icon in the notification area
        A session connection bar on the desktop

     Play sound: This audible notification lets you know that an administrator is
     remotely accessing the device.
        When session begins and ends: This setting is the default option.
        Repeatedly during session
        Never

Custom tabs
Your IT admin can remove the default tabs or add additional tabs to Software Center.
Custom tabs are named by your admin, and they open a web site that the admin
specifies. For instance, you might have a tab called "Help Desk" that opens your IT
organization's help desk web site.

More information for IT administrators
More information is available for IT administrators on how to plan for and configure
Software Center in the following articles:

     Plan for Software Center
     Software Center client settings
     Device restart notifications
     Introduction to Remote Control

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.46 -->

How to use the Configuration Manager
console
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

Administrators use the Configuration Manager console to manage the Configuration
Manager environment. This article covers the fundamentals of navigating the console.

Open the console
The Configuration Manager console is always installed on every site server. You can also
install it on other computers. For more information, see Install the Configuration
Manager console.

The simplest method to open the console on a Windows computer is to go to Start and
start typing Configuration Manager console . You may not need to type the entire string
for Windows to find the best match.

If you browse the Start menu, look for the Configuration Manager console icon in the
Microsoft Endpoint Manager group.

Connect to a site server
The console connects to your central administration site server or to your primary site
servers. You can't connect a Configuration Manager console to a secondary site. During
installation, you specified the fully qualified domain name (FQDN) of the site server to
which the console connects.

<!-- p.47 -->

To connect to a different site server, use the following steps:

   1. Select the arrow at the top of the ribbon, and choose Connect to a New Site.

   2. Type in the FQDN of the site server. If you've previous session to site server, select
     the server from the drop-down list.

   3. Select Connect.

   Tip

  You can specify the minimum authentication level for administrators to access
  Configuration Manager sites. This feature enforces administrators to sign in to
  Windows with the required level. For more information, see Plan for the SMS
  Provider.

Navigation
Some areas of the console may not be visible depending on your assigned security role.
For more information about roles, see Fundamentals of role-based administration.

Workspaces
The Configuration Manager console has four workspaces:

<!-- p.48 -->

     Assets and Compliance

     Software Library

     Monitoring

     Administration

Reorder workspace buttons by selecting the down arrow and choosing Navigation Pane
Options. Select an item to Move Up or Move Down. Select Reset to restore the default
button order.

Minimize a workspace button by selecting Show Fewer Buttons. The last workspace in
the list is minimized first. Select a minimized button and choose Show More Buttons to
restore the button to its original size.

Nodes

<!-- p.49 -->

Workspaces are a collection of nodes. One example of a node is the Software Update
Groups node in the Software Library workspace.

Once you are in the node, you can select the arrow to minimize the navigation pane.

Use the navigation bar to move around the console when you minimize the navigation
pane.

In the console, nodes are sometimes organized into folders. When you select the folder,
it usually displays a navigation index or a dashboard.

  ７ Note

  You can use PowerShell to manage console folders with the following cmdlets:

<!-- p.50 -->

       Get-CMFolder
       New-CMFolder
       Remove-CMFolder
       Set-CMFolder

Ribbon
The ribbon is at the top of the Configuration Manager console. The ribbon can have
more than one tab and can be minimized using the arrow on the right. The buttons on
the ribbon change based on the node. Most of the buttons in the ribbon are also
available on context menus.

Details pane
You can get additional information about items by reviewing the details pane. The
details pane can have one or more tabs. The tabs vary depending on the node.

Columns
You can add, remove, reorder, and resize columns. These actions allow you to display
the data you prefer. Available columns vary depending on the node. To add or remove a

<!-- p.51 -->

column from your view, right-click on an existing column heading and select an item.
Reorder columns by dragging the column heading where you would like it to be.

At the bottom of the column context menu, you can sort or group by a column.
Additionally, you can sort by a column by selecting its header.

Reclaim lock for editing objects
If the Configuration Manager console stops responding, you can be locked out of
making further changes until the lock expires after 30 minutes. This lock is part of the
Configuration Manager SEDO (Serialized Editing of Distributed Objects) system. For
more information, see Configuration Manager SEDO.

You can clear your lock on any object in the Configuration Manager console. This action
only applies to your user account that has the lock, and on the same device from which
the site granted the lock. When you attempt to access a locked object, you can now
Discard Changes, and continue editing the object. These changes would be lost anyway
when the lock expired.

<!-- p.52 -->

View recently connected consoles
You can view the most recent connections for the Configuration Manager console. The
view includes active connections and those connections that recently connected. You'll
always see your current console connection in the list and you only see connections
from the Configuration Manager console. You won't see PowerShell or other SDK-based
connections to the SMS Provider. The site removes instances from the list that are older
than 30 days.

Prerequisites to view connected consoles
     Your account needs the Read permission on the SMS_Site object.

     Configure the administration service REST API. For more information, see What is
     the administration service?.

View connected consoles
   1. In the Configuration Manager console, go to the Administration workspace.

   2. Expand Security and select the Console Connections node.

   3. View the recent connections, with the following properties:

          User name
          Machine name
          Connected site code
          Console version
          Last connected time: When the user last opened the console
          An open console in the foreground sends a heartbeat every 10 minutes,
          which shows in the Last Console Heartbeat column.

<!-- p.53 -->

Start Microsoft Teams Chat from Console
Connections
You can message other Configuration Manager administrators from the Console
Connections node using Microsoft Teams. When you choose to Start Microsoft Teams
Chat with an administrator, Microsoft Teams is launched and a chat is opened with the
user.

Prerequisites
        For starting a chat with an administrator, the account you want to chat with needs
        to have been discovered with Microsoft Entra ID or AD User Discovery.
        Microsoft Teams installed on the device from which you run the console. note
        All prerequisites to view connected consoles

Start Microsoft Teams Chat
   1. Go to Administration > Security > Console Connections.
   2. Right-click on a user's console connection and select Start Microsoft Teams Chat.

             If the User Principal Name isn't found for the selected administrator, Start
             Microsoft Teams Chat is grayed out.
             An error message, including a download link, appears if Microsoft Teams isn't
             installed on the device from which you run the console.
             If Microsoft Teams is installed on the device from which you run the console,
             it will open a chat with the user.

<!-- p.54 -->

Known issues
The error message notifying you that Microsoft Teams isn't installed won't be displayed
if the following Registry key doesn't exist:

Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Unins
tall

To work around the issue, manually create the Registry key.

In-console documentation dashboard
The Documentation node in the Community workspace includes information about
Configuration Manager documentation and support articles. It includes the following
sections:

       Recommended: a manually curated list of important articles.
       Troubleshooting articles: guided walkthroughs to assist with troubleshooting
       Configuration Manager components and features.
       New and updated support articles: articles that are recently new or updated.

Troubleshooting connection errors
The Documentation node has no explicit proxy configuration. It uses any OS-defined
proxy in the Internet Options control panel applet. To retry after a connection error,
refresh the Documentation node.

Dark theme for the console
(Introduced in version 2203)

Starting in version 2203, the Configuration Manager console offers a dark theme. To use
the theme, select the arrow from the top left of the ribbon, then choose Switch console
theme. Select Switch console theme again to return to the light theme. As of version
2303, the main screen of the console and delete secondary site wizards adhere to the
dark theme.

<!-- p.55 -->

Known issue
     Console restart is required on doing the theme switch, as the node navigation
     pane might not properly render when you move to a new workspace.
     Currently, there are locations in the console that may not display the dark theme
     correctly. We are continuously working to improve the dark theme.

Connect via Windows PowerShell
The Configuration Manager console includes a PowerShell module with over a thousand
cmdlets to interact programmatically from the command line. Select the arrow at the
top of the ribbon, and choose Connect via Windows PowerShell.

For more information, see Get started with Configuration Manager cmdlets.

Command-line options
The Configuration Manager console has the following command-line options:

                                                                       ﾉ   Expand table

<!-- p.56 -->

 Option                    Description

 /sms:debugview=1          A DebugView is included in all ResultViews that specify a view.
                           DebugView shows raw properties (names and values).

 /sms:NamespaceView=1      Shows namespace view in the console.

 /sms:ResetSettings        The console ignores user-persisted connection and view states. The
                           window size isn't reset.

 /sms:IgnoreExtensions     Disables any Configuration Manager extensions.

 /sms:NoRestore            The console ignores previous persisted node navigation.

 /server=[ServerName]      Connect to a CAS or Primary site server by specifying the fully qualified
                           domain name (FQDN) or server name for that site.

Next steps
     Console notifications
     Console tips
     Accessibility features
     Task sequence editor

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.57 -->

Configuration Manager console
notifications
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Configuration Manager console notifies you for specific events that occur. You can
configure some of the event notifications for your Configuration Manager sites.

      Non-configurable event notifications:
         When an update is available for Configuration Manager itself
         When lifecycle and maintenance events occur in the environment
      Configurable event notifications:
         Non-critical site health changes
         Messages from Microsoft

This notification is a bar at the top of the console window below the ribbon. It replaces
the previous experience when Configuration Manager updates are available. These in-
console notifications still display critical information, but don't interfere with your work
in the console. You can't dismiss critical notifications. The console displays all
notifications in a new notification area of the title bar.

About console notifications
Notifications follow the permissions of role-based administration. For example, if a user
doesn't have permissions to see Configuration Manager updates, they won't see those
notifications.

Some notifications have a related action. For example, if the console version doesn't
match the site version, select Install the new console version. This action launches the
console installer.

The following notifications reevaluate every five minutes:

      Site is in maintenance mode

<!-- p.58 -->

     Site is in recovery mode
     Site is in upgrade mode

The following notifications are most applicable to the technical preview branch:

     Evaluation version is within 30 days of expiration (Warning): the current date is
     within 30 days of the expiration date of the evaluation version
     Evaluation version is expired (Critical): the current date is past the expiration date
     of the evaluation version
     Console version mismatch (Critical): the console version doesn't match the site
     version
     Site upgrade is available (Warning): there's a new update package available

Most console notifications are per session. The console evaluates queries when a user
launches it. To see changes in the notifications, restart the console. If a user dismisses a
non-critical notification, it notifies again when the console restarts if it's still applicable.

     Dismissing or snoozing a notification is persistent for your user across consoles
     starting in version 2010.

Console notification improvements

Improvements starting in version 2010
Starting in Configuration Manager 2010, you have an updated look and feel for in-
console notifications. Notifications are more readable and the action link is easier to
find. The age of the notification is displayed to help you find the latest information. If
you dismiss or snooze a notification, that action is now persistent for your user across
consoles.

Right-click or select ... on the notification to take one of the following actions:

     Translate text: Launches Bing Translator        for the text.
     Copy text: Copies the notification text to the clipboard.
     Snooze: Snoozes the notification for the specified duration:
         One hour
         One day
         One week
         One month
     Dismiss: Dismisses the notification.

<!-- p.59 -->

To see these improvements for notifications, update the Configuration Manager console
to the latest version.

New notifications in version 2010

To help you manage security risk in your environment, you'll be notified in-console
about devices with operating systems that are past the end of support date and that are
no longer eligible to receive security updates.

Environments with the following operating systems installed on client devices receive a
notification:

     Windows 7, Windows Server 2008 (non-Azure), and Windows Server 2008 R2 (non-
     Azure) without ESU.
         Selecting More info takes you to the Management insights Security group to
         review the Update clients running Windows 7 and Windows Server 2008 rule.

     Versions of Windows 10 Semi-Annual Channel that are past the end-of-support
     date for Enterprise and Education and Home and Pro editions.
         Selecting More info takes you to the Management insights Simplified
         Management group to review the Update clients to a supported Windows 10
         version rule.

You can also view the Product Lifecycle Dashboard to see information about which
operating systems are out of support. This information (such as the support lifecycle for
Windows 10 versions) is provided for your convenience and only for use internally within

<!-- p.60 -->

your company. You should not solely rely on this information to confirm update
compliance. Be sure to verify the accuracy of the information provided to you.

Improvements starting in version 2006
        You have an option to receive Messages from Microsoft
        If you configure Azure services to cloud-attach your site, you'll see notifications
        with an action to renew the secret key. The site evaluates the state of the following
        alerts once per hour:
          One or more Microsoft Entra app secret keys will expire soon
          One or more Microsoft Entra app secret keys have expired

   ） Important

   When you use an imported Microsoft Entra app, you aren't notified of an
   upcoming expiration date from console notifications.

Configure a site to show non-critical
notifications
You can configure each site to show non-critical notifications in the properties of the
site.

   1. In the Administration workspace, expand Site Configuration, then select the Sites
        node.
   2. Select the site you want to configure for non-critical notifications.
   3. In the ribbon, select Properties.
   4. On the Alerts tab, select the option to Enable console notifications for non-
        critical site health changes.

             If you enable this setting, all console users see critical, warning, and
             information notifications. This setting is enabled by default.
             If you disable this setting, console users only see critical notifications.

Configure a site to receive messages from
Microsoft
Starting in version 2006, you can choose to receive notifications from Microsoft in the
Configuration Manager console. These notifications help you stay informed about new

<!-- p.61 -->

or updated features, changes to Configuration Manager and attached services, and
issues that require action to remediate.

  ７ Note

  For push notifications from Microsoft to show in the console, the service
  connection point needs access to configmgrbits.azureedge.net . It also needs
  access to this endpoint for updates and servicing, so you may have already
  allowed it.

Configure notification settings for Microsoft messages
   1. Navigate to Administration > Site Configuration > Sites.

   2. Select a site, and then in the ribbon, select Properties.

   3. In the Alerts tab, enable the notifications by selecting Receive messages from
     Microsoft. You can deselect any of the following notifications if you prefer not to
     receive them:

           Prevent/fix: Known issues affecting your organization that may require you to
           take action.

           Plan for change: Changes to Configuration Manager that may require you to
           take action.

           Stay informed: Informs you of new or updated features that are available.

<!-- p.62 -->

                                                                                  

Console extension installation notifications
(Introduced in version 2103)

Users are notified when console extensions are approved for installation. These
notifications occur for users in the following scenarios:

     The Configuration Manager console requires a built-in extension, such as
     WebView2, to be installed or updated.
     Console extensions are approved and notifications are enabled from
     Administration > Overview > Updates and Servicing > Console Extensions.
        When notifications are enabled, users within the security scope for the
        extension receive the following prompts:

   1. In the upper-right corner of the console, select the bell icon to display
     Configuration Manager console notifications.

<!-- p.63 -->

  2. The notification will say New custom console extensions are available.

  3. Select the link Install custom console extensions to launch the install.

  4. When the install completes, select Close to restart the console and enable the new
     extension.

  ７ Note

  When you upgrade to Configuration Manager 2107, you will be prompted to install
  the WebView2 console extension again. For more information about the WebView2
  installation, see the WebView2 installation section if the Community hub article.

For more information, see Manage console extensions.

Log files

<!-- p.64 -->

For more information and troubleshooting assistance, see the SmsAdminUI.log file on
the console computer. By default, this log file is at the following path: C:\Program Files
(x86)\Microsoft Endpoint Manager\AdminConsole\AdminUILog\SmsAdminUI.log .

Next steps
     Use the console

     Console tips

     Accessibility features

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.65 -->

Manage Configuration Manager console
extensions
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Starting in Configuration Manager 2103, the Console extensions node allows you to
start managing the approval and installation of console extensions used in your
environment. Having extensions in the console doesn't make them immediately
available. From a high level, the steps are:

   1. An administrator has to approve an extension for the site
   2. The administrator has to enable notifications for the extension.
   3. The console users can then install the extension to their local console.

After you approve an extension, when you open the console, you'll see a console
notification. From the notification, you can start the extension installer, or use the Install
option from the Console extensions node. After the installer completes, the console
restarts automatically, and you can use the extension.

The old style of console extensions will start being phased out in favor of the new style
since they're more secure and centrally managed. The new style of console extensions
has the following benefits:

      Centralized management of console extensions for the site instead of manually
      placing binaries on individual consoles.
      A clear separation of console extensions from different extension providers.
      The ability for admins to have more control over which console extensions are
      loaded and used in the environment, to keep them more secure.
      A hierarchy setting that allows for only using the new style of console extension.

        ） Important

        If this setting is used, your old style extensions that aren't approved through
        the Console Extensions node will no longer be able to be used. The setting,
        Only allow console extensions that are approved for the hierarchy, is
         enabled by default if you installed from the 2103 baseline image. The setting

        remains disabled by default, if you upgraded from a version prior to 2103. If
        the setting was enabled in error, disabling the setting allows the old style
        extensions to be used again.

<!-- p.66 -->

Prerequisites
The Configuration Manager console needs to be able to connect to the administration
service and the administration service needs to be functional.

About the Console Extensions node
(Introduced in version 2103)

The Console Extensions node is located under Administration > Overview > Updates
and Servicing. Actions for console extensions are grouped in the ribbon and the right-
click menu. Console extensions downloaded from Community hub will be shown here.

                                                                                     

Actions for Console Extensions group:

     Refresh: Refreshes the node
     Import Console Extension: Launches the Import Console Extension wizard (added
     in 2111)

Actions for All Sites group:

     Approve Installation: Approves the console extension for installation across all
     sites. An extension must be approved before notifications are enabled.
     Revoke Approval:
        Revokes the ability to install the extension from the Console Extensions node.
        Notifies then uninstalls existing instances of the extension across the hierarchy
        at the next launch of a locally installed console.
        Allows for reapproval of the extension at a later date.
     Enable Notifications: Upon next launch of the console, notifies users within the
     security scope that the extension can be installed.
     Disable Notifications: Disables the console notification messages for the
     extension. Users within the security scope can still install approved extensions from

<!-- p.67 -->

     the Console Extensions node.
     Require Extension (added in 2111): Automatically installs the extension for users
     within the security scope on the next launch before connecting to the site. The
     user launching the console needs local administrator privileges for the extension
     installation.
     Make Optional (added in 2111): Removes the requirement for an extension.
     Console users can still install the extension locally from the Console Extensions
     node.
     Delete:
        Revokes the ability to install the extension from the Console Extensions node.
        Notifies then uninstalls existing instances of the extension across the hierarchy
        at the next launch of a locally installed console.
        Removes the extension from the Console Extensions node so it can't be
        reapproved later.

Classify group:

     Set Security Scopes: Set the security scopes to secure the object and limit access.

Local Extension group:

     Install: Installs the selected extension for the current local console
     Uninstall: Uninstalls the selected extension from the current local console

  ７ Note

       The WebView2 console extension is approved by default to enable using
       Community hub. The files are automatically downloaded from
        https://developer.microsoft.com/en-us/microsoft-edge/webview2/#download-

       section with the other redistributable files.

       When you upgrade to Configuration Manager 2107, you will be prompted to
       install the WebView2 console extension again.

Enable hierarchy approved console extensions
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select Sites.
   2. Select Hierarchy Settings from the ribbon.
   3. On the General tab, enable or disable the Only allow console extensions that are
     approved for the hierarchy option.

<!-- p.68 -->

   4. Select Ok when done to close the Hierarchy Settings Properties.

  ２ Warning

  If this setting is enabled , your old style extensions that aren't approved through the
  Console Extensions node will no longer be able to be used. The setting, Only allow
  console extensions that are approved for the hierarchy, is enabled by default if
  you installed from the 2103 baseline image. The setting remains disabled by
  default, if you upgraded from a version prior to 2103. If the setting was enabled in
  error, disabling the setting allows the old style extensions to be used again.

Get console extensions
There are three ways to get the new style of hierarchy approved console extensions into
Configuration Manager:

     An extension may come with Configuration Manager, such as WebView2
     Download console extensions from Community hub
     Import console extensions

Install and test an extension on a local console
   1. Change the security scope for the extension. Changing the security scope is
     recommended for initial testing of an extension.
      a. Go to the Console Extensions node under Administration > Overview >
        Updates and Servicing.
     b. Select the extension, then select Set Security Scopes from the ribbon.
      c. Remove the Default security scope and add a scope that only contains one or
        two admins for initial testing.
     d. Choose OK to save the security scope for the extension.

   2. Approve the extension by selecting Approve Installation from the ribbon or right-
     click menu.

           If the extension isn't approved, you won't be able to install it or enable in-
           console notifications for it.
           If you restart your console at this point, a notification about the available
           extension won't occur since you haven't enabled the option yet.

   3. Install the extension on the local console by choosing Install.

<!-- p.69 -->

   4. Once the extension is installed, verify it displays and you can use it from the local
     console.

Enable user notifications for extension
installation
   1. If needed, modify the security scopes for the extension to allow access by more
     admins. These admins will be targeted with the in-console notification for installing
     the extension.
   2. Select Enable Notifications.
   3. Launch a Configuration Manager console that doesn't have the extension installed.
     Ideally, use a test account that you gave access to when you modified the security
     scope.
   4. Verify that the notification for the extension occurs and that you can install the
     extension.

Allow unsigned console extensions for the
hierarchy
(Applies to Configuration Manager version 2107 or later)

Starting in Configuration Manager version 2107, you can choose to allow unsigned
hierarchy approved console extensions. It's a best practice to always used signed
extensions to minimize security risks and to confirm the authenticity of a console
extension. However, in some cases you may need to allow unsigned console extensions
due to an unsigned internally developed extension, or for testing your own custom
extension in a lab. To allow import and install of unsigned hierarchy approved console
extensions, you'll enable a hierarchy setting.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select Sites.
   2. Select Hierarchy Settings from the ribbon.
   3. On the General tab, enable the Hierarchy approved console extensions can be
     unsigned option.
   4. Select Ok when done to close the Hierarchy Settings Properties.

  ７ Note

  Currently, when an unsigned extension isn't enabled for user notification, in the
  Console Extensions node, the Required column remains blank instead of

<!-- p.70 -->

  populating a value of No.

Require installation of a console extension
(Introduced in 2111)

Starting in Configuration Manager version 2111, you can require a console extension to
be installed before it connects to the site. After you require an extension, it
automatically installs for the local console the next time an admin launches it. To require
the installation of a console extension:

   1. In the Configuration Manager console, go to the Administration workspace.
   2. Expand Updates and Servicing and select the Console Extensions node.
   3. Select the extension, then select Require Extension from either the right-click
     menu or the ribbon.

           Selecting Make Optional for an extension removes the extension
           requirement. Console users can still install it locally from the Console
           Extensions node.

   4. The next time the console is launched by a user within the extension's security
     scope, installation starts automatically.

           The user launching the console needs local administrator privileges for the
           extension installation.

Console extension installation user
notifications
Users are notified when console extensions are approved for installation. These
notifications occur for users in the following scenarios:

     The Configuration Manager console requires a built-in extension, such as
     WebView2, to be installed or updated.
     Console extensions are approved and notifications are enabled from
     Administration > Overview > Updates and Servicing > Console Extensions.
        When notifications are enabled, users within the security scope for the
        extension receive the following prompts:

   1. In the upper-right corner of the console, select the bell icon to display
     Configuration Manager console notifications.

<!-- p.71 -->

   2. The notification will say New custom console extensions are available.

   3. Select the link Install custom console extensions to launch the install.

   4. When the install completes, select Close to restart the console and enable the new
     extension.

  ７ Note

  When you upgrade to Configuration Manager 2107, you will be prompted to install
  the WebView2 console extension again. For more information about the WebView2
  installation, see the WebView2 installation section if the Community hub article.

Status messages for console extensions
(Introduced in 2111)

<!-- p.72 -->

Starting in version 2111, the site creates status messages for events related to console
extensions. Status messages improve the visibility and transparency of console
extensions that are used with your site. Use these status messages to make sure your
site uses known and trusted console extensions. The status messages have IDs from
54201 to 54208. They all include the following information:

     The user that made the change
     The ID of the extension
     The version of the extension

There are four categories of message events:

     Required or optional
     Approve or disapprove
     Enable or disable
     Tombstone or untombstone

For example, the description of status message ID 54201 is User "%1" made console
extension with ID "%2" and version "%3" required.

Next steps
     Console extensions from Community hub
     Import console extensions
     Configuration Manager console notifications
     Console tips

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.73 -->

Import Configuration Manager console
extensions
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Starting in Configuration Manager 2103, you can import console extensions to be used
in your environment. These extensions show up under the Console extensions node.
Importing and just having extensions in the console doesn't make them immediately
available. An administrator still has to approve the extension for the site and enable
notifications. Then console users can install the extension to their local console. For
more information about managing and installing console extensions, see Manage
Configuration Manager console extensions.

Based on the version of Configuration Manager you're running, different import options
are available. Initially, only signed extensions could be imported through the
administration service. Support for importing unsigned extensions was added later. Then
a wizard that could import both signed and unsigned extensions for you without having
to run a script was introduced in version 2111.

                                                                           ﾉ    Expand table

 Configuration Manager version      2103               2107               2111 or later

 Import a signed extension          Yes                Yes                Yes

 Import an unsigned extension       No                 Yes, when you      Yes, when you
                                                       allow unsigned     allow unsigned

 Import from the administration     Yes, signed        Yes                Yes
 service with a PowerShell script   extensions only

 Import from the Import Console     No                 No                 Yes
 Extension wizard

How to import console extensions
To import console extensions, you'll follow four basic steps. Exactly how you can import
will be determined by the version of Configuration Manager you're using and if the
extension is signed or not. To import and install a hierarchy approved console extension,
the high-level steps are:

<!-- p.74 -->

   1. Determine if you need to allow unsigned hierarchy approved console extensions
     (version 2107 and later).
   2. Import the console extension using one of the following methods:

           Import a signed console extension with a script (version 2103 and later)
           Import an unsigned console extension with a script (version 2107 and later)
           Use the Import Console Extension wizard (version 2111 and later)

   3. Test the extension in a local console.
   4. Enable notifications to allow console users to install the console extension.

Allow unsigned console extensions for the
hierarchy
(Applies to Configuration Manager version 2107 or later)

Starting in Configuration Manager version 2107, you can choose to allow unsigned
hierarchy approved console extensions. It's a best practice to always used signed
extensions to minimize security risks and to confirm the authenticity of a console
extension. However, in some cases you may need to allow unsigned console extensions
due to an unsigned internally developed extension, or for testing your own custom
extension in a lab. To allow import and install of unsigned hierarchy approved console
extensions, you'll enable a hierarchy setting.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select Sites.
   2. Select Hierarchy Settings from the ribbon.
   3. On the General tab, enable the Hierarchy approved console extensions can be
     unsigned option.
   4. Select Ok when done to close the Hierarchy Settings Properties.

  ７ Note

  Currently, when an unsigned extension isn't enabled for user notification, in the
  Console Extensions node, the Required column remains blank instead of
  populating a value of No.

Import a signed console extension with a script
(Applies to Configuration Manager version 2103 or later)

<!-- p.75 -->

When you have an extension packaged in a signed .cab file, you can import it into
Configuration Manager. You'll do this by posting it through the administration service
using a PowerShell script. Once the extension is inserted into the site, you can approve
and install it locally from the Console Extensions node. To import, run the following
PowerShell script after editing the $adminServiceProvider and $cabFilePath :

     $adminServiceProvider - The top-level SMSProvider server where the

     administration service is installed
     $cabFilePath - Path to the extension's signed .cab file

  PowerShell

  $adminServiceProvider = "SMSProviderServer.contoso.com"
  $cabFilePath = "C:\Testing\MyExtension.cab"
  $adminServiceURL =
  "https://$adminServiceProvider/AdminService/v1/ConsoleExtensionMetadata/Admi
  nService.UploadExtension"
  $cabFileName = (Get-Item -Path $cabFilePath).Name
  $Data = Get-Content $cabFilePath
  $Bytes = [System.IO.File]::ReadAllBytes($cabFilePath)
  $base64Content = [Convert]::ToBase64String($Bytes)

     $Headers = @{
         "Content-Type" = "Application/json"
     }

     $Body = @{
                   CabFile = @{
                       FileName = $cabFileName
                       FileContent = $base64Content
                   }
               } | ConvertTo-Json

     $result = Invoke-WebRequest -Method Post -Uri $adminServiceURL -Body
  $Body -Headers $Headers -UseDefaultCredentials

  if ($result.StatusCode -eq 200) {Write-Host "$cabFileName was published
  successfully."}
  else {Write-Host "$cabFileName publish failed. Review AdminService.log for
  more information."}

Import an unsigned console extension with a
script
(Applies to Configuration Manager version 2107 or later)

<!-- p.76 -->

Starting in Configuration Manager version 2107, you can choose to allow unsigned
hierarchy approved console extensions. It's a best practice to always used signed
extensions to minimize security risks and to confirm the authenticity of a console
extension. However, in some cases you may need to allow unsigned console extensions
due to an unsigned internally developed extension, or for testing your own custom
extension in a lab.

When you have the .cab file for an extension, you can test it in a Configuration
Manager lab environment. You'll do this by posting it through the administration
service. Once the extension is inserted into the site, you can approve it and install it
locally from the Console Extensions node. To import, run the following PowerShell script
after editing the $adminServiceProvider and $cabFilePath :

      $adminServiceProvider - The top-level SMSProvider server where the

     administration service is installed
      $cabFilePath - Path to the extension's .cab file

  PowerShell

  $adminServiceProvider = "SMSProviderServer.contoso.com"
  $cabFilePath = "C:\Testing\MyExtension.cab"
  $adminServiceURL =
  "https://$adminServiceProvider/AdminService/v1/ConsoleExtensionMetadata/Admi
  nService.UploadExtension"
  $cabFileName = (Get-Item -Path $cabFilePath).Name
  $Data = Get-Content $cabFilePath
  $Bytes = [System.IO.File]::ReadAllBytes($cabFilePath)
  $base64Content = [Convert]::ToBase64String($Bytes)
  $Headers = @{
      "Content-Type" = "Application/json"
  }
  $Body = @{
              CabFile = @{
                  FileName = $cabFileName
                  FileContent = $base64Content
              }
              AllowUnsigned = $true
          } | ConvertTo-Json
  $result = Invoke-WebRequest -Method Post -Uri $adminServiceURL -Body $Body -
  Headers $Headers -UseDefaultCredentials
  if ($result.StatusCode -eq 200) {Write-Host "$cabFileName was published
  successfully."}
  else {Write-Host "$cabFileName publish failed. Review AdminService.log for
  more information."}

  ７ Note

<!-- p.77 -->

  Currently, when an unsigned extension isn't enabled for user notification, in the
  Console Extensions node, the Required column remains blank instead of
  populating a value of No.

Import console extensions wizard
(Applies to Configuration Manager version 2111 or later)

Starting in version 2111, you can use the Import Console Extension wizard to import
console extensions that are managed for the hierarchy. You no longer need to use a
PowerShell script to import a signed or unsigned console extension. To import a console
extension using the wizard:

   1. From the Administration workspace, expand Updates and Servicing, then select
     the Console Extensions node.
   2. Select Import Console Extension from either the ribbon or the right-click menu.
   3. When the wizard launches, select Browse and navigate to the extension's cab file.
   4. If needed, select the option for Allow extension to be unsigned.
   5. Select Next to review the import summary, then complete the wizard to import the
     extension.

  ７ Note

  To import unsigned extensions, the Hierarchy approved console extensions can be
  unsigned option needs to be enabled in the Hierarchy Settings. For more
  information, see Allow unsigned hierarchy approved console extensions.

Install and test an extension on a local console
   1. Change the security scope for the extension. Changing the security scope is
     recommended for initial testing of an extension.
      a. Go to the Console Extensions node under Administration > Overview >
        Updates and Servicing.
     b. Select the extension, then select Set Security Scopes from the ribbon.
      c. Remove the Default security scope and add a scope that only contains one or
        two admins for initial testing.
     d. Choose OK to save the security scope for the extension.

   2. Approve the extension by selecting Approve Installation from the ribbon or right-
     click menu.

<!-- p.78 -->

           If the extension isn't approved, you won't be able to install it or enable in-
           console notifications for it.
           If you restart your console at this point, a notification about the available
           extension won't occur since you haven't enabled the option yet.

   3. Install the extension on the local console by choosing Install.

   4. Once the extension is installed, verify it displays and you can use it from the local
     console.

Enable user notifications for extension
installation
   1. If needed, modify the security scopes for the extension to allow access by more
     admins. These admins will be targeted with the in-console notification for installing
     the extension.
   2. Select Enable Notifications.
   3. Launch a Configuration Manager console that doesn't have the extension installed.
     Ideally, use a test account that you gave access to when you modified the security
     scope.
   4. Verify that the notification for the extension occurs and that you can install the
     extension.

Next steps
     Manage console extensions
     Console extensions from Community hub
     Develop custom console extensions

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.79 -->

Configuration Manager console changes
and tips
Article • 03/28/2024

Applies to: Configuration Manager (current branch)

Use the information below to find out about changes to the Configuration Manager
console and tips for using the console:

General tips

Console improvements in version 2207
(Introduced in version 2207)

The following improvements were made to the console and user experience:

      When using the search bar, the Path criteria is added whenever subfolders are
      included in the search. The Path criteria is informational and can't be edited.

Console improvements in version 2203
(Introduced in version 2203)

The following improvements were made to the console and user experience:

      When using temporary device nodes, device actions like Run Scripts are now
      available to make the experience in the console consistent.
      Additional Management Insights rules now have click-through actions
      Copy/paste is available for more objects from details panes.
         Added the Name property in the details pane for configuration items,
         configuration item related policies, and applications.
      Software update search results and the search criteria are now cached when you
      navigate to another node. When you navigate back to the All Software Updates
      node, your search criteria and results are preserved from your last query. Closing
      the console will clear the cached query.

<!-- p.80 -->

     Added a search filter to the Products and Classifications tabs in the Software
     Update Point Component Properties.
     You can now exclude subcontainers when doing Active Directory System
     Discovery and Active Directory User Discovery in untrusted domains.
     Added a Cloud Sync column to collections to indicate if the collection is
     synchronizing with Microsoft Entra ID.
     Added the Collection ID to the collection summary details tab
     Increased the size of the Membership Rules pane in the Properties page for
     collections.
     Added a View Script option for Run PowerShell Script steps when using the View
     action for a task sequence.
     The console now offers a dark theme. For more information, see How to use the
     console.

Export to CSV
(Introduced in version 2111)

Starting in Configuration Manager 2111, you can export the contents of a grid view in
the console along with the column headers to a comma-separated values (CSV) file that
can be used to import to Excel or other applications. While you could previously cut and
paste from a grid view, exporting to CSV makes extracting a large number of rows faster
and easier. You can export either all or selected items from the following nodes:

     Device Collections
     User Collections
     Devices
     Users

To export the information, select Export to CSV file from either the ribbon or the right-
click menu. Choose Export selected items to only export items you've already selected,
or you can choose to Export all items.
