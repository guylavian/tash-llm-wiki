---
title: "Protect data and infrastructure documentation — pages 241-280"
type: reference
domain: sccm
slug: sccm-intune-configmgr-protect-p0241-0280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-protect-p0241-0280
family: sccm
documentKind: "doc"
abstract: "Smart Card or other certificate Supported connection types: Microsoft SSL (SSTP) Microsoft Automatic IKEv2 PPTP L2TP MSCHAP v2 Supported connection types: Microsoft SSL (SSTP) Microsoft Automatic IKEv2 PPTP L2TP Use machine certificates Supported connection types: IKEv2 Addition"
---

# Protect data and infrastructure documentation — pages 241-280

<!-- p.241 -->

Smart Card or other certificate
Supported connection types:

     Microsoft SSL (SSTP)
     Microsoft Automatic
     IKEv2
     PPTP
     L2TP

MSCHAP v2
Supported connection types:

     Microsoft SSL (SSTP)
     Microsoft Automatic
     IKEv2
     PPTP
     L2TP

Use machine certificates
Supported connection types:

     IKEv2

Additional authentication options
When the Windows client version supports it, the option to Configure the
authentication method is available. This option opens the Windows properties window
to configure the authentication method.

Depending on the selected options, you might be asked to specify more information, for
example:

     Remember the user credentials at each logon: User credentials are remembered
     so that users don't have to enter them each time they connect.

     Select a client certificate for client authentication: Select a previously created
     client SCEP certificate profile to authenticate the VPN connection. For more
     information, see Create PFX certificate profiles.

<!-- p.242 -->

Next steps
     For third-party VPN connections, distribute the VPN app before you deploy the
     VPN profile. If you don't deploy the app, users will be prompted to do so when
     they try to connect to the VPN. For more information, see Deploy applications.

     Deploy the VPN profile. For more information, see How to deploy profiles.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.243 -->

Find a package family name (PFN) for
per-app VPN
Article • 01/12/2024

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

There are two ways to find a PFN so that you can configure a per-app VPN.

Find a PFN for an app that's installed on a
Windows 10 computer
If the app you're working with is already installed on a Windows 10 computer, you can
use the Get-AppxPackage PowerShell cmdlet to get the PFN.

The syntax for Get-AppxPackage is:

  Syntax

  Get-AppxPackage [[-Name] <String> ] [[-Publisher] <String> ] [-AllUsers] [-
  User <String> ] [ <CommonParameters>]

  ７ Note

  You may have to run PowerShell as an admin in order to retrieve the PFN

For example, to get info on all the universal apps installed on the computer use Get-
AppxPackage .

To get info on an app you know the name of, or part of the name of, use Get-
AppxPackage *<app_name> . Note the use of the wildcard character, particularly helpful if

you're not sure of the full name of the app. For example to get the info for OneNote,
use Get-AppxPackage *OneNote .

<!-- p.244 -->

Here's the information retrieved for OneNote:

Name : Microsoft.Office.OneNote

Publisher : CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond,
S=Washington, C=US

Architecture : X64

ResourceId :

Version : 17.6769.57631.0

PackageFullName : Microsoft.Office.OneNote_17.6769.57631.0_x64__8wekyb3d8bbwe

InstallLocation : C:\Program Files\WindowsApps

\Microsoft.Office.OneNote_17.6769.57631.0_x64__8wekyb3d8bbwe

IsFramework : False

PackageFamilyName : Microsoft.Office.OneNote_8wekyb3d8bbwe

PublisherId : 8wekyb3d8bbwe

Find a PFN if the app is not installed on a
computer
   1. Go to https://www.microsoft.com/store/apps
   2. Enter the name of the app in the search bar. In our example, search for OneNote.
   3. Click the link to the app. The URL that you access has a series of letters at the end.
     In our example, the URL looks like this:
     https://www.microsoft.com/store/apps/onenote/9wzdncrfhvjl

   4. In a different tab, paste the following URL,
     https://bspmts.mp.microsoft.com/v1/public/catalog/Retail/Products/<app

     id>/applockerdata , replacing <app id> with the app ID you obtained from

     https://www.microsoft.com/store/apps        - that series of letters at the end of the
     URL in step 3. In our example, example of OneNote, you'd paste:
     https://bspmts.mp.microsoft.com/v1/public/catalog/Retail/Products/9wzdncrfhvjl

     /applockerdata .

In Microsoft Edge, the information you want is displayed; in Internet Explorer, click Open
to see the information. The PFN value is given on the first line. Here's how the results

<!-- p.245 -->

look for our example:

  JSON

  {
    "packageFamilyName": "Microsoft.Office.OneNote_8wekyb3d8bbwe",
    "packageIdentityName": "Microsoft.Office.OneNote",
    "windowsPhoneLegacyId": "ca05b3ab-f157-450c-8c49-a1f127f5e71d",
    "publisherCertificateName": "CN=Microsoft Corporation, O=Microsoft
  Corporation, L=Redmond, S=Washington, C=US"
  }

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.246 -->

Deploy resource access profiles in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

After you create one of the following resource access profiles, deploy it to one or more
collections:

      Wi-Fi
      VPN
      Certificate

When you deploy these profiles, you specify the target collection, and specify how often
the client evaluates the profile for compliance.

Deploy a profile
   1. In the Configuration Manager console, go to the Assets and Compliance
      workspace. Expand Compliance Settings, expand Company Resource Access, and
      then choose the appropriate profile node. For example, Wi-Fi Profiles.

   2. In the list of profiles, select the profile that you want to deploy. Then in the Home
      tab of the ribbon, in the Deployment group, select Deploy.

   3. In the deploy profile window, specify the following information:

              Collection: Select the collection where you want to deploy the profile.

              Generate an alert: Enable this option to configure an alert. The site generates
              this alert if the profile compliance is less than the specified percentage by the
              specified date and time. You can also select whether you want an alert to be
              sent to System Center Operations Manager.

<!-- p.247 -->

           Random delay (hours): For certificate profiles that contain Simple Certificate
           Enrollment Protocol (SCEP) settings, specify a delay window to avoid
           excessive processing on the Network Device Enrollment Service (NDES). The
           default value is 64 hours.

           Specify the compliance evaluation schedule for this...profile: Specify how
           often the client evaluates compliance for this profile. Select a Simple
           schedule or configure a Custom schedule. By default, the simple schedule is
           every 12 hours.

   4. Select OK to close the window and create the deployment.

Delete a deployment
If you want to delete a deployment, select it from the list. In the details pane, switch to
the Deployments tab. Select the deployment, and then in the Deployment tab of the
ribbon, select Delete.

  ） Important

  When you remove a VPN profile deployment, Configuration Manager doesn't
  remove the VPN profile from Windows. If you want to remove the profile from
  devices, manually remove it.

Next steps
Monitor Wi-Fi and VPN profiles

Monitor certificate profiles

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.248 -->

What happened to hybrid MDM?
07/21/2025

Applies to: Configuration Manager (current branch)

  ２ Warning

  Microsoft retired the hybrid MDM service offering as of September 1, 2019. Any remaining
  hybrid MDM devices won't receive policy, apps, or security updates.

Remove hybrid MDM
If your Configuration Manager site had a Microsoft Intune Subscription, you need to remove it.

   1. In the Configuration Manager console, go to the Administration workspace. Expand
     Cloud Services, and select the Microsoft Intune Subscription node. Delete your existing
     Intune Subscription.

   2. In the Remove Microsoft Intune Subscription Wizard, select the option to Remove
     Microsoft Intune Subscription from Configuration Manager, and then click Next.

   3. Complete the wizard.

Deprecation announcement
The following note is the original deprecation announcement:

  ７ Note

  As of August 14, 2018, hybrid mobile device management is a deprecated feature.
  Starting with the 1902 Intune service release, expected at the end of February 2019, new
  customers can't create a new hybrid connection.

  Since launching on Azure over a year ago, Intune has added hundreds of new customer-
  requested and market-leading service capabilities. It now offers far more capabilities than
  those offered through hybrid mobile device management (MDM). Intune on Azure
  provides a more integrated, streamlined administrative experience for your enterprise
  mobility needs.

  As a result, most customers choose Intune on Azure over hybrid MDM. The number of
  customers using hybrid MDM continues to decrease as more customers move to the

<!-- p.249 -->

cloud. Therefore, on September 1, 2019, Microsoft will retire the hybrid MDM service
offering.

This change doesn't affect on-premises Configuration Manager or co-management for
Windows 10 devices. If you're unsure whether you're using hybrid MDM, go to the
Administration workspace of the Configuration Manager console, expand Cloud Services,
and select Microsoft Intune Subscriptions. If you have a Microsoft Intune subscription set
up, your tenant is configured for hybrid MDM.

How does this affect me?

     Microsoft will support your hybrid MDM usage for the next year. The feature will
     continue to receive major bug fixes. Microsoft will support existing functionality on
     new OS versions, such as enrollment on iOS 12. There will be no new features for
     hybrid MDM.

     If you migrate to Intune on Azure before the end of the hybrid MDM offering, there
     should be no end user impact.

     On September 1, 2019, any remaining hybrid MDM devices will no longer receive
     policy, apps, or security updates.

     Licensing remains the same. Intune on Azure licenses are included with hybrid MDM.

     The on-premises MDM feature in Configuration Manager isn't deprecated. Starting
     in Configuration Manager version 1810, you can use on-premises MDM without an
     Intune connection. For more information, see An Intune connection is no longer
     required for new on-premises MDM deployments.

     The on-premises Conditional Access feature of Configuration Manager is also
     deprecated with hybrid MDM. If you use Conditional Access on devices managed
     with the Configuration Manager client, make sure they are protected before you
     migrate.

            1. Set up Conditional Access policies in Azure
            2. Set up compliance policies in Intune portal
            3. Finish hybrid migration, and set the MDM authority to Intune
            4. Enable co-management
            5. Move the compliance policies co-management workload to Intune

     For more information, see Conditional Access with co-management.

<!-- p.250 -->

  What do I need to do to prepare for this change?

            Start planning your migration for MDM from the ConfigMgr console to Azure. Many
            customers, including Microsoft IT, have gone through this process.

            Contact your partner of record or FastTrack for assistance. FastTrack for Microsoft
            365   can assist in your migration from hybrid MDM to Intune on Azure.

  For more information, see the Intune support blog post .

Next steps
For more information on supported features for managing MDM devices, see the following
articles:

      What is Microsoft Intune?
      What is on-premises MDM?
      Device management with Exchange

<!-- p.251 -->

Monitor Email, Wi-Fi and VPN profiles in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

After you have deployed Configuration Manager Email, Wi-Fi or VPN profiles to users in
your hierarchy, you can use the following procedures to monitor the compliance status
of the profile:

      How to View Compliance Results in the Configuration Manager Console

      How to View Compliance Results by Using Reports

How to View Compliance Results in the
Configuration Manager Console
Use this procedure to view details about the compliance of deployed profiles in the
Configuration Manager console.

To view compliance results in the Configuration Manager console
   1. In the Configuration Manager console, click Monitoring.

   2. In the Monitoring workspace, click Deployments.

   3. In the Deployments list, select the profile deployment for which you want to
      review compliance information.

   4. You can review summary information about the compliance of the profile
      deployment on the main page. To view more detailed information, select the
      profile deployment, and then, on the Home tab, in the Deployment group, click
      View Status to open the Deployment Status page.

<!-- p.252 -->

   The Deployment Status page contains the following tabs:

        Compliant: Displays the compliance of the profile that is based on the
        number of affected assets. You can double-click a rule to create a temporary
        node under the Users node in the Assets and Compliance workspace, which
        contains all users that are compliant with this profile. The Asset Details pane
        displays the users that are compliant with the profile. Double-click a user in
        the list to display additional information.

          ） Important

          A profile is not evaluated if it is not applicable on a client device;
          however, it is returned as compliant.

        Error: Displays a list of all errors for the selected profile deployment that is
        based on the number of affected assets. You can double-click a rule to create
        a temporary node under the Users node of the Assets and Compliance
        workspace, which contains all users that generated errors with this profile.
        When you select a user, the Asset Details pane displays the users that are
        affected by the selected issue. Double-click a user in the list to display
        additional information about the issue.

        Non-Compliant: Displays a list of all noncompliant rules within the profile
        that is based on the number of affected assets. You can double-click a rule to
        create a temporary node under the Users node of the Assets and
        Compliance workspace, which contains all users that are not compliant with
        this profile. When you select a user, the Asset Details pane displays the users
        that are affected by the selected issue. Double-click a user in the list to
        display further information about the issue.

        Unknown: Displays a list of all users that did not report compliance for the
        selected profile deployment together with the current client status of the
        devices.

 5. On the Deployment Status page, you can review detailed information about the
   compliance of the deployed profile. A temporary node is created under the
   Deployments node that helps you find this information again quickly.

How to View Compliance Results by Using
Reports

<!-- p.253 -->

Compliance settings, which include profiles in Configuration Manager, also includes a
number of built-in reports that let you monitor information about profiles. These reports
have the report category of Compliance and Settings Management.

  ） Important

  You must use a wildcard (%) character when you use the parameters Device filter
  and User filter in the compliance settings reports.

For more information about how to configure reporting in Configuration Manager, see
Introduction to reporting.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.254 -->

How to monitor certificate profiles in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

View Compliance Results in the Configuration
Manager Console
To monitor SCEP certificate compliance do not use the console, rather, use reports.

   1. In the Configuration Manager console, choose Monitoring> Deployments.

   2. Select the certificate profile deployment of interest.

   3. Review summary certificate compliance information on the main page. For more
      detailed information, select the certificate profile, and then on the Home tab, in
      the Deployment group, choose View Status to open the Deployment Status page.

      The Deployment Status page contains the following tabs:

            Compliant: Displays the compliance of the certificate profile based on the
            number of assets that are affected. You can double-click a rule to create a
            temporary node under the Users node in the Assets and Compliance
            workspace. This node contains all users that are compliant with the certificate
            profile. The Asset Details pane also displays the users that are compliant with
            this profile. Double-click a user in the list for more information.

              ） Important

              A certificate profile is not evaluated if it is not applicable on a client
              device. However, it is returned as compliant.

<!-- p.255 -->

       Error: Displays a list of all errors for the selected certificate profile
       deployment based on the number of assets that are affected. You can
       double-click a rule to create a temporary node under the Users node of the
       Assets and Compliance workspace. This node contains all users that
       generated errors with this profile. When you select a user, the Asset Details
       pane displays the users that are affected by the selected issue. Double-click a
       user in the list to display for more information.

       Non-Compliant: Displays a list of all noncompliant rules within the certificate
       profile based on the number of assets that are affected. You can double-click
       a rule to create a temporary node under the Users node of the Assets and
       Compliance workspace. This node contains all users that are not compliant
       with this profile. When you select a user, the Asset Details pane displays the
       users that are affected by the selected issue. Double-click a user in the list to
       display further information about the issue.

       Unknown: Displays a list of all users that did not report compliance for the
       selected certificate profile deployment together with the current client status
       of the devices.

4. On the Deployment Status page, review detailed information about the
  compliance of the deployed certificate profile. A temporary node is created under
  the Deployments node that helps you find this information again quickly.

  The enrollment status of the certificate is displayed as a number. Use the following
  table to understand what each number means:

                                                                           ﾉ      Expand table

   Enrollment    Description
   status

   0x00000001    The enrollment succeeded, and the certificate has been issued.

   0x00000002    The request has been submitted and the enrollment is pending, or the
                 request has been issued out of band.

   0x00000004    Enrollment must be deferred.

   0x00000010    An error occurred.

   0x00000020    The enrollment status is unknown.

   0x00000040    The status information has been skipped. This can occur if a HYPERLINK
                 "https://msdn.microsoft.com/windows/ms721572 " \l

<!-- p.256 -->

       Enrollment        Description
       status

                         "_security_certification_authority_gly" certification authority is not valid or
                         has not been selected for monitoring.

       0x00000100        Enrollment has been denied.

View Compliance Results by Using Reports
Compliance settings in Configuration Manager include built-in reports that you can use
to monitor information about certificate profiles. These reports have the report category
of Compliance and Settings Management.

  ） Important

  You must use a wildcard (%) character when you use the parameters Device filter
  and User filter in the reports for compliance settings.

To monitor SCEP certificate compliance use these certificate reports under the report
node Company Resource Access:

     Certificate issuance history
     List of assets with certificates nearing expiry
     List of assets by certificate issuance status

For more information about how to configure reporting in Configuration Manager, see
Introduction to reporting.

Feedback
Was this page helpful?       Yes        No

Provide product feedback

<!-- p.257 -->

How to monitor Endpoint Protection
status
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can monitor Endpoint Protection in your Microsoft Configuration Manager hierarchy
by using the Endpoint Protection Status node under Security in the Monitoring
workspace, the Endpoint Protection node in the Assets and Compliance workspace,
and by using reports.

How to Monitor Endpoint Protection by Using
the Endpoint Protection Status Node
   1. In the Configuration Manager console, click Monitoring.

   2. In the Monitoring workspace, expand Security and then click Endpoint Protection
      Status.

   3. In the Collection list, select the collection for which you want to view status
      information.

        ） Important

        Collections are available for selection in the following cases:

                When you select View this collection in the Endpoint Protection
                dashboard on the Alerts tab of the <collection name>Properties dialog
                box.
                  When you deploy an Endpoint Protection antimalware policy to the
                  collection.
                  When you enable and deploy Endpoint Protection client settings to
                  the collection.

   4. Review the information that is displayed in the Security State and Operational
      State sections. You can click any status link to create a temporary collection in the
      Devices node in the Assets and Compliance workspace. The temporary collection
      contains the computers with the selected status.

<!-- p.258 -->

          ） Important

          Information that is displayed in the Endpoint Protection Status node is based
          on the last data that was summarized from the Configuration Manager
          database and might not be current. If you want to retrieve the latest data, on
          the Home tab, click Run Summarization, or click Schedule Summarization to
          adjust the summarization interval.

How to Monitor Endpoint Protection in the
Assets and Compliance Workspace
   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, perform one of the following actions:

             Click Devices. In the Devices list, select a computer, and then click the
             Malware Detail tab.

             Click Device Collections. In the Device Collections list, select the collection
             that contains the computer you want to monitor and then, on the Home tab,
             in the Collection group, click Show Members.

   3. In the <collection name> list, select a computer, and then click the Malware Detail
     tab.

How to Monitor Endpoint Protection by Using
Reports
Use the following reports to help you view information about Endpoint Protection in
your hierarchy. You can also use these reports to help troubleshoot any Endpoint
Protection problems. For more information about how to configure reporting in
Configuration Manager, see Introduction to reporting and Log files. The Endpoint
Protection reports are in the Endpoint Protection folder.

                                                                                 ﾉ   Expand table

 Report name                   Description

 Antimalware Activity          Displays an overview of antimalware activity for a specified
 Report                        collection.

<!-- p.259 -->

 Report name                     Description

 Infected Computers              Displays a list of computers on which a specified threat is detected.

 Top Users By Threats            Displays a list of users with the most number of detected threats.

 User Threat List                Displays a list of threats that were found for a specified user
                                 account.

Malware Alert Levels
Use the following table to identify the different Endpoint Protection alert levels that
might be displayed in reports, or in the Configuration Manager console.

                                                                                     ﾉ   Expand table

 Alert level    Description

 Failed         Endpoint Protection failed to remediate the malware. Check your logs for details
                of the error.

                Note: For a list of Configuration Manager and Endpoint Protection log files, see
                the "Endpoint Protection" section in the Log files topic.

 Removed        Endpoint Protection successfully removed the malware.

 Quarantined    Endpoint Protection moved the malware to a secure location and prevented it
                from running until you remove it or allow it to run.

 Cleaned        The malware was cleaned from the infected file.

 Allowed        An administrative user selected to allow the software that contains the malware to
                run.

 No Action      Endpoint Protection took no action on the malware. This might occur if the
                computer is restarted after malware is detected and the malware is no longer
                detected; for instance, if a mapped network drive on which malware is detected is
                not reconnected when the computer restarts.

 Blocked        Endpoint Protection blocked the malware from running. This might occur if a
                process on the computer is found to contain malware.

Feedback
Was this page helpful?    Yes         No

<!-- p.260 -->

Provide product feedback

<!-- p.261 -->

BitLocker settings reference
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

BitLocker management policies in Configuration Manager contain the following policy
groups:

      Setup
      Operating system drive
      Fixed drive
      Removable drive
      Client management

The following sections describe and suggest configurations for the settings in each
group.

Setup
The settings on this page configure global BitLocker encryption options.

Drive encryption method and cipher strength
Suggested configuration: Enabled with the default or greater encryption method.

  ７ Note

  The Setup properties page includes two groups of settings for different versions of
  Windows. This section describes them both.

Windows 8.1 devices

For Windows 8.1 devices, enable the option for Drive encryption method and cipher
strength, and select one of the following encryption methods:

      AES 128-bit with Diffuser
      AES 256-bit with Diffuser
      AES 128-bit (default)
      AES 256-bit

<!-- p.262 -->

For more information on how to create this policy with Windows PowerShell, see New-
CMBLEncryptionMethodPolicy.

Windows 10 or later devices

For Windows 10 or later devices, enable the option for Drive encryption method and
cipher strength (Windows 10 or later). Then individually select one of the following
encryption methods for OS drives, fixed data drives, and removable data drives:

     AES-CBC 128-bit
     AES-CBC 256-bit
     XTS-AES 128-bit (default)
     XTS-AES 256-bit

   Tip

  BitLocker uses Advanced Encryption Standard (AES) as its encryption algorithm with
  configurable key lengths of 128 or 256 bits. On Windows 10 or later devices, the
  AES encryption supports cipher block chaining (CBC) or ciphertext stealing (XTS).

  If you need to use a removable drive on devices that don't run Windows 10, use
  AES-CBC.

For more information on how to create this policy with Windows PowerShell, see New-
CMBLEncryptionMethodWithXts.

General usage notes for drive encryption and cipher strength
     If you disable or don't configure these settings, BitLocker uses the default
     encryption method.

     Configuration Manager applies these settings when you turn on BitLocker.

     If the drive is already encrypted or is in progress, any change to these policy
     settings doesn't change the drive encryption on the device.

     If you use the default value, the BitLocker Computer Compliance report may
     display the cipher strength as unknown. To work around this issue, enable this
     setting and set an explicit value for cipher strength.

Prevent memory overwrite on restart

<!-- p.263 -->

Suggested configuration: Not configured

Configure this policy to improve restart performance without overwriting BitLocker
secrets in memory on restart.

When you don't configure this policy, BitLocker removes its secrets from memory when
the computer restarts.

For more information on how to create this policy with Windows PowerShell, see New-
CMNoOverwritePolicy.

Validate smart card certificate usage rule compliance
Suggested configuration: Not configured

Configure this policy to use smartcard certificate-based BitLocker protection. Then
specify the certificate Object identifier.

When you don't configure this policy, BitLocker uses the default object identifier
1.3.6.1.4.1.311.67.1.1 to specify a certificate.

For more information on how to create this policy with Windows PowerShell, see New-
CMScCompliancePolicy.

Organization unique identifiers
Suggested configuration: Not configured

Configure this policy to use a certificate-based data recovery agent or the BitLocker To
Go reader.

When you don't configure this policy, BitLocker doesn't use the Identification field.

If your organization requires higher security measurements, configure the Identification
field. Set this field on all targeted USB devices, and align it with this setting.

For more information on how to create this policy with Windows PowerShell, see New-
CMUidPolicy.

OS drive
The settings on this page configure the encryption settings for the drive on which
Windows is installed.

<!-- p.264 -->

Operating system drive encryption settings
Suggested configuration: Enabled

If you enable this setting, the user has to protect the OS drive, and BitLocker encrypts
the drive. If you disable it, the user can't protect the drive. If you don't configure this
policy, BitLocker protection isn't required on the OS drive.

  ７ Note

  If the drive is already encrypted, and you disable this setting, BitLocker decrypts the
  drive.

If you have devices without a Trusted Platform Module (TPM), use the option to Allow
BitLocker without a compatible TPM (requires a password). This setting allows
BitLocker to encrypt the OS drive, even if the device doesn't have a TPM. If you allow
this option, Windows prompts the user to specify a BitLocker password.

On devices with a compatible TPM, two types of authentication methods can be used at
startup to provide added protection for encrypted data. When the computer starts, it
can use only the TPM for authentication, or it can also require the entry of a personal
identification number (PIN). Configure the following settings:

     Select protector for operating system drive: Configure it to use a TPM and PIN, or
     just the TPM.

     Configure minimum PIN length for startup: If you require a PIN, this value is the
     shortest length the user can specify. The user enters this PIN when the computer
     boots to unlock the drive. By default, the minimum PIN length is 4 .

   Tip

  For higher security, when you enable devices with TPM + PIN protector, consider
  disabling the following group policy settings in System > Power Management >
  Sleep Settings:

        Allow Standby States (S1-S3) When Sleeping (Plugged In)

        Allow Standby States (S1-S3) When Sleeping (On Battery)

For more information on how to create this policy with Windows PowerShell, see New-
CMBMSOSDEncryptionPolicy.

<!-- p.265 -->

Allow enhanced PINs for startup
Suggested configuration: Not configured

Configure BitLocker to use enhanced startup PINs. These PINs permit the use of more
characters such as uppercase and lowercase letters, symbols, numbers, and spaces. This
setting applies when you turn on BitLocker.

  ） Important

  Not all computers can support enhanced PINs in the pre-boot environment. Before
  you enable its use, evaluate whether your devices are compatible with this feature.

If you enable this setting, all new BitLocker startup PINs allow the user to create
enhanced PINs.

        Require ASCII-only PINs: Help make enhanced PINs more compatible with
        computers that limit the type or number of characters that you can enter in the
        pre-boot environment.

If you disable or don't configure this policy setting, BitLocker doesn't use enhanced
PINs.

For more information on how to create this policy with Windows PowerShell, see New-
CMEnhancedPIN.

Operating system drive password policy
Suggested configuration: Not configured

Use these settings to set the constraints for passwords to unlock BitLocker-protected OS
drives. If you allow non-TPM protectors on OS drives, configure the following settings:

        Configure password complexity for operating system drives: To enforce
        complexity requirements on the password, select Require password complexity.

        Minimum password length for operating system drive: By default, the minimum
        length is 8 .

        Require ASCII-only passwords for removable OS drives

If you enable this policy setting, users can configure a password that meets the
requirements that you define.

<!-- p.266 -->

For more information on how to create this policy with Windows PowerShell, see New-
CMOSPassphrase.

General usage notes for OS drive password policy

      For these complexity requirement settings to be effective, also enable the group
      policy setting Password must meet complexity requirements in Computer
      Configuration > Windows Settings > Security Settings > Account Policies >
      Password Policy.

      BitLocker enforces these settings when you turn it on, not when you unlock a
      volume. BitLocker lets you unlock a drive with any of the protectors that are
      available on the drive.

      If you use group policy to enable FIPS-compliant algorithms for encryption,
      hashing, and signing, you can't allow passwords as a BitLocker protector.

Reset platform validation data after BitLocker recovery
Suggested configuration: Not configured

Control whether Windows refreshes platform validation data when it starts after
BitLocker recovery.

If you enable or don't configure this setting, Windows refreshes platform validation data
in this situation.

If you disable this policy setting, Windows doesn't refresh platform validation data in
this situation.

For more information on how to create this policy with Windows PowerShell, see New-
CMTpmAutoResealPolicy.

Pre-boot recovery message and URL
Suggested configuration: Not configured

When BitLocker locks the OS drive, use this setting to display a custom recovery
message or a URL on the pre-boot BitLocker recovery screen. This setting only applies to
Windows 10 or later devices.

When you enable this setting, select one of the following options for the pre-boot
recovery message:

<!-- p.267 -->

     Use default recovery message and URL: Display the default BitLocker recovery
     message and URL in the pre-boot BitLocker recovery screen. If you previously
     configured a custom recovery message or URL, use this option to revert to the
     default message.

     Use custom recovery message: Include a custom message in the pre-boot
     BitLocker recovery screen.
        Custom recovery message option: Type the custom message to display. If you
        also want to specify a recovery URL, include it as part of this custom recovery
        message. The maximum string length is 32,768 characters.

     Use custom recovery URL: Replace the default URL displayed in the pre-boot
     BitLocker recovery screen.
        Custom recovery URL option: Type the URL to display. The maximum string
        length is 32,768 characters.

  ７ Note

  Not all characters and languages are supported in pre-boot. First test your custom
  message or URL to make sure it appears correctly on the pre-boot BitLocker
  recovery screen.

For more information on how to create this policy with Windows PowerShell, see New-
CMPrebootRecoveryInfo.

Encryption policy enforcement settings (OS drive)
Suggested configuration: Enabled

Configure the number of days that users can postpone BitLocker compliance for the OS
drive. The Noncompliance grace period begins when Configuration Manager first
detects it as noncompliant. After this grace period expires, users can't postpone the
required action or request an exemption.

If the encryption process requires user input, a dialog box appears in Windows that the
user can't close until they provide the required information. Future notifications for
errors or status won't have this restriction.

If BitLocker doesn't require user interaction to add a protector, after the grace period
expires, BitLocker starts encryption in the background.

<!-- p.268 -->

If you disable or don't configure this setting, Configuration Manager doesn't require
users to comply with BitLocker policies.

To enforce the policy immediately, set a grace period of 0 .

For more information on how to create this policy with Windows PowerShell, see New-
CMUseOsEnforcePolicy.

Fixed drive
The settings on this page configure encryption for other data drives in a device.

Fixed data drive encryption
Suggested configuration: Enabled

Manage your requirement for encryption of fixed data drives. If you enable this setting,
BitLocker requires users to put all fixed data drives under protection. It then encrypts the
data drives.

When you enable this policy, either enable auto-unlock or the settings for Fixed data
drive password policy.

     Configure auto-unlock for fixed data drive: Allow or require BitLocker to
     automatically unlock any encrypted data drive. To use auto-unlock, also require
     BitLocker to encrypt the OS drive.

If you don't configure this setting, BitLocker doesn't require users to put fixed data
drives under protection.

If you disable this setting, users can't put their fixed data drives under BitLocker
protection. If you disable this policy after BitLocker encrypts fixed data drives, BitLocker
decrypts the fixed data drives.

For more information on how to create this policy with Windows PowerShell, see New-
CMBMSFDVEncryptionPolicy.

Deny write access to fixed drives not protected by
BitLocker
Suggested configuration: Not configured

<!-- p.269 -->

Require BitLocker protection for Windows to write data to fixed drives on the device.
BitLocker applies this policy when you turn it on.

When you enable this setting:

     If BitLocker protects a fixed data drive, Windows mounts it with read and write
     access.

     For any fixed data drive that BitLocker doesn't protect, Windows mounts it as read-
     only.

When you don't configure this setting, Windows mounts all fixed data drives with read
and write access.

For more information on how to create this policy with Windows PowerShell, see New-
CMFDVDenyWriteAccessPolicy.

Fixed data drive password policy
Suggested configuration: Not configured

Use these settings to set the constraints for passwords to unlock BitLocker-protected
fixed data drives.

If you enable this setting, users can configure a password that meets your defined
requirements.

For higher security, enable this setting, and then configure the following settings:

     Require password for fixed data drive: Users have to specify a password to unlock
     a BitLocker-protected fixed data drive.

     Configure password complexity for fixed data drives: To enforce complexity
     requirements on the password, select Require password complexity.

     Minimum password length for fixed data drive: By default, the minimum length is
      8.

If you disable this setting, users can't configure a password.

When the policy isn't configured, BitLocker supports passwords with the default settings.
The default settings don't include password complexity requirements, and require only
eight characters.

For more information on how to create this policy with Windows PowerShell, see New-
CMFDVPassPhrasePolicy.

<!-- p.270 -->

General usage notes for fixed data drive password policy
     For these complexity requirement settings to be effective, also enable the group
     policy setting Password must meet complexity requirements in Computer
     Configuration > Windows Settings > Security Settings > Account Policies >
     Password Policy.

     BitLocker enforces these settings when you turn it on, not when you unlock a
     volume. BitLocker lets you unlock a drive with any of the protectors that are
     available on the drive.

     If you use group policy to enable FIPS-compliant algorithms for encryption,
     hashing, and signing, you can't allow passwords as a BitLocker protector.

Encryption policy enforcement settings (fixed data drive)
Suggested configuration: Enabled

Configure the number of days that users can postpone BitLocker compliance for fixed
data drives. The Noncompliance grace period begins when Configuration Manager first
detects the fixed data drive as noncompliant. It doesn't enforce the fixed data drive
policy until the OS drive is compliant. After the grace period expires, users can't
postpone the required action or request an exemption.

If the encryption process requires user input, a dialog box appears in Windows that the
user can't close until they provide the required information. Future notifications for
errors or status won't have this restriction.

If BitLocker doesn't require user interaction to add a protector, after the grace period
expires, BitLocker starts encryption in the background.

If you disable or don't configure this setting, Configuration Manager doesn't require
users to comply with BitLocker policies.

To enforce the policy immediately, set a grace period of 0 .

For more information on how to create this policy with Windows PowerShell, see New-
CMUseFddEnforcePolicy.

Removable drive
The settings on this page configure encryption for removable drives, such as USB keys.

<!-- p.271 -->

Removable data drive encryption
Suggested configuration: Enabled

This setting controls the use of BitLocker on removable drives.

     Allow users to apply BitLocker protection on removable data drives: Users can
     turn on BitLocker protection for a removable drive.

     Allow users to suspend and decrypt BitLocker on removable data drives: Users
     can remove or temporarily suspend BitLocker drive encryption from a removable
     drive.

When you enable this setting, and allow users to apply BitLocker protection, the
Configuration Manager client saves recovery information about removable drives to the
recovery service on the management point. This behavior allows users to recover the
drive if they forget or lose the protector (password).

When you enable this setting:

     Enable the settings for Removable data drive password policy

     Disable the following group policy settings in System > Removable Storage
     Access for both user & computer configurations:
        All removable storage classes: Deny all access
        Removable disks: Deny write access
        Removable disks: Deny read access

If you disable this setting, users can't use BitLocker on removable drives.

For more information on how to create this policy with Windows PowerShell, see New-
CMRDVConfigureBDEPolicy.

Deny write access to removable drives not protected by
BitLocker
Suggested configuration: Not configured

Require BitLocker protection for Windows to write data to removable drives on the
device. BitLocker applies this policy when you turn it on.

When you enable this setting:

     If BitLocker protects a removable drive, Windows mounts it with read and write
     access.

<!-- p.272 -->

     For any removable drive that BitLocker doesn't protect, Windows mounts it as
     read-only.

     If you enable the option to Deny write access to devices configured in another
     organization, BitLocker only gives write access to removable drives with
     identification fields that match the allowed identification fields. Define these fields
     with the Organization unique identifiers global settings on the Setup page.

When you disable or don't configure this setting, Windows mounts all removable drives
with read and write access.

  ７ Note

  You can override this setting with the group policy settings in System > Removable
  Storage Access. If you enable the group policy setting Removable disks: Deny
  write access, then BitLocker ignores this Configuration Manager setting.

For more information on how to create this policy with Windows PowerShell, see New-
CMRDVDenyWriteAccessPolicy.

Removable data drive password policy
Suggested configuration: Enabled

Use these settings to set the constraints for passwords to unlock BitLocker-protected
removable drives.

If you enable this setting, users can configure a password that meets your defined
requirements.

For higher security, enable this setting, and then configure the following settings:

     Require password for removable data drive: Users have to specify a password to
     unlock a BitLocker-protected removable drive.

     Configure password complexity for removable data drives: To enforce complexity
     requirements on the password, select Require password complexity.

     Minimum password length for removable data drive: By default, the minimum
     length is 8 .

If you disable this setting, users can't configure a password.

<!-- p.273 -->

When the policy isn't configured, BitLocker supports passwords with the default settings.
The default settings don't include password complexity requirements, and require only
eight characters.

For more information on how to create this policy with Windows PowerShell, see New-
CMRDVPassPhrasePolicy.

General usage notes for removable data drive password policy
     For these complexity requirement settings to be effective, also enable the group
     policy setting Password must meet complexity requirements in Computer
     Configuration > Windows Settings > Security Settings > Account Policies >
     Password Policy.

     BitLocker enforces these settings when you turn it on, not when you unlock a
     volume. BitLocker lets you unlock a drive with any of the protectors that are
     available on the drive.

     If you use group policy to enable FIPS-compliant algorithms for encryption,
     hashing, and signing, you can't allow passwords as a BitLocker protector.

Client management
The settings on this page configure BitLocker management services and clients.

BitLocker Management Services
Suggested configuration: Enabled

When you enable this setting, Configuration Manager automatically and silently backs
up key recovery information in the site database. If you disable or don't configure this
setting, Configuration Manager doesn't save key recovery information.

     Select BitLocker recovery information to store: Configure the key recovery service
     to back up BitLocker recovery information. It provides an administrative method of
     recovering data encrypted by BitLocker, which helps prevent data loss because of
     the lack of key information.

     Allow recovery information to be stored in plain text: Without a BitLocker
     management encryption certificate for SQL Server, Configuration Manager stores
     the key recovery information in plain text. For more information, see Encrypt
     recovery data in the database.

<!-- p.274 -->

     Client checking status frequency (minutes): At the configured frequency, the
     client checks the BitLocker protection policies and status on the computer and also
     backs up the client recovery key. By default, the Configuration Manager client
     checks BitLocker status every 90 minutes.

        ） Important

        Don't set this value to less than 60. A smaller frequency value may cause the
        client to briefly report inaccurate compliance states.

For more information on how to create these policies with Windows PowerShell, see:

     Set-CMBlmPlaintextStorage
     New-CMBMSClientConfigureCheckIntervalPolicy

User exemption policy
Suggested configuration: Not configured

Configure a contact method for users to request an exemption from BitLocker
encryption.

If you enable this policy setting, provide the following information:

     Maximum days to postpone: How many days the user can postpone an enforced
     policy. By default, this value is 7 days (one week).

     Contact method: Specify how users can request an exemption: URL, email address,
     or phone number.

     Contact: Specify the URL, email address, or phone number. When a user requests
     an exemption from BitLocker protection, they see a Windows dialog box with
     instructions on how to apply. Configuration Manager doesn't validate the
     information you enter.

        URL: Use the standard URL format, https://website.domain.tld . Windows
        displays the URL as a hyperlink.

        Email address: Use the standard email address format, user@domain.tld .
        Windows displays the address as the following hyperlink:
        mailto:user@domain.tld?subject=Request exemption from BitLocker protection .

<!-- p.275 -->

        Phone number: Specify the number you want your users to call. Windows
        displays the number with the following description: Please call <your number>
        for applying exemption .

If you disable or don't configure this setting, Windows doesn't display the exemption
request instructions to users.

   ７ Note

   BitLocker manages exemptions per user, not per computer. If multiple users sign in
   to the same computer, and any one user isn't exempt, BitLocker encrypts the
   computer.

For more information on how to create this policy with Windows PowerShell, see New-
CMBMSUserExemptionPolicy.

URL for the security policy link
Suggested configuration: Enabled

Specify a URL to display to users as the Company Security Policy in Windows. Use this
link to provide users with information about encryption requirements. It shows when
BitLocker prompts the user to encrypt a drive.

If you enable this setting, configure the security policy link URL.

If you disable or don't configure this setting, BitLocker doesn't show the security policy
link.

For more information on how to create this policy with Windows PowerShell, see New-
CMMoreInfoUrlPolicy.

Next steps
If you use Windows PowerShell to create these policy objects, then use the New-
CMBlmSetting cmdlet. This cmdlet creates a BitLocker management policy settings
object that contains all of the specified policies. To deploy the policy settings to a
collection, use the New-CMSettingDeployment cmdlet.

Feedback

<!-- p.276 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.277 -->

Troubleshoot BitLocker
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the information in this article to help you troubleshoot issues with BitLocker
management in Configuration Manager.

Server error in self-service
When trying to open the self-service portal
( https://webserver.contoso.com/SelfService ) for the first time, you see the following
error message:

  error

   Configuration Error - Server Error in '/SelfService' Application

   Description: An error occurred during the processing of a configuration file
   required to service this request. Please review the specific error details
   below and modify your configuration file appropriately.

   Parser Error Message: Could not load file or assembly 'System.Web.Mvc,
   Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of
   its dependencies. The system cannot find the file specified.

To fix this issue, make sure you installed the prerequisite for Microsoft ASP.NET MVC 4.0
on the web server.

See also
For more information about using BitLocker event logs, see BitLocker event logs.

For a list of known errors and possible causes for event log entries, see the following
articles:

      Client event logs
      Server event logs

To understand why clients are reporting not compliant with the BitLocker management
policy, see Non-compliance codes.

<!-- p.278 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.279 -->

BitLocker event logs
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The BitLocker management agent and web services use Windows event logs to record
messages. In the Event Viewer, go to Applications and Services Logs, Microsoft,
Windows. The log channel (node) varies depending upon the computer and the
component:

      MBAM: BitLocker management agent on a client computer
      MBAM-Web:
         Recovery service on the management point
         Self-service portal
         Administration and monitoring website

For more information about specific messages in these logs, see the following articles:

      Client event logs
      Server event logs

In each node, by default you'll see two log channels: Admin and Operational. For more
detailed troubleshooting information, you can also show analytics and debug logs.

Log properties
In Windows Event Viewer, select a specific log. For example, Admin. Go to the Action
menu, and select Properties. Configure the following settings:

      Maximum log size (KB): by default, this setting is 1028 (1 MB) for all logs.
      When maximum event log size is reached: by default, the Admin and Operational
      logs are set to Overwrite events as needed (oldest events first).

Analytic and debug logs
You can enable more detailed logs for troubleshooting purposes. In Event Viewer, go to
the View menu, and select Show Analytic and Debug Logs. Now when you browse to
the log channel, you'll see two additional logs: Analytic and Debug.

   Tip

<!-- p.280 -->

  By default, these logs have the following properties:

        Maximum log size (KB): 1028 (1 MB)
        Do not overwrite events (Clear logs manually)

Export logs to text
Especially with the analytic and debug logs, you may find it easier to review the logs
entries in a single text file. Use the following PowerShell commands to export the event
log entries to text files:

  PowerShell

  # Out-String with a larger -Width does a better job compared to using Out-
  File with -Width. -Oldest is only required with debug/analytic logs.

  # Debug log
  Get-WinEvent -LogName Microsoft-Windows-MBAM/Debug -Oldest | Format-Table -
  AutoSize | Out-String -Width 4096 | Out-File C:\Temp\MBAM_Log_Debug.txt

  # Analytic log
  Get-WinEvent -LogName Microsoft-Windows-MBAM/Analytic -Oldest | Format-Table
  -AutoSize | Out-String -Width 4096 | Out-File C:\Temp\MBAM_Log_Analytic.txt

  # Admin log
  # The above command truncates the output from the admin log, this sample
  reformats the strings
  Get-WinEvent -LogName Microsoft-Windows-MBAM/Admin |
      Select TimeCreated, LevelDisplayName, TaskDisplayName, @{n='Message';e=
  {$_.Message.trim()}} |
      Format-Table -AutoSize -Wrap | Out-String -Width 4096 |
      Out-File -FilePath C:\Temp\MBAM_Log_Admin.txt

Feedback
Was this page helpful?        Yes    No

Provide product feedback
