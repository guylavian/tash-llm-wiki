---
title: "Exchange Server — pages 1841-1880"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1841-1880
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1841-1880
family: exchange
documentKind: "doc"
abstract: "Configure the transient failure retry attempts, the transient failure retry interval, and the outbound connection failure retry interval Transient failure retry attempts: The number of connection attempts that are tried after the connection attempts controlled by the QueueGlitch"
---

# Exchange Server — pages 1841-1880

<!-- p.1841 -->

Configure the transient failure retry attempts, the
transient failure retry interval, and the outbound
connection failure retry interval
    Transient failure retry attempts: The number of connection attempts that are tried after
    the connection attempts controlled by the QueueGlitchRetryCount and
    QueueGlitchRetryInterval keys have failed. A valid value is 0 through 15, and the default
    value is 6. If you set the value to 0, the next connection attempt is controlled by the
    outbound connection failure retry interval.

    Transient failure retry interval: The interval between each transient failure retry attempt.
    On Mailbox servers, the default value is 5 minutes. On Edge Tranport Servers, the default
    value is 10 minutes.

    Outbound connection failure retry interval: The retry interval for outgoing connection
    attempts that have previously failed (the transient failure retry attempts and the transient
    failure retry interval). On Mailbox servers, the default value is 10 minutes. On Edge
    Tranport Servers, the default value is 30 minutes.

Use the EAC to configure the transient failure retry attempts,
the transient failure retry interval, or the outbound
connection failure retry interval on Mailbox servers
  1. In the EAC, go to Servers > Servers, select the server, and then click Edit   .

  2. In the server properties window that opens, click Transport limits.

  3. In the Retries section, enter a value for any of these settings:

          Outbound connection failure retry interval (seconds)

          Transient failure retry interval (minutes)

          Transient failure retry attempts

    When you're finished, click Save.

Use the Exchange Management Shell to configure the
transient failure retry attempts, the transient failure retry
interval, and the outbound connection failure retry interval on
Mailbox severs or Edge Transport servers

<!-- p.1842 -->

To configure the intervals in the Transport service on Mailbox servers or Edge Transport servers,
use this syntax:

  PowerShell

  Set-TransportService -Identity <ServerIdentity> -TransientFailureRetryCount
  <Integer> -TransientFailureRetryInterval <hh:mm:ss> -
  OutboundConnectionFailureRetryInterval <dd.hh:mm:ss>

To configure the intervals in the Front End Transport service on Mailbox servers, use this syntax:

  PowerShell

  Set-FrontEndTransportService -Identity <ServerIdentity> -
  TransientFailureRetryCount <Integer> -TransientFailureRetryInterval <hh:mm:ss>

This example changes the following values on the Mailbox server named Mailbox01:

     The number of transient failure retry attempts is set to 8.

     The transient failure retry interval is set to 1 minute.

     The outbound connection failure retry interval is set to 45 minutes.

  PowerShell

  Set-TransportService -Identity Mailbox01 -TransientFailureRetryCount 8 -
  TransientFailureRetryInterval 00:01:00 -OutboundConnectionFailureRetryInterval
  00:45:00

How do you know this worked?
To verify that you've configured these intervals, do any of these steps:

     On a Mailbox server, open the EAC and go to Servers > Servers, select the server, and
     then click Edit   . In the server properties window that opens, click Transport limits, and
     verify the values in the Retries section.

     In the Exchange Management Shell on a Mailbox server or Edge Transport server, run this
     command to verify the property values:

        PowerShell

        Get-TransportService | Format-List
        Name,TransientFailureRetry*,OutboundConnectionFailureRetryInterval

<!-- p.1843 -->

     In the Exchange Management Shell on a Mailbox serve, run this command to verify the
     property values:

        PowerShell

        Get-FrontEndTransportService | Format-List Name,TransientFailureRetry*

Use the Exchange Management Shell to configure
the message retry interval
The message retry interval specifies how long to wait between sending attempts for individual
messages in queues that have a status of Retry. The default value is 15 minutes, and we
recommend that you don't change the default value unless you're directed to do so by
Microsoft Customer Service and Support, or specific product documentation.

To configure the message retry interval, use this syntax:

  PowerShell

  Set-TransportService -Identity <ServerIdentity> -MessageRetryInterval
  <dd.hh:mm:ss>

This example changes the message retry interval to 20 minutes on the Mailbox server named
Mailbox01.

  PowerShell

  Set-TransportService -Identity Mailbox01 -MessageRetryInterval 00:20:00

How do you know this worked?
To verify that you've configured the message retry interval on a Mailbox server or Edget
Transport server, run this command in the Exchange Management Shell to verify the
MessageRetryInterval property value:

  PowerShell

  Get-TransportService | Format-List Name,MessageRetryInterval

Configure the delay DSN timeout settings

<!-- p.1844 -->

     Delay DSN message notification timeout interval: How long to wait before sending
     delay DSN messages to senders. This setting applies to the Transport service on a Mailbox
     server or an Edge Transport server.

Note: This value should always be greater than the transient failure retry count multiplied by
the transient failure retry interval (the default total is 30 minutes on a Mailbox server, and one
hour on an Edge Transport server).

     Internal and external delay DSN settings: Specifies whether delay DSN messages can be
     sent to internal or external message senders (senders who are inside or outside the
     Exchange organization). This setting applies to the Transport service on all Mailbox
     servers in the organization.

Use the EAC to configure the delay DSN message notification
timeout interval on Mailbox servers
   1. In the EAC, click Servers > Servers, select the server, and then click Edit   .

   2. In the server properties window that opens, click Transport limits.

   3. In the Notifications section, enter a value for Notify sender when message is delayed
     after (hours), and then click Save.

Use the Exchange Management Shell to configure the delay
DSN message notification timeout interval on Mailbox servers
or Edge Transport servers
To configure the delay DSN message notification timeout interval, use this syntax:

  PowerShell

  Set-TransportService -Identity <ServerIdentity> -DelayNotificationTimeout
  <dd.hh:mm:ss>

This example changes the delay DSN message notification timeout interval to 6 hours on the
Mailbox server named Mailbox01.

  PowerShell

  Set-TransportService -Identity Mailbox01 -DelayNotificationTimeout 06:00:00

<!-- p.1845 -->

Use the Exchange Management Shell to enable or disable the
sending of delay DSN notifications to external or internal
message senders
To configure the delay DSN notification settings, use this syntax:

  PowerShell

  Set-TransportConfig -ExternalDelayDSNEnabled <$true | $false> -
  InternalDelayDSNEnabled <$true |$false>

This example prevents the sending of delay DSN notification messages to external senders.

  PowerShell

  Set-TransportConfig -ExternalDelayDSNEnabled $false

This example prevents the sending of delay DSN notification messages to internal senders.

  PowerShell

  Set-TransportConfig -InternalDelayDSNEnabled $false

How do you know this worked?
To verify that you've configured the delay DSN timeout settings, do any of these steps:

     On a Mailbox server, open the EAC and go to Servers > Servers, select the server, and
     then click Edit   . In the server properties window that opens, click Transport limits, and
     verify the Notify sender when message is delayed after (hours) value in the
     Notifications section.

     In the Exchange Management Shell on a Mailbox server or Edge Transport server, run
     these commands to verify the property values:

        PowerShell

        Get-TransportService | Format-List Name,DelayNotificationTimeout

        PowerShell

        Get-TransportConfig | Format-List *DelayDSNEnabled

<!-- p.1846 -->

Configure the message expiration timeout interval
The message expiration timeout interval specifies how long to wait before the message expires
and is returned to the sender in a non-delivery report (also known as an NDR or bounce
message). This setting applies to the Transport service on a Mailbox server or an Edge
Transport server.

Use the EAC to configure the message expiration timeout
interval on Mailbox servers
   1. In the EAC, click Servers > Servers, select the server, and then click Edit   .

   2. In the server properties window that opens, click Transport limits.

   3. In the Message expiration section, enter a value for Maximum time since submission
     (days), and then click Save.

Use the Exchange Management Shell to configure the
message expiration timeout interval on Mailbox servers or
Edge Transport servers
To configure the message expiration timeout interval, use the following syntax.

  PowerShell

  Set-TransportService -Identity <ServerIdentity> -MessageExpirationTimeout
  <dd.hh:mm:ss>

This example changes the message expiration timeout interval to 4 days on the Exchange
server named Mailbox01.

  PowerShell

  Set-TransportService -Identity Mailbox01 -MessageExpirationTimeout 4.00:00:00

How do you know this worked?
To verify that you've configured the message expiration timeout interval, do any of these steps:

     On a Mailbox server, open the EAC and go to Servers > Servers, select the server, and
     then click Edit   . In the server properties window that opens, click Transport limits, and

<!-- p.1847 -->

verify the Maximum time since submission (days) value in the Message expiration
section.

In the Exchange Management Shell on a Mailbox server or Edge Transport server, run this
command to verify the MessageExpirationTimeout property value:

  PowerShell

  Get-TransportService | Format-List Name,MessageExpirationTimeout

<!-- p.1848 -->

DSNs and NDRs in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019        Subscription Edition

When there's a problem delivering a message, Exchange sends an NDR to the message sender
that indicates there was a problem. NDRs include a code that indicates why the message wasn't
delivered, and possible solutions to help get the message delivered.

The information that's included in NDRs is designed to be easy to read and helpful for both
users and administrators. In some cases, senders can identify and fix their own problems (for
example, when there's a typo in the recipient's email address). In other cases, an administrator
might need to fix an issue in the Exchange environment, or notify the administrators in the
destination domain about problems in their messaging environment.

For procedures related to NDRs in Exchange Server, see Procedures for DSNs and NDRs in
Exchange Server.

If you need help with NDRs in Microsoft 365, Office 365, or Exchange Online, see Email non-
delivery reports in Exchange Online.

Information in NDRs
This is an example of an NDR:

<!-- p.1849 -->

The information in an NDR is separated into two sections:

   1. User information section: This section appears first and attempts to explain (in non-
     technical terms) why delivery of the message failed, and possible steps to successfully
     deliver the message.

       ７ Note

       This section can display content in any language other than English.

          The text that's displayed in this section is inserted by the Exchange server that
          generated the NDR.

          When applicable, the fully qualified domain name (FQDN) of the server that rejected
          the message is included in the user information section (for example
          mbx01.contoso.com).

          If delivery failed for multiple recipients, the email address and reason for failure is
          listed for each recipient is listed..

   2. Diagnostic information for administrators section: This section provides deeper
     technical information to help administrators troubleshoot the issues that caused the

<!-- p.1850 -->

delivery failure. A key piece of information in this section is the enhanced status code (for
example, 4.4.7).

  ７ Note

  This section will display some of the content in English and some in other language.

     The enhanced status code is returned by the server that generated the NDR (the
     source server that couldn't deliver the message, or the destination server that
     rejected the message).

     The enhanced status code determines the text that's displayed in the user
     information section (the code value isn't altered by Exchange).

You can use the New-SystemMessage cmdlet in the Exchange Management Shell to
modify the text that appears in user information section for a given enhanced status code
(including different text in different languages). By creating custom explanations, you can
provide specific content for your environment, such as contact information for your help
desk, or links to your Intranet for self-service support. For more information, see
Procedures for DSNs and NDRs in Exchange Server.

     The Common enhanced status codes section in this topic explains what the numbers
     mean, the codes that you're likely to encounter, and suggestions to fix the
     underlying problem that prevented the message from being delivered.

The following information is also available in this section:

     Generating server: The messaging server that created the NDR. If a remote server
     isn't listed below the sender's email address, the generating server is also the server
     that rejected the original email message. If message delivery fails between senders
     and recipients in the Exchange organization, the same server typically rejects the
     original message and generates the NDR.

     The rejected recipients: The recipient's email address in the original message that
     couldn't be delivered. If delivery fails for multiple recipients, the email address of
     each recipient is listed. This field also contains the following sub-fields for each
     email address:

     Remote server: The FQDN of the server that rejected the original message during
     SMTP transmission (delivery failed after the message body was sent, but before the
     server acknowledged receiving the message). This field isn't present when:

<!-- p.1851 -->

            The server that rejected the message also generated the NDR. This is typical for
            delivery failures between senders and recipients in the same Exchange organization.

            The remote server acknowledged receiving the original message, but the message
            was rejected for other reasons (for example, content restrictions).

            Enhanced status code

            SMTP response: The US-ASCII text string that's returned by the messaging server
            that rejected the original message. This is typically a short explanation of the
            enhanced status code. This string is not rewritten by Exchange.

            Original message headers: This area contains the message header of the rejected
            message. These header fields can provide useful diagnostic information (for
            example, server hops in the message routing path, or whether the To field matches
            the email address of the rejected recipient).

Common enhanced status codes
Enhanced status codes are defined in RFC 3463, and use the syntax <class>. <subject>.
<detail>:

     <class>: 4 indicates a temporary delivery error. 5 indicates a permanent delivery error.

     <subject>: The RFC categorizes the values like this:

        1: Addressing

        2: Mailbox (the recipient)

        3: Mail system (the destination mail system)

        4: Network and routing

        5: Mail delivery protocol

        7: Security or policy

     <detail>: A 1 to 3 digit number that further classifies the error.

The following tables contain the enhanced status codes that are returned in NDRs for the most
common message delivery failures.

  ７ Note

<!-- p.1852 -->

 For information about enhanced status codes in Microsoft 365 or Office 365 and hybrid
 environments, see Email non-delivery reports in Exchange Online.

Temporary delivery failures

                                                                                      ﾉ   Expand table

Enhanced    Description    Possible causes and solutions
status
code

4.3.1       Insufficient   Free disk space is low (for example, the disk that holds the queue
            system         database doesn't have the required amount of free space). For more
            resources      information, see Understanding back pressure. To move the queue
                           database to a different disk, see Change the location of the queue
                           database.
                           Available memory is low (for example, Exchange installed on a virtual
                           machine that's configured to use dynamic memory). Always use static
                           memory on Exchange virtual machines. For more information, see
                           Exchange memory requirements and recommendations.

4.3.2       Service not    You've configured a custom Receive connector in the Transport (Hub)
            available      service on a Mailbox server that listens on port 25. Typically, custom
            or             Receive connectors that listen on port 25 belong in the Front End
            Service not    Transport service on the Mailbox server.
            active         Important Exchange server components are inactive. You can confirm this
                           by running the following command in the Exchange Management Shell:
                            Get-ServerComponent -Identity <ServerName> .
                           To restart all inactive components, run the following command: Set-
                           ServerComponentState -Identity <ServerName> -Component
                           ServerWideOffline -State Active -Requester Maintenance .
                           Incompatible transport agents (in particular, after an Exchange update).
                           After you identify the transport agent, disable it or uninstall it. For more
                           information, see Troubleshoot transport agents.

4.4.1       Connection     Transient network issues that might eventually correct themselves. The
            timed out      Exchange server periodically tries to connect to the destination server to
                           deliver the message. After multiple failures, the message is returned to
                           the sender in an NDR with a permanent failure code.
                           For more information about configuring the queue retry and failure
                           intervals, see Configure message retry, resubmit, and expiration intervals.
                           To manually retry a queue, see Retry queues.
                           Firewall or Internet service provider (ISP) restrictions on TCP port 25.

4.4.2       Connection     Transient network issues or server problems that might eventually correct
            dropped        themselves. The sending server will retry delivery of the message, and will
                           generate further status reports.

<!-- p.1853 -->

Enhanced   Description       Possible causes and solutions
status
code

                             The message size limit for the connection has been reached, or the
                             message submission rate for the source IP address has exceeded the
                             configured limit. For more information, see Message rate limits and
                             throttling.
                             Antispam, SMTP proxy, or firewall configuration issues are blocking email
                             from the Exchange server.

4.4.7       Message          Send connector configuration issues. For example:
           delayed                 The Send connector is configured to use DNS routing when it
           or                      should be using smart host routing, or vice-versa. Use nslookup to
            Queue expired;         verify that the destination domain is reachable from the Exchange
           Message                 server.
           expired                 The FQDN that the Send connector provides to HELO or EHLO
                                   requests doesn't match the host name in your MX record (for
                                   example, mail.contoso.com). Some messaging systems are
                                   configured to compare these values in an effort to reduce spam.
                                   The default value on a Send connector is blank, which means the
                                   FQDN of the Exchange server is used (for example,
                                   exchange01.contoso.com).

                             The Mailbox Transport Delivery service isn't started on the destination
                             server (which prevents the delivery of the message to the mailbox).

                             The destination messaging system has issues with Transport Neutral
                             Encryption Format (TNEF) messages (also known as rich text format or
                             RTF in Outlook). For example, meeting requests or messages with images
                             embedded in the message body.

                             If the destination domain uses the Sender Policy Framework (SPF) to
                             check message sources, there might be SPF issues with your domain (for
                             example, your SPF record doesn't include all email sources for your
                             domain).

Permanent delivery failures

                                                                                      ﾉ   Expand table

Enhanced   Description                         Possible causes and solutions.
status
code

5.1.0      Sender denied                       Replying to old messages, or messages that were
                                               exported as files (important recipient attributes might
                                               have changed). Verify that the recipient's email address
                                               is correct.

<!-- p.1854 -->

Enhanced   Description                     Possible causes and solutions.
status
code

                                           Malformed or missing attributes in contact entries.
                                           The sender is blocked by sender filtering (directly, or
                                           the sender is on a user's Blocked Senders list, and the
                                           Sender Filter agent is configured to use safelist
                                           aggregation. For more information, see Sender filtering
                                           and Safelist aggregation.

5.1.1      RESOLVER.ADR.ExRecipNotFound;   The recipient's email address is incorrect (the recipient
           not found                       doesn't exist in the destination messaging system).
           or                              Verify the recipient's email address.
           User unknown                    You recreated a deleted mailbox, and internal users are
                                           addressing email messages in Outlook or Outlook on
                                           the web using old entries in their autocomplete cache
                                           (the X.500 values or LegacyExchangeDN values for the
                                           recipient are now different). Tell users to delete the
                                           entry from their autocomplete cache and select the
                                           recipient again.

5.1.3      STOREDRV.Submit; invalid        The recipient's email address is incorrect (for example,
           recipient address               it contains unsupported characters or invalid
                                           formatting).

5.1.4      Recipient address reserved by   Receive connectors reject SMTP connections that
           RFC 2606                        contain the top level domains defined in RFC 2606
                                           (.test, .example, .invalid, or .localhost), This behavior is
                                           controlled by the
                                           RejectReservedTopLevelRecipientDomains parameter on
                                           the New-ReceiveConnector and Set-ReceiveConnector
                                           cmdlets.

5.1.5      Recipient address reserved by   Receive connectors reject SMTP connections that
           RFC 2606                        contain the second level domains defined in RFC 2606
                                           (example.com, example.net, or example.org). This
                                           behavior is controlled by the
                                           RejectReservedSecondLevelRecipientDomains parameter
                                           on the New-ReceiveConnector and Set-
                                           ReceiveConnector cmdlets.

5.1.6      Recipient addresses in single   Receive connectors reject SMTP connections that
           label domains not accepted      contain single label domains (for example,
                                           chris@contoso instead of chris@contoso.com) This
                                           behavior is controlled by the
                                           RejectSingleLabelRecipientDomains parameter on the
                                           New-ReceiveConnector and Set-ReceiveConnector
                                           cmdlets.

<!-- p.1855 -->

Enhanced   Description                        Possible causes and solutions.
status
code

5.1.7      Invalid address                    There's a problem with the sender's email address.
           or                                 Verify the sender's email address.
           Unknown sender address

5.1.8      Access denied, bad outbound        The sender has exceeded a message rate limit (for
           sender                             example, an application server is configured to relay a
                                              large number of messages through Exchange. For
                                              more information, see Message rate limits and
                                              throttling and Allow anonymous relay on Exchange
                                              servers.

5.2.1      Content Filter agent quarantined   The message was quarantined by content filtering. To
           this message                       configure exceptions to content filtering, see Use the
                                              Exchange Management Shell to configure recipient
                                              and sender exceptions for content filtering.

5.2.2      Mailbox full                       The recipient's mailbox has exceeded its storage quota
                                              and is no longer able to accept new messages. For
                                              more information about configuring mailbox quotas,
                                              see Configure storage quotas for a mailbox.

5.2.3      RESOLVER.RST.RecipSizeLimit;       The message is too large. Send the message again
           message too large for this         without any attachments, or configure a larger
           recipient                          message size limit for the recipient. For more
                                              information, see Recipient limits.

5.3.0      Too many related errors            The message was determined to be malformed, and
                                              was moved to the poison message queue. For more
                                              information, see Types of queues.

5.3.2      STOREDRV.Deliver: Missing or bad   You're using the ABP Routing agent, and the recipient
           StoreDriver MDB properties         isn't a member of the global address list that's
                                              specified in their address book policy (ABP). For more
                                              information, see Use the Exchange Management Shell
                                              to install and configure the Address Book Policy
                                              Routing Agent and Address book policies in Exchange
                                              Server.

5.3.3      Unrecognized command               Receive connectors that are used for internal mail flow
                                              are missing the required Exchange Server
                                              authentication mechanism. For more information
                                              about authentication on Receive connectors, see
                                              Receive connector authentication mechanisms.

5.3.4      Message size exceeds fixed         The message is too large. This error can be generated
           maximum message size               by the source or destination messaging system. Send
                                              the message again without any attachments, or

<!-- p.1856 -->

Enhanced   Description                       Possible causes and solutions.
status
code

                                             configure a larger message size limit. For more
                                             information, see Message size and recipient limits in
                                             Exchange Server.

5.3.5      System incorrectly configured     A mail loop was detected. Verify that the FQDN
                                             property on the Receive connector doesn't match the
                                             FQDN of another server, service, or device that's used
                                             in mail flow in your organization (by default, the
                                             Receive connector uses the FQDN of the Exchange
                                             server).

5.4.4      SMTPSEND.DNS.NonExistentDomain;   There's a DNS or network adapter configuration issue
           nonexistent domain                on the Exchange server. Verify the internal and external
                                             DNS lookup settings for the Exchange by running this
                                             command in the Exchange Management Shell:
                                             Get-TransportService | Format-List
                                             Name,ExternalDNS*,InternalDNS*; Get-
                                             FrontEndTransportService | Format-List
                                             Name,ExternalDNS*,InternalDNS*`

                                             You can configure these settings by using the
                                             InternalDNS* and ExternalDNS* parameters on the Set-
                                             TransportService and Set-FrontEndTransportService
                                             cmdlets.

                                             By default, these settings are used by Send connectors
                                             (the default value of the UseExternalDNSServersEnabled
                                             parameter value is $false ).

                                             Check the priority (order) of the network adapters in
                                             the operating system of the Exchange server.

5.4.6      Hop count exceeded - possible     A configuration error has caused an email loop. By
           mail loop                         default, after 20 iterations of an email loop, Exchange
                                             interrupts the loop and generates an NDR.
                                             Verify that Inbox rules for the recipient and sender, or
                                             forwarding rules on the recipient 's mailbox aren't
                                             causing this (the message generates a message, which
                                             generates another message, and the process continues
                                             indefinitely).
                                             Verify the mailbox doesn't have a targetAddress
                                             property value in Active Directory (this property
                                             corresponds to the ExternalEmailAddress parameter for
                                             mail users in Exchange).
                                             If you remove Exchange servers, or modify settings
                                             related to mail routing and mail flow, be sure to restart

<!-- p.1857 -->

Enhanced   Description                        Possible causes and solutions.
status
code

                                              the Microsoft Exchange Transport and Exchange
                                              Frontend Transport services.

5.5.2      Send hello first                   SMTP commands are sent out of sequence (for
                                              example, a server sends an SMTP command like AUTH
                                              or MAIL FROM before identifying itself with the EHLO
                                              command). After establishing a connection to a
                                              messaging server, the first SMTP command must
                                              always be EHLO or HELO.

5.5.3      Too many recipients                The combined total of recipients on the To, Cc, and Bcc
                                              lines of the message exceeds the total number of
                                              recipients allowed in a single message for the
                                              organization, Receive connector, or sender. For more
                                              information, see Message size and recipient limits in
                                              Exchange Server.

5.7.1      Unable to relay                    You have an application server or device that's trying
           or                                 to relay messages through Exchange. For more
           Client was not authenticated       information, see Allow anonymous relay on Exchange
                                              servers.
                                              The recipient is configured to only accept messages
                                              from authenticated (typically, internal) senders. For
                                              more information, see Configure message delivery
                                              restrictions for a mailbox.

5.7.3      Cannot achieve Exchange Server     A firewall or other device is blocking the Extended
           authentication                     SMTP command that's required for Exchange Server
           or                                 authentication (X-EXPS).
           Not Authorized                     Internal email traffic is flowing through connectors that
                                              aren't configured to use the Exchange Server
                                              authentication method . Verify the remote IP address
                                              ranges on any custom Receive connectors.

5.7.900    Delivery not authorized, message   The message was rejected by a mail flow rule (also
to         refused                            known as a transport rule). This enhanced status code
5.7.999                                       range is available when the rule is configured to reject
                                              messages (otherwise, the default code that's used is
                                              5.7.1). For more information, see Mail flow rule actions
                                              in Exchange Server.

<!-- p.1858 -->

Procedures for DSNs and NDRs in
Exchange Server
07/23/2025

APPLIES TO:      2016       2019     Subscription Edition

Like previous versions of Exchange, Exchange Server uses delivery status notifications (also
known as DSNs, non-delivery reports, NDRs, or bounce messages) to provide delivery status
and failure notifications to message senders. For more information about NDRs, see DSNs and
NDRs in Exchange Server.

You can use the default NDRs that are included in Exchange, or you can use the Exchange
Management Shell to create NDRs with custom text to meet the needs of your organization.
The custom NDR text replaces the default text for a given enhanced status code or quota
event. If you remove the custom NDR, the default NDR text is used (you can't completely
remove a default NDR). You can also disable custom NDRs to preserve them, but not use them
(the default NDR text is used).

What do you need to know before you begin?
     Estimated time to complete each procedure: less than 10 minutes.

     The main focus of this article is custom NDR text that replaces the text of default NDRs
     that are used by Exchange. You can create new NDRs for other enhanced status code
     values (for example, 5.999.999), but no one sees these NDRs if the enhanced status code
     isn't used by Exchange. You can use a range of custom enhanced status codes as part of
     an action for a mail flow rule (also known as a transport rule). For more information, see
     Mail flow rule actions in Exchange Server.

     The procedures in this article are available on Mailbox servers and Edge Transport servers.

     You can't use the Exchange admin center (EAC) for most of the procedures in this article.
     You need to use the Exchange Management Shell. To learn how to open the Exchange
     Management Shell in your on-premises Exchange organization, see Open the Exchange
     Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "DSNs" entry in the Mail flow
     permissions article.

<!-- p.1859 -->

     For information about keyboard shortcuts that might apply to the procedures in this
     article, see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the Exchange Management Shell to view all
default NDRs
To output the list of all default NDRs in all languages to an HTML file named C:\My
Documents\Default NDRs.html, run this command:

  PowerShell

  Get-SystemMessage -Original | Select-Object -Property
  Identity,DsnCode,Language,Text | ConvertTo-Html | Set-Content -Path "C:\My
  Documents\Default NDRs.html"

   Tip

  You should output the list to a file, because the list is very long, and you receive errors if
  you don't have the required language packs installed.

For detailed syntax and parameter information, see Get-SystemMessage.

Use the Exchange Management Shell to view
custom NDRs
To view a summary list of all custom NDRs in your organization, run this command:

  PowerShell

  Get-SystemMessage

   Tip

<!-- p.1860 -->

  By default, there are no custom NDRs, so this command returns no results.

To view detailed information for a custom NDR, use this syntax:

  PowerShell

  Get-SystemMessage -Identity <NDRIdentity>

For an explanation of the available <NDRIdentity> values, see the Identity values for NDRs
section in this article.

This example returns detailed information for the custom NDR for the enhanced status code
5.1.2 sent to internal senders in English. If there's no custom NDR for this combination of
language, audience, and enhanced status code, you receive an error.

  PowerShell

  Get-SystemMessage En\Internal\5.1.2 | Format-List

This example returns detailed information for the custom English NDR for the
ProhibitSendReceive quota on mailboxes. If there's no custom NDR for this combination of
language and quota, you receive an error.

  PowerShell

  Get-SystemMessage En\ProhibitSendReceiveMailBox | Format-List

For detailed syntax and parameter information, see Get-SystemMessage.

Create custom NDRs

Use the Exchange Management Shell to create custom NDRs
for enhanced status codes
To create a custom NDR for an enhanced status code, use this syntax:

  PowerShell

  New-SystemMessage -Internal <$true | $false> -Language <Locale> -DSNCode <x.y.z> -
  Text "<NDR text>"

<!-- p.1861 -->

The values are:

     Internal: Controls whether the NDR is sent to internal or external senders. For internal
     senders, use the value $true . For external senders, use the value $false . For example, in
     the custom text for internal senders, you can include help desk contact information that
     you wouldn't want to include in NDRs for external senders.
     Language: For the list of available languages, see the Supported languages for NDRs
     section in this article.
     DSNCode: The enhanced status code. Valid values are 4.x.y or 5.x.y where x and y are one
     to three digit numbers.
     Text: You can use plain text or HTML formatting. For more information, see the HTML tags
     and special characters in NDRs section in this article.

This example creates a custom plain text NDR for the enhanced status code 5.1.2 sent to
external senders in English.

  PowerShell

  New-SystemMessage -Internal $false -Language En -DSNCode 5.1.2 -Text "You tried to
  send a message to a disabled mailbox that's no longer accepting messages. Please
  contact your System Administrator for more information."

This example creates a custom HTML NDR for the enhanced status code 5.1.2 sent to internal
senders in English.

  PowerShell

  New-SystemMessage -DSNCode 5.1.2 -Internal $true -Language En -Text 'You tried to
  send a message to a <B>disabled</B> mailbox. Please visit <A
  HREF="https://it.contoso.com">Internal Support</A> or contact &quot;InfoSec&quot;
  for more information.'

For detailed syntax and parameter information, see New-SystemMessage.

Use the Exchange Management Shell to create custom NDRs
for quotas
To create a custom NDR for quotas, use this syntax:

  PowerShell

  New-SystemMessage -Language <Locale> -QuotaMessageType <Quota> -Text "<NDR text>"

<!-- p.1862 -->

The values are:

     Language: For the list of available languages, see Supported languages for NDRs.
     QuotaMessageType: For a list of the available quotas, see Identity values for NDRs.
     Text: You can use plain text or HTML formatting. For more information, see HTML tags
     and special characters in NDRs.

This example creates a custom English plain text NDR for the ProhibitSendReceive quota on
mailboxes.

  PowerShell

  New-SystemMessage -Language En -QuotaMessageType ProhibitSendReceiveMailBox -Text
  "Your mailbox is full, and can't send or receive messages. Delete any unwanted
  large messages (messages with attachments) and empty your Deleted Items folder"

For detailed syntax and parameter information, see New-SystemMessage.

How do you know you successfully created a custom NDR?
To verify you successfully created a custom NDR, do these steps:

     Run the following command and verify the property values:

        PowerShell

        Get-SystemMessage | Format-List Identity,DsnCode,Language,Text

     Send a test message that generates the custom NDR that you configured.

Use the Exchange Management Shell to modify
custom NDRs
To modify custom NDRs, use this syntax:

  PowerShell

  Set-SystemMessage -Identity <NDRIdentity> [-Text "<NDR text>"] [-Original]

For an explanation of the available <NDRIdentity> values, see the Identity values for NDRs
section in this article. For an explanation of the <NDR text> values, see the HTML tags and
special characters in NDRs section in this article.

<!-- p.1863 -->

This example changes the text in the custom NDR for the enhanced status code 5.1.2 sent to
internal senders in English.

  PowerShell

  Set-SystemMessage -Identity En\Internal\5.1.2 -Text "The mailbox you tried to send
  an email message to is disabled and is no longer accepting messages. Please
  contact the Help Desk at extension 123 for assistance."

This example changes the text in the custom English NDR for the ProhibitSendReceive quota
on mailboxes.

  PowerShell

  Set-SystemMessage -Identity En\ProhibitSendReceiveMailBox -Text "Your mailbox is
  full. Delete large messages and empty your Deleted Items folder."

This example disables the specified custom NDR. The custom NDR is preserved, and appears in
the results of Get-SystemMessage, but the default NDR is used instead.

  PowerShell

  Set-SystemMessage -Identity En\Internal\5.1.2 -Original

Note: If there's no corresponding default NDR, you receive an error when you use the Original
switch.

For detailed syntax and parameter information, see Set-SystemMessage.

How do you know you successfully modified a custom NDR?
To verify you successfully modified a custom NDR, replace <NDRIdentity> with the appropriate
value, and run this command to verify the property values:

  PowerShell

  Get-SystemMessage -Identity <NDRIdentity> | Format-List

Use the Exchange Management Shell to remove
custom NDRs
To remove a custom NDR, use this syntax:

<!-- p.1864 -->

  PowerShell

   Remove-SystemMessage -Identity <NDRIdentity>

For an explanation of the available <NDRIdentity> values, see the Identity values for NDRs
section in this article.

This example removes the custom NDR for the enhanced status code 5.1.2 sent to internal
senders in English.

  PowerShell

   Remove-SystemMessage -Identity En\Internal\5.1.2

This example removes the custom English NDR for the ProhibitSendReceive quota on
mailboxes.

  PowerShell

   Remove-SystemMessage -Identity En\ProhibitSendReceiveMailBox

For detailed syntax and parameter information, see Remove-SystemMessage.

How do you know you successfully removed a custom NDR?
To verify you successfully removed a custom NDR, run this command to verify the custom NDR
isn't listed:

  PowerShell

   Get-SystemMessage

Forward copies of NDRs to the Exchange recipient
mailbox
You can configure your Exchange organization to send copies of NDRs to the Exchange
recipient. However, by default, no mailbox is assigned to the Exchange recipient, so any
messages that are sent to the Exchange recipient are discarded. To send copies of NDRs to the
Exchange recipient mailbox, you need to:

   1. Assign a mailbox to the Exchange recipient.

<!-- p.1865 -->

   2. Specify the enhanced status codes that you want to monitor (not quotas).

Step 1: Use the Exchange Management Shell to assign a
mailbox to the Exchange recipient
Note: Due to the high volume of messages, we recommend using a dedicated mailbox for the
Exchange recipient. For more information about creating mailboxes, see Create shared
mailboxes in the Exchange admin center and Create user mailboxes in Exchange Server.

To assign a mailbox to the Exchange recipient, use this syntax:

  PowerShell

  Set-OrganizationConfig -MicrosoftExchangeRecipientReplyRecipient <MailboxIdentity>

This example assigns the existing mailbox named "Contoso System Mailbox" to the Exchange
recipient.

  PowerShell

  Set-OrganizationConfig -MicrosoftExchangeRecipientReplyRecipient "Contoso System
  Mailbox"

Step 2: Specify the enhanced status codes that you want to
monitor
     You can use the EAC or the Exchange Management Shell.

     By default, even though there are no enhanced status codes specified, NDRs for these
     codes are automatically sent to the Exchange recipient:
         5.1.4

         5.2.0
         5.2.4

         5.4.4
         5.4.6

         5.4.8

     You can only specify enhanced status codes. You can't specify quotas.

Use the EAC to specify the enhanced status codes to monitor

<!-- p.1866 -->

For more information about the EAC, see Exchange admin center in Exchange Server.

   1. In the EAC, go to Mail flow > Receive connectors.

   2. Select More options (    ) and select Organization transport settings.

   3. In the Organization transport settings window that opens, select the Delivery tab. In the
     DSN codes section, do one or more of these steps:

           To add entries, type the enhanced status code that you want to monitor (4. <y.z> or
           5. <y.z>), and then select Add (    ). Repeat this step as many times as you need to.

           To modify an existing entry, select it select Edit (   ), and then modify it inline.

           To remove an existing entry, select it and then select Remove (       ).

     When you're finished, select Save.

Use the Exchange Management Shell to specify the enhanced status
codes to monitor

To add enhanced status codes to monitor, which replaces any existing values, use this syntax:

  PowerShell

  Set-TransportConfig -GenerateCopyOfDSNFor <x.y.z>,<x.y.z>...

This example configures the Exchange organization to forward all NDRs for the enhanced
status code values 5.7.1, 5.7.2, and 5.7.3 to the Exchange recipient.

  PowerShell

  Set-TransportConfig -GenerateCopyOfDSNFor 5.7.1,5.7.2,5.7.3

To add or remove entries without modifying any existing values, use this syntax:

  PowerShell

  Set-TransportConfig -GenerateCopyOfDSNFor @{Add="<x.y.z>","<x.y.z>"...; Remove="
  <x.y.z>","<x.y.z>"...}

This example adds the enhanced status code 5.7.5 and removes 5.7.1 from the existing list of
NDRs that are forwarded to the Exchange recipient.

  PowerShell

<!-- p.1867 -->

  Set-TransportConfig -GenerateCopyOfDSNFor @{Add="5.7.5"; Remove="5.7.1"}

How do you know you successfully configured copies of NDRs
to be sent to the Exchange recipient mailbox?
To verify you successfully configured copies of NDRs to be sent to the Exchange recipient
mailbox,

     Run the following command and verify the property values:

       PowerShell

       Get-TransportConfig | Format-List GenerateCopyOfDSNFor

     Monitor the Exchange recipient mailbox to see if NDRs that contain the specified
     enhanced status codes are delivered there.

Identity values for NDRs
The identity of an NDR uses one of these formats:

     NDRs for enhanced status codes: <Language>\<Internal | External>\ <DSNcode>. For
     example, En\Internal\5.1.2 or Ja\External\5.1.2 .
        <DSNcode>: Valid values are 4.x.y or 5.x.y where x and y are one to three digit
        numbers. To generate a list of the enhanced status codes that are used by Exchange,
        see the Use the Exchange Management Shell to view all default NDRs section earlier in
        this article.
        Internal or External: You can use different text in NDRs for internal or external senders.
        <Language>: For the list of supported languages, see the Supported languages for
        NDRs section in this article.

     NDRs for quotas: <Language>\ <QuotaMessageType>. For example,
     En\ProhibitSendReceiveMailBox .

        <Language>: For the list of supported languages, see the Supported languages for
        NDRs section in this article.

        <QuotaMessageType>: Valid values are:

        Mailbox size quotas:

<!-- p.1868 -->

  ProhibitSendReceiveMailBox: A mailbox exceeds its ProhibitSendReceiveQuota
  limit.
  ProhibitSendMailbox: A mailbox exceeds its ProhibitSendQuota limit.
  WarningMailbox: A mailbox exceeds its IssueWarningQuota limit when it has a
   ProhibitSendQuota or ProhibitSendReceiveQuota limit configured.

  WarningMailboxUnlimitedSize: A mailbox exceeds its IssueWarningQuota limit when
  it doesn't have a ProhibitSendQuota or ProhibitSendReceiveQuota limit configured.

Public folder size quotas:
  ProhibitPostPublicFolder: A public folder exceeds its ProhibitPostQuota limit.
  WarningPublicFolder: A public folder exceeds its IssueWarningQuota limit when it
  has a ProhibitPostQuota limit configured.
  WarningPublicFolderUnlimitedSize: A public folder exceeds its IssueWarningQuota
  limit when it doesn't have a ProhibitPostQuota limit configured.

Maximum number of messages in a mailbox folder:
  ProhibitReceiveMailboxMessagesPerFolderCount: A mailbox exceeds its
   MailboxMessagesPerFolderCountReceiveQuota limit.

  WarningMailboxMessagesPerFolderCount: A mailbox exceeds its
   MailboxMessagesPerFolderCountWarningQuota limit when it has a
   ailboxMessagesPerFolderCountReceiveQuota limit configured.

  WarningMailboxMessagesPerFolderUnlimitedCount: A mailbox exceeds its
   MailboxMessagesPerFolderCountWarningQuota limit when it doesn't have a
   MailboxMessagesPerFolderCountReceiveQuota limit configured.

Maximum number of subfolders in a mailbox folder:
  ProhibitReceiveFolderHierarchyChildrenCountCount: A mailbox exceeds its
   FolderHierarchyChildrenCountReceiveQuota limit.

  WarningFolderHierarchyChildrenCount: A mailbox exceeds its
   FolderHierarchyChildrenCountWarningQuota limit when it has a

   FolderHierarchyChildrenCountReceiveQuota limit configured.

  WarningFolderHierarchyChildrenUnlimitedCount: A mailbox exceeds its
   FolderHierarchyChildrenCountWarningQuota limit when it doesn't have a
   FolderHierarchyChildrenCountReceiveQuota limit configured.

  ProhibitReceiveFoldersCount: A mailbox exceeds its FoldersCountReceiveQuota
  limit.
  WarningFoldersCount: A mailbox exceeds its FoldersCountWarningQuota limit when
  it has a FoldersCountReceiveQuota limit configured.
  WarningFoldersCountUnlimited A mailbox exceeds its FoldersCountWarningQuota
  limit when it doesn't have a FoldersCountReceiveQuota limit configured.

<!-- p.1869 -->

         Maximum number of levels (depth) in a mailbox folder:
              ProhibitReceiveFolderHierarchyDepth: A mailbox exceeds its
              FolderHierarchyDepthWarningQuota limit.

              WarningFolderHierarchyDepth: A mailbox exceeds its
              FolderHierarchyDepthWarningQuota limit when it has a

              FolderHierarchyDepthReceiveQuota limit configured.

              WarningFolderHierarchyDepthUnlimited:: A mailbox exceeds its
              FolderHierarchyDepthWarningQuota limit when it doesn't have a
              FolderHierarchyDepthReceiveQuota limit configured.

Supported languages for NDRs
This table lists the supported language that codes you can use in custom NDRs.

                                                                              ﾉ   Expand table

 Language code             Language

 af                        Afrikaans

 am-ET                     Amharic (Ethiopia)

 ar                        Arabic

 as-IN                     Assamese (India)

 bg                        Bulgarian

 bn-BD                     Bengali (Bangladesh)

 bn-IN                     Bengali (India)

 bs-Cyrl-BA                Bosnian (Cyrillic, Bosnia and Herzegovina)

 bs-Latn-BA                Bosnian (Latin, Bosnia and Herzegovina)

 ca                        Catalan

 cs                        Czech

 cy-GB                     Welsh (Great Britain)

 da                        Danish

 de                        German

 el                        Greek

<!-- p.1870 -->

Language code   Language

en              English

es              Spanish

et              Estonian

eu              Basque

fa              Persian

fi              Finnish

fil-PH          Filipino (Philippines)

fr              French

ga-IE           Irish (Ireland)

gl              Galician

gu              Gujarati

ha-Latn-NG      Hausa (Latin, Nigeria)

he              Hebrew

hi              Hindi

hr              Croatian

hu              Hungarian

hy              Armenian

id              Indonesian

ig-NG           Igbo (Nigeria)

is              Icelandic

it              Italian

iu-Latn-CA      Inuktitut (Latin, Canada)

ja              Japanese

ka              Georgian

kk              Kazakh

km-KH           Khmer (Cambodia)

<!-- p.1871 -->

Language code   Language

kn              Kannada

ko              Korean

kok             Konkani

ky              Kyrgyz

lb-LU           Luxembourgish (Luxembourg)

lo-LA           Lao (Lao People's Democratic Republic)

lt              Lithuanian

lv              Latvian

mi-NZ           Maori (New Zealand)

mk              Macedonian

ml-IN           Malayalam (India)

mr              Marathi

ms              Malay

ms-BN           Malay (Brunei Darussalam)

mt-MT           Maltese (Malta)

ne-NP           Nepali (Nepal)

nl              Dutch

nn-NO           Norwegian (Nynorsk)

no              Norwegian

nso-ZA          Sesotho sa Leboa (South Africa)

or-IN           Oriya (India)

pa              Punjabi

pl              Polish

ps-AF           Pashto (Afghanistan)

pt              Portuguese

pt-PT           Portuguese (Portugal)

<!-- p.1872 -->

Language code   Language

qut-GT          K'iche (Guatemala)

quz-PE          Quechua (Peru)

ro              Romanian

ru              Russian

rw-RW           Kinyarwanda (Rwanda)

si-LK           Sinhala (Sri Lanka)

sk              Slovak

sl              Slovenian

sq              Albanian

sr              Serbian

sr-Cyrl-CS      Serbian (Cyrillic, Serbia)

sv              Swedish

sw              Kiswahili

ta              Tamil

te              Telugu

th              Thai

tn-ZA           Setswana (South Africa)

tr              Turkish

tt              Tatar

uk              Ukrainian

ur              Urdu

uz              Uzbek

vi              Vietnamese

wo-SN           Wolof (Senegal)

xh-ZA           isiXhosa (South Africa)

yo-NG           Yoruba (Nigeria)

<!-- p.1873 -->

 Language code                Language

  zh-Hans                     Chinese (Simplified)

  zh-Hant                     Chinese (Traditional)

  zh-HK                       Chinese (Hong Kong Special Administrative Region)

  zu-ZA                       isiZulu (South Africa)

To control the languages that are used in NDRs, you use these parameters on the Set-
TransportConfig cmdlet:

        ExternalDsnDefaultLanguage: Specifies the default language to use on external NDRs. The
        default value is blank ( $null ), which means the default Windows server language is used.
        InternalDsnDefaultLanguage: Specifies the default language to use on internal NDRs. The
        default value is blank ( $null ), which means the default Windows server language is used.
        ExternalDsnLanguageDetectionEnabled:
            $true : Exchange tries to send an external NDR in the same language as the original

            message. This value is the default.
            $false : Language detection is disabled for external NDRs. The

            ExternalDsnDefaultLanguage parameter determines the NDR language.
        InternalDsnLanguageDetectionEnabled:
            $true : Exchange tries to send an internal NDR in the same language as the original

            message. This value is the default.
            $false : Language detection is disabled for internal NDRs. The

            InternalDsnDefaultLanguage parameter determines the NDR language.

HTML tags and special characters in NDRs
The custom text that you include in an NDR can contain a maximum of 512 characters, which
includes text and HTML tags. For example, you can include a detailed description of the
problem, contact information for your help desk, and a link to your support department's web
site.

To control whether Exchange uses HTML or plain text in NDRs, you use these parameters on
the Set-TransportConfig cmdlet:

        ExternalDsnSendHtml:
            $true : Use HTML tags in NDRs for external senders. This value is the default.

            $false : Use plain text in NDRs for external senders.

        InternalDsnSendHtml:

<!-- p.1874 -->

            $true : Use HTML tags in NDRs for internal senders. This value is the default.
            $false : Use plain text in NDRs for internal senders.

The following table describes the HTML tags that you can use in the NDR text.

                                                                                         ﾉ   Expand table

 Description     HTML tags

 Bold             <B> and </B>

 Italic           <EM> and </EM>

 Line break       <BR>

 Paragraph        <P> and </P>

 Hyperlink        <A HREF="url"> and </A>

                 Note: Because this tag contains double quotation marks, you need to use single quotation
                 marks (not double quotation marks) around the complete text string if you use this tag in
                 your custom text. Otherwise, you receive an error.

Certain characters in an NDR require escape codes to identify them literally, and not by their
function in the NDR. These characters are described in the following table:

                                                                                         ﾉ   Expand table

 Character                                         Escape code

 <                                                  &lt;

 >                                                  &gt;

 "                                                  &quot;

 &                                                  &amp;

For example, if you want the NDR to display the text Please contact the Help Desk at
<1234>. , you need to the value "Please contact the Help Desk at &lt;1234&gt;."

The following example shows a custom NDR text value that uses HTML tags and escape codes.

     text

     'You tried to send a message to a <B>disabled</B> mailbox. Please visit <A
     HREF="https://it.contoso.com">Internal Support</A> or contact &quot;InfoSec&quot;

<!-- p.1875 -->

for more information.'

<!-- p.1876 -->

Content conversion in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

Content conversion is the process of correctly formatting a message for each recipient. The
decision to perform content conversion on a message depends on the destination and format
of the message. The types of content conversion that occur in Exchange 2016 and Exchange
2019 are unchanged from Exchange 2013:

      Message conversion for external recipients: This type of content conversion includes the
      Transport Neutral Encapsulation Format (TNEF) conversion options and message
      encoding options for external recipients. Messages sent to recipients inside the Exchange
      organization don't require this type of content conversion. This type of content
      conversion is handled by the categorizer in the Transport service on a Mailbox server.
      Categorization on each message happens after a newly arrived message is put in the
      Submission queue. In addition to recipient resolution and routing resolution, content
      conversion is performed on the message before the message is put in a delivery queue. If
      a single message contains multiple recipients, the categorizer determines the appropriate
      encoding for each message recipient. Content conversion tracing doesn't capture any
      content conversion failures that the categorizer encounters as it converts messages sent
      to external recipients.

      MAPI conversion for internal recipients: This type of content conversion is handled by
      the Mailbox Transport service. The Mailbox Transport service exists on Mailbox servers to
      transmit messages between mailbox databases on the local server, and the Transport
      service on Mailbox servers. Specifically, the Mailbox Transport Submission service
      transmits messages from the sender's Outbox to the Transport service on a Mailbox
      server. The Mailbox Transport Delivery service transmits messages from the Transport
      service on a Mailbox server to the recipient's Inbox. The Mailbox Transport Submission
      service converts all outgoing messages from MAPI and the Mailbox Transport Delivery
      service converts all incoming messages to MAPI. Content conversion tracing captures
      these MAPI conversion failures. For more information, see Managing Content Conversion
      Tracing.

Exchange and Outlook message formats
The following list describes the basic message formats available in Exchange and Outlook:

      Plain text: A plain text message uses only US-ASCII text as described in RFC 5322. The
      message can't contain different fonts or other text formatting. The following two formats
      can be used for a plain text message:

<!-- p.1877 -->

  The message headers and the message body are composed of US-ASCII text.
  Attachments must be encoded by using Uuencode. Uuencode represents Unix-to-Unix
  encoding and defines an encoding algorithm to store binary attachments in the body
  of an email message by using US-ASCII text characters.

  The message is MIME-encoded with a Content-Type value of text/plain , and a
  Content-Transfer-Encoding value of 7bit for the text parts of a multipart message.
  Any message attachments are encoded by using Quoted-printable or Base64
  encoding. By default, when you compose and send a plain text message in Outlook,
  the message is MIME-encoded with a Content-Type value of text/plain .

HTML: An HTML message supports text formatting, background images, tables, bullet
points, and other graphical elements. By definition, an HTML-formatted message must be
MIME-encoded to preserve these formatting elements.

Rich text format (RTF): RTF supports text formatting and other graphical elements. RTF is
synonymous with TNEF (TNEF and RTF can be used interchangeably). The rich text
message format is completely different from the rich text document format that's
available in Word.

TNEF: The Transport Neutral Encapsulation Format is a Microsoft-specific format for
encapsulating MAPI message properties. A TNEF message contains a plain text version of
the message and an attachment that packages the original formatted version of the
message. Typically, this attachment is named Winmail.dat. The Winmail.dat attachment
includes the following information:
  Original formatted version of the message (for example, fonts, text sizes, and text
  colors)
  OLE objects (for example, embedded pictures or embedded Office documents)
  Special Outlook features (for example, custom forms, voting buttons, or meeting
  requests)
  Regular message attachments that were in the original message

The resulting plain text message can be represented in the following formats:
  RFC 5322-compliant message composed of only US-ASCII text with a Winmail.dat
  attachment encoded in Uuencode
  Multipart MIME-encoded message that has a Winmail.dat attachment

Outlook and other email clients that fully understand TNEF process the Winmail.dat
attachment and display the original message content without ever displaying the
Winmail.dat attachment. Email clients that don't understand TNEF may present TNEF
messages in any of the following ways:
  The plain text version of the message is displayed, and the message contains an
  attachment named Winmail.dat, Win.dat, or some other generic name such as Att

<!-- p.1878 -->

        nnnnn.dat or Att nnnnn.eml where the nnnnn placeholder represents a random
        number.
        The plain text version of the message is displayed. The TNEF attachment is ignored or
        removed. The result is a plain text message.
        Messaging servers that understand TNEF can be configured to remove TNEF
        attachments from incoming messages. The result is a plain text message. Moreover,
        some email clients may not understand TNEF, but recognize and ignore TNEF
        attachments. The result is a plain text message.

     There are third-party utilities that can help convert Winmail.dat attachments.

     TNEF is understood by all versions of Exchange since Exchange Server version 5.5.

     Summary Transport Neutral Encapsulation Format (STNEF): STNEF is equivalent to TNEF.
     However, STNEF messages are encoded differently than TNEF messages. Specifically,
     STNEF messages are always MIME-encoded, and always have the Content-Transfer-
     Encoding value Binary . Therefore, there's no plain text representation of the message,
     and there's no distinct Winmail.dat attachment contained in the body of the message.
     The whole message is represented by using only binary data. Messages that have a
     Content-Transfer-Encoding value of Binary can only be transferred between messaging
     servers that support and advertise the BINARYMIME and CHUNKING SMTP extensions as
     defined in RFC 3030. The messages are always transferred between messaging servers by
     using the BDAT command, instead of the standard DATA command.

     STNEF is understood by all versions of Exchange since Exchange 2000. STNEF is
     automatically used for all messages transferred between Exchange servers in the
     organization since native mode Exchange Server 2003.

     Exchange never sends STNEF messages to external recipients. Only TNEF messages can
     be sent to recipients outside the Exchange organization.

Content conversion options for external recipients
The content conversion options that you can set in an Exchange organization for external
recipients can be described in the following categories:

     TNEF conversion options: These conversion options specify whether TNEF should be
     preserved or removed from messages that leave the Exchange organization.
     Message encoding options: These options specify message encoding options, such as
     MIME and non-MIME character sets, message encoding, and attachment formats.

These conversion and encoding options are independent of one another. For example, whether
TNEF messages can leave the Exchange organization isn't related to the MIME encoding

<!-- p.1879 -->

settings or plain text encoding settings of those messages.

You can specify the content conversion at various levels of the Exchange organization as
described in the following list:

     Remote domain settings: Remote domains define the settings for outgoing message
     transfers between the Exchange organization and external domains.. Even if you don't
     create remote domain entries for specific domains, there's a predefined remote domain
     named Default that applies to all remote address spaces (*). For more information about
     remote domains, see Remote Domains.

     Mail user and mail contact settings: Mail users and mail contacts are similar because
     both have external email addresses and contain information about people outside the
     Exchange organization. The main difference is mail users have accounts that they can use
     to log on to Active Directory and access resources in the organization. For more
     information, see Recipients.

     Outlook settings: You can set these message formatting and encoding options in
     Outlook:
        Message format: You can set the default message format for all messages. You can
        override the default message format as you compose a specific message.
        Internet message format: You can control whether TNEF messages are sent to remote
        recipients or whether they are first converted to a more compatible format. You can
        also specify various message encoding options for messages sent to remote recipients.
        These settings don't apply to messages sent to recipients in the Exchange
        organization.
        Internet recipient message format (Outlook 2010 or earlier): You can control whether
        TNEF messages are sent to specific contacts in your Contacts folder. These conversion
        options aren't available for recipients in the Exchange organization.
        Internet recipient message encoding options (Outlook 2010 or earlier): You can
        control the MIME or plain text encoding options for specific contacts in your Contacts
        folder. These conversion options aren't available for recipients in the Exchange
        organization.
        International options: You can control the character sets used in messages.

     For more information about these settings, see TNEF conversion options and Message
     encoding options in Exchange Server.

Understanding the structure of email messages
To better understand the content conversion options for external recipients, you need to
understand the structure of email messages. An SMTP message is based on plain 7-bit US-

<!-- p.1880 -->

ASCII text to compose and send email messages. A standard SMTP message consists of the
following elements:

     Message envelope: The message envelope is defined in RFC 5321. The message envelope
     contains information required to transmit and deliver the message. Recipients never see
     the message envelope, because it's generated by the message transmission process and
     isn't actually part of the message contents.

     Message contents: The message contents are defined in RFC 5322. The message contents
     consist of the following elements:

        Message header: The message header is a collection of header fields. Header fields
        consist of a field name, followed by a colon (:) character, followed by a field body, and
        ended by a carriage return/line feed (CR/LF) character combination.

        A field name must be composed of printable US-ASCII text characters except the colon
        (:) character. Specifically, ASCII characters that have values from 33 through 57 and 59
        through 126 are permitted.

        A field body may be composed of any US-ASCII characters, except for the carriage
        return (CR) character and the line feed (LF) character. However, a field body may
        contain the CR/LF character combination when used in header folding. Header folding
        is the separation of a single header field body into multiple lines as described in
        section 2.2.3 of RFC 5322. Other field body syntax requirements are described in
        sections 3 and 4 of RFC 5322.

        Message body: The message body is a collection of lines of US-ASCII text characters
        that appears after the message header. The message header and the message body
        are separated by a blank line that ends with the CR/LF character combination. The
        message body is optional. Any line of text in the message body must be less than 998
        characters. The CR and LF characters can only appear together to indicate the end of a
        line.

When SMTP messages contain elements that aren't plain US-ASCII text, the message must be
encoded to preserve those elements. The MIME standard defines a method of encoding
content in messages that isn't text. MIME allows for text in other character sets, attachments
without text, multipart message bodies, and header fields in other character sets. MIME is
defined in RFC 2045, RFC 2046, RFC 2047, RFC 4288, RFC 4289, and RFC 2049. MIME defines a
collection of header fields that specifies additional message attributes. The following sections
describe some important MIME header fields.

MIME-Version header field
