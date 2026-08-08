---
title: "Device compliance documentation — pages 1-40"
type: reference
domain: sccm
slug: sccm-intune-configmgr-compliance-p0001-0040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-compliance-p0001-0040
family: sccm
documentKind: "doc"
abstract: "Device compliance documentation Configuration Manager gives you the tools and resources you need to manage the configuration and compliance of devices in your organization. About device compliance ｅ OVERVIEW Introduction to device compliance Get started with compliance settings"
---

# Device compliance documentation — pages 1-40

<!-- p.1 -->

Device compliance documentation
Configuration Manager gives you the tools and resources you need to manage the
configuration and compliance of devices in your organization.

  About device compliance

  ｅ OVERVIEW
  Introduction to device compliance

  Get started with compliance settings

  Ｙ ARCHITECTURE
  Plan for and configure compliance settings

  Get started

  ｂ GET STARTED
  Common tasks for managing compliance

  Create configuration items for Windows 10 and later devices

  Create configuration baselines

  ｀ DEPLOY
  Deploy configuration baselines

  ｃ HOW-TO GUIDE
  Monitor compliance settings

  Top tasks

  ｃ HOW-TO GUIDE
  Create custom configuration items

<!-- p.2 -->

Create remote connection profiles

Create user data and profiles configuration items

ｐ CONCEPT
OneDrive for Business Profiles

Manage configuration data

<!-- p.3 -->

Understand compliance in
Configuration Manager
Article • 12/31/2024

Configuration Manager supports compliance features to help organizations meet
national, regional, and industry-specific regulations. Configuration Manager aligns with
Microsoft's commitment to data protection, privacy, and compliance, by offering tools
to help secure and manage data effectively.

Shared responsibility model
Microsoft ensures that Configuration Manager complies with various industry standards
and regulatory frameworks. However, customers are responsible for implementing their
data protection and compliance strategies to align with their specific organizational
requirements.

Compliance dependencies
Configuration Manager leverages other Microsoft services for compliance, including:

      Microsoft Entra ID: Identity and access management.
      Microsoft Intune: Enforces device compliance and conditional access policies.

Microsoft Intune capabilities for compliance
Microsoft Intune helps enforce compliance policies and protect organizational data
specifically for Intune:

      Conditional Access: Ensures only compliant devices and apps managed by Intune
      can access sensitive data. See Conditional Access.
      Device Compliance Enforcement: Enforces device compliance policies to meet
      organizational security requirements. See Device Compliance Policies.

For more information about Intune compliance capabilities, visit the Microsoft Intune
documentation.

  ７ Note

<!-- p.4 -->

  For more information about how to concurrently manage Windows 10 or later
  devices by using both Configuration Manager and Microsoft Intune, see What is
  co-management?.

Data encryption
Use Configuration Manager to manage BitLocker Drive Encryption (BDE) for on-
premises Windows clients, which are joined to Active Directory. It provides full BitLocker
lifecycle management that can replace the use of Microsoft BitLocker Administration
and Monitoring. For more information, see Plan for BitLocker management.

Compliance features
Configuration Manager includes several compliance features that help organizations
manage device compliance. For more information, see Ensure device compliance with
Configuration Manager.

Related articles
     Microsoft Privacy Statement
     Microsoft Trust Center
     Additional privacy information
     Fundamentals of security

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.5 -->

Ensure device compliance with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Compliance settings in Configuration Manager gives you the tools and resources you
need to manage the configuration and compliance of devices in your organization. This
helps you support the following business requirements:

      Compare the configuration of Windows PCs, Macs computers, servers, and mobile
      devices you manage against best practices configurations you create, or obtain
      from other vendors

      Identify unauthorized device configurations

      Report compliance with regulatory policies and in-house security policies

      Identify security vulnerabilities

      Provide the help desk with the information to detect probable causes of reported
      incidents and problems by identifying noncompliant configurations

      Automatically remediate some noncompliant settings on mobile devices

      Remediate noncompliance by deploying applications, packages and programs, or
      scripts to a collection that is automatically populated with devices that report that
      they are out of compliance

Get started
Learn the basics about compliance settings, and the tasks you can accomplish with
them.

Get started with compliance settings

Plan and design
Before you start working with compliance settings, make sure you have implemented
the necessary prerequisites that you'll find in this topic.

Plan for and configure compliance settings

<!-- p.6 -->

Common tasks
In this section, you'll find some common scenarios that will help you learn to use
compliance settings in Configuration Manager.

Common tasks for managing compliance

Remote connection profiles
This configuration item type allows you to configure your user's PCs to remotely
connect to work computers when they are not connected to the domain or if their
personal computers are connected over the Internet.

Create remote connection profiles

User data and profiles
This configuration item type contains settings that can manage folder redirection, offline
files and roaming profiles on computers that run Windows 8 and later for users in your
hierarchy.

Create user data and profiles configuration items

Windows edition upgrade policy
The edition upgrade policy lets you automatically upgrade Windows 10 devices to a
newer version. You can specify a product key to upgrade Windows 10 desktop versions,
or a license file that can be used to upgrade devices running Windows 10 Mobile and
Windows 10 Holographic.

Upgrade Windows devices with the edition upgrade policy

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.7 -->

Get started with compliance settings in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before creating Configuration Manager compliance settings, first learn about core
concepts and understand how they work.

How compliance settings work
Compliance settings let you manage the configuration and compliance of clients in your
organization.

Configuration items fall into two main categories:

      Settings for devices that are managed with the Configuration Manager client -
      typically devices on which you've installed Configuration Manager client software
      to let you manage the device.

      Settings for devices that are managed without the Configuration Manager client
      - typically devices that are managed with Microsoft Intune, or with Configuration
      Manager on-premises device management.

What devices are supported?
                                                                                   ﾉ   Expand table

 Device type                       More information

 Windows PCs (with the             Create custom configuration items to assess objects such as
 Configuration Manager client)     registry keys, files, and Active Directory attributes.

                                   When you use the Windows 10 or later configuration item
                                   type, select settings from a predefined list.

 Windows PCs (enrolled with on-    Select settings from a predefined list.
 premises MDM)

 Windows Phone devices (enrolled   Select settings from a predefined list.
 with on-premises MDM)

<!-- p.8 -->

 Device type                       More information

 Mac computers (with the           Create custom configuration items to assess objects such as
 Configuration Manager client)     macOS preferences, and results returned by a script.

  ７ Note

  On-premises MDM and the Configuration Manager client for macOS are both
  deprecated. For more information, see Removed and deprecated features for
  Configuration Manager.

What is a configuration item?
A configuration item is a container that stores specific information. The information you
configure depends on the configuration item type. Configuration items can include the
following information:

     Detection method information is only for Windows configuration items that
     contain application settings. It detects whether an application is installed. This
     detection uses the Windows installer file for the application, or by using a custom
     script.

     Settings represent the business or technical conditions to assess compliance on
     client devices. Configure a new setting or browse to an existing setting on a
     reference computer.

     Compliance rules specify the conditions that define the compliance of a
     configuration item setting. Before the client evaluates a setting for compliance, it
     must have at least one compliance rule. Some settings remediate noncompliant
     values. Create new rules, or browse to an existing setting in any configuration item
     and select rules in it.

     Supported platforms are the device platforms you define on which the client
     evaluates compliance of the configuration items. If you deploy a configuration
     item to a device that is not in the supported platforms list, it does not evaluate
     compliance.

What is a configuration baseline?
Define a configuration baseline that includes the configuration items to evaluate. Also
include the settings and rules that describe the required level of compliance. Import this

<!-- p.9 -->

configuration data from Configuration Manager configuration packs. Microsoft and
other vendors define these configuration packs. Or create new configuration items and
configuration baselines.

After you define a configuration baseline, deploy it to user and device collections. The
client then evaluates the baseline settings for compliance on a schedule. You can deploy
more than one configuration baseline to devices. This granularity provides greater
control of compliance.

Client devices evaluate their compliance against each deployed configuration baseline
and immediately report the results to the site by using state messages and status
messages. If a device is currently disconnected from the network, but downloaded the
configuration baseline, it still evaluates compliance of the configuration items. It sends
the compliance information when it reconnects.

Monitoring configuration baselines
     Monitor the results of the compliance evaluation in the Configuration Manager
     console, under the Monitoring workspace, in the Deployments node. For example:
        Common causes of noncompliance
        Errors
        The number of affected users and devices
     Run compliance settings reports with additional details. For example:
        Which devices are compliant or non-compliant
        Which element of the configuration baseline is causing a computer to be non-
        compliant
     View compliance evaluation results from Windows computers running the
     Configuration Manager client. Open the Configuration Manager control panel,
     and switch to the Configurations tab.

User data and profiles configuration items
Configuration items for user data and profiles include settings that control how users on
computers that run Windows 8 and later manage:

     Folder redirection
     Offline files
     Roaming profiles

Deploy these configuration items to user collections. Monitor their compliance from the
Monitoring node of the Configuration Manager console. Unlike other configuration

<!-- p.10 -->

items, don't add them to configuration baselines before you deploy them. Deploy them
directly by clicking Deploy in the ribbon.

For more information, see Create user data and profiles configuration items.

Remote connection profiles
Remote connection profiles provide a set of tools and resources to help you create,
deploy, and monitor remote connection settings. By deploying these settings to devices,
you minimize the effort that end users require to connect their computers to the
corporate network.

For more information, see Create remote connection profiles.

Windows edition upgrade
The edition upgrade policy automatically upgrades devices that run certain versions of
Windows 10 to a newer edition. This policy supplies a new product key or license file
that the device consumes to upgrade.

For more information, see Upgrade Windows devices with the edition upgrade policy

Next steps
Plan for and configure compliance settings

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.11 -->

Plan for and configure compliance
settings in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before you start working with Configuration Manager compliance settings, there are a
few prerequisites you need to know about, and some configuration tasks you'll need to
perform.

Prerequisites for compliance settings
                                                                                ﾉ   Expand table

 Prerequisite                           More information

 Windows Configuration Manager          See below
 clients must be enabled and
 configured for compliance
 evaluation.

 If you want to run reports, then you   Introduction to reporting
 must configure reporting for your
 site.

 Required security permissions.         The Compliance Settings Manager security role includes
                                        the necessary permissions to manage compliance settings,
                                        user data and profiles configuration items, and remote
                                        connection profiles.

                                        Configure role-based administration

Enable and configure compliance settings (for
Windows PCs only)
This procedure configures the default client settings for compliance settings and applies
to all computers in your hierarchy. If you want these settings to apply to only some
computers, create a custom device client setting and assign it to a collection that
contains the computers for which you want to use compliance settings. For more
information about how to create custom device settings, see How to configure client
settings.

<!-- p.12 -->

   Tip

  Other device types require no specific configuration to evaluate compliance
  settings.

   1. In the Configuration Manager console, click Administration > Client Settings >
     Default Settings.
   2. On the Home tab, in the Properties group, click Properties.
   3. In the Default Settings dialog box, click Compliance Settings.
   4. Configure the following client settings for compliance settings:

              Enable compliance evaluation on clients - Set to True if you want to evaluate
              compliance on client devices.
              Schedule compliance evaluation - Click Schedule if you want to modify the
              default compliance evaluation schedule on client devices.
              Enable User Data and Profiles - Enable this option if you want to create and
              deploy user data and profiles configuration items to Windows computers. For
              details, see Create user data and profiles configuration items.

   5. Click OK to close the Default Settings dialog box.

Client computers are configured with these settings the next time they download client
policy.

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.13 -->

Common tasks for managing
compliance with Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

In this section, you'll find some common scenarios that will help you learn to use
compliance settings in Configuration Manager.

For devices that run the Configuration
Manager client
Common tasks for managing compliance on devices with the Configuration Manager
client

For devices that do not run the Configuration
Manager client
Common tasks for managing compliance on devices not running the Configuration
Manager client

Scenarios for creating and deploying
configuration baselines
Common tasks for creating and deploying configuration baselines with Configuration
Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.14 -->

Common tasks for managing
compliance on devices with the
Configuration Manager client
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article gives you an introduction to using Configuration Manager compliance
settings by guiding you through some common scenarios that you might come across.

If you're already familiar with compliance settings, you can find detailed information
about all the features you use in Configuration items for devices managed with the
Configuration Manager client.

Before you start, read Get started with compliance settings to learn some basics about
compliance settings. Read Plan for and configure compliance settings for information
about necessary prerequisites.

General information for each scenario
In each scenario, you'll create a configuration item that performs a specific task. To open
the Create Configuration Item Wizard and get started, take these steps:

   1. In the Configuration Manager console, select Assets and Compliance >
      Compliance Settings > Configuration Items.

   2. On the Home tab, in the Create group, select Create Configuration Item.

   3. On the General page of the Create Configuration Item Wizard, shown in the
      following screenshot, specify a name and description for the configuration item.
      Then choose the appropriate configuration item type for each scenario in this
      article.

<!-- p.15 -->

Scenario: Disable Bluetooth on Windows 10 or
later devices
In this scenario, your security department has determined that the Bluetooth capability
on devices could be used to transmit sensitive corporate information outside the
company. You decide to disable Bluetooth on these devices.

   1. On the General page of the Create Configuration Item Wizard, select the Windows
     10 or later configuration item type, and then select Next.

   2. On the Supported Platforms page of the wizard, select all Windows 10 or later
     platforms.

   3. On the Device Settings page, select Device, and then select Next.

   4. On the Device page, select Prohibited as the value for Bluetooth.

   5. Select Remediate noncompliant settings to ensure the change is applied to all
     Windows 10 or later devices.

   6. Complete the wizard to create the configuration item.

<!-- p.16 -->

You can now use the information in the Common tasks for creating and deploying
configuration baselines with Configuration Manager article to help you deploy the
configuration you've created to devices.

Scenario: Remediate an incorrect registry value
on Windows desktop computers

  ７ Note

  On Mac computers running the Configuration Manager client, you have two
  options for assessing compliance:

        Evaluate a macOS X preferences (plist) file.
        Use a custom script and evaluate the results returned by the script.

  For more information, see How to create configuration items for macOS X devices
  managed with the Configuration Manager client.

In this scenario, you discover that an important line-of-business app doesn't run
correctly on some Windows 8.1 computers that you manage. You determine that this is
because a registry key named HKEY_LOCAL_MACHINE\SOFTWARE\Woodgrove\LOB
App\Configuration\Configuration1 is set to a value of 0 on some computers. For the
line-of-business app to run successfully, this value needs to be set to 1.

In this procedure, you'll create a configuration item that monitors for and automatically
remediates any incorrect registry key values that are found.

   1. On the General page of the Create Configuration Item Wizard, select the Windows
     Desktops and Servers (custom) configuration item type, and then select Next.

   2. On the Supported Platforms page of the wizard, select Windows 8.1 (to ensure the
     configuration item applies only to affected computers).

   3. On the Settings page, select New to create a new setting.

   4. On the General tab of the Create Setting dialog box, configure these settings:

           Name > Example setting

           Setting type > Registry value

           Data type > Integer (because the value contains a number only)

<!-- p.17 -->

           Hive > HKEY_LOCAL_MACHINE

           Key > SOFTWARE\Woodgrove\LOB App\Configuration\Configuration1

           Value > 1 (the required value)

   5. On the Compliance Rules tab of the Create Setting dialog box, select New. In the
     Create Rule dialog box, configure these settings:

           Name > Example Rule

           Selected setting > Verify that the selected setting is Example setting.

           Rule type > Value

           The setting must comply with the following rule > Verify that the setting
           name is correct and configure the option to specify that the setting value
           must equal 1.

           Remediate noncompliant rules when supported > Select this check box to
           ensure that Configuration Manager will reset the registry key value to the
           correct value if it's incorrect.

   6. Complete the wizard to create the configuration item.

You can now use the information in the Common tasks for creating and deploying
configuration baselines article to help you deploy the configuration you've created to
devices.

Next steps
Create and deploy configuration baselines

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.18 -->

Common tasks for creating and
deploying configuration baselines with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic contains common scenarios to help you learn about how to create and deploy
Configuration Manager configuration baselines.

If you are already familiar with compliance settings, you can find detailed
documentation about all the features you use in the Create configuration baselines and
Deploy configuration baselines topics.

Before you start, read Get started with compliance settings to learn some basics about
compliance settings, and also read Plan for and configure compliance settings to
implement any necessary prerequisites.

Create a configuration baseline
In this example, you've created a configuration item for only or later PCs that run the
Configuration Manager client.

This configuration item enforces a required password of at least 6 characters on
Windows 10 or later PCs. The configuration item is named Windows 10 or later
password enforcement.

Use the following procedure to learn how to add this configuration item to a
configuration baseline to prepare it for deployment.

   1. In the Configuration Manager console, click Assets and Compliance > Compliance
      Settings > Configuration Baselines.

   2. On the Home tab, in the Create group, click Create Configuration Baseline.

   3. In the Create Configuration Baseline dialog box, configure the following settings:

            Name - Enter Windows 10 or later passwords (or another name of your
            choice)

   4. Click Add > Configuration Items.

<!-- p.19 -->

   5. In the Add Configuration Items dialog box, select the Windows 10 or later
     password enforcement configuration item that you previously created, then click
     Add.

   6. Click OK to close the Add Configuration Items dialog box and return to the Create
     Configuration Baseline dialog box.

   7. Click OK to close the Create Configuration Baseline dialog box.

     You can now see the configuration baseline in the Configuration Baselines node of
     the Configuration Manager console.

Deploy the configuration baseline
In this example, you deploy the configuration baseline you created in the previous
procedure to a collection of computers.

   1. In the Configuration Manager console, click Assets and Compliance > Compliance
     Settings > Configuration Baselines.

   2. From the list of configuration baselines, select Windows 10 or later passwords.

   3. On the Home tab, in the Deployment group, click Deploy.

   4. In the Deploy Configuration Baselines dialog box, configure the following
     settings:

            Selected configuration baselines - Ensure that the Windows 10 or later
            passwords configuration baseline was automatically added to this list.

            Remediate noncompliant rules when supported - Check this box to ensure
            that if the correct settings are not present on targeted devices, then they are
            remediated by Configuration Manager.

            Collection - Click Browse to choose the collection of computers on which the
            configuration baseline is evaluated and remediated for compliance. In this
            example, the configuration baseline was deployed to the built-in All Desktop
            and Server Clients collection.

               Tip

              Don't worry if the collection you choose contains computers or devices
              that don't run Windows 10 or later. As long as you configured supported

<!-- p.20 -->

              platforms in the configuration item you created, only Windows 10 or
              later PCs are evaluated for compliance.

           If necessary, configure the schedule by which the configuration baseline is
           evaluated. Otherwise, keep the default of 7 Days.

   5. Click OK to close the Deploy Configuration Baselines dialog box and create the
     deployment.

     If you want to take a quick look at compliance statistics for this deployment, in the
     Monitoring workspace, click Deployments. At the bottom of the screen, you see a
     Compliance Statistics chart.

Next steps
For more detailed information about how to monitor configuration baselines, see
Monitor compliance settings.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.21 -->

Security and privacy for compliance
settings in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Security guidance

Don't monitor sensitive data
To help avoid information disclosure, don't configure configuration items to monitor
potentially sensitive information.

Don't configure compliance rules that use data that can
be modified by end users
If you create a compliance rule based on data that users can modify, such as registry
settings for configuration choices, the compliance results won't be reliable.

Only import configuration packs from external sources
that are digitally signed
Import configuration packs and other configuration data from external sources only if
they have a valid digital signature from a trusted publisher.

Published configuration data can be digitally signed so that you can verify the
publishing source and make sure that the data hasn't been tampered with. If the digital
signature verification check fails, you're warned and prompted to continue with the
import. If you can't verify the source and integrity of the data, don't import unsigned
data.

Implement access controls to protect reference
computers
Make sure that when an administrative user configures a registry or file system setting
by browsing to a reference computer, the reference computer isn't compromised.

<!-- p.22 -->

Secure the communication channel when you browse to a
reference computer
To prevent tampering of the data when it's transferred over the network, use internet
protocol security (IPsec) or server message block (SMB) signing between the computer
that runs the Configuration Manager console and the reference computer.

Restrict and monitor role-based administration for
compliance settings
Restrict and monitor the administrative users who are granted the Compliance Settings
Manager role-based security role.

Administrative users with this role can deploy configuration items to all devices and all
users in the hierarchy. Configuration items are powerful and can include, for example,
scripts and registry reconfiguration.

Privacy information
You can use compliance settings to evaluate whether your client devices are compliant
with configuration items that you deploy in configuration baselines. Some settings can
be automatically remediated if they out of compliance. Compliance information is sent
to the site server by the management point and stored in the site database. The
information is encrypted when devices send it to the management point, but not stored
in encrypted format in the site database. Compliance information isn't sent to Microsoft.

By default, devices don't evaluate compliance settings. You configure the configuration
items and configuration baselines, and then deploy them to devices.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.23 -->

Create configuration items in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Compliance settings in Configuration Manager let you create and deploy configurations
to both devices that are managed by Configuration Manager, and devices that are
enrolled with Microsoft Intune.

Configuration items for devices managed with
the Configuration Manager client
Before you start, read Get started with compliance settings. To learn some basics about
compliance settings, read Plan for and configure compliance settings to implement any
necessary prerequisites. In each scenario, you'll create a configuration item that does a
specific task.

      How to create configuration items for Windows 10 or later devices managed with
      the Configuration Manager client
      How to create configuration items for macOS X devices managed with the
      Configuration Manager client
      How to create custom configuration items for Windows desktop and server
      computers managed with the Configuration Manager client

Configuration items for devices managed with
Intune
Before you start, read Get started with compliance settings. To learn some basics about
compliance settings, read Plan for and configure compliance settings to implement any
necessary prerequisites. To review information about configuration items for devices
managed with Intune, see Configuration items for devices managed with Intune.

Next steps
Get started with compliance settings

<!-- p.24 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.25 -->

Create configuration items for Windows 10
or later devices
10/27/2025

Use the Configuration Manager Windows 10 or later configuration item to manage settings for
Windows 10 or later computers that are managed by the Configuration Manager client.

  ） Important

  In this release, if you created a Password setting as part of a configuration item of the
  type Windows 10 or later (for a device managed with the Configuration Manager client),
  be aware of the following problem. If the setting doesn't already exist, or hasn't been
  configured on the Windows 10 or later device, it will incorrectly evaluate as compliant.

  As a workaround, when you create a setting for these devices, ensure that Remediate
  noncompliant settings is selected on the settings pages of the Create Configuration Item
  wizard. In addition, when you deploy a configuration baseline containing a Windows 10 or
  later configuration item containing password settings, select Remediate noncompliant
  rules when supported. You make this selection in the Deploy Configuration Baselines
  dialog box. By using this workaround, the setting is monitored, and remediated if it's
  found to be noncompliant. After remediation, the setting is correctly reported as
  Compliant (unless a problem is encountered, in which case it will report Error).

To create a Windows 10 or later configuration item
   1. In the Configuration Manager console, select Assets and Compliance.

   2. In the Assets and Compliance workspace, expand Compliance Settings, and then select
     Configuration Items.

   3. On the Home tab, in the Create group, select Create Configuration Item.

   4. On the General page of the Create Configuration Item wizard, specify a name and
     optional description for the configuration item.

   5. Under Specify the type of configuration item that you want to create, select Windows
     10 or later.

   6. If you create and assign categories to help you search and filter configuration items in the
     Configuration Manager console, select Categories.

<!-- p.26 -->

 7. On the Supported Platforms page of the wizard, select the specific Windows 10 or later
   platforms that will evaluate the configuration item.

 8. On the Device Settings page of the wizard, select the settings group that you want to
   configure. (For details, see Windows configuration item settings reference in this article.)
   Then select Next.

       Tip

      If the setting that you want isn't listed, select the Configure additional settings that
      are not in the default setting groups check box.

 9. On each settings page, configure the settings you require, and whether you want to
   remediate them when they aren't compliant on devices (when this is supported).

10. For each settings group, you can also configure the severity reported when a
   configuration item is found to be noncompliant:

         None: Devices that fail this compliance rule don't report a failure severity for
         Configuration Manager reports.

         Information: Devices that fail this compliance rule report a failure severity of
         Information for Configuration Manager reports.

         Warning: Devices that fail this compliance rule report a failure severity of Warning
         for Configuration Manager reports.

         Critical: Devices that fail this compliance rule report a failure severity of Critical for
         Configuration Manager reports.

         Critical with event: Devices that fail this compliance rule report a failure severity of
         Critical for Configuration Manager reports. This severity level is also logged as a
         Windows event in the application event log.

11. On the Platform Applicability page of the wizard, review any settings that aren't
   compatible with the supported platforms you selected earlier. You can go back and
   remove these settings, or you can continue.

       Tip

      Unsupported settings are not assessed for compliance.

12. Complete the wizard.

<!-- p.27 -->

    You can view the new configuration item in the Configuration Items node of the Assets
    and Compliance workspace.

Windows 10 or later configuration item settings
reference

Password

                                                                                       ﾉ   Expand table

Setting                Details

Require password       Requires a password on supported devices.
settings on devices

Minimum password       The minimum length in characters for the password.
length (characters)

Password expiration    The number of days before the password must be changed.
in days

Number of passwords    Prevents reusing previous passwords.
remembered

Number of failed       Wipes the device if sign-in fails this number of times.
logon attempts
before a device is
wiped

Idle time before       Specifies how many minutes the device must be inactive before it's
device is locked       automatically locked.

Password complexity    Choose whether you can specify a PIN such as '1234', or whether you must
                       supply a strong password.

Number of complex      If you selected a Strong password, use this setting to configure the number of
character sets         complex character sets required. For a strong password, this setting should be
required in password   set to at least 3, which means both letters and numbers are required. Select 4 if
                       you want to enforce a password that additionally requires special characters,
                       such as (%$.
                       (Windows 10 or later only)

Device

                                                                                       ﾉ   Expand table

<!-- p.28 -->

Setting name                Details

Bluetooth                   Allows use of the Bluetooth feature on the device.

Cloud

                                                                                            ﾉ   Expand table

Setting name                                    Details

Settings synchronization                        Allows synchronization of settings between devices.

Credentials synchronization                     Allows synchronization of credentials between devices.

Settings synchronization over metered           Allows settings to be synchronized when the internet
connections                                     connection is metered.

Roaming

                                                                                            ﾉ   Expand table

Setting name           Details

Data roaming           Allows roaming between networks when accessing data.

Encryption

                                                                                            ﾉ   Expand table

Setting name                             Details

File encryption on device                Requires that files on the device are encrypted.

System security

                                                                                            ﾉ   Expand table

Setting name                          Details

User Account Control                  Configures how Windows User Account Control works on the device.
                                      For example, you can disable it, or set the level at which it notifies
                                      you.

<!-- p.29 -->

 Setting name                      Details

 Network firewall                  Enables or disables Windows Firewall.

 SmartScreen                       Enables or disables Windows SmartScreen.

 Virus protection                  Requires that antivirus software must be installed and configured.

 Virus protection signatures are   Requires that the signature files for the antivirus software on the
 up to date                        device must be up to date.

See also
Configuration items for devices managed with the Configuration Manager client

<!-- p.30 -->

Create configuration items for macOS X
devices
Article • 10/04/2022

  ） Important

  Starting in January 2022, this feature of Configuration Manager is deprecated. For
  more information, see Mac computers.

Use the Configuration Manager Mac OS X (custom) configuration item to manage
settings for macOS X devices that are managed by the Configuration Manager client.

The macOS X operating system uses property list (.plist) files to store application
settings. Use compliance settings to evaluate and remediate settings in a property list
file. You can also manage macOS X settings by writing a shell script that returns a value
that you can evaluate and remediate for compliance.

Create a custom macOS X configuration item
   1. In the Configuration Manager console, select Assets and compliance.

   2. In the Assets and Compliance workspace, expand Compliance Settings, and then
      select Configuration Items.

   3. On the Home tab, in the Create group, select Create Configuration Item.

   4. On the General page of the Create Configuration Item wizard, specify a name and
      optional description for the configuration item.

   5. Under Specify the type of configuration item that you want to create, select Mac
      OS X (custom).

   6. If you create and assign categories to help you search and filter configuration
      items in the Configuration Manager console, select Categories.

   7. On the Supported Platforms page of the wizard, select the specific macOS X
      versions that will evaluate the configuration item.

   8. On the Settings page of the wizard, add new settings that are evaluated for
      compliance on Mac computers. Select New to open the Create Setting dialog box.

<!-- p.31 -->

 9. In the Create Setting dialog box, enter a unique name and a description for the
   setting.

10. Choose the Setting type you want, and then supply the required information:

        Mac OS X Preferences

              Application ID: Specify the application ID of the property list file from
              which you want to evaluate a key for compliance.

              For example, if you want to edit settings for the Safari Web browser, you
              might use com.apple.Safari.plist.

              Key: Specify the name of the key that you want to evaluate for compliance
              on Mac computers. Use the following syntax: /<dictionary>/<keyname>.

                ） Important

                The key name is case sensitive, and won't be evaluated if it differs
                from the key name on the Mac computer. Additionally, you can't edit
                the key name after you have specified it. If you need to edit the key
                name, delete and then re-create the setting.

        Script

              Discovery Script: Select Add Script, and then enter a shell script to assess
              settings on the Mac computer for compliance. Use the echo command in
              the shell script to return values to Configuration Manager for compliance.
              Configuration Manager uses the results returned in STDOUT to evaluate
              compliance.

                ） Important

                Don't include the reboot command in the discovery script. Because
                the discovery script runs each time the client restarts, this causes the
                Mac computer to continually restart.

              Remediation script (optional): Optionally, select Add Script, and then
              enter a shell script that is used to remediate any noncompliant settings
              found on Mac client computers.

                ） Important

<!-- p.32 -->

                To ensure that you don't introduce formatting characters that the Mac
                computer can't interpret, don't use copy and paste. Instead, type in
                the script.

11. Choose the Data type, which is the format in which the condition returns the data
   before it's used to evaluate the setting.

      ７ Note

      The Floating point data type supports only 3 digits after the decimal point.

      Configuration Manager doesn't support using the Boolean data type for Mac
      configuration item script settings. Instead, set the data type to Integer, and
      ensure that the script returns an integer value.

12. Select OK to save the setting and close the Create Setting dialog box. Then
   continue to add as many settings as you require.

13. On the Compliance Rules page of the wizard, specify the conditions that define
   the compliance of a configuration item. Before a setting can be evaluated to
   compliance, it must have at least one compliance rule. Select New to add a new
   rule.

14. In the Create Rule dialog box, provide the following information:

           Name: Enter a name for the compliance rule.

           Description: Enter a description for the compliance rule.

           Selected setting: Select Browse to open the Select Setting dialog box. Select
           the setting that you want to define a rule for, or select New Setting. When
           you are finished, choose Select.

              Tip

             You can also select Properties to view information about the currently
             selected setting.

           Rule type: Select the type of compliance rule that you want to use:

             Value: Create a rule that compares the value returned by the configuration
             item against a value that you specify.

<!-- p.33 -->

  Existential: Create a rule that evaluates the setting depending on whether
  it exists on a device.

For a rule type of Value, specify the following information:

  The setting must comply with the following rule: Select an operator and
  a value that is assessed for compliance with the selected setting. You can
  use the following operators:

     Equals

     Not equal to

     Greater than

     Less than

     Between

     Greater than or equal to

     Less than or equal to

     One of: In the text box, specify one entry on each line.

     None of: In the text box, specify one entry on each line.

  Remediate noncompliant rules when supported: Select this option if you
  want Configuration Manager to automatically remediate noncompliant
  rules.

     ） Important

     You can only remediate noncompliant rules when the rule operator is
     set to Equals.

  Report noncompliance if this setting instance is not found: The
  configuration item reports noncompliance if this setting isn't found on the
  Mac computer.

  Noncompliance severity for reports: Specify the severity level reported if
  this compliance rule fails. The available severity levels are:

     None: Computers that fail this compliance rule don't report a failure
     severity for Configuration Manager reports.

<!-- p.34 -->

     Information: Computers that fail this compliance rule report a failure
     severity of Information for Configuration Manager reports.

     Warning: Computers that fail this compliance rule report a failure
     severity of Warning for Configuration Manager reports.

     Critical: Computers that fail this compliance rule report a failure severity
     of Critical for Configuration Manager reports.

     Critical with event: Computers that fail this compliance rule report a
     failure severity of Critical for Configuration Manager reports. The Mac
     client computer also logs this severity level.

For a rule type of Existential, specify the following information:

  Choose either:

     The setting must exist on client devices

     The setting must not exist on client devices

  Noncompliance severity for reports: Specify the severity level that is
  reported if this compliance rule fails. The available severity levels are:

     None: Computers that fail this compliance rule don't report a failure
     severity for Configuration Manager reports.

     Information: Computers that fail this compliance rule report a failure
     severity of Information for Configuration Manager reports.

     Warning: Computers that fail this compliance rule report a failure
     severity of Warning for Configuration Manager reports.

     Critical: Computers that fail this compliance rule report a failure severity
     of Critical for Configuration Manager reports.

     Critical with event: Computers that fail this compliance rule report a
     failure severity of Critical for Configuration Manager reports. The Mac
     client computer also logs this severity level.

  ７ Note

  The options shown might vary, depending on the setting type you are
  configuring a rule for.

<!-- p.35 -->

 15. Select OK to close the Create Rule dialog box.

 16. On the Summary page, confirm the settings for the new configuration item. Then,
     complete the wizard.

See the new configuration item in the Configuration Items node of the Assets and
Compliance workspace.

If you now want to add this configuration item to a configuration baseline, see How to
create configuration baselines.

Next steps
Configuration items for devices managed with the Configuration Manager client

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.36 -->

Create custom configuration items for
Windows desktop and server computers
managed with the Configuration
Manager client
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the Configuration Manager custom Windows Desktops and Servers configuration
item to manage settings for Windows computers and servers that are managed by the
Configuration Manager client.

Start the wizard
   1. In the Configuration Manager console, go to the Assets and Compliance
      workspace, expand Compliance Settings, and select the Configuration Items
      node.

   2. On the Home tab of the ribbon, in the Create group, select Create Configuration
      Item.

   3. On the General page of the Create Configuration Item Wizard, specify a name,
      and optional description for the configuration item.

   4. Under Specify the type of configuration item that you want to create, select
      Windows Desktops and Servers (custom).

              If you want to supply detection method settings that check for the existence
              of an application, select This configuration file contains application settings.

   5. To help you search and filter configuration items in the Configuration Manager
      console, select Categories to create and assign categories.

Detection methods
Use this procedure to provide detection method information for the configuration item.

  ７ Note

<!-- p.37 -->

  This information only applies if you select This configuration item contains
  application settings on the General page of the wizard.

A detection method in Configuration Manager contains rules that are used to detect
whether an application is installed on a computer. This detection occurs before the
client assesses its compliance for the configuration item. To detect whether an
application is installed, you can detect the presence of a Windows Installer file for the
application, use a custom script, or select Always assume application is installed to
assess the configuration item for compliance regardless of whether the application is
installed.

To detect an application installation by using the
Windows Installer file
   1. On the Detection Methods page of the Create Configuration Item Wizard, select
      the option to Use Windows Installer detection.

   2. Select Open, browse to the Windows Installer (.msi) file that you want to detect,
      and then select Open.

   3. The Version field automatically populates with the version number of the Windows
      Installer file. If the displayed value is incorrect, enter a new version number here.

   4. If you want to detect each user profile on the computer, select This application is
      installed for one or more users.

To detect a specific application and deployment type
   1. On the Detection Methods page of the Create Configuration Item Wizard, select
      to Detect a specific application and deployment type. Choose Select.

   2. In the Specify Application dialog box, select the application and an associated
      deployment type that you want to detect.

To detect an application installation by using a custom
script
When a Windows PowerShell script runs as a detection method, the Configuration
Manager client calls PowerShell with the -NoProfile parameter. This option starts
PowerShell without profiles. A PowerShell profile is a script that runs when PowerShell
starts.

<!-- p.38 -->

   1. On the Detection Methods page of the Create Configuration Item Wizard, select
     the option to Use a custom script to detect this application.

   2. In the list, select the language of the script. Choose from the following formats:

           VBScript

           JScript

           PowerShell

   3. Select Open, browse to the script that you want to use, and then select Open.

       ） Important

       When using a signed PowerShell script, ensure you select Open. You can't use
       copy and paste for a signed script.

Specify supported platforms
On the Supported Platforms page of the Create Configuration Item Wizard, select the
Windows versions on which you want the configuration item to be assessed for
compliance, or choose Select all.

You can also Specify the version of Windows manually. Select Add and specify each
part of the Windows build number.

  ７ Note

  When specifying Windows Server 2016, the selection for All Windows Server 2016
  and higher 64-bit) also includes Windows Server 2019. To specify Windows Server

  2016 only, use the option to Specify the version of Windows manually.

Configure settings
Use this procedure to configure the settings in the configuration item.

Settings represent the business or technical conditions that are used to assess
compliance on client devices. You can configure a new setting or browse to an existing
setting on a reference computer.

   1. On the Settings page of the Create Configuration Item Wizard, select New.

<!-- p.39 -->

 2. On the General tab of the Create Setting dialog box, provide the following
   information:

         Name: Enter a unique name for the setting. You can use a maximum of 256
         characters.

         Description: Enter a description for the setting. You can use a maximum of
         256 characters.

         Setting type: In the list, choose and configure one of the following setting
         types to use for this setting:
            Active Directory query
            Assembly
            File system
            IIS metabase
            Registry key
            Registry value
            Script
            SQL query
            WQL query
            XPath query

         Data type: Choose the format in which the condition returns the data before
         it's used to assess the setting. The Data type list isn't displayed for all setting
         types.

            Tip

           The Floating point data type supports only three digits after the decimal
           point.

 3. Configure additional details about this setting under the Setting type list. The
   items you can configure vary depending on the setting type you've selected.

 4. Select OK to save the setting and close the Create Setting dialog box.

Active Directory query
   LDAP prefix: Specify a valid prefix to the Active Directory Domain Services query to
   assess compliance on client computers. To do a global catalog search, use either
   LDAP:// or GC:// .

<!-- p.40 -->

     Distinguished Name (DN): Specify the distinguished name of the Active Directory
     Domain Services object that is assessed for compliance on client computers.

     Search filter: Specify an optional LDAP filter to refine the results from the Active
     Directory Domain Services query to assess compliance on client computers. To
     return all results from the query, enter (objectclass=*) .

     Search scope: Specify the search scope in Active Directory Domain Services

        Base: Queries only the specified object

        One Level: This option isn't used in this version of Configuration Manager

        Subtree: Queries the specified object and its complete subtree in the directory

     Property: Specify the property of the Active Directory Domain Services object
     that's used to assess compliance on client computers.

     For example, if you want to query the Active Directory property that stores the
     number of times a user incorrectly enters a password, enter badPwdCount in this
     field.

     Query: Displays the query constructed from the entries in LDAP prefix,
     Distinguished name (DN), Search Filter (if specified), and Property.

Assembly
An assembly is a piece of code that can be shared between applications. Assemblies can
have the file name extension .dll or .exe. The global assembly cache is the folder
%SystemRoot%\Assembly on client computers. This cache is where Windows stores all

shared assemblies.

     Assembly name: Specifies the name of the assembly object that you want to
     search for. The name can't be the same as other assembly objects of the same
     type. First register it in the global assembly cache. The assembly name can be up
     to 256 characters long.

File system
     Type: In the list, select whether you want to search for a File or a Folder.

     Path: Specify the path of the specified file or folder on client computers. You can
     specify system environment variables and the %USERPROFILE% environment variable
     in the path.
