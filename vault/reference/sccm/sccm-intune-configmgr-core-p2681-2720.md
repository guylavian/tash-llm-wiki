---
title: "Core infrastructure documentation — pages 2681-2720"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2681-2720
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2681-2720
family: sccm
documentKind: "doc"
abstract: "７ Note Power management can only collect causes that prevented computers from entering sleep or hibernate from computers running Windows 7 or Windows Server 2008 R2. Use the following parameters to configure this report. Required report parameters The following parameters must b"
---

# Core infrastructure documentation — pages 2681-2720

<!-- p.2681 -->

  ７ Note

  Power management can only collect causes that prevented computers from
  entering sleep or hibernate from computers running Windows 7 or Windows Server
  2008 R2.

Use the following parameters to configure this report.

Required report parameters
The following parameters must be specified to run this report.

                                                                                   ﾉ   Expand table

 Parameter          Description
 Name

 Collection name    From the drop-down list, select a collection to use for this report.

 Report interval    Specify the number of days to report. The default value is 7 days. The
 (days)             maximum value is 365 days. Specify 0 to run the report for today.

Hidden report parameters
This report has no hidden parameters that you can set.

Report links
This report contains links to the following report which provides further information
about the selected item.

                                                                                   ﾉ   Expand table

 Report Name          Details

 Insomnia             Click a number in the Affected Computers column to see a list of computers
 Computer Details     that could not sleep or hibernate because of the selected cause.

                      For more information, see Insomnia Computer Details Report in this topic.

Power Capabilities report

<!-- p.2682 -->

The Power Capabilities report displays the power management hardware capabilities of
computers in the specified collection. This report is typically used in the monitoring
phase of power management to determine the power management capabilities of
computers in your organization. The information displayed in the report can then be
used to create collections of computers to apply power plans to, or to exclude from
power management. The power management capabilities displayed by this report are:

      Sleep Capable - Indicates whether the computer has the capability to enter sleep if
      it is configured to do so.

      Hibernate Capable – Indicates whether the computer can enter hibernate if it is
      configured to do so.

      Wake from Sleep – Indicates whether the computer can wake from sleep if it is
      configured to do so.

      Wake from Hibernate – Indicates whether the computer can wake from hibernate
      if it is configured to do so.

      The values reported by the Power Capabilities report indicate the sleep and
      hibernate capabilities of computers as reported by Windows. However, the
      reported values do not reflect cases where Windows or BIOS settings prevent these
      functions from working.

      Use the following parameters to configure this report.

Required report parameters

The following parameters must be specified to run this report.

                                                                                  ﾉ   Expand table

 Parameter      Description
 Name

 Collection     From the drop-down list, select a collection for this report.

 Display        From the drop-down list, select Not Supported to display only computers in the
 Filter         specified collection that are incapable of sleep, hibernate, wake from sleep, or
                wake from hibernate. Select Show All to display all computers in the specified
                collection.

Hidden report parameters

<!-- p.2683 -->

This report has no hidden parameters that you can set.

Report links
This report contains links to the following report which provides further information
about the selected item.

                                                                               ﾉ    Expand table

 Report Name     Details

 Computer        Click a computer name to see the power capabilities, power settings, and
 Details         applied power plans for the selected computer.

                 For more information, see Computer Details Report in this topic.

Power Settings report
The Power Settings report displays an aggregated list of power settings used by
computers in the specified collection. For each power setting, the possible power
modes, values, and units are displayed, together with a count of the number of
computers that use those values. This report can be used during the monitoring phase
of power management to help the administrator understand the existing power settings
used by computers in the site and to help plan optimal power settings to be applied by
using a power management plan. The report is also useful when troubleshooting to
validate that power settings were correctly applied.

  ７ Note

  The settings displayed are collected from client computers during hardware
  inventory. Depending on the time at which hardware inventory runs, settings from
  applied peak or non-peak power plans might be collected.

Use the following parameters to configure this report.

Required report parameters

The following parameters must be specified to run this report.

                                                                               ﾉ    Expand table

<!-- p.2684 -->

 Parameter Name          Description

 Collection name         From the drop-down list, select a collection for this report.

Hidden report parameters
The following hidden parameters can optionally be specified to change the behavior of
this report.

                                                                                  ﾉ      Expand table

 Parameter Name            Description

 numberOfLocalizations     Specify the number of languages in which you want to view power
                           setting names reported by client computers. If you only want to view
                           the most popular language, leave this setting at the default of 1. To view
                           all languages, set this value to 0.

Report links

This report contains links to the following report which provides further information
about the selected item.

                                                                                  ﾉ      Expand table

 Report Name       Details

 Power Settings    Click the number of computers in the Computers column to see a list of all
 Details           computers that use the power settings in that row.

                   For more information, see Power Settings Details Report in this topic.

Power Settings Details report
The Power Settings Details report displays further information about computers
selected in the Power Settings report. This report is called by the Power Settings report
and is not designed to be run directly by the site administrator.

Required report parameters

The following parameters must be specified to run this report.

<!-- p.2685 -->

                                                                                  ﾉ   Expand table

 Parameter     Description
 Name

 Collection    From the drop-down list, select a collection to use for this report.

 Power         From the drop-down list, select the power setting GUID on which you want to
 Setting       report. For a list of all power settings and their uses, see Available power
 GUID          management plan settings in the topic How to create and apply power plans.

 Power Mode    From the drop down list, select the type of power settings you want to display in
               the report results. Select Plugged In to view the power settings configured for
               when the computer is plugged in and On Battery to view the power settings
               configured for when the computer is running on battery power.

 Setting       From the drop-down list, select the value for the selected power setting name on
 Index         which you want to report. For example, if you want to display all computers with
               the turn off hard disk after setting set to 10 minutes, select turn off hard disk
               after for Power Setting Name and 10 for Setting Index.

Hidden report parameters
The following hidden parameters can optionally be specified to change the behavior of
this report.

                                                                                  ﾉ   Expand table

 Parameter Name            Description

 numberOfLocalizations     Specify the number of languages in which you want to view power
                           setting names reported by client computers. If you only want to view
                           the most popular language, leave this setting at the default of 1. To view
                           all languages, set this value to 0.

Report links
This report contains links to the following report which provides further information
about the selected item.

                                                                                  ﾉ   Expand table

 Report Name     Details

 Computer        Click a computer name to see the power capabilities, power settings, and
 Details         applied power plans for the selected computer.

<!-- p.2686 -->

 Report Name      Details

                  For more information, see Computer Details Report in this topic.

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.2687 -->

Security and privacy for power
management in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This section contains security and privacy information for power management in
Configuration Manager.

Security best practices for power management
There are no security-related best practices for power management.

Privacy information for power management
Power management uses features that are built into Windows to monitor power usage
and to apply power settings to computers during business hours and nonbusiness
hours. Configuration Manager collects power usage information from computers, which
includes data about when a user is using a computer. Although Configuration Manager
monitors power usage for a collection rather than for each computer, a collection can
contain just one computer. Power management is not enabled by default and must be
configured by an administrator.

The power usage information is stored in the Configuration Manager database and is
not sent to Microsoft. Detailed information is retained in the database for 31 days and
summarized information is retained for 13 months. You cannot configure the deletion
interval.

Before you configure power management, consider your privacy requirements.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2688 -->

Upgrade clients in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can use different methods to upgrade the Configuration Manager client software on
Windows computers and Mac computers. Here are the advantages and disadvantages
of each method.

   Tip

  If you are upgrading your server infrastructure from System Center 2012
  Configuration Manager, before upgrading the Configuration Manager clients,
  complete the server upgrades including installing all current branch updates. This
  process makes sure that you'll have the most recent version of the client software.

Group Policy installation
Supported client platform: Windows

Advantages:

      Doesn't require computers to be discovered before the client can be upgraded.

      Can be used for new client installations or for upgrades.

      Computers can read client installation properties that have been published to
      Active Directory Domain Services.

      Doesn't require you to configure and maintain an installation account for the
      intended client computer.

Disadvantages:

      Can cause high network traffic if you're upgrading many clients.

      If you don't extend the Active Directory schema for Configuration Manager, use
      Group Policy settings. These settings add client installation properties to
      computers in your site.

<!-- p.2689 -->

Logon script installation
Supported client platform: Windows

Advantages:

     Doesn't require computers to be discovered before the client can be installed.

     Can be used for new client installations or for upgrades.

     Supports using command-line properties for CCMSetup.

Disadvantages:

     Can cause high network traffic if you're upgrading many clients in a short time.

     Can take a long time to upgrade all client computers if users don't frequently sign
     in to the network.

For more information, see How to install clients by using logon scripts.

Manual installation
Supported client platform: Windows, macOS

Advantages:

     Doesn't require computers to be discovered before the client can be upgraded.

     Can be useful for testing purposes.

     Supports using command-line properties for CCMSetup.

Disadvantages:

     No automation, so can be time consuming.

For more information, see the following articles:

     How to install clients manually

     How to upgrade clients on Mac computers

Upgrade installation (application management)
Supported client platform: Windows

<!-- p.2690 -->

Advantages:

     Supports using command-line properties for CCMSetup.

Disadvantages:

     Can cause high network traffic if you distribute the client to large collections.

     Can only be used to upgrade the client software on computers that have been
     discovered and assigned to the site.

For more information, see How to install clients by using a package and program.

Automatic client upgrade
Supported client platform: Windows

Advantages:

     Because of the randomization over the specified period, only auto-upgrade is
     suitable for large-scale client upgrades. Other methods are either too slow on
     large scale, or don't have randomization.

       ７ Note

       Client piloting isn't good for large scale as it doesn't randomize at all.

     Can be used to automatically keep clients in your site at the latest version.

     Requires minimal administration.

Disadvantages:

     Can only be used to upgrade the client software and can't be used to install a new
     client.

     Applies to all clients in the hierarchy that are assigned to a site. Can't be scoped by
     collection.

     Limited scheduling options.

For more information, see How to upgrade clients for Windows computers.

Client testing

<!-- p.2691 -->

Supported client platform: Windows

Advantages:

     Can be used to test new client versions in a smaller pre-production collection.

     When testing is complete, clients in pre-production are promoted to production
     and automatically upgraded across the Configuration Manager site.

Disadvantages:

     Can only be used to upgrade the client software and can't be used to install a new
     client.

For more information, see How to test client upgrades in a pre-production collection.

Next steps
How to test client upgrades in a pre-production collection

How to exclude clients from upgrade

How to upgrade clients for Windows computers

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2692 -->

How to test client upgrades in a pre-
production collection
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can test a new Configuration Manager client version in a pre-production collection
before upgrading the rest of the site with it. When you do this process, the site only
updates devices that are part of the test collection. Once you've had a chance to test the
client, you can promote the client. Client promotion makes the new version of the client
software available to the rest of the site.

  ７ Note

  Only a user with the Full Administrator security role and the All security scope can
  promote a test client to production. For more information, see Fundamentals of
  role-based administration. This action is only available when connected to the
  central administration site (CAS) or a standalone primary site.

There are three steps to test clients in pre-production:

   1. Configure automatic client upgrades to use a pre-production collection.

   2. Install a Configuration Manager update that includes a new version of the client.

   3. Promote the new client to production.

Configure automatic client upgrades to use a
pre-production collection

  ） Important

  Pre-production client deployment isn't supported for workgroup computers. They
  can't use the authentication required for the distribution point to access the pre-
  production client package. They'll receive the latest client when it's promoted to be
  the production client.

   1. Set up a collection that contains the computers to which you want to deploy the
      pre-production client.

<!-- p.2693 -->

 2. In the Configuration Manager console, go to the Administration workspace,
    expand Site Configuration, and select the Sites node. In the ribbon, select
    Hierarchy Settings.

 3. Switch to the Client Upgrade tab, and configure the following settings:

          Select Upgrade all clients in the pre-production collection automatically
          using pre-production client.

          Select a collection to use as the Pre-production collection.

 ７ Note

 Only a user with the Full Administrator security role and the All security scope can
 change these settings.

Configure client upgrades during site update

<!-- p.2694 -->

   1. In the Configuration Manager console, go to the Administration workspace, and
     select the Updates and Servicing node. Select an available update, and then in the
     ribbon select Install Update Pack.

     For more information on installing updates, see Updates for Configuration
     Manager.

   2. During installation of the update, on the Client Options page of the wizard, select
     Test in pre-production collection.

   3. Complete the rest of the wizard and install the update pack.

After the wizard complete, clients in the pre-production collection will begin to deploy
the updated client. You can monitor the deployment of upgraded clients in the console.
Go to the Monitoring workspace, expand Client Status, and select the Pre-production
Client Deployment node. For more information, see How to monitor client deployment
status.

  ７ Note

  For computers in a pre-production collection that also host site system roles, their
  deployment status may report as Not compliant. This state may show even when
  the client was successfully updated. When you promote the client to production,
  the deployment status reports correctly.

Promote a new client to production
   1. In the Configuration Manager console, go to the Administration workspace, and
     select the Updates and Servicing node. In the ribbon, select Promote Pre-
     production Client.

           Tip

          The Promote Pre-production Client action is also available when you monitor
          client deployments in the console at Monitoring > Client Status > Pre-
          production Client Deployment.

   2. Review the client versions in production and pre-production, and make sure the
     correct pre-production collection is specified. When ready, select Promote, and
     then select Yes to confirm.

<!-- p.2695 -->

The updated client version now replaces the client version in use in your hierarchy. You
can then upgrade the clients for your whole site. For more information, see How to
upgrade clients for Windows computers.

  ７ Note

  To enable the pre-production client, or to promote a pre-production client to a
  production client, your account must be a member of a security role that has Read
  and Modify permissions for the Update Packages object.

  Client upgrades honor any Configuration Manager maintenance windows you
  configure. For more information on a known issue, see Client upgrade and
  maintenance windows.

Known issues

Pre-production client and site server high availability
Consider the following scenario:

     You enable the pre-production client.
     The site has a site server in passive mode.
     You update the site to the latest version.
     You promote the passive mode site server to the active site server.

After you promote the site server, the pre-production client version shows as the
production version. Depending on your configuration, it may automatically deploy to all
systems.

When you install an update, Configuration Manager currently updates the Client folder
of the site server in passive mode with the pre-production client version.

To work around this issue:

     Wait to promote the site server in passive mode until after you promote the pre-
     production client version to production version.

     If you have to fail over for high availability, manually correct the client version in
     the Client folder.

Next steps

<!-- p.2696 -->

How to exclude clients from upgrade

How to upgrade clients for Windows computers

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2697 -->

How to exclude clients from upgrade in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can exclude a collection of clients from automatically installing updated client
versions. Use this exclusion for a collection of computers that need greater care when
upgrading the client. A client that's in an excluded collection ignores requests to install
updated client software.

This exclusion applies to the following methods:

      Automatic upgrade
      Software update-based upgrade
      Logon scripts
      Group policy

  ７ Note

  Although the user interface states that clients won't upgrade via any method, there
  are two methods you can use to override these settings. Use client push or manual
  client installation to override this configuration. For more information, see How to
  upgrade an excluded client.

Configure exclusion
   1. In the Configuration Manager console, go to the Administration workspace.
      Expand Site Configuration, select the Sites node, and then select Hierarchy
      Settings in the ribbon.

   2. Switch to the Client Upgrade tab.

   3. Select the option to Exclude specified clients from upgrade. Then select the
      Exclusion collection you want to exclude. You can only select a single collection for
      exclusion.

   4. Select OK to close and save the configuration.

<!-- p.2698 -->

After clients in the excluded collection update policy, they don't automatically install
client updates. For more information, see How to upgrade clients for Windows
computers.

  ７ Note

  Excluded clients still download and run Ccmsetup, but don't upgrade.

When you remove a client from the exclude collection, it doesn't automatically upgrade
until the next auto-upgrade cycle.

How to upgrade an excluded client
If a device is a member of a collection that you excluded from upgrade, you can still
upgrade the client using one of the following methods:

     Client push installation: Ccmsetup allows client push installation because it's your
     direct intent. This method lets you upgrade a client without removing it from the
     collection, or removing the entire collection from exclusion.

<!-- p.2699 -->

     Manual client installation: Manually upgrade an excluded client by using the
     following Ccmsetup command-line parameter: /IgnoreSkipUpgrade

     If you attempt to manually upgrade a client that's a member of the excluded
     collection, and don't use this parameter, the client doesn't upgrade. For more
     information, see How to install Configuration Manager clients manually.

Next steps
     How to upgrade clients for Windows computers

     Extended interoperability client

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2700 -->

How to upgrade clients for Windows
computers in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Upgrade the Configuration Manager client on Windows computers using client
installation methods or the automatic client upgrade feature. The following client
installation methods are valid ways to upgrade client software on Windows computers:

      Group policy installation

      Logon script installation

      Manual installation

      Upgrade installation

For more information, see How to deploy clients to Windows computers.

Exclude clients from upgrade by specifying an exclusion collection. For more
information, see How to exclude clients from upgrade. Excluded clients still download
and run CCMSETUP, but won't upgrade.

   Tip

  If upgrade your server infrastructure from a previous version of Configuration
  Manager, complete the server upgrades before upgrading the Configuration
  Manager clients. This process includes installing all current branch updates. The
  latest current branch update contains the latest version of the client. Upgrade
  clients after you have installed all of the Configuration Manager updates.

  ７ Note

  If you plan to reassign the site for the clients during upgrade, specify the new site
  using the SMSSITECODE client.msi property. If you use the value of AUTO for the
   SMSSITECODE , also specify SITEREASSIGN=TRUE . This property allows for automatic

  site reassignment during upgrade. For more information, see Client installation
  properties - SMSSITECODE.

<!-- p.2701 -->

About automatic client upgrade
Configure the site to automatically upgrade clients to the latest Configuration Manager
version. When Configuration Manager identifies an assigned client's version is earlier
than the hierarchy version, it automatically upgrades the client. This scenario includes
upgrading the client to the latest version when it attempts to assign to a Configuration
Manager site.

A client can automatically upgrade in the following scenarios:

     The client version is earlier than the version used in the hierarchy.

     The client on the central administration site (CAS) has a language pack installed
     and the existing client doesn't.

     A client prerequisite in the hierarchy is a different version than the one installed on
     the client.

     One or more of the client installation files are a different version.

  ７ Note

  To identify the different versions of the Configuration Manager client in your
  hierarchy, use the report Count of Configuration Manager clients by client
  versions in the report folder Site - Client Information.

Configuration Manager creates an upgrade package by default. It automatically sends
the package to all distribution points in the hierarchy. If you make changes to the client
package on the CAS, Configuration Manager automatically updates the package, and
redistributes it. An example change is when you add a client language pack. If you
enable automatic client upgrade, every client automatically installs the new client
language package.

Enable automatic client upgrade across your hierarchy. This configuration keeps your
clients up to date with less effort.

If you also manage your Configuration Manager site systems as clients, determine
whether to include them as part of the automatic upgrade process. You can exclude all
servers, or a specific collection from client upgrade. Some Configuration Manager site
roles share the client framework. For example, the management point and pull
distribution point. These roles upgrade when you update the site, so the client version
on these servers updates at the same time.

<!-- p.2702 -->

Configure automatic client upgrade
Use the following procedure to configure automatic client upgrade at the CAS. This
configuration applies to all clients in your hierarchy.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and then select the Sites node.

   2. On the Home tab of the ribbon, in the Sites group, select Hierarchy Settings.

   3. Switch to the Client Upgrade tab. Review the version and date of the production
     client. Make sure it's the version you want to use to upgrade your clients. If it's not
     the client version you expect, you may need to promote the pre-production client
     to production. For more information, see How to test client upgrades in a pre-
     production collection.

   4. Select Upgrade all clients in the hierarchy using the production client. Select OK
     to confirm.

   5. If you don't want client upgrades to apply to servers, select Do not upgrade
     servers.

   6. Specify the number of days in which devices must upgrade the client. After the
     device receives policy, it upgrades the client at a random interval within this
     number of days. This behavior prevents a large number of clients simultaneously
     upgrading.

        ７ Note

        A computer must be running to upgrade the client. If a computer isn't running
        when it's scheduled to receive the upgrade, the upgrade doesn't occur. When
        the computer turns on, and it receives policy, it schedules the upgrade for a
        random time within the allowed number of days. If this occurs after the
        number of days to upgrade has expired, it schedules the upgrade at a random
        time within 24 hours after the computer was turned on.

        Because of this behavior, computers that are routinely shut down may take
        longer to upgrade than expected if the randomly scheduled upgrade time
        isn't within the normal working hours.

   7. To exclude clients from upgrade, select Exclude specified clients from upgrade,
     and specify the collection to exclude. For more information, see Exclude clients
     from upgrade.

<!-- p.2703 -->

   8. If you want the site to copy the client installation package to distribution points
     that you've enabled for prestaged content, select the option to Automatically
     distribute client installation package to distribution points that are enabled for
     prestaged content.

   9. Select OK to save the settings and close Hierarchy Settings Properties.

Clients receive these settings when they next download policy.

  ７ Note

  Client upgrades honor any Configuration Manager maintenance windows you've
  configured. The ClientServicing thread only runs the client setup bootstrap
  program (ccmsetup.exe) during a maintenance window. For more information on a
  known issue, see Client upgrade and maintenance windows.

  If the device runs an edition of Windows with a write filter, ccmsetup tries to
  download and install at the same time. Otherwise, ccmsetup randomizes a time to
  download content. After it downloads content and compiles the local policy,
  ClientServicing schedules the client upgrade during the next maintenance window.

Known issues

Client upgrade and maintenance windows
For clients version 2111 or earlier, when you upgrade them to a later version, the
process only honors any business hours that the user defines. It doesn't use the
administrator-defined maintenance window. For example:

     Administrator-defined maintenance window: 12 AM - 5 AM
     User-defined business hours: 5 AM - 10 PM

The client upgrade starts at 10 PM after the business hours. It doesn't wait until the start
of the maintenance window at 12 AM.

This issue is fixed with the version 2203 client. When you upgrade clients from version
2203 to a later version, they will honor maintenance windows.

Next steps

<!-- p.2704 -->

For alternative methods to upgrade clients, see How to deploy clients to Windows
computers.

Exclude specific clients from automatic upgrade. For more information, see How to
exclude clients from upgrade.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2705 -->

How to upgrade clients on Mac
computers in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in January 2022, this feature of Configuration Manager is deprecated. For
  more information, see Mac computers.

Follow the high-level steps in this article to upgrade the client for Mac computers by
using a Configuration Manager application. You can also download the Mac client
installation file, copy it to a shared network location or a local folder on the Mac
computer, and then instruct users to manually run the installation.

  ７ Note

  Before you do these steps, make sure that your Mac computer meets the
  prerequisites. For more information, see Supported operating systems for Mac
  computers.

Download the latest Mac client
The Mac client for Configuration Manager isn't supplied on the Configuration Manager
installation media. The Mac client installation files are contained in a Windows Installer
file named ConfigmgrMacClient.msi.

  ７ Note

  The macOS client installation package isn't available for new deployments, but
  existing deployments are supported until December 31, 2022.

Create the Mac client installation file
On a computer that runs Windows, run ConfigmgrMacClient.msi. This installer unpacks
the Mac client installation file, named Macclient.dmg. By default, you can find this file in

<!-- p.2706 -->

the following folder: C:\Program Files\Microsoft\System Center Configuration
Manager for Mac client.

Extract the client installation files
Copy Macclient.dmg to a Mac computer. Mount the Macclient.dmg file in macOS, and
then copy the contents to a folder on the Mac computer.

Create a .cmmac file
   1. Open the Tools folder of the Mac client installation files. Use the CMAppUtil tool
      to create a .cmmac file from the client installation package. You'll use this file to
      create the Configuration Manager application.

   2. Copy the new CMClient.pkg.cmmac file to a network location that's available to
      the computer running the Configuration Manager console.

      For more information, see the Supplemental procedures to create and deploy
      applications for Mac computers.

Create and deploy the app
   1. In the Configuration Manager console, create an application from the
      CMClient.pkg.cmmac file.

   2. Deploy this application to Mac computers in your hierarchy.

Install the updated client
The existing Configuration Manager client on Mac computers will prompt the user that
an update is available to install. After users install the client, they must restart their Mac
computer.

After the computer restarts, the Computer Enrollment wizard automatically runs to
request a new user certificate.

If you don't use Configuration Manager enrollment, but install the client certificate
independently from Configuration Manager, see Configure clients to use an existing
certificate.

<!-- p.2707 -->

Configure clients to use an existing certificate
Use this procedure to prevent the Computer Enrollment Wizard from running, and to
configure the upgraded client to use an existing client certificate.

   1. In the Configuration Manager console, create a configuration item of the type Mac
     OS X.

   2. Add a setting to this configuration item with the setting type Script.

   3. Add the following script to the setting:

        Shell

        #!/bin/sh
        echo "Starting script\n"
        echo "Changing directory to MAC Client\n"
        cd /Users/Administrator/Desktop/'MAC Client'/
        echo "Import root cert\n"
        /usr/bin/sudo /usr/bin/security import
        /Users/Administrator/Desktop/'MAC Client'/Root.pfx -A -k
        /Library/Keychains/System.Keychain -P ROOT
        echo "Using openssl to convert pfx to a crt\n"
        /usr/bin/sudo openssl pkcs12 -in /Users/Administrator/Desktop/'MAC
        Client'/Root.pfx -out Root1.crt -nokeys -clcerts -passin pass:ROOT
        echo "Adding trust to root cert\n"
        /usr/bin/sudo /usr/bin/security add-trusted-cert -d -r trustRoot -k
        /Library/Keychains/System.Keychain Root1.crt
        echo "Import client cert\n"
        /usr/bin/sudo /usr/bin/security import
        /Users/Administrator/Desktop/'MAC Client'/MacClient.pfx -A -k
        /Library/Keychains/System.Keychain -P MAC
        echo "Executing ccmclient with MP\n"
        sudo ./ccmsetup -MP
        https://SCCM34387.SCCM34387DOM.NET/omadm/cimhandler.ashx
        echo "Editing Plist file\n"
        sudo /usr/libexec/Plistbuddy -c 'Add:SubjectName string CMMAC003L'
        /Library/'Application Support'/Microsoft/CCM/ccmclient.plist
        echo "Changing directory to CCM\n"
        cd /Library/'Application Support'/Microsoft/CCM/
        echo "Making connection to the server\n"
        sudo open ./CCMClient
        echo "Ending Script\n"
        exit

   4. Add the configuration item to a configuration baseline. Then deploy the
     configuration baseline to all Mac computers that install a certificate independently
     from Configuration Manager.

<!-- p.2708 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2709 -->

Manage clients over the internet with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Typically in Configuration Manager, most of the managed computers and servers are
physically on the same internal network as the site system servers that perform
management functions. However, you can manage clients outside your internal network
when they are connected to the internet. This ability doesn't require the clients to
connect via VPN to reach the site system servers.

Configuration Manager provides two ways to manage internet-connected clients:

      Cloud management gateway

      Internet-based client management

  ７ Note

  You can have a combination of both services for a single site. If a device gets policy
  from the site for both IBCM and CMG, then it randomizes between them for
  communication. The only mechanism available to control communication is client
  authentication. For example, if a Microsoft Entra joined client doesn't trust the
  server authentication certificate of the internet-based management point, it can
  only use the CMG. If a domain-joined client doesn't trust the server authentication
  certificate of the CMG, it can only use the internet-based management point.

Cloud management gateway
The cloud management gateway provides management of internet-based clients. It uses
a combination of a Microsoft Azure cloud service, and an on-premises site system role
that communicates with that service. Internet-based clients use the cloud service to
communicate with the on-premises Configuration Manager.

CMG advantages
      No additional on-premises infrastructure investment required.

      Does not expose on-premises infrastructure to the internet.

<!-- p.2710 -->

     Cloud virtual machines that run the service are fully managed by Azure and require
     no maintenance.

     Easily set up and configured in the Configuration Manager console.

CMG disadvantages
     Cloud subscription cost.

     Management data sent through cloud service.

Internet-based client management
This method relies on internet-facing site system servers to which clients directly
communicate for management purposes. It requires clients and site system servers to be
configured for internet-based client management (IBCM).

IBCM advantages
     No cloud service dependency.

     No additional cost associated with a cloud subscription.

     Full control of servers and roles providing the service.

IBCM disadvantages
     Require additional infrastructure investment.

     Overhead and operational cost of additional infrastructure.

     Infrastructure must be exposed to the internet.

Next steps
Overview of cloud management gateway

Plan for internet-based client management

Feedback

<!-- p.2711 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2712 -->

Cloud management gateway overview
Article • 12/16/2024

Applies to: Configuration Manager (current branch)

The cloud management gateway (CMG) provides a simple way to manage Configuration
Manager clients over the internet. You deploy CMG as a cloud service in Microsoft
Azure. Then without more on-premises infrastructure, you can manage clients that roam
on the internet or are in branch offices across the WAN. You also don't need to expose
your on-premises infrastructure to the internet.

After establishing the prerequisites, creating the CMG consists of the following three
steps in the Configuration Manager console:

   1. Deploy the CMG cloud service to Azure.
   2. Add the CMG connection point role.
   3. Configure the site and site roles for the service.

Once deployed and configured, clients seamlessly access on-premises site roles whether
they're on the intranet or internet.

This article provides the foundational knowledge to learn about the CMG and the
scenarios where you can use it.

Scenarios

<!-- p.2713 -->

There are several scenarios for which a CMG is beneficial. The following scenarios are
some of the more common:

     Manage traditional Windows clients with Active Directory domain-joined identity.
     These clients include any supported version of Windows. It uses PKI certificates to
     secure the communication channel. Management activities include:
        Software updates and endpoint protection
        Inventory and client status
        Compliance settings
        Software distribution to the device
        Windows in-place upgrade task sequence

     Manage traditional Windows 10 or later clients with modern identity, either hybrid
     or pure cloud domain-joined with Microsoft Entra ID. Clients use Microsoft Entra ID
     to authenticate rather than PKI certificates. Using Microsoft Entra ID is simpler to
     set up, configure and maintain than more complex PKI systems. Management
     activities are the same as the first scenario plus:
        Software distribution to the user

     Install the Configuration Manager client on Windows 10 or later devices over the
     internet. Using Microsoft Entra ID allows the device to authenticate to the CMG for
     client registration and assignment. You can install the client manually, or using
     another software distribution method, such as Microsoft Intune.

     New device provisioning with co-management. When auto-enrolling existing
     clients, CMG isn't required for co-management. It's required for new devices
     involving Windows Autopilot, Microsoft Entra ID, Microsoft Intune, and
     Configuration Manager. For more information, see Paths to co-management.

Specific use cases
Across these scenarios, the following specific device use cases may apply:

     Roaming devices such as laptops

     Remote/branch office devices that are less expensive and more efficient to manage
     over the internet than across a WAN or through a VPN.

     Mergers and acquisitions, where it may be easiest to join devices to Microsoft
     Entra ID and manage through a CMG.

     Workgroup clients. These devices may require other configurations, such as
     certificates.

<!-- p.2714 -->

     To help with management of remote workgroup clients, use Configuration
     Manager token-based authentication. For more information, see Token-based
     authentication for CMG.

  ） Important

  By default all clients receive policy for a CMG, and start using it when they become
  internet-based. Depending upon the scenario and use case that applies to your
  organization, you may need to scope usage of the CMG. For more information, see
  the Enable clients to use a cloud management gateway client setting.

Next steps
Develop your design and plan for implementing a CMG in your environment:

  Plan for the CMG

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2715 -->

Plan for the CMG in Configuration
Manager
Article • 11/16/2023

Applies to: Configuration Manager (current branch)

To simplify management of internet-based clients, first develop a plan for the cloud
management gateway (CMG). Design how it fits in your environment and prepare for
your implementation.

For more foundational knowledge of CMG scenarios and use cases, see Overview of
CMG.

  ７ Note

  Some sections that were previously in this article have moved:

        Hierarchy design: CMG hierarchy design
        Performance and scale: CMG performance and scale

Planning checklist
The overall CMG planning process is divided into the following parts:

      Components and requirements: This article summarizes the components that make
      up the CMG system. It also lists the system requirements.

      Client authentication: Determine which authentication method you'll use for clients
      from potentially untrusted networks.

      Hierarchy design: Plan where to place the CMG in your environment.

      Supported configurations: Understand which Configuration Manager features you
      can support on internet-based clients that connect to the CMG.

      Performance and scale: Decide how many service components you'll need to best
      support your number of clients.

      Cost: Understand the cost of the Azure-based components.

<!-- p.2716 -->

CMG components
Deployment and operation of the CMG includes the following components:

     The CMG cloud service in Azure authenticates and forwards Configuration
     Manager client requests over the internet to the on-premises CMG connection
     point.

     The CMG connection point site system role enables a consistent and high-
     performance connection from the on-premises network to the CMG service in
     Azure. It also publishes settings to the CMG including connection information and
     security settings. The CMG connection point forwards client requests from the
     CMG to on-premises roles according to URL mappings. For example, the
     management point and software update point.

     The service connection point site system role runs the cloud service manager
     component, which handles all CMG deployment tasks. Additionally, it monitors and
     reports service health and logging information from Microsoft Entra ID. Make sure
     your service connection point is in online mode.

     The management point and software update point site system roles service client
     requests per normal.

     The CMG uses a certificate-based HTTPS web service to help secure network
     communication with clients.

     Internet-based clients connect to the CMG to access on-premises Configuration
     Manager components. There are multiple options for client identity and
     authentication:
       Microsoft Entra ID
       PKI certificates
       Configuration Manager site-issued tokens

     For more information, see Plan for CMG client authentication.

     The CMG creates an Azure storage account, which it uses for its standard
     operations. By default, the CMG is also content-enabled to provide deployment
     content to internet-based clients. This storage account doesn't support
     customizations, such as virtual network restrictions.

       ７ Note

       The cloud-based distribution point (CDP) is deprecated. Starting in version
       2107, you can't create new CDP instances. To provide content to internet-

<!-- p.2717 -->

       based devices, enable the CMG to distribute content.

Azure Resource Manager
You create the CMG using an Azure Resource Manager deployment. Azure Resource
Manager is a modern platform for managing all solution resources as a single entity,
called a resource group. When you deploy a CMG with Azure Resource Manager, the
site uses Microsoft Entra ID to authenticate and create the necessary cloud resources.

  ） Important

  Starting in version 2203, the option to deploy a CMG as a cloud service (classic) is
  removed. All CMG deployments should use a virtual machine scale set. For more
  information, see Removed and deprecated features.

Virtual machine scale sets

  ７ Note

  This feature was first introduced in version 2010 as a pre-release feature. Starting
  in version 2107, it's no longer a pre-release feature.

  Configuration Manager doesn't enable this optional feature by default. You must
  enable this feature before using it. For more information, see Enable optional
  features from updates.

Starting in version 2010, customers with a Cloud Solution Provider (CSP) subscription
can deploy the CMG with a virtual machine scale set in Azure. This support is only if
they don't currently have a CMG deployed using classic cloud services to another
subscription.

Starting in version 2107, all customers can deploy a CMG with a virtual machine scale
set. If you have an existing CMG deployed with the classic cloud service, convert the
CMG to use a virtual machine scale set.

With a few exceptions, the configuration, operation, and functionality of the CMG
remains the same.

     Other Azure resource providers in your Azure subscription.

<!-- p.2718 -->

    Different deployment names, for example,
    GraniteFalls.EastUS.CloudApp.Azure.Com for a deployment in the East US Azure
    region. This name change can affect how you create and manage the CMG server
    authentication certificate.

    The CMG connection point only communicates with the virtual machine scale set in
    Azure over HTTPS. It doesn't require TCP-TLS ports.

Limitations for a CMG with a virtual machine scale set

Limitations with versions 2107 and later

 ７ Note

 Starting in version 2111, CMG deployments with a virtual machine scale set support
 Azure US Government cloud environments.

    Users may experience a delay of up to three seconds for actions in Software
    Center.
    You can't approve/deny application requests through the CMG.
    Version 2107 doesn't support Azure US Government cloud environments.

Limitations with versions 2010 and 2103

    If you require more than one CMG instance, they all have to use the same
    deployment method.
    The supported number of concurrent client connections is 2,000 per VM instance.
    For more information, see CMG performance and scale.
    It's only supported with a standalone primary site.
    It doesn't support Azure US Government cloud environments.
    Users may experience a delay of up to three seconds for actions in Software
    Center.
    Configuration Manager currently creates the Azure storage container based on the
    name of the resource group. Azure has different naming requirements for resource
    groups and storage containers. Make sure the name of the resource group for this
    service only has lowercase letters, numbers, and hyphens. If you have an existing
    resource group that doesn't work, rename it in the Azure portal, or create a new
    resource group.
    If you have more than one HTTPS management point, then you can't install the
    Configuration Manager client on devices over the internet. If you need to Install

<!-- p.2719 -->

   off-premises clients using a CMG, then you can only have one HTTPS management
   point. You also need to enable the CMG for content.
   You can't approve/deny application requests through the CMG.

Requirements

  Tip

 To clarify some Azure terminology:

      The Microsoft Entra ID tenant is the directory of user accounts and app
      registrations. One tenant can have multiple subscriptions.
      An Azure subscription separates billing, resources, and services. It's associated
      with a single tenant.

 For more information, see Subscriptions, licenses, accounts, and tenants for
 Microsoft's cloud offerings.

   An Azure subscription to host the CMG. This subscription can be in one of the
   following environments:
      Global Azure cloud
      Azure US Government cloud

   Customers with a Cloud Service Provider (CSP) subscription need to use version
   2010 or later with a virtual machine scale set deployment.

   Integrate the site with Microsoft Entra ID to deploy the service with Azure
   Resource Manager. For more information, see Configure Microsoft Entra ID for
   CMG.

   When you onboard the site to Microsoft Entra ID, you can optionally enable
   Microsoft Entra user discovery. It isn't required to create the CMG, but required if
   you plan to use Microsoft Entra authentication with hybrid identities. For more
   information, see Install clients using Microsoft Entra ID and see About Microsoft
   Entra user discovery.

   An Azure administrator needs to participate in the initial creation of certain
   components. This persona can be the same as the Configuration Manager
   administrator, or separate. If separate, they don't require permissions in
   Configuration Manager.

<!-- p.2720 -->

        When you integrate the site with Microsoft Entra ID for deploying the CMG
        using Azure Resource Manager, you need a Global Administrator.

        When you create the CMG, you need an account that is an Azure Subscription
        Owner and a Microsoft Entra ID Global Administrator.

     Your user account needs to be a Full administrator or Infrastructure administrator
     in Configuration Manager.

     At least one on-premises Windows server to host the CMG connection point. You
     can colocate this role with other Configuration Manager site system roles.

     The service connection point must be in online mode.

     Configure the management point to allow traffic from the CMG. It also needs to
     require HTTPS, or configure the site for Enhanced HTTP.

     A server authentication certificate for the CMG.

     CMG names need to be between 3-24 alphanumeric characters. The name must
     begin with a letter, end with a letter or digit, and not contain consecutive hyphens.

     Other certificates may be required, depending upon your client OS version and
     authentication model. For more information, see Configure client authentication.

     Clients must use IPv4.

     Make sure the following client settings in the Cloud services group are enabled for
     devices that will use the CMG:
        Enable clients to use a cloud management gateway
        Allow access to cloud distribution point

       ７ Note

       If you enable the client setting to Download delta content when available,
       the content for third-party updates won't download to clients.

Next steps
Next, determine how clients will authenticate with the CMG:

 Plan for CMG client authentication
