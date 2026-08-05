---
title: "Exchange Server — pages 601-640"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0601-0640
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0601-0640
family: exchange
documentKind: "doc"
abstract: "We recommend that you configure a user principal name (UPN) that matches the primary email address of each user. If you don't provide a UPN that matches the email address of a user, the user will be required to manually provide their domain\\username or UPN in addition to their e"
---

# Exchange Server — pages 601-640

<!-- p.601 -->

  We recommend that you configure a user principal name (UPN) that matches the primary
  email address of each user. If you don't provide a UPN that matches the email address of
  a user, the user will be required to manually provide their domain\username or UPN in
  addition to their email address. If their UPN matches their email address, Outlook on the
  web (formerly known as Outlook on the web), ActiveSync, and Outlook will automatically
  match their email address to their UPN.

Step 4: Configure external URLs
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the " <Service> virtual directory settings" entry in the
Clients and mobile devices permissions topic.

Before clients can connect to your new server from the internet, you need to configure the
external domains (or URLs) on the virtual directories in the Client Access (frontend) services on
the Mailbox server and then in your public DNS records. The steps below configure the same
external domain on the external URL of each virtual directory. If you want to configure different
external domains on one or more virtual directory external URLs, you need to configure the
external URLs manually. For more information, see Default settings for Exchange virtual
directories.

   1. Open the EAC and go to Servers > Servers, select your internet-facing Mailbox server
     that your clients will connect to, and then click Edit   .

   2. In the Exchange server properties window that opens, select the Outlook Anywhere tab,
     configure the following settings:

     Specify the external host name...: Enter the externally accessible FQDN that your external
     clients will use to connect to their mailboxes (for example, mail.contoso.com).

     Specify the internal host name...: Enter the internally accessible FQDN (for example,
     mail.contoso.com).

     When you're finished, click Save.

   3. Go to Servers > Virtual directories and then select Configure external access domain          .

   4. In the Configure external access domain window opens, configure the following settings:

      a. Select the Mailbox servers to use with the external URL: Click Add

      b. In the Select a server dialog that opens, select the Mailbox server you want to
        configure and then click Add. After you've added all of the Mailbox servers that you

<!-- p.602 -->

        want to configure, click OK.

      c. Enter the domain name you will use with your external Mailbox servers: Enter the
        external domain that you want to apply (for example, mail.contoso.com). When you're
        finished, click Save.

Some organizations use a unique Outlook on the web FQDN to protect against future changes
to the underlying server FQDN. Many organizations use owa.contoso.com for their Outlook on
the web FQDN instead of mail.contoso.com. If you want to configure a unique Outlook on the
web FQDN, do the following steps. This checklist assumes you have configured a unique
Outlook on the web FQDN.

   1. Back at Servers > Virtual directories, select owa (Default Web Site) on the server that
     you want to configure, and then click Edit     .

   2. The owa (Default web site) window opens. On the General tab in the External URL field,
     enter the following information:

           https://

           The unique Outlook on the web FQDN you want to use (for example,
           owa.contoso.com), and then append /owa. For example,
           https://owa.contoso.com/owa .

           /owa

     In this example, the final value would be https://owa.contoso.com/owa

     When you're finished, click Save.

   3. Back at Servers > Virtual directories, select ecp (Default Web Site) on the server that you
     want to configure, and click Edit    .

   4. In the ecp (Default web site) window that opens, enter the same URL from the previous
     step, but append the value /ecp instead of /owa (for example,
     https://owa.contoso.com/ecp       ). When you're finished, click Save.

After you've configured the external URL in the Client Access services virtual directories on the
Mailbox server, you need to configure your public DNS records for Autodiscover, Outlook on
the web, and mail flow. The public DNS records should point to the external IP address or
FQDN of your internet-facing Mailbox server and use the externally accessible FQDNs that
you've configured on your Mailbox server. The recommended DNS records that you should
create to enable mail flow and external client connectivity are described in the following table:

<!-- p.603 -->

                                                                                    ﾉ    Expand table

 FQDN                                       DNS record type               Value

 Contoso.com                                MX                            Mail.contoso.com

 Mail.contoso.com                           A                             172.16.10.11

 Owa.contoso.com                            CNAME                         Mail.contoso.com

 Autodiscover.contoso.com                   CNAME                         Mail.contoso.com

How do you know this step worked?
To verify that you've successfully configured the external URLs in the Client Access services
virtual directories on the Mailbox server, do the following steps:

   1. In the EAC, go to Servers > Virtual directories.

   2. In the Select server field, select the internet-facing Mailbox server.

   3. Select a virtual directory and then, in the virtual directory details pane, verify that the
     External URL field is populated with the correct FQDN and service as shown in the
     following table:

                                                                                    ﾉ    Expand table

      Virtual directory                  External URL value

      Autodiscover                       No external URL displayed

      ECP                                https://owa.contoso.com/ecp

      EWS                                https://mail.contoso.com/EWS/Exchange.asmx

      Microsoft-Server-ActiveSync        https://mail.contoso.com/Microsoft-Server-ActiveSync

      OAB                                https://mail.contoso.com/OAB

      OWA                                https://owa.contoso.com/owa

      PowerShell                         http://mail.contoso.com/PowerShell

To verify that you've successfully configured your public DNS records, do the following steps:

   1. Open a command prompt and run nslookup.exe .

   2. Change to a DNS server that can query your public DNS zone.

<!-- p.604 -->

   3. In nslookup , look up the record of each FQDN you created. Verify that the value that's
     returned for each FQDN is correct.

   4. In nslookup , type set type=mx and then look up the accepted domain you added in Step
     1. Verify that the value returned matches the FQDN of the Mailbox server.

Step 5: Configure internal URLs
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the " <Service> virtual directory settings" entry in the
Clients and mobile devices permissions topic.

Before clients can connect to your new server from your internal network, you need to
configure the internal domains (or URLs) on the virtual directories in the Client Access
(frontend) services on the Mailbox server and then in your internal DNS records.

The procedure below lets you choose whether you want users to use the same URL on your
intranet and on the internet to access your Exchange server or whether they should use a
different URL. What you choose depends on the addressing scheme you have in place already
or that you want to implement. If you're implementing a new addressing scheme, we
recommend that you use the same URL for both internal and external URLs. Using the same
URL makes it easier for users to access your Exchange server because they only have to
remember one address.

Regardless of your decision, you need to configure a private DNS zone for the address space
you choose. For more information about administering DNS zones, see Administering DNS
Server.

For more information about internal and external URLs on virtual directories, see Default
settings for Exchange virtual directories Virtual Directory Management.

Configure internal and external URLs to be the same
   1. Open the Exchange Management Shell on your Mailbox server.

   2. Store the host name of your Mailbox server in a variable that will be used in the next step.
     For example, Mailbox01.

          PowerShell

          $HostName = "Mailbox01"

<!-- p.605 -->

   3. Run each of the following commands in the Exchange Management Shell to configure
     each internal URL to match the virtual directory's external URL.

       PowerShell

        Set-EcpVirtualDirectory "$HostName\ECP (Default Web Site)" -InternalUrl
        ((Get-EcpVirtualDirectory "$HostName\ECP (Default Web Site)").ExternalUrl)

       PowerShell

        Set-WebServicesVirtualDirectory "$HostName\EWS (Default Web Site)" -
        InternalUrl ((Get-WebServicesVirtualDirectory "$HostName\EWS (Default Web
        Site)").ExternalUrl)

       PowerShell

        Set-ActiveSyncVirtualDirectory "$HostName\Microsoft-Server-ActiveSync
        (Default Web Site)" -InternalUrl ((Get-ActiveSyncVirtualDirectory
        "$HostName\Microsoft-Server-ActiveSync (Default Web Site)").ExternalUrl)

       PowerShell

        Set-OabVirtualDirectory "$HostName\OAB (Default Web Site)" -InternalUrl
        ((Get-OabVirtualDirectory "$HostName\OAB (Default Web Site)").ExternalUrl)

       PowerShell

        Set-OwaVirtualDirectory "$HostName\OWA (Default Web Site)" -InternalUrl
        ((Get-OwaVirtualDirectory "$HostName\OWA (Default Web Site)").ExternalUrl)

       PowerShell

        Set-PowerShellVirtualDirectory "$HostName\PowerShell (Default Web Site)" -
        InternalUrl ((Get-PowerShellVirtualDirectory "$HostName\PowerShell (Default
        Web Site)").ExternalUrl)

After you've configured the internal URL on the Mailbox server virtual directories, you need to
configure your private DNS records for Outlook on the web and other connectivity. Depending
on your configuration, you'll need to configure your private DNS records to point to the
internal or external IP address or FQDN of your Mailbox server. Examples of recommended
DNS records that you should create are described in the following table:

                                                                               ﾉ   Expand table

<!-- p.606 -->

 FQDN                         DNS record type              Value

 Mail.contoso.com             CNAME                        Mailbox01.corp.contoso.com

 Owa.contoso.com              CNAME                        Mailbox01.corp.contoso.com

How do you know this step worked?
To verify that you've successfully configured the internal URL on the Mailbox server virtual
directories, do the following:

   1. In the EAC, go to Servers > Virtual directories.

   2. In the Select server field, select the internet-facing Mailbox server.

   3. Select a virtual directory and then click Edit   .

   4. Verify that the Internal URL field is populated with the correct FQDN and service as
     shown in the following table:

                                                                                    ﾉ   Expand table

       Virtual directory                 Internal URL value

       Autodiscover                      No internal URL displayed

       ECP                               https://owa.contoso.com/ecp

       EWS                               https://mail.contoso.com/EWS/Exchange.asmx

       Microsoft-Server-ActiveSync       https://mail.contoso.com/Microsoft-Server-ActiveSync

       OAB                               https://mail.contoso.com/OAB

       OWA                               https://owa.contoso.com/owa

       PowerShell                        http://mail.contoso.com/PowerShell

To verify that you have successfully configured your private DNS records, do the following:

   1. Open a command prompt and run nslookup.exe .

   2. Change to a DNS server that can query your private DNS zone.

   3. In nslookup , look up the record of each FQDN you created. Verify that the value that's
     returned for each FQDN is correct.

<!-- p.607 -->

Configure different internal and external URLs
   1. Open the EAC, and go to Servers > Virtual directories,

   2. On the internet-facing Mailbox server, select the virtual directory that you want to
     configure, and then click Edit    .

   3. The virtual directory properties window opens. In the Internal URL field, replace the
     existing host name value in the URL (likely, the FQDN of the Mailbox server) with the new
     value that you want to use (for example, internal.contoso.com).

     For example, in the properties of the Exchange Web Services (EWS) virtual directory,
     change the existing value from
     https://Mailbox01.corp.contoso.com/ews/exchange.asmx            to
     https://internal.contoso.com/ews/exchange.asmx .

     When you're finished, click Save.

   4. Repeat the previous steps for each virtual directory you want to change.

        ７ Note

        The ECP and OWA virtual directory internal URLs must be the same. You can't set an
        internal URL on the Autodiscover virtual directory.

After you've configured the internal URL on the Mailbox server virtual directories, you need to
configure your private DNS records for Outlook on the web, and other connectivity. Depending
on your configuration, you'll need to configure your private DNS records to point to the
internal or external IP address or FQDN of your Mailbox server. An example of the
recommended DNS record that you should create is described in the following table:

                                                                                 ﾉ     Expand table

 FQDN                           DNS record type           Value

 internal.contoso.com           CNAME                     Mailbox01.corp.contoso.com

How do you know this step worked?

To verify that you've successfully configured the internal URLs in the Client Access services
virtual directories on the Mailbox server, do the following steps:

   1. In the EAC, go to Servers > Virtual directories.

<!-- p.608 -->

   2. In the Select server field, select the internet-facing Mailbox server.

   3. Select a virtual directory and then click Edit   .

   4. Verify that the Internal URL field is populated with the correct FQDN. For example, you
     may have set the internal URLs to use internal.contoso.com.

                                                                                     ﾉ   Expand table

       Virtual directory                Internal URL value

       Autodiscover                     No internal URL displayed

       ECP                              https://internal.contoso.com/ecp

       EWS                              https://internal.contoso.com/EWS/Exchange.asmx

       Microsoft-Server-ActiveSync      https://internal.contoso.com/Microsoft-Server-ActiveSync

       OAB                              https://internal.contoso.com/OAB

       OWA                              https://internal.contoso.com/owa

       PowerShell                       http://internal.contoso.com/PowerShell

To verify that you've successfully configured your private DNS records, do the following:

   1. Open a command prompt and run nslookup.exe .

   2. Change to a DNS server that can query your private DNS zone.

   3. In nslookup , look up the record of each FQDN you created. Verify that the value that's
     returned for each FQDN is correct.

Step 6: Configure an SSL certificate
Some services, such as Outlook Anywhere and Exchange ActiveSync, require certificates to be
configured on your Exchange server. The following steps show you how to configure an SSL
certificate from a third-party certificate authority (CA):

   1. Create an Exchange Server certificate request for a certification authority.

             You should request a certificate from a third-party CA so your clients automatically
             trust the certificate. For more information, see Best practices for Exchange
             certificates.

<!-- p.609 -->

           If you configured your internal and external URLs to be the same, Outlook on the
           web (when accessed from the internet) and Outlook on the web (when accessed
           from the Intranet) should both show owa.contoso.com. OAB (when accessed from
           the internet) and OAB (when accessed from the Intranet) should show
           mail.contoso.com.

           If you configured the internal URLs to be internal.contoso.com, Outlook on the web
           (when accessed from the internet) should show owa.contoso.com and Outlook on
           the web (when accessed from the Intranet) should show internal.contoso.com.

   2. Complete a pending Exchange Server certificate request.

   3. Assign certificates to Exchange Server services

           At minimum, you should select SMTP and IIS.

           If you receive the warning Overwrite the existing default SMTP certificate?, click
           Yes.

How do you know this step worked?
To verify that you've successfully added a new certificate, do the following steps:

   1. In the EAC, go to Servers > Certificates.

   2. Select the new certificate and then, in the certificate details pane, verify that the following
     are true:

           Status shows Valid

           Assigned to services shows, at minimum, IIS and SMTP.

How do you know this task worked?
To verify that you've configured mail flow and external client access, do the following steps:

   1. In Outlook, on an Exchange ActiveSync device, or on both, create a new profile. Verify that
     Outlook or the mobile device successfully creates the new profile.

   2. In Outlook, or on the mobile device, send a new message to an external recipient. Verify
     the external recipient receives the message.

   3. In the external recipient's mailbox, reply to the message you just sent from the Exchange
     mailbox. Verify the Exchange mailbox receives the message.

<!-- p.610 -->

4. Go to https://owa.contoso.com/owa   and verify that there are no certificate warnings.

<!-- p.611 -->

Verify Exchange Server installations
07/23/2025

APPLIES TO:      2016      2019      Subscription Edition

After you install Exchange Server 2016 or Exchange Server 2019, we recommend that you verify
the installation by running the Get-ExchangeServer cmdlet and by reviewing the Exchange
Setup log. If the setup process fails or errors occur during installation, you can use the Setup
log to find the source of the problem.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Run Get-ExchangeServer
To verify that Exchange installed successfully, run the following commands in the Exchange
Management Shell. To open the Exchange Management Shell, see Open the Exchange
Management Shell.

This command returns a summary list of the names, Active Directory sites, Exchange server
roles, Exchange editions, and Exchange versions of all Exchange servers in the organization.

  PowerShell

  Get-ExchangeServer

This example returns additional details about the Exchange server named Mailbox01.

  PowerShell

  Get-ExchangeServer -Identity Mailbox01 | Format-List

For detailed syntax and parameter information, see Get-ExchangeServer.

Review the Windows Application log and the
Exchange Setup log

<!-- p.612 -->

     Exchange Setup logs events in the Application log of the Windows Server. This log
     contains a history of each action that the system takes during Exchange setup and any
     errors that occurred (By default, the logging method is set to Verbose). You can use the
     Windows Event Viewer to find the messages related to Exchange setup.

     The Exchange Setup log is available at <system
     drive>:\ExchangeSetupLogs\ExchangeSetup.log (<system drive> is the drive where
     Windows is installed). The Setup log tracks the progress of every task during the
     Exchange installation and configuration. The file contains information about the status of
     the prerequisite and system readiness checks before installation starts, the application
     installation progress, and the configuration changes that are made to the system. Check
     this log file to verify that Exchange was installed as expected.

We recommend that you start your review of the Windows Application log and/or the
Exchange Setup log by searching for errors. If you find an error entry, read the associated text
to determine the cause of the error.

<!-- p.613 -->

Install the Exchange management tools
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The management tools in Exchange Server 2016 and Exchange Server 2019 include the
Exchange Management Shell and the Exchange Toolbox. You can install the management tools
on other client computers or servers in the Active Directory domain to help you manage your
Exchange organization. The management tools have similar operating system, .NET Framework,
and Windows Management Framework (Windows PowerShell) requirements as an Exchange
server. The notable exception is: you can install the management tools on client versions of
Windows. For more information, see Exchange Server system requirements and Exchange
Server prerequisites.

   Tip

  If you wish to use Exchange Management Tools for Recipient Management without
  keeping an Exchange Server, see Manage on-premises recipients in a Hybrid
  Environment using Exchange Management tools

  ７ Note

  The management tools don't include the Exchange admin center (EAC). The EAC is a web-
  based console that's hosted on Exchange 2016 Mailbox servers, and like any web site, you
  can access the EAC from other computers. For more information about the EAC, see
  Exchange admin center in Exchange Server.

For more information about the Exchange Management Shell, see Exchange Server PowerShell
(Exchange Management Shell).

What do you need to know before you begin?
      Estimated time to complete: 20 minutes

      The computer where you want to install the Exchange management tools requires access
      to Setup.exe in the Exchange installation files. To download the latest version of Exchange,
      see Updates for Exchange Server.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

<!-- p.614 -->

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online, or Exchange Online Protection .

Use the Exchange 2016 Setup wizard to install the
Exchange management tools
 1. In File Explorer on the computer where you want to install the management tools, right-
   click on the Exchange ISO image file that you downloaded, and then select Mount. In the
   resulting virtual DVD drive that appears, start Exchange Setup by double-clicking
    Setup.exe .

 2. The Exchange Server Setup wizard opens. On the Check for Updates? page, choose one
   of the following options, and then click Next to continue:

   Connect to the Internet and check for updates: We recommend this option, which
   searches for updates to the version of Exchange that you're currently installing (it doesn't
   detect newer Cumulative Updates). This option takes you to the Downloading Updates
   page that searches for updates. Click Next to continue.

         Don't check for updates right now

<!-- p.615 -->

3. The Copying Files page shows the progress of copying files to the local hard drive.
  Typically, the files are copied to %WinDir%\Temp\ExchangeSetup , but you can confirm the
  location in the Exchange Setup log at C:\ExchangeSetupLogs\ExchangeSetup.log .

<!-- p.616 -->

4. On the Introduction page, click Next to continue.

5. On the License Agreement page, review the software license terms, select I accept the
  terms in the license agreement, and then click Next to continue.

<!-- p.617 -->

6. On the Recommended Settings page, choose one of the following settings:

       Use recommended settings: Exchange automatically sends error reports and
       information about your computer hardware and how you use Exchange to
       Microsoft. For information about what's sent to Microsoft and how it's used, click ?
       or the help links on the page.

       Don't use recommended settings: These settings are disabled, but you can enable
       them at any time after Setup completes.

  Click Next to continue.

<!-- p.618 -->

7. On the Server Role Selection page, configure the following settings:

       Select Management tools.

       Automatically install Windows Server roles and features that are required to
       install Exchange: Select this option to have the Setup wizard install the required
       Windows prerequisites. You might need to reboot the computer to complete the
       installation of some Windows features. If you don't select this option, you need to
       install the Windows features manually.

       Note: Selecting this option installs only the Windows features that are required by
       Exchange. You need to install other prerequisites manually. For more information,
       see Exchange Server prerequisites.

  Click Next to continue.

<!-- p.619 -->

8. On the Installation Space and Location page, either accept the default installation
  location ( C:\Program Files\Microsoft\Exchange Server\V15 ), or click Browse to choose a
  new location. Make sure that you have enough disk space available in the location where
  you want to install the management tools. Click Next to continue.

<!-- p.620 -->

9. If this is the first installation of Exchange in your organization (Exchange server or the
  management tools), you arrive on the Exchange Organization page. On this page,
  configure the following settings:

        Specify the name for this Exchange organization: The default value is First
        Organization, but you typically use the company name for this value. The
        organization name is used internally by Exchange, isn't typically seen by users,
        doesn't affect the functionality of Exchange, and doesn't determine what you can
        use for email addresses.

           The organization name can't contain more than 64 characters, and can't be blank.

           Valid characters are A to Z, a to z, 0 to 9, hyphen or dash (-), and space, but
           leading or trailing spaces aren't allowed.

           You can't change the organization name after it's set.

        Apply Active Directory split permission security model to the Exchange
        organization: Most organizations don't need to select this option. If you need to
        separate management of Active Directory security principals and the Exchange
        configuration, split permissions might work for you. For more information, click ?.

  Click Next to continue.

<!-- p.621 -->

10. On the Readiness Checks page, verify that the organization and server role prerequisite
   checks completed successfully. If they haven't, the only option on the page is Retry, so
   you need to resolve the errors before you can continue.

<!-- p.622 -->

   After you resolve the errors, click Retry to run the prerequisite checks again. You can fix
   some errors without exiting Setup, while the fix for other errors requires you to restart the
   computer. If you restart the computer, you need to start over at Step 2.

   When no more errors are detected on the Readiness Checks page, the Retry button
   changes to Install so you can continue. Be sure to review any warnings, and then click
   Install to install the management tools.

11. On the Setup Completed page, click Finish, and then restart the computer.

<!-- p.623 -->

Use Exchange unattended Setup mode to install
the Exchange management tools
 1. In File Explorer on the computer where you want to install the Exchange management
   tools, right-click on the Exchange ISO image file that you downloaded, and then select
   Mount.

 2. To install the Exchange management tools from the command line, use the following
   syntax in elevated command prompt (a Command Prompt window you opened by
   selecting Run as administrator):

 ７ Note

     The previous /IAcceptExchangeServerLicenseTerms switch will not work starting with
     the September 2021 Cumulative Updates (CUs). You now must use either
     /IAcceptExchangeServerLicenseTerms_DiagnosticDataON or
     /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF for unattended and scripted
     installs.

     The examples below use the /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
     switch. It's up to you to change the switch to

<!-- p.624 -->

        /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

  Console

  <Virtual DVD drive letter>:\Setup.exe
  /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Role:ManagementTools
  [/EnableErrorReporting] [/CustomerFeedbackEnabled:<True | False>]
  [/InstallWindowsComponents] [/TargetDir:<Target folder>] [/OrganizationName:
  <Name>]

This example uses the Exchange Setup files on drive E: to install the management tools on the
local server

  Console

  E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
  /Role:ManagementTools

For more information, see Install Exchange using unattended mode.

<!-- p.625 -->

Feature Flighting in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

Overview
Historically, before installing an Exchange update in production, organizations often deploy
updates in a test environment to first validate the update before deploying it to their
production environment. This is an important task, but it is also time-consuming, and it can
slow down the deployment of important updates. Moreover, not all organizations have test
environments.

Feature Flighting provides an additional way for administrators to test and roll out select new
features across their Exchange Server organization. Feature Flighting is an optional cloud-
based service for on-premises Exchange servers. It uses the Office Config Service (OCS) - the
same endpoint used by the Emergency Mitigation service and Microsoft Office clients—to
check for updates from Microsoft related to flighted features

With Feature Flighting, administrators can deploy updates immediately and control when a
flighted feature is enabled in their environment. Feature Flighting also enables Microsoft to
disable a flighted feature in case a significant issue is discovered after the update containing
the flighted feature is released.

Feature Flighting does not apply to all new features and changes in future updates. The
Exchange Server engineering team determines which features are distributed via Feature
Flighting, and a living, detailed list of flighted features is maintained in this article. Using
Feature Flighting is optional, but it is enabled by default. You can configure it or disable it by
following the steps outlined below.

Flighted Features
The table provides a detailed list of all currently flighted features. This table is a living table;
Microsoft updates the table with new flights and changes to the affected Ring at least 7 days
before they become active. Microsoft may not be able to announce changes several days in
advance if a feature needs to be disabled (Recalled) due to a regression or known issue.

                                                                                      ﾉ   Expand table

<!-- p.626 -->

 Feature    Description         Rings   Admin Approval     Recalled    Start Build      End Build

 PING.1.0   Heartbeat Probe     0,1,2   No                 No          15.02.1748.005   N/A

How Feature Flighting works
Feature Flighting is an innovative method for managing features and changes in Exchange
Server that allows Microsoft to introduce new features and changes for Exchange Server in an
initially disabled state. Here's how it works:

   1. Initial Introduction: When a flighted feature or change is introduced, it's included in the
     Exchange Server update (CU or SU) in a disabled state. This behavior ensures that the
     feature doesn't immediately affect the server's operation.
   2. Controlled Enablement: Flighted features and changes can then be automatically enabled
     on all Exchange servers within a specific Ring. This phased approach allows Microsoft to
     monitor the feature's performance and gather telemetry data.
   3. Evaluation and Deployment: Based on the collected telemetry (and any feedback we
     might receive on our blog , via support cases, or from other sources), Microsoft
     evaluates the feature's stability and effectiveness. If the feature performs well, it can then
     be gradually deployed to Exchange servers in other Rings.
   4. Recall Mechanism: A key advantage of Feature Flighting is the ability to recall a feature or
     change if any issues or regressions are detected. This helps ensure that any problematic
     features can be disabled quickly to maintain the stability and reliability of the Exchange
     Server environment.

  ７ Note

  Feature Flighting isn't available for Edge Transport servers.

This results into the following benefits:

     Enhanced Control: Administrators have more granular control over when and how new
     features are introduced.
     Improved Stability: By deploying features in a staged manner, potential issues can be
     identified and addressed before widespread deployment.
     Flexibility: The ability to recall features ensures that any regressions or known issues can
     be quickly mitigated.

Prerequisites

<!-- p.627 -->

A new service called Microsoft Exchange Flighting service (MSExchangeFlighting) controls
Feature Flighting. This service checks for and downloads Feature Flight Definitions (FFD) from
OCS hourly and manages the activation and deactivation of flighted features based on the
configured Ring.

Feature Flighting can't be used in air gapped environments or in environments without
outbound connectivity to OCS. the Exchange Flighting service requires outbound connectivity
to OCS to check for and download FFDs. You don't need to take any action if your servers can't
reach OCS. Additionally, Feature Flighting is not yet available on Edge Transport servers.

We recommend checking our documentation and the Exchange Team Blog                     regularly to stay
informed about known issues that may temporarily disable a feature as a mitigation measure.

                                                                                        ﾉ   Expand table

 Endpoint          Address                        Port   Description

 Office Config     officeclient.microsoft.com/*   443    Endpoint for the Microsoft Exchange Flighting
 Service                                                 Service to download FFDs

If you're using a network proxy to allow outbound connectivity, ensure that the
InternetWebProxy is configured on each of your Exchange servers:

  PowerShell

  Set-ExchangeServer -Identity <ServerName> -InternetWebProxy
  <http://proxy.contoso.local:port>

You must also configure the proxy settings for WinHTTP , which is a component of Windows that
handles HTTP requests for applications that don't use the WinINet API :

  command

  netsh winhttp set proxy <proxy.contoso.com:port>

In addition to outbound connectivity to OCS, the Flighting Service also needs outbound
connectivity to various Certificate Revocation List (CRL) endpoints. This is required to verify the
certificates used to sign the FFDs. We recommend letting Windows maintain the Certificate
Trust List (CTL)   on your machine. To enable Windows to maintain the CTL, ensure that the
following URL is accessible from the computer where Exchange Server is installed:

                                                                                        ﾉ   Expand table

<!-- p.628 -->

 Endpoint                       Address                       Port   Description

 Certificate Trust List         ctldl.windowsupdate.com/*     80     Endpoint for downloading the Certificate
 Download                                                            Trust List

Rings
Feature Flighting uses a deployment mechanism called Rings that defines when, or in what
sequence, a feature is enabled on a particular Exchange server. Every Exchange server running
Exchange Server 2019 CU15 or later is automatically assigned to a Ring. The default
assignment can be changed by an admin at any time. The following Rings are available:

                                                                                              ﾉ   Expand table

 Ring      Name           Default     Description
 No.                      Ring

 0         Early          No          This is the earliest Ring and it's intended to be used for testing new
           Adopter                    features. If an Exchange server is assigned to this Ring, flighted features
           Ring                       introduced in an update are immediately enabled after the update is
                                      installed. This happens regardless of the Feature Classification.

 1         Worldwide      Yes         This is the default Ring assigned to all Exchange servers when the first
           Ring                       build that supports Feature Flighting is installed (for example, CU15).
                                      Servers in this Ring receive new features as soon as Microsoft has
                                      confirmed that the features are ready for general availability.

 2         Admin          No          Exchange servers in this Ring don't automatically enable any new
           Action Ring                flighted features. This Ring allows admins to revert to previous
                                      experience (for example, roll back). Flighted features are shipped in a
                                      disabled state and must be enabled by the admin using Set-
                                      ExchangeFeature as explained in the Feature States section.

     ） Important

     Moving a server between Rings can result in certain features being enabled or disabled,
     depending on the Feature Status defined in the Flighting Service for the new Ring.

The following workflow outlines how the Ring determines whether a flighted feature should be
enabled or not:

<!-- p.629 -->

                                                                                              

You can use Exchange Management Shell (EMS) to assign an Exchange server to a specific Ring.
In this example, the Exchange server is assigned to Ring 0:

  PowerShell

  Set-ExchangeServer -Identity <ServerName> -RingLevel 0

  ） Important

  If you don't want Microsoft to automatically enable new features or make changes to your
  server via Feature Flighting, you must assign your Exchange servers to Ring 2. Stopping
  and/or disabling the Microsoft Exchange Flighting Service (MSExchangeFlighting) isn't
  supported.

The following example assigns a server to Ring 2:

  PowerShell

  Set-ExchangeServer -Identity <ServerName> -RingLevel 2

Feature Classification
There are two types of features that can be managed by the Flighting Service: features with
prerequisites and features without prerequisites. The key distinction is that some features

<!-- p.630 -->

depend on certain prerequisites that must be fulfilled:

     Features with prerequisites:
        These features need some preconditions to be met before they can be used. For
        example, all Exchange servers in the organization must be running a specific build.
        Example: Certificate Signing of PowerShell serialization payloads depends on a valid
        Auth Certificate, which is available on all Exchange servers.
     Features without any prerequisites:
        These features work out of the box without dependencies or prerequisites. All you
        need to do is install the update and enable the feature.
        Example: Support for AES256-CBC-encrypted content              doesn't have any
        dependencies or prerequisites.

For Exchange servers in Ring 1, features with prerequisites are assigned the
FeaturesAwaitingAdminApproval state, as they need administrator approval before becoming

active. In contrast, for Exchange servers in Ring 0, features with prerequisites are enabled
without waiting for administrator approval.

Feature States
Each flighted feature is assigned a Feature State that indicates the current state of the feature.
Feature States are an essential component of Feature Flighting. When a feature is flighted, it
gets one or more of the following Feature States assigned:

                                                                                       ﾉ   Expand table

 Feature State                   Feature      Description
                                 Enabled

 FeaturesEnabled                 Yes          This feature is enabled on the server.

 FeaturesDisabled                No           Feature Flighting didn't enable this feature on the server
                                              either because Microsoft recalled it due to a regression or
                                              because the Exchange Server administrator blocked it (for
                                              example, because the server doesn't fulfill the required
                                              prerequisites yet).

 FeaturesAwaitingAdminApproval   No           This feature requires explicit approval by an Exchange
                                              Server administrator.

 FeaturesApproved                Yes          An Exchange Server administrator explicitly approved this
                                              feature, and it's now active.

 FeaturesBlocked                 No           This feature was explicitly blocked by an Exchange Server
                                              administrator and remains in disabled state.

<!-- p.631 -->

For example, if a feature is waiting for approval, it has both the FeaturesAwaitingAdminApproval
and FeaturesDisabled states assigned. Once the admin approves the feature, it's assigned the
FeaturesApproved and FeaturesEnabled states.

   Tip

  If you run the latest version of the Exchange Server Health Checker     script, it shows you
  information such as the server's assigned Ring, as well as features controlled by the
  Feature Flighting.

You can use EMS to query the feature states for a specific Exchange server:

  PowerShell

  Get-ExchangeServer -Identity <ServerName> | Format-List Features*

To get an overview of all available features, use the Get-ExchangeFeature cmdlet. The following
command returns all features which are enabled:

  PowerShell

  Get-ExchangeFeature -Status "Enabled"

You can also use the -FeatureID parameter together with the name of a feature, to query its
status and a short description:

  PowerShell

  Get-ExchangeFeature -FeatureID "PING.1.0"

After executing the previous command, the Exchange server will return a result like the
following:

  PowerShell

  Server              FeatureID   RingLevel       Status                      Description
  ------              ---------   ---------       ------                      -----------
  EXCH01              PING.1.0    1               Enabled                     Heartbeat
  Probe. Validates the Telemetry Channel

This information is important in case you want to approve a new feature or change that
requires admin approval. You'll also need this information when you want to prevent a feature

<!-- p.632 -->

from becoming enabled.

Feature naming is standardized using the following format: <FeatureId>.<SettingId>.
<Version>

This format allows features to have multiple settings, which are used to control it. Assume that
there's a feature FeatureID=F4 which can be controlled via two setting overrides SettingId=1
and SettingId=2 , you'll see the following flighting entries:

      F4.1.0

      F4.2.0

To approve a new feature awaiting admin approval, use Set-ExchangeFeature with the -
Approve parameter. Once the feature is approved or blocked, it remains in an intermittent state

until the next Feature Flighting cycle runs, which may take up to an hour at most:

  PowerShell

  Set-ExchangeFeature -Identity <ComputerName> -FeatureID @("F1.1.1") -Approve

It's also possible to approve multiple features at once:

  PowerShell

  Set-ExchangeFeature -Identity <ComputerName> -FeatureID @("F1.1.1", "F1.2.1",
  "F2.1.1") -Approve

To prevent a feature from being enabled, use Set-ExchangeFeature with the -Block parameter.
As shown in the previous example, it's also possible to block multiple features at once:

  PowerShell

  Set-ExchangeFeature -Identity <ComputerName> -FeatureID @("F1.1.1", "F1.2.1",
  "F2.1.1") -Block

Example: Lifecycle of a flighted feature
This section illustrates the workflow and lifecycle of a flighted feature called Feature1 .

Contoso has two Exchange 2019 servers, EXCHPRD01 and EXCHPRD02 that are members of a

database availability group (DAG) called DAGPRD01 . They also have a third Exchange 2019

<!-- p.633 -->

server, EXCHTST01 which is used for validating and testing new updates, and which isn't a
member of the DAG.

The administrator first installs Exchange Server 2019 CU15 on EXCHTST01 and, after all tests
have been successfully completed, the administrator installs CU15 on EXCHPRD01 and
EXCHPRD02 . The administrator assigns EXCHTST01 to Ring 0 so that it receives the flighted

features and changes as soon as they become available.

First, they validate the current Ring assignment:

  PowerShell

  Get-ExchangeServer | Format-List Identity,RingLevel

  Identity : EXCHPRD01
  RingLevel : 1

  Identity : EXCHPRD02
  RingLevel : 1

  Identity : EXCHTST01
  RingLevel : 1

Next they assign EXCHTST01 to a Ring 0:

  PowerShell

  Set-ExchangeServer -Identity EXCHTST01 -RingLevel 0

  Confirm
  Changing the RingLevel of the server will change the flighting of the features
  based on the RingLevel selected. Changes will apply once the flighting service
  applies these changes. Are you sure you want to continue?
  [Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (default is "Y"):

A few months later, Microsoft releases an SU for CU15. In the release notes for the SU, the
administrator learns that the SU contains a new flighted feature, Feature1 . After installing the
SU on all servers, they want to confirm that Feature1 is enabled only on EXCHTST01 and not on
the production servers EXCHPRD01 and EXCHPRD02 :

  PowerShell

  Get-ExchangeServer | Get-ExchangeFeature

  Server                 FeatureID     RingLevel    Status                    Description
  ------                 ---------     ---------    ------                    -----------
  EXCHPRD01              PING.1.0      1            Enabled                   Heartbeat

<!-- p.634 -->

  Probe. Validates the Telemetry Channel
  EXCHPRD01           F1.1.0      1                Disabled                   Feature1
  introduces a new functionality
  EXCHPRD02           PING.1.0    1                Enabled                    Heartbeat
  Probe. Validates the Telemetry Channel
  EXCHPRD02           F1.1.0      1                Disabled                   Feature1
  introduces a new functionality
  EXCHTST01           PING.1.0    0                Enabled                    Heartbeat
  Probe. Validates the Telemetry Channel
  EXCHTST01           F1.1.0      0                Enabled                    Feature1
  introduces a new functionality

On EXCHTST01 , the administrator tests that their workflows and 3rd party applications aren't
adversely affected by Feature1 and they learn that there's a problem introduced by Feature1 .
So, the administrator uses the following command to prevent Feature1 from becoming
enabled in Ring 1 and to disable it in Ring 0 where it's already active:

  PowerShell

  Get-ExchangeServer | Set-ExchangeFeature -FeatureID "F1.1.0" -Block

  Confirm
  Are you sure you want to perform this action?
  By running this cmdlet, the features will be updated on server "EXCHTST01".
  [Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (default is "Y"):

They confirm that Feature1 was successfully blocked:

  PowerShell

  Get-ExchangeServer | Get-ExchangeFeature

  Server              FeatureID   RingLevel        Status                     Description
  ------              ---------   ---------        ------                     -----------
  EXCHPRD01           PING.1.0    1                Enabled                    Heartbeat
  Probe. Validates the Telemetry Channel
  EXCHPRD01           F1.1.0      1                Blocked                    Feature1
  introduces a new functionality
  EXCHPRD02           PING.1.0    1                Enabled                    Heartbeat
  Probe. Validates the Telemetry Channel
  EXCHPRD02           F1.1.0      1                Blocked                    Feature1
  introduces a new functionality
  EXCHTST01           PING.1.0    0                Enabled                    Heartbeat
  Probe. Validates the Telemetry Channel
  EXCHTST01           F1.1.0      0                Blocked                    Feature1
  introduces a new functionality

Contoso contacts Microsoft Support       to report the issue. Microsoft confirms the issue and
plans to address it in the next update. After the update with the fix is released, Contoso

<!-- p.635 -->

deploys the update on their servers. The administrator tests their workflows and 3rd party
applications and confirms that everything works as expected. The admin now wants to enable
Feature1 on their production servers.

After learning from the release notes that Feature1 has dependencies, the administrator
checks to see if admin approval is required:

  PowerShell

  Get-ExchangeServer -Identity EXCHPRD01 | Format-List Features*

  FeaturesApproved              : {}
  FeaturesAwaitingAdminApproval : {F1.1.0}
  FeaturesEnabled               : {PING.1.0}
  FeaturesBlocked               : {}
  FeaturesDisabled              : {}

To approve and enable Feature1 , the administrator runs the following command:

  PowerShell

  Get-ExchangeServer -Identity EXCHPRD* | Set-ExchangeFeature -FeatureID "F1.1.0" -
  Approve

  Confirm
  Are you sure you want to perform this action?
  By running this cmdlet, the features will be updated on server "EXCHPRD01".
  [Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (default is "Y"):

Next, they validate that the feature was approved and enabled:

  PowerShell

  Get-ExchangeServer -Identity EXCHPRD01 | Format-List Features*

  FeaturesApproved              : {F1.1.0}
  FeaturesAwaitingAdminApproval : {}
  FeaturesEnabled               : {PING.1.0, F1.1.0}
  FeaturesBlocked               : {}
  FeaturesDisabled              : {}

Once Microsoft considers all issues resolved, it enables the feature for all customers by default.
This will happen in the next update, which enables the feature outside of feature flighting for
all customers.

Diagnostic Data

<!-- p.636 -->

When data sharing is enabled, Feature Flighting sends diagnostic data to the OCS. This data
helps Microsoft to identify the saturation of flighted features. To learn more about what is
collected and how to disable data sharing, see Diagnostic Data collected for Exchange Server.

<!-- p.637 -->

Configure instant messaging integration
with Outlook on the web in Exchange
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

To configure instant messaging (IM) integration between Skype for Business Server and
Outlook on the web (formerly known as Outlook Web App) in Exchange 2016 or Exchange
2019, you need to use the Exchange Management Shell. This is different than previous versions
of Exchange where you needed to edit the web.config file. If you edit the web.config file
instead of using the steps in this topic, the settings are ignored and Outlook on the web users
receive the following error message:

There's a problem with instant messaging. Please try again later.

Also, the following health set errors are generated on the Exchange server:

      HealthSet: OWA.Protocol.Dep

      Subject: OWA.Protocol.Dep health set unhealthy
      (OwaIMInitializationFailedMonitor/OWA.Protocol.Dep) - Owa InstantMessaging provider

      failed to intialize

      Message: Owa InstantMessaging provider failed to initialize due to incorrect IM
      configuration on the server. Signin attempts to OWA IM will fail. Error Message:
      {Instant Messaging Certificate Thumbprint is null or empty on web.config).

Use the procedures in this topic to fix these errors and configure IM integration between Skype
for Business Server and Exchange 2016 or Exchange 2019. IM integration between Lync Server
2013 and Exchange 2016 or later isn't supported. For details on setting up Skype for Business
Server with Outlook on the web (formerly known as Outlook Web App), see Configure
integration between on-premises Skype for Business Server and Outlook Web App

What do you need to know before you begin?
      Estimated time to complete: 5 minutes

      Exchange and Skype for Business integration requires server certificates that are trusted
      by all of the servers involved. The procedures in this topic assume that you already have
      the required certificates. For more information, see Plan to integrate Skype for Business
      Server 2015 and Exchange. The required IM certificate thumbprint refers to the Exchange
      Server certificate assigned to the IIS service.

<!-- p.638 -->

     You can only use PowerShell to perform this procedure. To learn how to open the
     Exchange Management Shell in your on-premises Exchange organization, see Open the
     Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Client Access virtual directory
     settings" entry in the Clients and mobile devices permissions topic.

     Depending on your Skype for Business Server topology, you may have multiple FrontEnd
     pools, you should pick the regional endpoint (closest pool to the exchange AD site):
     IMServerName=<Skype Server\pool Name> .

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Use the Exchange Management Shell to configure
IM integration with Outlook on the web

Step 1: Specify the IM server and IM certificate thumbprint
Use the following syntax in the Exchange Management Shell to specify the IM server and IM
certificate thumbprint:

  PowerShell

  New-SettingOverride -Name "<UniqueOverrideName>" -Component OwaServer -Section
  IMSettings -Parameters @("IMServerName=<Skype server/pool
  name>","IMCertificateThumbprint=<Certificate Thumbprint>") -Reason "
  <DescriptiveReason>" [-Server <ServerName>]

Notes:

     To configure the same settings on all Exchange 2016 and Exchange 2019 servers in the
     Active Directory forest, don't use the Server parameter.

     To configure the settings on a specific Exchange 2016 or Exchange 2019 server, use the
     Server parameter and the name of the server (don't use the fully qualified domain name
     or FQDN). This method is useful when you need to specify different settings on different
     Exchange servers.

<!-- p.639 -->

This example specifies the IM server and IM certificate thumbprint on all Exchange 2016 and
Exchange 2019 servers in the organization.

     Setting override name: "IM Override" (must be unique)

     Skype for Business server name: skype01.contoso.com

     Certificate thumbprint: CDF34A740E9D225A1A06193A9D44B2CE22775308

     Override reason: Configure IM

  PowerShell

  New-SettingOverride -Name "IM Override" -Component OwaServer -Section IMSettings
  -Parameters
  @("IMServerName=skype01.contoso.com","IMCertificateThumbprint=CDF34A740E9D225A1A06
  193A9D44B2CE22775308") -Reason "Configure IM"

This example specifies the IM server and IM certificate thumbprint, but only on the server
named Mailbox01.

  PowerShell

  New-SettingOverride -Name "Mailbox01 IM Override" -Component OwaServer -Section
  IMSettings -Parameters
  @("IMServerName=skype01.contoso.com","IMCertificateThumbprint=CDF34A740E9D225A1A06
  193A9D44B2CE22775308") -Reason "Configure IM" -Server Mailbox01

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

<!-- p.640 -->

  Argument Refresh

Step 3: Restart the Outlook on the web pool on the Exchange
server
Run the following command in the Exchange Management Shell or in Windows PowerShell on
the server. You need to do this on every Exchange 2016 or Exchange 2019 server that's used for
Outlook on the web.

  PowerShell

  Restart-WebAppPool MSExchangeOWAAppPool

Use the Exchange Management Shell to update the
existing IM integration with Outlook on the Web
when the Exchange IIS Certificate is renewed or
changed

Step 1: Update the IM certificate thumbprint on the existing
Override
Use the following syntax in the Exchange Management Shell to specify new IM certificate
thumbprint:

  PowerShell

  Set-SettingOverride -Name "<UniqueOverrideName>" -Parameters
  @("IMCertificateThumbprint=<Certificate Thumbprint>") -Reason "
  <DescriptiveReason>" [-Server <ServerName>]

Notes:

     To update the thumbprint on all Exchange 2016 and Exchange 2019 servers in the Active
     Directory forest, don't use the Server parameter.

     To update the thumbprint on a specific Exchange 2016 or Exchange 2019 server, use the
     Server parameter and the name of the server (don't use the fully qualified domain name
     or FQDN). This method is useful when you need to specify different settings on different
     Exchange servers.
