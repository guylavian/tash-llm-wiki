---
title: "Exchange Server — pages 721-760"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0721-0760
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0721-0760
family: exchange
documentKind: "doc"
abstract: "Issue: Changing permissions for Public Folders by using an Outlook client fails with the following error: 'The modified Permissions can't be changed' This issue happens if the Public Folder for which you try to change the permissions, is hosted on a secondary Public Folder mailb"
---

# Exchange Server — pages 721-760

<!-- p.721 -->

Issue: Changing permissions for Public Folders by using an Outlook
client fails with the following error: 'The modified Permissions can't be
changed'

This issue happens if the Public Folder for which you try to change the permissions, is hosted
on a secondary Public Folder mailbox while the primary Public Folder mailbox is on a different
server.

The issue has been fixed with the latest Exchange Server update      . Follow the instructions as
outlined in this KB   to enable the fix.

Issue: Creating Public Folders by using an Outlook client fails with the
following error: 'Cannot create the public folder. You do not have
sufficient permissions to perform this operation on this object. See the
folder contact or your system administrator.'

This issue happens if the Public Folder for which you try to change the permissions, is hosted
on a secondary Public Folder mailbox while the primary Public Folder mailbox is on a different
server.

The issue has been fixed with the latest Exchange Server update      . Follow the instructions as
outlined in this KB   to enable the fix. Note that this fix does not work if a global override to
set PublicFolderHierarchyHandlerEnabler to disabled has been implemented to address the
issue outlined in this KB.

Warnings and errors during Extended Protection configuration script
execution

   1. The script shows a warning of known issues and asks for confirmation:

     To prevent administrators from running into scenarios where existing Exchange Server
     functions are disrupted due to enabling Extended Protection, the script provides a list of
     scenarios which have known issues. Read and evaluate this list carefully before enabling
     Extended Protection. You can proceed to turn on Extended Protection by pressing Y .

                                                                                              

   2. The script doesn't enable Extended Protection because a prerequisite check failed:

           No Exchange server runs a build that supports Extended Protection:

<!-- p.722 -->

          If no Exchange server in the organization is running a build that supports Extended
          Protection, the script doesn't enable Extended Protection on unsupported servers to
          make sure that server-to-server communication doesn't fail.

          To resolve this case, update all Exchange servers to the latest CU and SU and run the
          script again to enable Extended Protection.

          TLS mismatch was detected:

          A valid and consistent TLS configuration is required on all Exchange servers in scope.
          If the TLS settings on all servers in scope aren't the same, enabling Extended
          Protection disrupts client connections to mailbox servers.

                                                                                               

          Read the Exchange Server TLS configuration best practices for more information.

   3. Some Exchange servers aren't available/reachable:

     The script performs multiple tests against all Exchange servers, which are in scope. If one
     or more of these servers aren't reachable, the script excludes them as it can't perform the
     required configuration action on these machines.
                                                                                               

     If the server is offline, you should configure Extended Protection as soon as it's back
     online. If the server was unreachable for other reasons, you should run the script on the
     server itself to enable Extended Protection.

Users can't access their mailbox through one or more clients

There could be multiple reasons why some or all clients can start giving authentication errors
to users after Extended Protection was enabled.

     Users can't access their mailbox permanently or sporadically by using Outlook for
     Windows, Outlook for Mac, Outlook Mobile or the native iOS email client:

        If the TLS configuration across the Exchange organization isn't the same (for example,
        the TLS configuration has been changed on one of the Exchange servers after
        Extended Protection was enabled), this misconfiguration can cause client connections

<!-- p.723 -->

        to fail. To resolve this issue, check the instructions to properly configure TLS on all
        Exchange servers, and then use the script to configure Extended Protection again.

        Check if SSL Offloading is used. Any SSL termination causes the Extended Protection
        Channel Binding Token check to fail as SSL Offloading is considered as a man-in-the-
        middle, which is prevented by Extended Protection. To resolve this issue, disable SSL
        Offloading and use the script to enable Extended Protection again.

     Users can access their emails by using Outlook for Windows and OWA, but not through
     non-Windows clients like Outlook for Mac, Outlook Mobile or the iOS native email client.
     This can happen if the Extended Protection setting for EWS and/or Exchange ActiveSync is
     set to Required on one or all Front-End servers:

        To resolve this issue, either run the ExchangeExtendedProtectionManagement.ps1 script
        with the ExchangeServerNames parameter and pass the name of the Exchange server,
        which has a misconfigured Extended Protection setting. You can also run the script
        without any parameter to check and configure Extended Protection for all servers
        again

        Alternatively, you can also use IIS Manager (INetMgr.exe) and change the Extended
        Protection setting for those virtual Directories to the proper value as outlined in the
        table. We strongly recommend using the script as it checks for the correct values and
        performs the reconfiguration automatically if the values aren't set as expected.

     Users are unable to access OWA or ECP by using the Apple Safari browser on macOS or
     iOS when NTLM SSO is used and Extended Protection was enabled:

        For users on the macOS platform, we suggest utilizing a web browser with Extended
        Protection support. Our recommendation is Microsoft Edge (Chromium)            .

        For users on the iOS platform, there is no web browser with Extended Protection
        support.

        A solution that works on both platforms is to configure Hybrid Modern Authentication
        for OWA and ECP or use AD FS claims-based authentication with Outlook on the web.

If after following the above steps, some clients are still not working as expected, you can roll
back Extended Protection temporarily and report the issue to Microsoft by opening a support
case with us. Follow the steps as outlined in the Disabling Extended Protection section.

Hybrid free/busy or mailbox migration isn't working
If you're using Modern Hybrid, enabling Extended Protection can cause Hybrid features like
free/busy and mailbox migration to stop working if the configuration wasn't performed as

<!-- p.724 -->

described in this article. To resolve this issue, identify the hybrid servers that were published
using Hybrid Agent and disable Extended Protection on the Front-End EWS virtual directory on
these servers.

Public Folders are no longer visible/accessible
There are two issues that could affect Public Folders connectivity when Extended Protection is
enabled. Make sure to follow the instructions as outlined in the Extended Protection and Public
Folders section of this article.

FAQs
Question: Is it required to install the August 2022 Security Update (SU) if it was already installed
on the previous Cumulative Update (CU)?
Answer: Yes, it's required to install the August 2022 SU again if you update to a newer CU build
(for example, Exchange Server 2019 CU11 to Exchange Server 2019 CU12).

Remember: If you plan to do the update immediately (means CU + SU installation), Extended
Protection doesn't need to be switched off. If you plan to stay on the CU without installing the
SU immediately, you must disable Extended Protection as the CU build (without the SU being
installed), doesn't support Extended Protection and therefore, you might experience client
connectivity issues.

Question: Is it safe to enable Extended Protection in an environment that uses Active Directory
Federation Services (AD FS) for Outlook on the web (OWA)?
Answer: Yes, Extended Protection doesn't have an impact on AD FS claims-based authentication
with OWA.

Question: Is it safe to enable Windows Extended Protection in an environment that uses Hybrid
Modern Auth (HMA)?
Answer: Yes, HMA won't be impacted from this change. While Extended Protection doesn't
further enhance HMA, Windows authentication can still be used for applications that don't
support Hybrid Modern Auth. Considering this, the enablement of Extended Protection would
be recommended in any environment eligible that still has Exchange on-premises services.

Question: Does Extended Protection affect Hybrid Modern Auth or Microsoft Teams
integration?
Answer: Extended Protection doesn't affect Microsoft Teams integration or Hybrid Modern
Auth.

Question: I am unable to access OWA/ECP after enabling Extended Protection with an HTTP
400 status code, my OWA/ECP is published through the Entra Application Proxy, what can I do

<!-- p.725 -->

to resolve this?
Answer: Publishing Exchange OWA/ECP through the Entra Application Proxy isn't supported,
you'll need to publish OWA/ECP through a supported network topology by Extended
Protection Standards.

Question: While we understand that preventing MitM attacks is important, can we have our
own devices in the middle with our own certificates?
Answer: If the device uses the same certificate as the Exchange server, they can be used.

<!-- p.726 -->

Exchange Server non-RFC compliant P2
FROM header detection
ﾃ   Summarize this article for me

APPLIES TO:         2016            2019   Subscription Edition

Overview
Microsoft is aware of a vulnerability (CVE-2024-49040 ) that allows attackers to run spoofing
attacks against Microsoft Exchange Server. The vulnerability is caused by the current
implementation of the P2 FROM header verification, which happens in transport. The current
implementation allows some non-RFC 5322              compliant P2 FROM headers to pass which can
lead to the email client (for example, Microsoft Outlook) displaying a forged sender as if it were
legitimate.

Starting with the Exchange Server November 2024 Security Update (SU)          , Exchange Server can
detect and flag email messages that contain potentially malicious patterns in the P2 FROM
header.

How does it work
In case that Exchange Server detects a suspicious message, it automatically prepends the
following disclaimer to the body of the email message:

                                                                                             

Starting with the Exchange Server February 2026 Security Update (SU)        , Exchange Server also
shows a ? instead of the profile picture of the user in case that a suspicious message was
detected:

                                                                                        

<!-- p.727 -->

Exchange Server also adds the X-MS-Exchange-P2FromRegexMatch header to any email message
detected by this feature. If you want to take any action on emails detected by the feature, you
can use an Exchange Transport Rule (ETR) to detect the header and execute a specific action. In
this example, Exchange Server rejects the email if it contains the header:

 PowerShell

 New-TransportRule -HeaderContainsMessageHeader "X-MS-Exchange-P2FromRegexMatch" -
 HeaderContainsWords @("True") -RejectMessageReasonText "Message not accepted due to
 a non-RFC compliant P2 FROM header" -Name "NonCompliantP2FromDetectionRule" -
 SenderAddressLocation "Header"

More information about mail flow rules can be found in the Mail flow rules in Exchange Server
documentation.

Configuration
The new behavior is enabled by default as part of our secure by default approach. Although
it's possible to control the feature using New-SettingOverride. This section explains how the
feature can be controlled. Make sure to run the following commands from an elevated
Exchange Management Shell (EMS).

If you prefer not to have Exchange automatically prepend a disclaimer to messages detected
by the feature, you can disable the disclaimer action while keeping the custom header action
enabled. This allows you to detect these emails using an ETR and handle them differently, such
as by prepending a disclaimer of your choice. The following commands disable the disclaimer
action:

 PowerShell

 New-SettingOverride -Name "DisableP2FromRegexMatchDisclaimer" -Component
 "Transport" -Section "NonCompliantSenderSettings" -Parameters
 @("AddDisclaimerforRegexMatch=false") -Reason "Disabled For Troubleshooting"
 Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
 Component VariantConfiguration -Argument Refresh
 Restart-Service -Name MSExchangeTransport

If you prefer not to have Exchange automatically add the X-MS-Exchange-P2FromRegexMatch
header to emails detected by this feature, you can disable the header action while keeping the
disclaimer action enabled. This setting override was introduced with the Exchange Server
November 2024 SUv2       update. Use the following commands to disable the custom header
action:

<!-- p.728 -->

  PowerShell

  New-SettingOverride -Name "DisableP2FromRegexMatchHeader" -Component "Transport" -
  Section "NonCompliantSenderSettings" -Parameters
  @("AddP2FromRegexMatchHeader=false") -Reason "Disabled For Troubleshooting"
  Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
  Component VariantConfiguration -Argument Refresh
  Restart-Service -Name MSExchangeTransport

We strongly recommend you leave the feature enabled, as disabling the feature makes it easier
for bad actors to run phishing attacks against your organization. If you want to disable the
feature at all, use the following commands to disable the disclaimer and the custom header
action:

  PowerShell

  New-SettingOverride -Name "DisableP2FromRegexMatchDisclaimer" -Component
  "Transport" -Section "NonCompliantSenderSettings" -Parameters
  @("AddDisclaimerforRegexMatch=false") -Reason "Disabled For Troubleshooting"
  New-SettingOverride -Name "DisableP2FromRegexMatchHeader" -Component "Transport" -
  Section "NonCompliantSenderSettings" -Parameters
  @("AddP2FromRegexMatchHeader=false") -Reason "Disabled For Troubleshooting"
  Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
  Component VariantConfiguration -Argument Refresh
  Restart-Service -Name MSExchangeTransport

 Last updated on 02/10/2026

<!-- p.729 -->

Configure HTTP Strict Transport Security
(HSTS) in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Overview
HTTP Strict Transport Security (HSTS) is a widely supported standard     that helps protect
website visitors by ensuring that their browser always connects using an HTTPS connection.
HSTS works by sending a special HTTP response header from the server to the browser called
Strict-Transport-Security (STS). This header includes a max-age directive that specifies the

length of time (in seconds) so that the browser should remember that the site can be accessed
only using HTTPS. Once a browser receives this header, it automatically changes any HTTP
requests to access the site to HTTPS requests.

HSTS doesn't just add protection against common attack scenarios, it also helps remove the
need for the common (and now insecure) practice of redirecting users from an HTTP URL to an
HTTPS URL. HSTS can also be used to address active and passive network attacks. However,
HSTS doesn't address malware, phishing, or browser vulnerabilities.

How HSTS works
The browser is instructed to enforce HSTS when it receives the Strict-Transport-Security
header over an HTTPS connection; however, there are some requirements that must be met
before the browser enforces HSTS. Specifically, the certificate used to encrypt the session:

      Must be valid and trusted by the client;
      Must not be expired; and
      Must contain the domain or subdomain that was called in the browser.

See Securely browse the web with Microsoft Edge       for more general recommendations.

Once the browser is aware that a domain has enabled HSTS, it:

      Always use a https:// connection, including when clicking on an http:// link or after
      typing a URL into the address bar without specifying a protocol.
      Removes the ability for users to click through warnings (for example, expired, or invalid
      certificates, name mismatches, etc.).

<!-- p.730 -->

There are some scenarios (for example, user has a new computer, new profile, new browser or
has cleared browser data and settings) where a user is vulnerable for a short period of time
because they're visiting the site for the first time without HSTS being enforced. To address
these scenarios, the Chromium project maintains an HSTS Preload List (which is also used by
other browsers like Microsoft Edge and Mozilla Firefox). The Preload List enforces HSTS even
when visiting a site for the first time.

You can submit your domain to the HSTS list    . The webserver (or in our case, your Exchange
server) must also send the preload directive as part of the Strict-Transport-Security header
to signal that HSTS preloading should be performed by the browser.

How Exchange Server handles HTTP connections
By default, Exchange Server doesn't redirect HTTP to HTTPS traffic, as the Default Web Site
requires SSL. See Default settings for Exchange virtual directories for more information.

However, it's possible to configure an automatic redirect from HTTP to HTTPS by following the
steps outlined in Configure http to https redirection for Outlook on the web in Exchange
Server, and as a result, Exchange Server accepts connections established via HTTP and
responds with an HTTP 302 redirect .

HSTS can help to greatly reduce the number of insecure HTTP to HTTPS redirects as the rewrite
to HTTPS is performed by the browser itself and no longer by the server as part of an HTTP 302
redirect response. Using HSTS can also lead to performance improvements, although that isn't

its primary purpose.

Regardless of the default configuration (which doesn't allow unencrypted connections), it's a
good security practice to provide the Strict-Transport-Security header as part of the
response header.

Enable HSTS on Exchange Server
The STS header can be configured on Exchange Server 2019 and Exchange Server 2016,
although the way you configure each version is different.

  ） Important

  HSTS must only be configured on the Default Web Site as this is the endpoint to which
  clients connect. HSTS must not be configured on the Exchange Back End . You should also

<!-- p.731 -->

  consider configuring HSTS via Response Header on devices that are operating in front of
  an Exchange server over Layer 7 (e.g., load balancers or reverse proxies).

It's good practice to start with a max-age configuration of 300 (seconds) which is 5 minutes.
After the change has been made, you should closely monitor client connectivity to the
Exchange server and roll back the change if any issue arises.

Update to a max-age value of one week ( 604800 ) or one month ( 2592000 ) and wait for the full
max-age of the stage before you move on. A max-age value of one year ( 31536000 ) should be

set as a minimum from a security point of view and is also at least required, if you plan to add
your domain to the HSTS Preload List . Setting the max-age value to a value of two years
( 63072000 ) is recommended.

  ７ Note

  The following examples set the max-age value to 300 seconds which is a configuration that
  should be used only for validating functionality. Make sure to adjust the attribute value to
  a higher value when you are ready to bring the configuration to production.

Exchange Server 2019
To configure Exchange Server 2019 for sending the Strict-Transport-Security header, you can
use the Windows PowerShell or the IIS Manager user interface (UI). In the following section, we
describe both methods. The HSTS configuration is a per-server configuration and must
therefore be done on every Exchange server.

HSTS configuration via PowerShell
Run the following commands from an elevated PowerShell window to configure and enable
HSTS:

  ７ Note

  To configure a higher max-age value for Exchange Server 2019, you can run the commands
  again by using a higher value. There is no need to remove the existing configuration
  beforehand.

  PowerShell

<!-- p.732 -->

  Import-Module IISAdministration
  Reset-IISServerManager -Confirm:$false
  Start-IISCommitDelay

  $sitesCollection = Get-IISConfigSection -SectionPath
  "system.applicationHost/sites" | Get-IISConfigCollection
  $siteElement = Get-IISConfigCollectionElement -ConfigCollection $sitesCollection -
  ConfigAttribute @{"name"="Default Web Site"}
  $hstsElement = Get-IISConfigElement -ConfigElement $siteElement -ChildElementName
  "hsts"
  Set-IISConfigAttributeValue -ConfigElement $hstsElement -AttributeName "enabled" -
  AttributeValue $true
  Set-IISConfigAttributeValue -ConfigElement $hstsElement -AttributeName "max-age" -
  AttributeValue 300
  Set-IISConfigAttributeValue -ConfigElement $hstsElement -AttributeName
  "includeSubDomains" -AttributeValue $true

If you plan to add your domain to the HSTS Preload List , you must make sure that the
preload directive is also sent as part of the Strict-Transport-Security header. You must not

send the preload directive if you have no plans to submit your domain to the HSTS Preload
List .

  PowerShell

  Set-IISConfigAttributeValue -ConfigElement $hstsElement -AttributeName "preload" -
  AttributeValue $true

Finally, the following commands must be run to complete the HSTS configuration:

  PowerShell

  Stop-IISCommitDelay
  Remove-Module IISAdministration

HSTS configuration via IIS Manager
Do the following steps in the Internet Information Services Manager to configure and enable
HSTS:

   1. Start the IIS Manager ( InetMgr.exe )

   2. Navigate to Sites and click on Default Web Site

   3. In the Actions menu select HSTS...

<!-- p.733 -->

                                                                                       

4. Check the Enable checkbox, define the max-age value and select the directives according
  to the description in this article

                                                                         

    ） Important

    We can't redirect HTTP to HTTPS using the HSTS configuration, as this breaks
    connectivity for some scenarios, including the Exchange Management Shell (EMS). If
    you want to enable HTTP to HTTPS redirect, you must follow the steps outlined in
    Configure http to https redirection for Outlook on the web in Exchange Server.

<!-- p.734 -->

     5. Click OK to complete and activate the configuration

Exchange Server 2016

     ７ Note

     While HSTS configuration is possible via UI on operating systems supported by Exchange
     Server 2019, this control is not natively available on operating systems supported by
     Exchange Server 2016. We therefore only describe the steps to be done via PowerShell.

To configure Exchange Server 2016 for sending the Strict-Transport-Security header, run the
following commands from an elevated PowerShell window. The HSTS configuration is a per-
server configuration and must therefore be done on every Exchange server:

     ７ Note

     To configure a higher max-age value for Exchange Server 2016, you must first remove the
     HTTP Response header before running the following commands again.

Windows Server 2012 & 2012 R2

If you don't plan to add your domain to the HSTS Preload List , you must make sure that the
preload directive isn't sent as part of the Strict-Transport-Security header. Run the following

command to configure HSTS without sending the preload directive:

     PowerShell

     Import-Module WebAdministration
     Add-WebConfigurationProperty -Filter "system.webServer/httpProtocol/customHeaders"
     -PSPath "IIS:\Sites\Default Web Site" -Name . -AtElement @{name="Strict-Transport-
     Security"} -Value @{name="Strict-Transport-Security";value="max-age=300;
     includeSubDomains"}

or

If you plan to add your domain to the HSTS Preload List , you must make sure that the
preload directive is sent as part of the Strict-Transport-Security header. Run the following

command to configure Exchange Server to send the preload directive as part of the HSTS
configuration:

     PowerShell

<!-- p.735 -->

     Import-Module WebAdministration
     Add-WebConfigurationProperty -Filter "system.webServer/httpProtocol/customHeaders"
     -PSPath "IIS:\Sites\Default Web Site" -Name . -AtElement @{name="Strict-Transport-
     Security"} -Value @{name="Strict-Transport-Security";value="max-age=300;
     includeSubDomains; preload"}

Windows Server 2016

     PowerShell

     Import-Module IISAdministration
     Reset-IISServerManager -Confirm:$false
     Start-IISCommitDelay

     $iisConfig = Get-IISConfigSection -SectionPath "system.webServer/httpProtocol" -
     CommitPath "Default Web Site" | Get-IISConfigCollection -CollectionName
     "customHeaders"

If you don't plan to add your domain to the HSTS Preload List , you must make sure that the
preload directive isn't sent as part of the Strict-Transport-Security header. Run the following
command to configure HSTS without sending the preload directive:

     PowerShell

     New-IISConfigCollectionElement -ConfigCollection $iisConfig -ConfigAttribute
     @{"name"="Strict-Transport-Security"; "value"="max-age=300; includeSubDomains";}

or

If you plan to add your domain to the HSTS Preload List , you must make sure that the
preload directive is sent as part of the Strict-Transport-Security header. Run the following

command to configure Exchange Server to send the preload directive as part of the HSTS
configuration:

     PowerShell

     New-IISConfigCollectionElement -ConfigCollection $iisConfig -ConfigAttribute
     @{"name"="Strict-Transport-Security"; "value"="max-age=300; includeSubDomains;
     preload";}

Finally, the following commands must be run to complete the HSTS configuration:

     PowerShell

<!-- p.736 -->

  Stop-IISCommitDelay
  Remove-Module IISAdministration

Disable HSTS on Exchange Server
If you want to stop Exchange Server from sending the Strict-Transport-Security header, you
can roll back the configuration on a per-server base. The steps to disable HSTS are different on
Exchange Server 2016 and Exchange Server 2019.

  ７ Note

  The HSTS specification    allows you to send the max-age directive with a value of 0 . This
  configuration can be used to overwrite the browsers cached HSTS policy information. If
  you plan to remove your Exchange Server HSTS configuration, then it may be useful to
  first set a max-age value of 0 before removing the Strict-Transport-Security header
  configuration.

Exchange Server 2019
To make Exchange Server 2019 stop sending the Strict-Transport-Security header, you can
use the Windows PowerShell or the IIS Manager user interface (UI). In the following section, we
describe both methods.

HSTS configuration via PowerShell
Run the following commands from an elevated PowerShell window to disable HSTS:

  PowerShell

  Import-Module IISAdministration
  Reset-IISServerManager -Confirm:$false
  Start-IISCommitDelay

  $sitesCollection = Get-IISConfigSection -SectionPath
  "system.applicationHost/sites" | Get-IISConfigCollection
  $siteElement = Get-IISConfigCollectionElement -ConfigCollection $sitesCollection -
  ConfigAttribute @{"name"="Default Web Site"}
  $hstsElement = Get-IISConfigElement -ConfigElement $siteElement -ChildElementName
  "hsts"
  Set-IISConfigAttributeValue -ConfigElement $hstsElement -AttributeName "enabled" -
  AttributeValue $false
  Set-IISConfigAttributeValue -ConfigElement $hstsElement -AttributeName "max-age" -

<!-- p.737 -->

  AttributeValue 0
  Set-IISConfigAttributeValue -ConfigElement $hstsElement -AttributeName
  "includeSubDomains" -AttributeValue $false

If the previous HSTS configuration was to send the preload directive, make sure to disable this
as well:

  ） Important

  Remember to request removal from the HSTS preload list        as well. If you forget to
  remove the domain from the preload list, browsers will continue to try to enforce HSTS.

  PowerShell

  Set-IISConfigAttributeValue -ConfigElement $hstsElement -AttributeName "preload" -
  AttributeValue $false

Finally, the following commands must be run to complete the HSTS configuration:

  PowerShell

  Stop-IISCommitDelay
  Remove-Module IISAdministration

HSTS configuration via IIS Manager

Do the following steps in the Internet Information Services Manager to disable HSTS:

   1. Start the IIS Manager ( InetMgr.exe )

   2. Navigate to Sites and click on Default Web Site

   3. In the Actions menu select HSTS...

<!-- p.738 -->

                                                                                            

 4. Uncheck all directives, set the max-age directive to 0 and finally uncheck the Enable
   checkbox

                                                                            

 5. Click OK to complete the configuration

Exchange Server 2016

 ７ Note

<!-- p.739 -->

     While HSTS configuration is possible via UI on operating systems supported by Exchange
     Server 2019, this control is not natively available on operating systems supported by
     Exchange Server 2016. We therefore only describe the steps to be done via PowerShell.

To make Exchange Server 2016 stop sending the Strict-Transport-Security header, run the
following commands from an elevated PowerShell window on each of your Exchange servers:

Windows Server 2012 & 2012 R2

     PowerShell

     Import-Module WebAdministration
     Remove-WebConfigurationProperty -PSPath "IIS:\Sites\Default Web Site" -Filter
     "system.webServer/httpProtocol/customHeaders" -Name . -AtElement @{name="Strict-
     Transport-Security"}

Windows Server 2016

     PowerShell

     Import-Module IISAdministration
     Reset-IISServerManager -Confirm:$false
     Start-IISCommitDelay

     $iisConfig = Get-IISConfigSection -SectionPath "system.webServer/httpProtocol" -
     CommitPath "Default Web Site" | Get-IISConfigCollection -CollectionName
     "customHeaders"

If the previous HSTS configuration did not send the preload directive, then run the following
command:

     PowerShell

     Remove-IISConfigCollectionElement -ConfigCollection $iisConfig -ConfigAttribute
     @{"name"="Strict-Transport-Security"; "value"="max-age=300; includeSubDomains";}

or

If the previous HSTS configuration was to send the preload directive, make sure to run this
command:

     PowerShell

<!-- p.740 -->

  Remove-IISConfigCollectionElement -ConfigCollection $iisConfig -ConfigAttribute
  @{"name"="Strict-Transport-Security"; "value"="max-age=300; includeSubDomains;
  preload";}

Finally, the following commands must be run to complete the HSTS configuration:

  PowerShell

  Stop-IISCommitDelay
  Remove-Module IISAdministration

Validate that HSTS is working as expected
The best way to confirm that HSTS protection is working as expected is to use a modern
browser that supports HSTS (for example, Microsoft Edge, Firefox, Chrome, Safari, Opera, etc.).
The following steps can be followed when using the Microsoft Edge browser. If you are using a
different browser, consult the documentation to find out what the steps for checking the HSTS
flags are:

   1. Open the browser and establish an HTTPS connection to OWA or ECP. Make sure that the
      certificate returned by the Exchange server matches the (sub-) domain you've used (for
      example, e2k16-2.contoso.lab) and is trusted by the client machine (as this is required to
      activate the browser's HSTS protection for the domain).
   2. Type edge://net-internals/#hsts in the address bar and press Enter.
   3. Enter the domain name that you've used to access OWA or ECP (for example, e2k16-
      2.contoso.lab) into the Query HSTS/PKP domain box and press Enter.

Example:

                                                                                   

If the result is Not found , this means that HSTS isn't used for the domain. The reason could be
that the URL wasn't visited before or that the entry with the HSTS policy store has expired (it's
valid for the time that was specified in the max-age directive).

If a result is found, the output looks like this:

<!-- p.741 -->

                                                                                                

If HSTS is used and a connection isn't trusted (for example, the URL doesn't match the domain
for which the certificate is issued or the certificate is untrusted or expired), the user sees the
following warning which can't be bypassed:

Blocking page Microsoft Edge:

<!-- p.742 -->

                                 

Blocking page Mozilla Firefox:

                                 

<!-- p.743 -->

Configure certificate signing of PowerShell
serialization payloads in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

Overview
Certificate-based signing of PowerShell serialization payloads is a defense-in-depth security
feature to prevent malicious manipulation of serialized data to be exchanged via Exchange
Management Shell (EMS) sessions. It's available on Exchange Server 2013, Exchange Server
2016 and Exchange Server 2019.

The feature was introduced with the January 2023 Exchange Server Security Update . It was
shipped as disabled by default (opt-in), and needs to be enabled by the Exchange Server
administrator. It can be enabled via a setting override (Exchange Server 2016 and Exchange
Server 2019) or by the help of a registry value (Exchange Server 2013).

By installing the November 2023 (or later) Exchange Server Security Update       , the feature is
enabled by default (opt-out) on a per-server basis, and needs to be disabled by the Exchange
Server administrator if you don't want to use it. Make sure that the prerequisites for enabling
certificate signing of serialized data are fulfilled before installing the November 2023 (or later)
Exchange Server Security Update       . To disable the feature you need to create a new setting
override that explicitly turns the feature off.

What is data serialization
Data serialization is the process of converting the state of an object into a form (stream of
bytes) that can be persisted or transmitted to memory, a database, or a file. PowerShell, for
example, uses serialization when passing .NET objects between sessions. After an object was
submitted or stored, it can be reconstructed back to its previous format. This process is called
deserialization.

If you want to learn more about data serialization in PowerShell, we recommend reading the
How objects are sent to and from remote sessions        blog post.

Prerequisites for enabling certificate signing of
serialized data

<!-- p.744 -->

There are some prerequisites that must be fulfilled prior certificate signing of PowerShell
serialization payloads can be enabled without breaking connectivity between Exchange Servers:

     All Exchange servers in your environment must run the January 2023 Exchange Server
     Security Update or a later one     . If the feature is enabled in an environment that has
     Exchange servers, which don't support serialization signing, you might experience issues
     in server-to-server communication or when using the Exchange Management Shell.

     All Exchange servers (except Edge Transport and Management Tools only servers) must
     have access to the Exchange Server Auth Certificate which must be valid and must not be
     expired.

         Tip

        You can use the MonitorExchangeAuthCertificate            script to check if the Exchange
        Server Auth Certificate is valid. It can also be used to renew the OAuth certificate
        automatically or to replace it if it has already expired.

Validate that certificate signing of PowerShell
serialization payloads is used
You can verify if certificate signing of PowerShell serialization payloads is enabled, by checking
the DataSerialization log file, which is maintained by Exchange Server. You can find the log
file in the following directory: <ExchangeInstallPath>\V15\Logging\Data\Serialization .

Exchange maintains one log file per process. If you open an Exchange Management Shell
(EMS), a new log file is created. If you open a second EMS, another log file will be written. The
log file naming syntax is DataSerialization<yyyyMMdd>-<N>.LOG . Each of the log files can be up
to 10 MB in size. The maximum size of the serialization log directory is limited to 1 GB by
default. Log files are deleted if they are older than 30 days .

The EventData column contains the process name and the indicator that shows, whether
serialization signing is used or not.

Example of serialization signing in use:

"S:MSG=SerializationTypeConverter Initialized, Process Name = w3wp,

SerializationSigningEnabled = True, IsCustomParserEnabled = True"

Example of serialization signing not in use:

<!-- p.745 -->

"S:MSG=SerializationTypeConverter Initialized, Process Name = powershell,
SerializationSigningEnabled = False, IsCustomParserEnabled = True"

Enable certificate signing of PowerShell
serialization payloads

  ） Important

  It's not necessary to create the setting override when running the November 2023 (or
  later) Exchange Server Security Update . The certificate signing of PowerShell
  serialization payloads feature is enabled by default when running this build.

Enable when running Exchange Server 2016 and Exchange
Server 2019
You must create a new setting override to enable certificate signing of PowerShell serialization
payloads.

   1. Run the following command from an elevated Exchange Management Shell (EMS) on a
     server that's running Exchange Server in your environment:

       PowerShell

        New-SettingOverride -Name "EnableSigningVerification" -Component Data -
        Section EnableSerializationDataSigning -Parameters @("Enabled=true") -Reason
        "Enabling Signing Verification"

       ７ Note

       This command enables all servers that are running Exchange Server 2016 and
       Exchange Server 2019 in your environment for certificate signing of PowerShell
       serialization payloads. You don't need to run the command on every Exchange
       server.

   2. Refresh the VariantConfiguration argument by running the following command:

       PowerShell

        Get-ExchangeDiagnosticInfo -Process
        Microsoft.Exchange.Directory.TopologyService -Component VariantConfiguration

<!-- p.746 -->

        -Argument Refresh

   3. It's required to restart the World Wide Web Publishing service and the Windows Process
     Activation Service on the Exchange server, on which the setting override was created.

     Run the following command from an elevated PowerShell window or restart the server:

        PowerShell

        Restart-Service -Name W3SVC, WAS -Force

Enable when running Exchange Server 2013
If you run Exchange Server 2013, certificate signing of PowerShell serialization payloads must
be enabled by creating a registry value on each Exchange Server 2013.

   1. Create the registry value on an Exchange Server 2013 by running the following command:

        PowerShell

        New-ItemProperty -Path
        HKLM:\SOFTWARE\Microsoft\ExchangeServer\v15\Diagnostics -Name
        "EnableSerializationDataSigning" -Value 1 -Type String

   2. It's required to restart the World Wide Web Publishing service and the Windows Process
     Activation Service on each Exchange 2013 server, on which the registry value was

     created. Run the following command from an elevated PowerShell window or restart the
     server:

        PowerShell

        Restart-Service -Name W3SVC, WAS -Force

Disable certificate signing of PowerShell
serialization payloads

Disable when running Exchange Server 2016 and Exchange
Server 2019
To disable the feature on Exchange Server 2016 or Exchange Server 2019, the setting override
must be deleted or explicitly set to disabled.

<!-- p.747 -->

２ Warning

Disabling certificate signing of PowerShell serialization payloads makes your server
vulnerable to known Exchange vulnerabilities and weakens protection against unknown
threats. We recommend leaving this feature enabled.

1. Delete the setting override or set it explicitly to Enabled=false :

   When running the January 2023 SU to October 2023 Exchange SU, the setting override
   must be deleted to disable the feature.

   Run the following command from an elevated Exchange Management Shell:

        PowerShell

        Get-SettingOverride -Identity "EnableSigningVerification" | Remove-
        SettingOverride

   or

   When running the November 2023 or later Exchange SU, a setting override must be
   created to explicitly disable the feature.

   Run the following command from an elevated Exchange Management Shell:

        PowerShell

        New-SettingOverride -Name "DisableSigningVerification" -Component Data -
        Section EnableSerializationDataSigning -Parameters @("Enabled=false") -Reason
        "Disable Signing Verification"

2. Refresh the VariantConfiguration argument by running the following command:

        PowerShell

        Get-ExchangeDiagnosticInfo -Process
        Microsoft.Exchange.Directory.TopologyService -Component VariantConfiguration
        -Argument Refresh

3. It's required to restart the World Wide Web Publishing service and the Windows Process
   Activation Service on the Exchange server, on which the setting override was deleted or

   updated. Run the following command from an elevated PowerShell window or restart the
   server:

<!-- p.748 -->

         PowerShell

         Restart-Service -Name W3SVC, WAS -Force

   4. Close the Exchange Management Shell (EMS) that was used to run the commands
      mentioned in the previous steps. This is important to apply the configuration
      immediately.

Disable when running Exchange Server 2013
To disable the feature on Exchange Server 2013, the registry value must be deleted to explicitly
set to 0 .

   1. Set the registry value to 0 on Exchange Server 2013 by running the following command:

         PowerShell

         Set-ItemProperty -Path
         HKLM:\SOFTWARE\Microsoft\ExchangeServer\v15\Diagnostics -Name
         "EnableSerializationDataSigning" -Value 0

   2. It's required to restart the World Wide Web Publishing service and the Windows Process
      Activation Service on each Exchange 2013 server, on which the registry value was

      changed. Run the following command from an elevated PowerShell window or restart the
      server:

         PowerShell

         Restart-Service -Name W3SVC, WAS -Force

Known issues with certificate signing of serialized
data

  ） Important

  Ensure to always install the latest Exchange Server update , as it resolves some of the
  issues listed in this section. Issues addressed by the latest update are marked with a
  checkmark.

<!-- p.749 -->

❌ If signing of PowerShell serialization payloads is enabled, an expired Auth Certificate
will prevent the Get-ExchangeCertificate cmdlet from returning certificate details.

✅ If signing of PowerShell serialization payloads is enabled, the Get-
ExchangeCertificate cmdlet doesn't return a visible value when executed on a computer

with only the Exchange Management Tools installed, regardless of the validity of the Auth
Certificate.

❌ Certain scripts included with Exchange Server, such as
RedistributeActiveDatabases.ps1 , may not function as expected under the following

conditions:
   The feature for signing PowerShell Serialization payloads is enabled.
   You aren't using the default security groups provided by Exchange RBAC.
   The script is run by a user who is not a member of the Organization Management role
   group.

The following PowerShell scripts don't function properly when executed on a computer
that has only the Exchange Management Tools installed, without any other Exchange
Server role. To resolve this issue, run the script on an Exchange Server with the mailbox
role, using an elevated Exchange Management Shell (EMS).
   ✅ RedistributeActiveDatabases.ps1
   ✅ StartDagServerMaintenance.ps1
   ✅ Manage-MetaCacheDatabase.ps1
   ✅ Move-PublicFolderBranch.ps1

❌ Some piped PowerShell cmdlets might fail to run on a computer that has only the
Exchange Management Tools installed and no other Exchange Server role. To resolve this
issue, use ForEach-Object as demonstrated in the examples or run them on an Exchange
server with the mailbox role installed. This affects various cmdlet combinations, such as:

   Get-Mailbox | Get-CalendarDiagnosticLog

   Get-Mailbox | Get-MailboxFolderPermission

   Get-Mailbox | Get-MailboxFolderStatistics

   Get-MailboxDatabase | Get-MailboxStatistics

   Get-MailboxDatabase | Get-Mailbox

   Get-MailboxDatabase | Test-ExchangeSearch

   Get-PublicFolderClientPermission | Remove-PublicFolderClientPermission

<!-- p.750 -->

If you want to use them on an Exchange Management Tools server (without any other
Exchange Server role installed), you can work around this issue as shown here:

  PowerShell

  Get-Mailbox | ForEach-Object { Get-CalendarDiagnosticLog -Identity $_.Name
  }
  Get-Mailbox | ForEach-Object { Get-MailboxFolderPermission -Identity
  $_.Name }
  Get-Mailbox | ForEach-Object { Get-MailboxFolderStatistics -Identity
  $_.Name }
  Get-MailboxDatabase | ForEach-Object { Get-MailboxStatistics -Database
  $_.Name }
  Get-MailboxDatabase | ForEach-Object { Get-Mailbox -Database $_.Name }
  Get-MailboxDatabase | ForEach-Object { Test-ExchangeSearch -MailboxDatabase
  $_.Name }
  Get-PublicFolderClientPermission \pf1 | ForEach-Object { Remove-
  PublicFolderClientPermission -Identity $_.Identity.ToString() -User
  $_.User.ToString() }

<!-- p.751 -->

Exchange Emergency Mitigation
(EM) service
APPLIES TO:      2016      2019        Subscription Edition

The Exchange Emergency Mitigation service (EM service) helps to keep your Exchange Servers
secure by applying mitigations to address any potential threats against your servers. It uses the
cloud-based Office Config Service (OCS) to check for and download available mitigations and to
send diagnostic data to Microsoft.

The EM service runs as a Windows service on an Exchange Mailbox server. When you install the
September 2021 CU (or later) on Exchange Server 2016 or Exchange Server 2019, the EM service
is installed automatically on servers with the Mailbox role. The EM service won't be installed on
Edge Transport servers.

The use of the EM service is optional. If you don't want Microsoft to automatically apply
mitigations to your Exchange servers, you can disable the feature.

Mitigations
A mitigation is an action or set of actions that are taken automatically to secure an Exchange
server from a known threat that is being actively exploited in the wild. To help protect your
organization and mitigate risk, the EM service might automatically disable features or
functionality on an Exchange server.

The EM service can apply the following types of mitigations:

     IIS URL Rewrite rule mitigation: This mitigation is a rule that blocks specific patterns of
     malicious HTTP requests that can endanger an Exchange server.
     Exchange service mitigation: This mitigation disables a vulnerable service on an Exchange
     server.
     App Pool mitigation: This mitigation disables a vulnerable app pool on an Exchange server.

You have visibility and control over any applied mitigation by using Exchange PowerShell cmdlets
and scripts.

How it works

<!-- p.752 -->

If Microsoft learns about a security threat, we might create and release a mitigation for the issue.
If this happens, the mitigation is sent from the OCS to the EM service as a signed XML file
containing the configuration settings that are required to apply the mitigation.

After the EM service has been installed, it checks the OCS for available mitigations every hour.
The EM service then downloads the XML file and validates the signature to verify that the XML
wasn't tampered with. The EM service checks the issuer, the Extended Key Usage, and the
certificate chain. After successful validation, the EM service applies the mitigation.

Each mitigation is a temporary, interim fix until you can apply the Security Update that fixes the
vulnerability. The EM service isn't a replacement for Exchange SUs. However, it's the fastest and
easiest way to mitigate the highest risks to internet-connected, on-premises Exchange servers
before updating.

List of mitigations released
The following table describes the repository of all released mitigations.

                                                                                       ﾉ   Expand table

 Serial     Mitigation    Description               Lowest version     Highest             Rollback
 number     ID                                      applicable         version             procedure
                                                                       applicable

 1          PING1         EEMS heartbeat probe.     - Exchange SE:     N/A                 No rollback
                          Doesn't modify any        RTM                                    required.
                          Exchange settings.        - Exchange 2019:
                                                    September 2021
                                                    CU
                                                    - Exchange 2016:
                                                    September 2021
                                                    CU

 2          M1            Mitigation of CVE-2022-   - Exchange 2019:   - Exchange          See M1
                          41040    via a URL        RTM                2019: October       rollback
                          Rewrite configuration.    - Exchange 2016:   2022 SU             procedure.
                                                    RTM                - Exchange
                                                                       2016: October
                                                                       2022 SU

<!-- p.753 -->

 Serial      Mitigation    Description                 Lowest version     Highest              Rollback
 number      ID                                        applicable         version              procedure
                                                                          applicable

 3           M2            Mitigation of CVE-2026-     - Exchange SE:     - Exchange SE:       See M2
                           42897 via a URL             RTM                June 2026 SU         rollback
                           Rewrite configuration.      - Exchange 2019:   - Exchange           procedure.
                                                       RTM                2019: June 2026
                                                       - Exchange 2016:   SU
                                                       RTM                - Exchange
                                                                          2016: June 2026
                                                                          SU

Prerequisites
If these prerequisites aren't already on the Windows Server where Exchange is installed or to be
installed, Setup prompts you to install these prerequisites during the readiness check:

       IIS URL Rewrite Module
       Universal C Runtime in Windows (KB2999226)            for Windows Server 2012 and Windows
       Server 2012 R2

Connectivity
The EM service needs outbound connectivity to the OCS to check for and download mitigations.
If outbound connectivity to the OCS isn't available during the installation of Exchange Server,
Setup issues a warning during the readiness check.

While the EM service can be installed without connectivity to the OCS, it must have connectivity
to the OCS to download and apply the latest mitigations. The OCS must be reachable from the
computer on which Exchange Server is installed for the EM service to function correctly.

                                                                                           ﾉ   Expand table

 Endpoint               Address                        Port    Description

 Office Config          officeclient.microsoft.com/*   443     Required endpoint for the Exchange EM
 Service                                                       service

     ） Important

<!-- p.754 -->

  Make sure to exclude connections to officeclient.microsoft.com from SSL inspection
  workflows performed by firewalls or third-party software like AntiVirus as this could break
  the certificate validation logic, which is built into the EM service.

If a network proxy is deployed for outbound connectivity, you need to configure the
InternetWebProxy parameter on the Exchange server by running the following command:

  PowerShell

  Set-ExchangeServer -Identity <ServerName> -InternetWebProxy
  <http://proxy.contoso.com:port>

You must also configure the proxy address additionally in WinHTTP proxy settings:

  PowerShell

  netsh winhttp set proxy <proxy.contoso.com:port>

In addition to outbound connectivity to the OCS, EM service needs outbound connectivity to
various Certificate Revocation List (CRL) endpoints mentioned here.

These are required to verify authenticity of certificates used to sign the mitigations XML file.

We strongly recommend letting Windows maintain the Certificate Trust List (CTL)              on your
machine. Otherwise, this must be maintained manually regularly. To allow Windows to maintain
the CTL, the following URL must be reachable from the computer on which Exchange Server is
installed.

                                                                                         ﾉ   Expand table

 Endpoint                          Address                       Port     Description

 Certificate Trust List Download   ctldl.windowsupdate.com/*     80       Certificate Trust List download

Test-MitigationServiceConnectivity script
You can verify that an Exchange server has connectivity to the OCS by using the Test-
MitigationServiceConnectivity.ps1 script in the V15\Scripts folder in the Exchange server
directory.

  ７ Note

<!-- p.755 -->

  The Test-MitigationServiceConnectivity.ps1 script can't be run on a Management Tools
  server. You must run it on a Mailbox server.

If the server has connectivity, the output is:

 PowerShell

 Result: Success.
 Message: The Mitigation Service endpoint is accessible from this computer.

If the server doesn't have connectivity, the output is:

 PowerShell

 Result: Failed.
 Message: Unable to connect to the Mitigation Service endpoint from this computer. To
 learn about connectivity requirements, see https://aka.ms/HelpConnectivityEEMS.

Disable automatic mitigation through the EM service
One of the EM service functions is downloading mitigations from the OCS and automatically
applying them to the Exchange Server. If your organization has an alternate means of mitigating
a known threat, you might choose to disable automatic applications of mitigations. You can
enable or disable automatic mitigation at an organizational level or at the Exchange server level.

To disable automatic mitigation for your entire organization, run the following command:

 PowerShell

 Set-OrganizationConfig -MitigationsEnabled $false

By default, MitigationsEnabled is set to $true . When set to $false , the EM service still checks for
mitigations hourly but doesn't automatically apply mitigations to any Exchange server in the
organization, regardless of the value of the MitigationsEnabled parameter at the server level.

To disable automatic mitigation on a specific server, replace <ServerName> with the name of the
server, and then run the following command:

 PowerShell

 Set-ExchangeServer -Identity <ServerName> -MitigationsEnabled $false

<!-- p.756 -->

By default, MitigationsEnabled is set to $true . When set to $false , the EM service checks for
mitigations hourly but doesn't automatically apply them to the specified server.

The combination of the organization setting and the server settings determine the behavior of
the EM service on each Exchange server. This behavior is described in the following table:

                                                                                        ﾉ   Expand table

 Organization         Server        Result
 setting              setting

 True                 True          EM service automatically applies mitigations to the Exchange server.

 True                 False         EM service doesn't automatically apply mitigations to a specific
                                    Exchange server.

 False                False         EM service doesn't automatically apply mitigations to any Exchange
                                    server.

  ７ Note

  The MitigationsEnabled parameter automatically applies to all servers in an organization. This
  parameter is set to the value $true as soon as the first Exchange server in your organization
  is upgraded to the September 2021 CU (or later). This behavior is by design. After the other
  Exchange servers in the organization are upgraded with the September 2021 CU (or later),
  only then does the EM service honor the value of the MitigationsEnabled parameter.

View applied mitigations
After mitigations are applied to a server, you can view the applied mitigations by replacing
<ServerName> with the name of the server, and then running the following command:

 PowerShell

 Get-ExchangeServer -Identity <ServerName> | Format-List Name,MitigationsApplied

Example output:

 PowerShell

 Name            :      Server1
 MitigationsApplied     :   {M01.1, M01.2, M01.3}

<!-- p.757 -->

To see the list of applied mitigations for all Exchange servers in your environment, run the
following command:

 PowerShell

 Get-ExchangeServer | Format-List Name,MitigationsApplied

Example output:

 PowerShell

 Name            :       Server1
 MitigationsApplied      :   {M01.1, M01.2, M01.3}

 Name            :       Server2
 MitigationsApplied      :   {M01.1, M01.2, M01.3}

Reapply a mitigation
If you accidentally reverse a mitigation, the EM service reapplies it when it performs its hourly
check for new mitigations. To manually reapply any mitigation, restart the EM service on the
Exchange server by running the following command:

 PowerShell

 Restart-Service MSExchangeMitigation

Ten minutes after restarting, the EM service runs its check and applies any mitigations.

Block or remove mitigations
If a mitigation critically affects the functionality of your Exchange server, you can block the
mitigation, and manually reverse it.

To block any mitigation, add the Mitigation ID in the MitigationsBlocked parameter:

 PowerShell

 Set-ExchangeServer -Identity <ServerName> -MitigationsBlocked @("M1")

The previous command blocks the M1 mitigation, which ensures that EM service won't reapply
this mitigation in the next hourly cycle.

<!-- p.758 -->

To block more than one mitigation, use the following syntax:

 PowerShell

 Set-ExchangeServer -Identity <ServerName> -MitigationsBlocked @("M1","M2")

Blocking a mitigation doesn't automatically remove it, but after blocking a mitigation, you can
manually remove it. How a mitigation is removed depends on the type of mitigation. For
example, to remove an IIS rewrite rule mitigation, delete the rule in IIS Manager. To remove a
service or app pool mitigation, start the service or app pool manually. For the detailed steps to
remove a specific released mitigation, see the Rollback procedures for released mitigations
section.

You can also remove one or more mitigations from the blocked mitigations list by removing the
Mitigation ID in the MitigationsBlocked parameter in the same command.

For example:

 PowerShell

 Set-ExchangeServer -Identity <ServerName> -MitigationsBlocked @()

After a mitigation is removed from the blocked mitigations list, the EM service reapplies the
mitigation on its next run. To manually reapply the mitigation, stop and restart the EM service by
running the following command:

 PowerShell

 Restart-Service MSExchangeMitigation

Ten minutes after restarting, the EM service runs its check and applies any mitigations.

  ） Important

  Refrain from making any changes to the MitigationsApplied parameter, as it is used by the
  EM service to store and track mitigation status.

View applied and blocked mitigations

<!-- p.759 -->

You can view both applied and blocked mitigations for all Exchange servers in your organization
by using the Get-ExchangeServer cmdlet.

To view the list of applied and blocked mitigations for all Exchange servers, run the following
command:

 PowerShell

 Get-ExchangeServer | Format-List Name,MitigationsApplied,MitigationsBlocked

Example output:

 PowerShell

 Name            :      Server1
 MitigationsApplied     :   {M01.1, M01.3}
 MitigationsBlocked     :   {M01.2}

 Name            :      Server2
 MitigationsApplied     :   {M01.1, M01.2}
 MitigationsBlocked     :   {M01.3}

To view the list of applied and blocked mitigations on a per-server basis, replace <ServerName>
with the name of the server, and then run the following command:

 PowerShell

 Get-ExchangeServer -Identity <ServerName> | fl name, *Mitigations*

Example output:

 PowerShell

 Name            :      Server1
 MitigationsEnabled     :   True
 MitigationsApplied     :   {M01.1, M01.3}
 MitigationsBlocked     :   {M01.2}

Get-Mitigations script
You can use the Get-Mitigations.ps1 script to analyze and track the mitigations provided by
Microsoft. This script is available in the V15\Scripts folder in the Exchange Server directory.

<!-- p.760 -->

The script displays the ID, type, description, and status of each mitigation. The list includes any
applied, blocked, or failed mitigations.

To view the details of a specific server, provide the server name in the Identity parameter. For
example, .\Get-Mitigations.ps1 -Identity <ServerName> . To view the status of all the servers in
your organization, omit the Identity parameter.

Example: Export the list of applied mitigations and their descriptions to a CSV file by using the
ExportCSV parameter:

 PowerShell

 .\Get-Mitigations.ps1 -Identity <ServerName> -ExportCSV "C:\temp\CSVReport.csv"

  ） Important

  The Get-Mitigations script requires PowerShell version 4.0.

Remove mitigations after an SU or CU upgrade
After an SU or a CU has been installed, an admin must manually remove any mitigations that are
no longer needed. For example, if a Mitigation named M1 is no longer relevant after installing an
SU, the EM service stops applying it, and it's removed from the list of applied mitigations.
Depending on the type of mitigation, it can be removed from the server if necessary. For the
detailed steps to remove a specific released mitigation, see the Rollback procedures for released
mitigations section.

  ７ Note

  The Exchange Emergency Mitigation service can add IIS URL rewrite rule mitigations on a
  per-site/per-vDir level (for example, on the Default Web Site or only on the OWA vDir in
  Default Web Site ) as well as on the server level. Site/vDir level mitigations are added to the

  corresponding web.config file for the site/vDir whereas mitigations on the server level are
  added to the applicationHost.config file. It's expected that site level mitigations are
  removed after a CU has been installed. However, mitigations on the server level stay in place
  and must be manually removed if they are no longer needed.

  If a mitigation is applicable for the newly installed CU, the EM service reapplies it.
