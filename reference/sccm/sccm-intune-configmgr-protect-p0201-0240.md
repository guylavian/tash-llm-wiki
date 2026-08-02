---
title: "Protect data and infrastructure documentation — pages 201-240"
type: reference
domain: sccm
slug: sccm-intune-configmgr-protect-p0201-0240
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-protect-p0201-0240
family: sccm
documentKind: "doc"
abstract: "( FILE = 'C:\\Windows\\Temp\\BitLockerManagement_CERT_KEY', DECRYPTION BY PASSWORD = 'password' ); 7. Run the following query to grant required control permissions on the certificate: SQL GRANT CONTROL ON CERTIFICATE::BitLockerManagement_CERT TO RecoveryAndHardwareRead; GRANT CONTR"
---

# Protect data and infrastructure documentation — pages 201-240

<!-- p.201 -->

          (
                FILE = 'C:\Windows\Temp\BitLockerManagement_CERT_KEY',
                DECRYPTION BY PASSWORD = 'password'
          );

   7. Run the following query to grant required control permissions on the certificate:

          SQL

          GRANT CONTROL ON CERTIFICATE::BitLockerManagement_CERT TO
          RecoveryAndHardwareRead;
          GRANT CONTROL ON CERTIFICATE::BitLockerManagement_CERT TO
          RecoveryAndHardwareWrite;

   8. Fail over to the next node.

   9. Run the following query to register the DMK password with the local SMK. Execute once
        per replica:

          SQL

          EXEC sp_control_dbmasterkey_password
              @db_name = N'CM_XXX',
              @password = N'password',
              @action = N'add';

 10. Perform the previous two steps on any remaining nodes.

 11. Fail over to the original node.

 12. To verify that all nodes can automatically open the Database Master Key (DMK) and
        decrypt the data, see the next section Verify all nodes can automatically open the
        Database Master Key (DMK) and decrypt the data in this article.

Verify all nodes can automatically open the
Database Master Key (DMK) and decrypt the data
To verify that all nodes can automatically open the Database Master Key (DMK) and decrypt the
data:

   1. Fail over to a node.

   2. Run the following query:

          SQL

<!-- p.202 -->

       SELECT TOP 5 RecoveryAndHardwareCore.DecryptString(RecoveryKey, DEFAULT)
       FROM RecoveryAndHardwareCore_Keys
       ORDER BY LastUpdateTime DESC

 3. If the query returns plaintext values for any rows that have a valid key in them, then the
    node can automatically open the Database Master Key (DMK) and can decrypt the data.

 4. Repeat the previous three steps for each additional node.

  Tip

 For improved security, store the strong DMK password securely. For example, in Azure Key
 Vault or another secure secret store. Additionally, avoid hardcoding the DMK password in
 plain text in scripts or configuration files.

Related articles
    Encrypt recovery data in the database.
    Prepare to use a SQL Server Always On availability group with Configuration Manager.
    Configure a SQL Server Always On availability group for Configuration Manager.

<!-- p.203 -->

Windows Hello for Business settings in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager integrates with Windows Hello for Business. (This feature was
formerly known as Microsoft Passport for Work.) Windows Hello for Business is an
alternative sign-in method for Windows 10 devices. It uses Active Directory or a
Microsoft Entra account to replace a password, smart card, or virtual smart card. Hello
for Business lets you use a user gesture to sign in instead of a password. A user gesture
might be a PIN, biometric authentication, or an external device such as a fingerprint
reader.

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

  Active Directory Federation Services Registration Authority (ADFS RA) deployment
  is simpler, provides a better user experience, and has a more deterministic
  certificate enrollment experience. Use ADFS RA for certificate-based authentication
  with Windows Hello for Business.

For more information, see Windows Hello for Business.

  ７ Note

  Configuration Manager doesn't enable this optional feature by default. You must
  enable this feature before using it. For more information, see Enable optional
  features from updates.

Configuration Manager integrates with Windows Hello for Business in the following
ways:

        Control which gestures users can and can't use to sign in.

        Store authentication certificates in the Windows Hello for Business key storage
        provider (KSP). For more information, see Certificate profiles.

<!-- p.204 -->

   Create and deploy a Windows Hello for Business profile to control its settings on
   domain-joined Windows 10 devices that run the Configuration Manager client.
   Starting in version 1910, you can't use certificate-based authentication. When
   using key-based authentication, you don't need to deploy a certificate profile.

Configure a profile
 1. In the Configuration Manager console, go to the Assets and Compliance
   workspace. Expand Compliance Settings, expand Company Resource Access, and
   select the Windows Hello for Business Profiles node.

 2. In the ribbon, select Create Windows Hello for Business Profile to start the profile
   wizard.

 3. On the General page, specify a name and an optional description for this profile.

 4. On the Supported Platforms page, select the OS versions to which this profile
   should apply.

 5. On the Settings page, configure the following settings:

        Configure Windows Hello for Business: Specify whether this profile enables,
        disables, or doesn't configure Hello for Business.

        Use a Trusted Platform Module (TPM): A TPM provides an additional layer of
        data security. Choose one of the following values:

             Required: Only devices with an accessible TPM can provision Windows
             Hello for Business.

             Preferred: Devices first attempt to use a TPM. If it's not available, they can
             use software encryption.

        Authentication method: Set this option to Not configured or Key-based.

             ７ Note

             Starting in version 1910, certificate-based authentication with Windows
             Hello for Business settings in Configuration Manager isn't supported.

        Configure minimum PIN length: If you want to require a minimum length for
        the user's PIN, enable this option and specify a value. When enabled, the
        default value is 4 .

<!-- p.205 -->

Configure maximum PIN length: If you want to require a maximum length
for the user's PIN, enable this option and specify a value. When enabled the
default value is 127 .

Require PIN expiration (days): Specifies the number of days before the user
must change the device PIN.

Prevent reuse of previous PINs: Don't allow users to use PINs they have
previously used.

Require upper-case letters in PIN: Specifies whether users must include
uppercase letters in the Windows Hello for Business PIN. Choose from:

   Allowed: Users can use uppercase characters in their PIN, but don't have
   to.

   Required: Users must include at least one uppercase character in their PIN.

   Not allowed: Users can't use uppercase characters in their PIN.

Require lower-case letters in PIN: Specifies whether users must include
lowercase letters in the Windows Hello for Business PIN. Choose from:

   Allowed: Users can use lowercase characters in their PIN, but don't have
   to.

   Required: Users must include at least one lowercase character in their PIN.

   Not allowed: Users can't use lowercase characters in their PIN.

Configure special characters: Specifies the use of special characters in the
PIN. Choose from:

  ７ Note

  Special characters include the following set:

     characters

     ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | }
     ~

   Allowed: Users can use special characters in their PIN, but don't have to.

   Required: Users must include at least one special character in their PIN.

<!-- p.206 -->

             Not allowed: Users can't use special characters in their PIN. This behavior
             is also if the setting is Not configured.

          Configure the use of digits in PIN: Specifies the use of numbers in the PIN.
          Choose from:

             Allowed: Users can use numbers in their PIN, but don't have to.

             Required: Users must include at least one number in their PIN.

             Not allowed: Users can't use numbers in their PIN.

          Enable biometric gestures: Use biometric authentication such as facial
          recognition or fingerprint. These modes are an alternative to a PIN for
          Windows Hello for Business. Users still configure a PIN in case biometric
          authentication fails.

          If set to Yes, Windows Hello for Business allows biometric authentication. If
          set to No, Windows Hello for Business prevents biometric authentication for
          all account types.

          Use enhanced anti-spoofing: Configures enhanced anti-spoofing on devices
          that support it. If set to Yes, where supported, Windows requires all users to
          use anti-spoofing for facial features.

          Use Phone Sign In: Configures two-factor authentication with a mobile
          phone.

   6. Complete the wizard.

The following screenshot is an example of Windows Hello for Business profile settings:

<!-- p.207 -->

Configure permissions
 1. As a Domain Administrator or equivalent credentials, sign in to a secure,
   administrative workstation that has the following optional feature installed: RSAT:
   Active Directory Domain Services and Lightweight Directory Services Tools.

 2. Open the Active Directory Users and Computers console.

 3. Select the domain, go to the Action Menu, and select Properties.

 4. Switch to the Security tab, and select Advanced.

      Tip

     If you don't see the Security tab, close the properties window. Go to the View
     menu, and select Advanced Features.

 5. Select Add.

 6. Choose Select a principal and enter Key Admins .

 7. From the Applies to list, select Descendant User objects.

<!-- p.208 -->

   8. At the bottom of the page, select Clear all.

   9. In the Properties section, select Read msDS-KeyCredentialLink.

  10. Select OK to save your changes and close all windows.

Next steps
Certificate profiles

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.209 -->

Introduction to certificate profiles in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

Certificate profiles work with Active Directory Certificate Services and the Network
Device Enrollment Service (NDES) role. Create and deploy authentication certificates for
managed devices so that users can easily access organizational resources. For example,
you can create and deploy certificate profiles to provide the necessary certificates for
users to connect to VPN and wireless connections.

Certificate profiles can automatically configure user devices for access to organizational
resources such as Wi-Fi networks and VPN servers. Users can access these resources
without manually installing certificates or using an out-of-band process. Certificate
profiles help to secure resources because you can use more secure settings that are
supported by your public key infrastructure (PKI). For example, require server
authentication for all Wi-Fi and VPN connections because you've deployed the required
certificates on the managed devices.

Certificate profiles provide the following management capabilities:

      Certificate enrollment and renewal from a certification authority (CA) for devices
      that run different OS types and versions. These certificates can then be used for
      Wi-Fi and VPN connections.

      Deployment of trusted root CA certificates and intermediate CA certificates. These
      certificates configure a chain of trust on devices for VPN and Wi-Fi connections
      when server authentication is required.

      Monitor and report about the installed certificates.

Example 1: All employees need to connect to Wi-Fi hotspots in multiple office locations.
To enable easy user connection, first deploy the certificates needed to connect to Wi-Fi.
Then deploy Wi-Fi profiles that reference the certificate.

<!-- p.210 -->

Example 2: You have a PKI in place. You want to move to a more flexible, secure method
of deploying certificates. Users need to access organizational resources from their
personal devices without compromising security. Configure certificate profiles with
settings and protocols that are supported for the specific device platform. The devices
can then automatically request these certificates from an internet-facing enrollment
server. Then, configure VPN profiles to use these certificates so that the device can
access organizational resources.

Types
There are three types of certificate profiles:

     Trusted CA certificate: Deploy a trusted root CA or intermediate CA certificate.
     These certificates form a chain of trust when the device must authenticate a server.

     Simple Certificate Enrollment Protocol (SCEP): Request a certificate for a device or
     user by using the SCEP protocol. This type requires the Network Device Enrollment
     Service (NDES) role on a server running Windows Server 2012 R2 or later.

     To create a Simple Certificate Enrollment Protocol (SCEP) certificate profile, first
     create a Trusted CA certificate profile.

     Personal information exchange (.pfx): Request a .pfx (also known as PKCS #12)
     certificate for a device or user. There are two methods to create PFX certificate
     profiles:
        Import credentials from existing certificates
        Define a certificate authority to process requests

        ７ Note

        Configuration Manager doesn't enable this optional feature by default. You
        must enable this feature before using it. For more information, see Enable
        optional features from updates.

     You can use Microsoft or Entrust as certificate authorities for Personal information
     exchange (.pfx) certificates.

Requirements
To deploy certificate profiles that use SCEP, install the certificate registration point on a
site system server. Also install a policy module for NDES, the Configuration Manager

<!-- p.211 -->

Policy Module, on a server that runs Windows Server 2012 R2 or later. This server
requires the Active Directory Certificate Services role. It also requires a working NDES
that's accessible to the devices that require the certificates. If your devices need to enroll
for certificates from the internet, then your NDES server must be accessible from the
internet. For example, to safely enable traffic to the NDES server from the internet, you
can use Azure Application Proxy.

PFX certificates also require a certificate registration point. Also specify the certificate
authority (CA) for the certificate and the relevant access credentials. You can specify
either Microsoft or Entrust as certificate authorities.

For more information about how NDES supports a policy module so that Configuration
Manager can deploy certificates, see Using a Policy Module with the Network Device
Enrollment Service.

Depending on the requirements, Configuration Manager supports deploying certificates
to different certificate stores on various device types and operating systems. The
following devices and operating systems are supported:

     Windows 10

     Windows 10 Mobile

     Windows 8.1

     Windows Phone 8.1

  ７ Note

  Use Configuration Manager on-premises MDM to manage Windows Phone 8.1 and
  Windows 10 Mobile. For more information, see On-premises MDM.

A typical scenario for Configuration Manager is to install trusted root CA certificates to
authenticate Wi-Fi and VPN servers. Typical connections use the following protocols:

     Authentication protocols: EAP-TLS, EAP-TTLS, and PEAP
     VPN tunneling protocols: IKEv2, L2TP/IPsec, and Cisco IPsec

An enterprise root CA certificate must be installed on the device before the device can
request certificates by using a SCEP certificate profile.

You can specify settings in a SCEP certificate profile to request customized certificates
for different environments or connectivity requirements. The Create Certificate Profile
Wizard has two pages for enrollment parameters. The first, SCEP Enrollment, includes

<!-- p.212 -->

settings for the enrollment request and where to install the certificate. The second,
Certificate Properties, describes the requested certificate itself.

Deploy
When you deploy a SCEP certificate profile, the Configuration Manager client processes
the policy. It then requests a SCEP challenge password from the management point. The
device creates a public/private key pair, and generates a certificate signing request
(CSR). It sends this request to the NDES server. The NDES server forwards the request to
the certificate registration point site system via the NDES policy module. The certificate
registration point validates the request, checks the SCEP challenge password, and
verifies that the request wasn't tampered with. It then approves or denies the request. If
approved, the NDES server sends the signing request to the connected certificate
authority (CA) for signing. The CA signs the request, and then it returns the certificate to
the requesting device.

Deploy certificate profiles to user or device collections. You can specify the destination
store for each certificate. Applicability rules determine whether the device can install the
certificate.

When you deploy a certificate profile to a user collection, user device affinity determines
which of the users' devices install the certificates. When you deploy a certificate profile
with a user certificate to a device collection, by default each of the users' primary
devices install the certificates. To install the certificate on any of the users' devices,
change this behavior on the SCEP Enrollment page of the Create Certificate Profile
Wizard. If the devices are in a workgroup, Configuration Manager doesn't deploy user
certificates.

Monitor
You can monitor certificate profile deployments by viewing compliance results or
reports. For more information, see How to monitor certificate profiles.

Automatic revocation
Configuration Manager automatically revokes user and computer certificates that were
deployed by using certificate profiles in the following circumstances:

      The device is retired from Configuration Manager management.

      The device is blocked from the Configuration Manager hierarchy.

<!-- p.213 -->

To revoke the certificates, the site server sends a revocation command to the issuing
certification authority. The reason for the revocation is Cease of Operation.

  ７ Note

  To properly revoke a certificate, the computer account for the top-level site in the
  hierarchy needs the permission to issue and manage certificates on the CA.

  For improved security, you can also restrict CA managers on the CA. Then only give
  this account permissions on the specific certificate template that you use for the
  SCEP profiles on the site.

Next steps
     Create certificate profiles

     Configure certificate infrastructure

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.214 -->

Create certificate profiles
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

Use certificate profiles in Configuration Manager to provision managed devices with the
certificates they need to access company resources. Before creating certificate profiles,
set up the certificate infrastructure as described in Set up certificate infrastructure.

This article describes how to create trusted root and Simple Certificate Enrollment
Protocol (SCEP) certificate profiles. If you want to create PFX certificate profiles, see
Create PFX certificate profiles.

To create a certificate profile:

   1. Start the Create Certificate Profile Wizard.
   2. Provide general information about the certificate.
   3. Configure a trusted certificate authority (CA) certificate.
   4. Configure SCEP certificate information.
   5. Specify supported platforms for the certificate profile.

Start the wizard
To start the Create Certificate Profile:

   1. In the Configuration Manager console, go to the Assets and Compliance
      workspace, expand Compliance Settings, expand Company Resource Access, and
      then select the Certificate Profiles node.

   2. On the Home tab of the ribbon, in the Create group, select Create Certificate
      Profile.

General

<!-- p.215 -->

On the General page of the Create Certificate Profile Wizard, specify the following
information:

     Name: Enter a unique name for the certificate profile. You can use a maximum of
     256 characters.

     Description: Provide a description that gives an overview of the certificate profile.
     Also include other relevant information that helps to identify it in the
     Configuration Manager console. You can use a maximum of 256 characters.

     Specify the type of certificate profile that you want to create:

        Trusted CA certificate: Select this type to deploy a trusted root certification
        authority (CA) or intermediate CA certificate to form a certificate chain of trust
        when the user or device must authenticate another device. For example, the
        device might be a Remote Authentication Dial-In User Service (RADIUS) server
        or a virtual private network (VPN) server.

        Also configure a trusted CA certificate profile before you can create a SCEP
        certificate profile. In this case, the trusted CA certificate must be for the CA that
        issues the certificate to the user or device.

        Simple Certificate Enrollment Protocol (SCEP) settings: Select this type to
        request a certificate for a user or device with the Simple Certificate Enrollment
        Protocol and the Network Device Enrollment Service (NDES) role service.

        Personal Information Exchange PKCS #12 (PFX) settings - Import: Select this
        option to import a PFX certificate. For more information, see Import PFX
        certificate profiles.

        Personal Information Exchange PKCS #12 (PFX) settings - Create: Select this
        option to process PFX certificates using a certificate authority. For more
        information, see Create PFX certificate profiles.

Trusted CA certificate

  ） Important

  Before you create a SCEP certificate profile, configure at least one trusted CA
  certificate profile.

  After the certificate is deployed, if you change any of these values, a new certificate
  is requested:

<!-- p.216 -->

        Key Storage Provider
        Certificate template name
        Certificate type
        Subject name format
        Subject alternative name
        Certificate validity period
        Key usage
        Key size
        Extended key usage
        Root CA certificate

   1. On the Trusted CA Certificate page of the Create Certificate Profile Wizard, specify
     the following information:

            Certificate file: Select Import, and then browse to the certificate file.

            Destination store: For devices that have more than one certificate store,
            select where to store the certificate. For devices that have only one store, this
            setting is ignored.

   2. Use the Certificate thumbprint value to verify that you've imported the correct
     certificate.

SCEP certificates

1. SCEP Servers
On the SCEP Servers page of the Create Certificate Profile Wizard, specify the URLs for
the NDES Servers that will issue certificates via SCEP. You can automatically assign an
NDES URL based on the configuration of the certificate registration point, or add URLs
manually.

2. SCEP Enrollment
Complete the SCEP Enrollment page of the Create Certificate Profile Wizard.

     Retries: Specify the number of times that the device automatically retries the
     certificate request to the NDES server. This setting supports the scenario where a
     CA manager must approve a certificate request before it's accepted. This setting is
     typically used for high-security environments or if you have a stand-alone issuing

<!-- p.217 -->

CA rather than an enterprise CA. You might also use this setting for testing
purposes so that you can inspect the certificate request options before the issuing
CA processes the certificate request. Use this setting with the Retry delay
(minutes) setting.

Retry delay (minutes): Specify the interval, in minutes, between each enrollment
attempt when you use CA manager approval before the issuing CA processes the
certificate request. If you use manager approval for testing purposes, specify a low
value. Then you're not waiting a long time for the device to retry the certificate
request after you approve the request.

If you use manager approval on a production network, specify a higher value. This
behavior allows sufficient time for the CA administrator to approve or deny
pending approvals.

Renewal threshold (%): Specify the percentage of the certificate lifetime that
remains before the device requests renewal of the certificate.

Key Storage Provider (KSP): Specify where the key to the certificate is stored.
Choose from one of the following values:

  Install to Trusted Platform Module (TPM) if present: Installs the key to the
  TPM. If the TPM isn't present, the key is installed to the storage provider for the
  software key.

  Install to Trusted Platform Module (TPM) otherwise fail: Installs the key to the
  TPM. If the TPM module isn't present, the installation fails.

  Install to Windows Hello for Business otherwise fail: This option is available for
  Windows 10 or later devices. It allows you to store the certificate in the
  Windows Hello for Business store, which is protected by multi-factor
  authentication. For more information, see Windows Hello for Business.

     ７ Note

     This option doesn't support Smart card logon for the Enhanced key usage
     on the Certificate Properties page.

  Install to Software Key Storage Provider: Installs the key to the storage
  provider for the software key.

Devices for certificate enrollment: If you deploy the certificate profile to a user
collection, allow certificate enrollment only on the user's primary device, or on any

<!-- p.218 -->

     device to which the user signs in.

     If you deploy the certificate profile to a device collection, allow certificate
     enrollment for only the primary user of the device, or for all users that sign in to
     the device.

3. Certificate Properties
On the Certificate Properties page of the Create Certificate Profile Wizard, specify the
following information:

     Certificate template name: Select the name of a certificate template that you
     configured in NDES and added to an issuing CA. To successfully browse to
     certificate templates, your user account needs Read permission to the certificate
     template. If you can't Browse for the certificate, type its name.

        ） Important

        If the certificate template name contains non-ASCII characters, the certificate
        isn't deployed. (One example of these characters is from the Chinese
        alphabet.) To make sure that the certificate is deployed, first create a copy of
        the certificate template on the CA. Then rename the copy by using ASCII
        characters.

        If you browse to select the name of the certificate template, some fields on the
        page automatically populate from the certificate template. In some cases, you
        can't change these values unless you choose a different certificate template.

        If you type the name of the certificate template, make sure that the name
        exactly matches one of the certificate templates. It must match the names that
        are listed in the registry of the NDES server. Make sure that you specify the
        name of the certificate template, and not the display name of the certificate
        template.

        To find the names of certificate templates, browse to the following registry key:
        HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\MSCEP . It lists the

        certificate templates as the values for EncryptionTemplate,
        GeneralPurposeTemplate, and SignatureTemplate. By default, the value for all
        three certificate templates is IPSECIntermediateOffline, which maps to the
        template display name of IPSec (Offline request).

<!-- p.219 -->

       ２ Warning

       When you type the name of the certificate template, Configuration
       Manager can't verify the contents of the certificate template. You may be
       able to select options that the certificate template doesn't support, which
       may result in a failed certificate request. When this behavior happens, you'll
       see an error message for w3wp.exe in the CPR.log file that the template
       name in the certificate signing request (CSR) and the challenge don't
       match.

       When you type the name of the certificate template that's specified for the
       GeneralPurposeTemplate value, select the Key encipherment and the
       Digital signature options for this certificate profile. If you want to enable
       only the Key encipherment option in this certificate profile, specify the
       certificate template name for the EncryptionTemplate key. Similarly, if you
       want to enable only the Digital signature option in this certificate profile,
       specify the certificate template name for the SignatureTemplate key.

Certificate type: Select whether you'll deploy the certificate to a device or a user.

Subject name format: Select how Configuration Manager automatically creates the
subject name in the certificate request. If the certificate is for a user, you can also
include the user's email address in the subject name.

  ７ Note

  If you select IMEI number or Serial number, you can differentiate between
  different devices that are owned by the same user. For example, those devices
  could share a common name, but not an IMEI number or serial number. If the
  device doesn't report an IMEI or serial number, the certificate is issued with
  the common name.

Subject alternative name: Specify how Configuration Manager automatically
creates the values for the subject alternative name (SAN) in the certificate request.
For example, if you selected a user certificate type, you can include the user
principal name (UPN) in the subject alternative name. If the client certificate will
authenticate to a Network Policy Server, set the subject alternative name to the
UPN.

Certificate validity period: If you set a custom validity period on the issuing CA,
specify the amount of remaining time before the certificate expires.

<!-- p.220 -->

   Tip

  Set a custom validity period with the following command line: certutil -
  setreg Policy\EditFlags +EDITF_ATTRIBUTEENDDATE For more information

  about this command, see Certificate infrastructure.

You can specify a value that's lower than the validity period in the specified
certificate template, but not higher. For example, if the certificate validity period in
the certificate template is two years, you can specify a value of one year, but not a
value of five years. The value must also be lower than the remaining validity period
of the issuing CA's certificate.

Key usage: Specify key usage options for the certificate. Choose from the following
options:

   Key encipherment: Allow key exchange only when the key is encrypted.

   Digital signature: Allow key exchange only when a digital signature helps
   protect the key.

If you browsed for a certificate template, you can't change these settings, unless
you select a different certificate template.

Configure the selected certificate template with one or both of the two key usage
options above. If not, you'll see the following message in the certificate registration
point log file, Crp.log: Key usage in CSR and challenge do not match

Key size (bits): Select the size of the key in bits.

Extended key usage: Add values for the certificate's intended purpose. In most
cases, the certificate requires Client Authentication so that the user or device can
authenticate to a server. You can add any other key usages as required.

Hash algorithm: Select one of the available hash algorithm types to use with this
certificate. Select the strongest level of security that the connecting devices
support.

  ７ Note

  SHA-2 supports SHA-256, SHA-384, and SHA-512. SHA-3 supports only SHA-
  3.

<!-- p.221 -->

     Root CA certificate: Choose a root CA certificate profile that you previously
     configured and deployed to the user or device. This CA certificate must be the root
     certificate for the CA that will issue the certificate that you're configuring in this
     certificate profile.

        ） Important

        If you specify a root CA certificate that's not deployed to the user or device,
        Configuration Manager won't initiate the certificate request that you're
        configuring in this certificate profile.

Supported platforms
On the Supported Platforms page of the Create Certificate Profile Wizard, select the OS
versions where you want to install the certificate profile. Choose Select all to install the
certificate profile to all available operating systems.

Next steps
The new certificate profile appears in the Certificate Profiles node in the Assets and
Compliance workspace. It's ready for you to deploy to users or devices. For more
information, see How to deploy profiles.

Feedback
Was this page helpful?       Yes    No

Provide product feedback

<!-- p.222 -->

Configure certificate infrastructure
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

Learn to configure certificate infrastructure in Configuration Manager. Before you start,
check for any prerequisites that are listed in Prerequisites for certificate profiles.

Use these steps to configure your infrastructure for SCEP, or PFX certificates.

Step 1 - Install and Configure the Network
Device Enrollment Service and Dependencies
(for SCEP certificates only)
You must install and configure the Network Device Enrollment Service role service for
Active Directory Certificate Services (AD CS), change the security permissions on the
certificate templates, deploy a public key infrastructure (PKI) client authentication
certificate, and edit the registry to increase the Internet Information Services (IIS) default
URL size limit. If necessary, you must also configure the issuing certification authority
(CA) to allow a custom validity period.

  ） Important

  Before you configure Configuration Manager to work with the Network Device
  Enrollment Service, verify the installation and configuration of the Network Device
  Enrollment Service. If these dependencies are not working correctly, you will have
  difficulty troubleshooting certificate enrollment by using Configuration Manager.

To install and configure the Network Device Enrollment
Service and dependencies

<!-- p.223 -->

1. On a server that is running Windows Server 2012 R2, install and configure the
  Network Device Enrollment Service role service for the Active Directory Certificate
  Services server role. For more information, see Network Device Enrollment Service
  Guidance.

2. Check, and if necessary, modify the security permissions for the certificate
  templates that the Network Device Enrollment Service is using:

        For the account that runs the Configuration Manager console: Read
        permission.

        This permission is required so that when you run the Create Certificate Profile
        Wizard, you can browse to select the certificate template that you want to
        use when you create a SCEP settings profile. Selecting a certificate template
        means that some settings in the wizard are automatically populated, so there
        is less for you to configure and there is less risk of selecting settings that are
        not compatible with the certificate templates that the Network Device
        Enrollment Service is using.

        For the SCEP Service account that the Network Device Enrollment Service
        application pool uses: Read and Enroll permissions.

        This requirement is not specific to Configuration Manager but is part of
        configuring the Network Device Enrollment Service. For more information,
        see Network Device Enrollment Service Guidance.

     Tip

    To identify which certificate templates the Network Device Enrollment Service
    is using, view the following registry key on the server that is running the
    Network Device Enrollment Service:
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\MSCEP.

    ７ Note

    These are the default security permissions that will be appropriate for most
    environments. However, you can use an alternative security configuration. For
    more information, see Planning for certificate template permissions for
    certificate profiles.

3. Deploy to this server a PKI certificate that supports client authentication. You might
  already have a suitable certificate installed on the computer that you can use, or

<!-- p.224 -->

  you might have to (or prefer to) deploy a certificate specifically for this purpose.
  For more information about the requirements for this certificate, refer to the
  details for Servers running the Configuration Manager Policy Module with the
  Network Device Enrollment Service role service in the PKI Certificates for Servers
  section in the PKI certificate requirements for Configuration Manager topic.

      Tip

     If you need help deploying this certificate, you can use the instructions for
     Deploying the Client Certificate for Distribution Points, because the
     certificate requirements are the same with one exception:

          Do not select the Allow private key to be exported check box on the
          Request Handling tab of the properties for the certificate template.

          You do not have to export this certificate with the private key because
          you will be able to browse to the local Computer store and select it
          when you configure the Configuration Manager Policy Module.

4. Locate the root certificate that the client authentication certificate chains to. Then,
  export this root CA certificate to a certificate (.cer) file. Save this file to a secured
  location that you can securely access when you later install and configure the site
  system server for the certificate registration point.

5. On the same server, use the registry editor to increase the IIS default URL size limit
  by setting the following registry key DWORD values in
  HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\HTTP\Parameters:

        Set the MaxFieldLength key to 65534.

        Set the MaxRequestBytes key to 16777216.

        For more information, see Microsoft Support article 820129: Http.sys registry
        settings for Windows      .

6. On the same server, in Internet Information Services (IIS) Manager, modify the
  request-filtering settings for the /certsrv/mscep application, and then restart the
  server. In the Edit Request Filtering Settings dialog box, the Request Limits
  settings should be as follows:

        Maximum allowed content length (Bytes): 30000000

        Maximum URL length (Bytes): 65534

<!-- p.225 -->

           Maximum query string (Bytes): 65534

           For more information about these settings and how to configure them, see
           IIS Requests Limits.

   7. If you want to be able to request a certificate that has a lower validity period than
     the certificate template that you are using: This configuration is disabled by default
     for an enterprise CA. To enable this option on an enterprise CA, use the Certutil
     command-line tool, and then stop and restart the certificate service by using the
     following commands:

      a. certutil - setreg Policy\EditFlags +EDITF_ATTRIBUTEENDDATE

      b. net stop certsvc

      c. net start certsvc

        For more information, see Certificate services tools and settings.

   8. Verify that the Network Device Enrollment Service is working by using the
     following link as an example:
      https://server.contoso.com/certsrv/mscep/mscep.dll . You should see the built-in

     Network Device Enrollment Service webpage. This webpage explains what the
     service is and explains that network devices use the URL to submit certificate
     requests.

     Now that the Network Device Enrollment Service and dependencies are
     configured, you are ready to install and configure the certificate registration point.

Step 2 - Install and configure the certificate
registration point.
You must install and configure at least one certificate registration point in the
Configuration Manager hierarchy, and you can install this site system role in the central
administration site or in a primary site.

  ） Important

  Before you install the certificate registration point, see the Site System
  Requirements section in the Supported configurations for Configuration
  Manager topic for operating system requirements and dependencies for the
  certificate registration point.

<!-- p.226 -->

To install and configure the certificate registration point

  1. In the Configuration Manager console, click Administration.

  2. In the Administration workspace, expand Site Configuration, click Servers and
    Site System Roles, and then select the server that you want to use for the
    certificate registration point.

  3. On the Home tab, in the Server group, click Add Site System Roles.

  4. On the General page, specify the general settings for the site system, and then
    click Next.

  5. On the Proxy page, click Next. The certificate registration point does not use
    Internet proxy settings.

  6. On the System Role Selection page, select Certificate registration point from the
    list of available roles, and then click Next.

  7. On the Certificate Registration Mode page, select whether you want this
    certificate registration point to Process SCEP certificate requests, or Process PFX
    certificate requests. A certificate registration point cannot process both kinds of
    requests, but you can create multiple certificate registration points if you are
    working with both certificate types.

    If processing PFX certificates, you'll need to choose a certificate authority, either
    Microsoft or Entrust.

  8. The Certificate Registration Point Settings page varies according to the certificate
    type:

            If you selected Process SCEP certificate requests, then configure the
            following:
              Website name, HTTPS port number, and Virtual application name for the
              certificate registration point. These fields are filled in automatically with
              default values.
              URL for the Network Device Enrollment Service and root CA certificate -
              Click Add, then in the Add URL and Root CA Certificate dialog box,
              specify the following:
                  URL for the Network Device Enrollment Service: Specify the URL in the
                  following format: https://<server_FQDN>/certsrv/mscep/mscep.dll. For
                  example, if the FQDN of your server that is running the Network Device
                  Enrollment Service is server1.contoso.com, type
                  https://server1.contoso.com/certsrv/mscep/mscep.dll .

<!-- p.227 -->

     Root CA Certificate: Browse to and select the certificate (.cer) file that
     you created and saved in Step 1: Install and configure the Network
     Device Enrollment Service and dependencies. This root CA certificate
     allows the certificate registration point to validate the client
     authentication certificate that the Configuration Manager Policy Module
     will use.

If you selected Process PFX certificate requests, you configure the
connection details and credentials for the selected certificate authority.

  To use Microsoft as the certificate authority, click Add then in the Add a
  Certificate Authority and Account dialog box, specify the following:

     Certificate Authority Server Name - Enter the name of your certificate
     authority server.

     Certificate Authority Account - Click Set to select, or create the
     account that has permissions to enroll in templates on the certification
     authority.

     Certificate Registration Point Connection Account - Select or create
     the account that connects the certificate registration point to the
     Configuration Manager database. Alteratively, you can use the local
     computer account of the computer hosting the certificate registration
     point.

     Active Directory Certificate Publishing Account - Select an account, or
     create a new account that will be used to publish certificates to user
     objects in Active Directory.

     In the URL for the Network Device Enrollment and root CA certificate
     dialog box, specify the following, and then click OK:

  To use Entrust as the certificate authority, specify:

     The MDM web service URL

     The username and password credentials for the URL.

     When using the MDM API to define the Entrust web service URL, be
     sure to use at least version 9 of the API, as shown in the following
     sample:

      https://entrust.contoso.com:19443/mdmws/services/AdminServiceV9

<!-- p.228 -->

                 Earlier versions of the API do not support Entrust.

   9. Click Next and complete the wizard.

 10. Wait a few minutes to let the installation finish, and then verify that the certificate
     registration point was installed successfully by using any of the following methods:

           In the Monitoring workspace, expand System Status, click Component
           Status, and look for status messages from the
           SMS_CERTIFICATE_REGISTRATION_POINT component.

           On the site system server, use the <ConfigMgr Installation
           Path>\Logs\crpsetup.log file and <ConfigMgr Installation
           Path>\Logs\crpmsi.log file. A successful installation will return an exit code of
           0.

           By using a browser, verify that you can connect to the URL of the certificate
           registration point. For example,
           https://server1.contoso.com/CMCertificateRegistration . You should see a

           Server Error page for the application name, with an HTTP 404 description.

 11. Locate the exported certificate file for the root CA that the certificate registration
     point automatically created in the following folder on the primary site server
     computer: <ConfigMgr Installation Path>\inboxes\certmgr.box. Save this file to a
     secured location that you can securely access when you later install the
     Configuration Manager Policy Module on the server that is running the Network
     Device Enrollment Service.

         Tip

        This certificate is not immediately available in this folder. You might need to
        wait awhile (for example, half an hour) before Configuration Manager copies
        the file to this location.

Step 3 - Install the Configuration Manager
Policy Module (for SCEP certificates only).
You must install and configure the Configuration Manager Policy Module on each server
that you specified in Step 2: Install and configure the certificate registration point as
URL for the Network Device Enrollment Service in the properties for the certificate
registration point.

<!-- p.229 -->

To install the Policy Module

  1. On the server that runs the Network Device Enrollment Service, log on as a domain
    administrator and copy the following files from the
    <ConfigMgrInstallationMedia>\SMSSETUP\POLICYMODULE\X64 folder on the
    Configuration Manager installation media to a temporary folder:

          PolicyModule.msi

          PolicyModuleSetup.exe

    In addition, if you have a LanguagePack folder on the installation media, copy this
    folder and its contents.

  2. From the temporary folder, run PolicyModuleSetup.exe to start the Configuration
    Manager Policy Module Setup wizard.

  3. On the initial page of the wizard, click Next, accept the license terms, and then
    click Next.

  4. On the Installation Folder page, accept the default installation folder for the policy
    module or specify an alternative folder, and then click Next.

  5. On the Certificate Registration Point page, specify the URL of the certificate
    registration point by using the FQDN of the site system server and the virtual
    application name that is specified in the properties for the certificate registration
    point. The default virtual application name is CMCertificateRegistration. For
    example, if the site system server has an FQDN of server1.contoso.com and you
    used the default virtual application name, specify
    https://server1.contoso.com/CMCertificateRegistration .

  6. Accept the default port of 443 or specify the alternative port number that the
    certificate registration point is using, and then click Next.

  7. On the Client Certificate for the Policy Modulepage, browse to and specify the
    client authentication certificate that you deployed in Step 1: Install and configure
    the Network Device Enrollment Service and dependencies, and then click Next.

  8. On the Certificate Registration Point Certificate page, click Browse to select the
    exported certificate file for the root CA that you located and saved at the end of
    Step 2: Install and configure the certificate registration point.

      ７ Note

<!-- p.230 -->

        If you did not previously save this certificate file, it is located in the
        <ConfigMgr Installation Path>\inboxes\certmgr.box on the site server
        computer.

   9. Click Next and complete the wizard.

      If you want to uninstall the Configuration Manager Policy Module, use Programs
      and Features in Control Panel.

Now that you have completed the configuration steps, you are ready to deploy
certificates to users and devices by creating and deploying certificate profiles. For more
information about how to create certificate profiles, see How to create certificate
profiles.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.231 -->

Create Wi-Fi profiles
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

Use Wi-Fi profiles in Configuration Manager to deploy wireless network settings to users
in your organization. By deploying these settings, you make it easier for your users to
connect to Wi-Fi.

For example, you have a Wi-Fi network that you want to enable all Windows laptops to
connect to. Create a Wi-Fi profile containing the settings necessary to connect to the
wireless network. Then, deploy the profile to all users that have Windows laptops in your
hierarchy. Users of these devices see your network in the list of wireless networks and
can readily connect to this network.

You can configure Wi-Fi profiles for the following OS versions:

      Windows 8.1 32-bit or 64-bit

      Windows RT 8.1

      Windows 10 or Windows 10 Mobile

You can also use Configuration Manager to deploy wireless network settings to mobile
devices using on-premises mobile device management (MDM). For more general
information, see What is on-premises MDM.

When you create a Wi-Fi profile, you can include a wide range of security settings. These
settings include certificates for server validation and client authentication that have been
pushed using Configuration Manager certificate profiles. For more information about
certificate profiles, see Certificate profiles.

Create a Wi-Fi profile
   1. In the Configuration Manager console, go to the Assets and Compliance
      workspace, expand Compliance Settings, expand Company Resource Access, and

<!-- p.232 -->

  select the Wi-Fi Profiles node.

2. On the Home tab, in the Create group, choose Create Wi-Fi Profile.

3. On the General page of the Create Wi-Fi Profile Wizard, specify the following
  information:

       Name: Enter a unique name to identify the profile in the console.

       Description: Optionally add a description to provide further information for
       the Wi-Fi profile.

       Import an existing Wi-Fi profile item from a file: Select this option to use
       the settings from another Wi-Fi profile. When you select this option, the
       remaining pages of the wizard simplify to two pages: Import Wi-Fi Profile
       and Supported Platforms.

          ） Important

          Make sure that the Wi-Fi profile you import contains valid XML for a Wi-
          Fi profile. When you import the file, Configuration Manager doesn't
          validate the profile.

       Noncompliance severity for reports: Choose one of the following severity
       levels that the device reports if it evaluates the Wi-Fi profile to be
       noncompliant. For example, if the installation of the profile fails, it's
       noncompliant.

          None: Computers that fail this compliance rule don't report a failure
          severity for Configuration Manager reports.

          Information

          Warning

          Critical

          Critical with event: Computers that fail this compliance rule report a
          failure severity of Critical for Configuration Manager reports. Devices also
          log the noncompliant state as a Windows event in the application event
          log.

4. On the Wi-Fi Profile page of the wizard, specify the following information:

<!-- p.233 -->

       Network name: Provide the name that devices will display as the network
       name.

          ） Important

          Configuration Manager doesn't support using the apostrophe ( ' ) or
          comma ( , ) characters in the network name.

       SSID: Specify the case-sensitive ID of the wireless network.

       Connect automatically when this network is in range

       Look for other wireless network while connected to this network

       Connect when the network is not broadcasting its name (SSID)

5. On the Security Configuration page, specify the following information:

    ） Important

    If you're creating a Wi-Fi profile for on-premises MDM, the current branch of
    Configuration Manager only supports the following Wi-Fi security
    configurations:

          Security types: WPA2 Enterprise or WPA2 Personal
          Encryption types: AES or TKIP
          EAP types: Smart Card or other certificate or PEAP

       Security type: Select the security protocol that the wireless network uses, or
       select No authentication (Open) if the network is unsecured.

       Encryption: If the security type supports it, set the encryption method for the
       wireless network.

       EAP type: Select the authentication protocol for the selected encryption
       method.

          ７ Note

          For Windows Phone devices only: the EAP types LEAP and EAP-FAST
          aren't supported.

<!-- p.234 -->

           Select Configure to specify properties for the selected EAP type. This option
           isn't available for some selected EAP types.

              ） Important

              The EAP type configuration window is from Windows. Make sure that
              you run the Configuration Manager console on a computer that
              supports the selected EAP type.

           Remember the user credentials at each logon: Select this option to store
           user credentials so users don't have to enter wireless network credentials
           each time they sign in to Windows.

   6. On the Advanced Settings page of the wizard, specify additional settings for the
     Wi-Fi profile. Advanced settings might not be available, or might vary, depending
     on the options that you select on the Security Configuration page of the wizard.
     For example, authentication mode, or single sign-on options.

   7. On the Proxy Settings page, if your wireless network uses a proxy server, select the
     option to Configure proxy settings for this Wi-Fi profile. Then provide the
     configuration information for the proxy.

   8. On the Supported Platforms page, select the OS versions where this Wi-Fi profile
     is applicable.

   9. Complete the wizard.

Next step
  How to deploy Wi-Fi profiles

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.235 -->

VPN profiles in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

To deploy VPN settings to users in your organization, use VPN profiles in Configuration
Manager. By deploying these settings, you minimize the end-user effort required to
connect to resources on the company network.

For example, you want to configure all Windows 10 devices with the settings required to
connect to a file share on the internal network. Create a VPN profile with the settings
necessary to connect to the internal network. Then deploy this profile to all users that
have devices running Windows 10. These users see the VPN connection in the list of
available networks and can connect with little effort.

When you create a VPN profile, you can include a wide range of security settings. These
settings include certificates for server validation and client authentication that you
provision with Configuration Manager certificate profiles. For more information, see
Certificate profiles.

  ７ Note

  Configuration Manager doesn't enable this optional feature by default. You must
  enable this feature before using it. For more information, see Enable optional
  features from updates.

Supported platforms
The following table describes the VPN profiles you can configure for various device
platforms.

                                                                           ﾉ   Expand table

<!-- p.236 -->

 Connection type                   Windows   Windows   Windows RT   Windows
                                   8.1       RT        8.1          10

 Pulse Secure                      Yes       No        Yes          Yes

 F5 Edge Client                    Yes       No        Yes          Yes

 Dell SonicWALL Mobile             Yes       No        Yes          Yes
 Connect

 Check Point Mobile VPN            Yes       No        Yes          Yes

 Microsoft SSL (SSTP)              Yes       Yes       Yes          No

 Microsoft Automatic               Yes       Yes       Yes          No

 IKEv2                             Yes       Yes       Yes          No

 PPTP                              Yes       Yes       Yes          No

 L2TP                              Yes       Yes       Yes          No

Next step
  How to create VPN profiles

See also
     Prerequisites for VPN profiles

     Security and privacy for VPN profiles

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.237 -->

How to create VPN profiles in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2203, this company resource access feature is no longer
  supported. For more information, see Frequently asked questions about resource
  access deprecation.

Configuration Manager supports multiple VPN connection types. For more information
on the connection types available for the different device platforms, see VPN profiles.

For third-party VPN connections, distribute the VPN app before you deploy the VPN
profile. If you don't deploy the app, users will be prompted to do so when they try to
connect to the VPN. For more information, see Deploy applications.

Create a VPN profile
   1. In the Configuration Manager console, go to the Assets and Compliance
      workspace, expand Compliance Settings, expand Company Resource Access, and
      select the VPN Profiles node.

   2. On the Home tab of the ribbon, in the Create group, choose Create VPN Profile.

   3. On the General page of the Create VPN Profile Wizard, specify the following
      information:

            Name: Enter a unique name to identify the VPN profile in the console.

              ７ Note

              Don't use the following characters in the VPN profile name: \/:*?<>|; .
              The Windows VPN profile doesn't support these special characters.

            Description: Optionally enter a description to provide further information
            about the VPN profile.

<!-- p.238 -->

       VPN profile type: Select the appropriate platform.

       If you select the Windows 8.1 platform, you can also Import from file. This
       action imports VPN profile information from an XML file. If you select this
       option, the rest of the wizard simplifies to the following pages: Supported
       Platforms and Import VPN Profile.

4. On the Supported Platforms page, select the OS versions that this VPN profile
  supports.

5. On the Connection page, specify the following information:

       Connection type: Choose the VPN connection type. For more information on
       the supported types, see VPN profiles.

       Server list: Add a new server to use for the VPN connection. Depending on
       the connection type, you can add one or more VPN servers and specify which
       server is the default.

       Bypass VPN when connected to company network: Configure clients to not
       use the VPN when they're on your internal network. If necessary, specify a
       connection-specific DNS name.

6. On the Authentication Method page of the wizard, choose a method that's
  supported by the connection type. The settings and available options on this page
  vary depending on the selected connection type. For more information, see
  Authentication method reference.

7. On the Proxy Settings page, if your VPN uses a proxy server, select one of the
  options as appropriate for your environment. Then provide the configuration
  information for the proxy.

8. The Applications page only applies to Windows 10 profiles. Add desktop and
  universal apps that automatically connect to this VPN. The type of app determines
  the app identifier:

       For a desktop app, provide the file path of the app.

       For a universal app, provide the package family name (PFN). To learn how to
       find the PFN for an app, see Find a package family name for per-app VPN.

  You can also configure an option so that Only the listed apps can use this VPN.

    ） Important

<!-- p.239 -->

        Secure all lists of associated apps that you compile for configuring a per-app
        VPN. If an unauthorized user changes your list, and you import it to the per-
        app VPN app list, you potentially authorize VPN access to apps that shouldn't
        have access.

   9. The Boundaries page only applies to Windows 10 profiles to configure VPN
     boundaries. You can add the following options:

           Network traffic rules: Set the protocols, local port, remote port, and address
           ranges to enable for the VPN connection.

             ７ Note

             If you don't create a network traffic rule, all protocols, ports, and address
             ranges are enabled. After you create a rule, only the protocols, ports,
             and address ranges that you specify in that rule or in additional rules are
             used by the VPN connection.

           DNS names and servers: DNS servers that are used by the VPN connection
           after the device establishes the connection.

           Routes: Network routes that use the VPN connection. Creation of more than
           60 routes may cause the policy to fail.

 10. Complete the wizard.

The new VPN profile is displayed in the VPN Profiles node in the Assets and
Compliance workspace.

Authentication method reference
Available VPN authentication methods depend on the connection type:

Certificates
If the client certificate authenticates to a RADIUS server, like a Network Policy Server, set
the Subject Alternative Name in the certificate to the User Principal Name.

Supported connection types:

     Pulse Secure
     F5 Edge Client

<!-- p.240 -->

     Dell SonicWALL Mobile Connect
     Check Point Mobile VPN

Username and Password
Supported connection types:

     Pulse Secure
     F5 Edge Client
     Dell SonicWALL Mobile Connect
     Check Point Mobile VPN

Microsoft EAP-TTLS
Supported connection types:

     Microsoft SSL (SSTP)
     Microsoft Automatic
     PPTP
     IKEv2
     L2TP

Microsoft protected EAP (PEAP
Supported connection types:

     Microsoft SSL (SSTP)
     Microsoft Automatic
     IKEv2
     PPTP
     L2TP

Microsoft secured password (EAP-MSCHAP v2)
Supported connection types:

     Microsoft SSL (SSTP)
     Microsoft Automatic
     IKEv2
     PPTP
     L2TP
