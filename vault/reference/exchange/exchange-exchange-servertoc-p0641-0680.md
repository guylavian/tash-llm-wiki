---
title: "Exchange Server — pages 641-680"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0641-0680
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0641-0680
family: exchange
documentKind: "doc"
abstract: "This example updates the IM certificate thumbprint on all Exchange 2016 and Exchange 2019 servers in the organization. Setting override name: \"IM Override\" (must use the one already in place from previous steps since we are updating, not creating new) Skype for Business server n"
---

# Exchange Server — pages 641-680

<!-- p.641 -->

This example updates the IM certificate thumbprint on all Exchange 2016 and Exchange 2019
servers in the organization.

     Setting override name: "IM Override" (must use the one already in place from previous
     steps since we are updating, not creating new)

     Skype for Business server name: skype01.contoso.com

     Certificate thumbprint: NKT34A740E9D225A1A06193A9D44B2CE22771080

     Override reason: Configure IM

  PowerShell

  Set-SettingOverride -Name "<UniqueOverrideName>" -Component OwaServer -Section
  IMSettings -Parameters @("IMServerName=<Skype server/pool
  name>","IMCertificateThumbprint=<Certificate Thumbprint>") -Reason "
  <DescriptiveReason>" [-Server <ServerName>]

This example specifies the IM server and IM certificate thumbprint, but only on the server
named Mailbox01.

  PowerShell

  Set-SettingOverride -Identity "Mailbox01 IM Override" -Parameters
  @("IMServerName=skype01.contoso.com","IMCertificateThumbprint=NKT34A740E9D225A1A06
  193A9D44B2CE22771080") -Reason "Configure IM" -Server Mailbox01

Step 2: Refresh the IM settings on the Exchange server
Use the following syntax in the Exchange Management Shell to refresh the IM settings on the
server. You need to do this on every Exchange 2016 or Exchange 2019 server that's used for
Outlook on the web.

  PowerShell

  Get-ExchangeDiagnosticInfo -Server <ServerName> -Process
  Microsoft.Exchange.Directory.TopologyService -Component VariantConfiguration -
  Argument Refresh

This example refreshes the IM settings on the server named Mailbox01.

  PowerShell

  Get-ExchangeDiagnosticInfo -Server Mailbox01 -Process
  Microsoft.Exchange.Directory.TopologyService -Component VariantConfiguration -

<!-- p.642 -->

  Argument Refresh

Step 3: Restart the Outlook on the web pool on the Exchange
server
Run the following command in the Exchange Management Shell or in Windows PowerShell on
the server. You need to do this on every Exchange 2016 or Exchange 2019 server that's used for
Outlook on the web.

  PowerShell

  Restart-WebAppPool MSExchangeOWAAppPool

How do you know this worked?
You'll know that you've successfully configured IM integration with Outlook on the web when
the error message goes away, and clients are able to sign in to IM.

To verify the values of the IMServerName and IMCertificateThumbprint properties on an
Exchange server, replace <ServerName> with the name of the server (not the FQDN), and run
the following command:

  PowerShell

  [xml]$diag=Get-ExchangeDiagnosticInfo -Server <ServerName> -Process
  MSExchangeMailboxAssistants -Component VariantConfiguration -Argument
  "Config,Component=OwaServer";
  $diag.Diagnostics.Components.VariantConfiguration.Configuration.OwaServer.IMSettin
  gs

Note: In Exchange 2016 CU3 or earlier, you need to use different values for some of the
parameters:

     Process: Microsoft.Exchange.Directory.TopologyService (instead of
     MSExchangeMailboxAssistants ).

     Argument: Config (instead of "Config,Component=OwaServer" ).

<!-- p.643 -->

Change the offline address book
generation schedule in Exchange
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

An offline address book (OAB) is a copy of an address book that's been downloaded so that an
Outlook user can access the information it contains while disconnected from the server. By
default, a new OAB is generated every 8 hours in Exchange Server 2016 and Exchange Server
2019, but you can change the interval by using the Exchange Management Shell.

For additional management tasks related to OABs, see Procedures for offline address books in
Exchange Server.

What do you need to know before you begin?
      Estimated time to complete this procedure: 5 minutes.

      You can only use PowerShell to perform this procedure. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Offline address books" entry in
      the Email address and address book permissions topic.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

Change the offline address book generation
schedule
Changing the OAB generation schedule is a two-step process:

   1. Change the OAB generation schedule.

   2. Apply the new OAB generation schedule.

<!-- p.644 -->

Step 1: Use the Exchange Management Shell to change the
OAB generation schedule
To change the OAB generation schedule, use this syntax:

  PowerShell

  New-SettingOverride -Name "<UniqueOverrideName>" -Component TimeBasedAssistants -
  Section OABGeneratorAssistant -Parameters @("WorkCycle=<Timespan>") -Reason "
  <DescriptiveReason>" [-Server <ServerName>]

Notes:

     To specify a <TimeSpan> value, use the syntax d.hh:mm:ss , where d = days, hh = hours,
     mm = minutes, and ss = seconds.

     To configure the OAB generation schedule on all Exchange 2016 and Exchange 2019
     Mailbox servers in the Active Directory forest, don't use the Server parameter.

     To configure the OAB generation schedule on a specific Exchange 2016 or Exchange 2019
     Mailbox server, use the Server parameter and the name (not the fully qualified domain
     name or FQDN) of the server. This method is useful when you need to specify different
     OAB generation schedules on different Exchange servers.

     In Exchange 2016 Cumulative Update 3 (CU3) or earlier, the Component parameter value
     is MailboxAssistants .

This example specifies that the OAB is generated every two hours on all Exchange 2016 and
Exchange 2019 servers in the organization that are responsible for generating OABs.

     Setting override name: "OAB Generation Override" (must be unique)

     WorkCycle: 02:00:00 (2 hours)

     Override reason: Generate OAB every 2 hours

  PowerShell

  New-SettingOverride -Name "OAB Generation Override" -Component TimeBasedAssistants
  -Section OABGeneratorAssistant -Parameters @("WorkCycle=02:00:00") -Reason
  "Generate OAB every 2 hours"

This example specifies the same OAB generation schedule, but only on the server named
Mailbox01.

<!-- p.645 -->

  PowerShell

  New-SettingOverride -Name "Mailbox01 OAB Generation Override" -Component
  TimeBasedAssistants -Section OABGeneratorAssistant -Parameters
  @("WorkCycle=02:00:00") -Reason "Generate OAB every 2 hours" -Server Mailbox01

Step 2: Use the Exchange Management Shell to apply the new
OAB generation schedule
To apply the new OAB generation schedule, use this syntax:

  PowerShell

  Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
  Component VariantConfiguration -Argument Refresh [-Server <ServerName>]

Notes:

     If you didn't use the Server parameter in Step 1, don't use it here. If you used the Server
     parameter in Step 1, use the same server name here.

     If you delete the custom OAB generation schedule by using the Remove-SettingOverride
     cmdlet, you still need to run this command to change the generation schedule back to
     the default value of 8 hours.

This example applies the new OAB generation schedule on all Exchange 2016 and Exchange
2019 Mailbox servers in the organization.

  PowerShell

  Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
  Component VariantConfiguration -Argument Refresh

This example applies the new OAB generation schedule on the server named Mailbox01.

  PowerShell

  Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
  Component VariantConfiguration -Argument Refresh -Server Mailbox01

How do you know this worked?

<!-- p.646 -->

To verify that you've configured the OAB generation schedule on one or more Exchange
servers, replace <ServerName> with the name of the server (not the FQDN), and run the
following command to verify the value of the WorkCycle property:

  PowerShell

  [xml]$diag=Get-ExchangeDiagnosticInfo -Server <ServerName> -Process
  MSExchangeMailboxAssistants -Component VariantConfiguration -Argument
  "Config,Component=TimeBasedAssistants";
  $diag.Diagnostics.Components.VariantConfiguration.Configuration.TimeBasedAssistant
  s.OABGeneratorAssistant

Note: In Exchange 2016 CU3 or earlier, you need to run this command instead:
[xml]$diag=Get-ExchangeDiagnosticInfo -Server <ServerName> -Process

Microsoft.Exchange.Directory.TopologyService -Component VariantConfiguration -Argument
Config;

$diag.Diagnostics.Components.VariantConfiguration.Configuration.MailboxAssistants.OABGene
ratorAssistant .

See also
Procedures for offline address books in Exchange Server

<!-- p.647 -->

Configure certificate based authentication
in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

Certificate based authentication (CBA) in Exchange allows Outlook on the web (formerly known
as Outlook Web App) and Exchange ActiveSync clients to be authenticated by client certificates
instead of entering a username and password.

  ７ Note

  Microsoft has received inquiries from customers regarding the KB5014754: Certificate-
  based authentication changes on Windows domain controllers              update, which enforces
  a change to make certificate-based authentication more secure. We have tested this
  update with the supported versions and builds of Exchange Server, running the latest
  Exchange Server updates       , and can confirm that Exchange Servers, which are configured
  to support CBA, are not affected by this change.

Before you configure Exchange, you need to issue a client certificate to each user. Because of
the sheer number of certificates involved, you should use an automated internal public key
infrastructure (PKI) to issue and manage the client certificates. An example of an automated
internal PKI is Active Directory Certificate Services (AD CS). For more information about AD CS,
see Active Directory Certificate Services Overview.

Here's more information about the certificate requirements:

      The client certificate must be issued for client authentication (for example, the default
      User certificate template in AD CS).

      The client certificate must contain the user principal name (UPN) of the user (in the
      certificate's Subject or Subject Alternative Name fields).

      The client certificate must be associated with the user account in Active Directory.

      All servers and devices that are involved in access to Outlook on the web and ActiveSync
      (including proxy servers and client devices) must trust the entire chain of trust for the
      client certificates (the root certificate of the certification authority, and any intermediate
      CAs that were used to issue certificates).

For CBA in Outlook on the web, the client certificate needs to be installed on the local
computer, device, or on a smart card. For CBA in ActiveSync, the client certificate needs to be

<!-- p.648 -->

installed on the local device. You can automate the installation of certificates on devices by
using a mobile device management (MDM) solution like Intune. For more information about
Intune, see Overview of Microsoft Intune    .

What do you need to know before you begin?
     Estimated time to complete this task: 20 minutes

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "IIS Manager" entry in the
     Outlook on the web permissions section of the Clients and mobile devices permissions
     topic.

     To learn how to open the Exchange Management Shell in your on-premises Exchange
     organization, see Open the Exchange Management Shell.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Step 1: Use the Exchange Management Shell to
install the Client Certificate Mapping
Authentication feature on all of your Exchange
servers
All Exchange servers that share the same namespace and URLs need to use the same
authentication methods. You need to install the Client Certificate Mapping Authentication
feature on all of your Exchange servers.

In the Exchange Management Shell, run the following command:

  PowerShell

  Install-WindowsFeature Web-Client-Auth

For detailed syntax and parameter information, see Install-WindowsFeature.

<!-- p.649 -->

Step 2: Use IIS Manager to enable Active Directory
Client Certificate Authentication for the Exchange
server
 1. Open IIS Manager on the Exchange server. An easy way to do this in Windows Server
   2012 or later is to press Windows key + Q, type inetmgr, and select Internet Information
   Services (IIS) Manager in the results.

 2. Select the server, and verify Features View is selected at the bottom of the page.

 3. In the IIS section, double-click Authentication.

 4. On the Authentication page that opens, select Active Directory Client Certificate
   Authentication from the list, and in the Actions pane, click Enable.

<!-- p.650 -->

     You'll see a warning that SSL must be enabled to use Active Directory Client Certificate
     Mapping.

Step 3: Use IIS Manager to configure the Outlook
on the web, Exchange admin center, and
ActiveSync virtual directories to require client
certificates
Note: You need to require client certificates, because accepting client certificates (to support
both CBA and regular username and password authentication) doesn't work consistently across
all types of ActiveSync devices.

   1. In IIS Manager, expand the server, expand Sites, and then expand Default Web Site.

   2. Select the owa virtual directory, and verify Features View is selected at the bottom of the
     page.

   3. In the IIS section, double-click SSL Settings.

   4. On the SSL Settings page, verify Require SSL is checked, and select the Client certificates
     value Require.

   5. In the Actions pane, click Apply.

   6. Select the Microsoft-Server-ActiveSync virtual directory.

<!-- p.651 -->

   7. In the IIS section, double-click SSL Settings.

   8. On the SSL Settings page, verify Require SSL is checked, and select the Client certificates
     value Require.

   9. In the Actions pane, click Apply.

Note: Although you can perform these procedures on the command line, the steps might not
configure a required registry key. You can use the earlier procedures in IIS Manager (which will
definitely set the registry key correctly), or you need to verify that the registry key
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\HTTP\Parameters\SslBindingInfo\0.0.0
.0:443 is set to the value 1 after you perform the procedures on the command line.

To perform these procedures on the command line, open an elevated command prompt on the
Exchange server (a Command Prompt window you open by selecting Run as administrator)
and run the following commands:

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/owa/" -
  section:system.webserver/security/access /sslFlags:"Ssl, SslRequireCert"
  /commit:apphost

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/ecp/" -
  section:system.webserver/security/access /sslFlags:"Ssl, SslRequireCert"
  /commit:apphost

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/Microsoft-
  Server-ActiveSync/" -section:system.webserver/security/access /sslFlags:"Ssl,
  SslRequireCert" /commit:apphost

Step 4: Use the Exchange Management Shell to
disable authentication other authentication
methods on the Outlook on the web, Exchange
admin center, and ActiveSync virtual directories
After you require client certificates for authentication, you need to disable all other
authentication methods on the Outlook on the web, Exchange admin center (EAC) and

<!-- p.652 -->

ActiveSync virtual directories. By default, only Basic authentication and Forms authentication
are enabled.

   1. In the Exchange Management Shell, replace <ServerName> with the name of your
     Exchange server, and run the following command to disable all other authentication
     methods on the Outlook on the web virtual directory:

       PowerShell

        Set-OwaVirtualDirectory "<ServerName>\owa (Default Web Site)" -
        BasicAuthentication $false -WindowsAuthentication $false -
        DigestAuthentication $false -FormsAuthentication $false -AdfsAuthentication
        $false -OAuthAuthentication $false

     For detailed syntax and parameter information, see Set-OwaVirtualDirectory.

   2. In the Exchange Management Shell, replace <ServerName> with the name of your
     Exchange server, and run the following command to disable all other authentication
     methods on the EAC virtual directory:

       PowerShell

        Set-EcpVirtualDirectory "<ServerName>\ecp (Default Web Site)" -
        BasicAuthentication $false -WindowsAuthentication $false -
        DigestAuthentication $false -FormsAuthentication $false -AdfsAuthentication
        $false

     For detailed syntax and parameter information, see Set-EcpVirtualDirectory.

   3. Replace <ServerName> with the name of your Exchange server, and run the following
     command to disable all other authentication methods on the ActiveSync virtual directory:

       PowerShell

        Set-ActiveSyncVirtualDirectory "<ServerName>\Microsoft-Server-ActiveSync
        (Default Web Site)" -BasicAuthEnabled $false -WindowsAuthEnabled $false

     For detailed syntax and parameter information, see Set-ActiveSyncVirtualDirectory.

Step 5: Use IIS Manager to enable client certificate
mapping for the Outlook on the web, Exchange
admin center, and ActiveSync virtual directories

<!-- p.653 -->

） Important

After you perform this step, running the Set-ActiveSyncVirtualDirectory cmdlet might
disable the client certificate mapping for ActiveSync.

1. In IIS Manager, expand the server, expand Sites, and then expand Default Web Site.

2. Select the owa virtual directory, and verify Features View is selected at the bottom of the
   page.

3. In the Management section, double-click Configuration Editor.

4. On the Configuration Editor page, click the drop down on Section, and navigate to
   system.webServer > security > authentication >
   clientCertificateMappingAuthentication.

5. Set the enabled value to True, and in the Actions pane, click Apply.

6. Select the ecp virtual directory.

7. In the Management section, double-click Configuration Editor.

8. On the Configuration Editor page, click the drop down on Section, and navigate to
   system.webServer > security > authentication >
   clientCertificateMappingAuthentication.

<!-- p.654 -->

   9. Set the enabled value to True, and in the Actions pane, click Apply.

 10. Select the Microsoft-Server-ActiveSync virtual directory.

 11. In the Management section, double-click Configuration Editor.

 12. On the Configuration Editor page, click the drop down on Section, and navigate to
     system.webServer > security > authentication >
     clientCertificateMappingAuthentication.

 13. Set the enabled value to True, and in the Actions pane, click Apply.

Note: To perform these procedures on the command line, open an elevated command prompt
on the Exchange server and run the following commands:

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/owa/" -
  section:system.webserver/security/authentication/clientCertificateMappingAuthentic
  ation /enabled:"True" /commit:apphost

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/ecp/" -
  section:system.webserver/security/authentication/clientCertificateMappingAuthentic
  ation /enabled:"True" /commit:apphost

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/Microsoft-
  Server-ActiveSync/" -
  section:system.webserver/security/authentication/clientCertificateMappingAuthentic
  ation /enabled:"True" /commit:apphost

Step 6 (Optional): Add the root certificate of a
third-party certification authority to the Enterprise
NTAuth store in Active Directory
You only need to perform this step if you aren't using AD CS to issue the client certificates. This
setting indicates that the certification authority (CA) is trusted to issue client certificates for
Active Directory authentication.

<!-- p.655 -->

   1. Export the CA's root certificate to a Base-64 encoded or DER binary encoded X.509 .cer
     file. In this example, we'll use C:\Data\CARoot.cer.

   2. On any domain member server (for example, a domain controller or an Exchange server),
     open an elevated command prompt run the following command:

       Console

        %windir%\system32\certutil.exe -enterprise -addstore NTAuth
        "C:\Data\CARoot.cer"

     Note that this step requires membership in the Enterprise Admins group.

Step 7 (Optional): Use IIS Manager to increase the
UploadReadAheadSize value for the Outlook on
the web and ActiveSync virtual directories
If your clients receive errors, you might need to increase the uploadReadAheadSize values in
the IIS metabase to allow for the request headers.

   1. In IIS Manager, expand the server, expand Sites, and then expand Default Web Site.

   2. Select the owa virtual directory, and verify Features View is selected at the bottom of the
     page.

   3. In the Management section, double-click Configuration Editor.

   4. On the Configuration Editor page, click the drop down on Section, and navigate to
     systemwebServer > serverRuntime.

<!-- p.656 -->

 5. Set the uploadReadAheadSize value to 49152, and in the Actions pane, click Apply.

 6. Select the ecp virtual directory.

 7. In the Management section, double-click Configuration Editor.

 8. On the Configuration Editor page, click the drop down on Section, and navigate to
   systemwebServer > serverRuntime.

 9. Set the uploadReadAheadSize value to 49152, and in the Actions pane, click Apply.

10. Select the Microsoft-Server-ActiveSync virtual directory.

11. In the Management section, double-click Configuration Editor.

<!-- p.657 -->

 12. On the Configuration Editor page, click the drop down on Section, and navigate to
     systemwebServer > serverRuntime.

 13. Set the uploadReadAheadSize value to 49152, and in the Actions pane, click Apply.

Note: To perform these procedures on the command line, open an elevated command prompt
on the Exchange server and run the following commands:

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/owa/" -
  section:system.webserver/serverRuntime /uploadReadAheadSize:49152

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/ecp/" -
  section:system.webserver/serverRuntime /uploadReadAheadSize:49152

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/Microsoft-
  Server-ActiveSync/" -section:system.webserver/serverRuntime
  /uploadReadAheadSize:49152

<!-- p.658 -->

Enabling Modern Auth in Exchange on-
premises
ﾃ   Summarize this article for me

APPLIES TO:         2016            2019   Subscription Edition

Overview
Starting with Exchange Server 2019 CU13, Exchange Server supports OAuth 2.0 (also known as
Modern Authentication ) for pure on-premises environments using ADFS as a Security Token

Service (STS). This document provides the prerequisites and steps to enable this feature.

Modern Auth in Exchange Server 2019 shouldn't be confused with Hybrid Modern
Authentication (HMA), which uses Microsoft Entra ID for Modern Authentication. In fact, HMA
is still the recommended method to enable Modern Auth for all on-premises and cloud users
in an Exchange Hybrid configuration. This new feature enables the use of Modern Auth for
organizations who do not have Microsoft Entra ID or are not in an Exchange Hybrid
configuration.

How will Modern Authentication work and is this
feature applicable to me?
With Modern Auth, users can authenticate to Exchange using ADFS. When Modern Auth is
enabled for a user, their Outlook client is redirected to ADFS. Users can then authenticate by
providing credentials or performing multi-factor authentication. Once ADFS authenticates a
user, it generates access tokens. Exchange Server validates these access tokens to provide
client access to the user's mailbox.

The following diagram illustrates the coordination between Exchange Server, ADFS and
Outlook to authenticate a user using Modern Auth.

<!-- p.659 -->


    In the previous chart, steps 3a , 4a , 5a and 6a take place when Modern Auth is enabled for the
    end user. Steps 3b , 4b occur when Modern Auth is disabled for a user.

    Refer to the following table to evaluate if this feature is applicable for you.

                                                                                        ﾉ   Expand table

     Exchange Configuration                        Is this feature   Remarks
                                                   applicable?

     On-Premises Exchange organization with only   Yes               N/A
     Exchange Server 2019

     On-Premises Exchange organization with mix    No                Exchange Server 2013 is out of
     of Exchange Server 2019, Exchange Server                        support.
     2016, and Exchange Server 2013

<!-- p.660 -->

 Exchange Configuration                        Is this feature   Remarks
                                               applicable?

 On-Premises Exchange organization with mix    Yes               Only Exchange 2019 servers can be
 of Exchange Server 2019 and Exchange Server                     used as Front-End (Client Access)
 2016                                                            Servers.

 Exchange Hybrid organization using HMA        No                HMA using Microsoft Entra ID is the
                                                                 preferred solution. Refer to the
                                                                 guidance on using new auth policies.

 Exchange Hybrid organization without HMA      No                Use HMA with Microsoft Entra ID.

Prerequisites to enable Modern Authentication in
Exchange

Exchange Server 2019 CU13 or later
To use Modern Auth, all servers used for client connections must have Exchange Server 2019
CU13 or later installed. ADFS Modern Auth in Outlook for Mac (Microsoft 365) requires
Exchange Server Subscription Edition (SE) with the December 2025 or later Security Update.

ADFS 2019 or later
To enable Modern Auth in an on-premises Exchange environment, Active Directory Federation
Services (ADFS) on Windows Server 2019 or later is required. It's unsupported to install and
configure the ADFS role on an Exchange Server. For more information, see Plan Your AD FS
Deployment Topology.

You may also need Web Application Proxy Server (on Windows Server 2019 or later) to enable
client access from outside corporate network. Read the (Optional) Configure Web Application
Proxy can be configured for Extranet Access section for more details.

Client prerequisites
To utilize Modern Auth, users require client applications, such as Outlook or other native
operating system clients, which are compatible with Modern Auth via ADFS.

Outlook on Windows

<!-- p.661 -->

Support for Modern Auth via ADFS is available in the following versions of Microsoft Outlook
for Windows . The Microsoft Outlook Windows client, starting from build number

16.0.17628.10000 , utilizes the latest MSAL library for authentication. To ensure you are using

the most up-to-date authentication stack, it is recommended to install the latest version.

Outlook in Microsoft 365 Apps:

                                                                                     ﾉ   Expand table

 Channel                                            Supported      Version         Build (or later)

 Insider Channel                                    Yes            2304            16327.20200

 Current Channel                                    Yes            2304            16327.20214

 Monthly Enterprise Channel                         Yes            2304            16327.20324

 Semi-Annual Enterprise Channel (Preview)           Yes            2402            17328.20184

 Semi-Annual Enterprise Channel                     Yes            2402            17328.20452

Outlook for Windows (volume license & retail):

                                                                                     ﾉ   Expand table

 Version                                    Supported       Version          Build (or later)

 Outlook 2016 (Any version)                 No              N/A              N/A

 Outlook 2019 (Any version)                 No              N/A              N/A

 Outlook 2021 (Retail)                      Yes             2304             16327.20214

 Outlook 2021 (Volume)                      No              N/A              N/A

 Outlook 2024 (Retail)                      Yes             2410             18129.20158

 Outlook 2024 (Volume)                      Yes             2408             17932.20162

You can check the build number of your Office by following steps mentioned here .

Outlook on Mac

Support for Modern Auth via ADFS is available in Outlook for Mac (Microsoft 365) through
Microsoft 365 starting from build number 16.106 (Build 26020821) . Note that Modern Auth
via ADFS is currently not supported in the standalone versions such as Outlook 2024 for Mac .

<!-- p.662 -->

Windows OS
The Windows client must be Windows 11 22H2 or later and it must have the March 14, 2023
update      installed.

You can review Windows Update history to verify that KB5023706 is installed.

                                                                                              

Apple platforms

Support for Modern Auth via ADFS is available in the Apple Mail app starting with macOS
Sequoia and iOS 17.6.1 , and in Outlook for Mac (Microsoft 365) starting with macOS Sequoia .

Protocols that work with ADFS Modern Auth
The following table outlines the protocols that can be accessed by utilizing ADFS Modern Auth
tokens. We're continuously working to add ADFS Modern Auth support to more Exchange
Server protocols.

                                                                                   ﾉ   Expand table

 Protocol                                      ADFS Modern Auth Supported

 MAPI over HTTP (MAPI/HTTP)                    Yes

 Outlook Anywhere (RPC/HTTP)                   No

 Exchange Active Sync (EAS)                    Yes

 Exchange Web Services (EWS)                   Yes

 Outlook on the Web (OWA)                      Yes (claims-based authentication)

 Exchange Admin Center (ECP)                   Yes (claims-based authentication)

 Offline Address Book (OAB)                    Yes

 IMAP                                          No

 POP                                           No

<!-- p.663 -->

Steps to configure Modern Authentication in
Exchange Server using ADFS as STS
This section provides details on to implement Modern Auth in Exchange Server 2019 CU13.

Install Exchange 2019 CU13 on all FE Servers (at least)
All servers used for client connections must be upgraded to Exchange 2019 CU13. This
approach ensures that initial client connections to Exchange 2019 use OAuth, and proxied
connections to Exchange Server 2016 use Kerberos.

Exchange 2019 CU13 adds support for new authentication policies to allow or block Modern
Auth at user level. Blocking Modern Auth is used to ensure clients that don't support Modern
Auth can still connect.

Running /PrepareAD with Setup is required to add several new authentication policy
parameters to Exchange Server.

   1. BlockModernAuthActiveSync
   2. BlockModernAuthAutodiscover
   3. BlockModernAuthImap
   4. BlockModernAuthMapi
   5. BlockModernAuthOfflineAddressBook
   6. BlockModernAuthPop
   7. BlockModernAuthRpc
   8. BlockModernAuthWebServices

After installing CU13 or later, any pre-existing auth policies (including the default
authentication policy) have the parameters disabled. That means that if you're already using
HMA you don't need to change the pre-existing auth policies.

No new authentication policy required for Exchange Hybrid
Existing Exchange Hybrid configurations should use Hybrid Modern Auth (HMA). Hybrid
installations using HMA can leave the values of the BlockModernAuth* parameters at 0 to
continue using HMA. The steps outlined for setting up Modern Auth with ADFS are only
relevant for organizations who aren't using Exchange Hybrid and are purely on-premises.

Set up Active Directory Federation Services (ADFS)

<!-- p.664 -->

You need to install and configure ADFS in the environment to allow Exchange clients to use
Forms authentication (OAuth) to connect to Exchange Server. Refer to the Checklist: Setting Up
a Federation Server to assist with your ADFS configuration.

The ADFS feature can be installed by running the following command from an elevated
PowerShell window on the new server that becomes the ADFS server:

  PowerShell

  Install-WindowsFeature ADFS-Federation -IncludeManagementTools

Certificate requirements for ADFS configuration in Exchange Server
Organization

ADFS requires two basic types of certificates (refer this article for detailed information):

   1. A service communication Secure Sockets Layer (SSL) certificate for encrypted web services
      traffic between the ADFS server, clients, Exchange servers, and the optional Web
      Application Proxy server. We recommend that you use a certificate that's issued by an
      internal or commercial certification authority (CA), because all clients need to trust this
      certificate.
   2. A token-signing certificate for encrypted communication and authentication between the
      ADFS server, Active Directory domain controllers, and Exchange servers. You can obtain a
      token-signing certificate by requesting one from a CA or by creating a self-signed
      certificate.

For more information about creating and importing SSL certificates in Windows, see Server
Certificates.

Here's a summary of the certificates that we're using in this scenario:

                                                                                    ﾉ   Expand table

 Common name (CN) in the certificate    Type      Required on    Comments
 (in the Subject, Subject Alternative             servers
 Name, or a wildcard certificate
 match)

 adfs.contoso.com                       Issued    ADFS server,   Federation servers use an SSL
 enterpriseregistration.contoso.com     by a CA   Web            certificate to secure Web services
                                                  Application    traffic for SSL communication with
                                                  Proxy server   clients and with federation server
                                                  (optional)     proxies.

<!-- p.665 -->

Common name (CN) in the certificate     Type       Required on    Comments
(in the Subject, Subject Alternative               servers
Name, or a wildcard certificate
match)

                                                                  Because the SSL certificate must be
                                                                  trusted by client computers, we
                                                                  recommend that you use a certificate
                                                                  that is signed by a trusted CA. All
                                                                  certificates that you select must have
                                                                  a corresponding private key.

ADFS Token Signing - adfs.contoso.com   Self-      ADFS server,   A token-signing certificate is an X509
                                        signed     Web            certificate. Federation servers use
                                        or issue   Application    associated public/private key pairs to
                                        by a CA    Proxy server   digitally sign all security tokens that
                                                   (optional)     they produce. This process includes
                                                                  the signing of published federation
                                                                  metadata and artifact resolution
                                                                  requests.

                                                                  You can have multiple token-signing
                                                                  certificates configured in the ADFS
                                                                  Management snap-in to allow for
                                                                  certificate rollover when one
                                                                  certificate is close to expiring. By
                                                                  default, all the certificates in the list
                                                                  are published, but only the primary
                                                                  token-signing certificate is used by
                                                                  ADFS to actually sign tokens. All
                                                                  certificates that you select must have
                                                                  a corresponding private key.

                                                                  You can obtain a token-signing
                                                                  certificate by requesting one from an
                                                                  enterprise CA or a public CA or by
                                                                  creating a self-signed certificate.

mail.contoso.com                        Issued     Exchange       This certificate is the typical
autodiscover.contoso.com                by a CA    servers,       certificate that's used to encrypt
                                                   Web            external client connections to
                                                   Application    Outlook on the web (and other
                                                   Proxy server   Exchange services). For more
                                                   (optional)     information, see Certificate
                                                                  requirements for Exchange services.

Deploy and Configure ADFS Server

<!-- p.666 -->

Use Windows Server 2019 or later to deploy an ADFS server. Follow the steps in the Deploy an
ADFS server and Configure and test the ADFS server documentation. Ensure that the federation
metadata URL can be accessed in a web browser from both the Exchange server and at least
one client machine.

The URL uses this syntax: https://<FederationServiceName>/federationmetadata/2007-
06/federationmetadata.xml

Example: https://adfs.contoso.com/federationmetadata/2007-06/federationmetadata.xml

Configure Authentication Method in ADFS

To use Modern Auth in Outlook on Windows, you need to configure the Primary
Authentication Methods . We recommend choosing Forms Authentication for both Extranet

and Intranet . This configuration can be done by running the following commands from a
PowerShell window on the ADFS server:

 PowerShell

 Set-AdfsGlobalAuthenticationPolicy -PrimaryIntranetAuthenticationProvider
 FormsAuthentication
 Set-AdfsGlobalAuthenticationPolicy -PrimaryExtranetAuthenticationProvider
 FormsAuthentication

Choose appropriate SSO Lifetime
Choose an appropriate Single Sign-On (SSO) lifetime so end users aren't required to frequently
reauthenticate. To validate the current SSO lifetime configuration, open a new PowerShell
window on the ADFS server and execute the following command:

 PowerShell

 Get-AdfsProperties | Format-List SsoLifetime, PersistentSsoLifetimeMins,
 KmsiLifetimeMins, DeviceUsageWindowInDays, KmsiEnabled, PersistentSsoEnabled,
 BrowserSsoEnabled

Use the Set-AdfsProperties cmdlet to configure the appropriate values for SsoLifetime ,
PersistentSsoLifetimeMins , KmsiLifetimeMins , and DeviceUsageWindowInDays . These settings

should be adjusted to enable SSO and define its expiry. Depending on the SSO mode, such as
Keep Me Signed In (KMSI) or Device registration , you may also need to enable KsmiEnabled

and PersistentSsoEnabled . More details about ADFS SSO can be found in the AD FS 2016
Single Sign On Settings documentation.

<!-- p.667 -->

Configure device registration in ADFS
It's recommended to enable the Device Registration feature in ADFS to benefit from an
improved SSO experience. To enable Device Registration , follow the steps outlined in the
Configure a federation server with Device Registration Service documentation.

Next, complete all the steps to configure Device Registration Service Discovery and the
Device Registration Discovery Server SSL certificate , as described in the Configuring
Device Registration documentation.

To use device registration, end users must join their device to a Workplace. More details can be
found in the following documentations:

     Walkthrough: Workplace Join with a Windows Device
     Walkthrough: Workplace Join with an iOS Device
     Walkthrough: Workplace Join to an Android device

Verify that device registration is configured, and device authentication is enabled by checking
the Device Registration Overview . This step is recommended to reduce the number of
authentication prompts for users and can help enforce Access Control Policies in ADFS.

Configure KSMI in ADFS
If you prefer not to use Device Registration or are unable to do so, you can enable the Keep
Me Signed In feature instead. ADFS then creates a persistent cookie immediately after user
authentication, eliminating the need for reauthentication in subsequent sessions, provided the
cookie remains valid.

The expiration time of the refresh token is equal the persistent SSO cookie's lifetime for Keep
me signed in . The persistent SSO cookie lifetime is one day by default with maximum of seven

days. Otherwise, refresh token lifetime equals session SSO cookie lifetime (8 hours by default).
More information about KSMI can be found in the AD FS single sign-on settings
documentation.

KMSI is disabled by default and can be enabled by setting the ADFS property KmsiEnabled to
True . Make sure to run the following steps from a PowerShell window on your ADFS server:

 PowerShell

 Set-AdfsProperties -EnableKmsi $true

With KMSI disabled, the default single sign-on period is 8 hours . The single sign-on period can
be configured using the property SsoLifetime . The property is measured in minutes, so its

<!-- p.668 -->

default value is 480 :

  PowerShell

  Set-AdfsProperties -SsoLifetime <LifetimeInMinutes>

With KMSI enabled, the default single sign-on period is 24 hours . The single sign-on period
with KMSI enabled can be configured using the property KmsiLifetimeMins . The property is
measured in minutes, so its default value is 1440 :

  PowerShell

  Set-AdfsProperties -KmsiLifetimeMins <LifetimeInMinutes>

Create the ADFS Outlook Application Group

If this is your first time configuring ADFS Modern Authentication in Exchange on-premises,
please follow the steps in this section of the guide. If you have an existing ADFS Modern
Authentication configuration that was set up before support for clients other than Microsoft
Outlook for Windows , refer to the steps in the Update the existing ADFS Outlook Application

Group section of this documentation. The following PowerShell commands must be executed
from a PowerShell window on your ADFS server. If you don't plan to use iOS and macOS
applications, such as the native Apple Mail app, you can skip creating the ADFS native client
application for iOS and macOS. However, we recommend creating them for the sake of
completeness.

First, we're going to create the ADFS Application Group :

  PowerShell

  New-AdfsApplicationGroup -Name "Outlook" -ApplicationGroupIdentifier "Outlook" -
  Disabled:$false

Next we create three more Scopes - EAS.AccessAsUser.All , EWS.AccessAsUser.All and
offline_access :

  PowerShell

  Add-AdfsScopeDescription -Name "EAS.AccessAsUser.All" -Description "EAS scope"
  Add-AdfsScopeDescription -Name "EWS.AccessAsUser.All" -Description "EWS scope"
  Add-AdfsScopeDescription -Name "offline_access" -Description "Offline Access"

<!-- p.669 -->

Now, we're creating two Native Client Applications - Outlook - Native application and iOS
and macOS - Native mail application :

 PowerShell

 Add-AdfsNativeClientApplication -Name "Outlook - Native application" -
 ApplicationGroupIdentifier "Outlook" -Identifier "d3590ed6-52b3-4102-aeff-
 aad2292ab01c" -RedirectUri @("ms-appx-web://Microsoft.AAD.BrokerPlugin/d3590ed6-
 52b3-4102-aeff-
 aad2292ab01c","msauth.com.microsoft.Outlook://auth","urn:ietf:wg:oauth:2.0:oob")
 Add-AdfsNativeClientApplication -Name "iOS and macOS - Native mail application" -
 ApplicationGroupIdentifier "Outlook" -Identifier "f8d98a96-0999-43f5-8af3-
 69971c7bb423" -RedirectUri @("com.apple.mobilemail://oauth-
 redirect","com.apple.preferences.internetaccounts://oauth-
 redirect/","com.apple.Preferences://oauth-redirect/")

As a next step, we create Web Api Applications . We create one application per URI that is used
in your Exchange Server environment. If you use, for example, autodiscover.contoso.com and
mail.contoso.com , you must create two Web Api Applications . Make sure to replace the URIs

in the following example with the URIs, which you use in your setup. It's important to make
sure all client-facing URIs are covered. Include the trailing / and make sure that the URIs start
with https:// :

 PowerShell

 # Replace the URIs with your URIs
 $exchangeServerServiceFqdns =
 @("https://autodiscover.contoso.com/","https://mail.contoso.com/")

 $issuanceTransformRules = @"
 @RuleName = "ActiveDirectoryUserSID"
 c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/primarysid"]
  => issue(claim = c);

 @RuleName = "ActiveDirectoryUPN"
 c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn"]
  => issue(claim = c);

 @RuleName = "AppIDACR"
  => issue(Type = "appidacr", Value = "2");

 @RuleName = "SCP"
  => issue(Type = "scp", Value = "user_impersonation");

 @RuleName = "SCPEAS"
  => issue(Type = "scp", Value = "EAS.AccessAsUser.All");

 @RuleName = "SCPEWS"
  => issue(Type = "scp", Value = "EWS.AccessAsUser.All");

<!-- p.670 -->

 @RuleName = "offlineaccess"
   => issue(Type = "scp", Value = "offline_access");
 "@
 foreach ($fqdn in $exchangeServerServiceFqdns) {
      Add-AdfsWebApiApplication -Name "Outlook - Web API ($((New-
 Guid).ToString("N")))" -ApplicationGroupIdentifier "Outlook" -Identifier $fqdn -
 IssuanceTransformRules $issuanceTransformRules -AccessControlPolicyName "Permit
 Everyone"
 }

As a last step, we add the client permissions for all of the Native Client Applications in the
existing Web Api Applications :

 PowerShell

 $clientRoleIdentifier = @("f8d98a96-0999-43f5-8af3-69971c7bb423","d3590ed6-52b3-
 4102-aeff-aad2292ab01c")
 (Get-AdfsWebApiApplication -ApplicationGroupIdentifier "Outlook") | ForEach-Object
 {
      [string]$serverRoleIdentifier = $_.Identifier
      foreach ($id in $clientRoleIdentifier) {
          Grant-AdfsApplicationPermission -ClientRoleIdentifier $id -
 ServerRoleIdentifier $serverRoleIdentifier -ScopeNames
 "winhello_cert","email","profile","vpn_cert","logon_cert","user_impersonation","all
 atclaims","offline_access","EAS.AccessAsUser.All","EWS.AccessAsUser.All","openid","
 aza"
      }
 }

Update the existing ADFS Outlook Application Group

  ） Important

  Skip the steps in this section if you don't have an existing ADFS Outlook Application
  Group, which was configured before support for clients other than Microsoft Outlook for
  Windows was introduced.

If you have an existing ADFS Outlook Application Group configuration, which was set up before
support for clients other than Microsoft Outlook for Windows was introduced, follow the steps
here to enable support for other platforms. The following PowerShell commands must be
executed from a PowerShell window on your ADFS server.

First we're creating three extra Scopes - EAS.AccessAsUser.All , EWS.AccessAsUser.All and
offline_access :

<!-- p.671 -->

 PowerShell

 Add-AdfsScopeDescription -Name "EAS.AccessAsUser.All" -Description "EAS scope"
 Add-AdfsScopeDescription -Name "EWS.AccessAsUser.All" -Description "EWS scope"
 Add-AdfsScopeDescription -Name "offline_access" -Description "Offline Access"

Now, we're creating a new Native Client Applications - iOS and macOS - Native mail
application :

 PowerShell

 Add-AdfsNativeClientApplication -Name "iOS and macOS - Native mail application" -
 ApplicationGroupIdentifier "Outlook" -Identifier "f8d98a96-0999-43f5-8af3-
 69971c7bb423" -RedirectUri @("com.apple.mobilemail://oauth-
 redirect","com.apple.preferences.internetaccounts://oauth-
 redirect/","com.apple.Preferences://oauth-redirect/")

We update the existing Native Client Application - Outlook - Native application . Make sure
to replace the TargetName with the target name that you're using in the existing configuration:

 PowerShell

 Set-AdfsNativeClientApplication -TargetName "Outlook - Native application" -
 RedirectUri @("ms-appx-web://Microsoft.AAD.BrokerPlugin/d3590ed6-52b3-4102-aeff-
 aad2292ab01c","msauth.com.microsoft.Outlook://auth","urn:ietf:wg:oauth:2.0:oob")

As a next step, we must create one Web Api Application for each Identifier (URI) which is
used in your Exchange Server environment and exists in your current ADFS Modern
Authentication configuration:

 PowerShell

 $duplicateFqdnHashSet = New-Object System.Collections.Generic.HashSet[string]
 $issuanceTransformRules = @"
 @RuleName = "ActiveDirectoryUserSID"
 c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/primarysid"]
  => issue(claim = c);

 @RuleName = "ActiveDirectoryUPN"
 c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn"]
  => issue(claim = c);

 @RuleName = "AppIDACR"
  => issue(Type = "appidacr", Value = "2");

 @RuleName = "SCP"
  => issue(Type = "scp", Value = "user_impersonation");

<!-- p.672 -->

 @RuleName = "SCPEAS"
  => issue(Type = "scp", Value = "EAS.AccessAsUser.All");

 @RuleName = "SCPEWS"
  => issue(Type = "scp", Value = "EWS.AccessAsUser.All");

 @RuleName = "offlineaccess"
   => issue(Type = "scp", Value = "offline_access");
 "@
 (Get-AdfsWebApiApplication -ApplicationGroupIdentifier "Outlook") | ForEach-Object
 {
      if ($_.Identifier.Count -gt 1) {
          Write-Host "[+] More than one identifier was found in Web Api Application:
 $($_.Name)" -ForegroundColor Yellow
          $_.Identifier | Select-Object -Skip 1 | ForEach-Object {
              Write-Host "[+] Identifier $_ must be added to a new Web Api
 Application and will now be removed from the existing one" -ForegroundColor Yellow
              [void]$duplicateFqdnHashSet.Add($_)
          }

         Set-AdfsWebApiApplication -TargetName $_.Name -Identifier ($_.Identifier)
 [0] -IssuanceTransformRules $issuanceTransformRules -AccessControlPolicyName
 "Permit Everyone"
     }
 }

 foreach($identifier in $duplicateFqdnHashSet) {
     Write-Host "[+] Creating a new Web Api Application for: $identifier" -
 ForegroundColor Yellow
     Add-AdfsWebApiApplication -Name "Outlook - Web API ($((New-
 Guid).ToString("N")))" -ApplicationGroupIdentifier "Outlook" -Identifier
 $identifier -IssuanceTransformRules $issuanceTransformRules -
 AccessControlPolicyName "Permit Everyone"
     Write-Host "[+] Done!`r`n" -ForegroundColor Green
 }

As a last step, we add the client permissions for all of the Native Client Applications in the
existing Web Api Applications :

 PowerShell

 $clientRoleIdentifier = @("f8d98a96-0999-43f5-8af3-69971c7bb423","d3590ed6-52b3-
 4102-aeff-aad2292ab01c")
 $requiredScopes =
 @("winhello_cert","email","profile","vpn_cert","logon_cert","user_impersonation","a
 llatclaims","offline_access","EAS.AccessAsUser.All","EWS.AccessAsUser.All","openid"
 ,"aza")

 (Get-AdfsWebApiApplication -ApplicationGroupIdentifier "Outlook") | ForEach-Object
 {
     [string]$serverRoleIdentifier = $_.Identifier
     Write-Host "[+] Processing Server Role: $serverRoleIdentifier" -ForegroundColor
 Yellow

<!-- p.673 -->

     foreach ($id in $clientRoleIdentifier) {
         Write-Host "[+] Processing Client Role: $id" -ForegroundColor Yellow
         $permissionEntry = Get-AdfsApplicationPermission | Where-Object {
 $_.ClientRoleIdentifier -eq $id -and $_.ServerRoleIdentifier -eq
 $serverRoleIdentifier }
         if ($null -eq $permissionEntry) {
             Write-Host "[+] No Application Permission found for Client Role: $id -
 Server Role: $serverRoleIdentifier" -ForegroundColor Yellow
             Grant-AdfsApplicationPermission -ClientRoleIdentifier $id -
 ServerRoleIdentifier $serverRoleIdentifier -ScopeNames $requiredScopes
         } else {
             Write-Host "[+] Application Permission found - validating Scopes" -
 ForegroundColor Yellow
             $missingScopesList = New-Object System.Collections.Generic.List[string]
             $requiredScopes | ForEach-Object {
                 if ($_ -in $permissionEntry.ScopeNames) {
                     Write-Host "[+] Scope: $_ is already set!" -ForegroundColor
 Green
                 } else {
                     Write-Host "[+] Scope: $_ is missing and must be added" -
 ForegroundColor Yellow
                     $missingScopesList.Add($_)
                 }
             }

             if ($missingScopesList.Count -ge 1) {
                 Write-Host "[+] The following Scopes will be added:
 $([string]::Join(", ", $missingScopesList))" -ForegroundColor Yellow
                 Set-AdfsApplicationPermission -TargetClientRoleIdentifier $id -
 TargetServerRoleIdentifier $serverRoleIdentifier -AddScope $missingScopesList
                 Write-Host "[+] Done!`r`n" -ForegroundColor Green
             } else {
                 Write-Host "[+] There is nothing to do!`r`n" -ForegroundColor Green
             }
         }
     }
 }

Remove existing ADFS Outlook Application Group

  Ｕ Caution

  Following the steps in this section removes the existing ADFS Outlook Application Group
  configuration.

If you have an existing ADFS Outlook Application Group configuration and you want to remove
it, follow the steps here to delete the existing configuration. All of the following PowerShell
commands must be executed from a PowerShell window on your ADFS server.

<!-- p.674 -->

First, we're going to delete the ADFS Application Group :

 PowerShell

 Remove-AdfsApplicationGroup -TargetApplicationGroupIdentifier "Outlook"

As a last step, we delete the custom Scopes which were added:

 PowerShell

 Remove-AdfsScopeDescription -TargetName "EAS.AccessAsUser.All"
 Remove-AdfsScopeDescription -TargetName "EWS.AccessAsUser.All"
 Remove-AdfsScopeDescription -TargetName "offline_access"

(Optional) Configure Web Application Proxy can be configured for
Extranet Access
Web Application Proxy is part of the Remote Access server role in Windows Server. It provides
reverse proxy functionality to allow users to access your web applications from outside the
corporate network. Web Application Proxy preauthenticates access to web applications by
using ADFS, and functions as an ADFS proxy.

If you plan to use Web Application proxy, use steps mentioned in Install and Configure the
Web Application Proxy Server to configure it. Once configured, you can publish rules for
Autodiscover.contoso.com or/and mail.contoso.com using the steps mentioned in Publish an

Application that uses OAuth2.

(Optional) Configure MFA for client access
   1. Refer to the following links to configure ADFS with an MFA provider of your choice.

           Configure 3rd party authentication providers as primary authentication in AD FS
           2019
           Configure Azure MFA as authentication provider with AD FS

   2. Configure Access Control Policy requiring MFA.

           Access Control Policies in Windows Server 2016 AD FS

Create Authentication Policies for End Users
It's possible that not all users in your organization have email clients that support Modern Auth
via ADFS. In this scenario, we recommend enabling Modern Authentication for users with

<!-- p.675 -->

supported clients and blocking it for those users without.

To enable Modern Authentication for a specific set of users and block it for the remaining
users, you need to create at least two authentication policies.

  ） Important

  The new authentication policies become available as soon as the Active Directory is
  prepared by using the Exchange 2019 CU13 or later media.

         An organization-wide policy to block Modern Authentication by default
         A secondary policy to selectively allow Modern Authentication for specific users

The following PowerShell commands must be executed from an Exchange Management Shell
(EMS) window on your Exchange server.

Create organization-level policy to block Modern Auth by default
Once Modern Authentication is enabled, all Outlook clients attempt to use OAuth tokens.
However, some clients that are not compatible with ADFS Modern Authentication can only
retrieve OAuth tokens from Microsoft Entra ID. So, these clients are unable to connect if
Modern Authentication is enabled.

To prevent this scenario, you can implement an organization-wide policy to disable Modern
Authentication. In the example, we create a new authentication policy named Block Modern
Auth .

  PowerShell

  New-AuthenticationPolicy "Block Modern Auth" -BlockModernAuthWebServices -
  BlockModernAuthActiveSync -BlockModernAuthAutodiscover -BlockModernAuthImap -
  BlockModernAuthMapi -BlockModernAuthOfflineAddressBook -BlockModernAuthPop -
  BlockModernAuthRpc

This policy can be set at Org level using the following command.

  PowerShell

  Set-OrganizationConfig -DefaultAuthenticationPolicy "Block Modern Auth"

Create user-level authentication policy to enable Modern Auth

<!-- p.676 -->

Next, create a second authentication policy that enables Modern Authentication. Assign this
policy to all users with supported Outlook clients to allow their clients to use Modern
Authentication.

In the example, we create a new authentication called Allow Modern Auth using following
command:

 PowerShell

 New-AuthenticationPolicy "Allow Modern Auth"

Configure Exchange Server to use ADFS OAuth tokens
   1. Verify if OAuth is enabled on the following virtual directories. If it's not enabled, do enable
     OAuth it for all these virtual directories:

       PowerShell

       Get-MapiVirtualDirectory | Format-List Server, *auth*
       Get-WebServicesVirtualDirectory | Format-List Server, *auth*
       Get-OabVirtualDirectory | Format-List Server, *auth*
       Get-AutodiscoverVirtualDirectory | Format-List Server, *auth*
       Get-ActiveSyncVirtualDirectory | Format-List Server, *auth*

     The output appears as follows. The primary detail to focus on is OAuth , as previously
     mentioned:

       PowerShell

       Get-MapiVirtualDirectory | Format-List Server, *auth*

       Server                        : EX1
       IISAuthenticationMethods      : {Ntlm, OAuth, Negotiate}
       InternalAuthenticationMethods : {Ntlm, OAuth, Negotiate}
       ExternalAuthenticationMethods : {Ntlm, OAuth, Negotiate}

     If OAuth is missing from any server or any of the five virtual directories, you need to add it
     using the relevant commands before proceeding: Set-MapiVirtualDirectory, Set-
     WebServicesVirtualDirectory, Set-OabVirtualDirectory, Set-AutodiscoverVirtualDirectory,
     and Set-ActiveSyncVirtualDirectory.

   2. Run the following command:

       PowerShell

<!-- p.677 -->

     New-AuthServer -Type ADFS -Name MyADFSServer -AuthMetadataUrl https://<adfs
     server FQDN>/FederationMetadata/2007-06/FederationMetadata.xml

   This command is required to create a new auth server object in Exchange Server for ADFS.
   Auth server objects are a list of trusted issuers. Only OAuth tokens from these issuers are
   accepted.

 3. Run the following command:

     PowerShell

     Set-AuthServer -Identity MyADFSServer -IsDefaultAuthorizationEndpoint $true

   Set the Auth server we just added as the DefaultAuthorizationEndpoint . When
   advertising the Modern Auth header, Exchange Server advertises the auth URL of the
   DefaultAuthorizationEndpoint . This is how clients know which endpoint to use for

   authentication.

 4. We need to run this command to enable Modern Auth at organization level:

     PowerShell

     Set-OrganizationConfig -OAuth2ClientProfileEnabled $true

 5. Enable Modern Auth for users with supported clients by assigning the Allow Modern Auth
   authentication policy:

     PowerShell

     Set-User -Identity User -AuthenticationPolicy "Allow Modern Auth"

 6. (Required when using Outlook on macOS) Run the following command:

     PowerShell

     New-SettingOverride -Name "EnableKeepADFSHeadersOnTokenExpiry" -Component
     "OAuth" -Section "KeepADFSHeadersOnTokenExpiry" -Parameters @("Enabled=true")
     -Reason "Required for ADFS MA when using Outlook on macOS"
     Get-ExchangeDiagnosticInfo -Process
     Microsoft.Exchange.Directory.TopologyService -Component VariantConfiguration -
     Argument Refresh

Client-Side Modern Authentication configuration

<!-- p.678 -->

We recommend testing Modern Auth with few users before deploying to all users. Once a pilot
group of users can use Modern Auth, more users can be deployed. Validate that your client
supports ADFS Modern Auth. More details about the supported clients can be found in the
Client prerequisites section.

Microsoft Windows

Enable Modern Auth and add your ADFS domain as trusted domain in Outlook:

   1. Create the following registry keys to make your ADFS domain a trusted domain. Make
     sure to add both keys with and without the / at the end of the ADFS domain:

           HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\AAD\AuthTrustedDomains\https://y

           our-ADFS-domain/
           HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\AAD\AuthTrustedDomains\https://y

           our-ADFS-domain

     You can use PowerShell to create the registry keys or deploy them by the help of a Group
     Policy. Run the following commands from a PowerShell window on each client computer.
     Replace your-ADFS-domain with your ADFS domain.

       PowerShell

       New-Item -Path "HKLM:\SOFTWARE\Policies\Microsoft\AAD\AuthTrustedDomains" -
       Force
       (Get-Item
       HKLM:).OpenSubKey("SOFTWARE\Policies\Microsoft\AAD\AuthTrustedDomains",
       $true).CreateSubKey("https://your-ADFS-domain/")
       (Get-Item
       HKLM:).OpenSubKey("SOFTWARE\Policies\Microsoft\AAD\AuthTrustedDomains",
       $true).CreateSubKey("https://your-ADFS-domain")

   2. To enable ADFS Modern Auth in Microsoft Outlook for Windows add the
      EnableExchangeOnPremModernAuth REG_DWORD value under

      HKCU\SOFTWARE\Microsoft\Office\16.0\Common\Identity\ .

     You can use PowerShell to create the registry value or deploy it via a Group Policy. Run
     the following command from a PowerShell window on each client computer.

       PowerShell

       Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Office\16.0\Common\Identity\"
       -Name "EnableExchangeOnPremModernAuth" -Value 1 -Type DWord

<!-- p.679 -->

Apple macOS
To enable Modern Auth for Microsoft Outlook on supported versions of Apple macOS, you
need to modify the preferences for the Microsoft Outlook application.

Open a Terminal window and run the following command, replacing host1 with the FQDN of
your ADFS server. Ensure you don't include the protocol or add any slashes at the end of the
FQDN. For example, if your ADFS server is reachable via https://fs.contoso.com/ , use
fs.contoso.com . If you have multiple ADFS namespaces, add them separated by a space.

 Terminal

 defaults write com.microsoft.Outlook ADFSAuthorizedURLs -array host1

For managed devices, administrators can use a Mobile Device Management (MDM) solution to
centrally manage and push a list of ADFS FQDNs to client devices. The following table outlines
the configuration settings required to control this feature via MDM:

                                                                               ﾉ   Expand table

 Settings                                        Values

 Targeted app                                    Outlook Mac

 Configuration key                               trustedauthorities

 Value type                                      String

 Configuration value                             <ADFS FQDNs>

Verify Modern Auth flow
Once configured correctly, users experience the ADFS login prompt when they connect to an
Exchange server.

Effect on other clients when Modern Auth is enabled
Users enabled for Modern Authentication who use multiple clients (for example, Outlook on
Windows and Outlook Mobile ) experience different behaviors across each client. In the following

summary we describe the client behaviors when Modern Authentication is enabled, assuming
Block Modern Auth is applied as the DefaultAuthenticationPolicy at the organization level.

<!-- p.680 -->

                                                                                    ﾉ   Expand table

 Client                      Behavior

 Outlook for Windows         Uses Modern Auth by default.
 (Classic)

 Outlook for Windows (New)   Tries to use Modern Auth but fails.

 Outlook for Mac             Uses Modern Auth if enabled on the client.

 Outlook iOS                 Falls back to Basic auth.

 Outlook Android             Falls back to Basic auth.

 iOS Mail app                Uses Modern Auth.

 macOS Mail app              Uses Modern Auth.

 Gmail app                   Falls back to Basic auth.

 OWA/ECP                     Doesn't use authentication policy.
                             Depending on how it's configured, it uses either Modern Auth or Basic
                             auth.

 Windows Mail app            Doesn't fall back to Basic auth.

 Thunderbird client          Doesn't fall back to Basic auth.

 PowerShell                  Uses Basic auth.

Effect on OWA/ECP when Modern Auth is enabled for other
clients
You may or may not be using ADFS claims-based authentication for Outlook on the web. The
steps mentioned are required to enabled OAuth for other clients, and doesn't affect how
OWA/ECP is configured.

Use AD FS claims-based authentication with Outlook on the web

Wait time after change authentication policy
After changing the authentication policy to allow Modern Auth or block legacy auth:

     Wait 30 minutes for new policies to be read by front-end servers

     or
