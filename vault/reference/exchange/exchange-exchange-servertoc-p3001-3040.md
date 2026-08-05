---
title: "Exchange Server — pages 3001-3040"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p3001-3040
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p3001-3040
family: exchange
documentKind: "doc"
abstract: "Get-SenderReputationConfig | Format-List InternalMailEnabled Use the Exchange Management Shell to configure sender blocking in sender reputation Sender blocking uses the calculated sender reputation level (SRL) of the sender and a specified SRL threshold to temporarily block the"
---

# Exchange Server — pages 3001-3040

<!-- p.3001 -->

  Get-SenderReputationConfig | Format-List InternalMailEnabled

Use the Exchange Management Shell to configure
sender blocking in sender reputation
Sender blocking uses the calculated sender reputation level (SRL) of the sender and a specified
SRL threshold to temporarily block the sender. To configure the sender blocking in sender
reputation, use the following syntax:

  PowerShell

  Set-SenderReputationConfig -SenderBlockingEnabled <$true | $false> -
  SrlBlockThreshold <0 - 9> [-SenderBlockingPeriod <0 - 48>]

This example lowers the sender reputation level (SRL) block threshold to 6 (which means
senders with an SRL of 6, 7, 8, or 9 are blocked), and blocks the offending senders for 36 hours:

  PowerShell

  Set-SenderReputationConfig -SrlBlockThreshold 6 -SenderBlockingPeriod 36

This example disables sender blocking.

  PowerShell

  Set-SenderReputationConfig -SenderBlockingEnabled $false

Notes:

     The default value of the SenderBlockingEnabled parameter is $true .

     The default value of the SenderBlockingPeriod parameter is 24.

     The default value of the SrlBlockThreshold parameter is 7.

     You can't disable sender blocking and open proxy server detection at the same time. One
     must be enabled when the other is disabled, or they both can be enabled.

How do you know this worked?

<!-- p.3002 -->

To verify that you have successfully configured sender blocking in sender reputation, run the
following command to verify the property values:

  PowerShell

  Get-SenderReputationConfig | Format-List *block*

Use the Exchange Management Shell to configure
open proxy server detection in sender reputation
By default, sender reputation uses open proxy server detection as one of the criteria to
calculate the SRL of the source server. In open proxy server detection, the Exchange server tries
to send a test message from the source messaging server. If the test message is successfully
delivered back to the Exchange server, it indicates the source server is configured as an open
proxy server (intentionally or unintentionally).

Open proxy server detection uses the protocols and TCP ports that are described in the
following table, so these outbound ports need to be open in your firewall:

                                                                                 ﾉ   Expand table

 Protocols                                                      Ports

 SOCKS4, SOCKS5                                                 1081, 1080

 Wingate, Telnet, Cisco                                         23

 HTTP CONNECT, HTTP POST                                        6588, 3128, 80

Also, if your organization uses a proxy server to control outbound Internet traffic, you need to
configure sender reputation to use your proxy server to access the Internet. Specifically, you
need to define the proxy server name, type, and TCP port that sender reputation requires to
access the Internet.

To configure open proxy server detection in sender reputation, use the following syntax:

  PowerShell

  Set-SenderReputationConfig -OpenProxyDetectionEnabled <$true | $false> [-
  ProxyServerName <String> -ProxyServerPort <Port> -ProxyServerType <None | Socks4 |
  Socks5 | HttpConnect | HttpPost | Telnet | Cisco | Wingate>]

<!-- p.3003 -->

This example configures sender reputation to connect to the Internet through the proxy server
named SERVER01 that uses the HTTP CONNECT protocol on port 80.

  PowerShell

  Set-SenderReputationConfig -ProxyServerName SERVER01 -ProxyServerPort 80 -
  ProxyServerType HttpConnect

This example disables open proxy server detection in sender reputation.

  PowerShell

  Set-SenderReputationConfig -OpenProxyDetectionEnabled $false

Notes:

     The default value of the OpenProxyDetectionEnabled parameter is $true .

     The default value of the ProxyServerName parameter is blank ( $null ).

     The default value of the ProxyServerPort parameter is 0.

     The default value of the ProxyServerType parameter is None .

     You can't disable open proxy server detection and sender blocking at the same time. One
     must be enabled when the other is disabled, or they both can be enabled.

How do you know this worked?
To verify that you have successfully configured open proxy server detection in sender
reputation, run the following command to verify the property values:

  PowerShell

  Get-SenderReputationConfig | Format-List *proxy*

See also
Get-SenderReputationConfig

Set-SenderReputationConfig

<!-- p.3004 -->

How to use attachment filtering on Edge
Transport servers in Exchange Server
Article • 04/30/2025

APPLIES TO:          2016   2019     Subscription Edition

In Exchange Server, you can use attachment filtering on Edge Transport servers to control the
attachments that users receive in email messages. Attachment filtering is performed by the
Attachment Filtering agent, which is available only on Edge Transport servers, and is basically
unchanged from Exchange Server 2010.

To configure the attachment filtering options, see Attachment filtering procedures on Edge
Transport servers.

Types of attachment filtering
You can use the following types of attachment filtering to control attachments that enter or
leave your organization through an Edge Transport server:

      Filtering based on file name or file name extension: You specify the exact file name or
      file name extension that you want to filter. For example, BadFileName.exe or *.exe .

      Filtering based on file MIME content type: You specify the MIME content type value that
      you want to filter. The MIME content type value indicates what the attachment is: for
      example, a JPEG image, an executable file, or a Microsoft Excel file. Content types are
      expressed as <type>/ <subtype>. For example, a JPEG image file is expressed as
      image/jpeg .

      To view a complete list of file name extensions and content types that attachment filtering
      can detect, run the following command in the Exchange Management Shell on the Edge
      Transport server:

        PowerShell

        Get-AttachmentFilterEntry | Format-Table -Auto Type,Name

After you define the files to look for, you can configure the action to take on messages that
contain these attachments. You can't specify different actions for different types of
attachments. You configure one of the following actions for all the messages that match any of
the attachment filters:

<!-- p.3005 -->

     Reject (block) the message: he message is blocked. The sender receives a non-delivery
     report (also known as an NDR, delivery status notification, DSN, or bounce message) that
     explains that the message wasn't delivered because it contained an unacceptable
     attachment. You can customize the text in the NDR. The default text is: Message rejected
     due to unacceptable attachments .

     Strip the attachment but allow the message through: The attachment is removed from
     the message. However, the message itself and any other attachments that don't match
     the filter are allowed through. If an attachment is stripped, it's replaced with a text file
     that explains why the attachment was removed. This is the default action.

     Silently delete the message: The message is deleted. Neither the sender nor the recipient
     receives notification.

Notes:

     You can't retrieve messages that have been blocked or attachments that have been
     stripped. When you configure attachment filters, carefully examine all possible file name
     matches and verify that legitimate attachments won't be affected by the filter.

     If you remove attachments from digitally signed, encrypted, or rights-protected
     messages, you invalidate the digital signature, which makes encrypted and rights-
     protected messages unreadable. A way to avoid this problem for outbound messages is
     to sign or encrypt the messages after they've been processed by the Attachment Filtering
     agent.

For more information, see Attachment filtering procedures on Edge Transport servers.

Default attachments in attachment filtering
The default attachments that are defined in attachment filtering are described in the following
table.

                                                                                   ﾉ   Expand table

 Type                              Name

 ContentType                        application/hta

 ContentType                        application/javascript

 ContentType                        application/msaccess

 ContentType                        application/prg

<!-- p.3006 -->

Type          Name

ContentType   application/x-javascript

ContentType   application/x-msdownload

ContentType   message/partial

ContentType   text/javascript

ContentType   text/scriptlet

ContentType   x-internet-signup

FileName      *.ade

FileName      *.adp

FileName      *.app

FileName      *.asx

FileName      *.bas

FileName      *.bat

FileName      *.chm

FileName      *.cmd

FileName      *.com

FileName      *.cpl

FileName      *.crt

FileName      *.csh

FileName      *.exe

FileName      *.fxp

FileName      *.hlp

FileName      *.hta

FileName      *.inf

FileName      *.ins

FileName      *.isp

FileName      *.js

<!-- p.3007 -->

Type       Name

FileName   *.jse

FileName   *.ksh

FileName   *.lnk

FileName   *.mda

FileName   *.mdb

FileName   *.mde

FileName   *.mdt

FileName   *.mdw

FileName   *.mdz

FileName   *.msc

FileName   *.msi

FileName   *.msp

FileName   *.mst

FileName   *.ops

FileName   *.pcd

FileName   *.pif

FileName   *.prf

FileName   *.prg

FileName   *.ps1

FileName   *.ps1xml

FileName   *.ps11

FileName   *.ps11xml

FileName   *.ps2

FileName   *.ps2xml

FileName   *.psc1

FileName   *.psc2

<!-- p.3008 -->

Type       Name

FileName   *.reg

FileName   *.scf

FileName   *.scr

FileName   *.sct

FileName   *.shb

FileName   *.shs

FileName   *.url

FileName   *.vb

FileName   *.vbe

FileName   *.vbs

FileName   *.wsc

FileName   *.wsf

FileName   *.wsh

FileName   *.xnk

<!-- p.3009 -->

Attachment filtering procedures on Edge
Transport servers
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

Attachment filtering in Exchange Server is provided by the Attachment Filter agent that's
available only on Edge Transport servers. Attachment filtering can help prevent files in email
messages from entering your organization. You can configure one or more attachment filter
entries to filter attachments either by content type or by file name.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Antispam features" entry in the
      Antispam and antimalware permissions and the "Transport agents" entry in the Mail flow
      permissions topic.

      Configuration changes that you make to attachment filtering on an Edge Transport server
      are made only to the local computer. If you have multiple Edge Transport servers in your
      perimeter network, you need to configure attachment filtering on each Edge Transport
      server separately.

      You can only use PowerShell to perform this procedure. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

Use the Exchange Management Shell to enable or
disable attachment filtering

<!-- p.3010 -->

When you enable or disable the Attachment Filtering agent, the change takes effect after you
restart the Microsoft Exchange Transport service. When you restart the Microsoft Exchange
Transport service on an Edge Transport server, mail flow on the server is temporarily
interrupted.

To disable attachment filtering, run the following command:

  PowerShell

  Disable-TransportAgent "Attachment Filtering Agent"

To enable attachment filtering, run the following command:

  PowerShell

  Enable-TransportAgent "Attachment Filtering Agent"

After you enable or disable attachment filtering, restart the Microsoft Exchange Transport
service by running the following command:

  PowerShell

  Restart-Service MSExchangeTransport

How do you know this worked?
To verify that you successfully enabled or disabled attachment filtering, run the following
command to verify the Enabled property value:

  PowerShell

  Get-TransportAgent "Attachment Filtering Agent"

Use the Exchange Management Shell to view and
find attachment filtering entries
Attachment filtering entries define the message attachments that you want to keep out of your
organization. To view the attachment filtering entries that are used by the Attachment Filtering
agent, run the following command:

  PowerShell

<!-- p.3011 -->

  Get-AttachmentFilterEntry | Format-Table -Auto Type,Name

To find a specific MIME content type entry, use the following syntax:

  PowerShell

  Get-AttachmentFilterEntry ContentType:<MIMEContentType>

For example, to see if there's a MIME content type entry for JPEG images, run the following
command:

  PowerShell

  Get-AttachmentFilterEntry ContentType:image/jpeg

If you receive the error, Couldn't find the specified identity. , then the MIME content type
isn't defined in the attachment filtering entries.

To view a specific file name or file name extension entry, use the following syntax:

  PowerShell

  Get-AttachmentFilterEntry FileName:<FileName or FileNameExtension>

For example, to see if there's a file name extension entry for JPEG attachments, run the
following command:

  PowerShell

  Get-AttachmentFilterEntry FileName:*.jpg

If you receive the error, Couldn't find the specified identity. , then the file name or file
name extension isn't defined in the attachment filtering entries.

For more information, see Get-AttachmentFilterEntry.

Use the Exchange Management Shell to add
attachment filtering entries

  ７ Note

<!-- p.3012 -->

  Adding a filter to XML files also blocks Office OpenXML attachment types, such as .docx ,
  .pptx , and .xlsx files. This is because these Office file formats are essentially ZIP archives

  containing XML files. Therefore, filtering XML files will inadvertently block these common
  Office document types.

To add an attachment filtering entry that filters attachments by MIME content type, use the
following syntax:

  PowerShell

  Add-AttachmentFilterEntry -Name <MIMEContentType> -Type ContentType

The following example adds a MIME content type entry that filters JPEG images.

  PowerShell

  Add-AttachmentFilterEntry -Name image/jpeg -Type ContentType

To add an attachment filtering entry that filters attachments by file name or file name
extension, use the following syntax:

  PowerShell

  Add-AttachmentFilterEntry -Name <FileName or FileNameExtension> -Type FileName

The following example filters attachments that have the .jpg file name extension.

  PowerShell

  Add-AttachmentFilterEntry -Name *.jpg -Type FileName

For more information, see Add-AttachmentFilterEntry.

How do you know this worked?
To verify that you successfully added an attachment filtering entry, send a test message that
contains the prohibited attachment from an external mailbox to an internal recipient and verify
that the message and the attachment are processed as you expect.

<!-- p.3013 -->

Use the Exchange Management Shell to remove
attachment filtering entries
To remove an attachment filtering entry that filters attachments by MIME content type, use the
following syntax:

  PowerShell

  Remove-AttachmentFilterEntry ContentType:<ContentType>

The following example removes the MIME content type entry for JPEG images.

  PowerShell

  Remove-AttachmentFilterEntry ContentType:image/jpeg

To remove an attachment filtering entry that filters attachments by file name or file name
extension, use the following syntax:

  PowerShell

  Remove-AttachmentFilterEntry FileName:<FileName or FileNameExtension>

The following example removes the file name entry for the .jpg file name extension.

  PowerShell

  Remove-AttachmentFilterEntry FileName:*.jpg

For more information, see Remove-AttachmentFilterEntry.

How do you know this worked?
To verify that you successfully removed an attachment filtering entry, send a test message that
contains the allowed attachment from an external mailbox to an internal recipient, and verify
that the message was successfully delivered with the attachment.

Use the Exchange Management Shell to view the
attachment filtering action

<!-- p.3014 -->

To view the attachment filtering action that's used when a prohibited attachment is detected in
a message, run the following command:

  PowerShell

  Get-AttachmentFilterListConfig | Format-List
  Action,AdminMessage,RejectResponse,ExceptionConnectors

Use the Exchange Management Shell to configure
the attachment filtering action
To configure the attachment filtering action that's used when a prohibited attachment is
detected in a message, use the following syntax:

  PowerShell

  Set-AttachmentFilterListConfig [-Action <Reject | Strip | SilentDelete>] [-
  RejectResponse "<Message text>"] [-AdminMessage "<Replacement file text>"] [-
  ExceptionConnectors <ConnectorGUID>]

This example makes the following changes to the attachment filtering configuration:

     Reject (block) messages that have prohibited attachments. Note that you can't specify
     different actions for different types of attachments.

     Use a custom response for rejected messages.

  PowerShell

  Set-AttachmentFilterListConfig -Action Reject -RejectResponse "This message
  contains a prohibited attachment. Your message can't be delivered. Please resend
  the message without the attachment."

For more information, see Set-AttachmentFilterListConfig.

How do you know this worked?
To verify that you successfully configured the attachment filtering action, send a test message
that contains a prohibited attachment from an external mailbox to an internal recipient and
verify that the message and the attachment are processed as you expect.

<!-- p.3015 -->

Connection filtering on Edge Transport
servers in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

Connection filtering is an antispam feature in Exchange Server that allows or blocks email
based on the message source. Connection filtering is performed by the Connection Filtering
agent that's available only on Edge Transport servers, and is basically unchanged from
Exchange Server 2010. The Connection Filtering agent relies on the IP address of the
connecting mail server to determine what action, if any, to take on an inbound message.

By default, the Connection Filtering agent is the first antispam agent to evaluate an inbound
message on an Edge Transport server. The source IP address of the SMTP connection is
checked against the allowed and blocked IP addresses. If the source IP address is specifically
allowed, the message is sent to the recipients in your organization without additional
processing by other antispam agents. If the source IP address is specifically blocked, the SMTP
connection is dropped. If the source IP address isn't specifically allowed or blocked, the
message flows through the other antispam agents on the Edge Transport server.

Connection filtering compares the IP address of the source mail server to the values in the IP
allowlist, the IP blocklist, IP allowlist providers, and IP blocklist providers. You need to configure
at least one of these four IP address data stores for connection filtering to function. If you don't
specify any IP address data, you should disable the Connection Filtering agent. For more
information, see Connection filtering procedures on Edge Transport servers.

IP blocklist
The IP blocklist contains the IP addresses of email servers that you want to block. You manually
maintain the IP addresses in the IP blocklist. You can add individual IP addresses or IP address
ranges. You can specify an expiration time that specifies how long the IP address entry will be
blocked. When the expiration time is reached, the IP address entry in the IP blocklist is
disabled.

If the Connection Filtering agent finds the source IP address on the IP blocklist, the SMTP
connection will be dropped after all the RCPT TO headers (envelope recipients) in the message
are processed.

IP addresses can also be automatically added to the IP blocklist by the Sender Reputation
feature of the Protocol Analysis agent. For more information, see Sender reputation and the
Protocol Analysis agent.

<!-- p.3016 -->

IP allowlist
The IP allowlist contains the IP addresses of email servers that you want to designate as
trustworthy sources of email. Email from mail servers that you specify in the IP allowlist is
exempt from processing by other Exchange antispam agents.

You manually maintain the IP addresses in the IP allowlist. You can add individual IP addresses
or IP address ranges. You can specify an expiration time that specifies how long the IP address
entry will be allowed. When the expiration time is reached, the entry in the IP allowlist is
disabled.

IP blocklist providers
IP blocklist providers are frequently referred to as real-time blocklists, or RBLs. IP blocklist
providers compile lists of mail server IP addresses that send spam. Many IP blocklist providers
also compile lists of mail server IP addresses that could be used for spam. Examples include
mail servers that are configured for open relay, Internet service providers (ISPs) that assign
dynamic IP addresses, and ISPs that allow SMTP mail server traffic from dial-up accounts.

When you configure connection filtering to use an IP blocklist provider, the Connection
Filtering agent compares the IP address of the connecting mail server to the list of IP addresses
at the IP blocklist provider. If there's a match, the message isn't allowed in your organization.
You can configure connection filtering to use multiple IP blocklist providers, and you assign
different priority values to each provider.

The Connection Filtering agent checks the source IP address at the IP allowlist and the IP
blocklist. If the IP address doesn't exist on either list, the Connection Filtering agent queries the
IP blocklist provider according to the priority value that you assigned. If the IP address is
defined at an IP blocklist provider, the Edge Transport server waits for and processes the RCPT
TO header, responds to the sending mail server with an SMTP 550 error, and closes the
connection. The connection isn't immediately dropped so that the connection attempt can be
logged, and because you can specify recipients that are exempt from having messages blocked
by any IP blocklist providers.

If the IP address isn't defined at any of the IP blocklist providers, the Content Filtering agent
hands the message off to the next transport agent on the Edge Transport server.

For each IP blocklist provider, you can customize the SMTP 550 error that's returned to the
sender when a message is blocked. You should identify the IP blocklist provider that identified
the message source as spam. If a legitimate source mail server is erroneously identified as a
spam source, the administrator can then contact the IP blocklistt provider and take the steps
necessary to remove the mail server from the IP blocklist provider.

<!-- p.3017 -->

IP blocklist providers can return different codes to identify why an IP address is defined in their
lists. Most IP blocklist providers return bitmask or absolute value data types. Within these data
types, the IP blocklist provider can use multiple values to classify the IP address by threat type.

There are issues to consider when using IP blocklist providers:

     Outages or delays at the IP blocklist provider service can cause delays in the processing of
     messages on the Edge Transport server. You should always select reliable IP blocklist
     providers.

     Source servers that you know to be legitimate can be erroneously identified as spam
     sources. For example, the mail server can be unintentionally configured to act as an open
     relay. You should always select IP blocklist providers that provide clear procedures for
     evaluation and removal from their services.

Bitmask and absolute value examples
This section shows an example of the status codes returned by most blocklist providers. For
details about the status codes that the provider returns, see the documentation from the
specific provider.

For bitmask data types, the IP blocklist provider service returns a status code of 127.0.0. x,
where the integer x is any one of the values listed in the following table.

Values and status codes for bitmask data types

                                                                                  ﾉ   Expand table

 Value        Status code

 1            The IP address is on an IP blocklist.

 2            The SMTP server is configured to act as an open relay.

 4            The IP address supports a dial-up IP address.

For absolute value types, the IP blocklist provider returns explicit responses that define why the
IP address is defined in their blocklist. The following table shows examples of absolute values
and the explicit responses.

Values and status codes for absolute value data types

                                                                                  ﾉ   Expand table

<!-- p.3018 -->

 Value       Explicit response

 127.0.0.2   The IP address is a direct spam source.

 127.0.0.4   The IP address is a bulk mailer.

 127.0.0.5   The remote server sending the message is known to support multistage open relays.

IP allowlist providers
IP Allowlist providers are also known as safe lists. IP allowlist providers are configured just like
IP blocklist providers, but the results are the opposite: they define mail server IP addresses that
are definitely not associated with spam activity. If the IP address of the connecting mail server
is defined at an IP allowlis provider, the message is exempt from processing by other Exchange
antispam agents. For this reason, IP blocklist providers are used much more frequently than IP
allowlis providers. Choose your IP allowlis providers carefully.

Test IP blocklist providers and IP allowlis providers
After you configure connection filtering to use an IP blocklist provider or an IP allowlist
provider, you can run tests to verify that the providers are working correctly. Most providers
provide test IP addresses that you can use to test their services. When you test a provider, the
Connection Filtering agent issues a DNS query that should result in a specific response from
the provider. For more information about how to test IP addresses against an IP blocklist
provider service or an IP allowlis provider service, see Connection filtering procedures on Edge
Transport servers.

Configure connection filtering on Edge Transport
servers that aren't directly connected to the
Internet
You can use connection filtering on Edge Transport servers that don't directly receive email
from the Internet. In this scenario, the Edge Transport server is behind another mail server that
receives and processes messages directly from the Internet. For example, your organization
might send email traffic through an antispam server, service, or appliance before the messages
reach the Edge Transport server. In this scenario, the Connection Filtering agent needs to
extract the correct source IP address from the message. To do this, the Connection Filtering
agent needs to parse the Received header field values in the message header and compare
those values to the known IP addresses of the mail server that sits between the Edge Transport
server and the Internet.

<!-- p.3019 -->

Every mail server that accepts and relays an SMTP message along the delivery path adds its
own Received header field in the message header. The Received header typically contains the
domain name and IP address of the mail server that processed the message.

If the Edge Transport server doesn't accept messages directly from the Internet, you need to
use the InternalSMTPServers parameter on the Set-TransportConfig cmdlet on an Exchange
Mailbox server to identify the IP address of the mail server that sit between the Edge Transport
server and the Internet. The IP address data is replicated to Edge Transport servers by
EdgeSync. When messages are received by the Edge Transport server, the Connection Filtering
agent assumes an IP address in a Received header field that doesn't match a value specified by
the InternalSMTPServers parameter is the source IP address that needs to be checked.
Therefore, you need specify all internal SMTP servers in order for connection filtering to
function correctly.

<!-- p.3020 -->

Connection filtering procedures on Edge
Transport servers
Article • 04/30/2025

APPLIES TO:          2016      2019       Subscription Edition

Connection filtering is an antispam feature that's provided by the Connection Filtering agent,
which is available only on Edge Transport servers in Exchange Server. Connection filtering
enables the following features:

      IP blocklist
      IP blocklist providers
      IP allowlist
      IP allowlist providers

Each of these features can be enabled or disabled separately.

For more information about connection filtering, see Connection filtering on Edge Transport
servers.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Antispam features" entry in the
      Antispam and anti-malware permissions topic.

      You can only use PowerShell to perform this procedure. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online            , or Exchange Online Protection .

<!-- p.3021 -->

Use the Exchange Management Shell to enable or
disable connection filtering
To completely enable or disable connection filtering, you enable or disable the Connection
Filtering agent. The change takes effect after you restart the Microsoft Exchange Transport
service. When you restart the Microsoft Exchange service on an Edge Transport server, mail
flow on the server is temporarily interrupted.

To disable connection filtering, run the following command:

  PowerShell

  Disable-TransportAgent "Connection Filtering Agent"

To enable connection filtering, run the following command:

  PowerShell

  Enable-TransportAgent "Connection Filtering Agent"

To make the change take effect, restart the Microsoft Exchange Transport service by running
the following command:

  PowerShell

  Restart-Service MSExchangeTransport

How do you know this worked?
To verify that you successfully enabled or disabled connection filtering, run the following
command to verify the Enabled property value.

  PowerShell

  Get-TransportAgent "Connection Filtering Agent" | Format-List Enabled

IP blocklist procedures
These procedures apply to the IP blocklist that you manually configure. They don't apply to IP
blocklist providers.

<!-- p.3022 -->

Use the IPBlockListConfig cmdlets to view and configure how connection filtering uses the IP
blocklist. Use the IPBlockListEntry cmdlets to view and configure the IP addresses in the IP
blocklist.

Use the Exchange Management Shell to view the
configuration of the IP blocklist
To view the configuration of the IP blocklist, run the following command:

  PowerShell

  Get-IPBlockListConfig | Format-List *Enabled,*Response

Use the Exchange Management Shell to enable or disable the
IP blocklist
To disable the IP blocklist, run the following command:

  PowerShell

  Set-IPBlockListConfig -Enabled $false

To enable the IP blocklist, run the following command:

  PowerShell

  Set-IPBlockListConfig -Enabled $true

For more information, see Set-IPBlockListConfig.

How do you know this worked?
To verify that you successfully enabled or disabled the IP blocklist, run the following command
to verify the Enabled property value.

  PowerShell

  Get-IPBlockListConfig | Format-List Enabled

<!-- p.3023 -->

Use the Exchange Management Shell to configure the IP
blocklist
To configure the IP blocklist, use the following syntax:

  PowerShell

  Set-IPBlockListConfig [-ExternalMailEnabled <$true | $false>] [-
  InternalMailEnabled <$true | $false> -MachineEntryRejectionResponse "<Custom
  response text>"] [-StaticEntryRejectionResponse "<Custom response text>"]

This example configures the IP blocklist with the following settings:

     The IP blocklist filters incoming connections from internal and external mail servers. By
     default, connections are filtered from external mail servers only (ExternalMailEnabled is set
     to $true , and InternalMailEnabled is set to $false ). Non-authenticated connections and
     authenticated connections from external partners are considered external.

     The custom response text for connections that were filtered by IP addresses that were
     automatically added to the IP blocklist by the sender reputation feature of the Protocol
     Analysis agent is set to the value "Connection from IP address {0} was rejected by sender
     reputation."

     The custom response text for connections that were filtered by IP addresses that were
     manually added to the IP blocklist is set to the value "Connection from IP address {0} was
     rejected by connection filtering."

  PowerShell

  Set-IPBlockListConfig -InternalMailEnabled $true -MachineEntryRejectionResponse
  "Connection from IP address {0} was rejected by sender reputation." -
  StaticEntryRejectionResponse "Connection from IP address {0} was rejected by
  connection filtering."

For more information, see Set-IPBlockListConfig.

How do you know this worked?
To verify that you successfully configured the IP blocklist, run the following command to verify
the property values.

  PowerShell

<!-- p.3024 -->

  Get-IPBlockListConfig | Format-List *MailEnabled,*Response

Use the Exchange Management Shell to view IP blocklist
entries
To view all IP blocklist entries, run the following command:

  PowerShell

  Get-IPBlockListEntry

Note that each IP blocklist entry is identified by an integer value. The identity integer is
assigned in ascending order when you add entries to the IP blocklist and the IP allowlist.

To view a specific IP blocklist entry, use the following syntax:

  PowerShell

  Get-IPBlockListEntry <-Identity IdentityInteger | -IPAddress IPAddress>

For example, to view the IP blocklist entry that contains the IP address 192.168.1.13, run the
following command:

  PowerShell

  Get-IPBlockListEntry -IPAddress 192.168.1.13

For more information, see Get-IPBlockListEntry.

  ７ Note

  When you use the IPAddress parameter, the resulting IP blocklist entry can be an individual
  IP address, an IP address range, or a Classless InterDomain Routing (CIDR) IP. To use the
  Identity parameter, you specify the integer value that's assigned to the IP blocklist entry.

Use the Exchange Management Shell to add IP blocklist
entries
To add IP blocklist entries, use the following syntax:

<!-- p.3025 -->

  PowerShell

  Add-IPBlockListEntry <-IPAddress IPAddress | -IPRange IP range or CIDR IP> [-
  ExpirationTime <DateTime>] [-Comment "<Descriptive Comment>"]

This example adds the IP blocklist entry for the IP address range 192.168.1.10 through
192.168.1.15 and configures the IP blocklist entry to expire on July 4, 2018 at 15:00.

  PowerShell

  Add-IPBlockListEntry -IPRange 192.168.1.10-192.168.1.15 -ExpirationTime "7/4/2018
  15:00"

For more information, see Add-IPBlockListEntry.

How do you know this worked?

To verify that you successfully added an IP blocklist entry, run the following command and
verify that the new IP blocklist entry is displayed.

  PowerShell

  Get-IPBlockListEntry

Use the Exchange Management Shell to remove IP blocklist
entries
To remove IP blocklist entries, use the following syntax:

  PowerShell

  Remove-IPBlockListEntry <IdentityInteger>

This example removes the IP blocklist entry that has the Identity value 3.

  PowerShell

  Remove-IPBlockListEntry 3

This example removes the IP blocklist entry that contains the IP address 192.168.1.12 without
using the Identity integer value. Note that the IP blocklist entry can be an individual IP address
or an IP address range.

<!-- p.3026 -->

  PowerShell

  Get-IPBlockListEntry -IPAddress 192.168.1.12 | Remove-IPBlockListEntry

For more information, see Remove-IPBlockListEntry.

How do you know this worked?
To verify that you successfully removed an IP blocklist entry, run the following command and
verify that the IP blocklist entry you removed is gone.

  PowerShell

  Get-IPBlockListEntry

IP blocklist provider procedures
These procedures apply to IP blocklist providers. They don't apply to the IP blocklist.

Use the IPBlockListProvidersConfig cmdlets to view and configure how connection filtering
uses all IP blocklist providers. Use the IPBlockListProvider cmdlets to view, configure, and test
IP blocklist providers.

Use the Exchange Management Shell to view the
configuration of all IP blocklist providers
To view how connection filtering uses all IP blocklist providers, run the following command:

  PowerShell

  Get-IPBlockListProvidersConfig | Format-List *Enabled,Bypassed*

For more information, see Get-IPBlockListProvidersConfig.

Use the Exchange Management Shell to enable or disable all
IP blocklist providers
To disable all IP blocklist providers, run the following command:

  PowerShell

<!-- p.3027 -->

  Set-IPBlockListProvidersConfig -Enabled $false

To enable all IP blocklist providers, run the following command:

  PowerShell

  Set-IPBlockListProvidersConfig -Enabled $true

For more information, see Set-IPBlockListProvidersConfig.

How do you know this worked?

To verify that you enabled or disabled all IP blocklist providers, run the following command to
verify the value of the Enabled property:

  PowerShell

  Get-IPBlockListProvidersConfig | Format-List Enabled

Use the Exchange Management Shell to configure all IP
blocklist providers
To configure how connection filtering uses all IP blocklist providers, use the following syntax:

  PowerShell

  Set-IPBlockListProvidersConfig [-BypassedRecipients <recipient1,recipient2...>] [-
  ExternalMailEnabled <$true | $false>] [-InternalMailEnabled <$true | $false>]

This example configures all IP blocklist providers with the following settings:

     IP blocklist providers filter incoming connections from internal and external mail servers.
     By default, connections are filtered from external mail servers only (ExternalMailEnabled is
     set to $true , and InternalMailEnabled is set to $false ). Non-authenticated connections
     and authenticated connections from external partners are considered external.

     Messages sent to the internal recipients chris@fabrikam.com and michelle@fabrikam.com
     are excluded from filtering by IP blocklist providers. Note that if you want to add
     recipients to the list without affecting existing recipients, use the syntax, @{Add="
     <recipient1>","<recipient2>"...} .

<!-- p.3028 -->

  PowerShell

  Set-IPBlockListProvidersConfig -BypassedRecipients
  chris@fabrikam.com,michelle@fabrikam.com -InternalMailEnabled $true

For more information, see Set-IPBlockListProvidersConfig.

How do you know this worked?

To verify that you successfully configured all IP blocklist providers, run the following command
to verify the property values:

  PowerShell

  Get-IPBlockListProvidersConfig | Format-List *MailEnabled,Bypassed*

Use the Exchange Management Shell to view IP blocklist
providers
To view the summary list of all the IP blocklist providers, run the following command:

  PowerShell

  Get-IPBlockListProvider

To view the details of a specific provider, use the following syntax:

  PowerShell

  Get-IPBlockListProvider <IPBlockListProviderIdentity>

This example shows the details of the provider named Contoso IP blocklist Provider.

  PowerShell

  Get-IPBlockListProvider "Contoso IP blocklist Provider" | Format-List
  Name,Enabled,Priority,LookupDomain,*Match,*Response

For more information, see Get-IPBlockListProvider.

<!-- p.3029 -->

Use the Exchange Management Shell to add an IP blocklist
provider
To add an IP blocklist provider, use the following syntax:

  PowerShell

  Add-IPBlockListProvider -Name "<Descriptive Name>" -LookupDomain <FQDN> [-Priority
  <Integer>] [-Enabled <$true | $false>] [-AnyMatch <$true | $false>] [-BitmaskMatch
  <IPAddress>] [-IPAddressesMatch <IPAddressStatusCode1,IPAddressStatusCode2...>] [-
  RejectionResponse "<Custom Text>"]

This example creates an IP blocklist provider named "Contoso IP blocklist Provider" with the
following options:

     FQDN to use the provider: rbl.contoso.com

     Bitmask code to use from the provider: 127.0.0.1

  PowerShell

  Add-IPBlockListProvider -Name "Contoso IP blocklist Provider" -LookupDomain
  rbl.contoso.com -BitmaskMatch 127.0.0.1

  ７ Note

  When you add a new IP blocklist provider, it's enabled by default (the value of Enabled is
  $true ), and the priority value is incremented (the first entry has the Priority value 1).

For more information, see Add-IPBlockListProvider.

How do you know this worked?

To verify that you successfully added an IP blocklist provider, run the following command and
verify that the new IP blocklist provider is displayed.

  PowerShell

  Get-IPBlockListProvider

Use the Exchange Management Shell to enable or disable an
IP blocklist provider

<!-- p.3030 -->

To enable or disable a specific IP blocklist provider, use the following syntax:

  PowerShell

  Set-IPBlockListProvider <IPBlockListProviderIdentity> -Enabled <$true | $false>

This example disables the provider named Contoso IP blocklist Provider.

  PowerShell

  Set-IPBlockListProvider "Contoso IP blocklist Provider" -Enabled $false

This example enables the provider named Contoso IP blocklist Provider.

  PowerShell

  Set-IPBlockListProvider "Contoso IP blocklist Provider" -Enabled $true

For more information, see Set-IPBlockListProvider.

How do you know this worked?

To verify that you successfully enabled or disabled an IP blocklist provider, run the following
command to verify the value of the Enabled property:

  PowerShell

  Get-IPBlockListProvider | Format-Table -Auto Name,LookupDomain,Priority,Enabled

Use the Exchange Management Shell to configure an IP
blocklist provider
The configuration options that are available on the Set-IPBlockListProvider cmdlet are
identical to those on the Add-IPBlockListProvider cmdlet.

To configure an existing IP blocklist provider, use the following syntax:

  PowerShell

  Set-IPBlockListProvider <IPBlockListProviderIdentity> -Name "<Descriptive Name>" -
  LookupDomain <FQDN> [-Priority <Integer>] [-AnyMatch <$true | $false>] [-
  BitmaskMatch <IPAddress>] [-IPAddressesMatch

<!-- p.3031 -->

  <IPAddressStatusCode1,IPAddressStatusCode2...>] [-RejectionResponse "<Custom
  Text>"]

For example, to add the IP address status code 127.0.0.1 to the list of existing status codes for
the provider named Contoso IP blocklist Provider, run the following command:

  PowerShell

  Set-IPBlockListProvider "Contoso IP blocklist Provider" -IPAddressesMatch
  @{Add="127.0.0.1"}

For more information, see Set-IPBlockListProvider.

How do you know this worked?
To verify that you successfully configured an IP blocklist provider, run the following command
to verify the property values. Be sure to replace <IPBlockListProviderIdentity> with the name of
the IP blocklist provider.

  PowerShell

  Get-IPBlockListProvider <IPBlockListProviderIdentity> | Format-List

Use the Exchange Management Shell to test an IP blocklist
provider
To test an IP blocklist provider, use the following syntax:

  PowerShell

  Test-IPBlockListProvider <IPBlockListProviderIdentity> -IPAddress
  <IPAddressToTest>

This example tests the provider named Contoso IP blocklist Provider by looking up the IP
address 192.168.1.1.

  PowerShell

  Test-IPBlockListProvider "Contoso IP blocklist Provider" -IPAddress 192.168.1.1

For more information, see Test-IPBlockListProvider.

<!-- p.3032 -->

Use the Exchange Management Shell to remove an IP blocklist
provider
To remove an IP blocklist provider, use the following syntax:

  PowerShell

  Remove-IPBlockListProvider <IPBlockListProviderIdentity>

This example removes the IP blocklist provider named Contoso IP blocklist Provider.

  PowerShell

  Remove-IPBlockListProvider "Contoso IP blocklist Provider"

For more information, see Remove-IPBlockListProvider.

How do you know this worked?
To verify that you successfully removed an IP blocklist provider, run the following command
and verify that the IP blocklist provider you removed is gone.

  PowerShell

  Get-IPBlockListProvider

IP allowlist procedures
These procedures apply to the IP allowlist that you manually configure. They don't apply to IP
allowlist providers.

Use the IPAllowListConfig cmdlets to view and configure how connection filtering uses the IP
allowlist. Use the IPAllowListEntry cmdlets to view and configure the IP addresses in the IP
allowlist.

Use the Exchange Management Shell to view the
configuration of the IP allowlist
To view the configuration of the IP allowlist, run the following command.

  PowerShell

<!-- p.3033 -->

  Get-IPAllowListConfig | Format-List *Enabled

For more information, see Get-IPAllowListConfig.

Use the Exchange Management Shell to enable or disable the
IP allowlist
To disable the IP allowlist, run the following command:

  PowerShell

  Set-IPAllowListConfig -Enabled $false

To enable the IP allowlist, run the following command:

  PowerShell

  Set-IPAllowListConfig -Enabled $true

How do you know this worked?
To verify that you successfully enabled or disabled the IP allowlist, run the following command
to verify the value of the Enabled property:

  PowerShell

  Get-IPAllowListConfig | Format-List Enabled

Use the Exchange Management Shell to configure the IP
allowlist
To configure the IP allowlist, use the following syntax:

  PowerShell

  Set-IPAllowListConfig [-ExternalMailEnabled <$true | $false>] [-
  InternalMailEnabled <$true | $false>

This example configures the IP allowlist to filter incoming connections from internal and
external mail servers. By default, connections are filtered from external mail servers only

<!-- p.3034 -->

(ExternalMailEnabled is set to $true , and InternalMailEnabled is set to $false ). Non-
authenticated connections and authenticated connections from external partners are
considered external.

  PowerShell

  Set-IPAllowListConfig -InternalMailEnabled $true

For more information, see Set-IPAllowListConfig.

How do you know this worked?

To verify that you successfully configured the IP allowlist, run the following command to verify
the property values:

  PowerShell

  Get-IPAllowListConfig | Format-List *MailEnabled

Use the Exchange Management Shell to view IP allowlist
entries
To view all IP allowlist entries, run the following command:

  PowerShell

  Get-IPAllowListEntry

Note that each IP allowlist entry is identified by an integer value. The identity integer is
assigned in ascending order when you add entries to the IP blocklist and the IP allowlist.

To view a specific IP allowlist entry, use the following syntax:

  PowerShell

  Get-IPAllowListEntry <-Identity IdentityInteger | -IPAddress IPAddress>

For example, to view the IP allowlist entry that contains the IP address 192.168.1.13, run the
following command:

  PowerShell

<!-- p.3035 -->

  Get-IPAllowListEntry -IPAddress 192.168.1.13

For more information, see Get-IPAllowListEntry.

  ７ Note

  When you use the IPAddress parameter, the resulting IP allowlist entry can be an individual
  IP address, an IP address range, or a Classless InterDomain Routing (CIDR) IP. To use the
  Identity parameter, you specify the integer value that's assigned to the IP allowlist entry.

Use the Exchange Management Shell to add IP allowlist
entries
To add IP allowlist entries, use the following syntax:

  PowerShell

  Add-IPAllowListEntry <-IPAddress IPAddress | -IPRange IP range or CIDR IP> [-
  ExpirationTime <DateTime>] [-Comment "<Descriptive Comment>"]

This example adds the IP allowlist entry for the IP address range 192.168.1.10 through
192.168.1.15 and configures the IP allowlist entry to expire on July 4, 2018 at 15:00.

  PowerShell

  Add-IPAllowListEntry -IPRange 192.168.1.10-192.168.1.15 -ExpirationTime "7/4/2018
  15:00"

For more information, see Add-IPAllowListEntry.

How do you know this worked?

To verify that you successfully added an IP allowlist entry, run the following command and
verify that the new IP allowlist entry is displayed.

  PowerShell

  Get-IPAllowListEntry

<!-- p.3036 -->

Use the Exchange Management Shell to remove IP allowlist
entries
To remove IP allowlist entries, use the following syntax:

  PowerShell

  Remove-IPAllowListEntry <IdentityInteger>

This example removes the IP allowlist entry that has the Identity value 3.

  PowerShell

  Remove-IPAllowListEntry 3

This example removes the IP allowlist entry that contains the IP address 192.168.1.12 without
using the Identity integer value. Note that the IP allowlist entry can be an individual IP address
or an IP address range.

  PowerShell

  Get-IPAllowListEntry -IPAddress 192.168.1.12 | Remove-IPAllowListEntry

For more information, see Remove-IPAllowListEntry.

How do you know this worked?

To verify that you successfully removed an IP allowlist entry, run the following command and
verify that the IP allowlist entry you removed is gone.

  PowerShell

  Get-IPAllowListEntry

IP allowlist provider procedures
These procedures apply to IP allowlist providers. They don't apply to the IP allowlist.

Use the IPAllowListProvidersConfig cmdlets to view and configure how connection filtering
uses all IP allowlist providers. Use the IPAllowListProvider cmdlets to view, configure, and test
IP allowlist providers.

<!-- p.3037 -->

Use the Exchange Management Shell to view the
configuration of all IP allowlist providers
To view how connection filtering uses all IP allowlist providers, run the following command:

  PowerShell

  Get-IPAllowListProvidersConfig | Format-List *Enabled

For more information, see Get-IPAllowListProvidersConfig.

Use the Exchange Management Shell to enable or disable all
IP allowlist providers
To disable all IP allowlist providers, run the following command:

  PowerShell

  Set-IPAllowListProvidersConfig -Enabled $false

To enable all IP allowlist providers, run the following command:

  PowerShell

  Set-IPAllowListProvidersConfig -Enabled $true

For more information, see Set-IPAllowListProvidersConfig.

How do you know this worked?

To verify that you enabled or disabled all IP allowlist providers, run the following command to
verify the Enabled property value:

  PowerShell

  Get-IPAllowListProvidersConfig | Format-List Enabled

Use the Exchange Management Shell to configure all IP
allowlist providers
To configure how connection filtering uses all IP allowlist providers, use the following syntax:

<!-- p.3038 -->

  PowerShell

  Set-IPAllowListProvidersConfig [-ExternalMailEnabled <$true | $false>] [-
  InternalMailEnabled <$true | $false>]

This example configures all IP allowlist providers to filter incoming connections from internal
and external mail servers. By default, connections are filtered from external mail servers only
(ExternalMailEnabled is set to $true , and InternalMailEnabled is set to $false ). Non-
authenticated connections and authenticated connections from external partners are
considered external.

  PowerShell

  Set-IPAllowListProvidersConfig -InternalMailEnabled $true

For more information, see Set-IPAllowListProvidersConfig.

How do you know this worked?
To verify that you successfully configured all IP allowlist providers, run the following command
to verify the property values:

  PowerShell

  Get-IPAllowListProvidersConfig | Format-List *MailEnabled

Use the Exchange Management Shell to view IP allowlist
providers
To view the summary list of all the IP allowlist providers, run the following command.

  PowerShell

  Get-IPAllowListProvider

To view the details of a specific provider, use the following syntax:

  PowerShell

  Get-IPAllowListProvider <IPAllowListProviderIdentity>

This example shows the details of the provider named Contoso IP allowlist Provider.

<!-- p.3039 -->

  PowerShell

  Get-IPAllowListProvider "Contoso IP allowlist Provider" | Format-List
  Name,Enabled,Priority,LookupDomain,*Match

For more information, see Get-IPAllowListProvider.

Use the Exchange Management Shell to add an IP allowlist
provider
To add an IP allowlist provider, use the following syntax:

  PowerShell

  Add-IPAllowListProvider -Name "<Descriptive Name>" -LookupDomain <FQDN> [-Priority
  <Integer>] [-Enabled <$true | $false>] [-AnyMatch <$true | $false>] [-BitmaskMatch
  <IPAddress>] [-IPAddressesMatch <IPAddressStatusCode1,IPAddressStatusCode2...>]

This example creates an IP allowlist provider named "Contoso IP allowlist Provider" with the
following options:

     FQDN to use the provider: allow.contoso.com

     Bitmask code to use from the provider: 127.0.0.1

  PowerShell

  Add-IPAllowListProvider -Name "Contoso IP allowlist Provider" -LookupDomain
  allow.contoso.com -BitmaskMatch 127.0.0.1

  ７ Note

  When you add a new IP allowlist provider, it's enabled by default (the value of Enabled is
  $true ), and the priority value is incremented (the first entry has the Priority value 1).

For more information, see Add-IPAllowListProvider.

How do you know this worked?
To verify that you successfully added an IP allowlist provider, run the following command and
verify that the new IP allowlist provider is displayed.

<!-- p.3040 -->

  PowerShell

  Get-IPAllowListProvider

Use the Exchange Management Shell to enable or disable an
IP allowlist provider
To enable or disable a specific IP allowlist provider, use the following syntax:

  PowerShell

  Set-IPAllowListProvider <IPAllowListProviderIdentity> -Enabled <$true | $false>

This example disables the provider named Contoso IP allowlist Provider.

  PowerShell

  Set-IPAllowListProvider "Contoso IP allowlist Provider" -Enabled $false

This example enables the provider named Contoso IP allowlist Provider.

  PowerShell

  Set-IPAllowListProvider "Contoso IP allowlist Provider" -Enabled $true

For more information, see Set-IPAllowListProvider.

How do you know this worked?
To verify that you successfully enabled or disabled an IP allowlist provider, run the following
command to verify the Enabled property value:

  PowerShell

  Get-IPAllowListProvider | Format-Table -Auto Name,LookupDomain,Priority,Enabled

Use the Exchange Management Shell to configure an IP
allowlist provider
The configuration options that are available on the Set-IPAllowListProvider cmdlet are
identical to those on the Add-IPAllowListProvider cmdlet.
