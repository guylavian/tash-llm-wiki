---
title: "Core infrastructure documentation — pages 2201-2240"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2201-2240
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2201-2240
family: sccm
documentKind: "doc"
abstract: "Device restart notifications Some customers prefer frequent restart notifications and allowing users a short time frame to postpone. Others allow users to postpone a restart for longer periods of time, and infrequently notify users of the pending restart. You have control over t"
---

# Core infrastructure documentation — pages 2201-2240

<!-- p.2201 -->

Device restart notifications
Some customers prefer frequent restart notifications and allowing users a short time
frame to postpone. Others allow users to postpone a restart for longer periods of time,
and infrequently notify users of the pending restart. You have control over the timing
and frequency of restart notifications.

Install required software at or after the deadline
When required software is installed at or after the deadline, your users will see
notifications depending on what client settings you selected.

If the setting When a deployment requires a restart, show a dialog window to the user
instead of a toast notification is set to:

     No: Windows shows toast notifications until the deployment reaches the final
     countdown notification.

     Yes: Software Center shows a notification:

        If the restart is greater than 24 hours away, it shows an estimated restart time.
        The timing of this notification is based on the setting: Specify the amount of
        time after the deadline before a device gets restarted (minutes).

        If the restart is less than 24 hours away, it shows a progress bar. The timing of
        this notification is based on the setting: Specify the amount of time after the
        deadline before a device gets restarted (minutes).

<!-- p.2202 -->

If the user selects Snooze, another temporary notification shows after the snooze period
elapses. This behavior assumes it hasn't yet reached the final countdown. The timing of
the next notification is based on the setting: Specify the frequency of reminder
notifications presented to the user, after the deadline, before a device gets restarted
(minutes). If the user selects Snooze, and your snooze interval is one hour, then
Software Center notifies the user again in 60 minutes. This behavior assumes it hasn't
yet reached the final countdown.

When it reaches the final countdown, Software Center shows the user a notification they
can't close. The progress bar is in red and the user can't Snooze it.

Proactively install required software before the deadline
If the user proactively installs required software that needs restart before the deadline,
they'll see a different notification. For more information about configuring these

<!-- p.2203 -->

settings, see Deployment User Experience settings and User notifications for required
deployments.

The following notification occurs when both the user experience setting allows
notifications and you don't use toast notifications for the deployment:

Once the deployment reaches its deadline, Software Center follows the behavior to
Install required software at or after the deadline.

Example configurations
The following examples describe how to configure the client settings to achieve specific
behaviors.

  ７ Note

  If the user puts the device to sleep, it doesn't pause or interrupt a countdown. For
  example, a restart countdown is halfway into a four-hour timer, and the user puts
  the device to sleep. 12 hours later the user wakes up the device. The device restarts,
  as it's past the deadline.

Reminders are off

<!-- p.2204 -->

                                                                                   ﾉ   Expand table

 Setting                                                                                      Value

 Specify the amount of time after the deadline before a device gets restarted (minutes)       180

 Specify the amount of time that a user is presented a final countdown notification before    60
 a device gets restarted (minutes)

 Specify the frequency of reminder notifications presented to the user, after the deadline,   240
 before a device gets restarted (minutes)

 When a deployment requires a restart, show a dialog window to the user instead of a          No
 toast notification

The device will restart three hours (180 minutes) after the deployment deadline. One
hour (60 minutes) before it restarts, the user sees a countdown that they can't close or
snooze. The first reminder notification is set to start four hours (240 minutes) after the
deadline, which is after the restart. So the user doesn't see any reminders.

Low reminder frequency

                                                                                   ﾉ   Expand table

 Setting                                                                                      Value

 Specify the amount of time after the deadline before a device gets restarted (minutes)       7200

 Specify the amount of time that a user is presented a final countdown notification before    120
 a device gets restarted (minutes)

 Specify the frequency of reminder notifications presented to the user, after the deadline,   900
 before a device gets restarted (minutes)

 When a deployment requires a restart, show a dialog window to the user instead of a          Yes
 toast notification

The device will restart five days (7200 minutes) after the deployment deadline. Two
hours (120 minutes) before it restarts, the user sees a countdown that they can't close or
snooze. This configuration allows for 118 hours to show reminders ( (7200 - 120) / 60 ).
15 hours (900 minutes) after the deadline, Software Center displays the first reminder. It
displays a maximum of six additional reminders every 15 hours (900 minutes). The user
sees the reminder as a window on the screen, instead of a notification that disappears in
a few seconds.

High reminder frequency

<!-- p.2205 -->

                                                                                   ﾉ   Expand table

 Setting                                                                                      Value

 Specify the amount of time after the deadline before a device gets restarted (minutes)       2880

 Specify the amount of time that a user is presented a final countdown notification before    60
 a device gets restarted (minutes)

 Specify the frequency of reminder notifications presented to the user, after the deadline,   30
 before a device gets restarted (minutes)

 When a deployment requires a restart, show a dialog window to the user instead of a          Yes
 toast notification

The device will restart two days (2880 minutes) after the deployment deadline. One hour
(60 minutes) before it restarts, the user sees a countdown that they can't close or
snooze. This configuration allows for 47 hours to show reminders ( (2880 - 60) / 60 ). 30
minutes after the deadline, Software Center displays the first reminder. It displays a
maximum of 92 additional reminders every 30 minutes. The user sees the reminder as a
window on the screen, instead of a notification that disappears in a few seconds.

Log files
To troubleshoot device restarts, use the RebootCoordinator.log and SCNotify.log files
on the client. Based on the specific type of deployment, you may also have to use
additional client log files.

Next steps
      How to configure client settings
      Application deployment User Experience settings
      User notifications for required app deployments

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.2206 -->

How to configure Wake on LAN in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Specify Wake on LAN (WoL) settings for Configuration Manager when you want to bring
computers out of a sleep state.

Wake on LAN starting in version 1810
Starting in Configuration Manager 1810, there's a new way to wake up sleeping
machines. You can wake up clients from the Configuration Manager console, even if the
client isn't on the same subnet as the site server. If you need to do maintenance or
query devices, you're not limited by remote clients that are asleep. The site server uses
the client notification channel to identify other clients that are awake on the same
remote subnet, then uses those clients to send a wake on LAN request (magic packet).
Using the client notification channel helps avoid MAC flaps, which could cause the port
to be shut down by the router. The new version of Wake on LAN can be enabled at the
same time as the older version.

Prerequisites and limitations
      At least one client in the target subnet must be awake.
      This feature doesn't support the following network technologies:
         IPv6
         802.1x network authentication
            802.1x network authentication may work with additional configuration
            depending on the hardware and its configuration.
      DHCP lease durations can't be set to infinite.
         With Configuration Manager version 2010 and later, if the DHCP lease is set to
         infinite a client won't be woken up or used as a peer to wake other devices.
         With Configuration Manager version 2006 and earlier, you may see the
         SleepAgent_<domain>@SYSTEM_0.log become very large and possibly a
         broadcast storm in environments where DHCP leases are set to infinite.

Limitations for Configuration Manager version 2006 and earlier:

      Machines only wake when you notify them through the Wake Up client
      notification.

<!-- p.2207 -->

        For wake-up when a deadline occurs, the older version of Wake on LAN is used.
           Starting in Configuration Manager version 2010, you can wake up at deadline
           with the new version of WoL. For more information, see Notify client to wake
           when a deployment deadline occurs.
        If the older version isn't enabled, client wake-up won't occur for deployments
        created with the settings Use Wake-on-LAN to wake up clients for required
        deployments or Send wake-up packets.

Security role permissions
     Notify resource under the Collection category

Configure the clients to use Wake on LAN starting in
version 1810
Previously you had to manually enable the client for wake on LAN in the properties of
the network adapter. Configuration Manager 1810 includes a new client setting called
Allow network wake-up. Configure and deploy this setting instead of modifying the
properties of the network adapter.

   1. Under Administration, go to Client Settings.

   2. Select the client settings you want to edit, or create new custom client settings to
     deploy. For more information, see How to configure client settings.

   3. Under the Power Management client settings, select Enable for the Allow network
     wake-up setting. For more information about this setting, see About client
     settings.

   4. Starting in Configuration Manager 1902, the new version of Wake on LAN honors
     the custom UDP port you specify for the Wake On LAN port number (UDP) client
     setting. This setting is shared by both the new and older version of Wake on LAN.

Wake up a client using client notification starting in 1810
You can wake up a single client or any sleeping clients in a collection. For devices that
are already awake in the collection, no action is taken for them. Only clients that are
asleep will be sent a Wake on LAN request. For more information on how to notify a
client to wake, see Client notification.

     To wake up a single client: Right-click on the client, go to Client Notification, then
     select Wake up.

<!-- p.2208 -->

     To wake up all sleeping clients in a collection: Right-click on the device collection,
     go to Client Notification, then select Wake up.
        This action can't be run on built-in collections.
        When you have a mix of asleep and awake clients in a collection, only the clients
        that are asleep are sent a Wake on LAN request.
        Starting in Configuration Manager 2002, this action is available from a console
        connected to a Central Administration site, a stand-alone site, or child primary
        site.
        In versions 1910 and earlier, this action is only active when the Configuration
        Manager console is connected to a stand-alone or child primary site. When
        connected to a Central Administration Site, the action isn't available.

Wake machine at deployment deadline using peer clients
on the same remote subnet
(Introduced in version 2010)

Starting in Configuration Manager version 2010, you can allow the site to wake devices
at the deadline of a deployment, using the client notification channel. Instead of the site
server issuing the magic packet directly, the site uses the client notification channel to
find an online machine in the last known subnet of the target device(s) and instructs the
online client to issue the WoL packet for the target device.

Prerequisites for waking a client at deadline using the client
notification channel
Target computer prerequisites:

     Offline

<!-- p.2209 -->

     Updated to latest Configuration Manager client version
     Targeted with a Required deployment with a Deadline and the Send wake-up
     packages option enabled.

Prerequisites for the computer sending the WoL magic packet to the target computer:

     Online
     Updated to latest client version
     On the same subnet as the target computer

Enable waking a client at deadline using the client notification
channel
  1. At the site level, enable Wake on LAN:
     a. In the Configuration Manager console, go to Administration > Site
       Configuration > Sites.
     b. Select the primary site to configure, and then choose Properties.
     c. In the Wake on LAN tab, select Enable Wake On LAN for this site and send the
       wake-up packets Using client notification channel.

<!-- p.2210 -->

  d. Select OK and repeat the procedure for all primary sites in the hierarchy.

                                                                                  

2. Verify Allow network wake-up under the Power Management client settings is
  enabled.

3. Create a deployment as Required with the Send wake-up packages option and a
  Deadline. Clients are sent a notification when a deadline is received on
  deployments such as task sequences, software distribution, or software updates
  installation.

<!-- p.2211 -->

                                                                                      

What to expect when only the new version of
Wake on LAN is enabled
When you have only the new version of Wake on LAN enabled, only the Wake Up client
notification is enabled. Clients aren't sent a notification when a deadline is received on
deployments such as task sequences, software distribution, or software updates
installation. Once a sleeping machine is back online, it will be reflected in the console
when it checks in with the Management Point.

     Starting in Configuration Manager version 1902, you can specify the Wake on LAN
     port. This setting is shared by both the new and older version of Wake on LAN.

     Starting in Configuration Manager version 2010, you can use the client notification
     channel to wake clients when a deadline is received on deployments such as task
     sequences, software distribution, or software updates installation. For more
     information, see Use the client notification channel to wake a client when a
     deployment deadline occurs.

<!-- p.2212 -->

What to expect when both versions of Wake on
LAN are enabled
When you have both versions of Wake on LAN enabled, you can use the Wake Up client
notification and wake up on deadline. The client notification functions a little differently
than traditional Wake on LAN. For a brief explanation of how the client notification
works, see the Wake on LAN starting in version 1810 section. The new client setting
Allow network wake-up will change the NIC properties to allow Wake on LAN. You no
longer need to manually change it for new machines that are added to your
environment. All other functionality of Wake on LAN hasn't been changed.

     Starting in version 1902, the Wake Up client notification honors your existing Wake
     On LAN port number (UDP) setting.
     Starting in Configuration Manager version 2010, you can use the client notification
     channel to wake clients when a deadline is received on deployments such as task
     sequences, software distribution, or software updates installation. For more
     information, see Use the client notification channel to wake a client when a
     deployment deadline occurs.

Wake on LAN for version 1806 and earlier
Specify Wake on LAN settings for Configuration Manager when you want to bring
computers out of a sleep state to install required software, such as software updates,
applications, task sequences, and programs.

You can supplement Wake on LAN by using the wake-up proxy client settings. However,
to use wake-up proxy, you must first enable Wake on LAN for the site and specify Use
wake-up packets only and the Unicast option for the Wake on LAN transmission
method. This wake-up solution also supports ad-hoc connections, such as a remote
desktop connection.

Use the first procedure to configure a primary site for Wake on LAN. Then, use the
second procedure to configure the wake-up proxy client settings. This second procedure
configures the default client settings for the wake-up proxy settings to apply to all
computers in the hierarchy. If you want these settings to apply to only selected
computers, create a custom device setting and assign it to a collection that contains the
computers that you want to configure for wake-up proxy. For more information about
how to create custom client settings, see How to configure client settings.

A computer that receives the wake-up proxy client settings will likely pause its network
connection for 1-3 seconds. This pause occurs because the client must reset the network

<!-- p.2213 -->

interface card to enable the wake-up proxy driver on it.

  ２ Warning

  To avoid unexpected disruption to your network services, first evaluate wake-up
  proxy on an isolated and representative network infrastructure. Then use custom
  client settings to expand your test to a selected group of computers on several
  subnets. For more information about how wake-up proxy works, see Plan how to
  wake up clients.

To configure Wake on LAN for a site for version 1806 and
earlier
To use Wake on LAN, you need to enable it for each site in a hierarchy.

   1. In the Configuration Manager console, go to Administration > Site Configuration
     > Sites.
   2. Select the primary site to configure, and then choose Properties.
   3. In the Wake on LAN tab, and configure the options that you require for this site.
     To support wake-up proxy, make sure you select Use wake-up packets only and
     Unicast. For more information, see Plan how to wake up clients.
   4. Select OK and repeat the procedure for all primary sites in the hierarchy.

<!-- p.2214 -->

To configure wake-up proxy client settings
  1. In the Configuration Manager console, go to Administration > Client Settings.
  2. Select Default Client Settings, and then choose Properties.
  3. Select Power Management and then choose Yes for Enable wake-up proxy.
  4. Review and if necessary, configure the other wake-up proxy settings. For more
     information on these settings, see Power management settings.
  5. Select OK to close the dialog box, and then OK to close the Default Client Settings
     dialog box.

You can use the following Wake On LAN reports to monitor the installation and
configuration of wake-up proxy:

     Wake-Up Proxy Deployment State Summary
     Wake-Up Proxy Deployment State Details

<!-- p.2215 -->

   Tip

  To test whether wake-up proxy is working, test a connection to a sleeping
  computer. For example, connect to a shared folder on that computer, or try
  connecting to the computer using Remote Desktop. If you use Direct Access, check
  that the IPv6 prefixes work by trying the same tests for a sleeping computer that is
  currently on the Internet.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2216 -->

How to deploy clients to Windows
computers in Configuration Manager
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

This article provides details on how to deploy the Configuration Manager client to
Windows computers. For more information on planning and preparing for client
deployment, see these articles:

      Client installation methods
      Prerequisites for deploying clients to Windows computers
      Security and privacy for Configuration Manager clients
      Best practices for client deployment

Client push installation
There are three main ways to use client push:

      When you configure client push installation for a site, client installation
      automatically runs on computers that the site discovers. This method is scoped to
      the site's configured boundaries when those boundaries are configured as a
      boundary group.

      Start client push installation by running the Client Push Installation Wizard for a
      specific collection or resource within a collection.

      Use the Client Push Installation Wizard to install the Configuration Manager client,
      which you can use to query the result. The installation will succeed only if one of
      the items returned by the query is the ResourceID attribute of the System
      Resource class.

If the site server can't contact the client computer or start the setup process, it
automatically retries the installation every hour. The server continues to retry for up to
seven days.

To help track the client installation process, install a fallback status point before you
install the clients. When you install a fallback status point, it's automatically assigned to
clients when they're installed by the client push installation method. To track client
installation progress, view the client deployment and assignment reports.

<!-- p.2217 -->

Client log files provide more detailed information for troubleshooting. The log files
don't require a fallback status point. For example, the CCM.log file on the site server
records any problems that occur when the site server connects to the computer. The
CCMSetup.log file on the client records the installation process.

  ） Important

  Client push only succeeds if all prerequisites are met. For more information, see
  Installation method dependencies.

Configure the site to automatically use client push for
discovered computers
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. Select the site for which you want to configure automatic site-wide client push
     installation.

   3. On the Home tab of the ribbon, in the Settings group, select Client Installation
     Settings, and then select Client Push Installation.

   4. On the General tab of the Client Push Installation Properties window, select Enable
     automatic site-wide client push installation.

   5. Starting in version 1806, when you update the site, a Kerberos check for client push
     is enabled. The option to Allow connection fallback to NTLM is enabled by
     default, which is consistent with previous behavior. If the site can't authenticate the
     client by using Kerberos, it retries the connection by using NTLM. The
     recommended configuration for improved security is to disable this setting, which
     requires Kerberos without NTLM fallback.

     It is recommended to disable this option in existing environments, where possible,
     to increase security.

        ７ Note

        When it uses client push to install the Configuration Manager client, the site
        server creates a remote connection to the client. Starting in version 1806, the
        site can require Kerberos mutual authentication by not allowing fallback to
        NTLM before establishing the connection. This enhancement helps to secure
        the communication between the server and the client.

<!-- p.2218 -->

    Depending on your security policies, your environment might already prefer
    or require Kerberos over the older NTLM authentication. For more information
    on the security considerations of these authentication protocols, read about
    the Windows security policy setting to restrict NTLM.

    To use this feature, clients must be in a trusted Active Directory forest.
    Kerberos in Windows relies on Active Directory for mutual authentication.

6. Starting in version 2207, when you update the site, the option to Allow connection
  fallback to NTLM is disabled by default on new site installations. It is
  recommended to increase security.

7. Select the system types to which Configuration Manager should push the client
  software. Select whether you want to install the client on domain controllers.

8. On the Accounts tab, specify one or more accounts for Configuration Manager to
  use when it connects to the target computer. Select the Create icon, enter the User
  name and Password (no more than 38 characters), confirm the password, and then
  select OK. Specify at least one client push installation account. This account must
  have local administrator rights on the target computer to install the client. If you
  don't specify a client push installation account, Configuration Manager tries to use
  the site system computer account. Cross-domain client push fails when using the
  site system computer account.

    ７ Note

    To use client push from a secondary site, specify the account at the secondary
    site that initiates the client push.

    For more information about the client push installation account, see the next
    procedure, Use the Client Push Installation Wizard.

9. Specify any required installation properties on the Installation Properties tab.

  If you've extended the Active Directory schema for Configuration Manager, the site
  publishes the specified client installation properties to Active Directory Domain
  Services. When CCMSetup runs without installation properties, it reads these
  properties from Active Directory.

    ７ Note

<!-- p.2219 -->

       If you enable client push installation on a secondary site, set the
       SMSSITECODE property to the Configuration Manager site code of its parent
       primary site. If you've extended the Active Directory schema for Configuration
       Manager, to automatically find the correct site assignment, set this property
       to AUTO.

Use the Client Push Installation Wizard
  1. In the Configuration Manager console, go to the Administration workspace,
    expand Site Configuration, and select the Sites node.

  2. Select the site for which you want to configure automatic site-wide client push
    installation.

  3. On the Home tab of the ribbon, in the Settings group, select Client Installation
    Settings, and then select Client Push Installation.

  4. Specify any required installation properties on the Installation Properties tab.

    If you've extended the Active Directory schema for Configuration Manager, the site
    publishes the specified client installation properties to Active Directory Domain
    Services. When CCMSetup runs without installation properties, it reads these
    properties from Active Directory.

  5. In the Configuration Manager console, go to the Assets and Compliance
    workspace.

  6. In the Devices node, select one or more computers. Or select a collection of
    computers in the Device Collections node.

  7. On the Home tab of the ribbon, choose one of these options:

          To push the client to one or more devices, in the Device group, select Install
          Client.

          To push the client to a collection of devices, in the Collection group, select
          Install Client.

  8. On the Before You Begin page of the Install Configuration Manager Client Wizard,
    review the information, and then select Next.

  9. Select the appropriate options on the Installation Options page.

 10. Review the installation settings, and then complete the wizard.

<!-- p.2220 -->

  ７ Note

  Use this wizard to install clients even if the site isn't configured for client push.

Software update-based installation
Software update-based client installation publishes the client to a software update point
as a software update. Use this method for a first-time installation or upgrade.

If the Configuration Manager client is installed on a computer, the computer receives
client policy from the site. This policy includes the software update-point server name
and port from which to get software updates.

  ） Important

  For software update-based installation, use the same Windows Server Update
  Services (WSUS) server for client installation and software updates. This server must
  be the active software update point in a primary site. For more information, see
  Install a software update point.

If the Configuration Manager client isn't installed on a computer, configure and assign a
Group Policy Object. The Group Policy specifies the server name of the software update
point.

You can't add command-line properties to a software update-based client installation. If
you've extended the Active Directory schema for Configuration Manager, the client
installation automatically queries Active Directory Domain Services for the installation
properties.

If you haven't extended the Active Directory schema, use Group Policy to provision client
installation settings. These settings are automatically applied to any software update-
based client installation. For more information, see the section on How to provision
client installation properties and the article on How to assign clients to a site.

Use the following procedures to configure computers without a Configuration Manager
client to use the software update point. There's also a procedure for publishing the
client software to the software update point.

   Tip

<!-- p.2221 -->

 If computers are in a pending restart state following a previous software
 installation, a software update-based client installation might cause the computer
 to restart.

Configure a Group Policy Object to specify the software
update point
 1. Use the Group Policy Management Console to open a new or existing Group
    Policy Object.

 2. Expand Computer Configuration, Administrative Templates, and Windows
    Components, and then select Windows Update.

 3. Open the properties of the setting Specify intranet Microsoft update service
    location, and then select Enabled.

 4. Set the intranet update service for detecting updates: Specify the name and port
    of the software update point server.

          If you've configured the Configuration Manager site system to use a fully
          qualified domain name (FQDN), use that format.

          If the Configuration Manager site system isn't configured to use an FQDN,
          use a short name format.

        Tip

       To determine the port number, see How to determine the port settings used
       by WSUS.

    Example in the FQDN format: http://server1.contoso.com:8530

 5. Set the intranet statistics server: This setting is typically configured with the same
    server name.

 6. Assign the Group Policy Object to the computers on which you want to install the
    client and receive software updates.

Publish the Configuration Manager client to the software
update point

<!-- p.2222 -->

   1. In the Configuration Manager console, go to the Administration workspace,
      expand Site Configuration, and select the Sites node.

   2. Select the site for which you want to configure software update-based client
      installation.

   3. On the Home tab of the ribbon, in the Settings group, select Client Installation
      Settings, and then select Software Update-Based Client Installation.

   4. Select Enable software update-based client installation.

   5. If the site's client version is more recent than the version on the software update
      point, the Later Version of Client Package Detected dialog box opens. Select Yes
      to publish the most recent version.

        ７ Note

        If you haven't already published the client software to the software update
        point, this dialog box is blank.

The software update for the Configuration Manager client isn't automatically updated
when there's a new version. When you update the site, repeat this procedure to update
the client.

Group Policy installation
Use Group Policy in Active Directory Domain Services to publish or assign the
Configuration Manager client. The client installs when the computer starts. When you
use Group Policy, the client appears in Add or Remove Programs in Control Panel. The
user can install it from there.

Use the Windows Installer package CCMSetup.msi for Group Policy-based installations.
This file is found in the <ConfigMgr installation directory>\bin\i386 folder on the site
server. You can't add properties to this file to change installation behavior.

  ） Important

  You must have administrator permissions to access the client installation files.

      If you've extended the Active Directory schema for Configuration Manager, and
      you selected the domain on the Publishing tab of the Site Properties dialog box,
      client computers automatically search Active Directory Domain Services for

<!-- p.2223 -->

      installation properties. For more information, see About client installation
      properties published to Active Directory Domain Services.

      If you haven't extended the Active Directory schema, see the section on
      provisioning client installation properties for information about storing installation
      properties in the Windows registry of computers. The client uses these installation
      properties when it installs.

For more information, see How to use Group Policy to remotely install software           .

Manual installation
Manually install the client software on computers by using CCMSetup.exe. You can find
this program and its supporting files in the Client folder in the Configuration Manager
installation folder on the site server. The site shares this folder to the network as:

\\<site server name>\SMS_<site code>\Client\

<site server name> is the primary site server name. <site code> is the primary site

code to which the client is assigned. To run CCMSetup.exe from the command line on
the client, connect to this network location, and then run the command.

  ） Important

  You must have administrator permissions to access the client installation files.

CCMSetup.exe copies all necessary prerequisites to the client computer and calls the
Windows Installer package (Client.msi) to install the client. You can't run Client.msi
directly.

To modify the behavior of the client installation, specify command-line options for both
CCMSetup.exe and Client.msi. Make sure that you specify CCMSetup parameters that
begin with / before you specify Client.msi properties. For example:

CCMSetup.exe /mp:SMSMP01 /logon SMSSITECODE=AUTO FSP=SMSFP01

In this example, the client installs with the following options:

                                                                            ﾉ   Expand table

<!-- p.2224 -->

 Option             Description

 /mp:SMSMP01        This CCMSetup parameter specifies the management point SMSMP01 for
                    downloading the required client installation files.

 /logon             This CCMSetup parameter specifies that the installation should stop if an
                    existing Configuration Manager client is found on the computer.

 SMSSITECODE=AUTO   This Client.msi property specifies that the client tries to locate the
                    Configuration Manager site code to use, by using Active Directory Domain
                    Services, for example.

 FSP=SMSFP01        This Client.msi property specifies that the fallback status point named
                    SMSFP01 is used to receive state messages sent from the client computer.

For more information, see About client installation parameters and properties.

   Tip

  For the procedure to install the Configuration Manager client on a modern
  Windows device by using Microsoft Entra identity, see Install and assign
  Configuration Manager clients using Microsoft Entra ID for authentication. That
  procedure is for clients on an intranet or the internet.

Manual installation examples
These examples are for Active Directory-joined clients on an intranet. They use the
following values:

     MPSERVER: server hosting the management point
     FSPSERVER: server hosting the fallback status point
     ABC: site code
     contoso.com: domain name

Assume that you've configured all site system servers with an intranet FQDN and
published the site information to Active Directory.

Start with the following steps on the client computer:

   1. Sign in as a local administrator.
   2. Map drive Z to \\MPSERVER\SMS_ABC\Client .
   3. Switch the command prompt to drive Z.

Then run one of the following commands:

<!-- p.2225 -->

Manual example 1
CCMSetup.exe

This command installs the client with no additional parameters or properties. The client
is automatically configured with the client installation properties published to Active
Directory Domain Services, including these settings:

      Site code: This setting requires the client's network location to be included in a
      boundary group that you've configured for client assignment.
      Management point.
      Fallback status point.
      Communicate using HTTPS only.

For more information, see About client installation properties published to Active
Directory Domain Services.

Manual example 2
CCMSetup.exe /MP:mpserver.contoso.com /UsePKICert SMSSITECODE=ABC

CCMHOSTNAME=server05.contoso.com CCMFIRSTCERT=1 FSP=server06.constoso.com

This command overrides the automatic configuration that Active Directory Domain
Services provides. It doesn't require that you include the client's network location in a
boundary group that's configured for client assignment. Instead, the installation
specifies these settings:

      Site code
      Intranet management point
      Internet-based management point
      Fallback status point that accepts connections from the internet
      Use a client public key infrastructure (PKI) certificate (if available) that has the
      longest validity period

Logon script installation
Configuration Manager supports using logon scripts to install the Configuration
Manager client software. Use the program file CCMSetup.exe in a logon script to trigger
the client installation.

Logon script installation uses the same methods as manual client installation. Specify
the /logon installation parameter for CCMSsetup.exe. If any version of the client already

<!-- p.2226 -->

exists on the computer, this parameter prevents the client from installing. This behavior
prevents reinstallation of the client each time the logon script runs.

If you don't specify an installation source by using the /Source parameter and no
management point from which to obtain installation is specified by the /MP parameter,
CCMSetup.exe locates the management point by searching Active Directory Domain
Services. This behavior occurs only if you've extended the schema for Configuration
Manager and published the site to Active Directory Domain Services. Alternatively, the
client can use DNS to locate a management point.

Package and program installation
Use Configuration Manager to create and deploy a package and program that upgrades
the client software for selected devices. Configuration Manager supplies a package
definition file that populates the package properties with typically used values.
Customize the behavior of the client installation by specifying additional command-line
parameters and properties.

  ７ Note

  You can't upgrade Configuration Manager 2007 clients by using this method.
  Instead, use automatic client upgrade, which automatically creates and deploys a
  package that contains the latest version of the client. For more information, see
  Upgrade clients.

  For more information about how to migrate from older versions of the
  Configuration Manager client, see Planning a client migration strategy.

Create a package and program for the client software
Use the following procedure to create a Configuration Manager package and program
that you can deploy to Configuration Manager client computers to upgrade the client
software.

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Application Management, and select the Packages node.

   2. On the Home tab of the ribbon, in the Create group, select Create Package from
     Definition.

<!-- p.2227 -->

   3. On the Package Definition page of the wizard, select Microsoft from the Publisher
     list, and select Configuration Manager Client Upgrade from the Package
     definition list.

   4. On the Source Files page, select Always obtain files from a source folder.

   5. On the Source Folder page, select Network path (UNC Name). Then enter the
     network path of the server and share that contains the client installation files.

          ７ Note

          The computer on which the Configuration Manager deployment runs must
          have access to the specified network folder. Otherwise, the client installation
          fails.

     To change any of the client installation properties, modify the CCMSetup.exe
     command line on the General tab of the Configuration Manager agent silent
     upgrade Properties program dialog box. The default installation properties are
      /noservice SMSSITECODE=AUTO .

   6. Distribute the package to all distribution points that you want to host the client
     upgrade package. Then deploy the package to device collections that contain
     clients that you want to upgrade.

Intune MDM-managed Windows devices
Deploy the Configuration Manager client to devices that are enrolled with Microsoft
Intune.

This procedure is for a traditional client that's connected to an intranet. It uses
traditional client authentication methods. To make sure the device remains in a
managed state after it installs the client, it must be on the intranet and within a
Configuration Manager site boundary.

For the procedure to install the Configuration Manager client on a Windows device by
using Microsoft Entra identity, see Install and assign Configuration Manager clients
using Microsoft Entra ID for authentication.

After you install the Configuration Manager client, devices don't unenroll from Intune.
They can use the Configuration Manager client and MDM enrollment at the same time.
For more information, see Co-management overview.

<!-- p.2228 -->

  ７ Note

  You can use other client installation methods to install the Configuration Manager
  client on an Intune-managed device. For example, if an Intune-managed device is
  on the intranet, and joined to the Active Directory domain, you can use group
  policy to install the Configuration Manager client.

Install the Configuration Manager client by using Intune
   1. In Intune, add a Windows line-of-business app that contains the Configuration
     Manager client installation file CCMSetup.msi. You can find this file in the
      \bin\i386 folder of the Configuration Manager installation directory on the site

     server.

   2. In the Intune Software Publisher, enter command-line parameters. For example,
     use this command with a traditional client on an intranet:

      CCMSETUPCMD="/MP:<FQDN of management point> SMSMP=<FQDN of management point>

     SMSSITECODE=<your site code> DNSSUFFIX=<DNS suffix of management point>"

        ７ Note

        For an example of a command to use with a Windows client using Microsoft
        Entra authentication, see How to prepare internet-based devices for co-
        management.

   3. Assign the app to a group of the enrolled Windows computers.

OS image installation
Preinstall the Configuration Manager client on a reference computer that you use to
create an OS image.

  ） Important

  When you use the Configuration Manager task sequence to deploy an OS image,
  the Prepare ConfigMgr Client step completely removes the Configuration Manager
  client.

<!-- p.2229 -->

Prepare the client computer for imaging
 1. Manually install the Configuration Manager client software on the reference
   computer. For more information, see How to install Configuration Manager clients
   manually.

     ） Important

     Don't specify a Configuration Manager site code for the client in the
     CCMSetup.exe command-line properties.

 2. At a command prompt, type net stop ccmexec to stop the SMS Agent Host service
   (CcmExec.exe) on the reference computer.

 3. Delete the SMSCFG.INI file from the Windows folder on the reference computer.

 4. Remove the certificates from the local computer's SMS certificate store.

 5. Remove any other valid client authentication certificates that are stored in the local
   computer store on the reference computer. For example, if you use PKI certificates,
   before you image the computer, remove the certificates in the Personal store for
   Computer and User.

 6. If the clients are installed in a different Configuration Manager hierarchy than the
   hierarchy of the reference computer, remove the trusted root key from the
   reference computer.

     ７ Note

     If clients can't query Active Directory Domain Services to locate a
     management point, they use the trusted root key to determine trusted
     management points. If you deploy all imaged clients in the same hierarchy as
     that of the master computer, leave the trusted root key in place.

     If you deploy the clients in different hierarchies, remove the trusted root key.
     Also provision these clients with the new trusted root key. For more
     information, see Planning for the trusted root key.

 7. Use your imaging software to capture an image of the reference computer.

 8. Deploy the image to the destination computers.

<!-- p.2230 -->

Workgroup computers
Configuration Manager supports client installation for computers in workgroups. Install
the client on workgroup computers by using the method specified in How to install
Configuration Manager clients manually.

Prerequisites
     Manually install the client on each workgroup computer. During installation, the
     interactive user must have local administrator rights.

     To access resources in the Configuration Manager site server domain, configure
     the network access account for the site. Specify this account in the software
     distribution site component. For more information, see Site components.

Limitations
     Workgroup clients can't locate management points from Active Directory Domain
     Services. Instead, they use DNS or another management point.

     Global roaming isn't supported. Workgroup clients can't query Active Directory
     Domain Services for site information.

     Active Directory discovery methods can't discover computers in workgroups.

     You can't deploy software to users of workgroup computers.

     You can't use the client push installation method to install the client on workgroup
     computers.

     Workgroup clients can't use Kerberos for authentication, and they might require
     manual approval.

     You can't configure a workgroup client as a distribution point. Configuration
     Manager requires that distribution point computers be members of a domain.

Install the client on workgroup computers
Check the prerequisites, and then follow the directions in the section How to install
Configuration Manager clients manually.

Workgroup example 1

<!-- p.2231 -->

This example does the following actions:

     Installs the client for intranet client management
     Specifies the site code
     Specifies the DNS suffix to locate a management point

CCMSetup.exe SMSSITECODE=ABC DNSSUFFIX=constoso.com

Workgroup example 2
This example requires the client to be on a network location that's configured in a
boundary group. If this requirement isn't met, automatic site assignment won't work.
The command includes a fallback status point on server FSPSERVER. This property helps
to track client deployment and to identify any client communication issues.

CCMSetup.exe FSP=fspserver.constoso.com

Internet-based client management

  ７ Note

  This section doesn't apply to clients that use a cloud management gateway. To
  install internet-based clients by using a cloud management gateway, see Install
  and assign Configuration Manager clients using Microsoft Entra ID for
  authentication.

When the Configuration Manager site supports internet-based client management for
clients that are sometimes on an intranet and sometimes on the internet, you have two
options when you install clients on the intranet:

     Include the Client.msi property CCMHOSTNAME=<internet FQDN of the internet-based
     management point> when you install the client, by using manual installation or client

     push, for example. When you use this method, directly assign the client to the site.
     You can't use automatic site assignment. See the How to install Configuration
     Manager clients manually section, which provides an example of this configuration
     method.

     Install the client for intranet client management, and then assign an internet-based
     client management point to the client. Change the management point by using the
     client properties on the Configuration Manager page in Control Panel, or by using
     a script. When you use this method, you can use automatic client assignment. For

<!-- p.2232 -->

     more information, see the How to configure clients for internet-based client
     management after client installation section.

To install clients that are on the internet, choose one of the following supported
methods:

     Provide a mechanism for these clients to temporarily connect to the intranet with a
     VPN. Then install the client by using any appropriate client installation method.

     Use an installation method that's independent of Configuration Manager. For
     example, package the client installation source files onto removable media and
     send the media to users. The client installation source files are located in the
      <installation path>\Client folder on the Configuration Manager site server. On

     the media, include a script to manually copy over the client folder. From this folder,
     install the client by using CCMSetup.exe and all the appropriate CCMSetup
     command-line properties.

  ７ Note

  Configuration Manager doesn't support installing a client directly from the
  internet-based management point or from the internet-based software update
  point.

Clients that are managed over the internet must communicate with internet-based site
systems. Ensure that these clients also have public key infrastructure (PKI) certificates
before you install the client. Install these certificates independently from Configuration
Manager. For more information, see PKI certificate requirements.

Install clients on the internet by specifying CCMSetup
command-line properties
   1. Follow the directions in the section How to install Configuration Manager clients
     manually. Always include the following options:

           CCMSetup command-line parameter /source:<local path of the copied
           Client folder>

           CCMSetup command-line parameter /UsePKICert

           Client.msi property CCMHOSTNAME=<FQDN of internet-based management point>

<!-- p.2233 -->

           Client.msi property SMSSIGNCERT=<local path of exported site server
           signing certificate>

           Client.msi property SMSSITECODE=<site code of internet-based management
           point>

        ７ Note

        If the site has more than one internet-based management point, it doesn't
        matter which one you specify for the CCMHOSTNAME property. When a
        Configuration Manager client connects to the specified internet-based
        management point, it sends the client a list of available internet-based
        management points in the site. The client randomly selects one from the list.

   2. If you don't want the client to check the certificate revocation list (CRL), specify the
     CCMSetup command-line parameter /NoCRLCheck .

   3. If you're using an internet-based fallback status point, specify the Client.msi
     property FSP=<internet FQDN of the internet-based fallback status point> .

   4. If you're installing the client for internet-only client management, specify the
     Client.msi property CCMALWAYSINF=1 .

   5. Determine whether you have to specify additional CCMSetup command-line
     parameters. For example, if the client has more than one valid PKI certificate, you
     might have to specify a certificate selection criterion. For a list of available
     properties, see About client installation parameters and properties.

Internet-based example
CCMSetup.exe /source: D:\Clients /UsePKICert CCMHOSTNAME=server1.contoso.com

SMSSIGNCERT=siteserver.cer SMSSITECODE=ABC FSP=server2.contoso.com CCMALWAYSINF=1
CCMFIRSTCERT=1

This example installs the client with the following behaviors:

     Use source files from a folder on drive D.
     Use a client PKI certificate.
     Select the certificate with the longest validity period.
     Internet-only client management.
     Assign the client to use the internet-based management point named SERVER1.
     Assign the internet-based fallback status point in the contoso.com domain.

<!-- p.2234 -->

     Assign the client to the ABC site.

To configure clients for internet-based client
management after client installation
To assign the internet-based management point after you install the client, use one of
these procedures. The first requires manual configuration and is appropriate for a few
clients. The second is more appropriate for configuring many clients.

Configure clients for internet-based client management after client
installation from the Configuration Manager control panel
   1. Open the Configuration Manager control panel on the client.

   2. On the Network tab, enter the fully qualified domain name (FQDN) of the internet-
     based management point as the Internet FQDN.

       ７ Note

       The Network tab is available only if the client has a client PKI certificate.

   3. If the client accesses the internet by using a proxy server, enter the proxy server
     settings.

Configure clients for internet-based client management after client
installation by using a script

PowerShell

   1. Open a PowerShell in-line editor, like PowerShell ISE or Visual Studio Code. You can
     also use a text editor, like Notepad.

   2. Copy and insert the following lines of code into the editor. Replace
     'mp.contoso.com' with the internet FQDN of your internet-based management

     point.

       PowerShell

        $newInternetBasedManagementPointFQDN = 'mp.contoso.com'
        $client = New-Object -ComObject Microsoft.SMS.Client
        $client.SetInternetManagementPointFQDN($newInternetBasedManagementPoint
        FQDN)

<!-- p.2235 -->

        Restart-Service CcmExec
        $client.GetInternetManagementPointFQDN()

        ７ Note

        The last line is there only to verify the new internet management point value.

        To delete a specified internet-based management point, remove the server
        FQDN value inside the quotation marks. The line becomes
        $newInternetBasedManagementPointFQDN = '' .

   3. Save the file with a .ps1 extension.

   4. Run the script with elevated rights on client computers. Use one of these methods:

           Deploy the file to existing Configuration Manager clients by using a package
           and a program.

           Run the file locally on existing Configuration Manager clients by double-
           clicking the script file in File Explorer.

You might have to restart the client for the changes to take effect.

Provision client installation properties
Provision client installation properties for group policy and software update-based client
installations. Use Windows Group Policy to provision computers with Configuration
Manager client installation properties. These properties are stored in the registry of the
computer. The client reads them when it installs. This procedure isn't normally required,
but it might be needed for some client installation scenarios, such as:

     You're using the group policy settings or software update-based client installation
     methods. You haven't extended the Active Directory schema for Configuration
     Manager.

     You want to override client installation properties on specific computers.

  ７ Note

  If any installation properties are supplied on the CCMSetup.exe command line,
  installation properties provisioned on computers aren't used.

<!-- p.2236 -->

A group policy administrative template named ConfigMgrInstallation.adm is supplied
on the Configuration Manager installation media. Use this template to provision client
computers with installation properties.

   Tip

  By default, ConfigMgrInstallation.adm doesn't support strings larger than 255
  characters. This configuration can impact adding multiple parameters or
  parameters with long values, such as CCMCERTISSUERS.

  To workaround this issue:

     1. Edit ConfigMgrInstallation.adm in Notepad.
     2. For the property VALUENAME SetupParameters , change the MAXLEN value to a
        larger integer. For example, MAXLEN 511 .

Configure and assign client installation properties by
using a group policy object
   1. Import the ConfigMgrInstallation.adm administrative template into a new or
     existing group policy object (GPO) by using an editor like Windows Group Policy
     Object Editor. You can find this file in the TOOLS\ConfigMgrADMTemplates folder on
     the Configuration Manager installation media.

   2. Open the properties of the imported setting Configure Client Deployment
     Settings.

   3. Select Enabled.

   4. In the CCMSetup box, enter the required CCMSetup command-line properties. For
     a list of all CCMSetup command-line properties and examples of their use, see
     About client installation parameters and properties.

   5. Assign the GPO to the computers that you want to provision with Configuration
     Manager client installation properties.

Feedback
Was this page helpful?    Yes    No

<!-- p.2237 -->

Provide product feedback

<!-- p.2238 -->

About client installation parameters and
properties in Configuration Manager
Article • 04/11/2023

Applies to: Configuration Manager (current branch)

Use the CCMSetup.exe command to install the Configuration Manager client. If you
provide client installation parameters on the command line, they modify the installation
behavior. If you provide client installation properties on the command line, they modify
the initial configuration of the installed client agent.

About CCMSetup.exe
The CCMSetup.exe command downloads needed files to install the client from a
management point or a source location. These files might include:

      The Windows Installer package client.msi that installs the client software

      Client prerequisites

      Updates and fixes for the Configuration Manager client

  ７ Note

  You can't directly install client.msi.

CCMSetup.exe provides command-line parameters to customize the installation.
Parameters are prefixed with a slash ( / ) and are generally lower case. You specify the
value of a parameter when necessary using a colon ( : ) immediately followed by the
value. For more information, see CCMSetup.exe command-line parameters.

You can also supply properties at the CCMSetup.exe command line to modify the
behavior of client.msi. Properties by convention are upper case. You specify a value for a
property using an equal sign ( = ) immediately followed by the value. For more
information, see Client.msi properties.

  ） Important

  Specify CCMSetup parameters before you specify properties for client.msi.

<!-- p.2239 -->

CCMSetup.exe and the supporting files are on the site server in the Client folder of the
Configuration Manager installation folder. Configuration Manager shares this folder to
the network under the site share. For example, \\SiteServer\SMS_ABC\Client .

At the command prompt, the CCMSetup.exe command uses the following format:

CCMSetup.exe [<Ccmsetup parameters>] [<client.msi setup properties>]

For example:

CCMSetup.exe /mp:SMSMP01 /logon SMSSITECODE=S01 FSP=SMSFSP01

This example does the following things:

     Specifies the management point named SMSMP01 to request a list of distribution
     points to download the client installation files.

     Specifies that installation should stop if a version of the client already exists on the
     computer.

     Instructs client.msi to assign the client to the site code S01.

     Instructs client.msi to use the fallback status point named SMSFP01.

   Tip

  If a parameter value has spaces, surround it with quotation marks.

If you extend the Active Directory schema for Configuration Manager, the site publishes
many client installation properties in Active Directory Domain Services. The
Configuration Manager client automatically reads these properties. For more
information, see About client installation properties published to Active Directory
Domain Services

CCMSetup.exe command-line parameters

/?

Shows available command-line parameters for ccmsetup.exe.

Example: ccmsetup.exe /?

/AllowMetered

<!-- p.2240 -->

Use this parameter to control the client's behavior on a metered network. This
parameter takes no values. When you allow client communication on a metered network
for ccmsetup, it downloads the content, registers with the site, and downloads the initial
policy. Any further client communication follows the configuration of the client setting
from that policy. For more information, see About client settings.

If you reinstall the client on an existing device, it uses the following priority to determine
its configuration:

   1. Existing local client policy
   2. The last command line stored in the Windows registry
   3. Parameters on the ccmsetup command line

/AlwaysExcludeUpgrade

This parameter specifies whether or not a client will auto upgrade when you enable
Automatic client upgrade.

Supported values:

      TRUE : The client won't automatically upgrade
      FALSE : The client automatically upgrades (default)

For example:

CCMSetup.exe /AlwaysExcludeUpgrade:TRUE

For more information, see Extended interoperability client.

  ７ Note

  When using the /AlwaysExcludeUpgrade parameter, the auto upgrade still runs.
  However when CCMSetup runs to perform the upgrade, it will note that
  /AlwaysExcludeUpgrade parameter has been set and will log the following line in the

  ccmsetup.log:

  Client is stamped with /alwaysexcludeupgrade. Stop proceeding.

  CCMSetup will then immediately exit and not perform the upgrade.

/BITSPriority
