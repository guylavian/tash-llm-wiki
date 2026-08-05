---
title: "Exchange Server — pages 1361-1400"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1361-1400
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1361-1400
family: exchange
documentKind: "doc"
abstract: "In the Exchange Management Shell, run this command to show all mailboxes where POP3 and IMAP4 access is disabled: PowerShell Get-CasMailbox -ResultSize unlimited -Filter \"PopEnabled -eq `$false -and ImapEnabled -eq `$false\" Configure authenticated SMTP settings for POP3 and IMAP"
---

# Exchange Server — pages 1361-1400

<!-- p.1361 -->

In the Exchange Management Shell, run this command to show all mailboxes where POP3
and IMAP4 access is disabled:

  PowerShell

  Get-CasMailbox -ResultSize unlimited -Filter "PopEnabled -eq `$false -and
  ImapEnabled -eq `$false"

<!-- p.1362 -->

Configure authenticated SMTP settings for
POP3 and IMAP4 clients in Exchange
Server
Article • 04/03/2025

APPLIES TO:        2016    2019      Subscription Edition

After you enable and configure POP3 or IMAP4 on an Exchange server as described in Enable
and configure POP3 on an Exchange server and Enable and configure IMAP4 on an Exchange
server, you need to configure the authenticated SMTP settings for POP3 and IMAP4 clients so
they can send email messages.

The default Receive connector named "Client Frontend <Server name>" in the Client Access
services on the Mailbox server listens for authenticated SMTP client submissions on port 587.
By default, this connector uses the following settings for internal and external client
(authenticated) SMTP connections:

      SMTP server: <ServerFQDN> . For example, mailbox01.contoso.com .

      TCP port: 587

      Encryption method: TLS. Note that this is opportunistic TLS (STARTTLS) that results in an
      encrypted connection after the initial plain text protocol handshake.

For more information, see Default Receive connectors created during setup and Client access
protocol architecture.

To configure the authenticated SMTP settings that are used by POP3 and IMAP4 clients,
perform the following steps:

   1. Configure the FQDN on the "Client Frontend <Server name>" Receive connector.

   2. Specify the certificate that's used to encrypt authenticated SMTP client connections.

   3. Configure Outlook on the web (formerly known as Outlook Web App) to display the
      SMTP settings for authenticated SMTP clients at Settings > Options > Mail > Accounts >
      POP and IMAP.

<!-- p.1363 -->

For more information about POP3 and IMAP4, see POP3 and IMAP4 in Exchange Server.

What do you need to know before you begin?
    Estimated time to complete: 5 minutes.

    Secure Sockets Layer (SSL) is being replaced by Transport Layer Security (TLS) as the
    protocol that's used to encrypt data sent between computer systems. They're so closely
    related that the terms "SSL" and "TLS" (without versions) are often used interchangeably.
    Because of this similarity, references to "SSL" in Exchange topics, the Exchange admin
    center, and the Exchange Management Shell have often been used to encompass both
    the SSL and TLS protocols. Typically, "SSL" refers to the actual SSL protocol only when a
    version is also provided (for example, SSL 3.0). To find out why you should disable the SSL
    protocol and switch to TLS, check out Protecting you against the SSL 3.0 vulnerability .

    If you have POP3 or IMAP4 clients that can only send SMTP email on port 25, you can
    configure port 25 on the "Client Frontend <Server name>" Receive connector to allow
    clients to send authenticated SMTP email. However, because port 25 is also configured on
    the "Client Frontend <Server name>" Receive connector for email from external SMTP
    servers, you'll need to modify the local IP addresses that are used to listen on port 25 on
    one or both of the connectors. For more information, see Receive connector local address
    bindings.

    You need to be assigned permissions before you can perform this procedure or
    procedures. To see what permissions you need, see the "Receive connectors" entry in the
    Mail flow permissions topic.

    For information about keyboard shortcuts that may apply to the procedures in this topic,
    see Keyboard shortcuts in the Exchange admin center.

<!-- p.1364 -->

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Step 1: Configure the FQDN on the "Client
Frontend <Server name>" Receive connector
You can skip this step if you want to keep the default server FQDN value (for example,
mailbox01.contoso.com). Or, you can specify an FQDN value that's more compatible with your
Internet naming convention or a TLS certificate that you want to use.

If you change the FQDN value, and you want internal POP3 or IMAP4 clients to use this
connector to send email, the new FQDN needs to have a corresponding record in your internal
DNS.

Regardless of the FQDN value, if you want external POP3 or IMAP4 clients to use this
connector to send email, the FQDN needs to have a corresponding record in your public DNS,
and the TCP port (587) needs to be allowed through your firewall to the Exchange server.

Use the EAC to configure the FQDN for authenticated SMTP
clients
   1. In the EAC, go to Mail flow > Receive connectors.

   2. In the list of Receive connectors, select Client Frontend <Server name>, and then click
       Edit (   ).

   3. In the Exchange Receive Connector page that opens, click Scoping.

   4. In the FQDN field, enter the SMTP server FQDN that you want to use for authenticated
       SMTP client connections (for example, mail.contoso.com) and then click Save.

<!-- p.1365 -->

Use the Exchange Management Shell to configure the FQDN
for authenticated SMTP clients
To configure the FQDN for authenticated SMTP clients, use the following syntax:

  PowerShell

  Get-ReceiveConnector -Identity "Client Frontend*" | Set-ReceiveConnector -Fqdn
  <FQDN>

This example configures the FQDN value mail.contoso.com.

  PowerShell

<!-- p.1366 -->

  Get-ReceiveConnector -Identity "Client Frontend*" | Set-ReceiveConnector -Fqdn
  mail.contoso.com

How do you know this step worked?
To verify that you've successfully the FQDN on the "Client Frontend <Server name> " Receive
connector, use either of the following procedures:

     the EAC, go to Mail flow > Receive connectors > select Client Frontend <Server name>,
     click Edit (    ) > Scoping, and verify the value in the FQDN field.

     In the Exchange Management Shell, run the following command:

        PowerShell

        Get-ReceiveConnector -Identity "Client Frontend*" | Format-List Name,Fqdn

Step 2: Use the Exchange Management Shell to
specify the certificate that's used to encrypt
authenticated SMTP client connections
The certificate needs to match or contain the FQDN value that you specified in the previous
step, and the POP3 and SMTP clients need to trust the certificate, which likely means a
certificate from a commercial certification authority. For more information, see Certificate
requirements for Exchange services.

Also, you need to assign the certificate to the Exchange SMTP service. For more information,
see Assign certificates to Exchange Server services.

To specify the certificate that's used for authenticated SMTP client connections, use the
following syntax:

  PowerShell

  $TLSCert = Get-ExchangeCertificate -Thumbprint <ThumbprintValue>

  PowerShell

  $TLSCertName = "<I>$($TLSCert.Issuer)<S>$($TLSCert.Subject)"

<!-- p.1367 -->

  PowerShell

  Get-ReceiveConnector -Identity "Client Frontend*" | Set-ReceiveConnector -
  TlsCertificateName $TLSCertName

This example uses the certificate that has the thumbprint value
434AC224C8459924B26521298CE8834C514856AB.

  PowerShell

  $TLSCert = Get-ExchangeCertificate -Thumbprint
  434AC224C8459924B26521298CE8834C514856AB

  PowerShell

  $TLSCertName = "<I>$($TLSCert.Issuer)<S>$($TLSCert.Subject)"

  PowerShell

  Get-ReceiveConnector -Identity "Client Frontend*" | Set-ReceiveConnector -
  TlsCertificateName $TLSCertName

How do you know this step worked?
To verify that you've specified the certificate that's used to encrypt authenticated SMTP client
connections, perform the following steps:

   1. Run the following command in the Exchange Management Shell:

        PowerShell

        Get-ReceiveConnector -Identity "Client Frontend*" | Format-List
        Name,Fqdn,TlsCertificateName

   2. Run the following command in the Exchange Management Shell:

        PowerShell

        Get-ExchangeCertificate | Format-List
        Thumbprint,Issuer,Subject,CertificateDomains,Services

   3. Verify the Subject or CertificateDomains field of the certificate that you specified on the
     Receive connector contains the Fqdn value of the Receive connector (exact match or

<!-- p.1368 -->

     wildcard match).

Step 3: Use the Exchange Management Shell to
configure Outlook on the web to display the SMTP
settings for authenticated SMTP clients
To configure Outlook on the web to display the SMTP settings server for authenticated SMTP
clients, run the following command:

  PowerShell

  Get-ReceiveConnector -Identity "Client Frontend*" | Set-ReceiveConnector -
  AdvertiseClientSettings $true

  ７ Note

  To prevent the SMTP settings from being displayed in Outlook on the web, change the
  value from $true to $false .

How do you know this step worked?
To verify that you've configured Outlook on the web to display the SMTP settings for
authenticated SMTP clients, perform the following steps:

   1. Open a mailbox in Outlook on the web, and then click Settings > Options.

   2. Click Mail > Accounts > POP and IMAP and verify the correct SMTP settings are
     displayed.

<!-- p.1369 -->

       ７ Note

       If the SMTP settings that you configured don't appear as expected in Outlook on the
       web, run the commands net stop w3svc /y and net start w3svc to restart Internet
       Information Services (IIS).

How do you know this task worked?
To verify that you've configured the authenticated SMTP settings on the Exchange server,
perform one or more following procedures:

     Use the Test-PopConnectivity or Test-ImapConnectivity cmdlets, which use authenticated
     SMTP to send test messages. For more information, see Test-PopConnectivity and Test-
     ImapConnectivity.

     Enable protocol logging on the "Client Frontend <Server name>" Receive connector,
     configure a POP3 or IMAP4 client to connect to a mailbox, send a test message from an
     internal network connection and/or an external Internet connection, and view the results
     in the protocol log. For more information, see Protocol logging.

       ７ Note

       You can't use POP3 or IMAP4 to connect to the Administrator mailbox. This limitation
       was intentionally included in Exchange 2016 and Exchange 2019 to enhance the
       security of the Administrator mailbox.

<!-- p.1370 -->

Outlook for iOS and Android
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Outlook for iOS and Android supports two authentication types in Exchange on-premises
environments: Basic authentication and hybrid Modern Authentication.

Outlook for iOS and Android uses Basic authentication with Exchange ActiveSync in the
following environments:

      In Exchange Server 2010 environments

      When a hybrid relationship with Microsoft 365 or Office 365 hasn't been configured

      When hybrid Modern Authentication hasn't been enabled

For more information, see Using Basic authentication with Outlook for iOS and Android.

For customers running Exchange Server 2013, Exchange Server 2016, or Exchange Server 2019
in a hybrid relationship with Microsoft 365 or Office 365, Outlook for iOS and Android can be
configured to use hybrid Modern Authentication. For more information, see Using hybrid
Modern Authentication with Outlook for iOS and Android.

  ７ Note

  The Outlook for iOS and Android Help Center        is available for users, including help for
  using the app on specific devices and troubleshooting information.

Differences when managing devices on "Hybrid
Modern Auth (HMA)" enabled on-premises
Exchange servers
Historically for other EAS implementations, a unique device ID is provisioned for each
smartphone trying to connect to the same OnPrem mailbox and ABQ (Allow, Block,
Quarantine) or any MDM can manage these device IDs like for native EAS applications.

However, when connecting to HMA enabled on-premises tenant using Outlook Mobile there
are some differences in design as the user's data is stored in a central cache inside of Exchange
Online tenant. To understand the design philosophy and its benefits see section Using hybrid
Modern Authentication with Outlook for iOS and Android. This capability also allows tenant

<!-- p.1371 -->

admins to safely issue remote wipe of data for scenarios where a user leaves the company, or a
device is compromised. Some of the differences are described below.

     Users connect to a cache created inside the Exchange Online tenant: When a user
     connects to a Hybrid Modern Authentication enabled On Premise tenant using Outlook
     Mobile application, on the backend Exchange creates a synchronized cache of users 4
     weeks of data in a user-protected mailbox. What this means is if multiple devices connect,
     they'll be accessing a single endpoint inside Exchange. And a unique device ID is seen On
     Premise side. The synchronized cache is also called a Cloud Cache account.

     Cloud Cache might generate multiple devices: The on-premises admin might see
     multiple devices because of how the Cloud Cache is bootstrapped and because expired
     devices may not be expired. When Exchange first validates the Cloud Cache account, it
     will use a generic device ID. Once the account has been verified, a new personalized
     device ID called the subscription is used.

     Blocking or issuing remote wipe: If the on-premises admin wants to remove access to
     content, they should run a remote wipe on-premises. The Cloud Cache will proxy the
     remote wipe to all connected devices. If the on-premises admin wants to block access to
     content, they should do it through on-premises. Then Cloud Cache will be unable to sync
     any new content. To get more detail about remote wipe, see section Perform a remote
     wipe on a mobile phone

Best practice with MDM
     We recommend using an MDM like Intune associated with Conditional Access feature to
     manage Outlook Mobile application. Refer to section Managing Outlook for iOS and
     Android in Exchange Online

     Intune management works for accounts connected using Hybrid Modern Auth to on-
     premises servers. Indeed, that is one of its value propositions. All devices connected to a
     single Cloud Cache present the same ID to the on-premises server because they share the
     same physical storage in that Microsoft 365 "middle tier". Intune management doesn't
     work for accounts connecting via Basic auth to on-premises because the on-premises
     admin has little visibility into the Microsoft 365 identities involved.

     A single on-premises user may have a single Microsoft 365 identity. He may have more
     than 1. That's because the Microsoft 365 identity is computed from the sign in name
     presented by the client user. This may be tim@contoso.com. It may be contoso.com/tim.
     Each can be used to control sign in to the on-premises server but there's no way inside
     Microsoft 365 to discover that these two different names represent the same on-premises

<!-- p.1372 -->

user. As such, each will have a different Microsoft 365 identity, a different Microsoft 365
Cloud Cache and present a different device ID to the on-premises EAS server.

<!-- p.1373 -->

Using hybrid Modern Authentication with
Outlook for iOS and Android
Article • 04/30/2025

APPLIES TO:        2016    2019        Subscription Edition

The Outlook app for iOS and Android is designed as the best way to experience Microsoft 365
or Office 365 on your mobile device by using Microsoft services to help find, plan, and
prioritize your daily life and work. Outlook provides the security, privacy, and support you need
while protecting corporate data via capabilities such as Microsoft Entra Conditional Access and
Intune app protection policies. The following sections provide an overview of the hybrid
Modern Authentication architecture, the required prerequisites for its deployment, and how to
securely deploy Outlook for iOS and Android for Exchange on-premises mailboxes.

Microsoft Cloud architecture for hybrid Exchange
Server customers
Outlook for iOS and Android is a cloud-backed application. This characteristic indicates that
your experience consists of a locally installed app powered by a secure and scalable service
running in the Microsoft Cloud.

For Exchange Server mailboxes, Outlook for iOS and Android's architecture is built directly into
the Microsoft Cloud, providing customers more benefits such as security, privacy, built-in
compliance, and transparent operations that Microsoft commits to in the Microsoft Trust
Center    and Azure Trust Center   .

Within the Microsoft 365 or Office 365-based architecture, Outlook for iOS and Android uses
the native Microsoft sync technology for data synchronization that is protected by a TLS-

<!-- p.1374 -->

secured connection end-to-end, between Microsoft 365 or Office 365 and the app.

The Exchange ActiveSync (EAS) connection between Exchange Online and the on-premises
environment enables synchronization of the users' on-premises data and includes four weeks
of email, all calendar data, all contact data, and out-of-office status in your Exchange Online
tenant. This data is removed automatically from Exchange Online after 30 days when the
account is deleted in Microsoft Entra ID.

Data synchronization between the on-premises environment and Exchange Online happens
independent of user behavior. This independency ensures that we can send new messages to
the devices quickly.

Processing information in the Microsoft Cloud enables advanced features and capabilities, such
as the categorization of email for the Focused Inbox, customized experience for travel and
calendar, and improved search speed. Relying on the cloud for intensive processing and
minimizing the resources required from users' devices enhances the app's performance and
stability. Lastly, it allows Outlook to build features that work across all email accounts,
regardless of the technological capabilities of the underlying servers (such as different versions
of Exchange Server, Microsoft 365, or Office 365).

Specifically, this new architecture has the following improvements:

   1. Enterprise Mobility + Security support: Customers can take advantage of Microsoft
     Enterprise Mobility + Security (EMS) including Microsoft Intune and Microsoft Entra ID P1
     or P2, to enable conditional access and Intune app protection policies, which control and
     secure corporate messaging data on the mobile device.

   2. Fully powered by Microsoft Cloud: The on-premises mailbox data is synchronized into
     Exchange Online, which provides the benefits of security, privacy, compliance, and
     transparent operations that Microsoft commits to in the Microsoft Trust Center           .

   3. OAuth protects users' passwords: Outlook uses hybrid Modern Authentication (OAuth)
     to protect users' credentials. Hybrid Modern Authentication provides Outlook with a
     secure mechanism to access the Exchange data without ever touching or storing a user's
     credentials. At sign-in, the user authenticates directly against an identity platform (either
     Microsoft Entra ID or an on-premises identity provider like ADFS) and receives an access
     token in return, which grants Outlook access to the user's mailbox or files. The service
     doesn't have access to the user's password at any point of time.

   4. Provides Unique Device IDs: Each Outlook connection is uniquely registered in Microsoft
     Intune and can therefore be managed as a unique connection.

   5. Unlocks new features on iOS and Android: This update enables the Outlook app to take
     advantage of native Microsoft 365 or Office 365 features that aren't supported in

<!-- p.1375 -->

     Exchange on-premises today, such as using full Exchange Online search and Focused
     Inbox. These features are available only when using Outlook for iOS and Android.

  ７ Note

  Device management through the on-premises Exchange admin center (EAC) is not
  possible. Intune is required to manage mobile devices.

Data security, access, and auditing controls
With on-premises data being synchronized with Exchange Online, customers have questions
about how the data is protected in Exchange Online. Encryption in the Microsoft Cloud
discusses how BitLocker is used for volume-level encryption. Service Encryption with Microsoft
Purview Customer Key is supported in the Outlook for iOS and Android architecture, but note
that the user must have an Office 365 Enterprise E5 license (or the corresponding versions of
those plans for Government or Education) to have an encryption policy assigned using the set-
mailuser cmdlet.

By default, Microsoft engineers have zero standing administrative privileges and zero standing
access to customer content in Microsoft 365 or Office 365. Administrative Access Controls
discusses personnel screening, background checks, Lockbox and Customer Lockbox, and more.

ISO Audited Controls on Service Assurance    documentation provides the status of audited
controls from global information security standards and regulations that Microsoft 365 and
Office 365 have implemented.

Connection flow
When Outlook for iOS and Android is enabled with hybrid Modern Authentication, the
connection flow is as follows.

<!-- p.1376 -->

1. After the user enters their email address, Outlook for iOS and Android connects to the
  AutoDetect service. AutoDetect determines the mailbox type by starting an AutoDiscover
  query to Exchange Online. Exchange Online determines that the user's mailbox is on-
  premises and returns a 302-redirect to AutoDetect with the on-premises Autodiscover
  URL. AutoDetect starts a query against the on-premises AutoDiscover service to
  determine the ActiveSync endpoint for the email address. The URL attempted on-
  premises is similar to this example:
  <https://autodiscover.contoso.com/autodiscover/autodiscover.json?

  Email=test%40contoso.com&Protocol=activesync&RedirectCount=3> .

2. AutoDetect starts a connection to the on-premises ActiveSync URL returned in Step 1
  above with an empty bearer challenge. The empty bearer challenge tells the on-premises
  ActiveSync that the client supports Modern Authentication. On-premises ActiveSync
  responds with a 401-challenge response and includes the WWW-Authenticate: Bearer

<!-- p.1377 -->

     header. Within the WWW-Authenticate: Bearer header is the authorization_uri value that
     identifies the Microsoft Entra endpoint that should be used to obtain an OAuth token.

  3. AutoDetect returns the Microsoft Entra endpoint to the client. The client begins the sign
     in flow and the user is presented with a Web form (or redirected to the Microsoft
     Authenticator app) and can enter credentials. Depending on the identity configuration,
     this process might or might not involve a federated endpoint redirect to an on-premises
     identity provider. Ultimately, the client obtains an access-and-refresh token pair, which is
     named AT1/RT1. This access token is scoped to the Outlook for iOS and Android client
     with an audience of the Exchange Online endpoint.

  4. Outlook for iOS and Android establishes a connection to Exchange Online and issues a
     provisioning request that includes the user's access token (AT1) and the on-premises
     ActiveSync endpoint.

  5. The MRS provisioning API within Exchange Online uses AT1 as input and obtains a second
     access-and-refresh token pair (named AT2/RT2) to access the on-premises mailbox via an
     on-behalf-of call to Active Directory. This second access token is scoped with the client
     being Exchange Online and an audience of the on-premises ActiveSync namespace
     endpoint.

  6. If the mailbox isn't provisioned, then the provisioning API creates a mailbox.

  7. The MRS provisioning API establishes a secure connection to the on-premises ActiveSync
     endpoint and synchronizes the user's messaging data using the AT2 access token as the
     authentication mechanism. RT2 is used periodically to generate a new AT2 so that data
     can be synchronized in the background without user intervention.

  8. Data is returned to the client.

Technical and licensing requirements
The hybrid Modern Authentication architecture has the following technical requirements:

  ７ Note

  On-premises accounts leveraging hybrid Modern Authentication with Outlook mobile are
  not supported with Office 365 US Government Community and Defense tenants, Office
  365 Germany tenants, and Office 365 China operated by 21Vianet tenants.

  1. Exchange on-premises setup:

<!-- p.1378 -->

       Exchange Server 2019 Cumulative Update 1 (CU1) or later, Exchange Server 2016
       Cumulative Update 8 (CU8) or later, or Exchange Server 2013 CU19 or later on all
       Exchange servers. In hybrid deployments (on-premises Exchange and Exchange
       Online) or in organizations that use Exchange Online Archiving (EOA) with their on-
       premises Exchange deployment, you need to deploy the most current CU or one CU
       before the most current version.

       All Exchange 2007 or Exchange 2010 servers must be removed from the
       environment. These versions of Exchange are out of mainstream support and don't
       work with Intune-managed Outlook for iOS and Android. In this architecture,
       Outlook for iOS and Android uses OAuth as the authentication mechanism. One of
       the on-premises configuration changes that occur enables the OAuth endpoint to
       the Microsoft Cloud as the default authorization endpoint. When this change is
       made, clients can start negotiating the use of OAuth. Because this change spans the
       whole organization, Exchange 2010 mailboxes fronted by either Exchange 2013 or
       2016 incorrectly think they can do OAuth (they can't), and end up in a disconnected
       state (Exchange 2010 doesn't support OAuth as an authentication mechanism).

2. Active Directory Synchronization. Active Directory synchronization of the entire on-
  premises mail recipient directory with Microsoft Entra ID, via Microsoft Entra Connect. If
  you have Microsoft Entra app and attribute filtering enabled in Microsoft Entra Connect
  configuration, ensure that the following applications are selected:

       Office 365 ProPlus
       Exchange Online
       Azure RMS
       Intune

  If you don't have Microsoft Entra app and attribute filtering enabled in Microsoft Entra
  Connect configuration, all required applications are already selected by default.

    ） Important

    Outlook for iOS and Android uses the tenant's Exchange Online Global Address List
    for on-premises mailboxes that leverage hybrid Modern Authentication. If all mail
    recipients aren't synchronized into Microsoft Entra ID, users will experience mail flow
    issues.

3. Exchange hybrid setup: Requires full hybrid relationship between Exchange on-premises
  with Exchange Online.

<!-- p.1379 -->

       A hybrid Microsoft 365 or Office 365 organization is configured in full hybrid
       configuration using Exchange Classic Hybrid Topology mode and is set up as
       specified in the Exchange Deployment Assistant .

          ７ Note

          Hybrid Modern Authentication is not supported with the Hybrid Agent.

       Requires a Microsoft 365 or Office 365 Enterprise, Business, or Education
       organization.

       The on-premises mailbox data is synchronized in the same datacenter region where
       that Microsoft 365 or Office 365 organization is set up or to the datacenter region
       defined in the account's PreferredDataLocation. For more information about where
       Microsoft 365 and Office 365 data is located, visit the Microsoft Trust Center   . For
       more information on PreferredDataLocation, see Multi-Geo Capabilities.

       The external URL host names for Exchange ActiveSync and AutoDiscover must be
       published as service principals to Microsoft Entra ID through the Hybrid
       Configuration Wizard.

       AutoDiscover and Exchange ActiveSync namespaces must be accessible from the
       Internet and can't be fronted by a pre-authentication solution.

       Ensure SSL or TLS offloading isn't being used between the load balancer and your
       Exchange servers, as this set up affects the use of the OAuth token. SSL and TLS
       bridging (termination and re-encryption) is supported.

4. Intune setup: Both Intune standalone and Co-Management deployments are supported
  (Basic Mobility and Security for Microsoft 365 isn't supported).

5. Microsoft 365 and Office 365 licensing:

       Outlook for iOS and Android is free for consumer usage from the iOS App store and
       from Google Play. However, commercial users require a Microsoft 365 or Office 365
       subscription that includes the Office desktop applications: Microsoft 365 Apps for
       Business, Microsoft 365 Business Standard, Microsoft 365 Apps for enterprise, Office
       365 Enterprise E3, Office 365 Enterprise E5, or the corresponding versions of those
       plans for Government or Education. Commercial users with the following
       subscriptions are allowed to use the Outlook mobile app on devices with integrated
       screens 10.1" diagonally or less: Office 365 Enterprise E1, Office 365 F1, Office 365
       A1, Microsoft 365 Business Basic, and if you only have an Exchange Online license

<!-- p.1380 -->

           (without Office). If you only have an Exchange on-premises (Exchange Server)
           license, you aren't licensed to use the app.
           Use of advanced Exchange Online features (for example, Service Encryption with
           Customer Key or Multi-Geo Capabilities) require the on-premises user to be
           assigned the applicable Office 365 or Microsoft 365 subscription license within the
           Microsoft 365 Admin Center.

     For more information on how to assign a license, see Add users individually or in bulk.

   6. EMS licensing: Each on-premises user must have one of the following licenses:

           Intune standalone + Microsoft Entra ID P1 or P2 or Microsoft Entra ID P1 or P2
           Enterprise Mobility + Security E3, Enterprise Mobility + Security E5

Implementation steps
Enabling support for hybrid Modern Authentication in your organization requires each of the
following steps, which are detailed in the following sections:

   1. Create a conditional access policy
   2. Create an Intune app protection policy
   3. Enable hybrid Modern Authentication

Create a conditional access policy
When an organization decides to standardize how users access Exchange data, using Outlook
for iOS and Android as the only email app for end users, they can configure a conditional
access policy that blocks other mobile access methods. Outlook for iOS and Android
authenticates via the Microsoft Entra identity object and then connects to Exchange Online.
Therefore, you need to create Microsoft Entra Conditional Access policies to restrict mobile
device connectivity to Exchange Online. To do this task, you need two conditional access
policies, with each policy targeting all potential users. Details on creating these policies can be
found in Conditional Access: Require approved client apps or app protection policy.

   1. Follow the steps in Require approved client apps or app protection policy with mobile
     devices. This policy allows Outlook for iOS and Android, but blocks OAuth and basic
     authentication capable Exchange ActiveSync mobile clients from connecting to Exchange
     Online.

        ７ Note

<!-- p.1381 -->

        This policy ensures mobile users can access all Office endpoints using the applicable
        apps.

   2. Follow the steps in Block Exchange ActiveSync on all devices, which prevents Exchange
     ActiveSync clients using basic authentication on non-mobile devices from connecting to
     Exchange Online.

     The above policies use the grant control Require app protection policy, which ensures
     that an Intune App Protection Policy is applied to the associated account within Outlook
     for iOS and Android before granting access. If the user isn't assigned to an Intune App
     Protection Policy, isn't licensed for Intune, or the app isn't included in the Intune App
     Protection Policy, then the policy prevents the user from obtaining an access token and
     gaining access to messaging data.

   3. Finally, follow Block legacy authentication with Microsoft Entra Conditional Access to
     block legacy authentication for other Exchange protocols on iOS and Android devices;
     this policy should target only Microsoft 365 or Office 365 Exchange Online cloud app and
     iOS and Android device platforms. This approach ensures mobile apps using Exchange
     Web Services, IMAP4, or POP3 protocols with basic authentication can't connect to
     Exchange Online.

  ） Important

  To leverage app-based conditional access policies, the Microsoft Authenticator app must
  be installed on iOS devices. For Android devices, the Intune Company Portal app is
  required. For more information, see App-based conditional access with Intune.

To block other mobile device clients (such as the native mail client included in the mobile
operating system) from connecting to your on-premises environment (which authenticate via
basic authentication against on-premises Active Directory):

You can use the built-in Exchange mobile device access rules and block all mobile devices from
connecting by setting the following command in the Exchange Management Shell:

  PowerShell

  Set-ActiveSyncOrganizationSettings -DefaultAccessLevel Block

  ７ Note

<!-- p.1382 -->

  The command might impact users connecting to Exchange on-premises with their mobile
  devices.

Create an Intune app protection policy
After hybrid Modern Authentication is enabled, all on-premises mobile users can use Outlook
for iOS and Android using the Microsoft 365 or Office 365-based architecture. Therefore, it's
important to protect corporate data with an Intune app protection policy.

Create Intune app protection policies for both iOS and Android using the steps documented in
How to create and assign app protection policies. At a minimum, each policy must fulfill the
following conditions:

   1. They include all Microsoft mobile applications, such as Word, Excel, or PowerPoint, as this
     inclusion ensures that users can access and manipulate corporate data within any
     Microsoft app in a secure fashion.

   2. They mimic the security features that Exchange provides for mobile devices, including:

             Requiring a PIN for access (which includes Select Type, PIN length, Allow Simple PIN,
             Allow fingerprint)
             Encrypting app data
             Blocking managed apps from running on "jailbroken" and rooted devices

   3. They're assigned to all users. This wide assignation ensures that all users are protected,
     regardless of whether they use Outlook for iOS and Android.

In addition to the above minimum policy requirements, you should consider deploying
advanced protection policy settings like Restrict cut, copy, and paste with other apps to
further prevent corporate data leakage. For more information on the available settings, see
Android app protection policy settings in Microsoft Intune and iOS app protection policy
settings.

  ） Important

  To apply Intune app protection policies against apps on Android devices that are not
  enrolled in Intune, the user must also install the Intune Company Portal. For more
  information, see Android app protection policy settings in Microsoft Intune.

Enable hybrid Modern Authentication

<!-- p.1383 -->

1. If you haven't enabled hybrid Modern Authentication, review the prerequisites as outlined
  in Hybrid Modern Authentication overview and prerequisites for using it with on-premises
  Skype for Business and Exchange servers. After you complete the prerequisites, do the
  steps in How to configure Exchange Server on-premises to use hybrid Modern
  Authentication.

2. Create an Exchange on-premises device access allow rule to allow Exchange Online to
  connect to your on-premises environment using the ActiveSync protocol:

    PowerShell

    If ((Get-ActiveSyncOrganizationSettings).DefaultAccessLevel -ne "Allow")
    {New-ActiveSyncDeviceAccessRule -Characteristic DeviceType -QueryString
    "OutlookService" -AccessLevel Allow}

    ７ Note

    Device management through the on-premises Exchange admin center is not
    possible. Intune is required to manage mobile devices.

3. Create an Exchange on-premises device access rule that prevents users from connecting
  to the on-premises environment with Outlook for iOS and Android with basic
  authentication over the Exchange ActiveSync protocol:

    PowerShell

    New-ActiveSyncDeviceAccessRule -Characteristic DeviceModel -QueryString
    "Outlook for iOS and Android" -AccessLevel Block

    ７ Note

    Once this rule is created, Outlook for iOS and Android with Basic authentication
    users are blocked.

4. Ensure your on-premises Exchange ActiveSync maxRequestLength is configured to match
  your transport configuration's MaxSendSize/MaxReceiveSize:

       Path: %ExchangeInstallPath%\FrontEnd\HttpProxy\Sync\web.config
       Property: maxRequestLength
       Value: set in KB size (10 MB is 10240, for example)

<!-- p.1384 -->

Client features that aren't supported
The following features aren't supported for on-premises mailboxes using hybrid Modern
Authentication with Outlook for iOS and Android.

     Draft folder and Draft messages synchronization
     Viewing more than four weeks of email by using the "Load More Messages" link at the
     bottom of the message list
     Shared calendar access and delegate calendar access
     Shared and delegate mailbox data access
     Cortana Time to Leave / Travel Time
     Rich meeting locations
     Task management with Microsoft To Do
     Add-ins
     Interesting Calendars
     Play My Emails
     Sensitivity labeling
     S/MIME
     Schedule Send

The following features are only supported when the on-premises infrastructure uses Exchange
Server 2016 and later:

     Calendar attachments

Connection Flow FAQ
Q: My organization has a security policy that requires Internet inbound connections to be
restricted to approved IP addresses or FQDNs. Is that configuration possible with this
architecture?

A: Microsoft recommends that the on-premises endpoints for AutoDiscover and ActiveSync
protocols be opened and accessible from the Internet without any restrictions. In certain
situations that might not be possible. For example, if you're in a coexistence period with
another third-party unified endpoint management (UEM) solution, you might want to place
restrictions on the ActiveSync protocol to prevent users from bypassing the UEM solution while
you migrate to Intune and Outlook for iOS and Android. If you must place restrictions on your
on-premises firewall or gateway edge devices, Microsoft recommends filtering based on FQDN
endpoints. If FQDN endpoints can't be used, then filter on IP addresses. Make sure the
following IP subnets and FQDNs are included on your allowlist:

<!-- p.1385 -->

     All Exchange Online FQDNs and IP subnet ranges as defined in More endpoints not
     included in the Microsoft 365 or Office 365 IP Address and URL Web service.

     The AutoDetect FQDNs and IP subnet ranges defined in Additional endpoints not
     included in the Microsoft 365 or Office 365 IP Address and URL Web service. These IP
     subnets and FQDNs are required because the AutoDetect service establishes connections
     to the on-premises infrastructure.

     All Outlook iOS and Android and Office mobile app FQDNs as defined in Microsoft 365
     and Office 365 URLs and IP address ranges.

Q: My organization currently uses a third-party UEM solution to control mobile device
connectivity. Exposing the Exchange ActiveSync namespace on the Internet introduces a way
for users to bypass the third-party UEM solution during the coexistence period. How can I
prevent this situation?

A: There are three potential solutions to resolving this issue:

   1. Implement Exchange mobile device access rules to control which devices are approved to
     connect.
   2. Some third-party UEM solutions integrate with Exchange mobile device access rules,
     blocking unapproved access, while adding approved devices in the user's
     ActiveSyncAllowedDeviceIDs property.
   3. Implement IP restrictions on the Exchange ActiveSync namespace.

Q: Can I use Azure ExpressRoute for managing traffic between the Microsoft Cloud and my on-
premises environment?

A: Connectivity to the Microsoft Cloud requires Internet connectivity. Microsoft recommends
exposing AutoDiscover and Exchange ActiveSync directly to the Internet; for more information,
see Microsoft 365 and Office 365 Network Connectivity Principles. However, Azure
ExpressRoute is supported for Exchange hybrid scenarios. For more information, see Azure
ExpressRoute for Microsoft 365 and Office 365.

With ExpressRoute, there's no private IP space for ExpressRoute connections, nor can there be
"private" DNS resolution. Any endpoint that your company wants to use over ExpressRoute
must resolve in public DNS. If that endpoint resolves to an IP that's contained in the advertised
prefixes associated with the ExpressRoute circuit (your company must configure those prefixes
in the Azure portal when you enable Microsoft peering on the ExpressRoute connection), the
outbound connection from Exchange Online to your on-premises environment is routed
through the ExpressRoute circuit. Your company needs to ensure that the return traffic
associated with these connections goes through the ExpressRoute circuit (avoiding asymmetric
routing).

<!-- p.1386 -->

  ） Important

  Because Outlook for Android, iOS, and Mac are unable to support Azure ExpressRoute
  (and mobile native mail clients as well), we do not recommend using Azure ExpressRoute
  if you are planning to access your email on a mobile or Mac device. This is because there
  cannot be any overlaps of the public IP space advertised to Microsoft on the ExpressRoute
  circuit and the public IP space advertised on your Internet circuit(s).

Q: Given only four weeks of message data are synchronized to Exchange Online, does this
mean that search queries executed in Outlook for iOS and Android can't return information
beyond the data available on the local device?

A: When a search query is performed in Outlook for iOS and Android, items that match the
search query are returned if they're located on the device. In addition, the search query is
passed to Exchange on-premises via Exchange Online. Exchange on-premises executes the
search query against the on-premises mailbox and returns the results to Exchange Online,
which relays the results to the client. The on-premises query results are stored in Exchange
Online for one day before being deleted.

Q: How do I know that the email account is added correctly in Outlook for iOS and Android?

A: On-premises mailboxes that are added via hybrid Modern Authentication are labeled as
Exchange (Hybrid) in the account settings in Outlook for iOS and Android, similar to the
following example:

<!-- p.1387 -->

Authentication FAQ
Q: What identity configurations are supported with hybrid Modern Authentication and Outlook
for iOS and Android?

A: The following identity configurations with Microsoft Entra ID are supported with hybrid
Modern Authentication:

     Federated Identity with any on-premises identity provider that is supported by Microsoft
     Entra ID
     Password Hash Synchronization via Microsoft Entra Connect
     Pass-through Authentication via Microsoft Entra Connect

Q: What authentication mechanism is used for Outlook for iOS and Android? Are credentials
stored in Microsoft 365 or Office 365?

A: See Account setup with modern authentication in Exchange Online.

<!-- p.1388 -->

Q: Do Outlook for iOS and Android and other Microsoft Office mobile apps support single
sign-on?

A: See Account setup with modern authentication in Exchange Online.

Q: What is the lifetime of the tokens generated and used by the Active Directory
Authentication Library (ADAL) in Outlook for iOS and Android?

A: See Account setup with modern authentication in Exchange Online.

Q: What happens to the access token when a user's password is changed?

A: See Account setup with modern authentication in Exchange Online.

Q: Is there a way for a user to bypass AutoDetect when adding their account to Outlook for iOS
and Android?

A: Yes, a user can bypass AutoDetect at any time and manually configure the connection using
Basic authentication over the Exchange ActiveSync protocol. To ensure that the user doesn't
establish a connection to your on-premises environment via a mechanism that doesn't support
Microsoft Entra Conditional Access or Intune app protection policies, the on-premises
Exchange Administrator needs to configure an Exchange device access rule that blocks the
ActiveSync connection. To do this task, type the following command in the Exchange
Management Shell:

  PowerShell

  New-ActiveSyncDeviceAccessRule -Characteristic DeviceModel -QueryString "Outlook
  for iOS and Android" -AccessLevel Block

Q: What happens when an organization moves from basic authentication with Outlook for iOS
and Android to hybrid Modern authentication?

A: After an organization enables hybrid modern authentication following the above
Implementation steps, end users need to delete their existing account profile in Outlook for
iOS and Android as the profile uses basic authentication. End users can then create a new
profile which uses hybrid Modern authentication.

Troubleshooting
This section describes the most common issues or errors with on-premises mailboxes using
hybrid Modern Authentication with Outlook for iOS and Android.

<!-- p.1389 -->

AutoDiscover and ActiveSync
During profile creation, the user should be presented a Modern Authentication dialog similar
to the one in the following screenshot:

If, instead, the user is presented with one of the following dialogs, then there's an issue with
either the Autodiscover or ActiveSync on-premises endpoints.

Here's an example of a user being presented with the legacy Basic authentication Exchange
ActiveSync experience:

<!-- p.1390 -->

And here's an example of what users see when AutoDetect isn't able to discover the
configuration for users' on-premises mailboxes.

<!-- p.1391 -->

In either scenario, verify that your on-premises environment is correctly configured. To do this
task: from the TechNet Gallery, download and execute the script for Validating Hybrid Modern
Authentication setup for Outlook for iOS and Android     .

When you review the output from the script, you should be seeing the following output from
AutoDiscover:

  JSON

  {
         "Protocol": "activesync",
         "Url": "https://mail.contoso.com/Microsoft-Server-ActiveSync"
  }

The on-premises ActiveSync endpoint should return the following response, where the WWW-
Authenticate header includes an authorization_uri:

<!-- p.1392 -->

  Console

  Content-Length →0
  Date →Mon, 29 Jan 2018 19:51:46 GMT
  Server →Microsoft-IIS/10.0 Microsoft-HTTPAPI/2.0
  WWW-Authenticate →Bearer client_id="00000002-0000-0ff1-ce00-000000000000",
  trusted_issuers="00000001-0000-0000-c000-000000000000@5de110f8-2e0f-4d45-891d-
  bcf2218e253d,00000004-0000-0ff1-ce00-000000000000@contoso.com",
  token_types="app_asserted_user_v1 service_asserted_app_v1",
  authorization_uri="https://login.windows.net/common/oauth2/authorize"
  Www-Authenticate →Basic realm="mail.contoso.com"
  X-Powered-By →ASP.NET
  request-id →5ca2c827-5147-474c-8457-63c4e5099c6e

If the AutoDiscover or ActiveSync responses aren't similar to the above examples, you can
investigate the following causes to be the possible ones:

   1. If the AutoDiscover endpoint can't be reached, then it's likely there's a firewall or load
     balancer configuration issue (for example, IP restrictions are configured and the required
     IP ranges aren't present). Also, there might be a device in front of Exchange requiring pre-
     authentication to access the AutoDiscover endpoint.

   2. If the AutoDiscover endpoint doesn't return the correct URL, then there's a configuration
     issue with the ActiveSync virtual directory's ExternalURL value.

   3. If the ActiveSync endpoint can't be reached, then there's a firewall or load balancer
     configuration issue. Again, one example is IP restrictions are configured and the required
     IP ranges aren't present. Also, there might be a device in front of Exchange requiring pre-
     authentication to access the ActiveSync endpoint.

   4. If the ActiveSync endpoint doesn't contain an authorization_uri value, verify that the
     EvoSTS authentication server is configured as the default endpoint using Exchange
     Management Shell:

        PowerShell

        Get-AuthServer EvoSts | Format-List IsDefaultAuthorizationEndpoint

   5. If the ActiveSync endpoint doesn't contain a WWW-Authenticate header, then a device in
     front of Exchange might be responding to the query.

Client synchronization issues
There are a few scenarios that can result in data being stale in Outlook for iOS and Android.
Typically, this data condition is due to an issue with the second access token (the token used by

<!-- p.1393 -->

MRS in Exchange Online to synchronize the data with the on-premises environment). The two
most common reasons for this issue are:

     SSL/TLS offloading on-premises.
     EvoSTS certificate metadata issues.

With SSL/TLS offloading, tokens are issued for a specific uri and that value includes the
protocol value ("https://"). When the load balancer offloads SSL/TLS, the request received by
Exchange comes in via HTTP, resulting in a claim mismatch due to the protocol value being
http://. The following example depicts a response header from a Fiddler trace:

  Console

  Content-Length →0
  Date →Mon, 29 Jan 2018 19:51:46 GMT
  Server →Microsoft-IIS/10.0 Microsoft-HTTPAPI/2.0
  WWW-Authenticate →Bearer client_id="00000002-0000-0ff1-ce00-000000000000",
  trusted_issuers="00000001-0000-0000-c000-000000000000@00c118a9-2de9-41d3-b39a-
  81648a7a5e4d",
  authorization_uri="https://login.windows.net/common/oauth2/authorize",
  error="invalid_token"
  WWW-Authenticate →Basic realm="mail.contoso.com"
  X-Powered-By →ASP.NET
  request-id →2323088f-8838-4f97-a88d-559bfcf92866
  x-ms-diagnostics →2000003;reason="The hostname component of the audience claim
  value is invalid. Expected 'https://mail.contoso.com'. Actual
  'http://mail.contoso.com'.";error_category="invalid_resource"

As specified above in the section Technical and licensing requirements, SSL/TLS offloading isn't
supported for OAuth flows.

For EvoSTS Certificate Metadata, the certificate metadata used by EvoSTS is occasionally
updated in Microsoft 365 or Office 365. The Exchange on-premises arbitration mailbox that has
the organization capability of "OrganizationCapabilityManagement" is responsible for
detecting the changes and for updating the corresponding metadata on-premises; this process
executes every eight hours.

Exchange Administrators can find this mailbox by executing the following cmdlet using
Exchange Management Shell:

  PowerShell

  $x=Get-mailbox -arbitration | ? {$_.PersistedCapabilities -like
  "OrganizationCapabilityManagement"};Get-MailboxDatabaseCopyStatus $x.database.name

<!-- p.1394 -->

On the server hosting the database for the OrganizationCapabilityManagement arbitration
mailbox, review the application event logs for events with a source of MSExchange
AuthAdmin. The events should tell you if Exchange can refresh the metadata. If the metadata is
out of date, you can manually refresh it with this cmdlet:

  PowerShell

  Set-AuthServer EvoSts -RefreshAuthMetadata

You can also create a scheduled task that executes the above command every 24 hours.

Exchange Online statistics
You can use the following Exchange Online cmdlets to see statistical information for each
synchronized on-premises mailbox.

   1. First, obtain the location of the synchronized on-premises mailbox in the tenant,
     specifying the on-premises mailbox's identity (for example, jane@contoso.com ).

        PowerShell

        $m = Get-MailboxLocation <identity>

   2. To see mailbox-related statistics, use

        PowerShell

        Get-MailboxStatistics $m.id

   3. To see mobile device statistics (like seeing when Outlook for iOS and Android last
     synchronized to Exchange Online), use

        PowerShell

        Get-MobileDeviceStatistics -Mailbox $m.id

For more information, see Get-MailboxStatistics and Get-MobileDeviceStatistics.

Other issues
There are other issues that might prevent hybrid Modern Authentication from functioning
correctly. For more information, see the troubleshooting section in Announcing Hybrid Modern

<!-- p.1395 -->

Authentication for Exchange On-Premises   .

<!-- p.1396 -->

Using Basic authentication with Outlook for
iOS and Android
Article • 04/30/2025

APPLIES TO:        2016      2019    Subscription Edition

The Outlook app for iOS and Android is designed to bring together email, calendar, contacts,
and other files, enabling users in your organization to do more from their mobile devices. This
article provides an overview of the architecture and the storage design of the app, so that
Exchange administrators can deploy and maintain Outlook for iOS and Android in their
Exchange organizations.

  ７ Note

  This article is about using the app in an Exchange 2010, Exchange 2013, Exchange 2016 or
  Exchange 2019 environment where hybrid modern authentication is not enabled. For
  more information about using hybrid Modern Authentication for on-premises mailboxes
  with the app, see Using hybrid Modern Authentication with Outlook for iOS and
  Android. For information about using the app with Exchange Online, see Outlook for iOS
  and Android in Exchange Online.

Outlook for iOS and Android architecture
Outlook for iOS and Android is a cloud-backed application. This characteristic means your
experience consists of a locally installed app powered by a secure and scalable service running
in the Microsoft Cloud.

For Exchange Server mailboxes, Outlook for iOS and Android's architecture is built directly into
the Microsoft Cloud. This layout of the architecture provides customers the extra benefits of
security, privacy, built-in compliance, and transparent operations that Microsoft commits to in
the Microsoft Trust Center    .

The following environments will take advantage of this Microsoft 365 or Office 365-based
architecture:

      In Exchange Server 2010 environments

      When a hybrid relationship between Exchange 2013, 2016, or 2019 on-premises and
      Microsoft 365 or Office 365 hasn't been configured

<!-- p.1397 -->

     When hybrid Modern Authentication hasn't been enabled between Exchange 2013, 2016,
     or 2019 on-premises and Microsoft 365 or Office 365

Within the Microsoft 365 or Office 365-based architecture, Outlook for iOS and Android utilizes
the native Microsoft sync technology for data synchronization that is protected by TLS-secured
connections end-to-end, between Microsoft 365 or Office 365 and the app.

The Exchange ActiveSync (EAS) connection between Exchange Online and the on-premises
environment enables synchronization of the users' on-premises data and includes four weeks
of email, all calendar data, all contact data, and out-of-office status. The region in which this
data is synchronized into depends on the IP address in use by the mobile device at the time
synchronization is set up. If you have a hybrid setup with an Exchange Online tenant, the on-
premises data is not synchronized into your tenant; instead, the data is synchronized into
Outlook.com in the same way as if you had an Exchange Server without hybrid. If you want to
control and manage your on-premises data from within your tenant, you need to enable hybrid
Modern Authentication with Outlook for iOS and Android.

Data synchronization between the Exchange on-premises environment and Exchange Online
happens independent of user behavior. This characteristic ensures that new messages are
delivered to the devices quickly. For more information on how the user authentication model
enables data synchronization independently of user behavior, see Passwords and security in
Outlook for iOS and Android for Exchange Server.

Processing information in the Microsoft Cloud enables advanced features and capabilities, such
as the categorization of email for the Focused Inbox, customized experience for travel and
calendar, and improved search speed. Relying on the cloud for intensive processing and
minimizing the resources required from users' devices enhances the app's performance and
stability. Lastly, it allows Outlook to build features that work across all email accounts,
regardless of the technological capabilities of the underlying servers (such as different versions
of Exchange Server, Microsoft 365, or Office 365).

  ） Important

<!-- p.1398 -->

  On-premises mailboxes using basic authentication with Outlook for iOS and Android do
  not support Enterprise Mobility + Security features such as Microsoft Entra Conditional
  Access and Intune app protection policies. For support with these technologies, see Using
  hybrid Modern Authentication with Outlook for iOS and Android.

Data security, access, and auditing controls
With on-premises data being synchronized with Exchange Online, customers have questions
about how the data is protected in Exchange Online. The white paper Encryption in the
Microsoft Cloud discusses how BitLocker is used for volume-level encryption.

By default, Microsoft engineers have zero standing administrative privileges and zero standing
access to customer content in Microsoft 365 and Office 365. The white paper Administrative
Access Controls in Microsoft 365 discusses personnel screening, background checks, Lockbox
and Customer Lockbox, and more.

ISO Audited Controls on Service Assurance     documentation provides the status of audited
controls from global information security standards and regulations that Microsoft 365 and
Office 365 have implemented.

Connectivity Requirements
Microsoft recommends that the on-premises endpoints for AutoDiscover and ActiveSync
protocols be opened and accessible from the Internet without any restrictions. In certain
situations that may not be possible. If you must place restrictions on your on-premises firewall
or gateway edge devices, Microsoft recommends filtering based on FQDN endpoints. If FQDN
endpoints cannot be used, then filter on IP addresses. Make sure the following IP subnets and
FQDNs are included in your allowlist:

     All Exchange Online FQDNs and IP subnet ranges as defined in Microsoft 365 and Office
     365 URLs and IP address ranges.

     The AutoDetect FQDNs and IP subnet ranges defined in More Microsoft 365 or Office 365
     IP Addresses and URLs not included in the web services. These ranges are required
     because the AutoDetect service establishes connections to the on-premises infrastructure.

     All Outlook iOS and Android and Office mobile app FQDNs as defined in Microsoft 365 or
     Office 365 URLs and IP address ranges.

Client features that aren't supported

<!-- p.1399 -->

The following features aren't support for on-premises mailboxes using basic authentication
with Outlook for iOS and Android:

     Draft folder and Draft messages synchronization

     Shared calendar access and Delegate calendar access

     Shared and delegate mailbox data access

     Cortana Time to Leave / Travel Time

     Rich meeting locations

     Task management with Microsoft To-Do

     Favorite People with Notifications

     Add-ins

     Interesting Calendars

     Avatar support

     Play My Emails

     S/MIME

     Sensitivity labeling

     Discover Feed

     Privacy settings

The following features are only supported when the on-premises infrastructure uses Exchange
Server 2016 and later:

     Calendar attachments

<!-- p.1400 -->

Account setup in Outlook for iOS and
Android using Basic authentication
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Outlook for iOS and Android offers Exchange administrators the ability to "push" account
configurations to their on-premises users who use Basic authentication with the ActiveSync
protocol. This capability works with any Unified Endpoint Management (UEM) provider who
uses the Managed App Configuration       channel for iOS or the Android in the Enterprise
channel for Android.

For on-premises users enrolled in Microsoft Intune, you can deploy the account configuration
settings using Intune in the Azure portal.

Once an account configuration is created and the user enrolls their device, Outlook for iOS and
Android detects that an account is "Found" and prompts the user to add the account. The only
information the user needs to enter to complete the setup process is their password. Then, the
user's mailbox content loads and the user can begin using the app.

The following images show an example of the end-user setup process after Outlook for iOS
and Android was configured in Intune.
