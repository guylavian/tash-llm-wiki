---
title: "Exchange Server — pages 681-720"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0681-0720
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0681-0720
family: exchange
documentKind: "doc"
abstract: "Perform an IIS reset on all front-end servers. Migrating to Hybrid Modern Auth after using enabling Modern Auth for Exchange Server If you're using Modern Auth with ADFS and later decide to configure Exchange Hybrid, you should transition to Hybrid Modern Auth. Detailed migratio"
---

# Exchange Server — pages 681-720

<!-- p.681 -->

     Perform an IIS reset on all front-end servers.

Migrating to Hybrid Modern Auth after using
enabling Modern Auth for Exchange Server
If you're using Modern Auth with ADFS and later decide to configure Exchange Hybrid, you
should transition to Hybrid Modern Auth. Detailed migration steps will be included in a future
version of this document.

Renewing certificates

Evaluate current certificate configuration
When it comes to client connections to Exchange Server, the certificate that should be
evaluated is the one bound to the Frontend IIS Site. For an ADFS server, ensuring that all
certificates returned in Get-AdfsCertificate are current is ideal.

   1. To identify the relevant certificate on an Exchange Server, perform the following within
     Exchange Management Shell:

       PowerShell

       Import-Module WebAdministration
       (Get-ChildItem IIS:SSLBindings | Where-Object {($_.Sites -ne $null) -and
       ($_.Port -eq "443")}).Thumbprint | ForEach-Object {Get-ExchangeCertificate $_
       | Where-Object {$_.Services -Match "IIS"} | Format-Table Thumbprint, Services,
       RootCAType, Status, NotAfter, Issuer -AutoSize -Wrap}

   2. To review active certificates on an ADFS Server, perform the following within PowerShell:

       PowerShell

       Get-AdfsCertificate | Format-Table CertificateType, Thumbprint, Certificate -
       AutoSize -Wrap

Update certificates on Exchange Server
If it's been found that the Exchange certificate needs to be updated for client connectivity, a
new certificate must be issued and imported onto the Exchange Servers. Afterwards, the
certificate should be enabled for IIS at minimum. Evaluate if other services should be enabled
for the new certificate based on your configuration.

<!-- p.682 -->

Sample on creating, completing, enabling, and importing a new certificate across all servers
based on the existing certificate within the Exchange Management Shell:

   1. Generate a new certificate request within the Exchange Management Shell based on your
     existing certificate:

       PowerShell

       $txtrequest = Get-ExchangeCertificate <Thumbprint> | New-ExchangeCertificate -
       GenerateRequest -PrivateKeyExportable $true

   2. Stage a variable containing the desired output path of your new certificate request:

       PowerShell

       $requestFile = "C:\temp\CertRequest.req"

   3. Create the certificate request file:

       PowerShell

       [System.IO.File]::WriteAllBytes($requestFile,
       [System.Text.Encoding]::Unicode.GetBytes($txtrequest))

        ７ Note

        The folder path for the certificate request must already exist.

   4. Share the request file with your Certificate Authority (CA). The steps required to get a
     completed certificate varies based on your CA.

        ７ Note

        .p7b is the preferred format for the completed request.

   5. Stage a variable containing the full path of the completed request:

       PowerShell

       $certFile = "C:\temp\ExchangeCert.p7b"

   6. Import the request onto the server that originally generated the request:

<!-- p.683 -->

     PowerShell

     Import-ExchangeCertificate -FileData
     ([System.IO.File]::ReadAllBytes($certFile)) -PrivateKeyExportable $true

 7. Stage variable for the password to protect the completed certificate:

     PowerShell

     $pw = Read-Host "Enter password" -AsSecureString

 8. Export the certificate Binary into a variable:

     PowerShell

     $binCert = Export-ExchangeCertificate <Thumbprint> -BinaryEncoded

 9. Stage variable for the desired output path of the completed certificate:

     PowerShell

     $certificate = "\\$env:computername\c$\temp\CompletedExchangeCert.pfx"

10. Export the completed request to be imported on other servers:

     PowerShell

     [System.IO.File]::WriteAllBytes($certificate, $binCert.FileData)

11. Enable the services that should be bound to the certificate:

     PowerShell

     Enable-ExchangeCertificate <Thumbprint> -Services IIS

      ７ Note

      You may need to add more services to the previous sample based on your previous
      certificates configuration.

12. Validate the certificate is working as intended by directing a client to the server for all
   client namespaces with a host file.

<!-- p.684 -->

 13. Import the Exchange certificate on all other Exchange servers:

       PowerShell

       Import-ExchangeCertificate -PrivateKeyExportable $true -FileData
       ([System.IO.File]::ReadAllBytes($certificate)) -Password $pw -Server <Server-
       Name>

       ７ Note

       Including the -PrivateKeyExportable parameter is optional when importing to other
       Exchange servers.

 14. Enable the Exchange certificate for needed Exchange services on all other Exchange
     servers:

       PowerShell

       Enable-ExchangeCertificate <Thumbprint> -Services IIS -Server <Server-Name>

       ７ Note

       You may need to add more services to the previous sample based on your previous
       certificates configuration.

Update certificate on ADFS
Depending on the certificate type that requires update on ADFS determines if you need to
follow the steps described below.

Service-Communications certificate

This sample provides the PowerShell required to import a certificate in .pfx format, such as
the one generated by following the Exchange Server certificate steps. Ensure you're logged on
the primary ADFS server.

   1. Stage a variable containing the password for the certificate:

       PowerShell

       $pw = Read-Host "Enter password" -AsSecureString

<!-- p.685 -->

   2. Stage a variable containing the full path for the certificate:

       PowerShell

       $certificate = "\\E2k19-1\c$\temp\CompletedExchangeCert.pfx"

   3. Import the certificate into the personal store of the LocalMachine:

       PowerShell

       Import-PfxCertificate -FilePath $certificate -CertStoreLocation
       Cert:\LocalMachine\my -Password $pw

   4. Update the Service-Communications certificate:

       PowerShell

       Set-AdfsSslCertificate -Thumbprint <Thumbprint>

Token-Signing and Token-Decryption certificates
Follow the steps outlined in the Obtain and Configure TS and TD Certificates for AD FS
documentation.

  ７ Note

  Using the default self-signed certificate for Token-Signing in ADFS claims-based
  authentication for Outlook on the web requires the certificate to be installed on the
  Exchange Servers.

Last updated on 02/17/2026

<!-- p.686 -->

Disable Basic authentication on Exchange
Server virtual directories
APPLIES TO:        2016     2019      Subscription Edition

Introduction
Basic authentication is a method of client authentication that requires a username and a
password to access a resource. However, Basic authentication can pose a security risk. As many
of our customers make business decisions to eliminate Basic authentication in their
environments, we're providing this documentation to help with these efforts as it relates to
Exchange Server.

  ） Important

  We don't support disabling NTLM or Negotiate (Windows Integrated Authentication,
  which includes NTLM and Kerberos) on the Exchange virtual directories.

  To prevent clients from using NTLM or Kerberos when connecting to Exchange servers, we
  support and recommend using Authentication Policies as described in the following blog
  post: Disabling Legacy Authentication in Exchange Server 2019        .

This article describes how to disable Basic authentication on each virtual directory where it's
enabled by default on an Exchange Server. If you previously enabled Basic authentication on
other virtual directories, do one of the following steps:

     Use your documented steps to reverse the changes made.
     Use the instructions in Default settings for Exchange Server virtual directories to set the
     authentication method back to default settings.

Prerequisites
     You should configure the virtual directories for Outlook on the web (formerly known as
     Outlook Web App or OWA) and the Exchange admin center (EAC) with the same
     authentication method.

     By default, Outlook on the web and the EAC use Forms Based Authentication (FBA), which
     relies on Basic authentication. If you disable Basic authentication on these virtual
     directories, you can't use FBA. You need to configure another authentication method.

<!-- p.687 -->

Disable Basic authentication on the Outlook on the
web virtual directory
The Outlook on the web virtual directory is used by web clients to connect to mailboxes on the
Exchange server. As previously described, the authentication methods on the Outlook on the
web and EAC virtual directories should be the same.

You can use the EAC or the Exchange Management Shell to disable Basic authentication on the
Outlook on the web virtual directory.

  ） Important

  Before you disable Basic authentication on the Outlook on the web virtual directory, you
  need to configure another authentication method. If the virtual directories are already
  configured with another authentication method (for example, NTLM, Kerberos, ADFS, or
  Certificate Based Authentication), Basic authentication is likely disabled. Otherwise, the
  following guidance helps you disable Basic authentication if you no longer require FBA
  and are already using another method.

Use the EAC to disable Basic authentication on the Outlook on
the web virtual directory
   1. Open the EAC and go to Servers > Virtual Directories.

   2. Select the server using the dropdown menu.

   3. Select the OWA (Default Web Site) virtual directory and then select Edit.

                                                                                               

   4. Select Authentication, clear the Basic authentication check box, and the select Save.

<!-- p.688 -->

                                                                                           

Use the Exchange Management Shell to disable Basic
authentication on the Outlook on the web virtual directory
In the Exchange Management Shell, the following example disables Basic authentication on the
OWA virtual directory on the server named EX01:

 PowerShell
 Set-OwaVirtualDirectory -Identity "EX01\owa (Default Web Site)" -BasicAuthentication
 $false

For detailed syntax and parameter information, see Set-OwaVirtualDirectory.

Disable Basic authentication on the ECP virtual
directory
The EAC virtual directory is the ECP virtual directory (the old name for the EAC was the
Exchange Control Panel or ECP). As previously described, the authentication methods on the
Outlook on the web and EAC virtual directories should be the same.

<!-- p.689 -->

You can use the EAC or the Exchange Management Shell to disable Basic authentication on the
ECP virtual directory.

  ） Important

  Before you disable Basic authentication on the ECP virtual directory, you need to configure
  another authentication method. If the virtual directories are already configured with
  another authentication method (for example, NTLM, Kerberos, ADFS, or Certificate Based
  Authentication), Basic authentication is likely disabled. Otherwise, the following guidance
  helps you disable Basic authentication if you no longer require FBA and are already using
  another method.

Use the EAC to disable Basic authentication on the ECP virtual
directory
   1. Open the EAC and go to Servers > Virtual Directories.

   2. Select the server using the dropdown menu.

   3. Select the ECP (Default Web Site) virtual directory, and then select Edit.

                                                                                           

   4. Select Authentication, clear the Basic authentication check box, and then select Save.

<!-- p.690 -->

                                                                                        

Use the Exchange Management Shell to disable Basic
authentication on the ECP virtual directory
In the Exchange Management Shell, the following example disables Basic authentication on the
ECP virtual directory on the server named EX01:

 PowerShell
 Set-EcpVirtualDirectory -Identity "EX01\ecp (Default Web Site)" -BasicAuthentication
 $false

For detailed syntax and parameter information, see Set-EcpVirtualDirectory.

Disable Basic authentication on the Autodiscover
virtual directory
The Autodiscover virtual directory is used by Outlook and mobile devices to automatically
configure the connection settings to the Exchange server.

You can use the EAC or the Exchange Management Shell to disable Basic authentication on the
Autodiscover virtual directory.

<!-- p.691 -->

Use the EAC to disable Basic authentication on the
Autodiscover virtual directory
 1. Open the EAC and go to Servers > Virtual Directories.

 2. Select the server using the dropdown menu.

 3. Select the Autodiscover (Default Web Site) virtual directory, and then select Edit.

                                                                                          

   Select Authentication, clear the Basic authentication check box, and then select Save.

                                                                                          

<!-- p.692 -->

Use the Exchange Management Shell to disable Basic
authentication on the Autodiscover virtual directory
In the Exchange Management Shell, the following command disables Basic authentication on
the Autodiscover virtual directory on the server named EX01:

 PowerShell

 Set-AutodiscoverVirtualDirectory -Identity "EX01\Autodiscover (Default Web Site)" -
 BasicAuthentication $false

For detailed syntax and parameter information, see Set-AutodiscoverVirtualDirectory.

Disable Basic authentication on the ActiveSync
virtual directory
The Exchange ActiveSync (EAS) virtual directory is used by ActiveSync mobile clients to connect
to their mailboxes on the Exchange server.

You can use the EAC or the Exchange Management Shell to disable Basic authentication on the
ActiveSync virtual directory.

  ） Important

  Before you disable Basic authentication on the ActiveSync virtual directory, you need to
  configure another authentication method (for example, Hybrid Modern Authentication
  (HMA) or Certificate Based Authentication (CBA)). Otherwise, ActiveSync clients can't
  connect to their mailboxes.

Use the EAC to disable Basic authentication on the ActiveSync
virtual directory
   1. Open the EAC and go to Servers > Virtual Directories.

   2. Select the server using the dropdown menu.

   3. Select the Microsoft-Server-ActiveSync (Default Web Site) virtual directory, and then
     select Edit.

<!-- p.693 -->

                                                                                          

     Select Authentication, clear the Basic authentication check box, and then select Save.

                                                                                          

Use the Exchange Management Shell to disable Basic
authentication on the ActiveSync virtual directory
In the Exchange Management Shell, the following example disables Basic authentication on the
Microsoft-Server-ActiveSync virtual directory on the server named EX01:

 PowerShell

<!-- p.694 -->

 Set-ActiveSyncVirtualDirectory -Identity "EX01\ Microsoft-Server-ActiveSync (Default
 Web Site)" -BasicAuthentication $False

For detailed syntax and parameter information, see Set-ActiveSyncVirtualDirectory.

Disable Basic authentication on the Outlook
Anywhere virtual directory
The Outlook Anywhere virtual directory is used by older Outlook clients that use the legacy
RPC over HTTP protocol to connect to their mailboxes on an Exchange server.

In the EAC, you can only set the external authentication method, not the internal authentication
method.

In contrast, the Set-OutlookAnywhere cmdlet in the Exchange Management Shell configures
both internal and external authentication methods. Because Kerberos authentication is typically
unavailable for external connections, we recommend using the DefaultAuthenticationMethod
parameter with the value NTLM . This method simultaneously updates the
ExternalClientAuthenticationMethod, InternalClientAuthenticationMethod, and
IISAuthenticationMethods settings.

  ） Important

  Most organizations no longer use the legacy RPC over HTTP protocol. MAPI over HTTP is
  now the default protocol in modern versions of Outlook.

  If you still use RPC over HTTP for internal connections only, we recommend using
  Kerberos if possible.

  OAuth isn't available for RPC over HTTP.

In the Exchange Management Shell, the following example disables Basic authentication for
internal and external connections on the Outlook Anywhere virtual directory on the server
named EX01. The command also sets the authentication method to NTLM for internal and
external connections:

 PowerShell
 Set-OutlookAnywhere -Identity "EX01\Rpc (Default Web Site)" -
 DefaultAuthenticationMethod NTLM

<!-- p.695 -->

For detailed syntax and parameter information, see [Set-OutlookAnywhere]
(/powershell/module/exchangepowershell/set-outlook anywhere).

Related articles
Disabling Legacy Authentication in Exchange Server 2019

How to configure Exchange Server on-premises to use Hybrid Modern Authentication

Using hybrid Modern Authentication with Outlook for iOS and Android

Configure certificate based authentication in Exchange 2016

Use AD FS claims-based authentication with Outlook on the web

Last updated on 11/14/2025

<!-- p.696 -->

Security best practices for Exchange Server
Article • 04/30/2025

APPLIES TO:        2016        2019    Subscription Edition

Overview
The following topics provides security best practices and recommendations for operating
Exchange Server in a secure manner. We're constantly adding new topics to this section. Check
back from time to time to make sure you're informed about the latest recommendations.

                                                                                        ﾉ    Expand table

 Topic                                 Description                                          Type

 Exchange Server update FAQ            Learn why it's important to keep your                Documentation
                                       Exchange server up-to-date.

 Exchange Server and SMB v1            Learn why it's important to disable insecure         Blog post
                                       SMB versions.

 Configure Download Domains in         Learn how to configure the Download Domain           Documentation
 Exchange Server                       feature in Exchange Server.

 Configure Windows Extended            Learn how to configure Extended Protection in        Documentation
 Protection in Exchange Server         Exchange Server.

 Configure HTTP Strict Transport       Learn how to configure HSTS in Exchange              Documentation
 Security (HSTS) in Exchange Server    Server.

 Configure certificate signing of      Learn how to configure the certificate signing       Documentation
 PowerShell serialization payload in   of PowerShell serialization payload feature in
 Exchange Server                       Exchange Server.

 Exchange Emergency Mitigation (EM)    Learn more about the Exchange Emergency              Documentation
 service                               Mitigation service in Exchange Server.

 Exchange Server TLS configuration     Learn more about how to configure TLS                Documentation
 best practices                        correctly in Exchange Server.

 Exchange Server non-RFC compliant     Learn more about the feature that detects            Documentation
 P2 FROM header detection              non-RFC compliant P2 FROM headers in
                                       Exchange Server.

<!-- p.697 -->

Configure Download Domains in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Overview
The Download Domains feature causes attachments to be loaded from a different URL than the
one, which is used by the user to access Outlook on the Web (OWA). This cross-site call
enforces the so-called SameSite cookies standard      of the browser, which enables a better
protection against cross-site request forgery (CSRF) attacks. A vulnerability that is addressed by
the Download Domains feature is, for example, CVE-2021-1730 .

What are cookies and when are they used
Cookies are text strings sent from websites and stored on a computer by the web browser.
They're used for authentication and personalization. For example, cookies are used to recall
stateful information, preserve user settings, record browsing activity, and display relevant ads.
Cookies are always linked to a particular domain and are installed by various parties.

Historically, sites such as example.com that make cross-origin requests to other domains such
as contoso.com have caused the browser to send example.com cookies as part of any request.

In most cases, the user benefits by being able to reuse some state (for example, login state)
across sites no matter from where a request originated. However, this behavior can be abused
in CSRF attacks. The SameSite component reduced the exposure through its implementation
and management in the Set-Cookie header.

How does the SameSite cookie standard work
A SameSite is defined as a top-level domain (TLD) plus one more domain name.

Example:

                                                                                 ﾉ    Expand table

 Scheme                       Domain Name                                      TLD

 https://                     contoso                                          .com

<!-- p.698 -->

The URL scheme is also taken into account. A request that comes from https://contoso.com
and goes to http://contoso.com (for example, by clicking on a link), is considered as cross-site
requests.

With the SameSite cookies standard, sites or web applications can set the SameSite attribute
on cookies via the Set-Cookie header or by using the document.cookie JavaScript property to
restrict in which cases a cookie is sent.

The SameSite cookies specification was introduced in Google Chrome version 51 as an
optional attribute. It was introduced with Windows 10 Build 17672         for Microsoft Edge and
Internet Explorer.

There are three values that are supported:

      Strict

        The browser won't send this cookie in any cross-site request
      Lax

        The browser sends this cookie in cross-site requests under certain conditions (all
        conditions must apply):
             The "safe" HTTP GET method is used
             The request comes from a top-level navigation, which was performed by the user
             (for example, a link was clicked)
      None

        The browser sends the cookie in any cross-site request as this setting disables the
         SameSite restriction

The SameSite cookies standard is supported by all major web browsers and if the SameSite
attribute isn't explicitly set by the web site or application, which issues the cookie, it's
automatically presumed by the web browser and treated by default as SameSite=Lax to
improve security against CSRF attacks.

     Microsoft Edge
     Google Chrome
     Mozilla Firefox

Looking at the Download Domains feature, a call to attachments.owa.contoso.com that was
initiated from owa.contoso.com is considered as cross-site request and cookies are only sent if
the conditions, described for the Lax value, have been met.

Enable Download Domains in your organization

<!-- p.699 -->

There are several steps that must be performed before the Download Domain feature can be
turned on for your organization. Follow the steps to configure the feature:

   1. Create a new DNS record of type CNAME (Alias). The record must point to the domain
     that you use to access Outlook on the Web (OWA).

     Example:

                                                                               ﾉ     Expand table

      Name                                            Type          Value

      attachments.owa.contoso.com                     CNAME         owa.contoso.com

       ７ Note

       If you are using different namespaces for internal and external OWA access, it's
       required to create two CNAME records and set them accordingly via the
        InternalDownloadHostName and ExternalDownloadHostName parameter as described in

       step 3.

       ） Important

       Users must NOT use the Download Domains to access Outlook on the Web as this
       would eliminate the protection provided by the Download Domains feature.

   2. Make sure to add the new subdomain to the certificate, which is used by Exchange Server
     and bound to the front-end. More information about certificate request on Exchange
     Server can be found in the Certificate procedures in Exchange Server article.

   3. Add the new subdomain to the Outlook on the Web configuration by running the
     following command from an elevated Exchange Management Shell (EMS):

       PowerShell

        Set-OwaVirtualDirectory -Identity "Contoso\OWA (Default Web Site)" -
        InternalDownloadHostName "attachments.owa.contoso.com" -
        ExternalDownloadHostName "attachments.owa.contoso.com"

       ７ Note

<!-- p.700 -->

       Make sure to set the correct hostnames if your Exchange configuration uses different
       namespaces for accessing OWA from internal and external networks. Using the
       wrong namespace can cause the user experience to be degraded (for example, inline
       images are invisible etc.).

   4. After all OWA virtual directories have been prepared and the new certificate has been
     deployed to all Exchange servers, the feature can be turned on by running the following
     command from an elevated Exchange Management Shell (EMS):

       PowerShell

        Set-OrganizationConfig -EnableDownloadDomains $true

   5. It's required to restart the World Wide Web Publishing service and the Windows Process
     Activation Service on each Exchange server to activate the feature. Run the following

     command from an elevated PowerShell window or restart the server:

       PowerShell

        Restart-Service -Name W3SVC, WAS -Force

Confirm that Download Domains are enabled
You can follow these steps to confirm that the Download Domain feature is enabled and works
as expected:

   1. Send an email with an inline image to your mailbox. It doesn't matter if the email was
     sent from an internal or external mailbox.
   2. Login into OWA and search for the test email that was sent to your mailbox.
   3. Make sure that the image is loaded and displayed in the reading pane.
   4. Right-click on the inline image and select Copy Image link
   5. Paste the link into Notepad.exe and check the URL. It should be the configured Download
     Domain (for example, attachments.owa.contoso.com). This result confirms that the
     Download Domain feature is active and works as expected.

Disable Download Domains in your organization
The Download Domain feature is configured via an organization-wide configuration and as a
result, can only be enabled or disabled on all or no Exchange servers. If you want to disable the

<!-- p.701 -->

feature, it's sufficient to run the following command from an elevated Exchange Management
Shell (EMS):

  PowerShell

  Set-OrganizationConfig -EnableDownloadDomains $false

Follow the steps as outlined in the Confirm that Download Domains are enabled section of this
article to confirm, that the feature is disabled.

<!-- p.702 -->

Configure Windows Extended Protection in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016       2019       Subscription Edition

Overview
Windows Extended Protection enhances the existing authentication in Windows Server and
mitigates authentication relay or man-in-the-middle (MitM) attacks. This mitigation is
accomplished by using security information that is implemented through channel-binding
information specified through a Channel Binding Token (CBT) which is primarily used for TLS
connections.

Extended Protection is enabled by default when installing Exchange Server 2019 CU14 (or
later). For more information, see Released: 2024 H1 Cumulative Update for Exchange Server        .

On older versions of Exchange Server (for example, Exchange Server 2016), Extended
Protection can be enabled by the help of the ExchangeExtendedProtectionManagement.ps1
script on some or all Exchange servers.

Terminology used in this documentation

Virtual Directory or vDir
Is used by Exchange Server to allow access to web applications such as Exchange ActiveSync ,
Outlook on the Web , and the AutoDiscover service. Several virtual directory settings can be
configured by an admin, including authentication, security, and reporting settings. Extended
Protection is one such authentication setting.

Extended Protection setting
Controls the behavior for checking of Channel Binding Tokens or CBT . Possible values for this
setting are listed in the following table:

                                                                               ﾉ   Expand table

 Value     Description

 None      Specifies that IIS doesn't perform CBT checking.

<!-- p.703 -->

 Value     Description

 Allow     Specifies that CBT checking is enabled, but not required. This setting allows secure
           communication with clients that support Extended Protection, and still supports clients that
           aren't capable of using Extended Protection.

 Require   This value specifies that CBT checking is required. This setting blocks clients that don't support
           Extended Protection.

SSL Flags
Configuration of SSL settings is required to ensure that clients connect to IIS virtual directories
in a specific way with client certificates. To enable Extended Protection, the required SSL flags
are SSL and SSL128 .

SSL Offloading
Terminates the connection on a device between the client and the Exchange Server and then
uses a nonencrypted connection to connect to the Exchange Server.

SSL Bridging
Describes a process where a device, located at the edge of a network, decrypts SSL traffic, and
then re-encrypts it before sending it on to the Web server.

Modern Hybrid or Hybrid Agent
This is the name of a method of configuring Exchange hybrid that removes some of the
configuration requirements for classic hybrid (for example, inbound network connections
through your firewall) to enable Exchange hybrid features. You can learn more about this
feature here.

Public Folders
Are designed for shared access and to help make content in a deep hierarchy easier to browse.
You can learn more about Public Folders here.

Prerequisites for enabling Extended Protection on
Exchange Server

<!-- p.704 -->

   Tip

  We recommend running the Exchange Server Health Checker          script to check whether
  all prerequisites are met on the Exchange server on which Extended Protection should be
  activated.

Exchange server versions that support Extended Protection
Extended Protection is supported on Exchange Server 2013, 2016 and 2019 starting with the
August 2022 Exchange Server Security Update (SU) releases      .

If your organization has Exchange Server 2016 or Exchange Server 2019 installed, they must be
running either the September 2021 Quarterly Exchange Cumulative Updates        or the 2022 H1
Cumulative Update    . You must have at least the August 2022 or later Security Update
installed before you continue with the configuration of Extended Protection.

If your organization has Exchange Server 2013 installed, Exchange Server must be on CU23
with the August 2022 or later Security Update installed.

  ２ Warning

  Exchange Server 2013 has reached end of support on April 11, 2023.

Outlook Anywhere configuration requirements
SSL offloading for Outlook Anywhere is enabled by default and must be disabled before
Extended Protection is enabled. Follow the steps as described in Example 3.

  ） Important

  Exchange Server 2019 CU14 (or later) installer disables SSL offloading for Outlook
  Anywhere automatically. This is part of the Extended Protection enabled by default

  approach.

NTLM version requirements
NTLMv1 is weak and doesn't provide protection against man-in-the-middle (MitM) attacks. It

should be considered as vulnerable    and no longer be used.

<!-- p.705 -->

NTLMv1 can't be used together with Extended Protection. If you enforce a client to use NTLMv1

instead of NTLMv2 and you have Extended Protection enabled on your Exchange servers, this
configuration leads to password prompts on the client side without a way to authenticate
successfully against the Exchange server.

  ７ Note

  To increase security, we recommend that you review and configure this setting regardless
  of whether you experience problems or not.

If you experience password prompts on your clients once Extended Protection is enabled, you
should check the following registry key and value on your client and on the Exchange Server
side:

Registry key: HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa

Registry value: LmCompatibilityLevel

It's recommended to set it to a value of 5 , which is Send NTLMv2 response only. Refuse LM &
NTLM . It must be set at least to a value of 3 which is Send NTLMv2 response only .

If you delete the value, the operating system enforces the system default. On Windows Server
2008 R2 and later, we treat it as if it's set to 3 .

If you want to manage the setting centrally, you can do so by using Group Policy:

Policy location: Computer Configuration\Windows Settings\Security Settings\Local
Policies\Security Options

More information: Network security: LAN Manager authentication level

TLS requirements
Before enabling Extended Protection, you must ensure that all TLS configurations are
consistent across all Exchange servers. For example, if one of the servers uses TLS 1.2 , you
must ensure that all the servers in the organization are configured using TLS 1.2 . Any variation
in TLS version use across servers can cause client or server to server connections to fail.

In addition to this requirement, the value of SchUseStrongCrypto registry value must be set to a
value of 1 across all the Exchange servers within the organization.

If this value isn't explicitly set to 1 , the default value of this key can be interpreted as 0 or 1
depending on the .NET version in use by the Exchange Server binaries and there is a chance

<!-- p.706 -->

that you experience connection issues in server to server communication. This can happen,
especially if different versions of Exchange Server (for example, Exchange Server 2016 and
Exchange Server 2019) are in use.

The same applies to the SystemDefaultTlsVersions registry value, which must also be explicitly
set to a value of 1 .

If these registry values aren't configured as expected, this misconfiguration can cause TLS
mismatch in server to server or client to server communication and as a result, could lead to
connectivity issues.

Refer to this Exchange Server TLS configuration best practices guide to configure the required
TLS settings on your Exchange servers.

Third-party software compatibility
Before enabling Extended Protection, it is essential to conduct tests on all third-party products
within your Exchange Server environment to ensure they function correctly. If you are uncertain
about whether Extended Protection is supported, you should reach out to the vendor for
confirmation.

We have seen, for example, anti-virus solutions, which were sending connections through a
local proxy server in order to protect the client machine. Such a scenario would prevent
communication to the Exchange server and would need to be disabled as it's considered as a
man-in-the-middle (MitM) connection, which will be blocked by Extended Protection.

Scenarios that could affect client connectivity
when Extended Protection was enabled

SSL Offloading scenarios
Extended Protection isn't supported in environments that use SSL Offloading. SSL termination
during SSL Offloading causes Extended Protection to fail. To enable Extended Protection in
your Exchange environment, you must not be using SSL offloading with your Load Balancers.

                                                                                              

SSL Bridging scenarios

<!-- p.707 -->

Extended Protection is supported in environments that use SSL Bridging under certain
conditions. To enable Extended Protection in your Exchange environment using SSL Bridging,
you must use the same SSL certificate on Exchange and your Load Balancers. Using different
certificates cause Extended Protection Channel Binding Token check to fail and as a result,
prevent clients from connecting to the Exchange server.

                                                                                              

Extended Protection and Public Folder scenarios
The following section covers Public Folder scenarios, which could lead to failures when
Extended Protection is enabled.

Extended Protection can't be enabled on Exchange Server 2013 servers
with Public Folders in a coexistence environment
To enable Extended Protection on Exchange Server 2013, ensure that you don't have any Public
Folders that are hosted on Exchange Server 2013. If you have coexistence of Exchange Server
2013 with Exchange Server 2016 or Exchange Server 2019, you must migrate your Public
Folders to Exchange Server 2016 or Exchange Server 2019 before enabling Extended
Protection. After Extended Protection was enabled and there are Public Folders on Exchange
Server 2013, they'll no longer appear to end users!

  ２ Warning

  Exchange Server 2013 has reached end of support on April 11, 2023.

Extended Protection can't be enabled on Exchange Server 2016 CU22 or
Exchange Server 2019 CU11 or older that hosts a Public Folder hierarchy

If you have an environment containing Exchange Server 2016 CU22 or Exchange Server 2019
CU11 or older and are utilizing Public Folders, you must confirm the version of the server that
hosts the Public Folder hierarchy before enabling Extended Protection!

Make sure that the server, which hosts the Public Folder hierarchy is upgraded to Exchange
Server 2016 CU23 or Exchange Server 2019 CU12 (or later) with the latest Security Updates
installed. Move the Public Folder hierarchy to an Exchange Server that runs a required version if
you can't upgrade the Exchange server to a supported version.

<!-- p.708 -->

The following table can be used to clarify:

                                                                                 ﾉ   Expand table

 Exchange          CU installed         SU installed        Hosts PF mailboxes    Is EP
 version                                                                          supported?

 Exchange 2013     CU23                 Aug 2022 (or        No                    Yes
                                        higher)

 Exchange 2016     CU22                 Aug 2022 (or        No hierarchy          Yes
                                        higher)             mailboxes

 Exchange 2016     CU23 (2022 H1) or    Aug 2022 (or        Any                   Yes
                   later                higher)

 Exchange 2019     CU11                 Aug 2022 (or        No hierarchy          Yes
                                        higher)             mailboxes

 Exchange 2019     CU12 (2022 H1) or    Aug 2022 (or        Any                   Yes
                   later                higher)

 Any other         Any other CU         Any other SU        Any                   No
 version

Extended Protection and Modern Hybrid configuration
The following section covers Exchange Server Modern Hybrid scenarios, which could lead to
failures when Extended Protection is enabled.

Extended Protection can't be fully configured on Exchange Servers that
are published using Hybrid Agent
In a Modern Hybrid configuration, Exchange servers are published via a Hybrid Agent, which
proxies the Exchange Online calls to the Exchange server.

Enabling Extended Protection on Exchange Servers that are published via Hybrid Agent, can
lead to disruption of hybrid features like mailbox moves and free/busy calls if not done
correctly. It's therefore important to identify all the Exchange servers, which are published by
the help of a Hybrid Agent and to not enable Extended Protection on the Front-End EWS
virtual directory on them.

Identifying Exchange servers that are published using Hybrid Agent

<!-- p.709 -->

In case that you don't have a list of servers, which were published via Hybrid Agent, you can
use the following steps to identify them. These steps aren't required if you're running a classic
Exchange Server Hybrid deployment.

   1. Log into a machine where the Hybrid Agent is installed and open the PowerShell module
     of the Hybrid Agent. Run Get-HybridApplication to identify the TargetUri used by the
     Hybrid Agent.
   2. The TargetUri parameter gives you the Fqdn of the Exchange server, which is configured
     to be used by the Hybrid Agent.

           Deduce the Exchange server identity using the Fqdn and make a note of the
           Exchange server name.
           If you're using a Load Balancer URL in TargetUri , you need to identify all the
           Exchange servers, which have the Client Access role installed, and which can be
           reached behind the Load Balancer URL.

  ） Important

  Extended Protection must not be enabled on the Front-End EWS virtual directory on
  Exchange Servers that are published via a Hybrid Agent.

We recommend the following steps to safeguard Exchange servers, which were published via
Hybrid Agent:

  ７ Note

  In the following scenario, the Hybrid Agent is installed on a server that does NOT run
  Exchange Server. Additionally, this server is located in a different network segment from
  the production Exchange servers.

   1. For Exchange servers published via the Hybrid Agent, inbound connections should be
     restricted by a firewall to allow connections only from the machine on which the Hybrid
     Agent is installed. This doesn't affect outbound communications from Exchange servers
     to Exchange Online.
   2. No mailboxes should be hosted on the Exchange servers, which were published via
     Hybrid Agent. Existing mailboxes should be migrated to other mailbox servers.

Enabling Extended Protection

<!-- p.710 -->

Extended Protection is automatically enabled during Exchange Server 2019 CU14 (or later)
setup. On older versions of Exchange Server, which support Extended Protection, it can be
enabled via a script provided by Microsoft (recommended)         or manually through IIS Manager.

To correctly configure Extended Protection, each virtual directory on all Exchange servers in the
organization (excluding Edge Transport servers) must be set to prescribed value of Extended
Protection and sslFlags .

The following table summarizes the settings needed for each virtual directory on the supported
versions of Exchange Server.

                                                                                    ﾉ   Expand table

 IIS Website    Virtual Directory              Recommended Value       Recommended sslFlags

 Default         API                           Required                Ssl,Ssl128
 Website

 Default         AutoDiscover                  Off                     Ssl,Ssl128
 Website

 Default         ECP                           Required                Ssl,Ssl128
 Website

 Default         EWS                           Accept (UI) / Allow     Ssl,Ssl128
 Website                                       (Script)

 Default         MAPI                          Required                Ssl,Ssl128
 Website

 Default         Microsoft-Server-ActiveSync   Accept (UI) / Allow     Ssl,Ssl128
 Website                                       (Script)

 Default         Microsoft-Server-             Accept (UI) / Allow     Ssl,Ssl128
 Website        ActiveSync/Proxy               (Script)

 Default         OAB                           Accept (UI) / Allow     Ssl,Ssl128
 Website                                       (Script)

 Default         OWA                           Required                Ssl,Ssl128
 Website

 Default         PowerShell                    Off                     SslNegotiateCert
 Website

 Default         RPC                           Required                Ssl,Ssl128
 Website

<!-- p.711 -->

IIS Website    Virtual Directory             Recommended Value    Recommended sslFlags

Exchange       API                           Required              Ssl,Ssl128
Backend

Exchange       AutoDiscover                  Off                   Ssl,Ssl128
Backend

Exchange       ECP                           Required              Ssl,Ssl128
Backend

Exchange       EWS                           Required              Ssl,Ssl128
Backend

Exchange       Microsoft-Server-ActiveSync   Required              Ssl,Ssl128
Backend

Exchange       Microsoft-Server-             Required              Ssl,Ssl128
Backend        ActiveSync/Proxy

Exchange       OAB                           Required              Ssl,Ssl128
Backend

Exchange       OWA                           Required              Ssl,Ssl128
Backend

Exchange       PowerShell                    Required              Ssl,SslNegotiateCert,Ssl128
Backend

Exchange       RPC                           Required              Ssl,Ssl128
Backend

Exchange       PushNotifications             Required              Ssl,Ssl128
Backend

Exchange       RPCWithCert                   Required              Ssl,Ssl128
Backend

Exchange       MAPI/emsmdb                   Required              Ssl,Ssl128
Backend

Exchange       MAPI/nspi                     Required              Ssl,Ssl128
Backend

 ７ Note

 After the initial release, we've updated Default Website/OAB to be Accept/Allow instead of
 Required and Default Website/PowerShell to be Off instead of Required . The change to
 Default Website/OAB is because of Outlook for Mac clients not being able to download

<!-- p.712 -->

  the OAB any longer with the Required setting. The change to Default Website/PowerShell
  is because the Exchange Server default configuration doesn't allow connections using
  NTLM authentication to PowerShell Front-End virtual directory and therefore, Extended
  Protection is not applicable.

  Making modifications to the Default Website/PowerShell virtual directory is not
  supported unless explicitly advised by Microsoft Customer Service and Support (CSS).

Enabling Extended Protection by using Exchange Server 2019
CU14 (or later) installer
With Exchange Server 2019 CU14 and later , the Exchange Server 2019 Cumulative Update
(CU) installer automatically enables Extended Protection on the Mailbox server where setup is
executed. This happens for any new installation or when upgrading an existing Exchange Server
installation to the latest version.

There are two new parameters that can be used in unattended setup mode to control the
Extended Protection enabled by default behavior.

The parameters can be used to skip the automatic activation of Extended Protection
( /DoNotEnableEP ) or to not enabled Extended Protection on the Front-End EWS virtual directory
( /DoNotEnableEP_FEEWS ).

  ２ Warning

  Disabling Extended Protection makes your server vulnerable to known Exchange Server
  vulnerabilities and weakens protection against unknown threats. We recommend leaving
  this feature enabled.

Extended Protection CU installer configuration scenarios

In this section, we provide the most common scenarios for configuring Extended Protection on
Exchange Server by the help of the Exchange Server 2019 CU14 (or later) Cumulative Update
(CU) installer.

Make sure that the Exchange server is properly configured and fulfills the requirements as
outlined in the Prerequisites for enabling Extended Protection on Exchange Server section.

Scenario 1: Enable Extended Protection on an Exchange Server 2019

<!-- p.713 -->

Run the Exchange Server 2019 CU14 (or later) setup in attended or unattended mode. The
installer will configure Extended Protection as part of the installation of the server on which it
was run.

Scenario 2: Enable Extended Protection on an Exchange Server 2019
which is published via Hybrid Agent

Follow the steps as outlined in the Identifying Exchange servers that are published using
Hybrid Agent section to identify the Exchange Servers which are published via Hybrid Agent.

Run the Exchange Server 2019 CU14 (or later) setup in unattended mode by using the
/DoNotEnableEP_FEEWS parameter. It skips enabling Extended Protection on the Front-End EWS

virtual directory:

  Console

  <Virtual DVD drive letter>:\Setup.exe
  /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Upgrade
  /DoNotEnableEP_FEEWS

Scenario 3: Skip enabling of Extended Protection by Exchange Server
2019 CU14 (or later) setup

Run the Exchange Server 2019 CU14 (or later) setup in unattended mode by using the
/DoNotEnableEP parameter. It skips enabling Extended Protection:

  Console

  <Virtual DVD drive letter>:\Setup.exe
  /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Upgrade /DoNotEnableEP

  ２ Warning

  Not enabling Extended Protection makes your server vulnerable to known Exchange
  vulnerabilities and weakens protection against unknown threats. We recommend turning
  this feature on.

Enabling Extended Protection by using the PowerShell script
You can use the ExchangeExtendedProtectionManagement.ps1             script, to enable Extended
Protection on some or all your Exchange servers at once.

<!-- p.714 -->

  ） Important

  Enabling Extended Protection within your Exchange Server environment involves making
  many changes on all Exchange servers. We recommend using the script provided by
  Microsoft instead of making these changes manually via IIS Manager.

  Make sure to download the latest version of the script before running it to configure
  Extended Protection.

You can run the script on any specific Exchange Server in your environment, which has the
Exchange Management Shell (EMS) installed.

Permissions to configure Extended Protection by using the PowerShell
script

The user who runs the script, must be a member of the Organization Management role group.
The script must be executed from an elevated Exchange Management Shell (EMS).

Extended Protection script configuration scenarios
In this section, we provide the most common scenarios for configuring Extended Protection on
Exchange Server by the help of the ExchangeExtendedProtectionManagement.ps1
PowerShell script.

Read the script documentation    for more examples and a description of the script
parameters.

Scenario 1: Enable Extended Protection on all Exchange Server

Run the script as follows to enable Extended Protection on all Exchange servers within your
organization:

  PowerShell

  .\ExchangeExtendedProtectionManagement.ps1

The script performs several checks to ensure that all Exchange servers are on the minimum
required CU and SU version to enable Extended Protection. It also checks if all Exchange
servers are using the same TLS configuration.

<!-- p.715 -->

After the prerequisites checks have been passed, the script will enable Extended Protection and
add the required SSL flags on all virtual directories of all Exchange servers in scope. It stops in
case that an Exchange server doesn't fullfil the requirements (for example, if an inconsistent
TLS configuration was detected).

                                                                                               

Scenario 2: Configure Extended Protection when running a Modern
Hybrid configuration

In case you have Modern Hybrid configuration, you must skip enabling Extended Protection on
the Front-End EWS virtual directory on Exchange Servers, which were published using the
Modern Hybrid Agent.

This configuration can be done by using the ExcludeVirtualDirectories parameter:

  PowerShell

  .\ExchangeExtendedProtectionManagement.ps1 -ExchangeServerNames MHServer1,
  MHServer2 -ExcludeVirtualDirectories "EWSFrontEnd"

Enable Extended Protection by using IIS Manager

<!-- p.716 -->

If you want to enable Extended Protection in your environment manually without using the
script, you can use the following steps.

  ７ Note

  When manually enabling Extended Protection, ensure that all virtual directories on your
  Exchange servers have Extended Protected configured according as described in the table
  above.

Set Extended Protection to required or accept for on a virtual directory
   1. Launch the IIS Manager (INetMgr.exe) on the Exchange server on which you want to
     configure Extended Protection
   2. Go to Sites and select either the Default Web Site or Exchange Back End
   3. Select the virtual directory, which you want to configure
   4. Select Authentication
   5. If Windows Authentication is enabled, select Windows Authentication

                                                                                           

   6. Select Advanced Settings (on the right side) and in the opening window, select the
     suitable value from the Extended Protection dropdown

<!-- p.717 -->

                                                                                   

Set the Required SSL setting for a virtual directory
  1. Click on the virtual directory to open the home page

                                                                                        

  2. Select SSL Settings
  3. Check the Require SSL settings to make sure that Require SSL is enabled for the virtual
    directory

<!-- p.718 -->

                                                                                              

   4. Click Apply to confirm the new setting

Disabling Extended Protection
You can use the ExchangeExtendedProtectionManagement.ps1             PowerShell script to disable
Extended Protection.

  ２ Warning

  Disabling Extended Protection makes your server vulnerable to known Exchange
  vulnerabilities and weakens protection against unknown threats. We recommend leaving
  this feature enabled.

The following command will disable Extended Protection configuration for all the Exchange
Servers that are online by setting the value at all current configuring locations to None :

  PowerShell

  .\ExchangeExtendedProtectionManagement.ps1 -DisableExtendedProtection

You can also specify a subset of servers on which Extended Protection should be disabled:

  PowerShell

  .\ExchangeExtendedProtectionManagement.ps1 -DisableExtendedProtection -

<!-- p.719 -->

  ExchangeServerNames ExchServer1, ExchServer2

Renew Exchange Certificates
Renewing certificates in Exchange Server is essential to maintain secure communication and
ensure the integrity of server operations. With the evolving security landscape, the lifespan of
certificates issued by public Certificate Authorities (CA) has become shorter, necessitating more
frequent renewals, often on an annual basis.

In this section, we outline the steps to renew or replace a certificate when running Exchange
Server with an Extended Protection configuration. Particularly when running Exchange Server
with a load balancer that has SSL Bridging configured, as mentioned in the SSL Bridging
scenario section, it is required to use the same certificate on the load balancer as on the front
end of your Exchange Server.

  ２ Warning

  Modifying certificates on the load balancer or the Exchange Server can disrupt client
  connections, leading to credential popups in Outlook due to certificate mismatches.

   1. Renew expiring certificates

     As a first step, you have to create a Certificate Signing Request (CSR). To do so, follow the
     steps as outlined in the Renew an Exchange Server certificate documentation.

     Next, submit the CSR to a CA of your choice to get the new certificate issued. Follow the
     steps in the Complete a pending Exchange Server certificate request documentation to
     complete the pending request on your Exchange Server.

   2. Disable Extended Protection

     As the next step, you need to temporarily disable Extended Protection on your Exchange
     servers. Skipping this step might prevent clients from connecting to the Exchange Server
     because the certificate used on the load balancer differs from the new certificate that
     becomes active on the Exchange Server.

     To disable Extended Protection, follow the steps in the Disabling Extended Protection
     section of this documentation.

   3. Assign certificates to Exchange Server services and load balancer

     Now it's time to assign the renewed certificate to the Exchange services. You can find the
     steps to do this in the Assign certificates to Exchange Server services documentation.

<!-- p.720 -->

     In the following example, the certificate is assigned to the IIS service on all Exchange
     servers running the Mailbox role. Make sure to run this command from an elevated
     Exchange Management Shell (EMS):

       PowerShell

        Get-ExchangeServer | Where-Object { $_.ServerRole -eq "Mailbox" } | ForEach-
        Object { Enable-ExchangeCertificate -Thumbprint <thumbprint> -Server $_.Fqdn
        -Services IIS }

   4. Re-enable Extended Protection

     After assigning the renewed certificate to the Exchange Server services and replacing it on
     the load balancer or reverse proxy device, it's time to enable Extended Protection again.
     To do this, follow the steps in the Enabling Extended Protection by using the PowerShell
     script section of this documentation.

     Remember not to enable Extended Protection on the EWS front-end if you are running an
     Exchange Modern Hybrid configuration. More information can be found in the Scenario 2:
     Configure Extended Protection when running a Modern Hybrid configuration section.

Troubleshooting
This section contains known issues that exist with Extended Protection and lists some
troubleshooting tips for known failure scenarios.

Known issues with Extended Protection

All previously reported issues with Extended Protection on Exchange Server have been fixed.
We strongly recommend installing the latest Exchange Server update       for the version of
Exchange that you run in your organization to benefit from the latest fixes and improvements.

Issue: When you execute /PrepareSchema, /PrepareDomain or
/PrepareAllDomains in Exchange Server 2019 CU14 unattended mode
setup shows that Extended Protection has been activated

This is a known issue with Exchange Server 2019 CU14 which can be safely ignored. Extended
Protection isn't enabled when running /PrepareSchema , /PrepareDomain or /PrepareAllDomains
to prepare the environment as described in the Prepare Active Directory and domains for
Exchange Server documentation.
