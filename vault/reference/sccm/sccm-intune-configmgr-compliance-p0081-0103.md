---
title: "Device compliance documentation — pages 81-103"
type: reference
domain: sccm
slug: sccm-intune-configmgr-compliance-p0081-0103
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-compliance-p0081-0103
family: sccm
documentKind: "doc"
abstract: "6. Complete the wizard, then deploy the policy. Deploy the OneDrive for Business Profile 1. In the Configuration Manager console, go to the Assets and Compliance workspace, expand Compliance Settings, and select the OneDrive for Business Profiles node. 2. Select the profile, the"
---

# Device compliance documentation — pages 81-103

<!-- p.81 -->

 6. Complete the wizard, then deploy the policy.

Deploy the OneDrive for Business Profile
 1. In the Configuration Manager console, go to the Assets and Compliance
   workspace, expand Compliance Settings, and select the OneDrive for Business
   Profiles node.

 2. Select the profile, then select Deploy in the ribbon.

 3. Specify the following settings for your deployment:

    a. Collection: Click Browse..., then select the collection for which you want to
      deploy the profile.

   b. Generate an alert:

            When compliance is below: Minimum percentage of client compliance to
            maintain otherwise an alert is generated.
            Date and time: The date alerts first start being generated based on profile
            compliance.

<!-- p.82 -->

          Generate System Center Operations Manager alert: Send a compliance
          alert to System Center Operations Manager.

   c. Schedule:

          Simple schedule: By default, this setting uses a simple schedule to start
          the compliance evaluation every seven days.
          Custom schedule: Define when to run the compliance evaluation. The start
          time is based on the local time for the computer that runs the
          Configuration Manager console at the time you create the schedule or you
          can use UTC.

4. Click OK to deploy the OneDrive for Business profile.

<!-- p.83 -->

Next steps
Create remote connection profiles

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.84 -->

Remote connection profiles in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use Configuration Manager remote connection profiles to allow your users to remotely
connect to work computers. These profiles let you deploy Remote Desktop Connection
settings to users in your hierarchy. Users can access any of their primary work computers
through Remote Desktop over a VPN connection.

  ） Important

  When you specify remote connection profile settings with Configuration Manager,
  the client stores the settings in Windows local policy. These settings might override
  Remote Desktop settings that you configure with another application. Additionally,
  if you use Windows Group Policy to configure Remote Desktop settings, the
  settings specified in the Group Policy will override Configuration Manager settings.

Configuration Manager creates a security group on clients, Remote PC Connect. When
you deploy a remote connection profile, the client adds the primary users of the
computer to this group. A local administrator can manually add or remove users to this
group, but Configuration Manager updates the membership when it next evaluates
compliance of the profile.

  ） Important

  If the user device affinity relationship between a user and a device changes,
  Configuration Manager disables the remote connection profile and Windows
  Firewall settings to prevent connections to the computer.

Prerequisites

External dependencies
      If you want to enable users to connect from the internet, install and configure a
      Remote Desktop Gateway server. For more information about how to install and

<!-- p.85 -->

   configure a Remote Desktop Gateway server, see Remote Desktop Services -
   Access from anywhere.

   If clients run a host-based firewall, it must enable the mstsc.exe program. When
   you configure a remote connection profile, enable the setting to Allow Windows
   Firewall exception for connections on Windows domains and on private
   networks. This setting allows Configuration Manager to automatically configure
   Windows Firewall.

      Tip

     Group Policy settings to configure Windows Firewall can override the
     configuration that you set in Configuration Manager. If you use Group Policy
     to configure Windows Firewall, make sure that Group Policy settings don't
     block mstsc.exe.

   If clients run a different host-based firewall, manually configure this firewall
   dependency.

Configuration Manager dependencies
   In order for a user to connect to a work computer, that computer must be a
   primary device of the user. For more information, see Link users and devices with
   user device affinity.

   To manage remote connection profiles, your user account needs specific
   permissions in Configuration Manager. The Compliance Settings Manager built-in
   role includes the permissions required to manage these profiles. For more
   information, see Configure role-based administration.

Security and privacy considerations

Security considerations
   Manually specify user device affinity instead of allowing users to identify their
   primary device. Don't enable usage-based configuration.

      Before you can deploy a remote connection profile, you need to enable the
      option to Allow all primary users of the work computer to remotely connect.
      With this configuration, you should always manually specify user device affinity.
      Don't consider the information that Configuration Manager collects from users

<!-- p.86 -->

        or from the device to be authoritative. If you deploy a profile, and a trusted
        administrative user doesn't specify user device affinity, unauthorized users
        might receive elevated privileges and can remotely connect to computers.

        Configuration Manager collects usage-based information through state
        messages, which is a fast but insecure communication channel. To help mitigate
        this threat, use Server Message Block (SMB) signing or Internet Protocol security
        (IPsec) between client computers and the management point.

     Restrict local administrative rights on the site server computer. A local
     administrator on the site server can manually add members to the Remote PC
     Connect security group that Configuration Manager automatically creates and
     maintains. This action might cause an elevation of privileges because members
     receive Remote Desktop permissions.

Privacy considerations
When a user remotely connects to a work computer, they download a .wsrdp file. This
file contains the device name and the Remote Desktop Gateway Server name. These
values are required to create the Remote Desktop session. The .wsrdp file is downloaded
and automatically saved locally. This file is overwritten the next time that the user runs a
Remote Desktop session.

Create a profile
   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, expand Compliance Settings, and select Remote Connection Profiles.

   2. On the Home tab of the ribbon, in the Create group, select Create Remote
     Connection Profile.

   3. On the General page of the Create Remote Connection Profile Wizard, specify a
     name and optional description for the profile. Both values have a maximum limit of
     256 characters.

   4. On the Profile Settings page, specify the following settings:

           Full name and port of the Remote Desktop Gateway server (optional):
           Specify the name of the Remote Desktop Gateway Server to use for
           connections. This value has the following requirements:
              The server name can't be longer than 256 characters.
              It can contain uppercase, lowercase, and numeric characters.

<!-- p.87 -->

             Aside from periods ( . ) between segments, and a colon ( : ) before the
             port, the only special characters are dash ( – ) and underscore ( _ ).
             Configuration Manager doesn't support the use of an internationalized
             domain name for this value.

          Allow connections only from computers that run Remote Desktop with
          Network Level Authentication: Enabled by default, this setting adds an
          additional level of security for the connection. For more information, see
          Grant Remote Desktop access.

          Enable the following connection settings:

             Allow remote connections to work computers

             Allow all primary users of the work computer to remotely connect

             Allow Windows Firewall exception for connections on Windows domains
             and on private networks

            ） Important

            All three settings must be the same before you can continue.

          Only disable these settings when you deploy a profile to turn off remote
          connections.

  5. Complete the wizard.

The new profile is displayed in the Remote Connection Profiles node in the Assets and
Compliance workspace.

Deploy
  1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, expand Compliance Settings, and select Remote Connection Profiles.

  2. In the Remote Connection Profiles list, select the profile that you want to deploy.
     In the Home tab of the ribbon, in the Deployment group, select Deploy.

  3. In the Deploy Remote Connection Profile window, specify the following
     information:

          Collection: Browse to select the device collection where you want to deploy
          the profile.

<!-- p.88 -->

           Remediate noncompliant rules when supported: Enable this setting to
           automatically remediate the profile settings when they're noncompliant on a
           device. The profile can be non-compliant when it doesn't exist.

           Allow remediation outside the maintenance window: If you configure a
           maintenance window for the collection to which you deploy the profile,
           enable this option to let Configuration Manager remediate it outside the
           maintenance window. For more information, see How to use maintenance
           windows.

           Generate an alert: Enable this option to configure a compliance alert.

           Specify the compliance evaluation schedule for this configuration baseline:
           Specify a simple or custom schedule by which the client evaluates the profile.

   4. Select OK to close the window and create the deployment.

Client evaluation
The client evaluates the profile when a user signs in.

If a device leaves a collection to which you deploy a remote connection profile,
Configuration Manager disables the settings on the device. However, for this process to
occur correctly, you must have already deployed at least one configuration item or
configuration baseline that contains a configuration item from your site.

Conflict resolution
Don't deploy more than one remote connection profile with conflicting settings to the
same device. For example, you deploy two profiles with different settings to the same
collection. You only configure one profile deployment to Remediate noncompliant rules
when supported. This deployment might override the settings in the other profile.
Configuration Manager doesn't support this type of remote connection profile
deployment.

Monitor
In the Configuration Manager console, go to the Monitoring workspace, and select
Deployments. In the Deployments list, select the remote connection profile
deployment.

<!-- p.89 -->

You can review summary information about the compliance of the remote connection
profile deployment on the main page. To view more detailed information, select the
profile deployment. Then on the Home tab of the ribbon, in the Deployment group,
select View Status. This action opens the Deployment Status page.

The Deployment Status page contains the following tabs:

     Compliant: Displays the compliance of the remote connection profile based on the
     number of assets that are affected.

        ） Important

        The client doesn't evaluate a remote connection profile if it's not applicable.
        However, it still reports compliant.

     Error: Displays a list of all errors for the selected remote connection profile
     deployment based on the number of assets that are affected.

     Non-Compliant: Displays a list of all noncompliant rules within the remote
     connection profile based on the number of assets that are affected.

     Unknown: Displays a list of all devices that didn't report compliance for the
     selected remote connection profile deployment, together with the current client
     status of the devices.

On any tab, open a rule to create a temporary subnode under the Users node in the
Assets and Compliance workspace. This subnode contains all devices with the
compliance state of the selected tab.

The Asset Details pane displays the devices with the selected compliance state for this
profile. Open a device in the list to display additional information.

Reports
Configuration Manager includes built-in reports that you can use to monitor
information about remote connection profiles. These reports have the report category
of Compliance and Settings Management.

  ） Important

  Use the wildcard character ( % ) when you use the parameters Device filter and User
  filter in the reports for compliance settings.

<!-- p.90 -->

For more information about how to configure reporting in Configuration Manager, see
Introduction to reporting.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.91 -->

Upgrade Windows devices to a new
edition with Configuration Manager
Article • 10/09/2023

Applies to: Configuration Manager (current branch)

The Edition Upgrade Policy lets you automatically upgrade Windows 11 and Windows
10 devices to a different edition.

The following upgrade paths are supported:

      From Windows 11 Pro to Windows 11 Enterprise
      From Windows 11 Home to Windows 11 Education
      From Windows 11 Pro N to Windows 11 Enterprise N
      From Windows 11 Home N to Windows 11 Education N
      From Windows 10 Pro to Windows 10 Enterprise
      From Windows 10 Home to Windows 10 Education
      From Windows 10 Mobile to Windows 10 Mobile Enterprise

The devices must run the Configuration Manager client software. Devices managed by
on-premises MDM aren't supported.

Before you start
Before you begin to upgrade devices to the latest version, review the following
prerequisites:

      For desktop editions of Windows 11 and Windows 10: A valid product key for the
      new version of Windows on all devices you target with the policy. This product key
      can be a multiple activation key (MAK), or a generic volume licensing key (GVLK). A
      GVLK is also referred to as a key management service (KMS) client setup key. For
      more information, see Plan for volume activation. For a list of KMS client setup
      keys, see Appendix A of the Windows Server activation guide.

      For Windows 10 Mobile: An XML license file from the Microsoft Volume Licensing
      Service Center (VLSC). This file contains the licensing information for the new
      version of Windows on all devices you target with the policy. Download the ISO file
      for Windows 10 Mobile Enterprise, which includes the licensing XML.

      To manage this policy type, you must be in the Configuration Manager Full
      Administrator security role.

<!-- p.92 -->

Configure the policy
 1. In the Configuration Manager console, go to the Assets and Compliance
   workspace, expand Compliance Settings, and select the Windows Edition
   Upgrade node.

 2. On the Home tab of the ribbon, in the Create group, select Create Edition
   Upgrade Policy.

 3. Select Create Policy.

 4. On the General page of the Create Edition Upgrade Policy Wizard, specify the
   following information:

         Name - Enter a name for the edition upgrade policy

         Description (optional) - Optionally, enter a description for the policy that
         helps you identify it in the Configuration Manager console

         SKU to upgrade device to - From the drop-down list, select the target
         edition of Windows 11 and Windows 10 desktop or Windows 10 Mobile

         License information - Select one of the following options:

            Product Key - Enter a valid product key for the target Windows 11 & 10
            desktop edition

              ７ Note

              After you create a policy containing a product key, you can't edit the
              product key later. Configuration Manager obscures the key for
              security reasons. To change the product key, re-enter the entire key.

            License File - Select Browse to choose a valid license file in XML format.
            Configuration Manager uses this license file to upgrade Windows 10
            Mobile devices.

 5. Complete the wizard.

Deploy the policy
 1. In the Configuration Manager console, go to the Assets and Compliance
   workspace, expand Compliance Settings, and select the Windows Edition

<!-- p.93 -->

     Upgrade node.

   2. Select the Windows edition upgrade policy you want to deploy. On the Home tab
     of the ribbon, in the Deployment group, select Deploy.

   3. Choose the device collection to which you want to deploy the policy.

   4. Select the schedule by which the client evaluates the policy.

   5. Complete the wizard.

Next steps
Monitor this deployment from the Deployments node of the Monitoring workspace. If
you see errors indicating an unsuccessful deployment, for example:

     Not applicable for this device
     Data type conversion failed

These errors don't mean that the deployment failed. Verify at the targeted device that
the upgrade ran successfully.

Once the client evaluates the targeted policy, it applies the upgrade within two hours.
Some versions of Windows may require a restart at that time. Make sure you inform any
users to which you deploy the policy, or schedule the policy to run outside of the users'
working hours.

If the following error appears in DcmWmiProvider.log on the client, check that you're
using the proper key for your activation scenario. For more information, see the Before
you start section. If you're using a key management service (KMS) for activation, make
sure to use a KMS client setup key.

Failed to execute CheckApplicabilityMethod with error = 0x80041001

OsEditionUpgradeProvider

See also
     Plan for volume activation

     Windows 10 edition upgrade

     Upgrade Windows 10 editions or switch out of S mode on devices using Microsoft
     Intune

<!-- p.94 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.95 -->

Configure Microsoft Edge Legacy
settings in Configuration Manager
Article • 02/03/2023

  ） Important

  If you're using Microsoft Edge version 77 or later, and are trying to open the
  settings pane, enter edge://settings/profiles in the browser address bar instead
  of search. For more information, see Get to know Microsoft Edge      .

  This article is for IT professionals to manage Microsoft Edge Legacy settings with
  Microsoft Configuration Manager.

Applies to: Configuration Manager (current branch)

For customers who use the Microsoft Edge Legacy web browser on Windows 10 clients,
create a Configuration Manager compliance policy to configure the browser settings.

  ２ Warning

  This feature is deprecated. Support ends for the Microsoft Edge Legacy desktop
  application on March 9, 2021. With the April cumulative update for Windows 10,
  the new Microsoft Edge replaces Microsoft Edge Legacy. For more information, see
  New Microsoft Edge to replace Microsoft Edge Legacy with April’s Windows 10
  Update Tuesday release      .

This policy only applies to clients on Windows 10, version 1703 or later, and Microsoft
Edge Legacy version 45 and earlier.

For more information on managing Microsoft Edge version 77 or later with
Configuration Manager, see Deploy Microsoft Edge, version 77 and later. For more
information on configuring policies for Microsoft Edge version 77 or later, see Microsoft
Edge - Policies.

Policy settings
This policy currently includes the following settings:

<!-- p.96 -->

   Set Microsoft Edge browser as default: configures the Windows 10 default app
   setting for web browser to Microsoft Edge

   Allow address bar drop-down: Requires Windows 10, version 1703 or later. For
   more information, see AllowAddressBarDropdown browser policy.

   Allow sync favorites between Microsoft browsers: Requires Windows 10, version
   1703 or later. For more information, see SyncFavoritesBetweenIEAndMicrosoftEdge
   browser policy.

   Allow clear browsing data on exit: Requires Windows 10, version 1703 or later. For
   more information, see ClearBrowsingDataOnExit browser policy.

   Allow Do Not Track headers: For more information, see AllowDoNotTrack browser
   policy.

   Allow autofill: For more information, see AllowAutofill browser policy.

   Allow cookies: For more information, see AllowCookies browser policy.

   Allow pop-up blocker: For more information, see AllowPopups browser policy.

   Allow search suggestions in address bar: For more information, see
   AllowSearchSuggestionsinAddressBar browser policy.

   Allow send intranet traffic to Internet Explorer: For more information, see
   SendIntranetTraffictoInternetExplorer browser policy.

   Allow password manager: For more information, see AllowPasswordManager
   browser policy.

   Allow Developer Tools: For more information, see AllowDeveloperTools browser
   policy.

   Allow extensions: For more information, see AllowExtensions browser policy.

  Tip

 For more information on using group policy to configure these and other settings,
 see Microsoft Edge Legacy group policies.

Configure Windows Defender SmartScreen settings for
Microsoft Edge Legacy

<!-- p.97 -->

This policy adds three settings for Windows Defender SmartScreen. The policy now
includes the following additional settings on the SmartScreen Settings page:

     Allow SmartScreen: Specifies whether Windows Defender SmartScreen is allowed.
     For more information, see the AllowSmartScreen browser policy.

     Users can override SmartScreen prompt for sites: Specifies whether users can
     override the Windows Defender SmartScreen Filter warnings about potentially
     malicious websites. For more information, see the
     PreventSmartScreenPromptOverride browser policy.

     Users can override SmartScreen prompt for files: Specifies whether users can
     override the Windows Defender SmartScreen Filter warnings about downloading
     unverified files. For more information, see the
     PreventSmartScreenPromptOverrideForFiles browser policy.

Create the browser profile
   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace. Expand Compliance Settings and select the Microsoft Edge Browser
     Profiles node. In the ribbon, select Create Microsoft Edge profile.

   2. Specify a Name for the policy, optionally enter a Description, and select Next.

   3. On the General Settings page, change the value to Configured for the settings to
     include in this policy. To continue the wizard, make sure to configure the setting to
     Set Edge Browser as default.

   4. Configure settings on the SmartScreen Settings page.

   5. On the Supported Platforms page, select the OS versions and architectures to
     which this policy applies.

   6. Complete the wizard.

Deploy the policy
   1. Select your policy, and in the ribbon select Deploy.

   2. Browse to select the user or device collection to which to deploy the policy.

   3. Select additional options as necessary:

      a. Generate alerts when the policy isn't compliant.

<!-- p.98 -->

      b. Set the schedule by which the client evaluates the device's compliance with this
           policy.

   4. Select OK to create the deployment.

Next steps
Like any compliance settings policy, the client remediates the settings on the schedule
you specify. Monitor and report on device compliance in the Configuration Manager
console.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.99 -->

Monitor compliance settings in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you have deployed Configuration Manager configuration baselines to devices in
your hierarchy, you can use one or more of the procedures in this topic to display the
compliance status of the configuration baseline:

  ７ Note

  The validation criteria fields in compliance settings reports (the equivalent on the
  client-side report is Constraints) display the underlying Service Modeling Language
  (SML). This can make it difficult for administrators who have authored the
  configuration item in the Configuration Manager console to understand what the
  validation criteria is if they do not have knowledge of SML. In this case, use the
  Monitoring workspace in the Configuration Manager console to view the
  properties of the configuration item and its validation criteria.

View compliance results in the Configuration
Manager console
Use this procedure to view details about the compliance of deployed configuration
baselines in the Configuration Manager console.

View compliance results in the Configuration Manager
console
   1. In the Configuration Manager console, click Monitoring > Deployments.

   2. In the Deployments list, select the configuration baseline deployment for which
      you want to review compliance information.

   3. You can review summary information about the compliance of the configuration
      baseline deployment on the main page. To view more detailed information, select
      the configuration baseline deployment, and then on the Home tab, in the
      Deployment group, click View Status to open the Deployment Status page.

<!-- p.100 -->

  The Deployment Status page contains the following tabs:

       Compliant: Displays the compliance of the configuration baseline based on
       the number of assets affected. You can click a rule to create a temporary
       node under the Users or Devices node that are in the Assets and Compliance
       workspace, which contains all users or devices that are compliant with this
       rule. The Asset Details pane displays the users or devices that are compliant
       with the configuration baseline. Double-click a user or device in the list to
       display additional information.

         ） Important

         A configuration item rule is not evaluated if it is not detected or not
         applicable on a client device; however, the rule is returned as compliant.

       Error: Displays a list of all errors for the selected configuration baseline
       deployment based on number of assets affected. You can click a rule to
       create a temporary node under the Users or Devices node of the Assets and
       Compliance workspace, which contains all users or devices that generated
       errors with this rule. When you select a user or device, the Asset Details pane
       displays the users or devices that are affected by the selected issue. Double-
       click a user or device in the list to display additional information about the
       issue.

       Non-Compliant: Displays a list of all noncompliant rules within the
       configuration baseline based on number of assets affected. You can click a
       rule to create a temporary node under the Users or Devices node of the
       Assets and Compliance workspace, which contains all users or devices that
       are not compliant with this rule. When you select a user or device, the Asset
       Details pane displays the users or devices that are affected by the selected
       issue. Double-click a user or device in the list to display further information
       about the issue.

       Unknown: Displays a list of all users and devices that did not report
       compliance for the selected configuration baseline deployment together with
       the current client status of devices.

4. On the Deployment Status page, you can review detailed information about the
  compliance of the deployed configuration baseline. A temporary node is created
  under the Deployments node that helps you find this information again quickly.

<!-- p.101 -->

View compliance results by using reports
Compliance settings in Configuration Manager includes a number of built-in reports
that let you monitor information about configuration items, configuration baselines, and
deployments. These reports have the report category of Compliance and Settings
Management.

  ） Important

  You must use a wildcard (%) character when you use the parameters Device filter
  and User filter in the compliance settings reports.

For more information about how to configure Reporting in Configuration Manager, see
Introduction to reporting.

View compliance results on a Configuration
Manager Windows client computer

  ７ Note

  You cannot view information on the Configuration Manager Windows client if you
  are logged on with a domain Guest account.

   1. Navigate to Configuration Manager in Control Panel of the client computer, and
     double-click it to open its properties.

   2. Click the Configurations tab, and view the list of deployed configuration baselines.

   3. View the Compliance State for each configuration baseline:

       ） Important

       The evaluation results are cached on the client for 15 minutes. If you initiate a
       re-evaluation within the 15 minute period, the compliance results are returned
       from this cache rather than a new evaluation. Therefore, if you make a change
       on the client that might affect the compliance evaluation results, wait until the
       15 minutes have elapsed before initiating a re-evaluation.

<!-- p.102 -->

             Compliant: The client computer is in compliance with the evaluated
             configuration baseline.

             Non-Compliant: The client computer is out of compliance with the evaluated
             configuration baseline.

             Unknown: The client computer has not yet evaluated the configuration
             baseline. If you want to initiate evaluation outside the compliance evaluation
             schedule, select the configuration baselines to evaluate, and then click
             Evaluate.

               ７ Note

               If you have local administrator credentials on the client computer, you
               can view details of each evaluated configuration baseline to determine
               which configuration item is reporting a noncompliant status. To do this,
               select the configuration baseline, and then click View Report.

   4. Click OK.

Create collections based on configuration
baseline compliance
Use the following procedure to create a Configuration Manager collection based on
devices with a specified compliance. You can create collections based on the following
compliance states:

     Compliant

     Error

     Non-compliant

     Unknown

   1. In the Configuration Manager console, click Assets and Compliance > Compliance
     Settings > Configuration Baselines.

   2. In the Configuration Baselines list, select the configuration baseline from which
     you want to create a collection.

   3. In the Deployment tab, in the Deployment Group, click Create New Collection
     and then, in the drop-down list, select the compliance level for which you want to

<!-- p.103 -->

     create a collection.

   4. The Create User Collection Wizard or the Create Device Collection Wizard opens,
     depending on whether the configuration item is deployed to users or devices. The
     wizard is automatically populated with the correct values to create the collection;
     however, you can edit these values.

   5. After you complete the wizard, the collection displays in the User Collections or
     the Device Collections node in the Assets and Compliance workspace.

Feedback
Was this page helpful?      Yes    No

Provide product feedback
