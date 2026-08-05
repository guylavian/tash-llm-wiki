---
title: "Exchange Server — pages 1281-1320"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1281-1320
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1281-1320
family: exchange
documentKind: "doc"
abstract: "Export only the contents of this mailbox's archive When you're finished, click Next. 3. On the next page, enter the UNC path and filename of the target .pst file. When you're finished, click Next. 4. On the last page, configure one of these settings: Leave the Send email to the"
---

# Exchange Server — pages 1281-1320

<!-- p.1281 -->

       Export only the contents of this mailbox's archive

  When you're finished, click Next.

3. On the next page, enter the UNC path and filename of the target .pst file.

  When you're finished, click Next.

4. On the last page, configure one of these settings:

       Leave the Send email to the mailbox below when the .pst file has been exported
       check box selected. Click Browse to add or remove notification recipients.

       Clear the Send email to the mailbox below when the .pst file has been exported
       check box.

<!-- p.1282 -->

     When you're finished, click Finish.

Use the Exchange Management Shell to create a mailbox
export request
To create a mailbox export request, use this syntax:

  PowerShell

  New-MailboxExportRequest [-Name <UniqueName>] -Mailbox <TargetMailboxIdentity> -
  FilePath <UNCPathToPST> [-IsArchive] [-SourceRootFolder <MailboxFolder>] [-
  TargetRootFolder <PSTFolder>] [-IncludeFolders <MailboxFolder1>,
  <MailboxFolder2>...] [-ExcludeFolders <MailboxFolder1>,<MailboxFolder2>...] [-
  ContentFilter <Filter>] [-Priority <PriorityValue>]

This example creates a new mailbox export request with these settings:

     Mailbox export request name: The default value MailboxExport is used, because we
     aren't using the Name parameter. The unique identity of the mailbox export request is
     <MailboxIdentity>\MailboxExportX (X is either not present, or has the value 0 to 9).

     Source mailbox: Valeria Barrios

     Target .pst file: \SERVER01\PSTFiles\Vbarrios.pst

     Content and folders: Content in all folder paths in the source mailbox is replicated in the
     target .pst file.

     Priority: Normal , because we aren't using the Priority parameter.

  PowerShell

  New-MailboxExportRequest -Mailbox "Valeria Barrios" -FilePath

<!-- p.1283 -->

  \\SERVER01\PSTFiles\Vbarrios.pst

This example creates a new mailbox export request with these settings:

     Mailbox export request name: The custom name Kathleen Reiter Export is specified by
     the Name parameter. Specifying a custom name allows more than 10 mailbox export
     requests for the mailbox. The unique identity value of the mailbox export request is
     <MailboxIdentity>\<MailboxExportRequestName> (for example, kreiter\Kathleen Reiter

     Export ).

     Source mailbox: The archive mailbox for Kathleen Reiter (Kathleen's primary mailbox alias
     is kreiter).

     Target .pst file: \SERVER01\PSTFiles\Archives\Kathleen Reiter.pst

     Content and folders: Only content in the Inbox folder of the mailbox is exported
     (regardless of the localized name of the folder).

     Priority: High

  PowerShell

  New-MailboxExportRequest -Name "Kathleen Reiter Export" -Mailbox kreiter -FilePath
  "\\SERVER01\PSTFiles\Kathleen Reiter.pst" -IsArchive -IncludeFolders "#Inbox#" -
  Priority High

For detailed syntax and parameter information, see New-MailboxExportRequest.

How do you know this worked?
To verify that you've successfully created a mailbox export request, do any of these steps:

     In the EAC, click the notification viewer   to view the status of the request.

     If you created the mailbox export request in the EAC, and selected the option to send
     notification email messages, check the notification messages. The sender is Microsoft
     Exchange. The first message has the subject Your Export PST request has been received .
     If the export request completed successfully, you'll receive another message with the
     subject Export PST has finished .

     Replace <MailboxIdentity> with the name, email address, or alias of the source mailbox,
     and run this command in the Exchange Management Shell to verify the basic property
     values:

<!-- p.1284 -->

        PowerShell

        Get-MailboxExportRequest -Mailbox "<MailboxIdentity>" | Format-List
        Name,FilePath,Mailbox,Status

     Replace <MailboxIdentity> and <MailboxExportRequestName> with the appropriate
     values, and run this command in the Exchange Management Shell to verify the details:

        PowerShell

        Get-MailboxExportRequestStatistics -Identity "<MailboxIdentity>\
        <MailboxExportRequestName>"

Use the Exchange Management Shell to view
mailbox export requests
By default, the Get-MailboxExportRequest cmdlet returns the name, source mailbox, and
status of mailbox export requests. If you pipeline the command to the Format-List cmdlet,
you'll only get a limited number of additional useful details:

     FilePath: The target .pst file.

     RequestGUID: The unique GUID value of the mailbox export request.

     RequestQueue: The mailbox database that the export request is being run on.

     BatchName: The optional batch name for the mailbox export request.

     Identity: The unique identity value of the mailbox export request (<MailboxIdentity>\
     <MailboxExportRequestName>).

By default, the Get-MailboxExportRequestStatistics cmdlet returns the name, status, alias of
the source mailbox, and the completion percentage of mailbox export requests. If you pipeline
the command to the Format-List cmdlet, you'll see detailed information about the mailbox
export request.

This example returns the summary list of all mailbox export requests.

  PowerShell

  Get-MailboxExportRequest

<!-- p.1285 -->

This example returns additional information for mailbox export requests from the mailbox Akia
Al-Zuhairi.

  PowerShell

  Get-MailboxExportRequest -Mailbox "Akia Al-Zuhairi" | Format-List

This example returns the summary list of in-progress mailbox export requests for mailboxes
that reside on the mailbox database named DB01.

  PowerShell

  Get-MailboxExportRequest -Status InProgress -Database DB01

This example returns the summary list of completed mailbox export requests in the batch
named Export DB01 PSTs.

  PowerShell

  Get-MailboxExportRequest -Status Completed -BatchName "Export DB01 PSTs"

For detailed syntax and parameter information, see Get-MailboxExportRequest.

To view detailed information about a mailbox export request, use this syntax:

  PowerShell

  Get-MailboxExportRequestStatistics -Identity <MailboxExportRequestIdentity> [-
  IncludeReport] | Format-List

Where <MailboxExportRequestIdentity> is the identity value of the mailbox export request
(<MailboxIdentity>\ <MailboxExportRequestName> or <RequestGUID>).

This example returns detailed information for the mailbox export request named
MailboxExport for Akia Al-Zuhairi's mailbox, including the log of actions in the Report
property.

  PowerShell

  Get-MailboxExportRequestStatistics -Identity "aal-zuhairi\MailboxExport" -
  IncludeReport | Format-List

For detailed syntax and parameter information, see Get-MailboxExportRequestStatistics.

<!-- p.1286 -->

Use the Exchange Management Shell to modify
mailbox export requests
You can modify mailbox export requests that haven't completed. You can't modify the
fundamental settings of an existing request (for example, the source mailbox, target .pst file,
the source content in the mailbox, or the destination in the target .pst file).

To modify a mailbox export request, use this syntax:

  PowerShell

  Set-MailboxExportRequest -Identity <MailboxIdentity>\<MailboxExportRequestName> [-
  BadItemLimit <value>] [-LargeItemLimit <value>] [-AcceptLargeDataLoss]

This example modifies the failed mailbox export request for the mailbox of Valeria Barrios to
accept up to five corrupted mailbox items.

  PowerShell

  Set-MailboxExportRequest -Identity "Valeria Barrios\MailboxExport" -BadItemLimit 5

For detailed syntax and parameter information, see Set-MailboxExportRequest.

Note: After you modify a suspended or failed mailbox export request, you need to resume it by
using the Resume-MailboxExportRequest cmdlet.

How do you know this worked?
To verify that you've successfully modified a mailbox export request, replace <MailboxIdentity>
and <MailboxExportRequestName> with the appropriate values, and run this command in the
Exchange Management Shell to verify the details:

  PowerShell

  Get-MailboxExportRequestStatistics -Identity "<MailboxIdentity>\
  <MailboxExportRequestName>" | Format-List

Use theExchange Management Shell to suspend
mailbox export requests

<!-- p.1287 -->

You can suspend mailbox export requests that are in progress. You can't suspend completed or
failed mailbox export requests.

To suspend a mailbox export request, use this syntax:

  PowerShell

  Suspend-MailboxExportRequest -Identity <MailboxIdentity>\
  <MailboxExportRequestName> [-SuspendComment "<Descriptive Comment>"]

This example suspends the mailbox export request from Kathleen Reiter's mailbox that's
named Kathleen Reiter Export.

  PowerShell

  Suspend-MailboxExportRequest -Identity "kreiter@contoso.com\Kathleen Reiter
  Export"

This example suspends all in-progress mailbox export requests with the comment "OK to
resume after 10 P.M. on Monday 6/19"

  PowerShell

  Get-MailboxExportRequest -Status InProgress | Suspend-MailboxExportRequest -
  SuspendComment "OK to resume after 10 P.M. on Monday 6/19"

For detailed syntax and parameter information, see Suspend-MailboxExportRequest.

Notes:

     You can also use the New-MailboxExportRequest cmdlet with the Suspend switch to
     create a suspended mailbox export request.

     You use the Resume-MailboxExportRequest parameter to resume suspended mailbox
     export requests.

How do you know this worked?
To verify that you've successfully suspended a mailbox export request, do any of these steps:

     Replace <MailboxIdentity> with the name, email address, or alias of the source mailbox,
     run this command in the Exchange Management Shell, and verify that the Status property
     has the value Suspended :

<!-- p.1288 -->

        PowerShell

        Get-MailboxExportRequest -Mailbox "<MailboxIdentity>" | Format-List
        Name,FilePath,Mailbox,Status

     Run this command in the Exchange Management Shell, and verify that the suspended
     mailbox export request is listed:

        PowerShell

        Get-MailboxExportRequest -Status Suspended

Use the Exchange Management Shell to resume
mailbox export requests
You can resume suspended or failed mailbox export requests.

To resume a mailbox export request, use this syntax:

  PowerShell

  Resume-MailboxExportRequest -Identity <MailboxIdentity>\<MailboxExportRequestName>

This example resumes the failed mailbox export request for Valeria Barrios' mailbox.

  PowerShell

  Resume-MailboxExportRequest -Identity vbarrios\MailboxExport

This example resumes all suspended mailbox export requests.

  PowerShell

  Get-MailboxExportRequest -Status Suspended | Resume-MailboxExportRequest

For detailed syntax and parameter information, see Resume-MailboxExportRequest.

How do you know this worked?
To verify that you've successfully resumed a mailbox export request, replace <MailboxIdentity>
with the name, email address, or alias of the source mailbox, run this command in the

<!-- p.1289 -->

Exchange Management Shell, and verify that the Status property doesn't have the value
Suspended :

  PowerShell

  Get-MailboxExportRequest -Mailbox <MailboxIdentity> | Format-List
  Name,FilePath,Mailbox,Status

Use the Exchange Management Shell to remove
mailbox export requests
You can remove fully or partially completed mailbox export requests.

     If you remove a partially completed mailbox export request, the request is removed from
     the MRS job queue. Any content that's already been exported from the source mailbox
     isn't removed from the target .pst file.

     By default, completed mailbox export request are removed after 30 days (you can
     override this value with the CompletedRequestAgeLimit parameter), and failed requests
     aren't automatically removed. But, if you use the RequestExpiryInterval parameter when
     you create or modify a mailbox export request, these results are available:

        RequestExpiryInterval with a timespan value: Completed and failed requests are
        automatically removed after the specified timespan.

        RequestExpiryInterval with the value unlimited: Completed and failed requests aren't
        automatically removed.

This example removes the mailbox export request named MailboxExport for Akia Al-Zuhairi's
mailbox.

  PowerShell

  Remove-MailboxExportRequest -Identity "aal-zuhairi\MailboxExport"

This example removes all completed mailbox export requests.

  PowerShell

  Get-MailboxExportRequest -Status Completed | Remove-MailboxExportRequest

For detailed syntax and parameter information, see Remove-MailboxExportRequest.

<!-- p.1290 -->

How do you know this worked?
To verify that you've successfully removed a mailbox export request, replace <MailboxIdentity>
with the name, email address, or alias of the source mailbox, run this command in the
Exchange Management Shell, and verify that the mailbox export request isn't listed:

  PowerShell

  Get-MailboxExportRequest -Mailbox <MailboxIdentity> | Format-List
  Name,FilePath,Mailbox,Status

<!-- p.1291 -->

Clients and mobile in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016        2019     Subscription Edition

There are many different clients that you can use to access information in an Exchange
mailbox. These clients include desktop programs such as Outlook, Outlook on the web
(formerly known as Outlook Web App), and mobile clients such as mobile phones, tablets, and
other mobile devices. Each of these clients offers a variety of features.

The following table contains links to topics that will help you learn about and manage some of
the clients and client access methods that you can use to access your Exchange mailbox.

                                                                                          ﾉ   Expand table

 Topic                          Description

 MAPI over HTTP in              Learn about the latest client access method that provides connectivity to
 Exchange Server                Outlook.

 Outlook Anywhere               Learn about the earlier client access method that provides connectivity to
                                Outlook. (This feature was formerly known as RPC/HTTP.)

 Exchange ActiveSync            Learn about the protocol that provides connectivity to a wide variety of
                                mobile phones and tablets. Using Exchange ActiveSync, users can access
                                email, calendar, contact, and task information.

 POP3 and IMAP4 in              Learn about how users can access their Exchange mailbox by using email
 Exchange Server                programs that use POP3 or IMAP4.

 Outlook for iOS and            Learn about the Outlook for iOS and Android app and how it allows your
 Android                        users to securely access their mailbox data remotely with their iOS and
                                Android devices.

 Install Office Online Server   Learn about how the integration of Office Online Server helps provide rich
 in an Exchange                 attachment preview functionality in Outlook on the web.
 organization

 Outlook on the web in          Learn about Outlook on the web, which provides users access to their
 Exchange Server                Exchange mailbox through a web browser.

 MailTips in Exchange           Learn about MailTips, the informative messages displayed to users while
                                they're composing a message.

<!-- p.1292 -->

MAPI over HTTP in Exchange Server
Article • 05/09/2025

APPLIES TO:        2016     2019      Subscription Edition

Messaging Application Programming Interface (MAPI) over HTTP is a transport protocol that
improves the reliability and stability of the Outlook and Exchange connections by moving the
transport layer to the industry-standard HTTP model. This allows a higher level of visibility of
transport errors and enhanced recoverability. Additional functionality includes support for an
explicit pause-and-resume function. This enables supported clients to change networks or
resume from hibernation while maintaining the same server context.

Implementing MAPI over HTTP does not mean that it is the only protocol that can be used for
Outlook to access Exchange. Outlook clients that are not MAPI over HTTP capable can still use
Outlook Anywhere (RPC over HTTP) to access Exchange through a MAPI-enabled Client Access
server.

In Exchange 2016 and Exchange 2019, MAPI over HTTP can be applied across your entire
organization, or at the individual mailbox level.

Benefits of MAPI over HTTP
MAPI over HTTP offers the following benefits to the clients that support it:

      Enables future innovation in authentication by using an HTTP based protocol.

      Provides faster reconnection times after a communications break because only TCP
      connections (not RPC connections) need to be rebuilt. Examples of a communication
      break include:

          Device hibernation

          Changing from a wired network to a wireless or cellular network

      Offers a session context that is not dependent on the connection. The server maintains
      the session context for a configurable period of time, even if the user changes networks.

MAPI over HTTP when upgrading Exchange
In Exchange 2016 or later, MAPI over HTTP is enabled by default at the organization level,
although you still need to configure the virtual directories as described in Configure MAPI over
HTTP for users to take advantage of it.

<!-- p.1293 -->

The scenarios where MAPI over HTTP is enabled or disabled by default at the organization level
are described in the following table:

                                                                                ﾉ   Expand table

 Scenario                                      Exchange 2019            Exchange 2016

 Upgrading from an Exchange 2016               MAPI over HTTP is        n/a
 environment                                   enabled by default

 Upgrading from an environment that contains   MAPI over HTTP is        MAPI over HTTP is
 any Exchange 2013 servers                     disabled by default      disabled by default

 Upgrading from an Exchange 2010               n/a                      MAPI over HTTP is
 environment                                                            enabled by default

During the upgrade from an organization that contains Exchange 2013 servers, administrators
will receive the MAPI over HTTP isn't enabled [WarnMapiHttpNotEnabled] readiness check
warning, and enabling MAPI over HTTP post-installation is recommended. In any organization
that contains Exchange 2013 servers, MAPI over HTTP won't be enabled by default, and
administrators will need to follow the steps in Configure MAPI over HTTP to enable it.

Supportability and Prerequisites
Consider the following requirements to enable MAPI over HTTP.

Supportability
Use the following matrix to verify that your clients and servers support MAPI over HTTP.

                                                                                ﾉ   Expand table

 Product                  Exchange      Exchange      Exchange       Exchange       Exchange
                          2019          2016          2013 SP1       2013 RTM       2010 SP3

 Outlook 2013 SP1 and     MAPI over     MAPI over     MAPI over      Outlook        RPC
 all later versions of    HTTP          HTTP          HTTP           Anywhere       Outlook
 Outlook                  Outlook       Outlook       Outlook                       Anywhere
                          Anywhere      Anywhere      Anywhere

 Outlook 2010 SP2 with    MAPI over     MAPI over     MAPI over      Outlook        RPC
 updates                  HTTP          HTTP          HTTP           Anywhere       Outlook
 KB2956191 and            Outlook       Outlook       Outlook                       Anywhere
 KB2965295 (April 14,     Anywhere      Anywhere      Anywhere
 2015)

<!-- p.1294 -->

 Product                   Exchange     Exchange      Exchange       Exchange    Exchange
                           2019         2016          2013 SP1       2013 RTM    2010 SP3

 Outlook 2013 RTM          Outlook      Outlook       Outlook        Outlook     RPC
                           Anywhere     Anywhere      Anywhere       Anywhere    Outlook
                                                                                 Anywhere

 All earlier versions of   Outlook      Outlook       Outlook        Outlook     RPC
 Outlook                   Anywhere     Anywhere      Anywhere       Anywhere    Outlook
                                                                                 Anywhere

Prerequisites
The following conditions are required for clients and servers to support MAPI over HTTP with
Exchange Server. Once the following prerequisites are in place, see Configure MAPI over HTTP
to enable it in your organization.

      Supported Outlook clients (see the table in the previous section).

      .NET Framework 4.5.2 or later.

<!-- p.1295 -->

Configure MAPI over HTTP in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016    2019         Subscription Edition

In Exchange 2016 and Exchange 2019, you can configure MAPI over HTTP at the organization
level or at the individual mailbox level. Mailbox-level settings always take precedence over
organization-wide settings.

The scenarios where MAPI over HTTP is enabled or disabled by default at the organization level
are described in the following table:

                                                                                 ﾉ   Expand table

 Scenario                                        Exchange 2019           Exchange 2016

 Upgrading from an Exchange 2016                 MAPI over HTTP is       n/a
 environment                                     enabled by default

 Upgrading from an environment that contains     MAPI over HTTP is       MAPI over HTTP is
 any Exchange 2013 servers                       disabled by default     disabled by default

 Upgrading from an Exchange 2010                 n/a                     MAPI over HTTP is
 environment                                                             enabled by default

  ７ Note

  When MAPI over HTTP is enabled at the organization level, the MapiHttpEnabled property
  value that's returned by the Get-OrganizationConfig cmdlet is True .

This topic describes how to configure and then enable MAPI over HTTP for Exchange
organizations that contain Exchange 2013 servers, or for any topology where MAPI over HTTP
has been previously disabled. You can also use the procedures in this article to disable MAPI
over HTTP at the organization level.

This topic also describes how to enable or disable MAPI over HTTP for an individual mailbox. At
the mailbox level, you have the ability to allow or block MAPI over HTTP connections internally,
externally, or both. In all cases, when MAPI over HTTP is disabled, connections will be made
with Outlook Anywhere.

Configure MAPI over HTTP

<!-- p.1296 -->

Complete the following steps to configure MAPI over HTTP for your organization. These steps
assume you have already configured the prerequisites described in MAPI over HTTP in
Exchange Server. Once configured (steps 1-3), use step 4 to enable or disable specific
permission scenarios at the organization level, at the mailbox level, or both.

   1. Virtual directory configuration: By default, Exchange creates a virtual directory for MAPI
     over HTTP. You use the Set-MapiVirtualDirectory cmdlet to configure the virtual
     directory. You need to configure an internal URL, an external URL, or both. For more
     information see, Set-MapiVirtualDirectory.

     For example, to configure the default MAPI virtual directory on the local Exchange server
     by setting the internal URL value to https://contoso.com/mapi      , and the authentication
     method to Negotiate , run the following command:

        PowerShell

        Set-MapiVirtualDirectory -Identity "Contoso\mapi (Default Web Site)" -
        InternalUrl https://Contoso.com/mapi -IISAuthenticationMethods Negotiate

   2. Certificate configuration: The digital certificate used by your Exchange environment must
     include the same InternalURL and ExternalURL values that are defined on the MAPI virtual
     directory. For more information on Exchange certificate management, see Digital
     certificates and encryption in Exchange Server. Make sure the Exchange certificate is
     trusted on the Outlook client workstation and that there are no certificate errors,
     especially when you access the URLs configured on the MAPI virtual directory.

   3. Update server rules: Verify that your load balancers, reverse proxies, and firewalls are
     configured to allow access to the MAPI over HTTP virtual directory.

   4. Use the following steps to enable MAPI over HTTP in your entire Exchange organization,
     or enable MAPI over HTTP for one or more individual mailboxes.

        ７ Note

        After you run the commands below, Outlook clients with MAPI over HTTP enabled
        will see a message to restart Outlook to use MAPI over HTTP.

     Enable MAPI over HTTP in your Exchange organization:

     To enable or disable MAPI over HTTP at the organizational level, use the Set-
     OrganizationConfig cmdlet with the MapiHttpEnabled parameter. Valid values are:

<!-- p.1297 -->

           $true: MAPI over HTTP connections are allowed for all mailboxes in the organization
           (unless MAPI over HTTP is disabled on a specific mailbox).

           $false: MAPI over HTTP connections aren't allowed for all mailboxes in the
           organization (unless MAPI over HTTP is enabled on a specific mailbox).

     The following example enables MAPI over HTTP connections for the entire organization:

        PowerShell

        Set-OrganizationConfig -MapiHttpEnabled $true

     Enable MAPI over HTTP for an individual mailbox:

     To enable or disable MAPI over HTTP at the mailbox level, use the Set-CasMailbox cmdlet
     with the MapiHttpEnabled parameter. Valid values are:

           $null: The mailbox follows organization-level settings. This is the default value.

           $true: Enable MAPI over HTTP for the mailbox. If MAPI over HTTP is disabled at the
           organizational level, it's enabled for the mailbox.

           $false: Disable MAPI over HTTP for the mailbox. If MAPI over HTTP is enabled at the
           organizational level, it's disabled for the mailbox, so the mailbox will use Outlook
           Anywhere connections.

     The following example enables MAPI over HTTP connections for a single mailbox:

        PowerShell

        Set-CasMailbox <user or mailbox ID> -MapiHttpEnabled $true

Test MAPI over HTTP connections
You can test the end-to-end MAPI over HTTP connection by using the Test-
OutlookConnectivity cmdlet. To use the Test-OutlookConnectivity cmdlet, the Microsoft
Exchange Health Manager (MSExchangeHM) service must be started.

The following example tests the MAPI over HTTP connection from the Exchange server named
ContosoMail.

  PowerShell

  Test-OutlookConnectivity -RunFromServerId ContosoMail -ProbeIdentity

<!-- p.1298 -->

  OutlookMapiHttpSelfTestProbe

A successful test returns output that's similar to the following example:

  PowerShell

  MonitorIdentity                                                  StartTime
  EndTime                Result      Error     Exception
  ---------------                                                  ---------                --
  -----                ------      -----     ---------
  OutlookMapiHttp.Protocol\OutlookMapiHttpSelfTestProbe            2/14/2018 7:15:00 AM
  2/14/2018 7:15:10 AM   Succeeded

For more information, see Test-OutlookConnectivity.

Logs for MAPI over HTTP activity are at the following locations:

     %ExchangeInstallPath%Logging\MAPI Address Book Service\

     %ExchangeInstallPath%Logging\MAPI Client Access\

     %ExchangeInstallPath%Logging\HttpProxy\Mapi\

Combining MAPI over HTTP configurations and
internal or external connections
In addition to the organization and mailbox settings described earlier in this topic, you can use
the MapiBlockOutlookExternalConnectivity parameter on the Set-CasMailbox cmdlet to allow or
deny external Outlook Anywhere or MAPI over HTTP connections to a specific mailbox. Valid
values are:

     True: Only internal connections are allowed to the mailbox.

     False: Internal and external connections are allowed to the mailbox. This is the default
     value.

The following table summarizes the results of the different setting combinations at the
organization level and on individual mailboxes.

                                                                                ﾉ   Expand table

<!-- p.1299 -->

MapiHttpEnabled      MapiHttpEnabled   MapiBlockOutlookExternalConnectivity   AutoDiscover
value on Set-        value on Set-     value on Set-CasMailbox                result
OrganizationConfig   CasMailbox

$true                $null             $false                                 MAPI over
                                                                              HTTP, internal
                                                                              and external

$true                $null             $true                                  MAPI over
                                                                              HTTP, internal
                                                                              only

$true                $true             $false                                 MAPI over
                                                                              HTTP, internal
                                                                              and external

$true                $true             $true                                  MAPI over
                                                                              HTTP, internal
                                                                              only

$true                $false            $false                                 Outlook
                                                                              Anywhere,
                                                                              internal and
                                                                              external

$true                $false            $true                                  Outlook
                                                                              Anywhere,
                                                                              internal only

$false               $null             $false                                 Outlook
                                                                              Anywhere,
                                                                              internal and
                                                                              external

$false               $null             $true                                  Outlook
                                                                              Anywhere,
                                                                              internal only

$false               $true             $false                                 MAPI over
                                                                              HTTP, internal
                                                                              and external

$false               $true             $true                                  MAPI over
                                                                              HTTP, internal
                                                                              only

$false               $false            $false                                 Outlook
                                                                              Anywhere,
                                                                              internal and
                                                                              external

<!-- p.1300 -->

 MapiHttpEnabled      MapiHttpEnabled   MapiBlockOutlookExternalConnectivity   AutoDiscover
 value on Set-        value on Set-     value on Set-CasMailbox                result
 OrganizationConfig   CasMailbox

 $false               $false            $true                                  Outlook
                                                                               Anywhere,
                                                                               internal only

Manage MAPI over HTTP
You can manage the configuration of MAPI over HTTP by using the following cmdlets:

     Set-MapiVirtualDirectory

     Get-MapiVirtualDirectory

     New-MapiVirtualDirectory

     Remove-MapiVirtualDirectory

<!-- p.1301 -->

Enable or disable MAPI access to mailboxes
in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

MAPI is a client protocol that lets users access their mailbox by using Outlook or other MAPI
email clients. By default, MAPI access to a user mailbox is enabled. Disabling MAPI access to a
mailbox prevents the user from using Outlook to access their mailbox in Exchange mode. It
doesn't prevent the user from using Outlook on the web or Outlook using other protocols (for
example, POP3, IMAP4, or Exchange ActiveSync) to access their mailbox.

Administrators can use the Exchange admin center (EAC) or the Exchange Management Shell
to enable or disable MAPI access to user mailbox.

For additional management tasks related to user access to mailboxes, see these topics:

      Enable or disable Outlook on the web access to mailboxes in Exchange Server

      Enable or disable Exchange ActiveSync access to mailboxes in Exchange Server

      Enable or disable POP3 or IMAP4 access to mailboxes in Exchange Server

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.

      For more information about accessing and using the EAC, see Exchange admin center in
      Exchange Server.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Client Access user settings" entry
      in the Clients and mobile devices permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

<!-- p.1302 -->

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online, or Exchange Online Protection .

Enable or disable MAPI access to a single mailbox

Use the EAC to Enable or disable MAPI access to a single
mailbox
 1. In the EAC, go to Recipients > Mailboxes.

 2. In the list of mailboxes, find the mailbox that you want to modify. You can:

         Scroll through the list of mailboxes.

         Click Search    and enter part of the user's name, email address, or alias.

         Click More options     > Advanced search to find the mailbox.

         Once you've found the mailbox that you want to modify, select it, and then click Edit
           .

 3. On the mailbox properties page that opens, click Mailbox features.

 4. In the Email Connectivity section, configure one of these settings:

         If you see MAPI: Enabled, click Disable to disable it, and then click Yes in the
         warning message that appears.

         If you see MAPI: Disabled, click Enable to enable it.

<!-- p.1303 -->

           When you're finished, click Save.

Use the Exchange Management Shell to enable or disable
MAPI access to a mailbox
To enable or disable MAPI access to a single mailbox, use this syntax:

  PowerShell

  Set-CasMailbox -Identity <MailboxIdentity> -MAPIEnabled <$true | $false>

This example disables MAPI access to the mailbox named Ken Sanchez.

  PowerShell

  Set-CasMailbox -Identity "Ken Sanchez" -MAPIEnabled $false

This example enables MAPI access to the mailbox named Esther Valle.

  PowerShell

  Set-CasMailbox -Identity "Esther Valle" -MAPIEnabled $true

For detailed syntax and parameter information, see Set-CASMailbox.

Enable or disable MAPI access to multiple
mailboxes

Use the EAC to enable or disable MAPI access to multiple
mailboxes
   1. In the EAC, go to Recipients > Mailboxes.

   2. In the list of mailboxes, find the mailboxes that you want to modify. You can:

           Scroll through the list of mailboxes.

           Click Search    and enter part of the user's name, email address, or alias.

           Click More options     > Advanced search to find the mailbox.

<!-- p.1304 -->

  3. In the list of mailboxes, select multiple mailboxes of the same type (for example, User)
     from the list. For example:

          Select a mailbox, hold down the Shift key, and select another mailbox that's farther
          down in the list.

          Hold down the CTRL key as you select each mailbox.

     After you select multiple mailboxes of the same type, the title of the details pane changes
     to Bulk Edit.

  4. In the details pane, scroll down to MAPI, click Enable or Disable, and then click OK in the
     warning message that appears.

Use the Exchange Management Shell to enable or disable
MAPI access to multiple mailboxes
You can use the Get-Mailbox, Get-User or Get-Content cmdlets to identify the mailboxes that
you want to modify. For example:

     Use the OrganizationalUnit parameter to filter the mailboxes by organizational unit (OU).

     Use the Filter parameter to create OPATH filters that identify the mailboxes. For more
     information, see Filterable Properties for the -Filter Parameter.

     Use a text file to specify the mailboxes. The text file contains one mailbox (email address,
     name, or other unique identifier) on each line like this:

<!-- p.1305 -->

       ebrunner@tailspintoys.com
       fapodaca@tailspintoys.com
       glaureano@tailspintoys.com
       hrim@tailspintoys.com

This example disables MAPI access to all user mailboxes in the North America\Finance OU.

  PowerShell

  $NAFinance = Get-Mailbox -OrganizationalUnit "OU=Marketing,OU=North
  America,DC=contoso,DC=com" -Filter "RecipientTypeDetails -eq 'UserMailbox'" -
  ResultSize Unlimited; $NAFinance | foreach {Set-CasMailbox $_.Identity -
  MAPIEnabled $false}

This example disables MAPI access to all user mailboxes in the Engineering department in
Washington state.

  PowerShell

  Get-User -Filter "RecipientType -eq 'UserMailbox' -and Department -like
  'Engineering*' -and StateOrProvince -eq 'WA'" | Set-CasMailbox -MAPIEnabled $false

This example uses the text file C:\My Documents\Accounts.txt to disable MAPI access to the
specified mailboxes.

  PowerShell

  Get-Content "C:\My Documents\Accounts.txt" | foreach {Set-CasMailbox $_ -
  MAPIEnabled $false}

For detailed syntax and parameter information, see Get-Mailbox and Get-User.

How do you know this worked?
To verify that you've successfully enabled or disabled MAPI access to a mailbox, do any of
these steps:

     In the EAC, go to Recipients > Mailboxes > select the mailbox > click Edit    > Mailbox
     features and verify the MAPI value in the Email Connectivity section.

<!-- p.1306 -->

In the Exchange Management Shell, replace <MailboxIdentity> with the identity of the
mailbox (for example, name, alias, or email address), and run this command:

  PowerShell

  Get-CasMailbox -Identity "<MailboxIdentity>"

Use the same filter that you used to identify the mailboxes, but use the Get-CasMailbox
cmdlet instead of Set-CasMailbox. For example:

  PowerShell

  Get-User -Filter "RecipientType -eq 'UserMailbox' -and Department -like
  'Engineering*' -and StateOrProvince -eq 'WA'" | Get-CasMailbox

In the Exchange Management Shell, run this command to show all mailboxes where
Outlook on the web access is disabled:

  PowerShell

  Get-CasMailbox -ResultSize unlimited -Filter "MAPIEnabled -eq `$false"

<!-- p.1307 -->

Exchange ActiveSync in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Exchange ActiveSync is an Exchange synchronization protocol that's optimized to work
together with high-latency and low-bandwidth networks. The protocol, based on HTTP and
XML, lets mobile phones access an organization's information on a server that's running
Microsoft Exchange.

Overview of Exchange ActiveSync
Exchange ActiveSync lets mobile phone users access their email, calendar, contacts, and tasks,
and lets them continue to access this information when they're working offline.

Standard encryption services add security to mobile communication with the server. You can
configure Exchange ActiveSync to use Secure Sockets Layer (SSL) encryption for
communications between the Exchange server and the mobile device.

  ７ Note

  Exchange ActiveSync does not support shared mailboxes or delegate access.

Features in Exchange ActiveSync
Exchange ActiveSync provides the following:

      Support for HTML messages

      Support for follow-up flags

      Conversation grouping of email messages

      Ability to synchronize or not synchronize an entire conversation

      Synchronization of Short Message Service (SMS) messages with a user's Exchange
      mailbox

      Support for viewing message reply status

      Support for fast message retrieval

      Meeting attendee information

<!-- p.1308 -->

     Enhanced Exchange Search

     PIN reset

     Enhanced device security through password policies

     Autodiscover for over-the-air provisioning

     Support for setting automatic replies when users are away, on vacation, or out of the
     office

     Support for task synchronization

     Direct Push

     Support for availability information for contacts

Managing Exchange ActiveSync
By default, Exchange ActiveSync is enabled. All users who have an Exchange mailbox can
synchronize their mobile device with the Microsoft Exchange server.

You can perform the following Exchange ActiveSync tasks:

     Enable and disable Exchange ActiveSync for users

     Set policies such as minimum password length, device locking, and maximum failed
     password attempts

     Initiate a remote wipe to clear all data from a lost or stolen mobile phone

     Run a variety of reports for viewing or exporting into a variety of formats

     Control which types of mobile devices can synchronize with your organization through
     device access rules

Managing mobile device access in Exchange ActiveSync
You can control which mobile devices can synchronize with Exchange Server. You do this by
monitoring new mobile devices as they connect to your organization or by setting up rules that
determine which types of mobile devices are allowed to connect. Regardless of the method
you choose to specify which mobile devices can synchronize, you can approve or deny access
for any specific mobile device for a specific user at any time.

Device security features in Exchange ActiveSync

<!-- p.1309 -->

In addition to the ability to configure security options for communications between the
Exchange server and your mobile devices, Exchange ActiveSync offers the following features to
enhance the security of mobile devices:

     Remote wipe: If a mobile device is lost, stolen, or otherwise compromised, you can issue
     a remote wipe command from the Exchange Server computer or from any Web browser
     by using Outlook Web App. This command erases all data from the mobile device.

     Device password policies: Exchange ActiveSync lets you configure several options for
     device passwords. The device password options include the following:

        Minimum password length (characters): This option specifies the length of the
        password for the mobile device. The default length is 4 characters, but as many as 18
        can be included.

        Minimum number of character sets: Use this text box to specify the complexity of the
        alphanumeric password and force users to use a number of different sets of characters
        from among the following: lowercase letters, uppercase letters, symbols, and numbers.

        Require alphanumeric password: This option determines password strength. You can
        enforce the usage of a character or symbol in the password in addition to numbers.

        Inactivity time (seconds): This option determines how long the mobile device must be
        inactive before the user is prompted for a password to unlock the mobile device.

        Enforce password history: Select this check box to force the mobile phone to prevent
        the user from reusing their previous passwords. The number that you set determines
        the number of past passwords that the user won't be allowed to reuse.

        Enable password recovery: Select this check box to enable password recovery for the
        mobile device. Administrators can use the Get-ActiveSyncDeviceStatistics cmdlet to
        look up the user's recovery password.

        Wipe device after failed (attempts): This option lets you specify whether you want the
        phone's memory to be wiped after multiple failed password attempts.

     Device encryption policies: There are a number of mobile device encryption policies that
     you can enforce for a group of users. These policies include the following:

        Require encryption on device: Select this check box to require encryption on the
        mobile device. This increases security by encrypting all information on the mobile
        device.

        Require encryption on storage cards: Select this check box to require encryption on
        the mobile device's removable storage card. This increases security by encrypting all

<!-- p.1310 -->

information on the storage cards for the mobile device.

<!-- p.1311 -->

Enable or disable Exchange ActiveSync
access to mailboxes in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

ActiveSync is a client protocol that lets users synchronize their Exchange mailbox with a mobile
device. By default, ActiveSync is enabled on new user mailboxes. Disabling ActiveSync on a
mailbox prevents the user from synchronizing their mailbox with a mobile device (by using
ActiveSync).

Administrators can use the Exchange admin center (EAC) or the Exchange Management Shell
to enable or disable Exchange ActiveSync access to a mailbox.

For more information about ActiveSync, see Exchange ActiveSync.

For information about setting up email on your mobile device, see these topics:

      Set up Office apps and email on iOS devices

      Set up Office apps and email on Android

For additional management tasks related to user access to mailboxes, see these topics:

      Enable or disable Outlook on the web access to mailboxes in Exchange Server

      Enable or disable POP3 or IMAP4 access to mailboxes in Exchange Server

      Enable or disable MAPI access to mailboxes in Exchange Server

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.

      For more information about accessing and using the EAC, see Exchange admin center in
      Exchange Server.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Exchange ActiveSync settings"
      entry in the Clients and mobile devices permissions topic.

<!-- p.1312 -->

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online, or Exchange Online Protection .

Enable or disable Exchange ActiveSync access to a
single mailbox

Use the EAC to enable or disable Exchange ActiveSync access
to a mailbox
 1. In the EAC, go to Recipients > Mailboxes.

 2. In the list of mailboxes, find the mailbox that you want to modify. You can:

         Scroll through the list of mailboxes.

         Click Search    and enter part of the user's name, email address, or alias.

         Click More options      > Advanced search to find the mailbox.

         Once you've found the mailbox that you want to modify, select it, and then click Edit
           .

 3. On the mailbox properties page that opens, click Mailbox features.

 4. In the Mobile Devices section, configure one of these settings:

         If ActiveSync is enabled on the mailbox, you'll see a Disable Exchange ActiveSync
         link. Click the link to disable ActiveSync, and then click Yes in the warning message
         that appears.

         If ActiveSync is disabled on the mailbox, you'll see a Enable Exchange ActiveSync
         link. Click the link to enable ActiveSync.

<!-- p.1313 -->

           When you're finished, click Save.

Use the Exchange Management Shell to enable or disable
Exchange ActiveSync access to a mailbox
To enable or disable ActiveSync access to a single mailbox, use this syntax:

  PowerShell

  Set-CasMailbox -Identity <MailboxIdentity> -ActiveSyncEnabled <$true | $false>

This example disables ActiveSync access to the mailbox named Yan Li.

  PowerShell

  Set-CasMailbox -Identity "Yan Li" -ActiveSyncEnabled $false

This example enables ActiveSync access to the mailbox named Elly Nkya.

  PowerShell

  Set-CasMailbox -Identity "Elly Nkya" -ActiveSyncEnabled $true

For detailed syntax and parameter information, see Set-CASMailbox.

<!-- p.1314 -->

Enable or disable Exchange ActiveSync access to
multiple mailboxes

Use the EAC to enable or disable Exchange ActiveSync access
to multiple mailboxes
  1. In the EAC, go to Recipients > Mailboxes.

  2. In the list of mailboxes, find the mailboxes that you want to modify. You can:

          Scroll through the list of mailboxes.

          Click Search     and enter part of the user's name, email address, or alias.

          Click More options       > Advanced search to find the mailbox.

  3. In the list of mailboxes, select multiple mailboxes of the same type (for example, User)
     from the list. For example:

          Select a mailbox, hold down the Shift key, and select another mailbox that's farther
          down in the list.

          Hold down the CTRL key as you select each mailbox.

     After you select multiple mailboxes of the same type, the title of the details pane changes
     to Bulk Edit.

  4. In the details pane, scroll down to Exchange ActiveSync, click Enable or Disable, and then
     click OK in the warning message that appears.

     Bulk select mailboxes in the EAC to enable or disable Exchange ActiveSync

Use the Exchange Management Shell to enable or disable
Exchange ActiveSync access to multiple mailboxes
You can use the Get-Mailbox, Get-User or Get-Content cmdlets to identify the mailboxes that
you want to modify. For example:

     Use the OrganizationalUnit parameter to filter the mailboxes by organizational unit (OU).

     Use the Filter parameter to create OPATH filters that identify the mailboxes. For more
     information, see Filterable Properties for the -Filter Parameter.

<!-- p.1315 -->

      Use a text file to specify the mailboxes. The text file contains one mailbox (email address,
      name, or other unique identifier) on each line like this:

        ebrunner@tailspintoys.com
        fapodaca@tailspintoys.com
        glaureano@tailspintoys.com
        hrim@tailspintoys.com

This example disables ActiveSync access to all user mailboxes in the North America\Finance
OU.

  PowerShell

  $NAFinance = Get-Mailbox -OrganizationalUnit "OU=Marketing,OU=North
  America,DC=contoso,DC=com" -Filter "RecipientTypeDetails -eq 'UserMailbox'" -
  ResultSize Unlimited; $NAFinance | foreach {Set-CasMailbox $_.Identity -
  ActiveSyncEnabled $false}

This example disables ActiveSync access to all user mailboxes in the Engineering department in
Washington state.

  PowerShell

  Get-User -Filter "RecipientType -eq 'UserMailbox' -and Department -like
  'Engineering*' -and StateOrProvince -eq 'WA'" | Set-CasMailbox -ActiveSyncEnabled
  $false

This example uses the text file C:\My Documents\Accounts.txt to disable ActiveSync access to
the specified mailboxes.

  PowerShell

  Get-Content "C:\My Documents\Accounts.txt" | foreach {Set-CasMailbox $_ -
  ActiveSyncEnabled $false}

For detailed syntax and parameter information, see Get-Mailbox and Get-User.

How do you know this worked?
To verify that you've successfully enabled or disabled Exchange ActiveSync access to a mailbox,
do any of these steps:

      In the EAC, go to Recipients > Mailboxes > select the mailbox > click Edit      > Mailbox
      features > and verify the Exchange ActiveSync value in the Mobile Devices section.

<!-- p.1316 -->

  If ActiveSync access is enabled for the mailbox, you'll see Disable Exchange
  ActiveSync.

  If ActiveSync access is disabled for the mailbox, you'll see Enable Exchange ActiveSync.

In the Exchange Management Shell, replace <MailboxIdentity> with the identity of the
mailbox (for example, name, alias, or email address), and run this command:

  PowerShell

  Get-CasMailbox -Identity "<MailboxIdentity>"

Use the same filter that you used to identify the mailboxes, but use the Get-CasMailbox
cmdlet instead of Set-CasMailbox. For example:

  PowerShell

  Get-User -Filter "RecipientType -eq 'UserMailbox' -and Department -like
  'Engineering*' -and StateOrProvince -eq 'WA'" | Get-CasMailbox

In the Exchange Management Shell, run this command to show all mailboxes where
ActiveSync access is disabled:

  PowerShell

<!-- p.1317 -->

Get-CasMailbox -ResultSize unlimited -Filter "ActiveSyncEnabled -eq `$false"

<!-- p.1318 -->

Mobile device mailbox policies in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

In Exchange Server, you can create mobile device mailbox policies to apply a common set of
policies or security settings to a collection of users. After you deploy Exchange ActiveSync in
your Exchange Server organization, you can create new mobile device mailbox policies or
modify existing policies. When you install Exchange Server, a default mobile device mailbox
policy is created. All users are automatically assigned this default mobile device mailbox policy.

Overview of mobile device mailbox policies
You can use mobile device mailbox policies to manage many different settings. These include
the following:

      Require a password
      Specify the minimum password length
      Require a number or special character in the password
      Designate how long a device can be inactive before requiring the user to re-enter a
      password
      Wipe a device after a specific number of failed password attempts

For more information about all the settings you can configure, see Mobile device policy
settings.

Exchange mobile device mailbox policies
Exchange ActiveSync is a client protocol that lets you synchronize a mobile device with your
Exchange mailbox. Exchange ActiveSync is enabled by default when you install Exchange
Server.

You can create mobile device mailbox policies in the Exchange admin center (EAC) or the
Exchange Management Shell. If you create a policy in the EAC, you can configure only a subset
of the available settings. You can configure the rest of the settings using the Exchange
Management Shell.

Mobile device password settings and biometrics

<!-- p.1319 -->

Many mobile devices support biometrics such as Apple Touch ID or Face ID. Exchange mobile
device mailbox policies do not control whether biometrics can be used instead of typing the
device PIN. Mobile device mailbox policies can be configured to require a device PIN, but then
the users control whether they use biometrics after complying with the device PIN
requirement.

Mobile device password settings and Android
Android 9.0 and earlier versions utilize Android's device admin functionality to manage device
password settings defined in a mobile device mailbox policy.

With Android 10.0 and later, Android has removed device admin functionality. Instead, apps
that require a screen lock query the device's (or the work profile's) screen lock complexity.
Apps that require a stronger screen lock direct the user to the system screen lock settings,
allowing the user to update the security settings to become compliant. At no time is the app
aware of the user's password; the app is only aware of the password complexity level. Android
supports the following four password complexity levels:

                                                                                     ﾉ    Expand table

 Password              Password requirements
 complexity level

 None                  No password requirements are configured

 Low                   Password can be a pattern or a PIN with either repeating (4444) or ordered
                       (1234, 4321, 2468) sequences

 Medium                Passwords that meet one of the following criteria:
                            PIN with no repeating (4444) or ordered (1234, 4321, 2468) sequences with
                             a minimum length of 4 characters
                             Alphabetic passwords with a minimum length of 4 characters
                             Alphanumeric passwords with a minimum length of 4 characters

 High                  Passwords that meet one of the following criteria:
                             PIN with no repeating (4444) or ordered (1234, 4321, 2468) sequences with
                             a minimum length of 8 characters
                             Alphabetic passwords with a minimum length of 6 characters
                             Alphanumeric passwords with a minimum length of 6 characters

From the perspective of an Exchange mobile device mailbox policy, Android's password
complexity levels are mapped to the following policy settings:

<!-- p.1320 -->

                                                                                          ﾉ   Expand table

 Mobile device mailbox policy setting                    Android password complexity level

 Password enabled = false                                None

 Allow simple password = true                            Low
 Min password length < 4

 Allow simple password = true                            Medium
 Min password length < 6

 Allow simple password = false                           Medium
 Alphanumeric password required = true
 Min password length < 6

 Allow simple password = true                            High
 Min password length > 6

 Allow simple password = false                           High
 Alphanumeric password required = true
 Min password length >= 6

Mobile device mailbox policy settings
The following table summarizes the settings you can specify using mobile device mailbox
policies.

                                                                                          ﾉ   Expand table

 Setting                Description

 Allow Bluetooth        This setting specifies whether a mobile device allows Bluetooth connections. The
                        available options are Disable, HandsFree Only, and Allow. The default value is
                        Allow.

 Allow Browser          This setting specifies whether Pocket Internet Explorer is allowed on the mobile
                        device. This setting doesn't affect third-party browsers installed on the mobile
                        device. The default value is $true .

 Allow Camera           This setting specifies whether the mobile device camera can be used. The default
                        value is $true .

 Allow Consumer         This setting specifies whether the mobile device user can configure a personal
 EMail                  email account (either POP3 or IMAP4) on the mobile device. The default value is
                        $true . This setting doesn't control access to email accounts that are using third-
                        party mobile device email programs.
