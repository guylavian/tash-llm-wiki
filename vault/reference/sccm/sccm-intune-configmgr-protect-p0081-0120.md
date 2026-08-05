---
title: "Protect data and infrastructure documentation — pages 81-120"
type: reference
domain: sccm
slug: sccm-intune-configmgr-protect-p0081-0120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-protect-p0081-0120
family: sccm
documentKind: "doc"
abstract: "Create and deploy Windows Firewall policies for Endpoint Protection in Configuration Manager Applies to: Configuration Manager (current branch) Firewall policies for Endpoint Protection in Configuration Manager let you perform basic Windows Firewall configuration and maintenance"
---

# Protect data and infrastructure documentation — pages 81-120

<!-- p.81 -->

Create and deploy Windows Firewall
policies for Endpoint Protection in
Configuration Manager
Applies to: Configuration Manager (current branch)

Firewall policies for Endpoint Protection in Configuration Manager let you perform basic
Windows Firewall configuration and maintenance tasks on client computers in your hierarchy.

You can use Windows Firewall policies to perform the following tasks:

     Control whether Windows Firewall is turned on or off.
     Control whether incoming connections are allowed to client computers.
     Control whether users are notified when Windows Firewall blocks a new program.

Prerequisites
     A site system server with the Endpoint Protection role installed.
     An Endpoint Protection Client Setting with Manage Endpoint Protection client on client
     computers set to Yes.

  ７ Note

  It is not necessary to have Install Endpoint Protection client enabled in the client setting.

Create the policy
   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, expand Endpoint Protection, and then click
     Windows Firewall Policies.

   3. On the Home tab, in the Create group, click Create Windows Firewall Policy.

   4. On the General page of the Create Windows Firewall Policy Wizard, specify a name and
     an optional description for this firewall policy, and then click Next.

   5. On the Profile Settings page of the wizard, configure the following settings for each
     network profile:

           Enable Windows Firewall

<!-- p.82 -->

             If Enable Windows Firewall is not enabled, the other settings on this page of the
             wizard are unavailable.

             Block all incoming connections, including those in the list of allowed programs

             Notify the user when Windows Firewall blocks a new program

  6. On the Summary page of the wizard, review the actions to be taken, and then complete
     the wizard.

  7. Verify that the new Windows Firewall policy is displayed in the Windows Firewall Policies
     list.

To deploy a Windows Firewall policy
  1. In the Configuration Manager console, click Assets and Compliance.

  2. In the Assets and Compliance workspace, expand Endpoint Protection, and then click
     Windows Firewall Policies.

  3. In the Windows Firewall Policies list, select the Windows Firewall policy that you want to
     deploy.

  4. On the Home tab, in the Deployment group, click Deploy.

  5. In the Deploy Windows Firewall Policy dialog box, specify the collection to which you
     want to assign this Windows Firewall policy, and specify an assignment schedule. The
     Windows Firewall policy evaluates for compliance by using this schedule and the
     Windows Firewall settings on clients to reconfigure to match the Windows Firewall policy.

  6. Click OK to close the Deploy Windows Firewall Policy dialog box and to deploy the
     Windows Firewall policy.

        ） Important

        When you deploy a Windows Firewall policy to a collection, this policy is applied to
        computers in a random order over a 2 hour period to avoid flooding the network.

Last updated on 03/19/2026

<!-- p.83 -->

Microsoft Defender for Endpoint
Article • 12/16/2024

Applies to: Configuration Manager (current branch)

Endpoint Protection can help manage and monitor Microsoft Defender for Endpoint.
Microsoft Defender for Endpoint helps enterprises detect, investigate, and respond to
advanced attacks on their networks. Configuration Manager policies can help you
onboard and monitor Windows 10 or later clients.

Microsoft Defender for Endpoint's cloud-based portal is Microsoft Defender Security
Center    . By adding and deploying a client onboarding configuration file, Configuration
Manager can monitor deployment status and Microsoft Defender for Endpoint agent
health. Microsoft Defender for Endpoint is supported on PCs running the Configuration
Manager client or managed by Microsoft Intune.

Prerequisites
      Subscription to Microsoft Defender for Endpoint
      Clients computers running the Configuration Manager client
      Clients using an OS listed in the supported client operating systems section below.
      Your administrative user account needs the Endpoint Protection Manager security
      role.

Supported client operating systems
You can onboard the following operating systems using Configuration Manager:

      Windows 11
      Windows 10, version 1709 or newer
      Windows Server 2025
      Windows Server 2022
      Windows Server 2019
      Windows Server Semi-Annual Channel (SAC), version 1803 or newer
      Windows Server 2016

  ） Important

  Operating systems that have reached the end of their product lifecycle aren't
  typically supported for onboarding unless they have been enrolled into the

<!-- p.84 -->

  Extended Security Updates (ESU program). For more information about supported
  operating systems and capabilities with Microsoft Defender for Endpoint, see
  Minimum requirements for Microsoft Defender for Endpoint.

Instructions to Onboarding to Microsoft Defender for Endpoint with Configuration
Manager 2207 and later versions

Instructions to Updating onboarding information for Microsoft Defender for Endpoint
devices with Configuration Manager

Onboarding to Microsoft Defender for
Endpoint with Configuration Manager 2207
and later versions
Different operating systems have different needs for onboarding to Microsoft Defender
for Endpoint. Up-level devices, such as Windows Server version 1803, need the
onboarding configuration file. Starting Current Branch 2207, For down-level server
operating system devices, you can choose between Microsoft Defender for Endpoint
(MDE) Client (recommended) or Microsoft Monitoring Agent (MMA) (legacy) in the
Client Settings. For Windows 8.1 devices, you need to use Microsoft Monitoring Agent
(MMA) (legacy) in the Client Settings.

<!-- p.85 -->

                                                                                

If you choose to use MMA, you need the Workspace key and Workspace ID to onboard.
Configuration Manager also installs the Microsoft Monitoring Agent (MMA) when
needed by onboarded devices but it doesn't update the agent automatically.

Up-level operating systems include:

     Windows 10, version 1607 and later
     Windows 11
     Windows Server Semi-Annual Channel (SAC), version 1803 or later
     Windows Server 2019
     Windows Server 2022
     Windows Server 2025

Down-level operating systems that support MDE Client include:

     Windows Server 2016

  ７ Note

<!-- p.86 -->

  Currently, the modern, unified Microsoft Defender for Endpoint for Windows
  Server 2012 R2 & 2016     is generally available. Configuration Manager version
  2107 with the update rollup supports configuration using Endpoint Protection
  policies, including those policies created in the Microsoft Intune admin center using
  tenant attach. Configuration Manager version 2207 now supports automatic
  deployment of MDE Client, if you choose to use through Client Settings. For older
  supported versions, see Server migration scenarios.

When you onboard devices to Microsoft Defender for Endpoint with Configuration
Manager, you deploy the Defender policy to a target collection or multiple collections.
Sometimes the target collection contains devices running any number of the supported
operating systems. The instructions for onboarding these devices vary based on if you're
targeting a collection containing devices with operating systems that are only up-level
and devices that support MDE Client or if the collection also includes down-level clients
that require MMA.

     If your collection contains only up-level devices and/or down-level server
     operating system devices that require MDE Client (based on the client settings),
     then you can use the onboarding instructions using Microsoft Defender for
     Endpoint Client (recommended).
     If your target collection contains down-level server operating system devices that
     require MMA (based on the client settings) or Windows 8.1 devices, then use the
     instructions to onboard devices using Microsoft Monitoring Agent.

  ２ Warning

  If your target collection contains down-level devices that require MMA, and you
  use the instructions for onboarding using MDE Client, then the down-level devices
  won't be onboarded. The optional Workspace key and Workspace ID fields are
  used for onboarding down-level devices that require MMA, but if they aren't
  included then the policy will fail on down-level clients that require MMA.

Onboard devices using MDE Client to Microsoft Defender
for Endpoint (recommended)
Up-level clients require an onboarding configuration file for onboarding to Microsoft
Defender for Endpoint. Up-level operating systems include:

     Windows 11
     Windows 10, version 1607 and later

<!-- p.87 -->

     Windows Server Semi-Annual Channel (SAC), version 1803 and later
     Windows Server 2019
     Windows Server 2022
     Windows Server 2025

Down-level operating systems that support MDE Client include:

     Windows Server 2016

Prerequisites

Prerequisites for Windows Server 2012 R2

If you have fully updated your machines with the latest monthly rollup    package, there
are no additional prerequisites.

The installer package will check if the following components have already been installed
via an update:

     Update for customer experience and diagnostic telemetry
     Update for Universal C Runtime in Windows

Prerequisites for Windows Server 2016

     The Servicing Stack Update (SSU) from September 14, 2021 or later must be
     installed.
     The Latest Cumulative Update (LCU) from September 20, 2018 or later must be
     installed. It is recommended to install the latest available SSU and LCU on the
     server. - The Microsoft Defender Antivirus feature must be enabled/installed and
     up to date. You can download and install the latest platform version using
     Windows Update. Alternatively, download the update package manually from the
     Microsoft Update Catalog      or from MMPC      .

Get an onboarding configuration file for up-level devices
   1. Go to the Microsoft Defender Security Center       and sign in.
   2. Select Settings, then select Onboarding under the Endpoint heading.
   3. For the operating system, select Windows 10 and 11.
   4. Choose Microsoft Endpoint Configuration Manager current branch and later for
     the deployment method.
   5. Select Download package.
   6. Download the compressed archive (.zip) file and extract the contents.

<!-- p.88 -->

      ７ Note

      The steps have you download the onboarding file for Windows 10 and 11 but
      this file is also used for up-level Server operating systems.

 ） Important

      The Microsoft Defender for Endpoint configuration file contains sensitive
      information which should be kept secure.
      If your target collection contains down-level devices that require MMA, and
      you use the instructions for onboarding using MDE Client, then the down-
      level devices won't be onboarded. The optional Workspace key and
      Workspace ID fields are used for onboarding down-level devices, but if they
      aren't included then the policy will fail on down-level clients.

Onboard the up-level devices
  1. In the Configuration Manager console, navigate to Administration > Client
    Settings.
  2. Create custom Client Device Settings or go to the properties of the required client
    setting and select Endpoint Protection
  3. For Microsoft Defender for Endpoint Client on Windows Server 2012 R2 and
    Windows Server 2016 setting, The default value is set as Microsoft Monitoring

<!-- p.89 -->

   Agent (legacy) which needs to be changed to MDE Client (recommended).

                                                                                    

 4. In the Configuration Manager console, navigate to Assets and Compliance >
   Endpoint Protection > Microsoft Defender ATP Policies and select Create
   Microsoft Defender ATP Policy. The policy wizard opens.
 5. Type the Name and Description for the Microsoft Defender for Endpoint policy
   and select Onboarding.
 6. Browse to the configuration file you extracted from the downloaded .zip file.
 7. Specify the file samples that are collected and shared from managed devices for
   analysis.

        None
        All file types

 8. Review the summary and complete the wizard.
 9. Right-click on the policy you created, then select Deploy to target the Microsoft
   Defender for Endpoint policy to clients.

Onboard devices with MDE Client and MMA to Microsoft
Defender for Endpoint

<!-- p.90 -->

You can onboard devices running any of the supported operating systems to Microsoft
Defender for Endpoint by providing the configuration file, Workspace key, and
Workspace ID to Configuration Manager.

Get the configuration file, workspace ID, and workspace key
  1. Go to the Microsoft Defender for Endpoint online service   and sign in.

  2. Select Settings, then select Onboarding under the Endpoints heading.

  3. For the operating system, select Windows 10 and 11.

  4. Choose Microsoft Endpoint Configuration Manager current branch and later for
     the deployment method.

  5. Select Download package.

                                                                                

  6. Download the compressed archive (.zip) file and extract the contents.

  7. Select Settings, then select Onboarding under the Device management heading.

  8. For the operating system, select either Windows 7 SP1 and 8.1 or Windows Server
     2008 R2 Sp1, 2012 R2 and 2016 from the list.

          The Workspace key and Workspace ID will be the same regardless of which
          of these options you choose.

  9. Copy the values for the Workspace key and Workspace ID from the Configure
     connection section.

       ） Important

<!-- p.91 -->

      The Microsoft Defender for Endpoint configuration file contains sensitive
      information which should be kept secure.

Onboard the devices

  1. In the Configuration Manager console, navigate to Administration > Client
    Settings.

  2. Create custom Client Device Settings or go to the properties of the required client
    setting and select Endpoint Protection

  3. For Microsoft Defender for Endpoint Client on Windows Server 2012 R2 and
    Windows Server 2016 setting, ensure the value is set as Microsoft Monitoring
    Agent (legacy).

  4. In the Configuration Manager console, navigate to Assets and Compliance >
    Endpoint Protection > Microsoft Defender ATP Policies.

  5. Select Create Microsoft Defender ATP Policy to open the policy wizard.

  6. Type the Name and Description for the Microsoft Defender for Endpoint policy
    and select Onboarding.

  7. Browse to the configuration file you extracted from the downloaded .zip file.

  8. Supply the Workspace key and Workspace ID then select Next.

         Verify that the Workspace key and Workspace ID are in the correct fields. The
         order in the console may vary from the order in Microsoft Defender for

<!-- p.92 -->

         Endpoint online service.

                                                                                  

 9. Specify the file samples that are collected and shared from managed devices for
   analysis.

         None
         All file types

10. Review the summary and complete the wizard.

11. Right-click on the policy you created, then select Deploy to target the Microsoft
   Defender for Endpoint policy to clients.

Monitor
 1. In the Configuration Manager console, navigate Monitoring > Security and then
   select Microsoft Defender ATP.

 2. Review the Microsoft Defender for Endpoint dashboard.

         Microsoft Defender ATP Agent Onboarding Status: The number and
         percentage of eligible managed client computers with active Microsoft
         Defender for Endpoint policy onboarded

<!-- p.93 -->

          Microsoft Defender ATP Agent Health: Percentage of computer clients
          reporting status for their Microsoft Defender for Endpoint agent

              Healthy - Working properly

              Inactive - No data sent to service during time period

              Agent state - The system service for the agent in Windows isn't running

              Not onboarded - Policy was applied but the agent hasn't reported policy
              onboard

Create an offboarding configuration file
   1. Sign in to the Microsoft Defender Security Center   .

   2. Select Settings, then select Offboarding under the Endpoint heading.

   3. Select Windows 10 and 11 for the operating system and Microsoft Endpoint
     Configuration Manager current branch and later for the deployment method.

          Using the Windows 10 and 11 option ensures that all devices in the collection
          are off boarded and the MMA is uninstalled when needed.

   4. Download the compressed archive (.zip) file and extract the contents. Offboarding
     files are valid for 30 days.

   5. In the Configuration Manager console, navigate to Assets and Compliance >
     Endpoint Protection > Microsoft Defender ATP Policies and select Create
     Microsoft Defender ATP Policy. The policy wizard opens.

   6. Type the Name and Description for the Microsoft Defender for Endpoint policy
     and select Offboarding.

   7. Browse to the configuration file you extracted from the downloaded .zip file.

   8. Review the summary and complete the wizard.

Select Deploy to target the Microsoft Defender for Endpoint policy to clients.

  ） Important

  The Microsoft Defender for Endpoint configuration files contains sensitive
  information which should be kept secure.

<!-- p.94 -->

Updating the onboarding information for
existing devices
Organizations may need to update the onboarding information on a device via
Microsoft Configuration Manager.

This can be necessary due to a change in the onboarding payload for Microsoft
Defender for Endpoint, or when directed by Microsoft support.

Updating the onboarding information will direct the device to start utilizing the new
onboarding payload at the next Restart.

This process compromises of actions to update the existing onboarding policy, and
executing a one time action on all existing devices to update the onboarding payload.
Utilize the Group Policy onboarding script to perform a one time uplift of devices from
the old payload to the new payload.

  ７ Note

  This information will not necessarily move a device between tenants without fully
  offboarding the device from the original tenant. For options migrating devices
  between Microsoft Defender for Endpoint organizations, engage Microsoft
  Support.

Validate the new onboarding payload
   1. Download the Group Policy onboarding package from the Microsoft Defender for
     Endpoint portal.

   2. Create a collection for validation of the new onboarding payload

   3. Exclude this collection from the existing Microsoft Defender for Endpoint
     collection targeted with the onboarding payload.

   4. Deploy the Group Policy onboarding script to the test collection.

   5. Validate the devices are utilizing the new onboarding payload.

Migrate to the new onboarding payload
   1. Download the Microsoft Configuration Manager onboarding package from the
     Microsoft Defender for Endpoint portal.

<!-- p.95 -->

   2. Update the existing Microsoft Defender for Endpoint onboarding policy with the
     new onboarding payload.

   3. Deploy the script from Validate the new onboarding payload to the existing target
     collection for the Microsoft Defender for Endpoint onboarding policy.

   4. Validate the devices are utilizing the new onboarding payload and successfully
     consuming the payload from the script

  ７ Note

  Once all devices are migrated you can remove the script and validation collections
  from your environment, using the onboarding policy moving forward.

Next steps
     Microsoft Defender for Endpoint

     Troubleshoot Microsoft Defender for Endpoint onboarding issues

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.96 -->

Create and deploy an Exploit Guard
policy
Article • 04/19/2024

Applies to: Configuration Manager (current branch)

You can configure and deploy Configuration Manager policies that manage all four
components of Windows Defender Exploit Guard. These components include:

      Attack Surface Reduction
      Controlled folder access
      Exploit protection
      Network protection

Compliance data for Exploit Guard policy deployment is available from within the
Configuration Manager console.

  ７ Note

  Configuration Manager doesn't enable this optional feature by default. You must
  enable this feature before using it. For more information, see Enable optional
  features from updates.

Prerequisites
Managed devices must run Windows 10 1709 or later; the minimum Windows Server
build is version 1809 or later until Server 2019 only. The following requirements must
also be satisfied, depending on the components and rules configured:

                                                                              ﾉ   Expand table

 Exploit Guard              Additional prerequisites
 component

 Attack Surface             Devices must have Microsoft Defender for Endpoint always-on
 Reduction                  protection enabled.

 Controlled folder access   Devices must have Microsoft Defender for Endpoint always-on
                            protection enabled.

 Exploit protection         None

<!-- p.97 -->

Exploit Guard           Additional prerequisites
component

Network protection      Devices must have Microsoft Defender for Endpoint always-on
                        protection enabled.

Create an Exploit Guard policy
 1. In the Configuration Manager console, go to Assets and compliance > Endpoint
    Protection, and then click Windows Defender Exploit Guard.

 2. On the Home tab, in the Create group, click Create Exploit Policy.

 3. On the General page of the Create Configuration Item Wizard, specify a name,
    and optional description for the configuration item.

 4. Next, select the Exploit Guard components you want to manage with this policy.
    For each component you select, you can then configure additional details.

         Attack Surface Reduction: Configure the Office threat, scripting threats, and
         email threats you want to block or audit. You can also exclude specific files or
         folders from this rule.
         Controlled folder access: Configure blocking or auditing, and then add Apps
         that can bypass this policy. You can also specify additional folders that are
         not protected by default.
         Exploit protection: Specify an XML file that contains settings for mitigating
         exploits of system processes and apps. You can export these settings from
         the Windows Defender Security Center app on a Windows 10 or later device.
         Network protection: Set network protection to block or audit access to
         suspicious domains.

 5. Complete the wizard to create the policy, which you can later deploy to devices.

      ２ Warning

      The XML file for exploit protection should be kept secure when transferring it
      between machines. The file should be deleted after import or kept in a secure
      location.

Deploy an Exploit Guard policy

<!-- p.98 -->

After you create Exploit Guard policies, use the Deploy Exploit Guard Policy wizard to
deploy them. To do so, open the Configuration Manager console to Assets and
compliance > Endpoint Protection, and then click Deploy Exploit Guard Policy.

  ） Important

  Once you deploy an Exploit Guard policy, such as Attack Surface Reduction or
  Controlled folder access, the Exploit Guard settings will not removed from the
  clients if you remove the deployment. Delete not supported is recorded in the
  client's ExploitGuardHandler.log if you remove the client's Exploit Guard
  deployment. The following PowerShell script can be run under SYSTEM context to
  remove these settings:

    PowerShell

     $defenderObject = Get-WmiObject -Namespace "root/cimv2/mdm/dmmap" -
     Class "MDM_Policy_Config01_Defender02" -Filter "InstanceID='Defender'
     and ParentID='./Vendor/MSFT/Policy/Config'"
     $defenderObject.AttackSurfaceReductionRules = $null
     $defenderObject.AttackSurfaceReductionOnlyExclusions = $null
     $defenderObject.EnableControlledFolderAccess = $null
     $defenderObject.ControlledFolderAccessAllowedApplications = $null
     $defenderObject.ControlledFolderAccessProtectedFolders = $null
     $defenderObject.EnableNetworkProtection = $null
     $defenderObject.Put()

     $exploitGuardObject = Get-WmiObject -Namespace "root/cimv2/mdm/dmmap" -
     Class "MDM_Policy_Config01_ExploitGuard02" -Filter
     "InstanceID='ExploitGuard' and ParentID='./Vendor/MSFT/Policy/Config'"
     $exploitGuardObject.ExploitProtectionSettings = $null
     $exploitGuardObject.Put()

Windows Defender Exploit Guard policy
settings

Attack Surface Reduction policies and options
Attack Surface Reduction can reduce the attack surface of your applications with
intelligent rules that stop the vectors used by Office, script, and mail-based malware.
Learn more about Attack Surface Reduction and the Event IDs used for it.

     Files and Folders to exclude from Attack Surface Reduction rules - Click on Set
     and specify any files or folders to exclude.

<!-- p.99 -->

Email Threats:
  Block executable content from email client and webmail.
     Not configured
     Block
     Audit

Office Threats:
  Block Office application from creating child processes.
     Not configured
     Block
     Audit
  Block Office applications from creating executable content.
     Not configured
     Block
     Audit
  Block Office applications from injecting code into other processes.
     Not configured
     Block
     Audit
  Block Win32 API calls from Office macros.
     Not configured
     Block
     Audit

Scripting Threats:
  Block JavaScript or VBScript from launching downloaded executable content.
     Not configured
     Block
     Audit
  Block execution of potentially obfuscated scripts.
     Not Configured
     Block
     Audit

Ransomware threats: (starting in Configuration Manager version 1802)
  Use advanced protection against ransomware.
     Not configured
     Block
     Audit

Operating system threats: (starting in Configuration Manager version 1802)
  Block credential stealing from the Windows local security authority subsystem.

<!-- p.100 -->

              Not configured
              Block
              Audit
        Block executable files from running unless they meet a prevalence, age, or
        trusted list criteria.
              Not configured
              Block
              Audit

     External device threats: (starting in Configuration Manager version 1802)
        Block untrusted and unsigned processes that run from USB.
              Not configured
              Block
              Audit

Controlled folder access policies and options
Helps protect files in key system folders from changes made by malicious and suspicious
apps, including file-encrypting ransomware malware. For more information, see
Controlled folder access and the Event IDs it uses.

     Configure Controlled folder access:
        Block
        Block disk sectors only (starting in Configuration Manager version 1802)
              Allows Controlled folder access to be enabled for boot sectors only and does
              not enable the protection of specific folders or the default protected folders.
        Audit
        Audit disk sectors only (starting in Configuration Manager version 1802)
              Allows Controlled folder access to be enabled for boot sectors only and does
              not enable the protection of specific folders or the default protected folders.
        Disabled
     Allow apps through Controlled folder access -Click on Set and specify apps.
     Additional protected folders -Click on Set and specify additional protected
     folders.

Exploit protection policies
Applies exploit mitigation techniques to operating system processes and apps your
organization uses. These settings can be exported from the Windows Defender Security
Center app on Windows 10 or later devices. For more information, see Exploit
protection.

<!-- p.101 -->

     Exploit protection XML: -Click on Browse and specify the XML file to import.

        ２ Warning

        The XML file for exploit protection should be kept secure when transferring it
        between machines. The file should be deleted after import or kept in a secure
        location.

Network protection policy
Helps minimize the attack surface on devices from internet-based attacks. The service
restricts access to suspicious domains that might host phishing scams, exploits, and
malicious content. For more information, see Network protection.

     Configure network protection:
        Block
        Audit
        Disabled

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.102 -->

Create and deploy Microsoft Defender
Application Guard policy
Article • 12/05/2022

Applies to: Configuration Manager (current branch)

You can create and deploy Microsoft Defender Application Guard (Application Guard)
policies by using the Configuration Manager endpoint protection. These policies help
protect your users by opening untrusted web sites in a secure isolated container that
isn't accessible by other parts of the operating system.

Prerequisites
To create and deploy a Microsoft Defender Application Guard policy, you must use
Windows 10 1709 or later. The Windows 10 or later devices to which you deploy the
policy must be configured with a network isolation policy. For more information, see the
Microsoft Defender Application Guard overview.

Create a policy, and to browse the available
settings
   1. In the Configuration Manager console, choose Assets and Compliance.

   2. In the Assets and Compliance workspace, choose Overview > Endpoint
      Protection > Microsoft Defender Application Guard.

   3. In the Home tab, in the Create group, click Create Microsoft Defender Application
      Guard Policy.

   4. Using the article as a reference, you can browse and configure the available
      settings. Configuration Manager allows you to set certain policy settings:

            Application behavior
            Host interaction settings

   5. On the Network Definition page, specify the corporate identity, and define your
      corporate network boundary.

        ７ Note

<!-- p.103 -->

       Windows 10 or later PCs store only one network isolation list on the client.
       You can create two different kinds of network isolation lists and deploy them
       to the client:

             one from Windows Information Protection
             one from Microsoft Defender Application Guard

       If you deploy both policies, these network isolation lists must match. If you
       deploy lists that don't match to the same client, the deployment will fail. For
       more information, see the Windows Information Protection documentation.

   6. When you're finished, complete the wizard, and deploy the policy to one or more
     Windows 10 1709 or later devices.

Application behavior
Configures interactions between host devices and the Application Guard container.
Before Configuration Manager version 1802, both application behavior and host
interaction were under the Settings tab.

     Clipboard - Under settings prior to Configuration Manager 1802
        Permitted content type
           Text
           Images
     Printing:
        Enable printing to XPS
        Enable printing to PDF
        Enable printing to local printers
        Enable printing to network printers
     Graphics: (starting with Configuration Manager version 1802)
        Virtual graphics processor access
     Files: (starting with Configuration Manager version 1802)
        Save downloaded files to host
     Policies: (starting with Configuration Manager version 2207)
        Enable or disable cameras and microphones
        Certificate matching the thumbprints to the isolated container

Host interaction settings
Configures application behavior inside the Application Guard session. Before
Configuration Manager version 1802, both application behavior and host interaction

<!-- p.104 -->

were under the Settings tab.

     Other:
        Retain user-generated browser data
        Audit security events in the isolated application guard session

To edit Application Guard settings, expand Endpoint Protection in the Assets and
Compliance workspace, then click on the Microsoft Defender Application Guard node.
Right-click on the policy you want to edit, then select Properties.

Known issues
Applies to version 2203 or earlier

Devices running Windows 10, version 2004 will show failures in compliance reporting for
Microsoft Defender Application Guard File Trust Criteria. This issue occurs because some
subclasses were removed from the WMI class
MDM_WindowsDefenderApplicationGuard_Settings01 in Windows 10, version 2004. All other

Microsoft Defender Application Guard settings will still apply, only File Trust Criteria will
fail. Currently, there are no workarounds to bypass the error.

Applies to version 2207 or later

Enabling the policy doesn't install Microsoft Defender Application Guard feature by
default. Deploy a PowerShell script via ConfigMgr to all applicable machines.

Use the following commands to enable feature. Enable-WindowsOptionalFeature -
online -FeatureName "Windows-Defender-ApplicationGuard"

Next steps
For more information about Microsoft Defender Application Guard, see

     Microsoft Defender Application Guard overview.
     Microsoft Defender Application Guard FAQ.

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.105 -->

Windows Defender Application Control
management with Configuration
Manager
Article • 12/16/2024

Applies to: Configuration Manager (current branch)

Windows Defender Application Control is designed to protect devices against malware
and other untrusted software. It prevents malicious code from running by ensuring that
only approved code, that you know, can be run.

Application Control is a software-based security layer that enforces an explicit list of
software that is allowed to run on a PC. On its own, Application Control doesn't have
any hardware or firmware prerequisites. Application Control policies deployed with
Configuration Manager enable a policy on devices in targeted collections that meet the
minimum Windows version and SKU requirements outlined in this article. Optionally,
hypervisor-based protection of Application Control policies deployed through
Configuration Manager can be enabled through group policy on capable hardware.

For more information, see the Windows Defender Application Control deployment
guide.

  ７ Note

  This feature was previously known as configurable code integrity and Device Guard.

Using Application Control with Configuration
Manager
You can use Configuration Manager to deploy an Application Control policy. This policy
lets you configure the mode in which Application Control runs on devices in a collection.

You can configure one of the following modes:

   1. Enforcement enabled - Only trusted executables are allowed to run.
   2. Audit only - Allow all executables to run, but log untrusted executables that run in
      the local client event log.

<!-- p.106 -->

What can run when you deploy an Application
Control policy?
Application Control lets you strongly control what can run on devices you manage. This
feature can be useful for devices in high-security departments, where it's vital that
unwanted software can't run.

When you deploy a policy, typically, the following executables can run:

     Windows OS components
     Hardware Dev Center drivers with Windows Hardware Quality Labs signatures
     Windows Store apps
     The Configuration Manager client
     All software deployed through Configuration Manager that devices install after
     they process the Application Control policy
     Updates to built-in Windows components from:
        Windows Update
        Windows Update for Business
        Windows Server Update Services
        Configuration Manager
        Optionally, software with a good reputation as determined by the Microsoft
        Intelligent Security Graph (ISG). The ISG includes Windows Defender
        SmartScreen and other Microsoft services. The device must be running
        Windows Defender SmartScreen and Windows 10 version 1709 or later for this
        software to be trusted.

  ） Important

  These items don't include any software that isn't built-into Windows that
  automatically updates from the internet or third-party software updates. This
  limitation applies whether they're installed by any of the listed update mechanisms
  or from the internet. Application Control only allows software changes that are
  deployed through the Configuration Manager client.

Supported operating systems
To use Application Control with Configuration Manager, devices must be running
supported versions of:

     Windows 11 or later, Enterprise edition

<!-- p.107 -->

   Windows 10 or later, Enterprise edition
   Windows Server 2019 or later

  Tip

 Existing Application Control policies created with Configuration Manager version
 2006 or earlier won't work with Windows Server. To support Windows Server, create
 new Application Control policies.

Before you start
   Once a policy is successfully processed on a device, Configuration Manager is
   configured as a managed installer on that client. After the policy processes,
   software deployed by Configuration Manager is automatically trusted. Before the
   device processes the Application Control policy, software installed by
   Configuration Manager isn't automatically trusted.

      ７ Note

      For example, you can't use the Install Application step in a task sequence to
      install applications during an OS deployment. For more information, see Task
      sequence steps - Install Application.

   The default compliance evaluation schedule for Application Control policies is
   every day. This schedule is configurable during policy deployment. If you notice
   issues in policy processing, configure the compliance evaluation schedule to be
   more frequent. For example, every hour. This schedule dictates how often clients
   reattempt to process an Application Control policy if a failure occurs.

   Regardless of the enforcement mode you select, when you deploy an Application
   Control policy, devices can't run HTML applications with the .hta file extension.

Create an Application Control policy
 1. In the Configuration Manager console, go to the Assets and Compliance
   workspace.

 2. Expand Endpoint Protection, and then select the Windows Defender Application
   Control node.

<!-- p.108 -->

 3. On the Home tab of the ribbon, in the Create group, select Create Application
   Control policy.

 4. On the General page of the Create Application Control policy Wizard, specify the
   following settings:

         Name: Enter a unique name for this Application Control policy.

         Description: Optionally, enter a description for the policy that helps you
         identify it in the Configuration Manager console.

         Enforce a restart of devices so that this policy can be enforced for all
         processes: After the device processes the policy, a restart is scheduled on the
         client according to the Client Settings for Computer Restart. Applications
         currently running on the device won't apply the new Application Control
         policy until after a restart. However, applications launched after the policy
         applies will honor the new policy.

         Enforcement Mode: Choose one of the following enforcement methods:

            Enforcement Enabled: Only trusted applications are allowed to run.

            Audit Only: Allow all applications to run, but log untrusted programs that
            run. The audit messages are in the local client event log.

 5. On the Inclusions tab of the Create Application Control policy Wizard, choose if
   you want to Authorize software that is trusted by the Intelligent Security Graph.

 6. If you want to add trust for specific files or folders on devices, select Add. In the
   Add Trusted File or Folder dialog box, you can specify a local file or a folder path
   to trust. You can also specify a file or folder path on a remote device on which you
   have permission to connect. When you add trust for specific files or folders in an
   Application Control policy, you can:

         Overcome issues with managed installer behaviors.

         Trust line-of-business apps that you can't deploy with Configuration
         Manager.

         Trust apps that are included in an OS deployment image.

 7. Complete the wizard.

Deploy an Application Control policy

<!-- p.109 -->

   1. In the Configuration Manager console, go to the Assets and Compliance
      workspace.

   2. Expand Endpoint Protection, and then select the Windows Defender Application
      Control node.

   3. From the list of policies, select the one you want to deploy. On the Home tab of
      the ribbon, in the Deployment group, select Deploy Application Control Policy.

   4. In the Deploy Application Control policy dialog box, select the collection to which
      you want to deploy the policy. Then configure a schedule for when clients evaluate
      the policy. Finally, select whether the client can evaluate the policy outside of any
      configured maintenance windows.

   5. When you're finished, select OK to deploy the policy.

Monitor an Application Control policy
In general, use the information in the Monitor compliance settings article. This
information can help you monitor that the deployed policy has been correctly applied to
all devices.

To monitor the processing of an Application Control policy, use the following log file on
devices:

%WINDIR%\CCM\Logs\DeviceGuardHandler.log

To verify the specific software being blocked or audited, see the following local client
event logs:

      For blocking and auditing of executable files, use Applications and Services Logs
      > Microsoft > Windows > Code Integrity > Operational.

      For blocking and auditing of Windows Installer and script files, use Applications
      and Services Logs > Microsoft > Windows > AppLocker > MSI and Script.

Security and privacy information
      Devices that have a policy deployed to them in Audit Only or Enforcement
      Enabled mode, but haven't been restarted to enforce the policy, are vulnerable to
      untrusted software being installed. In this situation, the software might continue to
      run even if the device restarts, or receives a policy in Enforcement Enabled mode.

<!-- p.110 -->

     To help the effectiveness of the Application Control policy, first prepare the device
     in a lab environment. Deploy an Enforcement Enabled policy, then restart the
     device. Once you verify the apps work, then give the device to the user.

     Don't deploy a policy with Enforcement Enabled and then later deploy a policy
     with Audit Only to the same device. This configuration might result in untrusted
     software being allowed to run.

     When you use Configuration Manager to enable Application Control on devices,
     the policy doesn't prevent users with local administrator rights from circumventing
     the Application Control policies or otherwise running untrusted software.

     The only way to prevent users with local administrator rights from disabling
     Application Control is to deploy a signed binary policy. This deployment is possible
     through group policy, but not currently supported in Configuration Manager.

     Setting up Configuration Manager as a managed installer on devices uses a
     Windows AppLocker policy. AppLocker is only used to identify managed installers.
     All enforcement happens with Application Control.

Next steps
Manage antimalware policies and firewall settings

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.111 -->

Manage antimalware policies and
firewall settings
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the information in this topic to help you manage Endpoint Protection antimalware
policies and Windows Firewall policies, to perform on-demand scans, to force
computers to download the latest available definitions, and to remediate detected
malware.

Manage antimalware policies
In the Assets and Compliance workspace, expand Endpoint Protection, choose
Antimalware Policies, select the antimalware policy that you want to manage, and then
select a management task.

This table provides more information.

                                                                                    ﾉ   Expand table

 Task          Details

 Increase      If multiple antimalware policies are deployed to the same computer, they are
 Priority      applied in order. Use this option to increase the priority by which the selected
               antimalware policy is applied. Use the Order column to see the order in which the
               policies are applied.

               The antimalware policy that has the highest priority is always applied first.

 Decrease      If multiple antimalware policies are deployed to the same computer, they are
 Priority      applied in order. Use this option to decrease the priority by which the selected
               antimalware policy is applied. Use the Order column to view the order in which the
               policies are applied.

 Merge         Merges the two selected antimalware policies. In the Merge Policies dialog box,
               enter a name for the new, merged policy. The Base policy is the antimalware policy
               that is merged with this new antimalware policy.

               Note: If two settings conflict, the most secure setting is applied to computers.

 Deploy        Opens the Select Collection dialog box. Select the collection to which you want to
               deploy the antimalware policy, and then choose OK.

<!-- p.112 -->

Manage Windows Firewall policies
In the Assets and Compliance workspace, choose Endpoint Protection > Windows
Firewall Policies, select the Windows Firewall policy that you want to manage, and then
select a management task.

This table provides more information.

                                                                                ﾉ   Expand table

 Task          Details

 Increase      If multiple Windows Firewall policies are deployed to the same computer, they are
 Priority      applied in order. Use this option to increase the priority by which the selected
               Windows Firewall policy is applied. Use the Order column to view the order in
               which the policies are applied.

 Decrease      If multiple Windows Firewall policies are deployed to the same computer, they are
 Priority      applied in order. Use this option to decrease the priority by which the selected
               Windows Firewall policy is applied. Use the Order column to view the order in
               which the policies are applied.

 Deploy        Opens the Deploy Windows Firewall Policy dialog box from where you can deploy
               the firewall policy to a collection.

How to perform an on-demand scan of
computers
You can perform a scan of a single computer, multiple computers, or a collection of
computers in the Configuration Manager console. This scan occurs in addition to any
scheduled scans.

  ７ Note

  If any of the computers that you select do not have the Endpoint Protection client
  installed, the on-demand scan option is unavailable.

To perform an on-demand scan of computers
   1. In the Configuration Manager console, choose Assets and Compliance.

   2. In the Devices or Device Collections node, select the computer or collection of
        computers that you want to scan.

<!-- p.113 -->

   3. On the Home tab, in the Collection group, click Endpoint Protection, and then
     click Full Scan or Quick Scan.

     The scan will take place when the computer or collection of computers next
     downloads client policy. To monitor the results from the scan, use the procedures
     in How to monitor Endpoint Protection.

How to force computers to download the latest
definition files
You can force a single computer, multiple computers, or a collection of computers to
download the latest definition files from the Configuration Manager console.

  ７ Note

  If any of the computers that you select do not have the Endpoint Protection client
  installed, the Download Definition option is unavailable.

To force computers to download the latest definition files
   1. In the Devices or Device Collections node, select the computer or collection of
     computers for which you want to download definitions.

   2. On the Home tab, in the Collection group, choose Endpoint Protection, and then
     click Download Definition. The download will take place when the computer or
     collection of computers next downloads client policy.

       ７ Note

       Use the Endpoint Protection Status node under Security in the Monitoring
       workspace to discover clients that have out-of-date definitions.

Remediate detected malware
When malware is detected on client computers, this will be displayed in the Malware
Detected node under Endpoint Protection Status under Security in the Monitoring
workspace of the Configuration Manager console. Select an item from the Malware
Detected list, and then use one of the following management tasks to remediate or
allow the detected malware:

<!-- p.114 -->

     Allow this threat - Creates an antimalware policy to allow the selected malware.
     The policy is deployed to the All Systems collection and can be monitored in the
     Client Operations node of the Monitoring workspace.

     Restore files quarantined by this threat - Opens the Restore quarantined files
     dialog box where you can select one of the following options:

        Run the allow-threat or exclusion operation first to assure that files are not
        put back into quarantine - Restores the files that were quarantined because of
        the detected malware and also excludes the files from malware scans. If you do
        not exclude the files from malware scans, they will be quarantined again when
        the next scan runs.

        Restore files without a dependency on the allow or exclusion job - Restores
        the quarantined files but does not add them to the exclusion list.

     View infected clients - Displays a list of all clients that were infected by the
     selected malware.

     Exclude selected files or paths from scan - When you select this option from the
     malware details pane, the Exclude files and paths dialog box opens where you can
     specify the files and folders that you want to exclude from malware scans.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.115 -->

Example scenario: Use Endpoint
Protection to protect computers from
malware
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article provides an example scenario for how you can implement Endpoint
Protection in Configuration Manager to protect computers in your organization from
malware attacks.

Scenario overview
Configuration Manager is installed and used at Woodgrove Bank. The bank currently
uses Endpoint Protection to protect computers against malware attacks. Additionally,
the bank uses Windows Group Policy to ensure that the Windows Firewall is enabled on
all computers in the company and that users are notified when Windows Firewall blocks
a new program.

The Configuration Manager administrators have been asked to upgrade the Woodgrove
Bank antimalware software to Endpoint Protection so that the bank can benefit from the
latest antimalware features and be able to centrally manage the antimalware solution
from the Configuration Manager console.

Business requirements
This implementation has the following requirements:

      Use Configuration Manager to manage the Windows Firewall settings that are
      currently managed by Group Policy.

      Use Configuration Manager software updates to download malware definitions to
      computers. If software updates aren't available, for example if the computer isn't
      connected to the corporate network, computers must download definition updates
      from Microsoft Update.

      Users' computers must perform a quick malware scan every day. Servers, however,
      must run a full scan every Saturday, outside business hours, at 1 A.M.

      Send an email alert whenever any one of the following events occurs:

<!-- p.116 -->

         Malware is detected on any computer

         The same malware threat is detected on more than 5 percent of computers

         The same malware threat is detected more than 5 times in any 24-hour period

         More than 3 different types of malware are detected in any 24-hour period

     The admins then do the following steps to implement Endpoint Protection:

Steps to implement Endpoint Protection
                                                                                 ﾉ   Expand table

Process                                                   Reference

The admins review the available information about the     For overview information about
basic concepts for Endpoint Protection in Configuration   Endpoint Protection, see Endpoint
Manager.                                                  Protection.

The admins install the Endpoint Protection site system    For more information about how to
role on one site system server only, at the top of the    install the Endpoint Protection site
Woodgrove Bank hierarchy.                                 system role, see "Prerequisites" in
                                                          Configure Endpoint Protection.

The admins configure Configuration Manager to use an      For more information, see Configure
SMTP server to send the email alerts.                     alerts in Endpoint Protection.

Note: You must configure an SMTP server only if you
want to be notified by email when an Endpoint
Protection alert is generated.

The admins create a device collection that contains all   For more information about how to
computers and servers to install the Endpoint             create collections, see How to create
Protection client. They name this collection All          collections
Computers Protected by Endpoint Protection.

Tip: You can't configure alerts for user collections.

The admins configure the following alerts for the         See "Configure Alerts for Endpoint
collection:                                               Protection" in Configuring Endpoint
                                                          Protection.
1) Malware is detected: The admins configure an alert
severity of Critical.

2) The same type of malware is detected on a number
of computers: The admins configure an alert severity of
Critical and specify that the alert will be generated
when more than 5 percent of computers have malware

<!-- p.117 -->

Process                                                    Reference

detected.

3) The same type of malware is repeatedly detected
within the specified interval on a computer: The
admins configure an alert severity of Critical and
specify that the alert will be generated when malware is
detected more than 5 times in a 24-hour period.

4) Multiple types of malware are detected on the
same computer within the specified interval: The
admins configure an alert severity of Critical and
specify that the alert will be generated when more than
3 types of malware are generated in a 24-hour period.

The value for Alert Severity indicates the alert level
that will be displayed in the Configuration Manager
console and in alerts that they receive in an email
message.

They additionally select the option View this collection
in the Endpoint Protection dashboard so that they can
monitor the alerts in the Configuration Manager
console.

The admins configure Configuration Manager software        For more information, see the "Using
updates to download and deploy definition updates          Configuration Manager Software
three times a day by using an automatic deployment         Updates to Deliver Definition Updates"
rule.                                                      section in Use Configuration Manager
                                                           software updates to deliver definition
                                                           updates.

The admins examine the settings in the default             See How to create and deploy
antimalware policy, which contains recommended             antimalware policies for Endpoint
security settings from Microsoft. For computers to         Protection.
perform a quick scan every day to, they change the
following settings:

1) Run a daily quick scan on client computers: Yes.

2) Daily quick scan schedule time: 9:00 AM.

The admins note that Updates distributed from
Microsoft Update is selected by default as a definition
update source. This fulfills the business requirement
that computers download definitions from Microsoft
Update when they can't receive Configuration Manager
software updates.

<!-- p.118 -->

Process                                                   Reference

The admins create a collection that contains only the     See How to create collections
Woodgrove Bank servers named Woodgrove Bank
Servers.

The admins create a custom antimalware policy named       See How to create and deploy
Woodgrove Bank Server Policy. They add only the           antimalware policies for Endpoint
settings for Scheduled scans and make the following       Protection.
changes:

Scan type: Full

Scan day: Saturday

Scan time: 1:00 AM

Run a daily quick scan on client computers: No.

The admins deploy the Woodgrove Bank Server Policy        See "To deploy an antimalware policy to
custom antimalware policy to the Woodgrove Bank           client computers" How to create and
Servers collection.                                       deploy antimalware policies for
                                                          Endpoint Protection article.

The admins create a new set of custom client device       For more information, see Configure
settings for Endpoint Protection and names these          Custom Client Settings for Endpoint
Woodgrove Bank Endpoint Protection Settings.              Protection.

Note: If you don't want to install and enable Endpoint
Protection on all clients in your hierarchy, make sure
that the options Manage Endpoint Protection client
on client computers and Install Endpoint Protection
client on client computers are both configured as No
in the default client settings.

They configure the following settings for Endpoint
Protection:

Manage Endpoint Protection client on client
computers: Yes

This setting and value ensures that any existing
Endpoint Protection client that is installed becomes
managed by Configuration Manager.

Install Endpoint Protection client on client computers:
Yes.

The admins deploy the Woodgrove Bank Endpoint             See "Configure Custom Client Settings
Protection Settings client settings to the All            for Endpoint Protection" in Configuring

<!-- p.119 -->

 Process                                                   Reference

 Computers Protected by Endpoint Protection                Endpoint Protection in Configuration
 collection.                                               Manager.

 The admins use the Create Windows Firewall Policy         See How to create and deploy Windows
 Wizard to create a policy by configuring the following    Firewall policies for Endpoint Protection
 settings for the domain profile:

 1) Enable Windows Firewall: Yes

 2)
 Notify the user when Windows Firewall blocks a new
 program: Yes

 The admins deploy the new firewall policy to the          See "To deploy a Windows Firewall
 collection All Computers Protected by Endpoint            policy" in the How to create and deploy
 Protection that they created earlier.                     Windows Firewall policies for Endpoint
                                                           Protection

 The admins use the available management tasks for         See How to manage antimalware
 Endpoint Protection to manage antimalware and             policies and firewall settings for
 Windows Firewall policies, perform on-demand scans        Endpoint Protection
 of computers when necessary, force computers to
 download the latest definitions, and to specify any
 further actions to take when malware is detected.

 The admins use the following methods to monitor the       See How to monitor Endpoint
 status of Endpoint Protection and the actions that are    Protection
 taken by Endpoint Protection:

 1) By using the Endpoint Protection Status node under
 Security in the Monitoring workspace.

 2) By using the Endpoint Protection node in the Assets
 and Compliance workspace.

 3) By using the built-in Configuration Manager reports.

The admins report a successful implementation of Endpoint Protection to their manager,
and confirms that the computers at Woodgrove Bank are now protected from
antimalware, according to the business requirements that they were given.

Next steps
For more information, see How to Configure Endpoint Protection

<!-- p.120 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback
