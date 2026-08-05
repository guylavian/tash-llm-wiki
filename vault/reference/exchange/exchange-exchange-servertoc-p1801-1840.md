---
title: "Exchange Server — pages 1801-1840"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1801-1840
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1801-1840
family: exchange
documentKind: "doc"
abstract: "Properties of messages in queues Article • 04/30/2025 APPLIES TO: 2016 2019 Subscription Edition Filtering messages in queues by one or more message properties in Exchange Server allows you to quickly locate messages and take action on them. When an email message is sent to mult"
---

# Exchange Server — pages 1801-1840

<!-- p.1801 -->

Properties of messages in queues
Article • 04/30/2025

APPLIES TO:        2016       2019    Subscription Edition

Filtering messages in queues by one or more message properties in Exchange Server allows you to quickly
locate messages and take action on them. When an email message is sent to multiple recipients, the
message might be located in multiple queues on the server. When you filter messages in queues by
message properties, you can locate messages across all queues. The following scenarios are examples of
how you might use message filtering to manage mail flow:

       The Submission queue on the Mailbox server or Edge Transport server that receives email from the
       Internet has a high volume of messages that are queued for delivery. Many of the messages have the
       same subject. Therefore, you suspect that spam is being sent to your organization. You can create a
       filter to view all the messages that meet the subject criteria. If you determine that the messages are
       spam, you can select them all and delete them from the delivery queue without sending an NDR.

       A user reports that mail flow is slow. You examine the queues and see that many messages with
       random subjects appear to be coming from a single domain. You can create a filter to view all the
       queued messages from that domain. If you determine that the messages are spam, you can select
       them all and delete them from the queues without sending an NDR.

You can create message filters in Queue Viewer in the Exchange Toolbox, or by using the Filter parameter on
the message management cmdlets. Note that the message management cmdlets support more filterable
properties than Queue Viewer.

For more information about Queue Viewer, see Queue Viewer. For more information about the message
management cmdlets, see Procedures for messages in queues and Find queues and messages in queues in
the Exchange Management Shell.

Message properties to use as filters
The following table describes the message properties that you can use as filters in Queue Viewer and the
Exchange Management Shell.

                                                                                                      ﾉ   Expand table

 Queue        Exchange Management Shell        Comparison    Description
 Viewer                                        operators

 n/a          AccountForest                    n/a           his property is reserved for internal Microsoft use, and isn't
                                                             used in on-premises Exchange organizations.
                                                             In on-premises Exchange, this property is the forest root
                                                             domain where the mailbox resides (for example,
                                                             contoso.com).

 n/a          ComponentLatency                 n/a           This property is reserved for internal Microsoft use, and isn't
                                                             used in on-premises Exchange organizations.

<!-- p.1802 -->

Queue      Exchange Management Shell   Comparison       Description
Viewer                                 operators

Date       DateReceived                Greater          The date/time when the message was placed in the queue.
Received                               Than ( -gt )

                                       Greater
                                       Than or
                                       Equals ( -ge )

                                       Less Than ( -
                                       lt )

                                       Less Than or
                                       Equals ( -le )

n/a        DeferReason                 Equals ( -eq )   Indicates why the message was deferred. If the message
                                                        wasn't deferred, this property has the value None . A deferred
                                       Does not         message is returned to the Submission queue because of
                                       equal ( -ne )    transient errors that were encountered during recipient
                                                        resolution. For more information about deferred messages,
                                       Contains ( -
                                                        see Recipient resolution in Exchange Server. The possible
                                       like )
                                                        values are:

                                                        AD Transient Failure During Content Conversion )

                                                        AD Transient Failure During Resolve

                                                        Agent

                                                        Ambiguous Recipient

                                                        Config Update

                                                        Loop Detected

                                                        Marked As Retry Delivery If Rejected

                                                        Recipient does not have a mailbox database

                                                        Recipient Thread Limit Exceeded

                                                        Rerouted By Store Driver

                                                        Storage Transient Failure During Content Conversion

                                                        Target Site Inbound Mail Disabled

                                                        Transient Accepted Domains Load Failure

                                                        Transient Attribution Failure

                                                        Transient Failure

n/a        Directionality              Equals ( -eq )   Valid values are Incoming , Originating , and Undefined .

                                       Does Not
                                       Equal ( -ne )

<!-- p.1803 -->

Queue        Exchange Management Shell         Comparison       Description
Viewer                                         operators

Expiration   ExpirationTime                    Greater          The date/time when the message will expire and be deleted
Time                                           Than ( -gt )     from the queue if the message can't be delivered.

                                               Greater
                                               Than or
                                               Equals ( -ge )

                                               Less Than ( -
                                               lt )

                                               Less Than or
                                               Equals ( -le )

n/a          ExternalDirectoryOrganizationId   n/a              This property is reserved for internal Microsoft use, and isn't
                                                                used in on-premises Exchange organizations.
                                                                In on-premises Exchange, the value is 00000000-0000-0000-
                                                                0000-000000000000 .

From         FromAddress                       Equals ( -eq )   The SMTP address of the sender.
Address
                                               Does Not
                                               Equal ( -ne )

                                               Contains ( -
                                               contains )

n/a          Identity                          n/a              The identity of the message in the form of <Server>\
                                                                <Queue>\ <MessageInteger>. For more information see
                                                                Message identity.

Internet     InternetMessageId                 Equals ( -eq )   The value of the Message-Id: header field in the message
Message                                                         header. This value is constant for the lifetime of the
ID                                             Does Not         message. For messages created in Exchange, the value is in
                                               Equal ( -ne )    the format <GUID@ServerFQDN> , including the angle brackets
                                                                (< >). For example,
                                               Contains ( -
                                                                <4867a3d78a50438bad95c0f6d072fca5@mailbox01.contoso.com> .
                                               contains )

Last Error   LastError                         Equals ( -eq )   The last error that was recorded for a message. For example,
                                                                A matching connector cannot be found to route the
                                               Does Not         external recipient .
                                               Equal ( -ne )

                                               Contains ( -
                                               contains )

                                               Is Present

                                               Is Not
                                               Present

n/a          LockReason                        n/a              This property is reserved for internal Microsoft use, and isn't
                                                                used in on-premises Exchange organizations.

n/a          MessageLatency                    Equals ( -eq )   The amount of time that elapsed between when the
                                                                message first entered the Submission queue on the server,

<!-- p.1804 -->

Queue      Exchange Management Shell   Comparison       Description
Viewer                                 operators

                                       Does not         and when the message was placed in the queue. The value
                                       equal ( -ne )    uses the syntax hh:mm:ss.ff, where hh = hour, mm = minute,
                                                        ss = second, and ff = fractions of a second.
                                       Greater than
                                       ( -gt )

                                       Greater than
                                       or equal to
                                       ( -ge )

                                       Less than ( -
                                       lt )

                                       Less than or
                                       equal to ( -
                                       le

Message    MessageSourceName           Equals ( -eq )   The name of the transport component that submitted the
Source                                                  message to the queue. For example, if the message came in
Name                                   Does Not         through a Receive connector, the value is: SMTP:
                                       Equal ( -ne )    <ConnectorName>. If the message is a delivery status
                                                        notification (DSN), the value is DSN .
                                       Contains ( -
                                       contains )

n/a        OriginalFromAddress         Equals ( -eq )   The original sender's email address for any new side effect
                                                        messages that are created during categorization (for
                                       Does not         example, journal rules, NDRs, or mail flow rules rules, also
                                       equal ( -ne )    known as transport rules).

                                       Contains ( -
                                       like )

n/a        Priority                    Equals ( -eq )   The priority (importance) of the message that's assigned by
                                                        the user in Microsoft Outlook or Outlook on the web. Valid
                                       Does not         values are Low , Normal , and High . For more information, see
                                       equal ( -ne )    Priority Queuing.

Queue ID   Queue                       Equals ( -eq )   The queue that holds the message. The queue identity uses
                                                        the syntax <Server>\<Queue>. For more information, see
                                       Does Not         Queue identity.
                                       Equal ( -ne )

                                       Contains ( -
                                       contains )

n/a        Recipients                  Contains ( -     An array that contains details about the recipient and the
                                       like )           Send connector that will be used, or any errors that were
                                                        encountered. For example:
                                                        {chris@contoso.com;2;2;A matching connector cannot be
                                                        found to route the external recipient;16;<No Matching
                                                        Connector>;0}

n/a        RetryCount                  Equals ( -eq )   The number of times that delivery of the message to the
                                                        destination was tried, either automatically or manually.

<!-- p.1805 -->

Queue       Exchange Management Shell   Comparison       Description
Viewer                                  operators

                                        Does not
                                        equal ( -ne )

                                        Greater than
                                        ( -gt )

                                        Greater than
                                        or equal to
                                        ( -ge )

                                        Less than ( -
                                        lt )

                                        Less than or
                                        equal to ( -
                                        le

SCL         SCL                         Equals ( -eq )   The spam confidence level (SCL) rating of the message. Valid
                                                         SCL entries are integers 0 through 9, or -1 for internal
                                        Does Not         (authenticated) messages. For more information, see
                                        Equal ( -ne )    Exchange spam confidence level (SCL) thresholds.

                                        Greater
                                        Than ( -gt )

                                        Greater
                                        Than or
                                        Equals ( -ge )

                                        Less Than ( -
                                        lt )

                                        Less Than or
                                        Equals ( -le

Size (KB)   Size                        Equals ( -eq )   The size of the message. In Queue Viewer, you need to
                                                         specify the message size in kilobytes (KB), but in the
                                        Does Not         Exchange Management Shell, you can also specify other
                                        Equal ( -ne )    sizes, for example, bytes (B) or megabytes (MB).

                                        Greater
                                        Than ( -gt )

                                        Greater
                                        Than or
                                        Equals ( -ge )

                                        Less Than ( -
                                        lt )

                                        Less Than or
                                        Equals ( -le

Source IP   SourceIP                    Equals ( -eq )   The IPv4 or IPv6 address of the server that submitted the
                                                         message to the Exchange server that holds the message in

<!-- p.1806 -->

Queue     Exchange Management Shell   Comparison       Description
Viewer                                operators

                                      Does Not         the queue. The address could be the IP address of a remote
                                      Equal ( -ne )    SMTP server, or the IP address of the local Exchange server.

Status    Status                      Equals ( -eq )   The current message status. Valid values are:
                                                       Active
                                      Does Not
                                      Equal ( -ne )    Locked

                                                       Pending Remove ( PendingRemove )

                                                       Pending Suspend ( PendingSuspend )

                                                       Ready

                                                       Retry

                                                       Suspended

                                                       For more information, see Message status.

Subject   Subject                     Equals ( -eq )   The subject of the message (from the Subject: header field).

                                      Does Not
                                      Equal ( -ne )

                                      Contains ( -
                                      contains )

                                      Is Present
                                      Is Not
                                      Present

n/a       TrafficType                 n/a              This property is reserved for internal Microsoft use, and isn't
                                                       used in on-premises Exchange organizations.
                                                       In on-premises Exchange, this property is blank or has the
                                                       value Email .

n/a       TrafficSubType              n/a              This property is reserved for internal Microsoft use, and isn't
                                                       used in on-premises Exchange organizations.

<!-- p.1807 -->

Exchange Server: Queue Viewer
Article • 04/30/2025

APPLIES TO:        2016       2019    Subscription Edition

Queue Viewer is part of the Exchange Toolbox that's installed on Mailbox servers and Edge
Transport servers in Exchange Server 2016 and Exchange Server 2019. Queue Viewer is a
Microsoft Management Console (MMC) snap-in that you can use to view information about
and take action on queues and messages in queues. Queue Viewer is useful for
troubleshooting mail flow issues and identifying spam.

Queue Viewer is located in the Mail flow tools section of the Exchange Toolbox.

To find and open the Exchange Toolbox, use one of the following procedures:

      Windows 10: Click Start > All Apps > Microsoft Exchange Server <Version> > Exchange
      Toolbox.

      Windows Server 2012 R2 or Windows 8.1: On the Start screen, open the Apps view by
      clicking the down arrow near the lower-left corner or swiping up from the middle of the
      screen. The Exchange Toolbox shortcut is in a group named Microsoft Exchange Server
      <Version>.

      Windows Server 2012: Use any of the following methods:

          On the Start screen, click an empty area, and type Exchange Toolbox.

          On the desktop or the Start screen, press Windows key + Q. In the Search charm, type
          Exchange Toolbox.

          On the desktop or the Start screen, move your cursor to the upper-right corner, or
          swipe left from the right edge of the screen to show the charms. Click the Search
          charm, and type Exchange Toolbox.

      When the shortcut appears in the results, you can select it.

For more information about queues and messages in queues, see Queues and messages in
queues.

Topics that contain Queue Viewer procedures
The topics in the following table contain procedures that use Queue Viewer:

                                                                                 ﾉ   Expand table

<!-- p.1808 -->

Topic                        Description

Connect to a Server in       By default, Queue Viewer opens the queue database on the server where
Queue Viewer                 you opened Queue Viewer. However, you can connect to a different
                             server.

Set Queue Viewer Options     You can configure the queue and message refresh intervals, and the
                             number of items that are displayed on each page.

View queued message          Explains how to use Queue Viewer to view messages, and explains the
properties in Queue Viewer   message properties.

Export Lists from Queue      You can use the Export List link in the action pane to export the list of
Viewer                       queues or a list of messages for troubleshooting and diagnostics.

Queue properties             Describes the queue properties, and shows the properties that are
                             available in Queue View versus the Exchange Management Shell.

Properties of messages in    Describes the message properties, and shows the properties that are
queues                       available in Queue View versus the Exchange Management Shell.

Procedures for queues        Explains how to view, retry, resubmit, suspend, and resume queues.

Procedures for messages in   Explains how to remove, suspend, resume, and redirect messages in
queues                       queues.

<!-- p.1809 -->

Exchange Server: View queued message
properties in Queue Viewer
Article • 04/30/2025

APPLIES TO:        2016      2019     Subscription Edition

You can use the Queue Viewer in the Exchange Toolbox to view queues and the properties of
messages in queues. In Exchange Server 2016 and Exchange Server 2019, Queue Viewer is
available on Mailbox servers and Edge Transport servers.

For more information about queues, see Queues and messages in queues. For more
information about Queue Viewer, see Queue Viewer.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Queues" entry in the Mail flow
      permissions topic.

      To find and open the Exchange Toolbox, use one of the following procedures:

         Windows 10: Click Start > All Apps > Microsoft Exchange Server <Version> >
         Exchange Toolbox.

         Windows Server 2012 R2 or Windows 8.1: On the Start screen, open the Apps view by
         clicking the down arrow near the lower-left corner or swiping up from the middle of
         the screen. The Exchange Toolbox shortcut is in a group named Microsoft Exchange
         Server <Version>.

         Windows Server 2012: Use any of the following methods:
            On the Start screen, click an empty area, and type Exchange Toolbox.
            On the desktop or the Start screen, press Windows key + Q. In the Search charm,
            type Exchange Toolbox.
            On the desktop or the Start screen, move your cursor to the upper-right corner, or
            swipe left from the right edge of the screen to show the charms. Click the Search
            charm, and type Exchange Toolbox.

         When the shortcut appears in the results, you can select it.

      You can also use the Get-Message cmdlet in the Exchange Management Shell to view
      additional message properties that aren't visible in Queue Viewer. For more information,

<!-- p.1810 -->

   see Properties of messages in queues and Find queues and messages in queues in the
   Exchange Management Shell.

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online     , or Exchange Online Protection .

Use Queue Viewer to view the properties of a
message
 1. In the Exchange Toolbox, in the Mail flow tools section, double-click Queue Viewer to
   open the tool in a new window.

 2. In Queue Viewer, select the Messages tab to see the list of messages that are currently
   queued for delivery in your organization. The list of messages displays the following
   information:

         From Address: The sender's email address.

         Status: A message can have one of the following status values:

         Active: If the message is in a delivery queue, the message is being delivered to its
         destination. If the message is in the Submission queue, the message is being
         processed by the categorizer.

         Pending Remove: The message was deleted by the administrator, but was already
         being delivered. The message will be deleted if the delivery ends in an error that
         causes the message to re-enter the queue. Otherwise, delivery will continue.

         Pending Suspend: The message was suspended by the administrator, but was
         already being delivered. The message will be suspended if the delivery ends in an
         error that causes the message to re-enter the queue. Otherwise, delivery will
         continue.

         Ready: The message is waiting in the queue, and is ready to be processed.

         Retry: The queue's last connection attempt failed. The message is waiting for the
         next queue retry.

<!-- p.1811 -->

Suspended: The message was suspended by the administrator. For more
information, see Suspend messages in queues.

Size (KB): The size of the message rounded up to the nearest kilobyte (KB).

SCL: The spam confidence level (SCL) rating of the message. Valid SCL entries are
integers 0 through 9, or -1 for internal (authenticated) messages. For more
information, see Exchange spam confidence level (SCL) thresholds.

Queue ID: The queue that holds the message. The queue identity uses the syntax
<Server>\ <Queue>, where <Queue> is one of the following values:

Persistent queue name

Poison: Isolates messages that contain errors and are determined to be harmful to
Exchange after a server or service failure. The messages may be genuinely harmful in
their content and format, or the messages might have been the victims of a poorly
written transport agent or a software bug that crashed the Exchange server while it
was processing the otherwise valid messages.

Submission: Holds messages that have been accepted by the Transport service, but
haven't been processed. Messages in the Submission queue are either waiting to be
processed, or are actively being processed.

Unreachable: Contains messages that can't be routed to their destinations. Typically,
an unreachable destination is caused by configuration changes that have modified
the routing path for delivery. Regardless of destination, all messages that have
unreachable recipients reside in this queue.

Delivery queue name: The value of the NextHopDomain property of the queue,
which is effectively the name of the queue. For example, a domain name, Active
Directory site name, or database availability group (DAG) name. For more
information, see NextHopSolutionKey.

Message Source Name: The Exchange component that submitted the message to
the queue. For example, SMTP:Default <ServerName> .

Subject: The subject of the message.

Last Error: The last error that was encountered for the message.

For example, if you didn't create a Send connector to deliver Internet mail, messages
that are addressed to external recipients will go to the Unreachable queue, and the
Last Error value for the message will be: A matching connector cannot be found to

<!-- p.1812 -->

       route the external recipient . For more information about creating a Send

       connector, see Create a Send connector to send mail to the Internet.

       For more information about SMTP error codes, see DSNs and NDRs in Exchange
       Server.

3. When you right-click a message and select Properties, additional details are available on
  the General and Recipient Information tabs.

       The General tab displays the same Subject, From Address, Status, Size, Message
       Source Name, SCL, and Last Error values that are shown in the list of messages. The
       following additional properties are also displayed on the General tab:
       Identity: The identity of the message. The message identity uses the syntax
       <Server>\ <Queue>\ <MessageInteger>, where <Queue> is the identity of the
       queue as described in the Queue ID property, and <MessageInteger> is the unique
       integer value of the message that's displayed in the Identity property of the Get-
       Message cmdlet.
       Internet Message ID: The value of the Message-Id: header field in the message
       header. This value is constant for the lifetime of the message. For messages created
       in Exchange, the value is in the format <GUID@ServerFQDN> , including the angle
       brackets (< >). For example,
        <4867a3d78a50438bad95c0f6d072fca5@mailbox01.contoso.com> .

       Source IP: The IPv4 or IPv6 address of the internal Exchange server or external
       messaging server that submitted the message.
       Date Received: The date-time when the message entered the queue.
       Expiration Time: The date-time when the message will expire and will be deleted
       from the queue if the message can't be delivered.
       Recipients: The recipients in the message, with any corresponding error messages.
       To see the status and error messages for each recipient, go to the Recipient
       Information tab.
       The Recipient Information tab displays the Address, Status, and Last Error values
       for each recipient in the message. The Status value for a recipient can be Complete,
       Ready, or Retry.

<!-- p.1813 -->

Find queues and messages in queues in the
Exchange Management Shell
Article • 04/30/2025

APPLIES TO:        2016      2019     Subscription Edition

As in previous versions of Exchange, you can use the Exchange Management Shell in Exchange
Server to view information about queues and messages, and use that information to take
action on queues and messages. Typically, an active Exchange contains a large number of
queues and messages to be delivered, so it's important to understand how to identify the
queues or messages that you want to manage.

Note that you can also use Queue Viewer in the Exchange Toolbox to manage queues and
messages in queues. However, the queue and message viewing cmdlets in the Exchange
Management Shell support more filterable properties and filter options than Queue Viewer. For
more information about using Queue Viewer, see Queue Viewer.

Also remember that queues exist on Mailbox servers and Edge Transport servers (the Transport
service). For more information about queues and messages in queues, see Queues and
messages in queues.

Queue filtering parameters
The following table summarizes the filtering parameters that are available on the queue
management cmdlets.

                                                                                      ﾉ    Expand table

 Cmdlet           Filtering     Comments
                  parameters

 Get-Queue        Exclude       You can use the Include and Exclude parameters with the other filtering
                  Filter        parameters in the same command.
                  Identity      You can't use the Identity and Filter parameters in the same command.
                  Include       The Server parameter specifies the server where you want to run the
                  Server        command. You can't use the Server and Identity parameters in the same
                                command, but you can use the Server parameter with the other filtering
                                parameters in the same command.

 Resume-          Identity      You can't use the Identity parameter with the other filtering parameters
 Queue            Filter        in the same command.
 Retry-Queue      Server        The Server parameter specifies the server where you want to run the
 Suspend-                       command. You can use the Server and Filter parameters in the same
 Queue                          command.

<!-- p.1814 -->

 Cmdlet            Filtering     Comments
                   parameters

 Get-              Dag           You need to use one of the Dag, Site, Server, or Forest parameters, but
 QueueDigest       Filter        you can't use any of them together in the same command.
                   Forest        You can use the Filter parameter with any of the other filtering
                   Server        parameters.
                   Site

Queue identity
The Identity parameter uses the basic syntax <Server>\ <Queue>. Typically, this value uniquely
identifies the queue, so you can't use other filtering parameters with the Identity parameter.
The exception is the Get-Queue cmdlet, where you can use the Include and Exclude parameters
with the Identity parameter.

The following table explains the Identity parameter syntax on the queue management cmdlets.

                                                                                        ﾉ   Expand table

 Identity parameter value       Description

 <Server>\                      A persistent queue on the specified or local server.
 <PersistentQueueName> or       <PersistentQueueName> is Submission , Unreachable , or Poison .
 <PersistentQueueName>          For more information about persistent queues, see Types of queues.

 <Server>\<NextHopDomain> or    A delivery queue on the specified or local server.
 <NextHopDomain>                <NextHopDomain> is the name of the queue from the value of the
                                NextHopDomain property of the queue. For example, the address space
                                of a Send connector, the name of an Active Directory site, or the name of
                                a DAG. For more information, see NextHopSolutionKey.

 <Server>\<QueueInteger> or     A delivery queue on the specified or local server.
 <QueueInteger>                 <QueueInteger> is the unique integer value that's assigned to a delivery
                                queue or a shadow queue in the queue database. However, you need to
                                run the Get-Queue cmdlet to find this value in the Identity or
                                QueueIdentity properties.

 <Server>\Shadow\               A shadow queue on the specified or local server. For more information
 <QueueInteger> or Shadow\      about shadow queues and shadow redundancy, see Shadow redundancy
 <QueueInteger>                 in Exchange Server.

 <Server>\* or *                All queues on the specified or local server.
                                Note: Identity is a positional parameter, which means you can specify the
                                value without specifying the -Identity qualifier. For example, the
                                following commands produce the same result:
                                Get-Queue -Identity *

<!-- p.1815 -->

 Identity parameter value       Description

                                 Get-Queue *
                                 Get-Queue

Filter parameter on queue cmdlets
You can use the Filter parameter on all of the queue management cmdlets to identify one or
more queues based on the properties of the queues. The Filter parameter creates an OPath
filter with comparison operators to restrict the command to queues that meet the filter criteria.
You can use the logical operator -and to specify multiple conditions for the match. Here's a
generic example of the syntax:

Get-Queue -Filter "<Property1> -<ComparisonOperator> '<Value1>' -and <Property2> -
<ComparisonOperator> '<Value2>'..."

For a complete list of queue properties you can use with the Filter parameter, see Queue
properties.

For a list of comparison operators you can use with the Filter parameter, see the Comparison
operators to use when filtering queues or messages section in this topic.

For examples of procedures that use the Filter parameter to view and manage queues, see
Procedures for queues.

Include and Exclude parameters on Get-Queue
You can use the Include and Exclude parameters on the Get-Queue cmdlet by themselves, with
each othe , or with the other filtering parameters to fine-tune your results. For example, you
can:

       Exclude empty queues.

       Exclude queues to external destinations.

       Include queues that have a specific value of DeliveryType.

The Include and Exclude parameters use the following queue properties to filter queues:

                                                                                   ﾉ   Expand table

 Value          Description                                    Example

 DeliveryType   Includes or excludes queues based on the       Returns all delivery queues on the
                DeliveryType property that defines how the     local server where the next hop is a

<!-- p.1816 -->

 Value          Description                                        Example

                message will be transmitted to the next hop. The   Send connector that's hosted on the
                valid values are described in                      local server and is configured for
                NextHopSolutionKey.                                smart host routing.
                You can specify multiple values separated by       Get-Queue -Include
                commas.                                            SmartHostConnectorDelivery

 Empty          Includes or excludes empty queues. Empty           Returns all queues on the local server
                queues have the value 0 in the MessageCount        that contain messages.
                property.                                          Get-Queue -Exclude Empty

 External       Includes or excludes queues that have the value    Returns all internal queues on the
                External in the NextHopCategory property.          local server.
                                                                   Get-Queue -Exclude External
                External queues always have one of the following
                values for DeliveryType:

                      DeliveryAgent
                      DnsConnectorDelivery
                      NonSmtpGatewayDelivery
                      SmartHostConnectorDelivery

                For more information, see NextHopSolutionKey.

 Internal       This value includes or excludes queues that have   Returns all internal queues on the
                the value Internal in the NextHopCategory          local server.
                property. Note that a message for an external      Get-Queue -Include Internal
                recipient may require multiple internal hops
                before it reaches a gateway server where it's
                delivered externally.

Note that you can duplicate the functionality of the Include and Exclude parameters by using
the Filter parameter. For example, the following commands produce the same result:

      Get-Queue -Exclude Empty

      Get-Queue -Filter "MessageCount -gt 0"

However, as you can see, the syntax of the Include and Exclude parameters is simpler and easier
to remember.

Get-QueueDigest
The Get-QueueDigest cmdlet allows you to view information about some or all of the queues
in your organization by using a single command. Specifically, the Get-QueueDigest cmdlet
allows you to view information about queues based on their location on servers, in DAGs, in
Active Directory sites, or in the whole Active Directory forest.

<!-- p.1817 -->

Note that queues on a subscribed Edge Transport server aren't included in the results. Also,
Get-QueueDigest is available on an Edge Transport server, but the results are restricted to local
queues on the Edge Transport server.

  ７ Note

  By default, the Get-QueueDigest cmdlet displays delivery queues that contain ten or more
  messages, and the results are between one and two minutes old. For instructions on how
  to change these default values, see Configure Get-QueueDigest.

The following table describes the filtering and sorting parameters that are available on the Get-
QueueDigest cmdlet.

                                                                                            ﾉ   Expand table

 Parameter      Description

 Dag, Server,   These parameters are mutually exclusive (can't be used in the same command), and set the
 or Site        scope for the cmdlet. You need to specify one of these parameters or the Forest switch.
                Typically, you would use the name of the server, DAG or Active Directory site, but you can
                use any value that uniquely identifies the server, DAG, or site. You can specify multiple
                servers, DAGs, or sites separated by commas.

 Forest         This switch is required if you aren't using the Dag, Server, or Site parameters. You don't
                specify a value with this switch. By using this switch, you get queues from all Exchange
                Mailbox servers in the local Active Directory forest. You can't use this switch to view
                queues in remote Active Directory forests.

 DetailsLevel   Normal is the default value. The following properties are returned in the results:

                      QueueIdentity
                      ServerIdentity
                      MessageCount

                Verbose returns the following additional properties in the results:

                      DeferredMessageCount
                      LockedMessageCount*
                      IncomingRate
                      OutgoingRate
                      Velocity
                      NextHopDomain
                      NextHopCategory
                      NextHopConnector
                      DeliveryType*
                      Status
                      RiskLevel*

<!-- p.1818 -->

 Parameter     Description

                     OutboundIPPool*
                     LastError
                     TlsDomain

               None omits the queue name from the Details column in the results.

               * These properties are reserved for internal Microsoft use, and aren't used in on-premises
               Exchange organizations. For more information about all properties in this list, see Queue
               properties.

 Filter        Filter queues based on the queue properties as described in the Filter parameter on queue
               cmdlets section. You can use any of the filterable queue properties as described in the
               Queue properties topic.

 GroupBy       Groups the queue results. You can group the results by one of the following properties:
                    DeliveryType
                    LastError
                    NextHopCategory
                     NextHopDomain
                     NextHopKey
                     Status
                     ServerName

               By default, the results are grouped by NextHopDomain. For information about these
               queue properties, see Queue properties.

 ResultSize    Limits the queue results to the value you specify. The queues are sorted in descending
               order based on the number of messages in the queue, and grouped by the value specified
               by the GroupBy parameter. The default value is 1000. This means that by default, the
               command displays the top 1000 queues grouped by NextHopDomain, and sorted by the
               queues containing the most messages to the queues containing the least messages.

 Timeout       The parameter specifies the number of seconds before the operation times out. The
               default value is 00:00:10 or 10 seconds.

This example returns all non-empty external queues on the servers named Mailbox01,
Mailbox02, and Mailbox03.

  PowerShell

  Get-QueueDigest -Server Mailbox01,Mailbox02,Mailbox03 -Include External -Exclude
  Empty

Message filtering parameters

<!-- p.1819 -->

The following table summarizes the filtering parameters that are available on the message
management cmdlets.

                                                                                          ﾉ    Expand table

 Cmdlet       Filtering       Comments
              parameters

 Get-         Filter          You can't use the Filter, Identity, or Queue parameters in the same
 Message      Identity        command.
              Queue           The Server parameter specifies the server where you want to run the
              Server          command. You can use the Server and Filter parameters in the same
                              command.

 Remove-      Filter          You need to use either the Identity parameter or the Filter parameter, but
 Message      Identity        you can't use them both in the same command.
 Resume-      Server          The Server parameter specifies the server where you want to run the
 Message                      command. You can use the Server and Filter parameters in the same
 Suspend-                     command.
 Message

 Redirect-    Server          This cmdlet drains active messages from all delivery queues on the
 Message                      specified server, so Server is the only filtering parameter that's available.
                              For more information, see Redirect messages in queues.

 Export-      Identity        This parameter isn't really a filter, because it uniquely identifies the
 Message                      message. To identify multiple messages for this cmdlet, use Get-Message
                              and pipe the results to Export-Message. For more information and
                              examples, see Export messages from queues.

Message identity
The Identity parameter on the message management cmdlets uniquely identifies a message in
one or more queues, so you can't use any other message filtering parameters. The Identity
parameter uses the basic syntax <Server>\<Queue>\<MessageInteger> .

The following table describes the syntax you can use with Identity parameter on the message
management cmdlets.

                                                                                          ﾉ    Expand table

 **Identity parameter      Description**
 value

 <Server>\<Queue>\         A message in a specific queue on the specified or local server.
 <MessageInteger> or       <Queue> is the identity of the queue as described in the Queue identity
                           section:

<!-- p.1820 -->

 **Identity parameter     Description**
 value

 <Queue>\                       Persistent queue name
 <MessageInteger>               Delivery queue name
                                Queue integer
                                Shadow queue identity

                           <MessageInteger> is the unique integer value that's assigned to the message
                          when it first enters the queue database on the server. If the message is sent
                          to multiple recipients that require multiple queues, all copies of the message
                          in all queues in the queue database have the same integer value. However,
                          you need to run the Get-Message cmdlet to find this value in the Identity or
                          MessageIdentity properties.

 <Server>\*\              All copies of the message in all queues in the queue database on the
 <MessageInteger> or *\   specified or local server.
 <MessageInteger> or
 <MessageInteger>

Filter parameter on message cmdlets
You can use the Filter parameter with the Get-Message, Remove-Message, Resume-Message,
and Suspend-Message cmdlets to identify one or more messages based on the properties of
the messages. The Filter parameter creates an OPath filter with comparison operators to restrict
the command to messages that meet the filter criteria. You can use the logical operator -and
to specify multiple conditions for the match. Here's a generic example of the syntax:

Get-Message -Filter "<Property1> -<ComparisonOperator> '<Value1>' -and <Property2> -

<ComparisonOperator> '<Value2>'..."

For a complete list of message properties you can use with the Filter parameter, see Message
properties).

For a list of comparison operators you can use with the Filter parameter, see the Comparison
operators to use when filtering queues or messages section in this topic.

For examples of procedures that use the Filter parameter to view and manage messages, see
Procedures for messages in queues.

Queue parameter
The Queue parameter is available only on the Get-Message cmdlet. You can use this parameter
to get all messages in a specific queue, or all messages from multiple queues by using the

<!-- p.1821 -->

wildcard character (*). When you use the Queue parameter, use the queue identity format
<Server>\<Queue> as described in the Queue identity section in this topic.

Comparison operators to use when filtering queues
or messages
When you create a queue or message filter expression by using the Filter parameter, you need
to include an comparison operator for the property value to match. The comparison operators
that you can use, and how each operator functions are described in the following table. For all
operators, the values compared aren't case sensitive.

                                                                                       ﾉ   Expand table

 Operator   Function                                       Code example

 -eq        Exact match of the specified value.            Show all queues that have a status of Retry:
                                                           Get-Queue -Filter "Status -eq 'Retry'"
                                                           Show all messages that have a status of Retry:
                                                           Get-Message -Filter "Status -eq 'Retry'"

 -ne        Does not match the specified value.            Show all queues that don't have a status of
                                                           Active:
                                                           Get-Queue -Filter "Status -ne 'Active'"
                                                           Show all messages that don't have a status of
                                                           Active:
                                                           Get-Message -Filter "Status -ne 'Active'"

 -gt        Greater than the specified integer or          Show queues that currently contain more
            date/time value.                               than 1,000 messages:
                                                           Get-Queue -Filter "MessageCount -gt 1000"
                                                           Show messages that currently have a retry
                                                           count that's more than 3:
                                                           Get-Message -Filter "RetryCount -gt 3"

 -ge        Greater than or equal to the specified         Show queues that currently contain 1,000 or
            integer or date/time value.                    more messages:
                                                           Get-Queue -Filter "MessageCount -ge 1000"
                                                           Show messages that currently have a retry
                                                           count that's 3 or more:
                                                           Get-Message -Filter "RetryCount -ge 3"

 -lt        Less than the specified integer or date/time   Show queues that currently contain less than
            value.                                         1,000 messages:
                                                           Get-Queue -Filter "MessageCount -lt 1000"
                                                           Show messages that have an SCL that's less

<!-- p.1822 -->

 Operator      Function                                         Code example

                                                                than 6:
                                                                Get-Message -Filter "SCL -lt 6"

 -le           Less than or equal to the specified integer or   Show queues that currently contain 1,000 or
               date/time value.                                 fewer messages:
                                                                Get-Queue -Filter "MessageCount -le 1000"
                                                                Show messages that have an SCL that's 6 or
                                                                less:
                                                                Get-Message -Filter "SCL -le 6"

 -like         Contains the specified text. You need to         Show queues that have a destination to any
               include the wildcard character (*) in the text   SMTP domain that ends in Contoso.com:
               string.                                          Get-Queue -Filter "Identity -like
                                                                '*contoso.com'"
                                                                Show messages that have a subject that
                                                                contains the text "payday loan":
                                                                Get-Message -Filter "Subject -like '*payday
                                                                loan*'"

You can specify a filter that evaluates multiple expressions by using the logical operator -and .
The queues or messages must match all of the filter conditions to be included in the results.

This example displays a list of queues that have a destination to any SMTP domain name that
ends in Contoso.com and that currently contain more than 500 messages.

  PowerShell

  Get-Queue -Filter "Identity -like '*contoso.com*' -and MessageCount -gt 500"

This example displays a list of messages that are sent from any email address in the
contoso.com domain that have an SCL value that's greater than 5.

  PowerShell

  Get-Message -Filter "FromAddress -like '*Contoso.com*' -and SCL -gt 5"

Advanced paging parameters
When you use the Exchange Management Shell to view queues and messages in queues, your
query retrieves one page of information at a time. The advanced paging parameters control
the size of the results, and the order that the results are displayed in. All advanced paging
parameters are optional and can be used with or without other filtering parameters on the Get-

<!-- p.1823 -->

Queue and Get-Message cmdlets. If you don't specify any advanced paging parameters, the
query returns the results in ascending order of identity.

By default, when you specify a sort order, the Identity property is always included and sorted in
ascending order, because the other available queue or message properties aren't unique.

You can use the BookmarkIndex and BookmarkObject parameters to mark a position in the
sorted results. If the bookmark object no longer exists when you retrieve the next page of
results, the results start with the closest item to the bookmark, which depends on the sort
order that you specify.

The advanced paging parameters are described in the following table.

                                                                                            ﾉ   Expand table

 Parameter         Description

 BookmarkIndex     Specifies the position in the results where the displayed results start. The value of this
                   parameter is a 1-based index in the total results. If the value is less than or equal to
                   zero, the first complete page of results is returned. If the value is set to Int.MaxValue ,
                   the last complete page of results is returned.
                   You can't use this parameter with the BookmarkObject parameter.

 BookmarkObject    Specifies the object in the results where the displayed results start. If you specify a
                   bookmark object, that object is used as the point to start the search. The rows before
                   or after that object (depending on the value of the SearchForward parameter) are
                   retrieved.
                   You can't use this parameter with the BookmarkIndex parameter.

 IncludeBookmark   Specifies whether to include the bookmark object in the results. Valid values are:
                   $true : The bookmark object is included in the results. This is the default value.
                   $false : The bookmark object isn't included in the results. Use this value when you run
                   a query for a limited result size, and then specify the last item as the bookmark for the
                   next query. This prevents the bookmark object from being included in both results.

 ResultSize        Specifies the number of results to display per page. If you don't specify a value, the
                   default result size of 1,000 objects is used. Exchange limits the results to 250,000.

 ReturnPageInfo    This is a hidden parameter. It returns information about the total number of results
                   and the index of the first object of the current page. The default value is $false .

 SearchForward     Specifies the direction of the search.
                   Bookmark specified: Search forward or backward in the results relative to the
                   bookmark index or object.
                   No bookmark specified: Search forward or backward in the results from the first or
                   last item in the results.
                   Valid values are:
                   $true : Search forward from the first item in the results, or from the specified
                   bookmark. If there are no results beyond the bookmark, the query returns the last full

<!-- p.1824 -->

 Parameter           Description

                     page of results. This is the default value.
                     $false : Search backward from the last item in the results, or from the specified
                     bookmark. If there is less than a full page of results beyond the bookmark, the query
                     returns the first full page of results.

 SortOrder           Specifies the message properties that control the sort order of the results. The order
                     that the properties are specified indicates a descending order of precedence (the
                     results are sorted by the first property, then those results are sorted by the second
                     property, and son on).
                     This parameter uses the syntax: <+|-><Property1>,<+|-><Property2>... , where + sorts
                     the property in ascending order, and - sorts the property in descending order.
                     If you don't use this parameter, the results are sorted by the Identity property in
                     ascending order.

This example shows how to use the advanced paging parameters in a query. The command
returns the first 500 messages on the specified server. The results are sorted first in ascending
order by sender address, and then in descending order by message size.

  PowerShell

  Get-Message -Server mailbox01.contoso.com -ResultSize 500 -SortOrder
  +FromAddress,-Size

This example returns the first 500 messages on the specified server in the specified sort order,
sets a bookmark object, excludes the bookmark object from the results, and retrieves the next
500 messages in the same sort order.

   1. Run the following command to retrieve the first page of results.

        PowerShell

        $Results=Get-Message -Server mailbox01.contoso.com -ResultSize 500 -SortOrder
        +FromAddress,-Size

   2. To set the bookmark object, run the following command to save the last element of the
     first page to a variable.

        PowerShell

        $Temp=$Results[$results.length-1]

   3. To retrieve the next 500 objects on the specified server, and to exclude the bookmark
     object, run the following command.

<!-- p.1825 -->

PowerShell

Get-Message -Server mailbox01.contoso.com -BookmarkObject:$Temp -
IncludeBookmark $false -ResultSize 500 -SortOrder +FromAddress,-Size

<!-- p.1826 -->

Change the location of the queue database
in Exchange Server
07/23/2025

APPLIES TO:        2016      2019     Subscription Edition

Exchange Server uses an Extensible Storage Engine (ESE) database for queue message storage.
All the different queues are stored in a single ESE database. Queues exist on Exchange Mailbox
servers and Edge Transport servers. For more information about queues, see Queues and
messages in queues.

Keys in the %ExchangeInstallPath%Bin\EdgeTransport.exe.config XML application configuration
file control the location of the queue database and the queue database transaction logs. This
file is associated with the Exchange Transport service. The following list explains each key in
more detail.

     QueueDatabasePath: Specifies the location of the queue database files. The files are:
        Trn.log

        Trntmp.log

     The default location is %ExchangeInstallPath%TransportRoles\data\Queue .

     QueueDatabaseLoggingPath: Specifies the location of the queue database transaction log
     files. The files are:
        Trn nnn.log

        Trnres00001.jrs

        Trnres00002.jrs
        Temp.edb : This file verifies the queue database schema when the Exchange Transport

        service starts. Although Temp.edb isn't a transaction log file, it's kept in the same
        location as the transaction log files.

     The default location is %ExchangeInstallPath%TransportRoles\data\Queue .

What do you need to know before you begin?
     Estimated time to complete: 15 minutes.

     Exchange permissions don't apply to the procedures in this article. These procedures are
     performed in the operating system of the Exchange server.

<!-- p.1827 -->

   When you stop or restart the Exchange Transport service, mail flow on the server is
   interrupted.

   When you change the location of the queue database or the transaction logs, the existing
   queue database and transaction log files aren't moved. A new queue database and new
   transaction logs are created at the new location. The old files are left at the old location,
   but they're no longer used. If you want to reuse the old queue database or transaction
   log files at the new location, you need to move the files to the new location while the
   Exchange Transport service is stopped.

   The folder for the queue database and transaction logs needs the following permissions:

      Network Service: Full Control

      System: Full Control

      Administrators: Full Control

      If the folder doesn't exist, but the parent folder has these permissions, the new folder
      is created automatically.

   Any customized Exchange or Internet Information Server (IIS) settings that you made in
   Exchange XML application configuration files on the Exchange server (for example,
   web.config files or the EdgeTransport.exe.config file) will be overwritten when you install
   an Exchange Cumulative Update (CU). Be sure save this information so you can easily
   reapply the settings after the install. After you install the Exchange CU, you need to
   reconfigure these settings.

   For information about keyboard shortcuts that might apply to the procedures in this
   article, see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
 Server | Management.

Use the Command Prompt to create a new queue
database and transaction logs in a new location
 1. Create the folder where you want to keep the queue database and transaction logs. Make
   sure that the correct permissions are applied to the folder.

<!-- p.1828 -->

   2. In a Command prompt window, open the EdgeTransport.exe.config file in Notepad by
     running the following command:

        Console

        Notepad %ExchangeInstallPath%Bin\EdgeTransport.exe.config

   3. Find and modify the following keys in the <appSettings> section.

        XML

        <add key="QueueDatabasePath" value="<LocalPath>" />
        <add key="QueueDatabaseLoggingPath" value="<LocalPath>" />

     For example, to create a new queue database and transaction logs in D:\Queue\QueueDB,
     use the following values:

        XML

        <add key="QueueDatabasePath" value="D:\Queue\QueueDB" />
        <add key="QueueDatabaseLoggingPath" value="D:\Queue\QueueDB" />

     When you're finished, save and close the EdgeTransport.exe.config file.

   4. Restart the Exchange Transport service by running the following command:

        Console

        net stop MSExchangeTransport && net start MSExchangeTransport

How do you know you successfully created a new queue
database and new transaction logs in the new location?
To verify you successfully created a new queue database and new transaction logs in the new
location, do these steps:

   1. Verify the new database files Mail.que and Trn.chk exist at the new location.

   2. Verify the new transaction log files Trn.log , Trntmp.log , Trnres00001.jrs ,
     Trnres00002.jrs , and Temp.edb files exist at the new location.

   3. If you can delete the old queue database and transaction log files from the old location
     after the Exchange Transport service starts, the old queue database is no longer being

<!-- p.1829 -->

     used.

Use the Command Prompt to move the existing
queue database and transaction logs to a new
location

  ７ Note

  There's also a script named Move-TransportDatabase.ps1 in the
  %ExchangeInstallPath%Scripts folder to move the queue database and transaction logs.

  You need to specify the following parameters: queueDatabasePath,
  queueDatabaseLoggingPath, iPFilterDatabasePath, iPFilterDatabaseLoggingPath, and
  temporaryStoragePath.

Although you need to move the existing queue database to preserve any undelivered
messages in it, you typically don't need to move the existing transaction logs because:

     An ordinary shutdown of the Exchange Transport service writes all uncommitted
     transaction log entries to the queue database.

     Circular logging is used, so transaction logs that contain previously committed database
     changes aren't preserved.

   1. Create the folder where you want to keep the queue database and transaction logs. Make
     sure that the correct permissions are applied to the folder.

   2. In a Command prompt window, open the EdgeTransport.exe.config file in Notepad by
     running the following command:

       Console

        Notepad %ExchangeInstallPath%Bin\EdgeTransport.exe.config

   3. Find and modify the following keys in the <appSettings> section:

       XML

        <add key="QueueDatabasePath" value="<LocalPath>" />
        <add key="QueueDatabaseLoggingPath" value="<LocalPath>" />

<!-- p.1830 -->

     For example, to change the location of the queue database and transaction logs to
     D:\Queue\QueueDB, use the following values:

        XML

        <add key="QueueDatabasePath" value="D:\Queue\QueueDB" />
        <add key="QueueDatabaseLoggingPath" value="D:\Queue\QueueDB" />

     When you're finished, save and close the EdgeTransport.exe.config file.

   4. Stop the Exchange Transport service by running the following command:

        Console

        net stop MSExchangeTransport

   5. Move the existing database files Mail.que and Trn.chk from the old location to the new
     location.

   6. Move the existing transaction log files Trn.log , Trntmp.log , Trn nnnnn.log ,
     Trnres00001.jrs , Trnres00002.jrs , and Temp.edb from the old location to the new

     location.

   7. Start the Exchange Transport service by running the following command:

        Console

        net start MSExchangeTransport

How do you know you successfully moved the existing queue
database and transaction logs to the new location?
To verify you successfully moved the existing queue database and transaction logs to the new
location, do these steps:

   1. Verify the queue database files Mail.que and Trn.chk exist in the new location.

   2. Verify the transaction log files Trn.log , Trntmp.log , Trnres00001.jrs , Trnres00002.jrs ,
     and Temp.edb files exist in the new location.

   3. Verify there are no queue database or transaction log files in the old location.

<!-- p.1831 -->

Message retry, resubmit, and expiration
intervals in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

In Exchange Server, messages that can't be successfully delivered are subject to various retry,
resubmit, and expiration deadlines based on the message's source and destination. Retry is a
renewed connection attempt with the destination. Resubmit is the act of sending messages
back to the Submission queue for the categorizer to reprocess. The message expires after all
delivery efforts have failed over a specified period of time. After a message expires, the sender
is notified of the delivery failure, and the message is deleted from the queue.

In all three cases of retry, resubmit, or expire, you can manually intervene before the automatic
actions are performed on the messages.

For instructions on how to configure these intervals, see Configure message retry, resubmit,
and expiration intervals.

Configuration options for message retry
When a the Transport service on a Mailbox server or an Edge Transport server can't connect to
the next hop, the queue is put in a status of Retry. Connection attempts continue until the
queue expires or a connection is made.

Configuration options for automatic message retry in the
EdgeTransport.exe.config file
The automatic message retry interval settings that are available in the
%ExchangeInstallPath%Bin\EdgeTransport.exe.config XML application configuration file are

described in the following table.

  ７ Note

  Any customized Exchange or Internet Information Server (IIS) settings that you made in
  Exchange XML application configuration files on the Exchange server (for example,
  web.config files or the EdgeTransport.exe.config file) will be overwritten when you install
  an Exchange CU. Be sure save this information so you can easily re-apply the settings after
  the install. After you install the Exchange CU, you need to re-configure these settings.

<!-- p.1832 -->

                                                                                        ﾉ   Expand table

 Automatic message retry key         Default      Description
 name                                value

 MailboxDeliveryQueueRetryInterval   00:05:00     How frequently the queues try to connect to the
                                     (5           Mailbox Transport Delivery service for a destination
                                     minutes)     mailbox database that can't be successfully reached.
                                                  To specify a value, enter it as a time span: dd.hh:mm:ss
                                                  where dd = days, hh = hours, mm = minutes, and ss
                                                  = seconds.

                                                  A valid value is a timespan from 00:00:01 (one
                                                  second) through 1.00:00:00 (one day).

 QueueGlitchRetryCount               4            The number of connection attempts that are
                                                  immediately tried when a transport server has trouble
                                                  connecting with the destination server. Such
                                                  connection problems are typically caused by very brief
                                                  network outages.
                                                  A valid value is an integer from 0 through 15.

                                                  Typically, you don't need to modify this key unless the
                                                  network is unreliable and continues to experience
                                                  many accidentally dropped connections.

 QueueGlitchRetryInterval            00:01:00     The connection interval between each connection
                                     (1 minute)   attempt that's specified by the QueueGlitchRetryCount
                                                  key.

                                                  Typically, you don't need to modify this parameter
                                                  unless the network is unreliable and continues to
                                                  experience many accidentally dropped connections.

Configuration options for automatic message retry in the
Exchange admin center and the Exchange Management Shell
The automatic message retry interval settings that are available in the Exchange admin center
(EAC) and the Exchange Management Shell are described in the following table.

                                                                                        ﾉ   Expand table

<!-- p.1833 -->

Automatic             Default value          Exchange Management Shell                Exchange admin
message retry                                configuration                            center
setting                                                                               configuration on
                                                                                      Mailbox servers

Message retry         15 minutes             Cmdlet: Set-TransportService cmdlet      n/a
interval: The retry   ( 00:15:00 )
interval for                                 Parameter: MessageRetryInterval
individual            We recommend that
messages that         you don't modify
have a status of      the default value
Retry.                unless you're
                      directed to do so by
                      Microsoft Customer
                      Service and Support,
                      or specific product
                      documentation.

Outbound              Transport service on   Cmdlet: Set-TransportService             Servers > select
connection failure    Mailbox servers: 10                                             server > Edit (     )
retry interval: The   minutes ( 00:10:00 )   Parameter:                               > Transport
retry interval for                           OutboundConnectionFailureRetryInterval   limits > Retry
outbound              Edge Transport                                                  section >
connection            Servers: 30 minutes                                             Outbound
attempts that         ( 00:30:00 )                                                    connection
have previously                                                                       failure retry
failed. The                                                                           interval (seconds)
previously failed
connection
attempts are
controlled by the
transient failure
retry count and
interval values.

Transient failure     6                      Cmdlet: Set-TransportService             Servers > select
retry count: The                                                                      server > Edit ( )
number of                                    Parameter: TransientFailureRetryCount    > Transport
connection                                                                            limits > Retries
attempts that are                                                                     section >
tried after the                                                                       Transient failure
queue glitch retry                                                                    retry attempts
count and interval
values have failed.
These failures can
be caused by
server restarts or
cached DNS
lookup failures.

<!-- p.1834 -->

 Automatic             Default value          Exchange Management Shell                  Exchange admin
 message retry                                configuration                              center
 setting                                                                                 configuration on
                                                                                         Mailbox servers

 A valid value is an
 integer from 0
 through 15. The
 value 0 means the
 next connection
 attempt is
 controlled by the
 outbound
 connection failure
 retry interval.

 Transient failure     Transport service on   Cmdlet: Set-TransportService               Servers > select
 retry interval: The   Mailbox servers: 5                                                server > Edit ( )
 connection            minutes ( 00:05:00 )   Parameter: TransientFailureRetryInterval   > Transport
 interval between                                                                        limits > Retries
 each connection       Edge Transport                                                    section >
 attempt that's        servers: 10 minutes                                               Transient failure
 specified by the      ( 00:10:00 )                                                      retry interval
 transient failure                                                                       (minutes)
 retry count value.

Configuration options for manual message retry
When a delivery queue is in the status of Retry, you can manually force an immediate
connection attempt by using Queue Viewer in the Exchange Toolbox or the Retry-Queue
cmdlet in the Exchange Management Shell. The manual retry attempt overrides the next
scheduled retry time. If the connection isn't successful, the retry interval timer is reset. The
delivery queue must be in a status of Retry for this action to have any effect. For more
information, see Retry queues.

Configuration options for delay DSN messages
After each message delivery failure, the Transport service on the Edge Transport server or the
Mailbox server generates a delay delivery status notification (DSN) message and queues it for
delivery to the sender of the undeliverable message. This delay DSN message is sent only after
a delay notification interval has passed (the default is 4 hours), and only if the message wasn't
successfully delivered during that time. This delay prevents the sending of unnecessary delay
DSN messages due to temporary message transmission failures that are ultimately resolved.
You can selectively enable or disable the sending of delay DSN notification messages for
messages that originate inside or outside the Exchange organization.

<!-- p.1835 -->

The configuration options that are available for delay DSN notification messages are described
in the following table.

                                                                                          ﾉ   Expand table

 Delay DSN setting                           Default       Exchange Management        Exchange admin
                                             value         Shell configuration        center configuration
                                                                                      on Mailbox servers

 Delay notification timeout: How long        4 hours       Cmdlet: Set-               Servers > select
 the server waits before it sends a          ( 4:00:00 )   TransportService           server > Edit ( ) >
 delay DSN message to the sender.                                                     Transport limits >
                                                           Parameter:                 Notifications section
 This value should always be greater                       DelayNotificationTimeOut   > Notify sender when
 than the transient failure retry count                                               message is delayed
 multiplied by the transient failure retry                                            after (hours)
 interval (the default total is 30
 minutes on a Mailbox server, and one
 hour on an Edge Transport server).

 External delay DSN enabled: Specifies       $true         Cmdlet: Set-               Not available
 whether delay DSN messages can be                         TransportConfig
 sent to external message senders
 (senders who are outside the                              Parameter:
 Exchange organization).                                   ExternalDelayDSNEnabled

 ExternalDelayDSNEnabled

 Internal delay DSN enabled: Specifies       $true         Cmdlet: Set-               Not available
 whether delay DSN messages can be                         TransportConfig
 sent to internal message senders
 (message senders who are inside the                       Parameter:
 Exchange organization).                                   InternalDelayDSNEnabled

Configuration options for message resubmission
Message resubmission sends undelivered messages back to the Submission queue to be
reprocessed by the categorizer. For more information about the categorizer and the
Submission queue, see Understanding the Transport service on Mailbox servers.

Automatic message resubmission
Undelivered messages in delivery queues are automatically resubmitted if the delivery queue is
in the status of Retry and has been unable to successfully deliver any messages for a specified
period of time. That period of time is controlled by the MaxIdleTimeBeforeResubmit key in the

<!-- p.1836 -->

%ExchangeInstallPath%Bin\EdgeTransport.exe.config XML application configuration file. The

default value is 12:00:00 or 12 hours.

  ７ Note

  Any customized Exchange or Internet Information Server (IIS) settings that you made in
  Exchange XML application configuration files on the Exchange server (for example,
  web.config files or the EdgeTransport.exe.config file) will be overwritten when you install
  an Exchange CU. Be sure save this information so you can easily re-apply the settings after
  the install. After you install the Exchange CU, you need to re-configure these settings.

Manual Message Resubmission
You can manually resubmit messages by using the following methods:

     Resubmit a delivery queue that has the status of Retry, or resubmit the Unreachable
     queue. For more information, see Resubmit queues.
     Resubmit messages in the poison message queue. For more information, see Resubmit
     messages in the poison message queue.
     Suspend a queue, suspend the messages in the queue, export the messages to files, and
     copy the files to the Replay directory on any Mailbox server or Edge Transport server. For
     more information, see Export messages from queues.

Configuration options for message expiration
The message expiration timeout interval specifies the maximum length of time that an Edge
Transport server or Mailbox server (the Transport service) tries to deliver a failed message. If the
message can't be successfully delivered before the expiration timeout interval has passed, a
non-delivery report (also known as an NDR or bounce message) that contains the original
message or the message headers is delivered to the sender.

Automatic message expiration
The message expiration timeout interval is described in the following table.

                                                                                  ﾉ   Expand table

<!-- p.1837 -->

 Default value    Exchange Management Shell      Exchange admin center configuration on
                  configuration                  Mailbox servers

 2 days           Cmdlet: Set-TransportService   Servers > select server > Edit ( ) > Transport
 ( 2.00:00:00 )                                  limits > Message expiration section > Maximum
                  Parameter:                     time since submission (days)
                  MessageExpirationTimeOut

Manual Message Expiration
Although you can't manually force messages to expire, you can manually remove messages
from any queue (except the Submission queue) with or without an NDR. For more information,
see Remove messages from queues.

<!-- p.1838 -->

Configure message retry, resubmit, and
expiration intervals in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

In Exchange Server, you can configure message retry, resubmit, and expiration intervals in the
Transport service on Mailbox servers and Edge Transport servers. For detailed descriptions of
these settings, see Message retry, resubmit, and expiration intervals.

What do you need to know before you begin?
      Estimated time to complete each procedure: less than 5 minutes

      You can only use the Exchange admin center (EAC) on Mailbox servers. For more
      information about the EAC, see Exchange admin center in Exchange Server. To learn how
      to open the Exchange Management Shell in your on-premises Exchange organization, see
      Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Transport service" and "Edge
      Transport severs" entries in the Mail flow permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online         , or Exchange Online Protection .

Use EdgeTransport.exe.config to configure the
queue glitch retry count, the queue glitch retry
interval, the mailbox delivery queue retry interval,
and the maximum idle time before resubmit
interval

<!-- p.1839 -->

     Queue glitch retry count: The number of connection attempts that are immediately tried
     when the Transport service has trouble connecting to the destination server. Typically, you
     don't need to modify this key unless the network is unreliable and continues to
     experience many accidentally dropped connections.

     Queue glitch retry interval: The interval between each queue glitch retry. Typically, you
     don't need to modify this key unless the network is unreliable and continues to
     experience many accidentally dropped connections.

     Mailbox delivery queue retry interval: How frequently a queue try to connect to the
     Mailbox Transport Delivery service for a destination mailbox database that can't be
     successfully reached.

     Max idle time before resubmit: How long undelivered messages in delivery queues the
     status of Retry wait before they're resubmitted.

To configure these intervals, you modify keys in the
%ExchangeInstallPath%Bin\EdgeTransport.exe.config XML application configuration file on
Mailbox servers or Edge Transport servers. Changes you save to this file are applied after you
restart the Exchange Transport service. When you restart this service, mail flow on the server is
temporarily interrupted.

  ７ Note

  Any customized Exchange or Internet Information Server (IIS) settings that you made in
  Exchange XML application configuration files on the Exchange server (for example,
  web.config files or the EdgeTransport.exe.config file) will be overwritten when you install
  an Exchange CU. Be sure save this information so you can easily re-apply the settings after
  the install. After you install the Exchange CU, you need to re-configure these settings.

   1. In a Command prompt window on the Mailbox server or Edge Transport server, open the
     EdgeTransport.exe.config file in Notepad by running this command:

        Console

        Notepad %ExchangeInstallPath%Bin\EdgeTransport.exe.config

   2. Locate the following keys in the <appSettings> section.

        XML

        <add key="QueueGlitchRetryCount" value="<Integer>" />
        <add key="QueueGlitchRetryInterval" value="<hh:mm:ss>" />

<!-- p.1840 -->

        <add key="MailboxDeliveryQueueRetryInterval" value="<hh:mm:ss>" />
        <add key="MaxIdleTimeBeforeResubmit" value="<hh:mm:ss>" />

     This example changes the queue glitch retry count to 6, the queue glitch retry interval to
     30 seconds, the mailbox delivery queue retry interval to 3 minutes, and the maximum idle
     time before resubmit interval to 6 hours.

        XML

        <add key="QueueGlitchRetryCount" value="6" />
        <add key="QueueGlitchRetryInterval" value="00:00:30" />
        <add key="MailboxDeliveryQueueRetryInterval" value="00:03:00" />
        <add key="MaxIdleTimeBeforeResubmit" value="6:00:00" />

   3. When you're finished, save and close the EdgeTransport.exe.config file.

   4. Restart the Exchange Transport service by running this command:

        Console

        net stop MSExchangeTransport && net start MSExchangeTransport

How do you know this worked?
To verify that you've configured these intervals, do these steps:

   1. Open the EdgeTransport.exe.config file in Notepad by running this command:

        Console

        Notepad %ExchangeInstallPath%Bin\EdgeTransport.exe.config

   2. Verify the values of the following keys in the <appSettings> section.

        XML

        <add key="QueueGlitchRetryCount" value="<Integer>" />
        <add key="QueueGlitchRetryInterval" value="<hh:mm:ss>" />
        <add key="MailboxDeliveryQueueRetryInterval" value="<hh:mm:ss>" />
        <add key="MaxIdleTimeBeforeResubmit" value="<hh:mm:ss>" />
