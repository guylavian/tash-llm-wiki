---
title: "Exchange Server — pages 1321-1360"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1321-1360
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1321-1360
family: exchange
documentKind: "doc"
abstract: "Setting Description Allow Desktop Sync This setting specifies whether the mobile device can synchronize with a computer through a cable, Bluetooth, or IrDA connection. The default value is $true . Allow External Device This setting specifies whether an external device management"
---

# Exchange Server — pages 1321-1360

<!-- p.1321 -->

Setting                 Description

Allow Desktop Sync      This setting specifies whether the mobile device can synchronize with a computer
                        through a cable, Bluetooth, or IrDA connection. The default value is $true .

Allow External Device   This setting specifies whether an external device management program is allowed
Management              to manage the mobile device.

Allow HTML Email        This setting specifies whether email synchronized to the mobile device can be in
                        HTML format. If this setting is set to $false , all email is converted to plain text.

Allow Internet          This setting specifies whether the mobile device can be used as a modem for a
Sharing                 desktop or a portable computer. The default value is $true .

AllowIrDA               This setting specifies whether infrared connections are allowed to and from the
                        mobile device.

Allow Mobile OTA        This setting specifies whether the mobile device mailbox policy settings can be
Update                  sent to the mobile device over a cellular data connection. The default value is
                        $true .

Allow non-              This setting specifies whether mobile devices that may not support application of
provisionable devices   all policy settings are allowed to connect to Exchange Server by using Exchange
                        ActiveSync. Allowing non-provisionable mobile devices has security implications.
                        For example, some non-provisionable devices may not be able to implement an
                        organization's password requirements.

Allow POPIMAPEmail      This setting specifies whether the user can configure a POP3 or an IMAP4 email
                        account on the mobile device. The default value is $true . This setting doesn't
                        control access by third-party email programs.

Allow Remote            This setting specifies whether the mobile device can initiate a remote desktop
Desktop                 connection. The default value is true .

Allow simple            This setting enables or disables the ability to use a simple password such as 1111
password                or 1234. The default value is $true .

Allow S/MIME            This setting specifies whether the messaging application on the mobile device
encryption algorithm    can negotiate the encryption algorithm if a recipient's certificate doesn't support
negotiation             the specified encryption algorithm.

Allow S/MIME            This setting specifies whether S/MIME software certificates are allowed on the
software certificates   mobile device.

Allow storage card      This setting specifies whether the mobile device can access information that's
                        stored on a storage card.

Allow text messaging    This setting specifies whether text messaging is allowed from the mobile device.
                        The default value is $true .

<!-- p.1322 -->

Setting                 Description

Allow unsigned          This setting specifies whether unsigned applications can be installed on the
applications            mobile device. The default value is $true .

Allow unsigned          This setting specifies whether an unsigned installation package can be run on the
installation packages   mobile device. The default value is $true .

Allow Wi-Fi             This setting specifies whether wireless Internet access is allowed on the mobile
                        device. The default value is $true .

Alphanumeric            This setting requires that a password contains numeric and non-numeric
password required       characters. The default value is $true .

Approved                This setting stores a list of approved applications that can be run on the mobile
Application List        device.

Attachments enabled     This setting enables attachments to be downloaded to the mobile device. The
                        default value is $true .

Device encryption       This setting enables encryption on the mobile device. Not all mobile devices can
enabled                 enforce encryption. For more information, see the device and mobile operating
                        system documentation.

Device policy refresh   This setting specifies how often the mobile device mailbox policy is sent from the
interval                server to the mobile device.

IRM enabled             This setting specifies whether Information Rights Management (IRM) is enabled
                        on the mobile device.

Max attachment size     This setting controls the maximum size of attachments that can be downloaded
                        to the mobile device. The default value is Unlimited.

Max calendar age        This setting specifies the maximum range of calendar days that can be
filter                  synchronized to the mobile device. The following values are accepted:
                        1: All
                        2: OneDay
                        3: ThreeDays
                        4: OneWeek
                        5: TwoWeeks
                        6: OneMonth

Max email age filter    This setting specifies the maximum number of days of email items to synchronize
                        to the mobile device. The following values are accepted:
                        1: All
                        2: OneDay
                        3: ThreeDays
                        4: OneWeek
                        5: TwoWeeks
                        6: OneMonth

<!-- p.1323 -->

Setting                Description

Max email body         This setting specifies the maximum size at which email messages are truncated
truncation size        when synchronized to the mobile device. The value is in kilobytes (KB).

Max email HTML         This setting specifies the maximum size at which HTML email messages are
body truncation size   truncated when synchronized to the mobile device. The value is in kilobytes (KB).

Max inactivity time    This value specifies the length of time that the mobile device can be inactive
lock                   before a password is required to reactivate it. You can enter any interval between
                       30 seconds and 1 hour. The default value is 15 minutes.

Max password failed    This setting specifies the number of attempts a user can make to enter the
attempts               correct password for the mobile device. You can enter any number from 4
                       through 16. The default value is 8.

Min password           This setting specifies the number of character sets that are required in the
complex characters     password of the mobile device. The character sets are:
                             Lower case letters.
                             Upper case letters.
                             Digits 0 through 9.
                             Special characters (for example, exclamation marks).

                       You can enter any number from 1 through 4. The default value is 1.

Min password length    This setting specifies the minimum number of characters in the mobile device
                       password. You can enter any number from 1 through 16. The default value is 4.

Password enabled       This setting enables the mobile device password.

Password expiration    This setting enables the administrator to configure a length of time after which a
                       mobile device password must be changed.

Password history       This setting specifies the number of past passwords that can be stored in a user's
                       mailbox. A user can't reuse a stored password.

Password recovery      When this setting is enabled, the mobile device generates a recovery password
enabled                that's sent to the server. If the user forgets their mobile device password, the
                       recovery password can be used to unlock the mobile device and enable the user
                       to create a new mobile device password.

Require device         This setting specifies whether device encryption is required. If set to $true , the
encryption             mobile device must be able to support and implement encryption to synchronize
                       with the server.

Require encrypted      This setting specifies whether S/MIME messages must be encrypted. The default
S/MIME messages        value is $false .

Require encryption     This setting specifies what required algorithm must be used when encrypting

<!-- p.1324 -->

Setting                 Description

S/MIME algorithm        S/MIME messages.

Require manual          This setting specifies whether the mobile device must synchronize manually while
synchronization while   roaming. Allowing automatic synchronization while roaming will frequently lead
roaming                 to larger-than-expected data costs for the mobile device data plan.

Require signed          This setting specifies what required algorithm must be used when signing a
S/MIME algorithm        message.

Require signed          This setting specifies whether the mobile device must send signed S/MIME
S/MIME messages         messages.

Require storage card    This setting specifies whether the storage card must be encrypted. Not all mobile
encryption              device operating systems support storage card encryption. For more information,
                        see your mobile device and mobile operating system documentation.

Unapproved InROM        This setting specifies a list of applications that cannot be run in ROM.
application list

<!-- p.1325 -->

Mobile devices in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

There are many different mobile phones and devices enabled for Exchange ActiveSync. These
include Android phones and tablets, as well as the Apple iPhone, iPod, and iPad.

Both phone and non-phone mobile devices support Exchange ActiveSync, and in most
Exchange ActiveSync documentation, we use the term mobile device. Unless the feature or
features we're discussing require a cellular telephone signal, such as SMS message notification,
the term mobile device applies to both mobile phones and other mobile devices such as
tablets.

What Exchange ActiveSync does
Exchange ActiveSync is a communications protocol that enables over-the-air mobile access to
email messages, scheduling data, contacts, and tasks. Exchange ActiveSync is available on
third-party phones that are enabled for Exchange ActiveSync.

Exchange ActiveSync offers Direct Push technology. Direct Push uses an encrypted HTTPS
connection that's established and maintained between the mobile device and the server to
push new email messages and other Exchange data to the phone.

To use Direct Push with Microsoft Exchange Server 2013, your users must have a mobile device
that's designed to support Direct Push.

Exchange ActiveSync features
Exchange ActiveSync provides access to many different features that enable you to enforce
security policies on mobile devices. By using Exchange 2013, you can configure multiple mobile
device mailbox policies and control which mobile devices can synchronize with your Exchange
server. Exchange ActiveSync enables you to send a remote device wipe command that wipes all
data from a mobile device in case that mobile device is lost or stolen. Users can also initiate a
remote device wipe from Outlook Web App.

Exchange ActiveSync lets users generate a recovery password. This recovery password is saved
on the mobile device and is used when a user forgets their password. The user generates the
recovery password at the same time that they generate the device password or PIN. This
recovery password can be used to unlock the mobile device. Immediately after this recovery
password is used, the user will be required to create a new PIN.

<!-- p.1326 -->

POP3 and IMAP4 limitations
If your mobile device doesn't support Exchange ActiveSync, or you don't need the rich feature
set that Exchange ActiveSync provides, you can use POP3 or IMAP4 to access your email on
your mobile device. For more information about POP3 and IMAP4 access to your mailbox, see
POP3 and IMAP4 in Exchange Server.

<!-- p.1327 -->

Configure mobile phones to access email
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

This article is about enabling users in your organization to access their Exchange 2016 or
Exchange 2019 mailboxes with their mobile devices using Exchange ActiveSync.

Prerequisites
      You've reviewed the manufacturer's documentation for the mobile phone you want to
      configure.

      Exchange ActiveSync is enabled in your organization.

  ７ Note

  For device-specific information about setting up Exchange-based email on a phone or
  tablet, see Set up Office apps and email on a mobile device     .

Configure a mobile phone or device to use
Exchange ActiveSync
Most mobile phones and devices are capable of using Autodiscover in Exchange to configure
the mobile email client to use Exchange ActiveSync. To configure an email account on most
mobile devices, you'll need two pieces of information.

      The user's email address

      The user's password

If the mobile phone is unable to contact the Exchange server automatically through the
Autodiscover service, you'll need to set up the mobile phone manually. Manual setup requires
the user's email address and password, as well as the Exchange ActiveSync server name. In
most organizations, the Exchange ActiveSync server name is the same as the Outlook on the
web server name without the /owa, for example, mail.contoso.com.

<!-- p.1328 -->

Perform a remote wipe on a mobile phone
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Your users carry sensitive corporate information in their pockets every day. If one of them loses
their mobile phone, your data can end up in the hands of another person. If one of your users
loses their mobile phone, you can use the Exchange admin center (EAC) or the Exchange
Management Shell to wipe their phone clean of all corporate and user information.

  ７ Note

  This topic also provides instructions for how to use Outlook on the web to perform a
  remote wipe on a phone. The user must be signed in to Outlook on the web to perform a
  remote wipe.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mobile devices" entry in the
      Clients and mobile devices permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

  ７ Note

  Prior to EAS v16.1, remote wipe would perform a device-level wipe, restoring the device to
  factory conditions. With EAS v16.1 and later, EAS also supports account-only remote wipe.
  In order for this to work, the client must support the EAS v16.1 protocol. If the client
  doesn't support v16.1, the wipe will fail and an error will be given.

  Ｕ Caution

  Exchange ActiveSync v16.1 supports two different remote wipe processes: A Wipe Data
  remote wipe and also an Account Only Remote Wipe Device remote wipe. There are
  important differences between how Outlook responds and how native mail apps on iOS
  and Android respond to these different wipe commands.

<!-- p.1329 -->

  Outlook for iOS and Outlook for Android support only the Wipe Data command, which
  wipes only data within Outlook. The Outlook app will reset and all Outlook email,
  calendar, contacts, and file data will be removed, but no other data is wiped from the
  device. The Account Only Remote Wipe Device command is therefore redundant and is
  not supported by Outlook for iOS or Android.

  However, if a native iOS or Android mail app is connected to Exchange and receives a
  Wipe Data command from Exchange ActiveSync, all data on the device will be wiped,
  including photos, personal files, and so on.

  If a native iOS or Android mail app is connected to Exchange and receives an Account
  Only Remote Wipe Device command from Exchange ActiveSync, only the native mail
  app's Exchange ActiveSync mail, calendar, and account data are wiped.

  These commands are designed to destroy data. Exercise caution when using them.

After the remote wipe command is requested by the administrator, the wipe happens within
seconds of the Outlook app's next connection to Exchange.

Since Outlook for iOS and Android appears as a single mobile device association under a user's
mobile devices in Exchange, a remote wipe command will remove data and delete sync
relationships from all devices running Outlook (iPhone, iPad, Android) associated with that
user.

A remote wipe action deletes the synchronization profile, so when the user adds his or her
account to Outlook for iOS and Android, a new Device ID is generated and reported to
Exchange on-premises.

  ７ Note

  If you are using Intune, you should be using Intune to trigger data removal, not Exchange.
  Depending on the scenario, it could be accomplished via App Protection Policy selective
  wipe, or Device enrollment retire/wipe commands.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Use the EAC to wipe a user's phone

<!-- p.1330 -->

You can use the EAC to wipe a user's phone or cancel a remote wipe that has not yet
completed.

   1. In the EAC, navigate to Recipients > Mailboxes.

   2. Select the user, and under Mobile Devices, choose View details.

   3. On the Mobile Device Details page, select the lost mobile device, and then select Wipe
     Data (or Account Only Remote Wipe Device if desired).

   4. Select Save.

Use the Exchange Management Shell to wipe a
user's phone
You can use the Clear-MobileDevice cmdlet in the Exchange Management Shell to wipe a
user's phone.

The following command wipes the device named WM_TonySmith and sends a confirmation
message to admin@contoso.com.

  PowerShell

  Clear-MobileDevice -Identity WM_TonySmith -NotificationEmailAddresses
  "admin@contoso.com"

If the device connects to Exchange using a mail app other than Outlook, you can use the
following command to wipe only the mail app's Exchange ActiveSync mail, calendar, and
account data and leave all other data on the device intact:

  PowerShell

  Clear-MobileDevice -AccountOnly -Identity WM_TonySmith -NotificationEmailAddresses
  "admin@contoso.com"

The -AccountOnly switch has no effect on Outlook devices because an account-only remote
wipe is the only type of wipe that is supported by Outlook. See Clear-MobileDevice for more
information.

Use Outlook on the web to wipe a user's phone
Your users can use Outlook on the web to wipe their own phones.

<!-- p.1331 -->

   1. In Outlook on the web, select the Settings icon.

   2. Under Your app settings, select Mail.

   3. Under Options, click to expand General if necessary, and then select Mobile devices.

   4. Select the mobile phone.

   5. Click or tap the Wipe Device icon (or the Account Only Remote Wipe Device icon if
     desired).

Use the New Outlook on the web to wipe a user's
phone
   1. In Outlook on the web, select the Settings icon.

   2. Click on View All Outlook settings.

   3. Click General, and then select Mobile devices.

   4. Select the mobile phone.

   5. Click or tap the Wipe Device icon (or the Account Only Remote Wipe Device icon if
     desired).

How do you know this worked?
There are several ways to verify that the remote wipe completed.

     Run the Clear-MobileDevice cmdlet with the -NotificationEmailAddresses parameter
     configured. A message will be sent to the supplied email address when the remote wipe
     has completed.

     In the EAC, check the status of the mobile device. The status will change from Wipe
     Pending to Wipe Successful.

     In Outlook on the web, check the status of the mobile device. The status will change from
     Wipe Pending to Wipe Successful.

  ７ Note

<!-- p.1332 -->

In a Microsoft 365 or Office 365-based environment, the result of a remote device wipe is
not reported back to Exchange. Even when the wipe is successful, the status will display as
Pending.

<!-- p.1333 -->

POP3 and IMAP4 in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Although users typically access their Exchange mailboxes by using Outlook (MAPI), Outlook on
the web (formerly known as Outlook Web App), and Exchange ActiveSync, POP3 and IMAP4
are available in Exchange Server 2016 and Exchange Server 2019. To support clients that still
rely on these protocols, you need to start the services, and configure the settings for POP3 and
IMAP4. For detailed instructions, see the following topics:

      Enable and configure POP3 on an Exchange server

      Enable and configure IMAP4 on an Exchange server

      Configure authenticated SMTP settings for POP3 and IMAP4 clients in Exchange Server

After you enable and configure POP3 or IMAP4 on the Exchange server, you can enable or
disable POP3 or IMAP4 access to specific mailboxes. For more information, see Enable or
disable POP3 or IMAP4 access to mailboxes in Exchange Server.

Note: Clients connect to the POP3 and IMAP4 services in the Client Access (frontend) services
on the Mailbox server. They never connect directly to the POP3 and IMAP4 backend services.
For more information, see Client access protocol architecture.

POP3 and IMAP4 improvements in Exchange
Server
POP3 and IMAP4 functionality in Exchange 2016 and Exchange 2019 is basically unchanged
from Exchange 2013. These are the improvements in POP3 and IMAP4 as compared to
Exchange 2010:

      By default, the Client Access (frontend) services in Exchange 2016 and 2019 automatically
      proxy POP3 and IMAP4 client connections from one Active Directory site to the correct
      Mailbox server in a different Active Directory site. In previous versions of Exchange, you
      had to perform a manual configuration step to allow POP3 and IMAP4 clients to connect
      to their mailboxes from one site to another.

      You can't use the Anonymous or Guest accounts to access an Exchange 2016 or Exchange
      2019 mailbox by using POP3 or IMAP4. Access is blocked to prevent security
      vulnerabilities when you use non-standard accounts for POP3 and IMAP4 access.

<!-- p.1334 -->

     You can't connect to the Administrator mailbox by using POP3 or IMAP4 (you can use
     Outlook or Outlook Web App). This limitation was intentionally included in Exchange
     2016 to enhance security for the Administrator mailbox.

Overview of POP3 and IMAP4 functionality
The POP3 and IMAP4 protocols have the following benefits and limitations:

     POP3

         Designed for offline message processing.

         Can only download messages from a single folder (usually the Inbox) in the mailbox to
         a single folder in the POP3 application on the client computer or device.

         By default, downloaded messages are removed from the email server, and are stored
         only on the local computer or device. Therefore, users can't access the same email
         messages from multiple computers or devices (although many POP3 applications can
         be configured to keep copies of downloaded messages in the mailbox on the email
         server).

         Doesn't offer advanced collaboration features such as calendaring, contacts, and tasks.

     IMAP4

         Offers offline and online message processing.

         Can synchronize messages from multiple folders in the mailbox with the client
         computer or device. For example, most IMAP4 applications can be configured to keep
         a copy of sent messages in the mailbox on the email server.

         By default, copies of downloaded messages remain on the email server. Therefore,
         users can access the same messages from multiple computers.

         Supports additional features. For example, you can download the message headers
         (the message's sender and subject) before you decide to download the complete
         message.

         Doesn't offer advanced collaboration features such as calendaring, contacts, and tasks.

Note: POP3 and IMAP4 clients have limited access to Exchange calendar information. For more
information, see Configure Calendar Options for POP3 and Configure Calendar Options for
IMAP4.

<!-- p.1335 -->

POP3 and IMAP4 applications and settings
After you've enabled and configured the required services, users can connect to their Exchange
mailboxes by using any application that support POP3 and IMAP4. For example, Outlook,
Windows Mail, and Mozilla Thunderbird. POP3 and IMAP4 feature support varies by
application, so check the application's documentation.

Verify the POP3 or IMAP4 email program is configured to keep a copy of all messages on the
server. This allows the users to access their messages from different computers or applications.

Another important setting is how frequently the email program contacts the server to send and
receive mail. There are three basic settings:

     Send and receive messages when the application is started

     Send and receive messages manually: Messages are only sent and received when the
     user clicks a "send and receive" option in the application. This is a good setting for
     computers that aren't always connected to the Internet (for example, dial-up or metered
     Internet connections).

     Send and receive messages every set number of minutes: The application connects to
     the email server periodically to send messages and to download any new messages. This
     is a good setting for computers that are always connected to the Internet, because the
     application is kept up-to-date with the most current messages from the mailbox.

Note: If the application and server both support the IMAP4 IDLE command, users can send and
receive messages in near real time (Exchange supports the IMAP4 IDLE command). In most
cases, users don't need to configure any settings in their IMAP4 application to use this
connection method.

To configure a POP3 or IMAP4 client to connect to a mailbox, users need specific information
about the POP3 or IMAP4 settings. By default, Exchange uses the following settings for internal
POP3 connections:

     POP3 server FQDN: <ServerFQDN> . For example, mailbox01.contoso.com .

     TCP port and encryption method: 995 for always SSL/TLS encrypted connections, and
     110 for unencrypted connections, or for opportunistic TLS (STARTTLS) that results in an
     encrypted connection after the initial plain text protocol handshake.

To allow external POP3 clients to connect to mailboxes, you need to configure these settings
for external connections. For more information, see Enable and configure POP3 on an
Exchange server.

<!-- p.1336 -->

By default, Exchange uses the following settings for internal IMAP4 connections:

     IMAP4 server FQDN: <ServerFQDN> . For example, mailbox01.contoso.com .

     TCP port and encryption method: 993 for always SSL/TLS encrypted connections, and
     143 for unencrypted connections, or for opportunistic TLS (STARTTLS) that results in an
     encrypted connection after the initial plain text protocol handshake.

To allow external IMAP4 clients to connect to mailboxes, you need to configure these settings
for external connections. For more information, see Enable and configure IMAP4 on an
Exchange server.

<!-- p.1337 -->

Enable and configure POP3 on an Exchange
server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

By default, POP3 client connectivity isn't enabled in Exchange. To enable POP3 client
connectivity, you need to perform the following steps:

   1. Start the POP3 services, and configure the services to start automatically:

            Microsoft Exchange POP3: This is the Client Access (frontend) service that POP3
            clients connect to.

            Microsoft Exchange POP3 Backend: POP3 client connections from the Client Access
            service are proxied to the backend service on the server that holds the active copy
            of the user's mailbox. For more information, see Client Access protocol architecture.

   2. Configure the POP3 settings for external clients.

      By default, Exchange uses the following settings for internal POP3 connections:

            POP3 server FQDN: <ServerFQDN> . For example, mailbox01.contoso.com .

            TCP port and encryption method: 995 for always TLS encrypted connections, and
            110 for unencrypted connections, or for opportunistic TLS (STARTTLS) that results in
            an encrypted connection after the initial plain text protocol handshake.

      To allow external POP3 clients to connect to mailboxes, you need to configure the POP3
      server FQDN, TCP port, and encryption method for external connections. This step causes
      the external POP3 settings to be displayed in Outlook on the web (formerly known as
      Outlook Web App) at Settings > Options > Mail > Accounts > POP and IMAP.

<!-- p.1338 -->

  3. Restart the POP3 services to save the changes.

  4. Configure the authenticated SMTP settings for internal and external clients. For more
     information, see Configure authenticated SMTP settings for POP3 and IMAP4 clients in
     Exchange Server.

For more information about POP3, see POP3 and IMAP4 in Exchange Server.

What do you need to know before you begin?
     Estimated time to complete each procedure: 5 minutes.

     Secure Sockets Layer (SSL) is being replaced by Transport Layer Security (TLS) as the
     protocol that's used to encrypt data sent between computer systems. They're so closely
     related that the terms "SSL" and "TLS" (without versions) are often used interchangeably.
     Because of this similarity, references to "SSL" in Exchange topics, the Exchange admin
     center, and the Exchange Management Shell have often been used to encompass both
     the SSL and TLS protocols. Typically, "SSL" refers to the actual SSL protocol only when a
     version is also provided (for example, SSL 3.0). To find out why you should disable the SSL
     protocol and switch to TLS, check out Protecting you against the SSL 3.0 vulnerability .

     To learn how to open the Exchange Management Shell in your on-premises Exchange
     organization, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "POP3 and IMAP4 Permissions"
     section in the Clients and mobile devices permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

<!-- p.1339 -->

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Step 1: Start the POP3 services, and configure the
services to start automatically
You can perform this step by using the Windows Services console, or the Exchange
Management Shell.

Use the Windows Services console to start the POP3 services,
and configure the services to start automatically
  1. On the Exchange server, open the Windows Services console. For example:

          Run the command services.msc from the Run dialog, a Command Prompt window,
          or the Exchange Management Shell.

          Open Server Manager, and then click Tools > Services.

  2. In the list of services, select Microsoft Exchange POP3, and then click Action >
     Properties.

  3. The Microsoft Exchange POP3 Properties window opens. On the General tab, configure
     the following settings:

          Startup type: Select Automatic.

          Service status: Click Start.

     When you're finished, click OK.

  4. In the list of services, select Microsoft Exchange POP3 Backend, and then click Action >
     Properties.

  5. The Microsoft Exchange POP3 Backend Properties window opens. On the General tab,
     configure the following settings:

          Startup type: Select Automatic.

          Service status: Click Start.

<!-- p.1340 -->

     When you're finished, click OK.

Use the Exchange Management Shell to start the POP3
services, and configure the services to start automatically
   1. Run the following command to start the POP3 services:

        PowerShell

        Start-Service MSExchangePOP3; Start-Service MSExchangePOP3BE

   2. Run the following command to configure the POP3 services to start automatically:

        PowerShell

        Set-Service MSExchangePOP3 -StartupType Automatic; Set-Service
        MSExchangePOP3BE -StartupType Automatic

For more information about these cmdlets, see Start-Service and Set-Service.

How do you know this step worked?
To verify that you've successfully started the POP3 services, use either of the following
procedures:

     On the Exchange server, open Windows Task Manager. On the Services tab, verify that the
     Status value for the MSExchangePOP3 and MSExchangePOP3BE services is Running.

     In the Exchange Management Shell, run the following command to verify that the POP3
     services are running:

        PowerShell

        Get-Service MSExchangePOP3; Get-Service MSExchangePOP3BE

Step 2: Use the Exchange Management Shell to
configure the POP3 settings for external clients
To configure the POP3 settings for external clients, use the following syntax:

  PowerShell

<!-- p.1341 -->

  Set-PopSettings -ExternalConnectionSettings "<FQDN1>:<TCPPort1>:<SSL | TLS |
  blank>", "<FQDN2>:<TCPPort2>:<SSL | TLS | blank>"... -X509CertificateName <FQDN>
  [-SSLBindings "<IPv4Orv6Address1>:<TCPPort1>","<IPv4Orv6Address2>:<TCPPort2>"...]
  [-UnencryptedOrTLSBindings "<IPv4Orv6Address1>:<TCPPort1>","<IPv4Orv6Address2>:
  <TCPPort2>"...]

This example allows to configure the following settings for external POP3 connections:

     POP3 server FQDN: mail.contoso.com

     TCP port: 995 for always TLS encrypted connections, and 110 for unencrypted
     connections or opportunistic TLS (STARTTLS) encrypted connections.

     Internal Exchange server IP address and TCP port for always TLS encrypted
     connections: All available IPv4 and IPv6 addresses on the server on port 995 (we aren't
     using the SSLBindings parameter, and the default value is [::]:995,0.0.0.0:995 ).

     Internal Exchange server IP address and TCP port for unencrypted or opportunistic TLS
     (STARTTLS) encrypted connections: All available IPv4 and IPv6 addresses on the server
     on port 110 (we aren't using the UnencryptedOrTLSBindings parameter, and the default
     value is [::]:110,0.0.0.0:110 ).

     FQDN used for encryption: mail.contoso.com. This value identifies the certificate that
     matches or contains the POP3 server FQDN.

  PowerShell

  Set-PopSettings -ExternalConnectionSettings
  "mail.contoso.com:995:SSL","mail.contoso.com:110:TLS" -X509CertificateName
  mail.contoso.com

Notes:

     For detailed syntax and parameter information, see Set-PopSettings.

     The external POP3 server FQDN that you configure needs to have a corresponding record
     in your public DNS, and the TCP port (110 or 995) needs to be allowed through your
     firewall to the Exchange server.

     The combination of encryption methods and TCP ports that you use for the
     ExternalConnectionSettings parameter need to match the corresponding TCP ports and
     encryption methods that you use for the SSLBindings or UnencryptedOrTLSBindings
     parameters.

<!-- p.1342 -->

     Although you can use a separate certificate for POP3, we recommend that you use the
     same certificate as the other Exchange IIS (HTTP) services, which is likely a wildcard
     certificate or a subject alternative name (SAN) certificate from a commercial certification
     authority that's automatically trusted by all clients. For more information, see Certificate
     requirements for Exchange services.

     If you use a single subject certificate, or a SAN certificate, you also need to assign the
     certificate to the Exchange POP service. You don't need to assign a wildcard certificate to
     the Exchange POP service. For more information, see Assign certificates to Exchange
     Server services.

How you do know this step worked?
To verify that you've successfully configured the POP3 settings for external clients, run the
following command in the Exchange Management Shell and verify the settings:

  PowerShell

  Get-PopSettings | Format-List *ConnectionSettings,*Bindings,X509CertificateName

For more information, see Get-POPSettings.

Step 3: Restart the POP3 services
After you enable and configure POP3, you need to restart the POP3 services on the server by
using the Windows Services console, or the Exchange Management Shell.

Use the Windows Services console to restart the POP3
services
   1. On the Exchange server, open the Windows Services console.

   2. In the list of services, select Microsoft Exchange POP3, and then click Action > Restart.

   3. In the list of services, select Microsoft Exchange POP3 Backend, and then click Action >
     Restart.

Use the Exchange Management Shell to restart the POP3
services
Run the following command to restart the POP3 services.

<!-- p.1343 -->

  PowerShell

  Restart-Service MSExchangePOP3; Restart-Service MSExchangePOP3BE

For more information about this cmdlet, see Restart-Service.

To verify that you've successfully restarted the POP3 services, run the following command:

  PowerShell

  Get-Service MSExchangePOP3; Get-Service MSExchangePOP3BE

Step 4: Configure the authenticated SMTP settings
for POP3 clients
Because POP3 isn't used to send email messages, you need to configure the authenticated
SMTP settings that are used by internal and external POP3 clients. For more information, see
POP3 and IMAP4 in Exchange Server.

How do you know this task worked?
To verify that you have enabled and configured POP3 on the Exchange server, perform the
following procedures:

   1. Open a mailbox in Outlook on the web, and then click Settings > Options.

   2. Click Mail > Accounts > POP and IMAP and verify the correct POP3 settings are
     displayed.

<!-- p.1344 -->

     Note: If you configured 995/SSL and 110/TLS values for the ExternalConnectionSettings
     parameter on the Set-PopSettings cmdlet, only the 995/SSL value is displayed in Outlook
     on the web. Also, if the external POP3 settings that you configured don't appear as
     expected in Outlook on the web after you restart the POP3 services, run the commands
     net stop w3svc /y and net start w3svc to restart Internet Information Services (IIS).

   3. You can test POP3 client connectivity to the Exchange server by using the following
     methods:

          Internal clients: Use the Test-PopConnectivity cmdlet. For example, Test-
          PopConnectivity -ClientAccessServer <ServerName> -Lightmode -MailboxCredential

          (Get-Credential) . For more information, see Test-PopConnectivity.

          Note: The Lightmode switch tells the command test POP3 logons to the server. To
          test sending (SMTP) and receiving (POP3) a message, you need to configure the
          authenticated SMTP settings as described in POP3 and IMAP4 in Exchange Server.

          External clients: Use the POP Email test in the Microsoft Remote Connectivity
          Analyzer   .

          Note: You can't use POP3 to connect to the Administrator mailbox. This limitation
          was intentionally included in Exchange 2016 and Exchange 2019 to enhance the
          security of the Administrator mailbox.

Next steps
To enabled or disable POP3 access to individual mailboxes, see Enable or disable POP3 or
IMAP4 access to mailboxes in Exchange Server.

<!-- p.1345 -->

Enable and configure IMAP4 on an
Exchange server
Article • 04/03/2025

APPLIES TO:        2016     2019      Subscription Edition

By default, IMAP4 client connectivity isn't enabled in Exchange. To enable IMAP4 client
connectivity, you need to perform the following steps:

   1. Start the IMAP4 services, and configure the services to start automatically:

            Microsoft Exchange IMAP4: This is the Client Access (frontend) service that IMAP4
            clients connect to.

            Microsoft Exchange IMAP4 Backend: IMAP4 client connections from the Client
            Access service are proxied to the backend service on the server that holds the active
            copy of the user's mailbox. For more information, see Exchange architecture.

   2. Configure the IMAP4 settings for external clients.

      By default, Exchange uses the following settings for internal IMAP4 connections:

            IMAP4 server FQDN: <ServerFQDN> . For example, mailbox01.contoso.com .

            TCP port and encryption method: 993 for always TLS encrypted connections, and
            143 for unencrypted connections, or for opportunistic TLS (STARTTLS) that results in
            an encrypted connection after the initial plain text protocol handshake.

      To allow external IMAP4 clients to connect to mailboxes, you need to configure the
      IMAP4 server FQDN, TCP port, and encryption method for external connections. This step
      causes the external IMAP4 settings to be displayed in Outlook on the web (formerly
      known as Outlook Web App) at Settings > Options > Mail > Accounts > POP and IMAP.

<!-- p.1346 -->

  3. Restart the IMAP4 services to save the changes.

  4. Configure the authenticated SMTP settings for internal and external clients. For more
     information, see Configure authenticated SMTP settings for POP3 and IMAP4 clients in
     Exchange.

For more information about IMAP4, see POP3 and IMAP4 in Exchange Server.

What do you need to know before you begin?
     Estimated time to complete each procedure: 5 minutes.

     Secure Sockets Layer (SSL) is being replaced by Transport Layer Security (TLS) as the
     protocol that's used to encrypt data sent between computer systems. They're so closely
     related that the terms "SSL" and "TLS" (without versions) are often used interchangeably.
     Because of this similarity, references to "SSL" in Exchange topics, the Exchange admin
     center, and the Exchange Management Shell have often been used to encompass both
     the SSL and TLS protocols. Typically, "SSL" refers to the actual SSL protocol only when a
     version is also provided (for example, SSL 3.0). To find out why you should disable the SSL
     protocol and switch to TLS, check out Protecting you against the SSL 3.0 vulnerability .

     To learn how to open the Exchange Management Shell in your on-premises Exchange
     organization, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "POP3 and IMAP4 Permissions"
     section in the Clients and mobile devices permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

<!-- p.1347 -->

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

Step 1: Start the IMAP4 services, and configure the
services to start automatically
You can perform this step by using the Windows Services console, or the Exchange
Management Shell.

Use the Windows Services console to start the IMAP4
services, and configure the services to start automatically
  1. On the Exchange server, open the Windows Services console. For example:

          Run the command services.msc from the Run dialog, a Command Prompt window,
          or the Exchange Management Shell.

          Open Server Manager, and then click Tools > Services.

  2. In the list of services, select Microsoft Exchange IMAP4, and then click Action >
     Properties.

  3. The Microsoft Exchange IMAP4 Properties window opens. On the General tab, configure
     the following settings:

          Startup type: Select Automatic.

          Service status: Click Start.

     When you're finished, click OK.

  4. In the list of services, select Microsoft Exchange IMAP4 Backend, and then click Action >
     Properties.

  5. The Microsoft Exchange IMAP4 Backend Properties window opens. On the General tab,
     configure the following settings:

          Startup type: Select Automatic.

          Service status: Click Start.

<!-- p.1348 -->

     When you're finished, click OK.

Use the Exchange Management Shell to start the IMAP4
services, and configure the services to start automatically
   1. Run the following command to start the IMAP4 services:

        PowerShell

        Start-Service MSExchangeIMAP4; Start-Service MSExchangeIMAP4BE

   2. Run the following command to configure the IMAP4 services to start automatically:

        PowerShell

        Set-Service MSExchangeIMAP4 -StartupType Automatic; Set-Service
        MSExchangeIMAP4BE -StartupType Automatic

For more information about these cmdlets, see Start-Service and Set-Service.

How do you know this step worked?
To verify that you've successfully started the IMAP4 services, use either of the following
procedures:

     On the Exchange server, open Windows Task Manager. On the Services tab, verify that the
     Status value for the MSExchangeIMAP4 and MSExchangeIMAP4BE services is Running.

     In the Exchange Management Shell, run the following command to verify that the IMAP4
     services are running:

        PowerShell

        Get-Service MSExchangeIMAP4; Get-Service MSExchangeIMAP4BE

Step 2: Use the Exchange Management Shell to
configure the IMAP4 settings for external clients
To configure the IMAP4 settings for external clients, use the following syntax:

  PowerShell

<!-- p.1349 -->

  Set-ImapSettings -ExternalConnectionSettings "<FQDN1>:<TCPPort1>:<SSL | TLS |
  blank>", "<FQDN2>:<TCPPort2>:<SSL | TLS | blank>"... -X509CertificateName <FQDN>
  [-SSLBindings "<IPv4Orv6Address1>:<TCPPort1>","<IPv4Orv6Address2>:<TCPPort2>"...]
  [-UnencryptedOrTLSBindings "<IPv4Orv6Address1>:<TCPPort1>","<IPv4Orv6Address2>:
  <TCPPort2>"...]

This example allows to configure the following settings for external IMAP4 connections:

     IMAP4 server FQDN: mail.contoso.com

     TCP port: 993 for always TLS encrypted connections, and 143 for unencrypted
     connections or opportunistic TLS (STARTTLS) encrypted connections.

     Internal Exchange server IP address and TCP port for always TLS encrypted
     connections: All available IPv4 and IPv6 addresses on the server on port 993 (we aren't
     using the SSLBindings parameter, and the default value is [::]:993,0.0.0.0:993 ).

     Internal Exchange server IP address and TCP port for unencrypted or opportunistic TLS
     (STARTTLS) encrypted connections: All available IPv4 and IPv6 addresses on the server
     on port 143 (we aren't using the UnencryptedOrTLSBindings parameter, and the default
     value is [::]:143,0.0.0.0:143 ).

     FQDN used for encryption: mail.contoso.com. This value identifies the certificate that
     matches or contains the IMAP4 server FQDN.

  PowerShell

  Set-ImapSettings -ExternalConnectionSettings
  "mail.contoso.com:993:SSL","mail.contoso.com:143:TLS" -X509CertificateName
  mail.contoso.com

  ７ Note

        For detailed syntax and parameter information, see Set-IMAPSettings.

        The external IMAP4 server FQDN that you configure needs to have a corresponding
        record in your public DNS, and the TCP port (143 or 993) needs to be allowed
        through your firewall to the Exchange server.

        The combination of encryption methods and TCP ports that you use for the
        ExternalConnectionSettings parameter need to match the corresponding TCP ports
        and encryption methods that you use for the SSLBindings or
        UnencryptedOrTLSBindings parameters.

<!-- p.1350 -->

        Although you can use a separate certificate for IMAP4, we recommend that you use
        the same certificate as the other Exchange IIS (HTTP) services, which is likely a
        wildcard certificate or a subject alternative name (SAN) certificate from a commercial
        certification authority that's automatically trusted by all clients. For more
        information, see Certificate requirements for Exchange services.

        If you use a single subject certificate, or a SAN certificate, you also need to assign the
        certificate to the Exchange IMAP service. You don't need to assign a wildcard
        certificate to the Exchange IMAP service. For more information, see Assign
        certificates to Exchange Server services.

How you do know this step worked?
To verify that you've successfully configured the IMAP4 settings for external clients, run the
following command in the Exchange Management Shell and verify the settings:

  PowerShell

  Get-ImapSettings | Format-List *ConnectionSettings,*Bindings,X509CertificateName

For more information, see Get-IMAPSettings.

Step 3: Restart the IMAP4 services
After you enable and configure IMAP4, you need to restart the IMAP4 services on the server by
using the Windows Services console, or the Exchange Management Shell.

Use the Windows Services console to restart the IMAP4
services
   1. On the Exchange server, open the Windows Services console.

   2. In the list of services, select Microsoft Exchange IMAP4, and then click Action > Restart.

   3. In the list of services, select Microsoft Exchange IMAP4 Backend, and then click Action >
     Restart.

Use the Exchange Management Shell to restart the IMAP4
services

<!-- p.1351 -->

Run the following command to restart the IMAP4 services.

  PowerShell

  Restart-Service MSExchangeIMAP4; Restart-Service MSExchangeIMAP4BE

For more information about this cmdlet, see Restart-Service.

To verify that you've successfully restarted the IMAP4 services, run the following command:

  PowerShell

  Get-Service MSExchangeIMAP4; Get-Service MSExchangeIMAP4BE

Step 4: Configure the authenticated SMTP settings
for IMAP4 clients
Because IMAP4 isn't used to send email messages, you need to configure the authenticated
SMTP settings that are used by internal and external IMAP4 clients. For more information, see
Configure authenticated SMTP settings for POP3 and IMAP4 clients in Exchange Server.

How do you know this task worked?
To verify that you have enabled and configured IMAP4 on the Exchange server, perform the
following procedures:

   1. Open a mailbox in Outlook on the web, and then click Settings > Options.

   2. Click Mail > Accounts > POP and IMAP and verify the correct IMAP4 settings are
     displayed.

<!-- p.1352 -->

７ Note

If you configured 993/SSL and 143/TLS values for the ExternalConnectionSettings
parameter on the Set-ImapSettings cmdlet, only the 993/SSL value is displayed in Outlook
on the web. Also, if the external IMAP4 settings that you configured don't appear as
expected in Outlook on the web after you restart the IMAP4 services, run the commands
net stop w3svc /y and net start w3svc to restart Internet Information Services (IIS).

3. You can test IMAP4 client connectivity to the Exchange server by using the following
  methods:

         Internal clients: Use the Test-ImapConnectivity cmdlet. For example, Test-
         ImapConnectivity -ClientAccessServer <ServerName> -Lightmode -MailboxCredential
         (Get-Credential) . For more information, see Test-ImapConnectivity.

     ７ Note

     The Lightmode switch tells the command test IMAP4 logons to the server. To test
     sending (SMTP) and receiving (IMAP4) a message, you need to configure the
     authenticated SMTP settings as described in Configure authenticated SMTP settings
     for POP3 and IMAP4 clients in Exchange Server.

         External clients: Use the Imap Email test in the Microsoft Remote Connectivity
         Analyzer   .

     ７ Note

<!-- p.1353 -->

       You can't use IMAP4 to connect to the Administrator mailbox. This limitation was
       intentionally included in Exchange 2016 and Exchange 2019 to enhance the security
       of the Administrator mailbox.

Next steps
To enabled or disable IMAP4 access to individual mailboxes, see Enable or disable POP3 or
IMAP4 access to mailboxes in Exchange Server.

<!-- p.1354 -->

Enable or disable POP3 or IMAP4 access to
mailboxes in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

After you enable and configure POP3 or IMAP4 on an Exchange server as described in Enable
and configure POP3 on an Exchange server and Enable and configure IMAP4 on an Exchange
server, all user mailboxes (with the exception of the Administrator mailbox) can be accessed by
using POP3 or IMAP4. You can use the procedures in this topic to disable POP3 and IMAP4
access to specific mailboxes.

For more information about POP3 and IMAP4, see POP3 and IMAP4 in Exchange Server.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.

      To open the Exchange admin center (EAC), see Exchange admin center in Exchange
      Server. To open the Exchange Management Shell, see Open the Exchange Management
      Shell.

      The procedures in this topic don't apply to the Administrator mailbox, because you can't
      use POP3 or IMAP4 to connect to the Administrator mailbox. This limitation was
      intentionally included in Exchange 2016 and Exchange 2019 to enhance the security of
      the Administrator mailbox.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Recipient provisioning
      permissions" section in the Recipients Permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at Exchange
  Server .

<!-- p.1355 -->

Enable or disable POP3 or IMAP4 access to a single
mailbox

Use the EAC to enable or disable POP3 or IMAP4 access to a
mailbox
 1. In the EAC, go to Recipients > Mailboxes.

 2. In the list of mailboxes, find the mailbox that you want to modify. You can:

        Scroll through the list of mailboxes.

        Click Search (   ) and enter part of the user's name, email address, or alias.

        Click More options (    ) > Advanced search to find the mailbox.

   Once you've found the mailbox that you want to modify, select it, and then click Edit (   ).

 3. In the mailbox properties window that opens, click Mailbox Features.

   In the Email connectivity section, configure one or more of the following settings:

        POP3: To disable POP3 access to the mailbox, click Disable, and then click Yes in the
        warning message that appears. If POP3 is already disabled, click Enable to enable it.

        IMAP: To disable IMAP4 access to the mailbox, click Disable, and then click Yes in
        the warning message that appears. If IMAP4 is already disabled, click Enable to
        enable it.

   When you're finished, click Save.

<!-- p.1356 -->

Use the Exchange Management Shell to enable or disable
POP3 or IMAP4 access to a mailbox
To enable or disable POP3 or IMAP4 access to a single mailbox use the following syntax:

  PowerShell

  Set-CasMailbox -Identity <MailboxIdentity> -PopEnabled <$true | $false> -
  ImapEnabled <$true | $false>

This example disables POP3 and IMAP4 access to the mailbox named Rand Zaher.

  PowerShell

  Set-CasMailbox -Identity "Rand Zaher" -PopEnabled $false -ImapEnabled $false

This example enables POP3 and IMAP4 access to the mailbox named Rand Zaher.

  PowerShell

  Set-CasMailbox -Identity "Rand Zaher" -POPEnabled $true -ImapEnabled $true

For more information, see Set-CASMailbox.

Enable or disable POP3 or IMAP4 access to
multiple mailboxes

Use the EAC to enable or disable POP3 or IMAP4 access to
multiple mailboxes
   1. In the EAC, go to Recipients > Mailboxes.

   2. In the list of mailboxes, find the mailboxes that you want to modify. You can:

           Scroll through the list of mailboxes.

           Click Search (   ) and enter part of the user's name, email address, or alias.

           Click More options (    ) > Advanced search to find the mailbox.

   3. In the list of mailboxes, select multiple mailboxes of the same type (for example, User)
     from the list. For example:

<!-- p.1357 -->

          Select a mailbox, hold down the Shift key, and select another mailbox that's farther
          down in the list.

          Hold down the CTRL key as you select each mailbox.

     After you select multiple mailboxes of the same type, the title of the details pane changes
     to Bulk Edit.

  4. In the details pane, go to POP3 or IMAP, click Enable or Disable, and then click OK in the
     warning message that appears.

Use the Exchange Management Shell to enable or disable
POP3 or IMAP4 access to multiple mailboxes
You can use the Get-Mailbox, Get-User, or Get-Content cmdlets to identify the mailboxes that
you want to modify. For example:

     Use the OrganizationalUnit parameter to filter the mailboxes by organizational unit (OU).

     Use the Filter parameter to create OPATH filters that identify the mailboxes. For more
     information, see Filterable Properties for the -Filter Parameter.

     Use a text file to specify the mailboxes. The text file contains one mailbox (email address,
     name, or other unique identifier) on each line like this:

       ebrunner@tailspintoys.com
       fapodaca@tailspintoys.com

<!-- p.1358 -->

       glaureano@tailspintoys.com
       hrim@tailspintoys.com

This example disables POP3 and IMAP4 access to all user mailboxes in the North
America\Finance OU.

  PowerShell

  $NAFinance = Get-Mailbox -OrganizationalUnit "OU=Marketing,OU=North
  America,DC=contoso,DC=com" -Filter "RecipientTypeDetails -eq 'UserMailbox'" -
  ResultSize Unlimited; $NAFinance | foreach {Set-CasMailbox $_.Identity -PopEnabled
  $false -ImapEnabled $false}

This example disables POP3 and IMAP4 access to all mailboxes in the Engineering department
in Washington state.

  PowerShell

  Get-User -Filter "RecipientType -eq 'UserMailbox' -and Department -like
  'Engineering*' -and StateOrProvince -eq 'WA'" | Set-CasMailbox -PopEnabled $false
  -ImapEnabled $false

This example uses the text file C:\My Documents\Accounts.txt to disable POP3 or IMAP4 access
to the specified mailboxes.

  PowerShell

  Get-Content "C:\My Documents\Accounts.txt" | foreach {Set-CASMailbox $_ -
  PopEnabled $false -ImapEnabled $false}

For more information, see Get-Mailbox and Get-User.

Restart the POP3 or IMAP4 services
After you change the POP3 or IMAP4 access settings on a mailbox, you need to restart the
POP3 and IMAP4 services on the server. You can do this by using the Windows Services
console, or the Exchange Management Shell.

Use the Windows Services console to restart the POP3 or
IMAP4 services
   1. On the Exchange server, open the Windows Services console. For example:

<!-- p.1359 -->

           Run the command services.msc from the Run dialog, a Command Prompt window,
           or the Exchange Management Shell.

           Open Server Manager, and then click Tools > Services.

   2. In the list of services, do one or both of the following actions:

           POP3:

               a. Select Microsoft Exchange POP3, and then click Action > Restart.

               b. Select Microsoft Exchange POP3 Backend, and then click Action > Restart.

           IMAP4:

               a. Select Microsoft Exchange IMAP4, and then click Action > Restart.

               b. Select Microsoft Exchange IMAP4 Backend, and then click Action > Restart.

Use the Exchange Management Shell to restart the POP3 or
IMAP4 services
To restart the POP3 services, run the following command:

  PowerShell

  Restart-Service MSExchangePOP3; Restart-Service MSExchangePOP3BE

To restart the IMAP4 services, run the following command:

  PowerShell

  Restart-Service MSExchangeIMAP4; Restart-Service MSExchangeIMAP4BE

For more information about this cmdlet, see Restart-Service.

To verify that you've successfully restarted the POP3 or IMAP4 services, run the following
command:

  PowerShell

  Get-Service MSExchangePOP3; Get-Service MSExchangePOP3BE; Get-Service
  MSExchangeIMAP4; Get-Service MSExchangeIMAP4BE

<!-- p.1360 -->

How do you know this worked?
To verify that you've enabled or disabled POP3 or IMAP4 access to a mailbox, use any of the
following procedures:

     In the EAC, go to Recipients > Mailboxes > select the mailbox > click Edit      > Mailbox
     features > Email connectivity.

        If POP3 access is enabled for the mailbox, you'll see POP3: Enabled and the Disable
        link. If POP3 access is disabled, you'll see POP3: Disabled and the Enable link.

        If IMAP4 access is enabled for the mailbox, you'll see IMAP4: Enabled and a Disable
        link. If IMAP4 access is disabled, you'll see IMAP4: Disabled and the Enable link.

     In the Exchange Management Shell, replace <MailboxIdentity> with the identity of the
     mailbox (for example, name, alias, or email address), and run the following command:

       PowerShell

       Get-CasMailbox - Identity <MailboxIdentity>

     Use the same filter that you used to identify the mailboxes, but use the Get-CasMailbox
     cmdlet instead of Set-CasMailbox. For example:

       PowerShell

       Get-User -Filter "RecipientType -eq 'UserMailbox' -and Department -like
       'Engineering*' -and StateOrProvince -eq 'WA'" | Get-CasMailbox
