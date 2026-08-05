---
title: "Exchange Server — pages 1761-1800"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1761-1800
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1761-1800
family: exchange
documentKind: "doc"
abstract: "Delivery Type in Queue DeliveryType in the Exchange Description NextHopCategory NextHopDomain Viewer Management Shell later mailbox recipients. The destination mailbox database is in one of the following locations: The local Exchange 2013 or later Mailbox server. An Exchange 201"
---

# Exchange Server — pages 1761-1800

<!-- p.1761 -->

Delivery Type in Queue     DeliveryType in the Exchange        Description             NextHopCategory   NextHopDomain
Viewer                     Management Shell

                                                               later mailbox
                                                               recipients. The
                                                               destination mailbox
                                                               database is in one
                                                               of the following
                                                               locations:
                                                                     The local
                                                                     Exchange
                                                                     2013 or later
                                                                     Mailbox
                                                                     server.
                                                                     An Exchange
                                                                     2019 Mailbox
                                                                     server in the
                                                                     same
                                                                     Exchange
                                                                     2019 DAG.
                                                                     An Exchange
                                                                     2016 Mailbox
                                                                     server in the
                                                                     same
                                                                     Exchange
                                                                     2016 DAG.
                                                                     An Exchange
                                                                     2013 Mailbox
                                                                     server in the
                                                                     same
                                                                     Exchange
                                                                     2013 DAG.
                                                                     An Exchange
                                                                     2013 or later
                                                                     Mailbox
                                                                     server in the
                                                                     same Active
                                                                     Directory site
                                                                     in non-DAG
                                                                     environments.

SMTP Relay to Send         SmtpRelayToConnectorSourceServers   The queue holds         Internal          This value is the name of the destination Send
Connector Source Servers                                       messages for                              connector, Delivery Agent connector, or Foreign
                                                               delivery to an SMTP                       connector. For example, Contoso.com Send
                                                               or non-SMTP                               Connector .
                                                               address space that's
                                                               serviced by a Send
                                                               connector, Delivery
                                                               Agent connector, or
                                                               Foreign connector.
                                                               The connector has a
                                                               remote transport
                                                               server configured as
                                                               a source server.
                                                               The remote
                                                               transport server
                                                               could be an
                                                               Exchange 2013 or
                                                               later Mailbox server
                                                               or an Exchange
                                                               2010 Hub Transport
                                                               server.

                                                               The remote
                                                               transport server
                                                               could be located in
                                                               the local Active
                                                               Directory site, or in
                                                               a remote Active
                                                               Directory site.

SMTP Relay to Database     SmtpRelayToDag                      The queue holds         Internal          This value is the name of the destination DAG. For
Availability Group                                             messages for                              example, DAG1 .
                                                               delivery to

<!-- p.1762 -->

Delivery Type in Queue    DeliveryType in the Exchange           Description             NextHopCategory   NextHopDomain
Viewer                    Management Shell

                                                                 Exchange 2013 or
                                                                 later mailbox
                                                                 recipients, where
                                                                 the destination
                                                                 mailbox database is
                                                                 located in a remote
                                                                 DAG.
                                                                 The remote DAG
                                                                 could be located in
                                                                 the local Active
                                                                 Directory site, or in
                                                                 a remote Active
                                                                 Directory site.

SMTP Relay to Mailbox     SmtpRelayToMailboxDeliveryGroup        The queue holds         Internal          The queue name uses the syntax: Site:
Delivery Group                                                   messages for                              <ADSiteName>;Version:<ExchangeVersion> , where
                                                                 delivery to legacy                        <ADSiteName> is the name of the destination
                                                                 mailbox recipients,                       Active Directory site, and <ExchangeVersion> is the
                                                                 where the                                 version of Exchange 2010 on the Mailbox server.
                                                                 destination mailbox
                                                                 is on an Exchange
                                                                 2010 Mailbox
                                                                 server. The message
                                                                 is related to an
                                                                 Exchange 2010 Hub
                                                                 Transport server.
                                                                 The destination
                                                                 Exchange 2010 Hub
                                                                 Transport server
                                                                 could be in the local
                                                                 Active Directory
                                                                 site, or a remote
                                                                 Active Directory
                                                                 site.

SMTP Relay to Remote      SmtpRelayToRemoteActiveDirectorySite   The queue holds         Internal          This value is the target Active Directory site name.
Active Directory Site                                            messages for                              For example, NorthAmericaSite .
                                                                 delivery to a remote
                                                                 destination, and the
                                                                 routing topology
                                                                 requires the
                                                                 message to be
                                                                 routed through a
                                                                 specific Active
                                                                 Directory site. The
                                                                 site is an
                                                                 intermediate hop
                                                                 on the way to the
                                                                 final destination.
                                                                 This situation
                                                                 occurs under the
                                                                 following
                                                                 circumstances:
                                                                 The message needs
                                                                 to be routed
                                                                 through a hub site.

                                                                 The message
                                                                 requires delivery
                                                                 through a Send
                                                                 connector that's
                                                                 configured on an
                                                                 Edge Transport
                                                                 server that's
                                                                 subscribed to a
                                                                 remote Active
                                                                 Directory site.

SMTP Relay to specified   SmtpRelayToRemoteForest                This value isn't used   n/a               n/a
remote forest                                                    in on-premises
                                                                 Exchange

<!-- p.1763 -->

Delivery Type in Queue    DeliveryType in the Exchange   Description            NextHopCategory   NextHopDomain
Viewer                    Management Shell

SMTP Relay to Specified   SmtpRelayToServers             The queue holds        Internal          This value is the FQDN of the target expansion
Exchange Servers                                         messages for                             server. For example, mailbox01.contoso.com .
                                                         delivery to a
                                                         distribution group
                                                         that's configured
                                                         for a specific
                                                         expansion server.
                                                         The expansion
                                                         server could be an
                                                         Exchange 2013 or
                                                         later Mailbox server
                                                         or an Exchange
                                                         2010 Hub Transport
                                                         server.
                                                         The expansion
                                                         server could be
                                                         located in the local
                                                         Active Directory
                                                         site, or in a remote
                                                         Active Directory
                                                         site.

SmtpRelayToTiRg           SmtpRelayToTiRg                Note: This value       n/a               n/a
                                                         isn't used by
                                                         Exchange 2013 or
                                                         later. It's included
                                                         for backwards
                                                         compatibility with
                                                         Exchange 2010.

                                                         The queue holds
                                                         messages for
                                                         delivery by an
                                                         Exchange 2010 Hub
                                                         Transport server to
                                                         an Exchange 2003
                                                         routing group.

Smtp Relay in Active      SmtpRelayWithinAdSite          Note: This value       n/a               n/a
Directory Site                                           isn't used by
                                                         Exchange 2013 or
                                                         later. It's included
                                                         for backwards
                                                         compatibility with
                                                         Exchange 2010.

                                                         The queue holds
                                                         messages for
                                                         delivery by an
                                                         Exchange 2010 Hub
                                                         Transport server to
                                                         another Hub
                                                         Transport server in
                                                         the same Active
                                                         Directory site.

SMTP Relay in Active      SmtpRelayWithinAdSiteToEdge    The queue holds        Internal          This value is the name of the Send connector that
Directory Site to Edge                                   messages for                             sends outbound Internet mail from the Edge
Transport Server                                         delivery to an                           Transport server to the Internet. This Send
                                                         external SMTP                            connector is automatically created by the Edge
                                                         domain that's                            subscription, and is named EdgeSync -
                                                         serviced by a Send                       <ADSiteName> to Internet.
                                                         connector that's
                                                         configured on an
                                                         Edge Transport
                                                         server. The Edge
                                                         Transport server is
                                                         subscribed to the
                                                         local Active
                                                         Directory site.

<!-- p.1764 -->

 Delivery Type in Queue            DeliveryType in the Exchange              Description            NextHopCategory          NextHopDomain
 Viewer                            Management Shell

 Undefined                         Undefined                                 This value is used     Internal                 For the Submission queue, this value is
                                                                             only on the                                     Submisssion . For the poison message queue, this
                                                                             Submission queue                                value is Poison Message .
                                                                             and the poison
                                                                             message queue.

 Unreachable                       Unreachable                               This value is used     Internal                 This value is Unreachable Domain .
                                                                             only on the
                                                                             Unreachable queue.

IncomingRate, OutgoingRate, and Velocity
Exchange measures the rate of messages entering and leaving a queue and stores these values in queue properties. You can use these rates as an
indicator of queue and transport server health. The properties are described in the following table:

                                                                                                                                                         ﾉ   Expand table

 Property          Description

 IncomingRate      The rate that messages are entering the queue. The rate is the number of messages per second averaged over the last minute.

 OutgoingRate      The rate that messages are leaving the queue. The rate is the number of messages per second averaged over the last minute.

 Velocity          The drain rate of the queue, calculated by subtracting the value of IncomingRate from the value of OutgoingRate.

                   If the value is greater than 0, messages are leaving the queue faster than they are entering the queue.

                   If the value equals 0, messages are leaving the queue as fast as they are entering the queue. This is also the value you'll see when the queue is
                   inactive.

                   If the value is less than 0, messages are entering the queue faster than they are leaving the queue.

                   The Velocity value is displayed in the results of Get-Queue.

At a basic level, a positive value of Velocity indicates a healthy queue that's efficiently draining, and a negative value of Velocity indicates a queue
that isn't efficiently draining. However, you also need to consider the values of IncomingRate, OutgoingRate, and MessageCount, as well as the
magnitude of Velocity.

For example, consider a queue that has the following property values.

     Velocity: -50
     MessageCount: 1000
     OutgoingRate: 10
     IncomingRate: 60

Based on the property values for this queue, the negative value for Velocity clearly indicates that the queue isn't draining properly.

Now consider a queue that has the following property values.

     Velocity: -0.85
     MessageCount: 2
     OutgoingRate: 0.15
     IncomingRate: 1

Although the value for Velocity is negative, it's very close to zero, and the values of the other properties are also very small. Therefore, a negative
Velocity value for this queue doesn't indicate a problem with the queue.

Queue status
The current status of a queue is stored in the Status property of the queue. A queue can have one of the status values that's described in the
following table:

                                                                                                                                                         ﾉ   Expand table

<!-- p.1765 -->

 Queue         Description
 status

 Active        The queue is actively transmitting messages.

 Connecting    The queue is in the process of connecting to the next hop.

 Ready         The queue recently transmitted messages, but the queue is now empty.

 Retry         The last automatic or manual connection attempt failed, and the queue is waiting to retry the connection.

 Suspended     The queue has been manually suspended by an administrator to prevent message delivery. New messages can enter the queue, and messages that
               are in the act of being transmitted to the next hop will finish delivery and leave the queue. Otherwise, messages won't leave the queue until the
               queue is manually resumed by an administrator.
               Notes:

               You can suspend the following queues:

                       Delivery queues that have any status.
                       The Unreachable queue. When you suspend this queue, messages are no longer automatically resubmitted to the categorizer when
                       configuration updates are detected. To automatically resubmit these messages, you need to manually resume the queue.
                       The Submission queue. When you suspend this queue, messages aren't picked up by the categorizer until the queue is resumed.

               Suspending a queue doesn't change the status of the messages in the queue.

Other queue properties
There are other queue properties that are self-explanatory. You can use most of the queue properties as filter options. By specifying filter criteria,
you can quickly locate queues and take action on them. For a complete description of the filterable queue properties, see Queue properties.

An important queue property that's also worth mentioning here is the MessageCount property that shows how many messages are in a queue.
This property is an important indicator of queue health. For example, a delivery queue that contains a large number of messages that continues to
grow and never decreases could indicate a routing or transport pipeline issue that requires your attention.

Message properties
A message in a queue has many properties. Many of the properties reflect the information that was used to create the message. Some of the
messages status and information properties are heavily influenced by corresponding properties on the queue. However, an individual message
may have a different value than the corresponding property of the queue. Other properties contain status, time, or other indicators that are
updated frequently.

Message status
The current status of a message is stored in the Status property of the message. A message can have one of the status values that's described in
the following table:

                                                                                                                                                    ﾉ   Expand table

 Message status    Description

 Active            If the message is in a delivery queue, the message is being delivered to its destination. If the message is in the Submission queue, the message is
                   being processed by the categorizer.

 Locked            This value is reserved for internal Microsoft use, and isn't used in on-premises Exchange organizations.

 PendingRemove     The message was deleted by the administrator, but the message was already in the act of being transmitted to the next hop. The message will be
                   deleted if the delivery ends in an error that causes the message to reenter the queue. Otherwise, delivery will continue.

 PendingSuspend    The message was suspended by the administrator, but the message was already in the act of being transmitted to the next hop. The message will
                   be suspended if the delivery ends in an error that causes the message to reenter the queue. Otherwise, delivery will continue.

 Ready             The message is waiting in the queue and is ready to be processed.

 Retry             The last automatic or manual connection attempt fail for the queue that holds the message. The message is waiting for the next automatic
                   queue connection retry.

 Suspended         The message was manually suspended by an administrator.
                   Any messages in the poison message queue are in a permanently suspended state.

<!-- p.1766 -->

Other message properties
There are other message properties that are self-explanatory. You can use most of the message properties as filter options. By specifying filter
criteria, you can quickly locate messages and take action on them. For a complete description of the filterable message properties, see Properties
of messages in queues.

Manage queues and messages in queues
Queue Viewer and the historical queue and message management cmdlets in the Exchange Management Shell are restricted to a single Exchange
server. You can view or operate on individual queues or messages, or multiple queues or messages, but only on a specific server.

The Get-QueueDigest cmdlet was introduced in Exchange 2013 to provide a high-level, aggregate view of the state of queues on all servers within
a specific scope. The scope could be a DAG, an Active Directory site, a list of servers, or the entire Active Directory forest. Note that queues on a
subscribed Edge Transport server in the perimeter network aren't included in the results. Also, Get-QueueDigest is available on Edge Transport
servers, but the results are restricted to queues on the Edge Transport server.

  ７ Note

  By default, the Get-QueueDigest cmdlet displays delivery queues that contain ten or more messages, and the results are between one and
  two minutes old. For instructions on how to change these default values, see Configure Get-QueueDigest.

The following table describes the management tasks you can perform on queues or messages in queues.

                                                                                                                                                 ﾉ   Expand table

 Task                           Description                                                      Tool to use                                     Instructions

 View and filter queues on a    Displays one or more queues on a transport server. You can use   Queue Viewer or the Get-Queue cmdlet.           Procedures for
 server                         the results to take action on the queues.                                                                        queues

 View and filter queues on      Displays a summary list of queues.                               Get-QueueDigest cmdlet                          Procedures for
 specific servers in specific                                                                                                                    queues
 DAGs, specific Active
 Directory sites, or in the
 whole Active Directory
 forest.

 Suspend queues                 Temporarily prevent delivery of messages that are currently in   Queue Viewer or the Suspend-Queue cmdlet.       Procedures for
                                the queue. The queue continues to accept new messages, but                                                       queues
                                no messages leave the queue.

 Resume queues                  Reverses the effect of the suspend queue action, and enables     Queue Viewer or the Resume-Queue cmdlet.        Procedures for
                                delivery of queued messages to resume.                                                                           queues

 Retry queues                   Immediately tries to connect to the next hop. Without manual     Queue Viewer or the Retry-Queue cmdlet.         Procedures for
                                intervention, when the connection to the next hop fails, the                                                     queues
                                connection is attempted a specific number of times after a
                                specific time interval between each attempt.
                                Whether the connection attempt is manual or automatic, any
                                connection attempt resets the next retry time. For more
                                information, see Message retry, resubmit, and expiration
                                intervals.

 Resubmit messages in           Causes messages in the queue to be resubmitted to the            Retry-Queue with the Resubmit parameter         Procedures for
 queues                         Submission queue and to go back through the categorization                                                       queues
                                process.                                                         Note that you can use Queue Viewer to
                                                                                                 resubmit messages, but only from the poison
                                                                                                 message queue. To resubmit a poison message,
                                                                                                 you first need to resume the message in Queue
                                                                                                 Viewer, or by using the Resume-Message
                                                                                                 cmdlet.

 Suspend messages in            Temporarily prevents delivery of a message. You can use the      Queue Viewer or the Suspend-Message             Procedures for
 queues                         suspend message action to prevent delivery of a message to all   cmdlet.                                         messages in
                                the recipients in a specific queue or to all recipients in all                                                   queues
                                queues.

 Resume messages in             Reverses the effect of the suspend message action, and enables   Queue Viewer or the Resume-Message cmdlet.      Procedures for
 queues                         the delivery of queued messages to resume. You can resume the                                                    messages in
                                                                                                                                                 queues

<!-- p.1767 -->

Task                   Description                                                          Tool to use                                  Instructions

                       delivery of a message to all recipients in a specific queue, or to
                       all recipients in all queues.

Remove messages from   Permanently prevents the delivery of a message. You can              Queue Viewer or the Remove-Message cmdlet.   Procedures for
queues                 prevent the delivery of a message to any recipients in a specific                                                 messages in
                       queue, or to all recipients in all queues. Optionally, you can                                                    queues
                       send a non-delivery report (also known as an NDR, delivery
                       status notification, DSN or bounce message) to the sender when
                       the message is removed.

Export messages from   Copies a message to the location that you specify. The               Export-Message cmdlet only.                  Export
queues                 messages aren't deleted from the queue, but a copy of the                                                         messages from
                       message is saved as a file in the specified location. This enables                                                queues
                       administrators or officials in an organization to later examine
                       the messages. Before you export a message, you need to
                       temporarily suspend the message.

<!-- p.1768 -->

Procedures for queues
Article • 04/30/2025

APPLIES TO:        2016      2019     Subscription Edition

In Exchange Server, you can use the Queue Viewer in the Exchange Toolbox or the Exchange
Management Shell to manage queues. For more information about queues, see Queues and
messages in queues.

This topic describes how to perform the following procedures on queues:

      View queues
      Retry queues: When an Exchange server can't connect to the next hop, the queue is put
      into a status of Retry, and the server periodically tries to connect and deliver the
      messages. When you manually retry a queue, you override the scheduled retry time by
      forcing an immediate connection attempt.
      Resubmit queues: Resubmitting a queue is similar to retrying a queue, except the
      messages are sent back to the Submission queue for the categorizer to process, instead
      of immediately trying to connect to the next hop. This is useful if changes to your
      network infrastructure are preventing the messages in the queue from being delivered.
      Suspend queues: New messages can enter the queue, and messages that are in the act of
      being transmitted to the next hop will leave the queue, but otherwise, messages won't
      leave the queue until the queue is manually resumed.
      Resume queues: Restart outgoing message delivery for a queue that has a status of
      Suspended. When you resume a queue, the status of messages in the queue doesn't
      change (for example, messages that have a status of Suspended remain suspended and
      won't leave the queue).

For procedures on messages in queues, see Procedures for messages in queues.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes

      To find and open the Exchange Toolbox, use one of the following procedures:

         Windows 10: Click Start > All Apps > Microsoft Exchange Server <Version> >
         Exchange Toolbox.

         Windows Server 2012 R2 or Windows 8.1: On the Start screen, open the Apps view by
         clicking the down arrow near the lower-left corner or swiping up from the middle of
         the screen. The Exchange Toolbox shortcut is in a group named Microsoft Exchange
         Server <Version>.

<!-- p.1769 -->

      Windows Server 2012: Use any of the following methods:
         On the Start screen, click an empty area, and type Exchange Toolbox.
         On the desktop or the Start screen, press Windows key + Q. In the Search charm,
         type Exchange Toolbox.
         On the desktop or the Start screen, move your cursor to the upper-right corner, or
         swipe left from the right edge of the screen to show the charms. Click the Search
         charm, and type Exchange Toolbox.

      When the shortcut appears in the results, you can select it.

   To learn how to open the Exchange Management Shell in your on-premises Exchange
   organization, see Open the Exchange Management Shell.

   For more information about using filters and identity values in the Exchange Management
   Shell, see Find queues and messages in queues in the Exchange Management Shell.

   You need to be assigned permissions before you can perform this procedure or
   procedures. To see what permissions you need, see the "Queues" entry in the Mail flow
   permissions topic.

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online     , or Exchange Online Protection .

View queues

Use Queue Viewer to view queues
 1. In the Exchange Toolbox, in the Mail flow tools section, double-click Queue Viewer to
   open the tool in a new window.
 2. In Queue Viewer, click the Queues tab. A list of all queues on the server to which you're
   connected is displayed.
 3. You can use the Export List link in the action pane to export the list of queues. For more
   information, see How to Export Lists from the Exchange Management Consoles.

Use the Exchange Management Shell to view queues

<!-- p.1770 -->

To view queues, use the following syntax.

  PowerShell

  Get-Queue [-Filter <Filter> -Server <ServerIdentity> -Include <Internal | External
  | Empty | DeliveryType> -Exclude <Internal | External | Empty | DeliveryType>]

This example displays basic information about all non-empty queues on the server named
Mailbox01.

  PowerShell

  Get-Queue -Server Mailbox01 -Exclude Empty

This example displays detailed information for all queues on the local Exchange server that
contain more than 100 messages.

  PowerShell

  Get-Queue -Filter "MessageCount -gt 100" | Format-List

For more information, see Get-Queue and Find queues and messages in queues in the
Exchange Management Shell.

Use the Exchange Management Shell to view queue summary
information on multiple Exchange servers
The Get-QueueDigest cmdlet provides a high-level, aggregate view of the state of queues on
all servers within a specific scope (for example, a DAG, an Active Directory site, a list of servers,
or the entire Active Directory forest).

By default, the Get-QueueDigest cmdlet displays delivery queues that contain ten or more
messages, and the results are between one and two minutes old. For instructions on how to
change these default values, see Configure Get-QueueDigest.

Notes:

     Queues on a subscribed Edge Transport server aren't included in the results of Get-
     QueueDigest.
     Get-QueueDigest is available on Edge Transport servers, but the results are restricted to
     local queues on the server.

<!-- p.1771 -->

To view summary information about queues on multiple Exchange servers, run the following
command:

  PowerShell

  Get-QueueDigest <-Server <ServerIdentity1,ServerIdentity2...> | -Dag
  <DagIdentity1,DagIdentity2...> | -Site <ADSiteIdentity1,ADSiteIdentity2...> | -
  Forest> [-Filter <Filter>]

This example displays summary information about the queues on all Exchange 2013 or later
Mailbox servers in the Active Directory site named FirstSite where the message count is greater
than 100.

  PowerShell

  Get-QueueDigest -Site FirstSite -Filter "MessageCount -gt 100"

This example displays summary information about the queues on all Mailbox servers in the
database availability group (DAG) named DAG01 where the queue status has the value Retry.

  PowerShell

  Get-QueueDigest -Dag DAG01 -Filter "Status -eq 'Retry'"

For more information, see Get-QueueDigest.

Retry queues
When you retry a delivery queue, you force an immediate connection attempt and override the
next scheduled retry time. For more information about the schedule retry time for queues, see
Message retry, resubmit, and expiration intervals.

Notes:

     The queue must be in a status of Retry for this action to have any effect.
     If the connection isn't successful, the retry interval timer is reset.

Use Queue Viewer to retry a queue
   1. In the Exchange Toolbox, in the Mail flow tools section, double-click Queue Viewer to
     open the tool in a new window.

<!-- p.1772 -->

   2. In Queue Viewer, click the Queues tab. A list of all queues on the server that you're
     connected to is displayed.

   3. Click Create Filter, and enter your filter expression as follows:
      a. Select Status from the queue property drop-down list.
      b. Select Equals from the comparison operator drop-down list.
      c. Select Retry from the value drop-down list.
      d. Click Apply Filter. All queues that currently have a Retry status are displayed.
      e. Select one or more queues from the list. Right-click, and then select Retry Queue. If
        the connection attempt is successful, the queue status changes to Active. If no
        connection can be made, the queue remains in a status of Retry and the next retry
        time is updated.

Use the Exchange Management Shell to retry a queue
To retry queues, use the following syntax.

  PowerShell

  Retry-Queue <-Identity QueueIdentity | -Filter QueueFilter [-Server
  ServerIdentity]>

This example retries all queues on the local server with the status of Retry.

  PowerShell

  Retry-Queue -Filter "Status -eq 'Retry'"

This example retries the queue named contoso.com on the server named Mailbox01.

  PowerShell

  Retry-Queue -Identity Mailbox01\contoso.com

How do you know this worked?
To verify that you have successfully retried a queue, use either of the following procedures:

     In Queue Viewer, verify the values of the Status, Next Retry Time, and Last Error
     properties.

     In the Exchange Management Shell, replace <QueueIdentity> with the identity of the
     queue, and use the following syntax to verify the property values:

<!-- p.1773 -->

         PowerShell

         Get-Queue -Identity <QueueIdentity> | Format-Table -Auto
         Identity,Status,LastRetryTime,NextRetryTime

Resubmit queues
Resubmitting a queue sends all messages in the queue back to the Submission queue for the
categorizer to process. For more information about the categorizer, see Mail flow and the
transport pipeline.

Notes:

     You can't use Queue Viewer to resubmit queues. You can only use the Exchange
     Management Shell.
     You can resubmit the following queues:
         A delivery queue that has the status of Retry.
         The Unreachable queue. Any messages in the queue that have the status value of
         Suspended aren't resubmitted.
     You can't resubmit the poison message queue, but you can resubmit individual messages
     in the queue. For more information, see the Resubmit messages in the poison message
     queue section later in this topic.
     Instead of resubmitting the queue, you can export the messages to .eml files and
     resubmit them by using the Replay directory on any Exchange server. For more
     information, see Export messages from queues

Use the Exchange Management Shell to resubmit queues
To resubmit queues, use the following syntax:

  PowerShell

  Retry-Queue <-Identity QueueIdentity | -Filter "Status -eq 'Retry'" -Server
  ServerIdentity> -Resubmit $true

This example resubmits all messages located in any delivery queues with the status of Retry on
the server named Mailbox01.

  PowerShell

  Retry-Queue -Filter "Status -eq 'Retry'" -Server Mailbox01 -Resubmit $true

<!-- p.1774 -->

This example resubmits all messages located in the Unreachable queue on the server
Mailbox01.

  PowerShell

  Retry-Queue -Identity Mailbox01\Unreachable -Resubmit $true

For more information, see Retry-Queue.

How do you know this worked?
To verify that you have successfully resubmitted a queue, use either of the following
procedures:

     In Queue Viewer, verify the properties of the queue.

     In the Exchange Management Shell, replace <QueueIdentity> with the identity of the
     queue, and run the following command to verify the property values:

         PowerShell

         Get-Queue -Identity <QueueIdentity>

Resubmit messages in the poison message queue
A special case for resubmitting messages is the poison message queue. You can't resubmit the
poison message queue like other queues, but you can resubmit individual messages in the
poison message queue.

Notes:

     Messages in the poison message queue might be genuinely harmful, or they might be
     valid messages that are the victims of an poorly written transport agent or a software
     bug. If you're unsure of the safety of the messages in the poison message queue, you
     should export the messages to files so you can examine them. For more information, see
     Export messages from queues.
     The procedure to resubmit messages from the poison message queue is the same as
     resuming suspended messages from other queues. You can use Queue Viewer or the
     Exchange Management Shell. For more information about resuming messages, see
     Resume messages in queues.
     The poison message queue is only visible when the queue contains messages.

<!-- p.1775 -->

Use Queue Viewer to resubmit messages in the poison message queue
   1. In the Exchange Toolbox, in the Mail flow tools section, double-click Queue Viewer to
     open the tool in a new window.
   2. In Queue Viewer, click the Queues tab. A list of all queues on the server that you're
     connected to is displayed.
   3. Select the poison message queue. In the action pane, select View Messages.
   4. Select one or more messages from the list, right-click, and select Resume.

Use the Exchange Management Shell to resubmit messages in the
poison message queue
To resubmit a message from the poison message queue, perform the following steps.

   1. Find the identity of the message by running the following command on the local server.

       PowerShell

        Get-Message -Queue Poison | Format-Table Identity

   2. Use the identity of the message from the previous step in the following command.

       PowerShell

        Resume-Message <PoisonMessageIdentity>

     This example resumes a message from the poison message queue that has the message
     Identity value of 222.

       PowerShell

        Resume-Message 222

For more information, see Resume-Message.

How do you know this worked?
To verify that you have successfully resubmitted a message from the poison message queue,
use either of the following procedures to verify that the message is no longer in the queue:

     In Queue Viewer, view the poison message queue where you attempted to resubmit the
     message.

<!-- p.1776 -->

     In the Exchange Management Shell, run the following command:

         PowerShell

         Get-Message -Queue Poison

If the message you resubmitted was the only message in the poison message queue, and the
queue is no longer visible, that's also an indication of a successful message resubmission.

Suspend queues
You can suspend a queue to stop mail flow, and then suspend one or more messages in the
queue. For more information, see Suspend messages in queues.

Notes:

     You can suspend the following queues:
         A delivery queue that has any status.
         The Unreachable queue. Until you manually resume this queue, messages are no
         longer automatically resubmitted to the categorizer when configuration updates are
         detected.
         The Submission queue. Until you manually resume this queue, messages aren't picked
         up by the categorizer.
     Suspending a queue doesn't change the status of the messages in the queue to
     Suspended.

Use Queue Viewer to suspend a queue
   1. In the Exchange Toolbox, in the Mail flow tools section, double-click Queue Viewer to
     open the tool in a new window.
   2. In Queue Viewer, click the Queues tab. A list of all queues on the server that you're
     connected to is displayed. You can create a filter to display only queues that meet specific
     criteria.
   3. Select one or more queues, right-click, and then select Suspend.

Use the Exchange Management Shell to suspend a queue
To suspend a queue, use the following syntax:

  PowerShell

<!-- p.1777 -->

  Suspend-Queue <-Identity QueueIdentity | -Filter "QueueFilter" [-Server
  ServerIdentity]>

This example suspends all queues on the local server that have a message count equal to or
greater than 1,000 and that have a status of Retry.

  PowerShell

  Suspend-Queue -Filter "MessageCount -ge 1000 -and Status -eq 'Retry'"

This example suspends the queue named contoso.com on the server named Mailbox01.

  PowerShell

  Suspend-Queue -Identity Mailbox01\contoso.com

For more information, see Suspend-Queue.

How do you know this worked?
To verify that you have successfully suspended a queue, use either of the following procedures:

     In Queue Viewer, verify the queue has the Status value of Retry.

     In the Exchange Management Shell, replace <QueueIdentity> with the identity of the
     queue, and run the following command to verify the Status property value:

         PowerShell

         Get-Queue -Identity <QueueIdentity>

Resume queues
By resuming a queue, you restart outgoing message delivery from a queue that has a status of
Suspended.

Notes:

     You can only resume queues that have been suspended.
     Resuming a queue doesn't change the status of messages in the queue. For example,
     messages that have a status of Suspended remain suspended and don't leave the queue
     after you resume the queue.

<!-- p.1778 -->

Use Queue Viewer to resume queues
   1. In the Exchange Toolbox, in the Mail flow tools section, double-click Queue Viewer to
     open the tool in a new window.

   2. In Queue Viewer, click the Queues tab. A list of all queues on the server that you're
     connected to is displayed.

   3. Click Create Filter, and enter your filter expression as follows:
      a. Select Status from the queue property drop-down list.
     b. Select Equals from the comparison operator drop-down list.
      c. Select Suspended from the value drop-down list.

   4. Click Apply Filter. All queues on the server that are currently suspended are displayed.

   5. Select one or more queues from the list, right-click, and then select Resume.

Use the Exchange Management Shell to resume queues
To resume queues, use the following syntax:

  PowerShell

  Resume-Queue <-Identity QueueIdentity | -Filter "QueueFilter" [-Server
  ServerIdentity]>

This example resumes all queues on the local server that have a status of Suspended.

  PowerShell

  Resume-Queue -Filter "Status -eq 'Suspended'"

This example resumes the suspended delivery queue named contoso.com on the server named
Mailbox01.

  PowerShell

  Resume-Queue -Identity Mailbox01\contoso.com

For more information, see Resume-Queue.

How do you know this worked?

<!-- p.1779 -->

To verify that you have successfully resumed a queue, use either of the following procedures:

     In Queue Viewer, verify the queue doesn't have the Status value Suspended (for example,
     Active, Connecting, or Ready).

     In the Exchange Management Shell, replace <QueueIdentity> with the identity of the
     queue, and run the following command to verify the Status property value:

       PowerShell

       Get-Queue -Identity <QueueIdentity>

<!-- p.1780 -->

Queue properties in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016     2019       Subscription Edition

Filtering queues by one or more queue properties in Exchange Server allows you to quickly find
and take action on those queues. The following scenarios are examples of how you might use
queue filtering to manage mail flow:

       You receive a message from System Center Operations Manager that indicates a queue
       length has exceeded the established threshold. You want to investigate whether a server-
       wide mail flow problem exists.

       You create a filter to view all the queues on a server whose message count exceeds what
       you consider to be typical. If a mail flow problem is indicated, you can select all the
       queues in the results and suspend the queues while you continue to investigate.

       You suspend several queues to investigate the cause of mail flow problems. You
       determine that the problem was caused by an incorrect connector configuration that is
       now fixed.

       You can create a filter to view all the queues that have a status of Suspended, and then
       select all the queues in the filter results and resume the queues.

You can create queue filters in Queue Viewer in the Exchange Toolbox, or by using the Filter
parameter on the queue management cmdlets. Note that the queue management cmdlets
support more filterable properties than Queue Viewer.

For more information about Queue Viewer, see Queue Viewer. For more information about the
queue management cmdlets, see Procedures for queues and Find queues and messages in
queues in the Exchange Management Shell.

Queue properties to use as filters
The following table describes the queue properties that you can use as filters in Queue Viewer
and the Exchange Management Shell.

                                                                                     ﾉ   Expand table

 Queue       Exchange Management Shell          Comparison       Description
 Viewer                                         operators

 n/a         DeferredMessageCount               Equals ( -eq )   The number of messages returned to
                                                                 the Submission queue because of

<!-- p.1781 -->

Queue      Exchange Management Shell           Comparison       Description
Viewer                                         operators

                                               Does not         transient errors that were encountered
                                               equal ( -ne )    during recipient resolution. For more
                                                                information about deferred messages,
                                               Greater than     see Recipient resolution in Exchange
                                               ( -gt )          Server.

                                               Greater than
                                               or equal to
                                               ( -ge )

                                               Less than ( -
                                               lt )

                                               Less than or
                                               equal to ( -
                                               le )

n/a        DDeferredMessageCountsPerPriority   Equals ( -eq )   An array that shows the number of
                                                                deferred messages in the queue by
                                               Does Not         priority (importance) value. The
                                               Equal ( -ne )    MessageCountsPerPriority property
                                                                shows what each number means.
                                               Contains ( -
                                               like )           For example, the value {1, 5, 10, 0}
                                                                indicates the queue contains 1 deferred
                                                                High priority message, 5 deferred
                                                                Normal priority messages, 10 deferred
                                                                Low priority messages, and no deferred
                                                                messages that have the priority value
                                                                None.

Delivery   DeliveryType                        Equals ( -eq )   The results of the categorization of the
Type                                                            message, and how the Transport service
                                               Does Not         intends to transmit the message to the
                                               Equal ( -ne )    next hop. For a list of the available
                                                                DeliveryType values, see
                                                                NextHopSolutionKey.

n/a        FirstRetryTime                      Equals ( -eq )   The date/time of the first connection
                                                                attempt for a queue that has a status of
                                               Does not         Retry . For more information, see
                                               equal ( -ne )    Message retry, resubmit, and expiration
                                                                intervals.
                                               Greater than
                                               ( -gt )

                                               Greater than
                                               or equal to
                                               ( -ge )

<!-- p.1782 -->

Queue    Exchange Management Shell   Comparison       Description
Viewer                               operators

                                     Less than ( -
                                     lt )

                                     Less than or
                                     equal to ( -
                                     le )

n/a      Identity                    n/a              The identity of the queue in the form of
                                                      <Server>\ <Queue>. For more
                                                      information see Queue identity.

n/a      IncomingRate                Equals ( -eq )   A calculated number that indicates how
                                                      quickly messages are entering the
                                     Does not         queue. For more information, see
                                     equal ( -ne )    IncomingRate, OutgoingRate, and
                                                      Velocity.
                                     Greater than
                                     ( -gt )

                                     Greater than
                                     or equal to
                                     ( -ge )

                                     Less than ( -
                                     lt )

                                     Less than or
                                     equal to ( -
                                     le )

Last     LastError                   Equals ( -eq )   The last error that was recorded for the
Error                                                 queue. For more information about
                                     Does Not         SMTP error codes, see DSNs and NDRs
                                     Equal ( -ne )    in Exchange Server.

                                     Contains ( -
                                     contains )

                                     Is Present
                                     Is Not
                                     Present

Last     LastRetryTime               Greater          The date/time of the last connection
Retry                                Than ( -gt )     attempt for a queue that has a status of
Time                                                  Retry . For more information, see
                                     Greater          Message retry, resubmit, and expiration
                                     Than or          intervals.
                                     Equals ( -ge )

<!-- p.1783 -->

Queue     Exchange Management Shell   Comparison       Description
Viewer                                operators

                                      Less Than ( -
                                      lt )

                                      Less Than or
                                      Equals ( -le )

                                      Is Present
                                      Is Not
                                      Present

n/a       LockedMessageCount          n/a              This property is reserved for internal
                                                       Microsoft use, and isn't used in on-
                                                       premises Exchange organizations.

Message   MessageCount                Equals ( -eq )   The number of messages in the queue.
Count
                                      Does Not
                                      Equal ( -ne )

                                      Greater
                                      Than ( -gt )

                                      Greater
                                      Than or
                                      Equals ( -ge )

                                      Less Than ( -
                                      lt )

                                      Less Than or
                                      Equals ( -le )

n/a       MessageCountsPerPriority    Equals ( -eq )   An array that shows the number of
                                                       messages in the queue by priority
                                      Does Not         (importance) value. The
                                      Equal ( -ne )    MessageCountsPerPriority property
                                                       shows what each number means.
                                      Contains ( -
                                      like )           For example, the value {1, 100, 10, 0}
                                                       indicates the queue contains 1 High
                                                       priority message, 100 Normal priority
                                                       messages, 10 Low priority messages,
                                                       and no messages that have the priority
                                                       value None.

                                                       For more information about priority
                                                       queuing, see Priority Queuing.

<!-- p.1784 -->

Queue    Exchange Management Shell   Comparison       Description
Viewer                               operators

n/a      NextHopCategory             Equals ( -eq )   The value Internal or External for the
                                                      next hop based on the value of the
                                     Does Not         DeliveryType property. For more
                                     Equal ( -ne )    information, see NextHopSolutionKey.

n/a      NextHopConnector            Equals ( -eq )   The GUID of the next hop based on the
                                                      value of the DeliveryType property. For
                                     Does Not         more information, see
                                     Equal ( -ne )    NextHopSolutionKey.

                                     Contains ( -
                                     like )

Next     NextHopDomain               Equals ( -eq )   The name of next hop based on the
Hop                                                   value of the DeliveryType property. For
Domain                               Does Not         more information, see
                                     Equal ( -ne )    NextHopSolutionKey.

                                     Contains ( -
                                     like )

Next     NextRetryTime               Greater          The date/time of the next connection
Retry                                Than ( -gt )     attempt for a queue that has a status of
Time                                                  Retry . For more information, see
                                     Greater          Message retry, resubmit, and expiration
                                     Than or          intervals.
                                     Equals ( -ge )

                                     Less Than ( -
                                     lt )

                                     Less Than or
                                     Equals ( -le )

                                     Is Present
                                     Is Not
                                     Present

n/a      OutboundIPPool              n/a              This property is reserved for internal
                                                      Microsoft use, and isn't used in on-
                                                      premises Exchange organizations.

n/a      OutgoingRate                Equals ( -eq )   A calculated number that indicates how
                                                      quickly messages are leaving the queue.
                                     Does not         For more information, see
                                     equal ( -ne )    IncomingRate, OutgoingRate, and
                                                      Velocity.
                                     Greater than
                                     ( -gt )

<!-- p.1785 -->

Queue    Exchange Management Shell   Comparison       Description
Viewer                               operators

                                     Greater than
                                     or equal to
                                     ( -ge )

                                     Less than ( -
                                     lt )

                                     Less than or
                                     equal to ( -
                                     le )

n/a      OverrideSource              n/a              This property is reserved for internal
                                                      Microsoft use, and isn't used in on-
                                                      premises Exchange organizations.

n/a      PriorityDescriptions        n/a              The value descriptions in the
                                                      DeferredMessageCountsPerPriority
                                                      and MessageCountsPerPriority
                                                      properties. The value of this property is
                                                      {High, Normal, Low, None} .

                                                      Because the value of this property is
                                                      always the same, it won't make a good
                                                      filter.

n/a      RetryCount                  Equals ( -eq )   The number connection attempts for a
                                                      queue that has a status of Retry . For
                                     Does not         more information, see Message retry,
                                     equal ( -ne )    resubmit, and expiration intervals.

                                     Greater than
                                     ( -gt )

                                     Greater than
                                     or equal to
                                     ( -ge )

                                     Less than ( -
                                     lt )

                                     Less than or
                                     equal to ( -
                                     le )

n/a      RiskLevel                   n/a              This property is reserved for internal
                                                      Microsoft use, and isn't used in on-
                                                      premises Exchange organizations.

<!-- p.1786 -->

Queue    Exchange Management Shell   Comparison       Description
Viewer                               operators

Status   Status                      Equals ( eq )    The current queue status. A queue can
                                                      have one of the following status values:
                                     Does Not         Active, Connecting, Suspended, Ready,
                                     Equal ( -ne )    or Retry. For more information, see
                                                      Queue status.

n/a      TlsDomain                   Equals ( -eq )   The FQDN of the destination domain if
                                                      the domain is configured for Domain
                                     Does Not         Security (mutual TLS authentication).
                                     Equal ( -ne )

                                     Contains ( -
                                     like )

n/a      Velocity                    Equals ( -eq )   A calculated number that indicates how
                                                      effectively the queue is draining. For
                                     Does not         more information, see IncomingRate,
                                     equal ( -ne )    OutgoingRate, and Velocity

                                     Greater than
                                     ( -gt )

                                     Greater than
                                     or equal to
                                     ( -ge )

                                     Less than ( -
                                     lt )

                                     Less than or
                                     equal to ( -
                                     le )

<!-- p.1787 -->

Export messages from queues in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

On Mailbox servers and Edge Transport servers in Exchange Server, you can export the
messages in a queue to files. The exported messages aren't removed from the queue. Copies
of the messages are made in the specified location as a plain text files. You can view the
message files in Notepad or Outlook, and you can resubmit the message files by using the
Replay directory on any other Mailbox server or Edge Transport server inside or outside your
Exchange organization.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Queues" entry in Mail flow
      permissions topic.

      To export messages from a delivery queue, the Submission queue, or the Unreachable
      queue, the messages need to be in the Suspended state. For active, healthy queues, you
      first suspend the queue so you can then suspend the messages. Messages in the poison
      message queue are already in the Suspended state. For more information, see Suspend
      queues and Suspend messages in queues.

      You can't use Queue Viewer in the Exchange Toolbox to export messages. However, you
      can use Queue Viewer to locate, identify, and suspend the messages before you export
      them using the Exchange Management Shell. For more information about Queue Viewer,
      see Queue Viewer. To learn how to open the Exchange Management Shell in your on-
      premises Exchange organization, see Open the Exchange Management Shell.

      When you export messages from a queue, you don't remove the messages from the
      queue. If you resubmit the exported messages by using the Replay directory, you should
      remove the messages from the queue to avoid duplicate message delivery. For more
      information, see Remove messages from queues.

      Verify the following information about the target location for the exported message files:
         The target folder needs to exist before you export any messages, and won't be created
         for you. If you don't specify the complete path, the files are written to the current
         Exchange Management Shell working directory.

<!-- p.1788 -->

        The path can be local to the Exchange server, or it can be a UNC path to a share on a
        remote server (\server\share).
        Your account needs to have the Write permission in the target folder.

     We use the message's InternetMessageID property value for the exported message file
     names to help ensure uniqueness. The procedures include steps to remove angled
     brackets (> and <), because they aren't allowed in file names. Also, we use the .eml file
     name extension so you can easily open the files in Outlook or resubmit the files by using
     the Replay directory.

     For more information about identity and filters for queues and messages in queues, see
     the following topics:
        Find queues and messages in queues in the Exchange Management Shell
        Queue properties
        Properties of messages in queues

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Use the Exchange Management Shell to export a
specific message from a queue
To export a specific message from a queue, use the following syntax:

  PowerShell

  Export-Message -Identity <MessageIdentity> | AssembleMessage -Path <FilePath>\
  <FileName>.eml

This example takes the following actions on the server named Mailbox01:

   1. Suspends the contoso.com delivery queue.

   2. Suspends the message in the queue that has the InternalMessageID value 1234.

   3. Exports a copy of the message to the file D:\contoso Export\export.eml.

<!-- p.1789 -->

  PowerShell

  Suspend-Queue Mailbox01\contoso.com

  PowerShell

  Suspend-Message -Identity Mailbox01\contoso.com\1234

  PowerShell

  Export-Message -Identity Mailbox01\contoso.com\1234 | AssembleMessage -Path
  "D:\Contoso Export\export.eml"

Use the Exchange Management Shell to export all
messages from a queue
To export all messages from a queue, and use the InternetMessageID value of each message
as the file name, use the following syntax:

  PowerShell

  Get-Message -Queue <QueueIdentity> -ResultSize Unlimited | ForEach-Object {$Temp=
  <Path>+$_.InternetMessageID+".eml"; $Temp=$Temp.Replace("<","_");
  $Temp=$Temp.Replace(">","_"); Export-Message $_.Identity | AssembleMessage -Path
  $Temp}

This example takes the following actions on the server named Mailbox01:

   1. Suspends the contoso.com delivery queue.
   2. Suspends all messages in the queue.
   3. Exports copies of the messages to the local folder named D:\Contoso Export.

  PowerShell

  Suspend-Queue Mailbox01\contoso.com

  PowerShell

  Get-Queue Mailbox01\contoso.com | Get-Message -ResultSize Unlimited | Suspend-
  Message

  PowerShell

<!-- p.1790 -->

  Get-Message -Queue Mailbox01\Contoso.com -ResultSize Unlimited | ForEach-Object
  {$Temp="D:\Contoso Export\"+$_.InternetMessageID+".eml"; $Temp=$Temp.Replace("
  <","_"); $Temp=$Temp.Replace(">","_"); Export-Message $_.Identity |
  AssembleMessage -Path $Temp}

Use the Exchange Management Shell to export
specific messages from all queues on a server
To export specific messages from all queues on a server, and use the InternetMessageID value
of each message as the file name, use the following syntax:

  PowerShell

  Get-Message -Filter "<MessageFilter>" [-Server <ServerIdentity>] -ResultSize
  Unlimited | ForEach-Object {$Temp=<Path>+$_.InternetMessageID+".eml";
  $Temp=$Temp.Replace("<","_"); $Temp=$Temp.Replace(">","_"); Export-Message
  $_.Identity | AssembleMessage -Path $Temp}

This example takes the following actions on the server named Mailbox01:

   1. Suspends all queues on the server.
   2. Suspends all messages in all queues on the server from senders in the fabrikam.com
     domain.
   3. Exports copies of the messages to the local folder named D:\Fabrikam Export.

  PowerShell

  Suspend-Queue -Server Mailbox01

  PowerShell

  Suspend-Message -Filter "FromAddress -like '*@fabrikam.com'" -Server Mailbox01

  PowerShell

  Get-Message -Filter "FromAddress -like '*@fabrikam.com'" -Server Mailbox01 -
  ResultSize Unlimited | ForEach-Object {$Temp="D:\Fabrikam
  Export\"+$_.InternetMessageID+".eml"; $Temp=$Temp.Replace("<","_");
  $Temp=$Temp.Replace(">","_"); Export-Message $_.Identity | AssembleMessage -Path
  $Temp}

<!-- p.1791 -->

Use the Exchange Management Shell to export all
messages from all queues on a server
To export all messages from all queues on a server, and use the InternetMessageID value of
each message as the file name, use the following syntax:

  PowerShell

  Get-Message [-Server <ServerIdentity>] -ResultSize Unlimited | ForEach-Object
  {$Temp=<Path>+$_.InternetMessageID+".eml"; $Temp=$Temp.Replace("<","_");
  $Temp=$Temp.Replace(">","_"); Export-Message $_.Identity | AssembleMessage -Path
  $Temp}

This example takes the following actions on the server named Mailbox01:

   1. Suspends all queues on the server.
   2. Suspends all messages in all queues on the server.
   3. Exports copies of the messages to the local folder named D:\Mailbox01 Export.

  PowerShell

  Suspend-Queue -Server Mailbox01

  PowerShell

  Get-Queue -Server Mailbox01 | Get-Message -ResultSize Unlimited | Suspend-Message

  PowerShell

  Get-Message -Server Mailbox01 -ResultSize Unlimited | ForEach-Object
  {$Temp="D:\Mailbox01 Export\"+$_.InternetMessageID+".eml"; $Temp=$Temp.Replace("
  <","_"); $Temp=$Temp.Replace(">","_"); Export-Message $_.Identity |
  AssembleMessage -Path $Temp}

<!-- p.1792 -->

Procedures for messages in queues
Article • 04/30/2025

APPLIES TO:        2016      2019    Subscription Edition

In Exchange Server, you can use the Queue Viewer in the Exchange Toolbox or the Exchange
Management Shell to manage messages in queues. For more information about messages in
queues, see Message properties.

This topic describes how to perform the following procedures on messages in queues:

      Remove messages: You can remove messages from queues with our without a non-
      delivery report to the sender (also known as an NDR, delivery status notification, DSN, or
      bounce message).
      Suspend messages: When you suspend a message, you prevent delivery of the message.
      The message won't leave the queue until you resume the message.
      Resume messages: You can resume a message that currently has a status of Suspended.
      By resuming a message, you enable delivery of the message.
      Redirect messages: You can drain messages from all the delivery queues on a Mailbox
      server, and transfer those messages to another Mailbox server.

For information about exporting messages from queues, see Export messages from queues.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes

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

<!-- p.1793 -->

          charm, and type Exchange Toolbox.

        When the shortcut appears in the results, you can select it.

     To learn how to open the Exchange Management Shell in your on-premises Exchange
     organization, see Open the Exchange Management Shell.

     For more information about using filters and identity values in the Exchange Management
     Shell, see Find queues and messages in queues in the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Queues" entry in the Mail flow
     permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

Remove messages from queues
Note:

A message that's being sent to multiple recipients might be located in more than one queue.
To remove a message from more than one queue in a single operation, you need to use a filter.
For more information, see Properties of messages in queues and Message filtering parameters.

Use Queue Viewer to remove messages from queues
  1. In the Exchange Toolbox, in the Mail flow tools section, double-click Queue Viewer to
     open the tool in a new window.

  2. In Queue Viewer, click the Messages tab. A list of all messages on the server that you're
     connected to is displayed. To adjust the action to a single queue, click the Queues tab,
     double-click the queue name, and then click the Server\Queue tab that appears.

  3. Select one or more messages from the list, right-click, and then select Remove Messages
     (with NDR) or Remove Messages (without NDR). A dialog box appears that confirms the
     selected action and displays, Do you want to continue?. Click Yes.

<!-- p.1794 -->

   4. To remove all messages from a particular queue, click the Queues tab. Select a queue,
     right-click, and then select Remove Messages (with NDR) or Remove Messages (without
     NDR). A dialog box appears that confirms the selected action and displays, Do you want
     to continue?. Click Yes.

        ７ Note

        If you're working with a filtered list, the displayed page may not include all items in
        the filter. In this case, a prompt appears that displays: This action will affect all items
        on this page. To expand the scope of this action to include all items in this filter,
        check the following box before you click OK.

Use the Exchange Management Shell to remove messages
To remove messages from queues, use the following syntax.

  PowerShell

  Remove-Message <-Identity MessageIdentity | -Filter "MessageFilter"> -WithNDR
  <$true | $false>

This example removes messages in the queues that have a subject of "Win Big" without
sending an NDR.

  PowerShell

  Remove-Message -Filter "Subject -eq 'Win Big'" -WithNDR $false

This example removes the message with the message ID 3 from the Unreachable queue on
server named Mailbox01 and sends an NDR.

  PowerShell

  Remove-Message -Identity Mailbox01\Unreachable\3 -WithNDR $true

For more information, see Remove-Message

How do you know this worked?
To verify that you have successfully removed messages from queues, use either of the
following procedures:

<!-- p.1795 -->

    In Queue Viewer, select the queue or create a filter to verify the messages no longer exist.

    In the Exchange Management Shell, replace MessageFilter with the filter that you used, or
    <QueueIdentity> with the identity of the queue, and run either of the following
    commands to verify the messages no longer exist:

         PowerShell

         Get-Message -Filter "MessageFilter"

    Or

         PowerShell

         Get-Message -Queue <QueueIdentity>

    For more information, see Get-Message.

Suspend messages in queues
Notes:

    A message that's being sent to multiple recipients might be located in more than one
    queue. To suspend a message in more than one queue in a single operation, you need to
    use a filter. For more information, see Properties of messages in queues and Message
    filtering parameters.

    If you suspend a message that's in the act of being transmitted to the next hop, delivery
    of the message will continue, and the message status will be PendingSuspend. If delivery
    fails, the message will re-enter the queue, and then the message will be suspended.

Use Queue Viewer to suspend messages
  1. In the Exchange Toolbox, in the Mail flow tools section, double-click Queue Viewer to
    open the tool in a new window.

  2. In Queue Viewer, click the Messages tab. A list of all messages on the server that you're
    connected to is displayed. To limit the view to a single queue, click the Queues tab,
    double-click the queue name, and then click the Server\Queue tab that appears.

  3. Select one or more messages, right-click, and then select Suspend.

<!-- p.1796 -->

Use the Exchange Management Shell to suspend messages
To suspend messages, use the following syntax:

  PowerShell

  Suspend-Message <-Identity MessageIdentity | -Filter "MessageFilter">

This example suspends the message with the message ID 3 in the Unreachable queue on server
named Mailbox01.

  PowerShell

  Suspend-Message -Identity Mailbox01\Unreachable\3

This example suspends all messages in all queues on the local server that are from any sender
in the domain contoso.com.

  PowerShell

  Suspend-Message -Filter "FromAddress -like '*contoso.com'"

This example suspends all messages in the delivery queue for contoso.com on the server
named Mailbox01.

  PowerShell

  Get-Queue Mailbox01\contoso.com | Get-Message | Suspend-Message

This example suspends all messages in all queues on the local server.

  PowerShell

  Get-Queue | Get-Message | Suspend-Message

For more information, see Suspend-Message.

How do you know this worked?
To verify that you have successfully suspended messages in queues, use either of the following
procedures:

     In Queue Viewer, select the queue or create a filter to verify messages are suspended.

<!-- p.1797 -->

    In the Exchange Management Shell, replace MessageFilter with the filter that you used, or
    <QueueIdentity> with the identity of the queue, and run either of the following
    commands to verify that the messages are suspended:

         PowerShell

         Get-Message -Filter "MessageFilter"

    Or

         PowerShell

         Get-Message -Queue <QueueIdentity>

    For more information, see Get-Message.

Resume messages in queues
Notes:

    You can only resume messages that have a status of Suspended.
    The status of the queue that holds the messages affects the delivery of the message. For
    example, if you resume suspended messages in a queue that has a status of Suspended,
    the messages can't be delivered until you resume the queue. For more information about
    resuming queues, see Resume queues.

Use Queue Viewer to resume messages
  1. In the Exchange Toolbox, in the Mail flow tools section, double-click Queue Viewer to
    open the tool in a new window.

  2. In Queue Viewer, click the Messages tab. A list of all messages on the server that you're
    connected to is displayed. To adjust the action to focus on a single queue, click the
    Queues tab, double-click the queue name, and then click the Server\Queue tab that
    appears.

  3. Click Create Filter, and enter your filter expression as follows:
     a. Select Status from the message property drop-down list.
     b. Select Equals from the comparison operator drop-down list.
     c. Select Suspended from the value drop-down list.

  4. Click Apply Filter. All messages that have a status of Suspended are displayed.

<!-- p.1798 -->

   5. Select one or more messages from the list, right-click, and select Resume.

Use the Exchange Management Shell to resume messages
To resume messages, use the following syntax:

  PowerShell

  Resume-Message <-Identity MessageIdentity | -Filter "MessageFilter">

This example resumes all messages being sent from any sender in the contoso.com domain.

  PowerShell

  Resume-Message -Filter "FromAddress -like '*contoso.com'"

This example resumes the message with the message ID 3 in the Unreachable queue on server
named Mailbox01.

  PowerShell

  Resume-Message -Identity Mailbox01\Unreachable\3

How do you know this worked?
To verify that you have successfully resumed messages in queues, use either of the following
procedures:

     In Queue Viewer, select the queue or create a filter to verify the that messages are no
     longer suspended.

     In the Exchange Management Shell, replace MessageFilter with the filter that you used, or
     <QueueIdentity> with the identity of the queue, and run either of the following
     commands to verify that the messages are no longer suspended:

        PowerShell

          Get-Message -Filter "MessageFilter"

     Or

        PowerShell

<!-- p.1799 -->

         Get-Message -Queue <QueueIdentity>

     For more information, see Get-Message.

If you can't find the messages in any queues on the server, this likely indicates the message
was successfully delivered to the next hop.

Redirect messages in queues
Redirecting messages drains all active messages from delivery queues on the source Mailbox
server and routes them to the target Mailbox server. The messages are queued for delivery and
routed to the next hop.

Notes:

     Only active messages are redirected.
     Shadow queues and messages in the poison message queue aren't redirected.
     The source Mailbox server doesn't accept new messages while messages are being
     redirected.
     You can only use the Exchange Management Shell to redirect messages.

Use the Exchange Management Shell to redirect messages
To redirect messages, use the following syntax:

  PowerShell

  Redirect-Message -Server <ServerIdentity> -Target <ServerFQDN>

This example redirects messages from all delivery queues on the server named Mailbox01 to
the server named Mailbox02.contoso.com.

  PowerShell

  Redirect-Message -Server Mailbox01 -Target Mailbox02.contoso.com

For more information, see Redirect-Message.

How do you know this worked?

<!-- p.1800 -->

To verify that you have successfully redirected messages in queues, use either of the following
procedures:

     In Queue Viewer, verify that the Message Count value on delivery queues on the source
     server is empty or decreasing.

     In the Exchange Management Shell, run the following command to verify that the
     MessageCount property value for the delivery queues on the source server is decreasing
     or empty.

       PowerShell

        Get-Queue
