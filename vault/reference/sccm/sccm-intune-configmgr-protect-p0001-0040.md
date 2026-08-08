---
title: "Protect data and infrastructure documentation — pages 1-40"
type: reference
domain: sccm
slug: sccm-intune-configmgr-protect-p0001-0040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-protect-p0001-0040
family: sccm
documentKind: "doc"
abstract: "Tell us about your PDF experience. Protect data and infrastructure documentation Protect both your infrastructure and your data from exposure or malicious attack using Configuration Manager. Manage BitLocker Drive Encryption (BDE) ｂ GET STARTED Plan for BitLocker management ｀ DE"
---

# Protect data and infrastructure documentation — pages 1-40

<!-- p.1 -->

                                                                           Tell us about your PDF experience.

Protect data and infrastructure
documentation
Protect both your infrastructure and your data from exposure or malicious attack using
Configuration Manager.

  Manage BitLocker Drive Encryption (BDE)

  ｂ GET STARTED
  Plan for BitLocker management

  ｀ DEPLOY
  Deploy BitLocker management

  Set up BitLocker portals

  ｃ HOW-TO GUIDE
  View BitLocker reports

  Use the BitLocker administration and monitoring website

  Certificate profiles

  ｅ OVERVIEW
  Introduction to certificate profiles

  ｂ GET STARTED
  Planning for certificate template permissions for certificate profiles

  Prerequisites for certificate profiles

  ｀ DEPLOY
  Configure certificate infrastructure

  Create certificate profiles

<!-- p.2 -->

Deploy resource access profiles

Top tasks

ｃ HOW-TO GUIDE
Microsoft Defender for Endpoint onboarding

Troubleshoot Windows Defender or Endpoint Protection client

Manage antimalware policies and firewall settings

Windows Defender Application Control management

Create and deploy Windows Defender Application Guard

Windows Hello for Business settings

Endpoint Protection

ｅ OVERVIEW
Endpoint Protection overview

｀ DEPLOY
Create an Endpoint Protection point site system role

Configure alerts for Endpoint Protection

Configure definition updates for Endpoint Protection

ｃ HOW-TO GUIDE
Create and deploy antimalware policies for Endpoint Protection

Configure custom client settings for Endpoint Protection

Monitor Endpoint Protection status

<!-- p.3 -->

Protect data and site infrastructure
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

You want your users to securely access your organization's resources. Protect both your
infrastructure and your data from exposure or malicious attack. Use Configuration
Manager to enable access and help protect your organization's resources.

      Endpoint Protection lets you manage the following Microsoft Defender policies for
      client computers:
         Microsoft Defender Antimalware
         Microsoft Defender Firewall
         Microsoft Defender for Endpoint
         Microsoft Defender Exploit Guard
         Microsoft Defender Application Guard
         Microsoft Defender Application Control

         Tip

        To manage endpoint protection on co-managed Windows 10 or later devices
        using the Microsoft Intune cloud service, switch the Endpoint Protection
        workload to Intune. For more information, see Endpoint protection for
        Microsoft Intune.

      Protect data stored on on-premises Windows clients with BitLocker Drive
      Encryption (BDE). Configuration Manager provides full BitLocker lifecycle
      management that can replace the use of Microsoft BitLocker Administration and
      Monitoring (MBAM). For more information, see Plan for BitLocker management.

Use other components of Microsoft Intune to protect your devices. For more
information, see Protect devices with Microsoft Intune.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.4 -->

Endpoint Protection
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Endpoint Protection manages antimalware policies and Windows Defender Firewall
security for client computers in your Configuration Manager hierarchy.

When you use Endpoint Protection with Configuration Manager, you have the following
benefits:

      Configure antimalware policies, Windows Defender Firewall settings, and manage
      Microsoft Defender for Endpoint to selected groups of computers.
      Use Configuration Manager software updates to download the latest antimalware
      definition files to keep client computers up to date.
      Send email notifications, use in-console monitoring, and view reports. These
      actions inform administrative users when malware is detected on client computers.

Beginning with Windows 10 and Windows Server 2016 computers, Microsoft Defender
Antivirus is already installed. For these operating systems, a management client for
Microsoft Defender Antivirus is installed when the Configuration Manager client installs.
On Windows 8.1 and earlier computers, the Endpoint Protection client is installed with
the Configuration Manager client. Microsoft Defender Antivirus and the Endpoint
Protection client have the following capabilities:

      Malware and spyware detection and remediation
      Rootkit detection and remediation
      Critical vulnerability assessment and automatic definition and engine updates
      Network vulnerability detection through Network Inspection System
      Integration with Cloud Protection Service to report malware to Microsoft. When
      you join this service, the Endpoint Protection client or Microsoft Defender Antivirus
      downloads the latest definitions from the Malware Protection Center when
      unidentified malware is detected on a computer.

  ７ Note

  The Endpoint Protection client can be installed on a server that runs Hyper-V and
  on guest virtual machines with supported operating systems. To prevent excessive
  CPU usage, Endpoint Protection actions have a built-in randomized delay so that
  protection services do not run simultaneously.

<!-- p.5 -->

You can also manage Windows Defender Firewall settings with Endpoint Protection in
the Configuration Manager console.

Manage malware
Endpoint Protection in Configuration Manager allows you to create antimalware policies
that contain settings for Endpoint Protection client configurations. Deploy these
antimalware policies to client computers. Then monitor compliance in the Endpoint
Protection Status node under Security in the Monitoring workspace. Also use Endpoint
Protection reports in the Reporting node.

For more information, see the following articles:

      How to create and deploy antimalware policies: Create, deploy, and monitor
      antimalware policies with a list of the settings that you can configure.

      How to monitor Endpoint Protection: Monitoring activity reports, infected client
      computers, and more.

      How to manage antimalware policies and firewall settings: Remediate malware
      found on client computers.

      Log files for Endpoint Protection

Manage Windows Defender Firewall
Endpoint Protection in Configuration Manager provides basic management of the
Windows Defender Firewall on client computers. For each network profile, you can
configure the following settings:

      Enable or disable the Windows Defender Firewall.

      Block incoming connections, including connections in the list of allowed programs.

      Notify the user when Windows Defender Firewall blocks a new program.

  ７ Note

  Endpoint Protection supports managing the Windows Defender Firewall only.

For more information, see How to create and deploy Windows Defender Firewall
policies.

<!-- p.6 -->

Microsoft Defender for Endpoint
Configuration Manager manages and monitors Microsoft Defender for Endpoint,
formerly known as Windows Defender for Endpoint. The Microsoft Defender for
Endpoint service helps you detect, investigate, and respond to advanced attacks on your
network. For more information, see Microsoft Defender for Endpoints.

Endpoint Protection workflow
Use the following diagram to help you understand the workflow to implement Endpoint
Protection in your Configuration Manager hierarchy.

<!-- p.7 -->

Recommendations
Use the following recommendations for Endpoint Protection in Configuration Manager.

Configure custom client settings
When you configure client settings for Endpoint Protection, don't use the default client
settings. The defaults apply settings to all computers in your hierarchy. Instead,
configure custom client settings and assign these settings to collections of computers in
your hierarchy.

<!-- p.8 -->

When you configure custom client settings, you can do the following:

     Customize antimalware and security settings for different parts of your
     organization.
     Test the effects of running Endpoint Protection on a small group of computers
     before you deploy it to the entire hierarchy.
     Add more clients to the collection over time to phase your deployment of the
     Endpoint Protection settings.

Distributing definition updates by using software updates
If you use Configuration Manager software updates to distribute definition updates, put
definition updates in a package that doesn't include other software updates. This
practice keeps the size of the definition update package smaller which allows it to
replicate to distribution points more quickly.

Next steps
Example scenario: Using Endpoint Protection to protect computers from malware

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.9 -->

Plan for BitLocker management
Article • 12/04/2024

Applies to: Configuration Manager (current branch)

Use Configuration Manager to manage BitLocker Drive Encryption (BDE) for on-
premises Windows clients, which are joined to Active Directory. It provides full BitLocker
lifecycle management that can replace the use of Microsoft BitLocker Administration
and Monitoring (MBAM).

  ７ Note

  Configuration Manager doesn't enable this optional feature by default. You must
  enable this feature before using it. For more information, see Enable optional
  features from updates.

For more general information about BitLocker, see BitLocker overview. For a comparison
of BitLocker deployments and requirements, see the BitLocker deployment comparison
chart.

   Tip

  To manage encryption on co-managed Windows 10 or later devices using the
  Microsoft Intune cloud service, switch the Endpoint Protection workload to Intune.
  For more information on using Intune, see Windows Encryption.

Features
Configuration Manager provides the following management capabilities for BitLocker
Drive Encryption:

Client deployment
      Deploy the BitLocker client to managed Windows devices running Windows 8.1,
      Windows 10 or Windows 11.

      Manage BitLocker policies and escrow recovery keys for on-premises and internet-
      based clients

<!-- p.10 -->

Manage encryption policies
     For example: choose drive encryption and cipher strength, configure user
     exemption policy, fixed data drive encryption settings.

     Determine the algorithms with which to encrypt the device, and the disks that you
     target for encryption.

     Force users to get compliant with new security policies before using the device.

     Customize your organization's security profile on a per device basis.

     When a user unlocks the OS drive, specify whether to unlock only an OS drive or all
     attached drives.

Compliance reports
Built-in reports for:

     Encryption status per volume or per device
     The primary user of the device
     Compliance status
     Reasons for non-compliance

Administration and monitoring website
Allow other personas in your organization outside of the Configuration Manager
console to help with key recovery, including key rotation and other BitLocker-related
support. For example, help desk administrators can help users with key recovery.

   Tip

  Starting in version 2107, you can also get BitLocker recovery keys for a tenant-
  attached device from the Microsoft Intune admin center. For more information, see
  Tenant attach: BitLocker recovery keys.

User self-service portal
Let users help themselves with a single-use key for unlocking a BitLocker encrypted
device. Once this key is used, it generates a new key for the device.

<!-- p.11 -->

Prerequisites

General prerequisites
     To create a BitLocker management policy, you need the Full Administrator role in
     Configuration Manager.

     To use the BitLocker management reports, install the reporting services point site
     system role. For more information, see Configure reporting.

       ７ Note

       For the Recovery Audit Report to work from the administration and
       monitoring website, only use a reporting services point at the primary site.

Prerequisites for clients
     The device requires a TPM chip that's enabled in the BIOS and is resettable from
     Windows.

     Microsoft recommends devices with TPM version 2.0 or later. Devices with TPM
     version 1.2 may not properly support all BitLocker functionality.

     The computer's hard disk requires a BIOS that's compatible with TPM and that
     supports USB devices during computer startup.

  ７ Note

  Uploading of the TPM password hash mainly pertains to versions of Windows
  before Windows 10. Windows 10 or later by default doesn't save the TPM password
  hash, so these devices don't normally upload it. For more information, see About
  the TPM owner password.

BitLocker management doesn't support all client types that are supported by
Configuration Manager. For more information, see Supported configurations.

Prerequisites for the recovery service
     In version 2010 and earlier, the BitLocker recovery service requires HTTPS to
     encrypt the recovery keys across the network from the Configuration Manager

<!-- p.12 -->

   client to the management point. Use one of the following options:

      HTTPS-enable the IIS website on the management point that hosts the recovery
      service.

      Configure the management point for HTTPS.

   For more information, see Encrypt recovery data over the network.

     ７ Note

     When both the site and clients are running Configuration Manager version
     2103 or later, clients send their recovery keys to the management point over
     the secure client notification channel. If any clients are on version 2010 or
     earlier, they need an HTTPS-enabled recovery service on the management
     point to escrow their keys.

     Starting in version 2103, since clients use the secure client notification channel
     to escrow keys, you can enable the Configuration Manager site for enhanced
     HTTP. This configuration doesn't affect the functionality of BitLocker
     management in Configuration Manager.

   In version 2010 and earlier, to use the recovery service, you need at least one
   management point not in a replica configuration. Although the BitLocker recovery
   service installs on a management point that uses a database replica, clients can't
   escrow recovery keys. Then BitLocker won't encrypt the drive. Disable the BitLocker
   recovery service on any management point with a database replica.

   Starting in version 2103, the recovery service supports management points that
   use a database replica.

Prerequisites for BitLocker portals
   To use the self-service portal or the administration and monitoring website, you
   need a Windows server running IIS. You can reuse a Configuration Manager site
   system, or use a standalone web server that has connectivity to the site database
   server. Use a supported OS version for site system servers.

   On the web server that will host the self-service portal, install Microsoft ASP.NET
   MVC 4.0 and .NET Framework 3.5 feature before staring the install process. Other
   required Windows server roles and features will be installed automatically during
   the portal installation process.

<!-- p.13 -->

     Tip

    You don't need to install any version of Visual Studio with ASP.NET MVC.

  The user account that runs the portal installer script needs SQL Server sysadmin
  rights on the site database server. During the setup process, the script sets login,
  user, and SQL Server role rights for the web server machine account. You can
  remove this user account from the sysadmin role after you complete setup of the
  self-service portal and the administration and monitoring website.

Supported configurations
  BitLocker management isn't supported on virtual machines (VMs) or on server
  editions. For example, BitLocker management won't start the encryption on fixed
  drives of virtual machines. Additionally fixed drives in virtual machines may show
  as compliant even though they aren't encrypted.

  Starting in version 2409, Configuration Manager now supports BitLocker task
  sequence steps for ARM devices. In BitLocker Management, policies that include
  OS drive encryption with a TPM protector and Fixed drive encryption with the
  Auto-Unlock option are now compatible with ARM devices.

  In version 2010 and earlier, Microsoft Entra joined, workgroup clients, or clients in
  untrusted domains aren't supported. In these earlier versions of Configuration
  Manager, BitLocker management only supports devices that are joined to on-
  premises Active Directory including Microsoft Entra hybrid joined devices. This
  configuration is to authenticate with the recovery service to escrow keys.

  Starting in version 2103, Configuration Manager supports all client join types for
  BitLocker management. However, the client-side BitLocker user interface
  component is still only supported on Active Directory-joined and Microsoft Entra
  hybrid joined devices.

  Starting in version 2010, you can now manage BitLocker policies and escrow
  recovery keys over a cloud management gateway (CMG). This change also
  provides support for BitLocker management via internet-based client management
  (IBCM). There's no change to the setup process for BitLocker management. This
  improvement supports domain-joined and hybrid domain-joined devices. For
  more information, see Deploy management agent: Recovery service.
    If you have BitLocker management policies that you created before you
    updated to version 2010, to make them available to internet-based clients via

<!-- p.14 -->

        CMG:

            1. In the Configuration Manager console, open the properties of the existing
              policy.
            2. Switch to the Client Management tab.
            3. Select OK or Apply to save the policy. This action revises the policy so that
              it's available to clients over the CMG.

     By default, the Enable BitLocker task sequence step only encrypts used space on
     the drive. BitLocker management uses full disk encryption. Configure this task
     sequence step to enable the option to Use full disk encryption.

     Starting in version 2203, you can configure this task sequence step to escrow the
     BitLocker recovery information for the OS volume to Configuration Manager.

     For more information, see Task sequence steps - Enable BitLocker.

  ） Important

  The Invoke-MbamClientDeployment.ps1 PowerShell script is for stand-alone MBAM
  only. It should not be used with Configuration Manager BitLocker Management.

Next steps
Encrypt recovery data over the network

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.15 -->

Prerequisites for certificate profiles in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Certificate profiles in Configuration Manager have external dependencies and
dependencies in the product.

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

Dependencies External to Configuration
Manager
                                                                                   ﾉ   Expand table

 Dependency                  More information

 An enterprise issuing       For more information about Active Directory Certificate Services, see
 certification authority     Active Directory Certificate Services Overview.
 (CA) that is running
 Active Directory
 Certificate Services (AD
 CS).

 To revoke certificates
 the computer account
 of the site server at the
 top of the hierarchy
 requires Issue and
 Manage Certificates
 rights for each
 certificate template
 used by a certificate
 profile in Configuration
 Manager. Alternatively,
 grant Certificate
 Manager permissions

<!-- p.16 -->

Dependency                  More information

to grant permissions on
all certificate templates
used by that CA

Manager approval for
certificate requests is
supported. However,
the certificate
templates that are used
to issue certificates
must be configured for
Supply in the request
for the certificate
subject so that
Configuration Manager
can automatically
supply this value.

Use the PowerShell          The instruction file, readme_crp.txt, is located in
script to verify, and if    ConfigMgrInstallDir\cd.latest\SMSSETUP\POLICYMODULE\X64.
needed, install the
prerequisites for the       The PowerShell script, Test-NDES-CRP-Prereqs.ps1, is in the same
Network Device              directory as the instructions.
Enrollment Service
(NDES) role service and     The PowerShell script must be run locally on the NDES server.
the Configuration
Manager Certificate
Registration Point.

The Network Device          Configuration Manager communicates with the Network Device
Enrollment Service          Enrollment Service in Windows Server 2012 R2 to generate and verify
(NDES) role service for     Simple Certificate Enrollment Protocol (SCEP) requests.
Active Directory
Certificate Services,       If you will issue certificates to users or devices that connect from the
running on Windows          Internet, such as mobile devices that are managed by Microsoft Intune,
Server 2012 R2.             those devices must be able to access the server that runs the Network
                            Device Enrollment Service from the Internet. For example, install the
In addition:                server in a perimeter network (also known as a DMZ, demilitarized
                            zone, and screened subnet).
Port numbers other
than TCP 443 (for           If you have a firewall between the server that is running the Network
HTTPS) or TCP 80 (for       Device Enrollment Service and the issuing CA, you must configure the
HTTP) are not               firewall to allow the communication traffic (DCOM) between the two
supported for the           servers. This firewall requirement also applies to the server running the
communication               Configuration Manager site server and the issuing CA, so that
between the client and      Configuration Manager can revoke certificates.
the Network Device

<!-- p.17 -->

Dependency                  More information

Enrollment Service.         If the Network Device Enrollment Service is configured to require SSL, a
                            security best practice is to make sure that connecting devices can
The server that is          access the certificate revocation list (CRL) to validate the server
running the Network         certificate.
Device Enrollment
Service must be on a        For more information about the Network Device Enrollment Service,
different server from       see Using a Policy Module with the Network Device Enrollment Service.
the issuing CA.

A PKI client                This certificate authenticates the server that is running the Network
authentication              Device Enrollment Service to Configuration Manager.
certificate and exported
root CA certificate.        For more information, see PKI certificate requirements for
                            Configuration Manager.

Supported device            You can deploy certificate profiles to devices that run Windows 8.1,
operating systems.          Windows RT 8.1, and Windows 10.

Configuration Manager Dependencies
                                                                                     ﾉ   Expand table

Dependency                                   More information

Certificate registration point site system   Before you can use certificate profiles, you must install
role                                         the certificate registration point site system role. This
                                             role communicates with the Configuration Manager
                                             database, the Configuration Manager site server, and
                                             the Configuration Manager Policy Module.

                                             For more information about system requirements for
                                             this site system role and where to install the role in the
                                             hierarchy, see the Site System Requirements section in
                                             the Supported configurations for Configuration
                                             Manager article.

                                             The certificate registration point must not be installed
                                             on the same server that runs the Network Device
                                             Enrollment Service.

Configuration Manager Policy Module          To deploy certificate profiles, you must install the
that is installed on the server that is      Configuration Manager Policy Module. You can find this
running the Network Device Enrollment        policy module on the Configuration Manager
Service role service for Active Directory    installation media.
Certificate Services

<!-- p.18 -->

Dependency                                More information

Discovery data                            Values for the certificate subject and the subject
                                          alternative name are supplied by Configuration
                                          Manager and retrieved from information that is
                                          collected from discovery:

                                          For user certificates: Active Directory User Discovery

                                          For computer certificates: Active Directory System
                                          Discovery and Network Discovery

Specific security permissions to manage   You must have the following security permissions to
certificate profiles                      manage company resource access settings, such as
                                          certificate profiles, Wi-Fi profiles, and VPN profiles:

                                          To view and manage alerts and reports for certificate
                                          profiles: Create, Delete, Modify, Modify Report, Read,
                                          and Run Report for the Alerts object.

                                          To create and manage certificate profiles: Author
                                          Policy, Modify Report, Read, and Run Report for the
                                          Certificate Profile object.

                                          To manage Wi-Fi, certificate and VPN profile
                                          deployments: Deploy Configuration Policies, Modify
                                          Client Status Alert, Read, and Read Resource for the
                                          Collection object.

                                          To manage all configuration policies: Create, Delete,
                                          Modify, Read, and Set Security Scope for the
                                          Configuration Policy object.

                                          To run queries related to certificate profiles: Read
                                          permission for the Query object.

                                          To view certificate profiles information in the
                                          Configuration Manager console: Read permission for
                                          the Site object.

                                          To view status messages for certificate profiles: Read
                                          permission for the Status Messages object.

                                          To create and modify the Trusted CA certificate profile:
                                          Author Policy, Modify Report, Read, and Run Report
                                          for the Trusted CA Certificate Profile object.

                                          To create and manage VPN profiles: Author Policy,
                                          Modify Report, Read, and Run Report for the VPN

<!-- p.19 -->

 Dependency                               More information

                                          Profile object.

                                          To create and manage Wi-Fi profiles: Author Policy,
                                          Modify Report, Read, and Run Report for the Wi-Fi
                                          Profile object.

                                          The Company Resource Access Manager security role
                                          includes these permissions that are required to manage
                                          certificate profiles in Configuration Manager. For more
                                          information, see the Configure role-based
                                          administration section in the Configure security article.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.20 -->

Planning for certificate template permissions
for certificate profiles in Configuration
Manager
Article • 01/12/2024

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer supported. For more
  information, see Frequently asked questions about resource access deprecation.

The following information can help you plan for how to configure permissions for the certificate templates
that Configuration Manager uses when you deploy certificate profiles.

Default Security Permissions and Considerations
The default security permissions that are required for the certificate templates that Configuration Manager will
use to request certificates for users and devices are as follows:

      Read and Enroll for the account that the Network Device Enrollment Service application pool uses

      Read for the account that runs the Configuration Manager console

      For more information about these security permissions, see Configuring certificate infrastructure.

      When you use this default configuration, users and devices can't directly request certificates from the
      certificate templates and all requests must be initiated by the Network Device Enrollment Service. This is
      an important restriction, because these certificate templates must be configured with Supply in the
      request for the certificate Subject, which means that there is a risk of impersonation if a rogue user or a
      compromised device requests a certificate. In the default configuration, the Network Device Enrollment
      Service must initiate such a request. However, this risk of impersonation remains if the service that runs
      the Network Device Enrollment Service is compromised. To help avoid this risk, follow all security best
      practices for the Network Device Enrollment Service and the computer that runs this role service.

      If the default security permissions don't fulfill your business requirements, you have another option for
      configuring the security permissions on the certificate templates: You can add Read and Enroll
      permissions for users and computers.

Adding Read and Enroll Permissions for Users and
Computers
Adding Read and Enroll permissions for users and computers might be appropriate if a separate team
manages your certification authority (CA) infrastructure team, and that separate team wants Configuration
Manager to verify that users have a valid Active Directory Domain Services account before sending them a
certificate profile to request a user certificate. For this configuration, you must specify one or more security

<!-- p.21 -->

groups that contain the users, and then grant those groups Read and Enroll permissions on the certificate
templates. In this scenario, the CA administrator manages the security control.

You can similarly specify one or more security groups that contain computer accounts and grant these groups
Read and Enroll permissions on the certificate templates. If you deploy a computer certificate profile to a
computer that is a domain member, the computer account of that computer must be granted Read and Enroll
permissions. These permissions aren't required if the computer isn't a domain member. For example, if it's a
workgroup computer or personal mobile device.

Although this configuration uses another security control, we don't recommend it as a best practice. The
reason is that the specified users or owners of the devices might request certificates independently from
Configuration Manager and supply values for the certificate Subject that might be used to impersonate
another user or device.

In addition, if you specify accounts that can't be authenticated at the time that the certificate request occurs,
the certificate request will fail by default. For example, the certificate request will fail if the server that is
running the Network Device Enrollment Service is in an Active Directory forest that is untrusted by the forest
that contains the certificate registration point site system server. You can configure the certificate registration
point to continue if an account can't be authenticated because there's no response from a domain controller.
However, this isn't a security best practice.

If the certificate registration point is configured to check for account permissions and a domain controller is
available and rejects the authentication request (for example, the account is locked out or has been deleted),
the certificate enrollment request will fail.

To check for Read and Enroll permissions for users and domain-member
computers
   1. On the site system server that hosts the certificate registration point, create the following DWORD
     registry key to have a value of 0:
     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SCCM\CRP\SkipTemplateCheck

   2. If an account can't be authenticated because there's no response from a domain controller, and you
     want to bypass the permissions check:

           On the site system server that hosts the certificate registration point, create the following DWORD
           registry key to have a value of 1:
           HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SCCM\CRP\SkipTemplateCheckOnlyIfAccountAccessDenied

   3. On the issuing CA, on the Security tab in the properties for the certificate template, add one or more
     security groups to grant the user or device accounts Read and Enroll permissions.

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.22 -->

Prerequisites for Wi-Fi and VPN profiles
in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

Wi-Fi and VPN profiles in Configuration Manager have dependencies only within the
product.

You need the following security permissions to manage company resource access
settings, such as certificate profiles, Wi-Fi profiles, and VPN profiles:

      To view and manage alerts and reports for Wi-Fi and profiles: Create, Delete,
      Modify, Modify Report, Read, and Run Report for the Alerts object.

      To create and manage certificate profiles: Author Policy, Modify Report, Read, and
      Run Report for the Certificate Profile object.

      To manage Wi-Fi, certificate, and VPN profile deployments: Deploy Configuration
      Policies, Modify Client Status Alert, Read, and Read Resource for the Collection
      object.

      To manage all configuration policies: Create, Delete, Modify, Read, and Set
      Security Scope for the Configuration Policy object.

      To run queries that are related to Wi-Fi and VPN profiles: Read permission for the
      Query object.

      To view Wi-Fi and VPN profiles information in the Configuration Manager console:
      Read permission for the Site object.

      To view status messages for Wi-Fi and VPN profiles: Read permission for the Status
      Messages object.

      To create and modify the Trusted CA certificate profile: Author Policy, Modify
      Report, Read, and Run Report for the Trusted CA Certificate Profile object.

<!-- p.23 -->

     To create and manage VPN profiles: Author Policy, Modify Report, Read, and Run
     Report for the VPN Profile object.

     To create and manage Wi-Fi profiles: Author Policy, Modify Report, Read, and Run
     Report for the Wi-Fi Profile object.

The Company Resource Access Manager built-in security role includes these
permissions that are required to manage Wi-Fi profiles in Configuration Manager. For
more information, see Configure security.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.24 -->

Security and privacy for Wi-Fi and VPN
profiles in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

Security recommendations
Use the following security best practices when you manage Wi-Fi and VPN profiles for
devices.

Choose the most secure options that your Wi-Fi and VPN
infrastructure and client operating systems can support
Wi-Fi and VPN profiles provide a convenient method to centrally distribute and manage
Wi-Fi and VPN settings that your devices already support. Configuration Manager
doesn't add Wi-Fi or VPN functionality. Identify, implement, and follow any security
recommendations for your devices and infrastructure.

Privacy information
You can use Wi-Fi and VPN profiles to configure client devices to connect to Wi-Fi and
VPN servers. Then use Configuration Manager to evaluate whether those devices
become compliant after the profiles are applied. The management point sends
compliance information to the site server, and the information is stored in the site
database. The information is encrypted when devices send it to the management point,
but it isn't stored in encrypted format in the site database. The database retains the
information until the site maintenance task Delete Aged Configuration Management
Data deletes it. The default deletion interval is 90 days, but you can change it.
Compliance information isn't sent to Microsoft.

<!-- p.25 -->

By default, devices don't evaluate Wi-Fi and VPN profiles. In addition, you must
configure the profiles, and then deploy them to users.

Before you configure Wi-Fi or VPN profiles, consider your privacy requirements.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.26 -->

Security and privacy for certificate
profiles in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

Security guidance
Use the following guidance when you manage certificate profiles for users and devices.

Follow security guidance for the Network Device
Enrollment Service (NDES)
Identify and follow any security guidance for NDES. For example, configure the NDES
website in Internet Information Services (IIS) to require HTTPS and ignore client
certificates.

For more information, see Network Device Enrollment Service Guidance.

Choose the most secure options for certificate profiles
When you configure SCEP certificate profiles, choose the most secure options that
devices and your infrastructure can support. Identify, implement, and follow any security
guidance that's recommended for your devices and infrastructure.

Centrally specify user device affinity
Manually specify user device affinity instead of allowing users to identify their primary
device. Don't enable usage-based configuration.

If you use the option in a SCEP certificate profile to Allow certificate enrollment only on
the users primary device, don't consider the information that's collected from users or

<!-- p.27 -->

from the device to be authoritative. If you deploy SCEP certificate profiles with this
configuration, and a trusted administrative user doesn't specify user device affinity,
unauthorized users might receive elevated privileges and be granted certificates for
authentication.

  ７ Note

  If you do enable usage-based configuration, this information is collected by using
  state messages. Configuration Manager doesn't secure state messages. To help
  mitigate this threat, use SMB signing or IPsec between client computers and the
  management point.

Manage certificate template permissions
Don't add Read and Enroll permissions for users to the certificate templates. Don't
configure the certificate registration point to skip the certificate template check.

Configuration Manager supports the extra check if you add the security permissions of
Read and Enroll for users. If authentication isn't possible, you can configure the
certificate registration point to skip this check. But neither configuration is
recommended.

For more information, see Planning for certificate template permissions for certificate
profiles.

Privacy information
You can use certificate profiles to deploy root certification authority (CA) and client
certificates, and then evaluate whether those devices become compliant after the client
applies the profiles. The management point sends compliance information to the site
server, and Configuration Manager stores that information in the site database.
Compliance information includes certificate properties such as subject name and
thumbprint. The client encrypts this information when sent to the management point,
but the site database doesn't store it in an encrypted format. Compliance information
isn't sent to Microsoft.

Certificate profiles use information that Configuration Manager collects using discovery.
For more information, see Privacy information for discovery.

By default, devices don't evaluate certificate profiles. You need to configure the
certificate profiles, and then deploy them to users or devices.

<!-- p.28 -->

  ７ Note

  Certificates that are issued to users or devices might allow access to confidential
  information.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.29 -->

Frequently asked questions about resource
access deprecation
Applies to: Configuration Manager (current branch)

Starting in Configuration Manager version 2103, the following company resource access
features are deprecated:

     Certificate profiles, including the certificate registration point site system role
     VPN profiles
     Wi-Fi profiles
     Windows Hello for Business settings
     Email profiles
     The co-management resource access workload

  ） Important

  If above mentioned resource access profiles are configured in Intune, but the applicability
  to co-managed devices are controlled through the co-management Resource Access
  workload setting in Configuration Manager, post 2403 upgrade, the Resource Access
  workload is moved to Intune and hence all resource access profiles configured in Intune
  are now applicable and enforced to co-managed devices.

This article answers your frequently asked questions about these deprecated features.

What happens when you upgrade to CM
2403?
When you upgrade your Configuration Manager site to 2403, the prerequisite checker displays
an error. This blocks upgrade.

Action required by customer: Delete all Resource Access profiles and associated deployments
and move the co-management workload for Resource Access (if co-managed) to Intune.
Reevaluate the prerequisite rules, which allows you to proceed with upgrade.

<!-- p.30 -->

After the upgrade completion, if the cloud attach wizard is configured, the Resource Access
workload (configured to Intune) remains greyed out in console. If the customer isn't previously
cloud attached and configures the cloud attach wizard, during or after upgrade, the Resource
Access workload is defaulted to Intune and remains greyed out in the console. Company
Resource Access node in Asset Management workspace will be removed.

When will these features removed from
Configuration Manager?
Starting in version 2203, these features will still be available in Configuration Manager, but no
longer tested or supported. When you upgrade to version 2203, the prerequisite checker
displays a warning.

In version 2207, the creation of new company resource access profiles including the certificate
registration point site system role is disabled. Set/New/Import type PowerShell cmdlets for
Resource Access features are deprecated as well.

These features will be removed in 2403.

If I'm still using these features, can I upgrade
to version 2207?
Yes. If the site has any of these policies, the 2207 prerequisite checker will display a warning.
Before you upgrade to version 2211, replace the functionality of these features, and remove
the policies from the site.

If the site has the certificate registration point site system role, you also need to remove it. For
more information, see Remove a site system role.

What functionality is available to replace
these features?
Use Microsoft Intune to deploy resource access profiles. For more information, see Apply
features and settings on your devices using device profiles in Microsoft Intune.

Use co-management to enroll Configuration Manager clients to Intune.

<!-- p.31 -->

What do I do if I'm deploying wi-fi profiles
with Configuration Manager?
Before you upgrade to Configuration Manager version 2203, enable co-management, and
deploy the same wi-fi profiles with Intune. For more information, see Add and use Wi-Fi
settings on your devices in Microsoft Intune. If you don't take action, the existing wi-fi profiles
will persist on devices but are unmanaged.

What happens if I don't enable co-
management?
If you currently use these features, they're not tested or supported in version 2203. When you
upgrade to version 2207, they'll cause warning prerequisite checks. You can't create new wi-fi,
VPN, Windows Hello for Business, or certificate (SCEP, PFX, or root CA) profiles for
Configuration Manager clients. Any existing deployed profiles won't be removed from devices
and will continue to function. These existing profiles are unmanaged. For example, when a
certificate expires, Configuration Manager won't renew it.

What happens if I've enabled co-
management, but haven't switched the
resource access workload?
Starting in version 2211, the prerequisite checker will display a warning for co-managed clients
if the resource access workload is on Configuration Manager. If the resource access slider is
towards Configuration Manager, they aren't tested or supported in version 2203. Co-
management behavior is the same as if you used Configuration Manager 2111 or earlier to
switch the resource access workload to Intune. This Workload slider will be disabled, and you
can only use Microsoft Intune to deploy resource access profiles in upcoming Configuration
Manager versions.

What alternative options are available?
Configuration Manager version 2111 fully supports these features and is supported until June
2023. For more information, see Supported versions.

<!-- p.32 -->

Configure Endpoint Protection
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before you can use Endpoint Protection to manage security and malware on
Configuration Manager client computers, you must perform the configuration steps
detailed in this article.

How to Configure Endpoint Protection in
Configuration Manager
Endpoint Protection in Configuration Manager has external dependencies and
dependencies in the product.

Steps to Configure Endpoint Protection in Configuration
Manager
Use the following table for the steps, details, and more information about how to
configure Endpoint Protection.

  ） Important

  If you manage endpoint protection for Windows 10 or later computers, then you
  must configure Configuration Manager to update and distribute malware
  definitions for Windows Defender. Windows Defender is included in Windows 10
  and later but custom client settings for Endpoint Protection (Step 5 below) are still
  required.

                                                                                 ﾉ   Expand table

 Steps                        Details

 Step 1: Create an Endpoint   The Endpoint Protection point site system role must be installed
 Protection point site        before you can use Endpoint Protection. It must be installed on one
 system role                  site system server only, and it must be installed at the top of the
                              hierarchy on a central administration site or a stand-alone primary
                              site.

<!-- p.33 -->

 Steps                         Details

 Step 2: Configure alerts      Alerts inform the administrator when specific events have occurred,
 for Endpoint Protection       such as a malware infection. Alerts are displayed in the Alerts node
                               of the Monitoring workspace, or optionally can be emailed to
                               specified users.

 Step 3: Configure             Endpoint Protection can be configured to use various sources to
 definition update sources     download definition updates.
 for Endpoint Protection
 clients

 Step 4: Configure the         The default antimalware policy is applied when the Endpoint
 default antimalware policy    Protection client is installed. Any custom policies you have deployed
 and create custom             are applied by default, within 60 minutes of deploying the client.
 antimalware policies          Ensure that you have configured antimalware policies before you
                               deploy the Endpoint Protection client.

 Step 5: Configure custom      Use custom client settings to configure Endpoint Protection settings
 client settings for           for collections of computers in your hierarchy.
 Endpoint Protection
                               Note: Do not configure the default Endpoint Protection client
                               settings unless you are sure that you want these settings applied to
                               all computers in your hierarchy.

Feedback
Was this page helpful?       Yes     No

Provide product feedback

<!-- p.34 -->

Create an Endpoint Protection point site
system role
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Endpoint Protection point site system role must be installed before you can use
Endpoint Protection. It must be installed on one site system server only, and it must be
installed at the top of the hierarchy on a central administration site or a stand-alone
primary site.

Use one of the following procedures depending on whether you want to install a new
site system server for Endpoint Protection or use an existing site system server:

      Install on a new site system server
      Install on an existing site system server

  ） Important

  When you install an Endpoint Protection point, an Endpoint Protection client is
  installed on the server hosting the Endpoint Protection point. Services and scans
  are disabled on this client to enable it to co-exist with any existing antimalware
  solution that is installed on the server. If you later enable this server for
  management by Endpoint Protection and select the option to remove any third-
  party antimalware solution, the third-party product will not be removed. You must
  uninstall this product manually.

Prerequisites
The endpoint protection point requires the following Windows Server features:

      .NET Framework 3.5

      Windows Defender feature (Windows Server 2016)

      Windows Defender Antivirus feature (Windows Server 2019)

      Microsoft Defender Antivirus feature (Windows Server 2022 or later)

For more information, see Site and site system prerequisites.

<!-- p.35 -->

New site system server
 1. In the Configuration Manager console, click Administration.

 2. In the Administration workspace, expand Site Configuration, and then click
   Servers and Site System Roles.

 3. On the Home tab, in the Create group, click Create Site System Server.

 4. On the General page, specify the general settings for the site system, and then
   click Next.

 5. On the System Role Selection page, select Endpoint Protection point in the list of
   available roles, and then click Next.

 6. On the Endpoint Protection page, select the I accept the Endpoint Protection
   license terms check box, and then click Next.

     ） Important

     You cannot use Endpoint Protection in Configuration Manager unless you
     accept the license terms.

 7. On the Cloud Protection Service page, select the level of information that you
   want to send to Microsoft to help develop new definitions, and then click Next.

     ７ Note

     This option configures the Cloud Protection Service (formerly known as
     Microsoft Active Protection Service or MAPS) settings that are used by default.
     You can then configure custom settings for each antimalware policy you
     create. Join Cloud Protection Service, to help to keep your computers more
     secure by supplying Microsoft with malware samples that can help Microsoft
     to keep antimalware definitions more up-to-date. Additionally, when you join
     Cloud Protection Service, the Endpoint Protection client can use the dynamic
     signature service to download new definitions before they are published to
     Windows Update. For more information, see How to create and deploy
     antimalware policies for Endpoint Protection.

 8. Complete the wizard.

<!-- p.36 -->

Existing site system server
   1. In the Configuration Manager console, click Administration.

   2. In the Administration workspace, expand Site Configuration, click Servers and
     Site System Roles, and then select the server that you want to use for Endpoint
     Protection.

   3. On the Home tab, in the Server group, click Add Site System Roles.

   4. On the General page, specify the general settings for the site system, and then
     click Next.

   5. On the System Role Selection page, select Endpoint Protection point in the list of
     available roles, and then click Next.

   6. On the Endpoint Protection page, select the I accept the Endpoint Protection
     license terms check box, and then click Next.

        ） Important

        You cannot use Endpoint Protection in Configuration Manager unless you
        accept the license terms.

   7. On the Cloud Protection Service page, select the level of information that you
     want to send to Microsoft to help develop new definitions, and then click Next.

        ７ Note

        This option configures the Cloud Protection Service settings (formerly known
        as MAPS) that are used by default. You can configure custom settings for each
        antimalware policy you configure. For more information, see How to create
        and deploy antimalware policies for Endpoint Protection.

   8. Complete the wizard.

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.37 -->

Configure Alerts for Endpoint Protection
in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can configure Endpoint Protection alerts in Microsoft Configuration Manager to
notify administrative users when specific events, such as a malware infection, occur in
your hierarchy. Notifications display in the Endpoint Protection dashboard in the
Configuration Manager console in the Alerts node of the Monitoring workspace, or can
be emailed to specified users.

Use the following steps and the supplemental procedures in this topic to configure
alerts for Endpoint Protection in Configuration Manager.

  ） Important

  You must have the Enforce Security permission for collections to configure
  Endpoint Protection alerts.

Steps to Configure Alerts for Endpoint
Protection in Configuration Manager
   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, click Device Collections.

   3. In the Device Collections list, select the collection for which you want to configure
      alerts, and then on the Home tab, in the Properties group, click Properties.

        ７ Note

        You cannot configure alerts for user collections.

   4. On the Alerts tab of the <Collection Name> Properties dialog box, select View
      this collection in the Endpoint Protection dashboard if you want to view details
      about antimalware operations for this collection in the Monitoring workspace of
      the Configuration Manager console.

<!-- p.38 -->

    ７ Note

    This option is unavailable for the All Systems collection.

5. On the Alerts tab of the <Collection Name> Properties dialog box, click Add.

6. In the Add New Collection Alerts dialog box, in the Generate an alert when these
  conditions apply section, select the alerts that you want Configuration Manager to
  generate when the specified Endpoint Protection events occur, and then click OK.

7. In the Conditions list of the Alerts tab, select each Endpoint Protection alert, and
  then specify the following information:

        Alert Name - Accept the default name or enter a new name for the alert.

        Alert Severity - In the list, select the alert level to display in the Configuration
        Manager console.

8. Depending on the alert that you select, specify the following additional
  information:

        Malware detection - This alert is generated if malware is detected on any
        computer in the collection that you monitor. The Malware detection
        threshold specifies the malware detection levels at which this alert is
        generated:

           High - All detections - The alert is generated when there are one or more
           computers in the specified collection on which any malware is detected,
           regardless of what action the Endpoint Protection client takes.

           Medium - Detected, pending action - The alert is generated when there is
           one or more computers in the specified collection on which malware is
           detected, and you must manually remove the malware.

           Low - Detected, still active - The alert is generated when there are one or
           more computers in the specified collection on which malware is detected
           and is still active.

        Malware outbreak - This alert is generated if specified malware is detected
        on a specified percentage of computers in the collection that you monitor.

           Percentage of computers with malware detected - The alert is generated
           when the percentage of computers with malware that is detected in the

<!-- p.39 -->

             collection exceeds the percentage that you specify. Specify a percentage
             from 1 through 99.

               ７ Note

               The percentage value is based on the number of computers in the
               collection, but excludes computers that do not have a Configuration
               Manager client installed. It includes computers that do not yet have
               the Endpoint Protection client installed.

          Repeated malware detection - This alert is generated if specific malware is
          detected more than a specified number of times over a specified number of
          hours on the computers in the collection that you monitor. Specify the
          following information to configure this alert:

             Number of times malware has been detected: - The alert is generated
             when the same malware is detected on computers in the collection more
             than the specified number of times. Specify a number from 2 through 32.

             Interval for detection (hours): Specify the detection interval (in hours) in
             which the number of malware detections must occur. Specify a number
             from 1 through 168.

          Multiple malware detection - This alert is generated if more than a specified
          number of malware types are detected over a specified number of hours on
          computers in the collection that you monitor. Specify the following
          information to configure this alert:

             Number of malware types detected: The alert is generated when the
             specified number of different malware types are detected on computers in
             the collection. Specify a number from 2 through 32.

             Interval for detection (hours): Specify the detection interval, in hours, in
             which the number of malware detections must occur. Specify a number
             from 1 through 168.

   9. Click OK to close the <Collection Name> Properties dialog box.

Alert for outdated malware client
Beginning with Configuration Manager version 1702, you can configure an alert to
ensure Endpoint Protection clients are not outdated. From any device collection, you can

<!-- p.40 -->

now add columns to the list for the following attributes Antimalware Client Version and
Endpoint Protection Deployment State. For example, in the console navigate to Assets
and Compliance > Overview > Device Collections > All Desktops and Server Clients.
Right-click the column header and select those columns to add. To check for an alert,
view Alerts in the Monitoring workspace. If more than 20% of managed clients are
running an expired version of antimalware software, the Antimalware client version is
outdated alert is displayed. This alert doesn't appear on the Monitoring > Overview tab.
To update expired antimalware clients, enable software updates for antimalware clients.

To configure the percentage at which the alert is generated, expand Monitoring >
Alerts > All Alerts, double-click Antimalware clients out of date and modify the Raise
alert if percentage of managed clients with an outdated version of the antimalware
client is more than option.

  Next step >

  Back >

Feedback
Was this page helpful?      Yes    No

Provide product feedback
