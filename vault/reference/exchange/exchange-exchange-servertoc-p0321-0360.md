---
title: "Exchange Server — pages 321-360"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0321-0360
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0321-0360
family: exchange
documentKind: "doc"
abstract: "This example imports the chain of certificates file \\\\FileServer01\\Data\\Chain of Certificates.p7b . PowerShell Import-ExchangeCertificate -FileData ([System.IO.File]::ReadAllBytes('\\\\FileServer01\\Data\\Chain of Certificates.p7b')) For detailed syntax and parameter information, se"
---

# Exchange Server — pages 321-360

<!-- p.321 -->

This example imports the chain of certificates file \\FileServer01\Data\Chain of
Certificates.p7b .

  PowerShell

  Import-ExchangeCertificate -FileData
  ([System.IO.File]::ReadAllBytes('\\FileServer01\Data\Chain of Certificates.p7b'))

For detailed syntax and parameter information, see Import-ExchangeCertificate.

  ７ Note

        You need to repeat this procedure on each Exchange server where you want to
        import the certificate (run the command on the server, or use the Server parameter).
        The FileData parameter accepts local paths if the certificate file is located on the
        Exchange server where you're running the command, and this is the same server
        where you want to import the certificate. Otherwise, use a UNC path.
        If you want to be able to export the certificate from the server where you're
        importing it, you need to use the PrivateKeyExportable parameter with the value
        $true .

How do you know this worked?
To verify that you have successfully imported (installed) a certificate on an Exchange server, use
either of the following procedures:

     In the EAC at Servers > Certificates, verify the server where you installed the certificate is
     selected. The certificate should be in the list of certificates with the Status value Valid.

     In the Exchange Management Shell on the server where you installed the certificate, run
     the following command:

        PowerShell

        Get-ExchangeCertificate | where {$_.Status -eq "Valid"} | Format-List
        FriendlyName,Subject,CertificateDomains,Thumbprint,NotBefore,NotAfter

Next steps

<!-- p.322 -->

After you install the certificate on the server, you need to assign the certificate to one or more
Exchange services before the Exchange server is able to use the certificate for encryption. For
more information, see Assign certificates to Exchange Server services.

<!-- p.323 -->

Configure client-specific message size limits in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

In Exchange Server, there are several different message size limits that apply to messages as they travel
through your organization. For more information, see Message size and recipient limits in Exchange
Server.

However, there are client-specific message size limits you can configure for Outlook on the web (formerly
known as Outlook Web App) and email clients that use Exchange ActiveSync or Exchange Web Services
(EWS). If you change the Exchange organizational, connector, or user message size limits, you likely need
to change the limits for Outlook on the web, ActiveSync, and EWS. These limits are described in the
following tables. To change the message size limit for a specific client type, you need to change all the
values that are described in the table.

  ７ Note

  For any message size limit, you need to set a value that's larger than the actual size you want
  enforced. This accounts for the Base64 encoding of attachments and other binary data. Base64
  encoding increases the size of the message by approximately 33%, so the value you specify should be
  approximately 33% larger than the actual message size you want enforced. For example, if you
  specify a maximum message size value of 64 MB, you can expect a realistic maximum message size of
  approximately 48 MB.

ActiveSync
                                                                                                   ﾉ   Expand table

 Services     Configuration file                                        Keys and default values               Size

 Client       %ExchangeInstallPath%FrontEnd\HttpProxy\Sync\web.config   maxAllowedContentLength="30000000"    bytes
 Access                                                                 (not present by default; see
 (frontend)                                                             comments)

 Client       %ExchangeInstallPath%FrontEnd\HttpProxy\Sync\web.config   maxRequestLength="10240"              kilobytes
 Access
 (frontend)

 Backend      %ExchangeInstallPath%ClientAccess\Sync\web.config         maxAllowedContentLength="30000000     bytes
                                                                        bytes" (not present by default; see
                                                                        comments)

 Backend      %ExchangeInstallPath%ClientAccess\Sync\web.config         maxRequestLength="10240"              kilobytes

 Backend      %ExchangeInstallPath%ClientAccess\Sync\web.config         <add key="MaxDocumentDataSize"        bytes

<!-- p.324 -->

 Services      Configuration file                                       Keys and default values               Size

                                                                        value="10240000">

Comments on ActiveSync limits
By default, there is no maxAllowedContentLength key in the web.config files for ActiveSync. However, the
maximum message size for ActiveSync is affected by the maxAllowedContentLength value that is applied
to all web sites on the server. The default value is 30000000 bytes. To see these values for ActiveSync on
Mailbox servers in IIS Manager, perform the following steps:

   1. Do one of the following steps:

              For the Client Access (frontend) web site, open IIS Manager, navigate to Sites > Default Web
              Site and select Microsoft-Server-ActiveSync.

              For the backend web site, open IIS Manager, navigate to Sites > Exchange Back End and select
              Microsoft-Server-ActiveSync.

   2. Verify the Features View tab is selected at the bottom, and double-click Configuration Editor in the
     Management section.

   3. Click the drop down arrow in the Section field, navigate to system.webServer > security and select
     requestFiltering.

   4. In the results, expand requestLimits, and you'll see maxAllowedContentLength and the default value
     30000000 (bytes).

To change the maxAllowedContentLength value, enter a new value in bytes, and click Apply. You need to
change the value on the Client Access web site and the back end web site.

Note: You can change the same setting in IIS manager at Sites > Default Web Site > Microsoft-Server-
ActiveSync or Sites > Exchange Back End > Microsoft-Server-ActiveSync and then Request Filtering in
the IIS section > Edit Feature Settings in the Actions area > Maximum allowed content length (Bytes) in
the Request Limits section.

After you change the value in IIS Manager, a new maxAllowedContentLength key is written to the
corresponding Client Access or backend web.config file that's described in the table.

Exchange Web Services
                                                                                                  ﾉ   Expand table

 Service       Configuration file                                       Keys and default values                Size

 Client        %ExchangeInstallPath%FrontEnd\HttpProxy\ews\web.config    maxAllowedContentLength="67108864"    bytes
 Access
 (frontend)

<!-- p.325 -->

Service      Configuration file                                           Keys and default values                  Size

Backend      %ExchangeInstallPath%ClientAccess\exchweb\ews\web.config     maxAllowedContentLength="67108864"       bytes

Backend      %ExchangeInstallPath%ClientAccess\exchweb\ews\web.config     14 instances of                          bytes
                                                                          maxReceivedMessageSize="67108864"
                                                                          (for different combinations of
                                                                          http/https bindings and
                                                                          authentication methods)

Comments on EWS limits
    In the backend web.config file, there are two instances of the value
     maxReceivedMessageSize="1048576" for UMLegacyMessageEncoderSoap11Element bindings that you

    don't need to modify.

    maxRequestLength is an ASP.NET setting that's present in both web.config files, but isn't used by
    EWS, so you don't need to modify it.

Outlook on the web
                                                                                                    ﾉ      Expand table

Service      Configuration file                                         Keys and default values                  Size

Client       %ExchangeInstallPath%FrontEnd\HttpProxy\owa\web.config     maxAllowedContentLength="35000000"       bytes
Access
(frontend)

Client       %ExchangeInstallPath%FrontEnd\HttpProxy\owa\web.config     maxRequestLength="35000"                 kilobytes
Access
(frontend)

Backend      %ExchangeInstallPath%ClientAccess\Owa\web.config           maxAllowedContentLength="35000000"       bytes

Backend      %ExchangeInstallPath%ClientAccess\Owa\web.config           maxRequestLength="35000"                 kilobytes

Backend      %ExchangeInstallPath%ClientAccess\Owa\web.config           2 instances of                           bytes
                                                                        maxReceivedMessageSize="35000000"
                                                                        (for http and https bindings)

Backend      %ExchangeInstallPath%ClientAccess\Owa\web.config           2 instances of                           bytes
                                                                        maxStringContentLength="35000000"
                                                                        (for http and https bindings)

Comments on Outlook on the web limits
    In the backend web.config file, there's an instance of the value maxStringContentLength="102400" for
    the MsOnlineShellService binding that you don't need to modify.

<!-- p.326 -->

What do you need to know before you begin?
   Estimated time to complete: 15 minutes

   Exchange permissions don't apply to the procedures in this topic. These procedures are performed in
   the operating system of the Exchange server.

   Changes you save to the web.config configuration file are applied after you restart IIS.

   To allow for the 33% increase in size due to Base64 encoding, multiply your desired new maximum
   size value in megabytes by 4/3. To convert the value into kilobytes, multiply by 1024. To convert the
   value into bytes, multiply by 1048756 (1024*1024). Note that the size increase caused by Base64
   encoding could be greater than 33%, and depends on several factors (for example, the attachment
   size, file type, compression, and the email client).

   Any customized Exchange or Internet Information Server (IIS) settings that you made in Exchange
   XML application configuration files on the Exchange server (for example, web.config files or the
   EdgeTransport.exe.config file) will be overwritten when you install an Exchange CU. Be sure save this
   information so you can easily re-apply the settings after the install. After you install the Exchange CU,
   you need to re-configure these settings.

   For information about keyboard shortcuts that may apply to the procedures in this topic, see
   Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange Server        .

Use Notepad to configure a client-specific message
size limit
 1. Open the appropriate web.config files in Notepad. For example, to open the web.config files for EWS
   clients, run the following commands:

      Console

      Notepad %ExchangeInstallPath%ClientAccess\exchweb\ews\web.config

      Console

      Notepad %ExchangeInstallPath%FrontEnd\HttpProxy\ews\web.config

 2. Find the relevant keys in the appropriate web.config files as described in the tables earlier in the
   topic. For example, for EWS clients, find the maxAllowedContentLength key in the Client Access and
   backend web.config files and all 14 instances of the value maxReceivedMessageSize="67108864" in the
   backend web.config file.

<!-- p.327 -->

     <requestLimits maxAllowedContentLength="67108864" />
     ...maxReceivedMessageSize="67108864"...

  For example, to allow a Base64 encoded maximum message size of approximately 64 MB, change all
  instances of 67108864 to 89478486 (64*4/3*1048756):

     <requestLimits maxAllowedContentLength="89478486" />
     ...maxReceivedMessageSize="89478486"...

3. When you're finished, save and close the web.config files.

4. Restart IIS on the Exchange server by using either of the following methods:

       Open IIS Manager, select the server, and in the Actions pane, click Restart.

       Run the following commands from an elevated command prompt (a Command Prompt window
       you open by selecting Run as administrator):

          Console

          net stop w3svc /y

          Console

          net start w3svc

<!-- p.328 -->

Configure client-specific message size limits from the
command line
Instead of using Notepad, you can also configure the client-specific message size limits from the
command line. Open an elevated command prompt on the Exchange server (a Command Prompt window
you open by selecting Run as administrator) and run the appropriate commands for the limits that you
want to configure.

  ７ Note

       The size values in the commands are the default values, so you'll need to change them.

       Pay attention to whether the value is in bytes or kilobytes.

ActiveSync

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/Microsoft-Server-
  ActiveSync/" -section:system.webServer/security/requestFiltering
  /requestLimits.maxAllowedContentLength:30000000
  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/Microsoft-Server-
  ActiveSync/" -section:system.web/httpRuntime /maxRequestLength:10240
  %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/Microsoft-Server-
  ActiveSync/" -section:system.webServer/security/requestFiltering
  /requestLimits.maxAllowedContentLength:30000000
  %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/Microsoft-Server-
  ActiveSync/" -section:system.web/httpRuntime /maxRequestLength:10240
  %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/Microsoft-Server-
  ActiveSync/" -section:appSettings /[key='MaxDocumentDataSize'].value:10240000

Exchange Web Services

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/ews/" -
  section:system.webServer/security/requestFiltering
  /requestLimits.maxAllowedContentLength:67108864
  %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
  section:system.webServer/security/requestFiltering
  /requestLimits.maxAllowedContentLength:67108864
  %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
  section:system.serviceModel/bindings /customBinding.
  [name='EWSAnonymousHttpsBinding'].httpsTransport.maxReceivedMessageSize:67108864
  %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
  section:system.serviceModel/bindings /customBinding.
  [name='EWSAnonymousHttpBinding'].httpTransport.maxReceivedMessageSize:67108864
  %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
  section:system.serviceModel/bindings /customBinding.
  [name='EWSBasicHttpsBinding'].httpsTransport.maxReceivedMessageSize:67108864

<!-- p.329 -->

 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
 section:system.serviceModel/bindings /customBinding.
 [name='EWSBasicHttpBinding'].httpTransport.maxReceivedMessageSize:67108864
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
 section:system.serviceModel/bindings /customBinding.
 [name='EWSNegotiateHttpsBinding'].httpsTransport.maxReceivedMessageSize:67108864
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
 section:system.serviceModel/bindings /customBinding.
 [name='EWSNegotiateHttpBinding'].httpTransport.maxReceivedMessageSize:67108864
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
 section:system.serviceModel/bindings /customBinding.
 [name='EWSWSSecurityHttpsBinding'].httpsTransport.maxReceivedMessageSize:67108864
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
 section:system.serviceModel/bindings /customBinding.
 [name='EWSWSSecurityHttpBinding'].httpTransport.maxReceivedMessageSize:67108864
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
 section:system.serviceModel/bindings /customBinding.
 [name='EWSWSSecuritySymmetricKeyHttpsBinding'].httpsTransport.maxReceivedMessageSize:6710886
 4
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
 section:system.serviceModel/bindings /customBinding.
 [name='EWSWSSecuritySymmetricKeyHttpBinding'].httpTransport.maxReceivedMessageSize:67108864
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
 section:system.serviceModel/bindings /customBinding.
 [name='EWSWSSecurityX509CertHttpsBinding'].httpsTransport.maxReceivedMessageSize:67108864
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
 section:system.serviceModel/bindings /customBinding.
 [name='EWSWSSecurityX509CertHttpBinding'].httpTransport.maxReceivedMessageSize:67108864
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
 section:system.serviceModel/bindings /webHttpBinding.
 [name='EWSStreamingNegotiateHttpsBinding'].maxReceivedMessageSize:67108864
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/ews/" -
 section:system.serviceModel/bindings /webHttpBinding.
 [name='EWSStreamingNegotiateHttpBinding'].maxReceivedMessageSize:67108864

Outlook on the web

 %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/owa/" -
 section:system.webServer/security/requestFiltering
 /requestLimits.maxAllowedContentLength:35000000
 %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/owa/" -
 section:system.web/httpRuntime /maxRequestLength:35000
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/owa/" -
 section:system.webServer/security/requestFiltering
 /requestLimits.maxAllowedContentLength:35000000
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/owa/" -
 section:system.web/httpRuntime /maxRequestLength:35000
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/owa/" -
 section:system.serviceModel/bindings /webHttpBinding.
 [name='httpsBinding'].maxReceivedMessageSize:35000000
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/owa/" -
 section:system.serviceModel/bindings /webHttpBinding.
 [name='httpBinding'].maxReceivedMessageSize:35000000
 %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/owa/" -
 section:system.serviceModel/bindings /webHttpBinding.
 [name='httpsBinding'].readerQuotas.maxStringContentLength:35000000

<!-- p.330 -->

  %windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/owa/" -
  section:system.serviceModel/bindings /webHttpBinding.
  [name='httpBinding'].readerQuotas.maxStringContentLength:35000000

How do you know this worked?
To verify that you have successfully configured the client-specific message size limit, you need to send a
test message to and from a mailbox by using the affected client. You can try a few smaller attachments or
one large attachment so the test messages are approximately 33% less than the value you configured. For
example, a configured value of 85 MB results in a realistic maximum message size of approximately 64
MB.

<!-- p.331 -->

Availability service in Exchange Server
Article • 04/30/2025

APPLIES TO:          2016    2019     Subscription Edition

The Availability service makes free/busy information available to Outlook and Outlook on the
web (formerly known as Outlook Web App) clients. The Availability service improves
information workers' calendaring and meeting scheduling experience by providing secure,
consistent, and up-to-date free/busy information.

Outlook and Outlook on the web use the Availability service to perform the following tasks:

      Retrieve current free/busy information for Exchange mailboxes

      Retrieve current free/busy information from other Exchange organizations

      Retrieve published free/busy information from public folders for mailboxes on previous
      versions of Exchange

      View attendee working hours

      Show meeting time suggestions

How the availability service works in Exchange
Server
The Availability service retrieves free/busy information directly from the target Exchange
mailbox.

Outlook uses the Exchange Autodiscover service to obtain the URL of the Availability service.
For more information about the Autodiscover service, see Autodiscover service.

You can use the Exchange Management Shell to configure the Availability service. You can't use
the Exchange admin center (EAC) to configure the Availability service.

The Availability service API is available as a web service to let developers write third-party
integration tools.

Availability service and automatic reply messages
The Availability service provides access to automatic-reply messages that users send when they
are out of the office or away for an extended period of time.

<!-- p.332 -->

Information workers use the Automatic Replies feature (formerly known as Out of Office) in
Outlook and Outlook on the web to alert others when they're unavailable to respond to email
messages. This functionality makes it easier to set and manage automatic reply messages for
both information workers and administrators.

Methods used to retrieve free/busy information
The following table lists the methods used to retrieve free/busy information in different single-
forest topologies.

                                                                                           ﾉ   Expand table

 Client              Source mailbox           Target          Free/busy retrieval method
                     retrieving free/busy     mailbox
                     information

 Outlook 2010 or     Exchange 2010 or later   Exchange        The Availability service reads free/busy
 later                                        2010 or later   information from the target mailbox.

 Outlook on the      Exchange 2010 or later   Exchange        Outlook on the web or Outlook Web App
 web or Outlook                               2010 or later   calls the Availability service API, which reads
 Web App                                                      the free/busy information from the target
                                                              mailbox.

<!-- p.333 -->

Configure the Availability service for cross-
forest topologies in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019     Subscription Edition

The Availability service improves information workers' free/busy information by providing
secure, consistent, and up-to-date free/busy information to clients that are running Outlook. By
default, this service is installed with Exchange Server. In cross-forest topologies where all
connecting clients are running Outlook, the Availability service is the only method of retrieving
free/busy information. You can use the Exchange Management Shell to configure the
Availability service for cross-forest topologies.

  ７ Note

  You can't use the Exchange admin center (EAC) to configure the Availability service for
  cross-forest topologies.

Using the Availability service in trusted and
untrusted forests
You can use the Availability service in cross-forest topologies across trusted or untrusted
forests. The type of free/busy information that's available depends on if you're using a trusted
or untrusted forest.

Trusted forests: In trusted forests, you can configure the Availability service to retrieve
free/busy information on a per-user basis. When the Availability service is configured to
retrieve free/busy information on a per-user basis, the service can make cross-forest requests
on behalf of a particular user. This allows a user in a remote forest to retrieve detailed
free/busy information for someone who is not in the same forest.

Untrusted forests: In untrusted forests, you can only configure the Availability service to
retrieve free/busy information on an organization-wide basis. When the Availability service
makes free/busy cross-forest requests at the organizational level, free/busy information is
returned for each user in the organization. In untrusted forests, it isn't possible to control the
level of free/busy information that's returned on a per-user basis.

Configuring Windows for cross-forest topologies

<!-- p.334 -->

By default, a global address list (GAL) contains mail recipients from a single forest. If you have a
cross-forest environment, we recommend using Microsoft Identity Lifecycle Manager (ILM)
2007 Feature Pack 1 (FP1) to ensure that the GAL in any given forest contains mail recipients
from other forests. ILM 2007 FP1 creates mail users that represent recipients from other forests,
thereby allowing users to view them in the GAL and send mail. For example, users in Forest A
appear as a mail user in Forest B and vice versa. Users in the target forest can then select the
mail user object that represents a recipient in another forest to send mail.

To enable GAL synchronization, you create management agents that import mail-enabled
users, contacts, and groups from designated Active Directory services into a centralized
metadirectory. In the metadirectory, mail-enabled objects are represented as mail users.
Groups are represented as contacts without any associated membership. The management
agents then export these mail users to an organizational unit in the specified target forest.

What do you need to know before you begin?
     Estimated time to complete each procedure: 5 minutes.

     To open the Exchange Management Shell, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Availability Service Permissions"
     entries in the Clients and mobile devices permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

     There are additional considerations when the target forest is Exchange Server 2013 or
     Exchange Server 2016. See Cross forest free/busy lookup fails when target forest is
     Exchange Server 2013 or Exchange Server 2016         for more information.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online       , or Exchange Online Protection .

Use the Exchange Management Shell to configure
per-user free/busy information in a trusted cross-
forest topology

<!-- p.335 -->

This example configures the Availability service to retrieve per-user free/busy information on a
Mailbox server in the target forest.

  PowerShell

  Get-MailboxServer | Add-ADPermission -Accessrights Extendedright -Extendedrights
  "ms-Exch-EPI-Token-Serialization" -User "<Remote Forest Domain>\Exchange servers"

This example defines the free/busy access method that the Availability service uses on the local
Mailbox server in the source forest. The local Mailbox server is configured to access free/busy
information from the forest ContosoForest.com on a per-user basis. This example uses the
service account to retrieve free/busy information.

  PowerShell

  Add-AvailabilityAddressSpace -Forestname ContosoForest.com -AccessMethod PerUserFB
  -UseServiceAccount $true

  ７ Note

  To configure bidirectional cross-forest availability, repeat these steps in the Exchange
  Management Shell for the target forest.

If you choose to configure cross-forest availability with trust, and also choose to use a service
account (instead of specifying organization-wide or per-user credentials), you must extend
permissions as shown in the example in the next section, "Use the Exchange Management Shell
to configure trusted cross-forest availability with a service account." Performing that procedure
in the target forest gives Mailbox servers in the source forest permission to serialize the
original user context.

Use the Exchange Management Shell to configure
trusted cross-forest availability with a service
account
This example configures trusted cross-forest availability with a service account.

  PowerShell

  Get-MailboxServer | Add-ADPermission -Accessrights Extendedright -Extendedright
  "ms-Exch-EPI-Token-Serialization" -User "<Remote Forest Domain>\Exchange servers"

<!-- p.336 -->

For detailed information about syntax and parameters, see the following topics:

     Get-MailboxServer

     Add-ADPermission

     Add-AvailabilityAddressSpace

     Set-AvailabilityConfig

Use the Exchange Management Shell to configure
organization-wide free/busy information in an
untrusted cross-forest topology
This example sets the organization-wide account on the availability configuration object to
configure the access level for free/busy information in the target forest.

  PowerShell

  Set-AvailabilityConfig -OrgWideAccount "Contoso.com\User"

This example adds the Availability address space configuration object for the source forest, and
you're prompted to enter the credentials for organization-wide user in Contoso.com domain.

  PowerShell

  Add-AvailabilityAddressspace -Forestname Contoso.com -Accessmethod OrgWideFB -
  Credential (Get-Credential)

<!-- p.337 -->

Planning and deployment for Exchange
Server
07/01/2025

APPLIES TO:        2016    2019      Subscription Edition

This article contains links to articles and information about planning for and then deploying
Exchange Server.

  ） Important

  Ensure that you read the Release notes for Exchange Server topics before you begin your
  deployment. The release notes contains important information on issues you might
  encounter during and after your deployment.

   Tip

  As a companion to this article, we recommend using the Microsoft Exchange Server
  Deployment Assistant     . Use this tool to generate a customized checklist for planning,
  installing, or upgrading Exchange. Guidance is available for multiple scenarios, including
  an on-premises, hybrid, or cloud deployment.

Plan for Exchange Server
Use the information available in the following links to help plan your deployment of Exchange
Server into your organization.

  ） Important

  For information about installing Exchange Server in a test environment, see the Establish
  an Exchange Server test environment section later in this article.

Exchange architecture

  Learn about the Mailbox and Edge Transport server roles and more in Exchange.

Exchange Server system requirements

<!-- p.338 -->

  Understand the system requirements that need to be satisfied in your organization before
  you can install an Exchange Server.

Exchange Server prerequisites

  Learn about the Windows Server features and the other software that needs to be installed
  for a successful installation of an Exchange Server.

Active Directory

  Learn about how an Exchange Server uses Active Directory and how your Active Directory
  deployment affects your Exchange Server deployment.

Antispam and antimalware protection in Exchange Server

  Learn about the built-in antispam and antimalware protection options in an Exchange
  Server.

Exchange Server Hybrid Deployments

  Learn about planning a hybrid deployment between Microsoft 365 or Office 365 and your
  on-premises Exchange organization.

Exchange Server virtualization

  Learn how you can deploy an Exchange Server in a virtualized environment.

Exchange Online and Exchange development

  Learn about the application programming interfaces (APIs) that are available for
  applications that use Exchange Server.

Establish an Exchange Server test environment
Before you install your first Exchange server, we recommend that you install an Exchange
Server in an isolated test environment. This approach reduces the risk of end-user downtime
and negative ramifications to the production environment.

The test environment will act as your "proof of concept" for your new Exchange design and will
make it possible to move forward or roll back any implementations before deploying an
Exchange Server into your production environments. Having an exclusive test environment for

<!-- p.339 -->

validation and testing allows you to do pre-installation checks for your future production
environments. By installing in a test environment first, we believe that your organization will
have a better likelihood of success in a full production implementation.

For many organizations, the costs of building a test lab may be high because of the need to
duplicate the production environment. To reduce the hardware costs associated with a
prototype lab, we recommend the use of virtualization by using Hyper-V technologies in
Windows Server. Hyper-V enables server virtualization, allowing multiple virtual operating
systems to run on a single physical machine.

For detailed information about Hyper-V, see Server Virtualization. For information about the
Microsoft support of production Exchange servers on hardware virtualization software, see
Exchange Server virtualization.

Deploy Exchange Server
During the deployment phase, you install an Exchange Server into your organization. Before
you begin the deployment phase, you should plan your Exchange organization. For more
information, see the Plan for Exchange Server section earlier in this article.

Use the information available in the following links to help you deploy an Exchange Server.

Prepare Active Directory and domains for Exchange

  Learn about the steps you need to take to prepare your Active Directory forest for
  Exchange Server and the changes an Exchange Server installation makes to your forest.

Install Exchange Mailbox servers using the Setup wizard

  Learn about using the Setup wizard to install Mailbox servers.

Always install the latest Exchange Cumulative Update (CU) (Exchange Server build numbers
and release dates | Microsoft Docs). There is no need to install the RTM build or previous builds
and then upgrade to the latest CU. This is because each CU is a full build of the product.

Update with latest Exchange Security Update (SU) before bringing the server online. Verify
with the Exchange Health Checker script: https://aka.ms/ExchangeHealthChecker        .

Use unattended mode in Exchange Setup

  Learn about using the unattended setup at the command line to install, remove, update,
  and recover Exchange servers.

<!-- p.340 -->

Install Exchange Edge Transport servers using the Setup wizard

  Learn about using the Setup wizard to install Edge Transport servers in a perimeter
  network.

Upgrade Exchange to the latest Cumulative Update

  Learn about finding and installing the latest CU for the Exchange servers in your
  organization.

Keep your servers as up to date as possible. Always be either on latest released Exchange CU
or latest released -1 CU.

   1. This page contains links to the latest Exchange CU bits: Exchange Server build numbers
     and release dates | Microsoft Docs.

   2. See: Upgrade Exchange to the latest Cumulative Update | Microsoft Docs.

Ensure Windows Update/Microsoft Update (WU/MU) is turned on and consider further
turning on Automatic Update to pick up SUs.

Use an elevated command prompt to run any Cumulative Update or Security Update. If you
run into any problems when running update setup, see https://aka.ms/exupdatefaq         .

Periodically, run the Exchange Health Checker script to check if the latest Exchange SUs are in
place: https://aka.ms/ExchangeHealthChecker     .

Exchange Server Hybrid Deployments

  Read this article for information that will help you deploy an Exchange Server in an existing
  hybrid deployment.

Exchange Server post-installation tasks

  Learn about post-installation tasks to complete your Exchange Server installation.

Exchange Setup
You can use different types and modes of an Exchange Server Setup to install and maintain the
various editions and versions of an Exchange Server.

Exchange editions and versions

<!-- p.341 -->

Exchange is available in two server editions: Standard Edition and Enterprise Edition. The
edition you install is defined by your product key (the only available download can install both
versions). For more information, see Exchange licensing FAQs    .

Types of Exchange Server Setup
You have the following options for an Exchange Server Setup:

     Exchange Setup wizard: Running Setup.exe without any command line switches provides
     an interactive experience where you're guided by the Exchange Server Setup wizard.

     Exchange unattended setup: Running Setup.exe with command line switches enables you
     to install Exchange from an interactive command line or through a script.

Modes of Exchange Server Setup
Exchange setup includes the following modes:

     Install: Install a new server role (Mailbox server, Edge Transport server, or Management
     tools). This mode is available in the Exchange Setup wizard and unattended setup.

     Uninstall: Remove the Exchange installation from a computer. You can use this mode
     from both the Exchange Setup wizard and unattended setup.

     Upgrade: Install a CU on an existing Exchange server. You can use this mode from both
     the Exchange Setup wizard and unattended setup.

       ７ Note

       Exchange doesn't support in-place upgrades from previous versions. This mode is
       used only to install CUs.

     RecoverServer: You need to recover data from the Exchange server after a catastrophic
     failure. To do this, you install a new Windows server with the same FQDN as the failed
     server (for example, mailbox01.contoso.com), and then run Exchange Setup with the
     /Mode:RecoverServer switch without specifying the Exchange server roles.

     Setup detects the Exchange server object in Active Directory and installs the
     corresponding files and configuration automatically. After you recover the server, you can
     restore databases and reconfigure any additional settings. To run in RecoverServer mode:

        Exchange can't be already installed on the server.

<!-- p.342 -->

The Exchange server object must exist in Active Directory.

You can only use unattended setup.

７ Note

You must complete one mode of Setup before you can use another mode.

<!-- p.343 -->

Exchange Server 2019 and Subscription
Edition system requirements
10/09/2025

APPLIES TO:      2016       2019      Subscription Edition

   Tip

  Looking for the Exchange Server 2016 system requirements? See Exchange Server 2016
  system requirements.

This documentation outlines the system requirements for Exchange Server 2019 and Exchange
Server Subscription Edition (SE). For simplicity, both versions are referred to as "Exchange
Server" throughout.
Before installing Exchange Server, we recommend reviewing this information to verify that your
network, hardware, software, client applications, and related components meet the necessary
requirements. Additionally, ensure you understand the supported coexistence scenarios
between Exchange Server SE, Exchange Server 2019, and earlier versions.

  ７ Note

  For Exchange Server 2019 installations in the Chinese Region, install the Exchange Server
  2019 August 2023 (or higher) Security Update          to enable extended character support.

To install Exchange Server, see Deploy new installations of Exchange.

Supported coexistence scenarios for Exchange
Server
The supported coexistence scenarios between Exchange Server SE, Exchange Server 2019, and
earlier supported versions of Exchange Server are described in the following table:

                                                                                    ﾉ   Expand table

 Exchange         Exchange 2019 and Exchange SE organization coexistence
 version

 Exchange 2016    Supported with Exchange 2016 CU23 on all Exchange 2016 servers in the organization,
                  including Edge Transport servers.

<!-- p.344 -->

Supported hybrid deployment scenarios for
Exchange Server
Exchange Server supports hybrid deployments with Microsoft 365 organizations. For more
information about specific hybrid deployments, see Hybrid Deployment Prerequisites.

Network and directory server requirements for
Exchange Server
The requirements for the network and the directory servers in your Exchange Server
organization are described in the following table:

                                                                                          ﾉ   Expand table

 Component        Requirements

 Domain           All domain controllers in the forest must be running one of the supported versions of
 controllers      Windows Server. A comprehensive list of supported domain controller operating
                  systems can be found in the Exchange Server supportability matrix.

 Active           A comprehensive list of supported forests at the functional level can be found in the
 Directory        Exchange Server supportability matrix.
 forest

 Active           The Active Directory site where you install the Exchange Server must contain at least one
 Directory site   writeable domain controller that's also a global catalog server; or else, the installation
                  will fail. Furthermore, you can't install the Exchange server and then remove the domain
                  controller from the Active Directory site.

 DNS              Exchange Server supports the following DNS namespaces:
 namespace              Contiguous
                        Noncontiguous
                        Single label domains
                        Disjoint

                  For more information about DNS namespaces that are supported by Exchange, see
                  KB2269838     .

 IPv6             Exchange Server supports IPv6 only when IPv4 is also installed and enabled on the
                  Exchange server.
                  If you deploy Exchange in this configuration, and your network supports IPv4 and IPv6,
                  all Exchange servers can send data to and receive data from devices, servers, and clients
                  that use IPv6 addresses. For more information, see IPv6 Support in Exchange 2013.

<!-- p.345 -->

Directory server architecture for Exchange Server
Active Directory domain controllers on 64-bit hardware with a 64-bit version of Windows
Server will increase directory service performance for Exchange Server.

Installing Exchange Server on directory servers
For security and performance reasons, we don't recommend installing Exchange Server on
Active Directory servers. Install Exchange Server only on member servers.

To learn more about the issues that you'll encounter when you install Exchange on a directory
server, see Installing Exchange on a domain controller is not recommended
[WarningInstallExchangeRolesOnDomainController]. After Exchange is installed, changing the
server role from a member server to a directory server or vice-versa isn't supported.

Hardware requirements for Exchange Server
For information about deploying Exchange in a virtualized environment, see Exchange Server
virtualization.

                                                                                          ﾉ   Expand table

 Component        Requirements                                Notes

 Processor        Either of the following types of 64-bit     For information on supported operating
                  processors:                                 systems, see the Supported operating
                        Intel processor that supports Intel   systems for Exchange Server section later in
                        64 architecture (formerly known as    this topic.
                        Intel EM64T).
                        AMD processor that supports the
                        AMD64 platform.

                  Notes:

                        Intel Itanium IA64 processors
                        aren't supported.
                        Recommended supported
                        processor sockets are up to 2 on
                        physical machines.

<!-- p.346 -->

Component     Requirements                                   Notes

Memory        Varies by Exchange server role:                Exchange Server has large memory support
                    Mailbox: 128 GB minimum                  (up to 256 GB).
                       recommended
                       Edge Transport: 64 GB minimum
                       recommended.

Paging file   Set the paging file minimum and                None
size          maximum value to the same size: 25% of
              installed memory.

Disk space             At least 30 GB of free space on the   None
                       drive where you're installing
                       Exchange.
                       At least 200 MB of free space on
                       the system drive.
                       At least 500 MB of free space on
                       the drive that contains the
                       message queue database.

Screen        1024 x 768 pixels (XGA) or higher              None
resolution

File system   NTFS: Required on partitions that              None
              contain the following types of files:

                       The System partition.
                       Exchange binaries.
                       Files generated by Exchange
                       diagnostic logging.
                       Transport database files (for
                       example, the mail queue
                       database).

              ReFS: Supported on partitions that
              contain the following types of Exchange
              files:

                       Mailbox databases.
                       Transaction logs.
                       Transport database files (for
                       example, the mail queue database)
                       .

Supported operating systems for Exchange Server

<!-- p.347 -->

A comprehensive list of supported operating systems can be found in the Exchange Server
supportability matrix.

Supported PowerShell versions for Exchange Server
Exchange Server supports the version of PowerShell that's included in the release of Windows
Server where Exchange is installed. Don't install standalone downloads of Windows
Management Framework (WMF) or PowerShell on Exchange servers.

Installing other software on Exchange Server
We don't support installing Office client or Office server software on Exchange servers (for
example, SharePoint Server, Skype for Business Server, Office Online Server, or Project Server).
Other software that you want to install on an Exchange server need to be designed to run on
the same computer as Exchange Server.

Supported .NET Framework versions for Exchange
Server
We recommend that you use the latest version of the .NET Framework that's supported by the
release of Exchange you're installing.

A comprehensive list of supported .NET Framework versions can be found in the Exchange
Server supportability matrix.

Supported clients (with latest updates) in Exchange
Server
A comprehensive list of supported email clients can be found in the Exchange Server
supportability matrix.

Lync/Skype For Business Server integration with
Exchange Server
If you're integrating Lync presence and instant messaging with Exchange Server, Lync Server
2013 Cumulative Update (CU) 10 or higher is required. If you're integrating Skype for Business
presence and instant messaging with Exchange Server, Skype for Business Server CU 7 or
higher is required.

<!-- p.348 -->

Exchange third-party clients
Exchange Server offers several well-known protocols and publishes APIs that third-party
vendors often write clients for.

Microsoft makes no warranties, expressed or implied, as to the overall suitability, fitness,
compatibility, or security of clients that are created by third-party developers.

If you want to use a third-party client that uses our protocols or APIs, we recommend that you
thoroughly review and test all considerations (functionality, security, maintenance,
management, and so on) before you deploy the client in the enterprise workspace. We also
recommend that you ensure that the third-party vendor offers an appropriate Enterprise
Support Agreement (ESA).

<!-- p.349 -->

Exchange Server 2016 system requirements
Article • 05/09/2025

APPLIES TO:        2016    2019      Subscription Edition

   Tip

  Looking for the Exchange Server 2019 and Exchange Server SE requirements? See
  Exchange Server 2019 and SE system requirements.

Before you install Exchange Server 2016, we recommend that you review this topic to ensure
your network, hardware, software, clients, and other elements meet the requirements for
Exchange 2016. Also, ensure you understand the coexistence scenarios that are supported for
Exchange 2016 and earlier versions of Exchange.

To install Exchange 2016, see Deploy new installations of Exchange.

Supported coexistence scenarios for Exchange
2016
There are no earlier supported versions of Exchange Server that can coexist with Exchange
Server 2016.

Supported hybrid deployment scenarios for
Exchange 2016
Exchange 2016 supports hybrid deployments with Microsoft 365 organizations. For more
information about specific hybrid deployments, see Hybrid Deployment Prerequisites.

Network and directory server requirements for
Exchange 2016
The following table lists the requirements for the network and the directory servers in your
Exchange 2016 organization:

                                                                               ﾉ   Expand table

<!-- p.350 -->

 Component        Requirement

 Domain           All domain controllers in the forest must be running one of the supported versions of
 controllers      Windows Server. A comprehensive list of supported domain controller operating
                  systems can be found in the Exchange Server supportability matrix.

 Active           A comprehensive list of supported forest functional level can be found in the Exchange
 Directory        Server supportability matrix.
 forest

 Active           The Active Directory site where you install the Exchange Server must contain at least
 Directory site   one writeable domain controller that's also a global catalog server; or else, the
                  installation will fail. Furthermore, you can't install the Exchange server and then remove
                  the domain controller from the Active Directory site.

 DNS              Exchange 2016 supports the following domain name system (DNS) namespaces:
 namespace                Contiguous
 support                  Noncontiguous
                          Single label domains
                          Disjoint

                  For more information about DNS namespaces supported by Exchange, see Microsoft
                  Knowledge Base article 2269838, Microsoft Exchange compatibility with Single Label
                  Domains, Disjoined Namespaces, and Discontiguous Namespaces           .

 IPv6 support     In Exchange 2016, IPv6 is supported only when IPv4 is also installed and enabled. If
                  Exchange 2016 is deployed in this configuration, and the network supports IPv4 and
                  IPv6, all Exchange servers can send data to and receive data from devices, servers, and
                  clients that use IPv6 addresses. For more information, see IPv6 Support in Exchange
                  2013.

Directory server architecture for Exchange 2016
The use of 64-bit Active Directory domain controllers increases directory service performance
for Exchange 2016.

Installing Exchange 2016 on directory servers
For security and performance reasons, we recommend that you install Exchange 2016 only on
member servers and not on Active Directory servers. To learn about the issues you can face
when installing Exchange 2016 on a directory server, see Installing Exchange on a domain
controller is not recommended [WarningInstallExchangeRolesOnDomainController]. After
Exchange 2016 is installed, changing its role from a member server to a directory server, or vice
versa, isn't supported.

<!-- p.351 -->

Hardware requirements for Exchange 2016
For information about deploying Exchange in a virtualized environment, see Exchange Server
virtualization.

                                                                                         ﾉ   Expand table

 Component        Requirement                                        Notes

 Processor        Either of the following types of 64-bit            For more information, see Sizing
                  processors:                                        Exchange 2016 Deployments .
                        Intel processor that supports Intel 64
                        architecture (formerly known as Intel        For information on supported
                        EM64T).                                      operating systems, see the Supported
                        AMD processor that supports the AMD64        operating systems for Exchange 2016
                        platform.                                    section later in this topic.

                  Note: Intel Itanium IA64 processors aren't
                  supported.

 Memory           Varies by Exchange server role:                    For more information, see Sizing
                        Mailbox: 8 GB minimum.                       Exchange 2016 Deployments      .
                        Edge Transport: 4 GB minimum.

 Paging file      Set the paging file minimum and maximum            None
 size             value to the same size:
                        Less than 32 GB of RAM installed:
                        Physical RAM plus 10 MB, up to a
                        maximum value of 32 GB (32,778MB).
                        32 GB or more of RAM installed: 32 GB
                        plus 10 MB (32,778MB)

 Disk space             At least 30 GB of free space on the drive    For more information, see Sizing
                        where you're installing Exchange, plus an    Exchange 2016 Deployments .
                        additional 500 MB for each Unified
                        Messaging (UM) language pack that you
                        plan to install.
                        At least 200 MB of free space on the
                        System drive.
                        At least 500 MB of free space on the drive
                        that contains the message queue
                        database.

 Drive            DVD-ROM drive, local or network accessible.        None

 Screen           1024 x 768 pixels (XGA) or higher                  None
 resolution

<!-- p.352 -->

 Component      Requirement                                        Notes

 File format    NTFS: Required on partitions that contain the      None
                following types of files:

                      The System partition.
                      Exchange binaries.
                      Files generated by Exchange diagnostic
                      logging.
                      Transport database files (for example, the
                      mail queue database).

                ReFS: Supported on partitions that contain the
                following types of Exchange files:

                      Mailbox databases.
                      Transaction logs.
                      Content indexing files.

Supported operating systems for Exchange 2016
A comprehensive list of supported operating systems can be found in the Exchange Server
supportability matrix.

Important: We don't support the installation of Exchange 2016 on a computer that's running
Windows Server Core or Nano Server. The Windows Server Desktop Experience feature needs
to be installed. To install Exchange 2016, you need to do one of the following steps to install
the Desktop Experience on Windows Server prior to starting Exchange 2016 Setup:

     Windows Server 2012 and Windows Server 2012 R2: Run the following command in
     Windows PowerShell:

        PowerShell

        Install-WindowsFeature Server-Gui-Mgmt-Infra,Server-Gui-Shell -Restart

     Windows Server 2016: Install Windows Server 2016 and choose the Desktop Experience
     installation option. If a computer is running Windows Server 2016 Core mode and you
     want to install Exchange 2016 on it, you'll need to reinstall the operating system and
     choose the Desktop Experience installation option.

Supported Windows Management Framework versions for
Exchange 2016

<!-- p.353 -->

Exchange 2016 only supports the version of Windows Management Framework that's built in
to the release of Windows that you're installing Exchange on. Don't install versions of Windows
Management Framework that are made available as stand-alone downloads on servers running
Exchange.

Installing other software on Exchange 2016 servers
We don't support installing Office clients or other Office server products (for example,
SharePoint Server, Skype for Business Server, Office Online Server, or Project Server) on
Exchange 2016 servers. Software that you want to install on an Exchange 2016 server need to
be designed to run on the same computer as Exchange Server.

Supported .NET Framework versions for Exchange
2016
We recommend that you use the latest version of .NET Framework that's supported by the
release of Exchange you're installing.

A comprehensive list of supported .NET Framework versions can be found in the Exchange
Server supportability matrix.

Supported clients (with latest updates) in Exchange
2016
A comprehensive list of supported email clients can be found in the Exchange Server
supportability matrix.

Exchange third-party clients
Exchange Server offers several well-known protocols, and publishes APIs that third-party
vendors often write clients for.

Microsoft makes no warranties, expressed or implied, as to the overall suitability, fitness,
compatibility, or security of clients that are created by third-party developers.

If you want to use a third-party client that uses our protocols or APIs, we recommend that you
thoroughly review and test all considerations (functionality, security, maintenance,
management, and so on) before you deploy the client in the enterprise workspace. We also
recommend that you ensure that the third-party vendor offers an appropriate Enterprise
Support Agreement (ESA).

<!-- p.354 -->

<!-- p.355 -->

Exchange Server 2019 and SE prerequisites
06/16/2025

APPLIES TO:        2016    2019      Subscription Edition

   Tip

  Looking for the for Exchange Server 2016 prerequisites? See Exchange Server 2016
  prerequisites.

Overview
This topic provides the steps for installing the necessary Windows Server operating system
prerequisites for Exchange Server 2019 and Exchange Server Subscription Edition (SE) Mailbox
servers and Edge Transport servers, and also the Windows prerequisites for installing the
Exchange Management Tools on Windows client computers. For simplicity, both versions are
referred to as "Exchange Server" throughout.

After you've prepared your environment for Exchange Server, use the Microsoft Exchange
Server Deployment Assistant     for the next steps in your actual deployment. For information
on hybrid deployments, see Exchange Server Hybrid Deployments.

To actually install Exchange Server, see Deploy new installations of Exchange.

What do you need to know before you begin?
This section provides comprehensive recommendations and the most up-to-date information
about the components necessary for Exchange Server. These components are essential
prerequisites for the proper functioning of Exchange Server.

     Verify that your Active Directory meets the requirements for Exchange 2019 and SE.

     To ensure compatibility and optimal performance, make sure to use a supported
     operating systems for Exchange Server.

     Before you begin installing Exchange Server, ensure that your computer has the latest
     Windows updates installed.

     The Remote Registry Service must be set to Automatic and must not be set to Disabled .
     For recommended security guidelines, please refer to Security Guidelines regarding
     Remote Registry.

<!-- p.356 -->

Windows Server prerequisites for Exchange Server
The requirements to install Exchange Server on supported Operating Systems (OS) are
described in the following sections. We recommend either of the following methods to install
the Windows prerequisites for Exchange Server:

     Use the /InstallWindowsComponents switch in unattended Setup mode.
     Select the check box in the Exchange Setup Wizard to install Windows prerequisites.

When you use one of these options, you don't need to restart the computer after the Windows
components have been added.

Exchange Server preparing Active Directory
You can use any member of the Active Directory domain to prepare Active Directory for
Exchange Server. To prepare Active Directory using the graphical user interface (GUI), you need
to install the Exchange Management Tools role.

   1. The computer which is used to prepare the Active Directory requires the following
     software:

     a. Supported version of .NET Framework

        When installing on Windows Server Core, you must use the /q option to install this
        package. Additionally, you can use the /log [PATH] option to enable logging if
        desired.

     b. Visual C++ Redistributable Package for Visual Studio 2012

        If you're using unattended Setup from the command line to prepare Active Directory,
        this package isn't required. For an overview of the latest supported versions and more
        information, please refer to Prepare Active Directory and domains.

        The system requirements for the Visual C++ Redistributable package do not explicitly
        mention support for the latest Windows Server versions. However, the redistributable
        package is safe to install on these versions of Windows.

   2. Install the Remote Server Administration Tools (RSAT) for Active Directory Domain
     Services (ADDS) by running the following command in Windows PowerShell:

       PowerShell

       Install-WindowsFeature RSAT-ADDS

<!-- p.357 -->

Exchange Server Management tools
 1. Install the following software:

    a. Supported version of .NET Framework

   b. Visual C++ Redistributable Package for Visual Studio 2012

      The system requirements for the Visual C++ Redistributable package do not explicitly
      mention support for the latest Windows Server versions. However, the redistributable
      package is safe to install on these versions of Windows.

 2. Install the following Windows features:
    a. If you want to install the Exchange Server Management tools on supported Windows
      Server OS, make sure to install the following Windows features:

         PowerShell

         Install-WindowsFeature -Name Web-Mgmt-Console, Web-Metabase

   b. If you want to install the Exchange Server Management tools on supported Windows
      Client OS, make sure to install the following Windows features:

         PowerShell

         Enable-WindowsOptionalFeature -Online -FeatureName IIS-ManagementConsole,
         IIS-Metabase -All

Exchange Server Mailbox server role
 1. Install the following software:

    a. Supported version of .NET Framework

      When installing on Windows Server Core, you must use the /q option to install this
      package. Additionally, you can use the /log [PATH] option to enable logging if
      desired.

   b. Visual C++ Redistributable Package for Visual Studio 2012

    c. Visual C++ Redistributable Package for Visual Studio 2013

      The system requirements for the Visual C++ Redistributable package do not explicitly
      mention support for the latest Windows Server versions. However, the redistributable

<!-- p.358 -->

     package is safe to install on these versions of Windows.

2. Add the required Skype for Business Server components:

  a. Install the Server Media Foundation windows feature by executing the following
     command in Windows PowerShell:

       PowerShell

       Install-WindowsFeature Server-Media-Foundation

  b. Install Unified Communications Managed API 4.0 . This package is available for
     download and can be found in the \UCMARedist folder on the Exchange Server media.

     When installing on Windows Server Core, you must use the installation package
     located in \UCMARedist on distributed media. To install the package by using
     PowerShell, run the following command:

       PowerShell

       .\UCMARunTimeSetup.exe -q

3. If you aren't going to use Exchange Setup to install the required Windows components (in
  the wizard or from the command line), run the one of the following commands in
  Windows PowerShell:
  a. Windows features:
      i. Desktop Experience:

          PowerShell

          Install-WindowsFeature Server-Media-Foundation, NET-Framework-45-Core,
          NET-Framework-45-ASPNET, NET-WCF-HTTP-Activation45, NET-WCF-Pipe-
          Activation45, NET-WCF-TCP-Activation45, NET-WCF-TCP-PortSharing45, RPC-
          over-HTTP-proxy, RSAT-Clustering, RSAT-Clustering-CmdInterface, RSAT-
          Clustering-Mgmt, RSAT-Clustering-PowerShell, WAS-Process-Model, Web-Asp-
          Net45, Web-Basic-Auth, Web-Client-Auth, Web-Digest-Auth, Web-Dir-
          Browsing, Web-Dyn-Compression, Web-Http-Errors, Web-Http-Logging, Web-
          Http-Redirect, Web-Http-Tracing, Web-ISAPI-Ext, Web-ISAPI-Filter, Web-
          Metabase, Web-Mgmt-Console, Web-Mgmt-Service, Web-Net-Ext45, Web-
          Request-Monitor, Web-Server, Web-Stat-Compression, Web-Static-Content,
          Web-Windows-Auth, Web-WMI, Windows-Identity-Foundation, RSAT-ADDS

     ii. Server Core:

          PowerShell

<!-- p.359 -->

            Install-WindowsFeature Server-Media-Foundation, NET-Framework-45-Core,
            NET-Framework-45-ASPNET, NET-WCF-HTTP-Activation45, NET-WCF-Pipe-
            Activation45, NET-WCF-TCP-Activation45, NET-WCF-TCP-PortSharing45, RPC-
            over-HTTP-proxy, RSAT-Clustering, RSAT-Clustering-CmdInterface, RSAT-
            Clustering-PowerShell, WAS-Process-Model, Web-Asp-Net45, Web-Basic-Auth,
            Web-Client-Auth, Web-Digest-Auth, Web-Dir-Browsing, Web-Dyn-Compression,
            Web-Http-Errors, Web-Http-Logging, Web-Http-Redirect, Web-Http-Tracing,
            Web-ISAPI-Ext, Web-ISAPI-Filter, Web-Metabase, Web-Mgmt-Service, Web-
            Net-Ext45, Web-Request-Monitor, Web-Server, Web-Stat-Compression, Web-
            Static-Content, Web-Windows-Auth, Web-WMI, RSAT-ADDS

      iii. (Optional) Remove MSMQ: The Windows feature Message Queuing (MSMQ) is no
         longer a requirement for Exchange Server and can be safely uninstalled if it's
         currently installed:

            PowerShell

            Remove-WindowsFeature NET-WCF-MSMQ-Activation45, MSMQ

   b. IIS URL Rewrite Module

Exchange Server Edge Transport server role
 1. Install the following software:

    a. Supported version of .NET Framework

      When installing on Windows Server Core, you must use the /q option to install this
      package. Additionally, you can use the /log [PATH] option to enable logging if
      desired.

   b. Visual C++ Redistributable Package for Visual Studio 2012

      The system requirements for the Visual C++ Redistributable package do not explicitly
      mention support for the latest Windows Server versions. However, the redistributable
      package is safe to install on these versions of Windows.

 2. If you aren't going to use Exchange Setup to install the required Windows components (in
   the wizard or from the command line), run the following command in Windows
   PowerShell:

      PowerShell

      Install-WindowsFeature ADLDS

<!-- p.360 -->

Exchange Server 2016 prerequisites
06/11/2025

APPLIES TO:      2016      2019      Subscription Edition

   Tip

  Looking for the for Exchange Server 2019 or Exchange Server SE prerequisites? See
  Exchange Server 2019 and SE prerequisites.

Overview
This topic provides the steps for installing the necessary Windows Server operating system
prerequisites for Exchange Server 2016 Mailbox servers and Edge Transport servers, and also
the Windows prerequisites for installing the Exchange Management Tools on Windows client
computers.

After you've prepared your environment for Exchange Server, use the Microsoft Exchange
Server Deployment Assistant     for the next steps in your actual deployment. For information
on hybrid deployments, see Exchange Server Hybrid Deployments.

To actually install Exchange Server, see Deploy new installations of Exchange.

What do you need to know before you begin?
This section provides comprehensive recommendations and the most up-to-date information
about the components necessary for Exchange Server. These components are essential
prerequisites for the proper functioning of Exchange Server.

     Verify that your Active Directory meets the requirements for Exchange 2016.

     To ensure compatibility and optimal performance, make sure to use a supported
     operating systems for Exchange Server.

     Before you begin installing Exchange Server, ensure that your computer has the latest
     Windows updates installed.

     The Remote Registry Service must be set to Automatic and must not be set to Disabled .
     For recommended security guidelines, please refer to Security Guidelines regarding
     Remote Registry.
