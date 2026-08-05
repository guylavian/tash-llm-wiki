---
title: "Exchange Server — pages 1721-1760"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1721-1760
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1721-1760
family: exchange
documentKind: "doc"
abstract: "Event name Description POISONMESSAGE A message was put in the poison message queue or removed from the poison message queue. PROCESS The message was successfully processed. PROCESSMEETINGMESSAGE A meeting message was processed by the Mailbox Transport Delivery service. RECEIVE A"
---

# Exchange Server — pages 1721-1760

<!-- p.1721 -->

Event name              Description

POISONMESSAGE           A message was put in the poison message queue or removed from the
                        poison message queue.

PROCESS                 The message was successfully processed.

PROCESSMEETINGMESSAGE   A meeting message was processed by the Mailbox Transport Delivery
                        service.

RECEIVE                 A message was received by the SMTP receive component of the transport
                        service or from the Pickup or Replay directories (source: SMTP ), or a
                        message was submitted from a mailbox to the Mailbox Transport
                        Submission service (source: STOREDRIVER ).

REDIRECT                A message was redirected to an alternative recipient after an Active
                        Directory lookup.

RESOLVE                 A message's recipients were resolved to a different email address after an
                        Active Directory lookup.

RESUBMIT                A message was automatically resubmitted from Safety Net. For more
                        information, see Safety Net in Exchange Server.

RESUBMITDEFER           A message resubmitted from Safety Net was deferred.

RESUBMITFAIL            A message resubmitted from Safety Net failed.

SEND                    A message was sent by SMTP between transport services.

SUBMIT                  The Mailbox Transport Submission service successfully transmitted the
                        message to the Transport service. For SUBMIT events, the source-context
                        property contains the following details:

                              MDB: The mailbox database GUID.
                              Mailbox: The mailbox GUID.
                              Event: The event sequence number.
                              MessageClass: The type of message. For example, IPM.Note .
                              CreationTime: Date-time of the message submission.
                              ClientType: For example, User , OWA , or ActiveSync .

SUBMITDEFER             The message transmission from the Mailbox Transport Submission service
                        to the Transport service was deferred.

SUBMITFAIL              The message transmission from the Mailbox Transport Submission service
                        to the Transport service failed.

SUPPRESSED              The message transmission was suppressed.

THROTTLE                The message was throttled.

<!-- p.1722 -->

 Event name                  Description

 TRANSFER                    Recipients were moved to a forked message because of content
                             conversion, message recipient limits, or agents. Sources include ROUTING
                             or QUEUE.

Source values in the message tracking log
The values in the source field in the message tracking log indicate the transport component
that's responsible for the message tracking event. The following table describes the values of
the source field.

                                                                                      ﾉ   Expand table

 Source value                   Description

 ADMIN                          The event source was human intervention. For example, an
                                administrator used Queue Viewer to delete a message, or submitted
                                message files using the Replay directory.

 AGENT                          The event source was a transport agent.

 APPROVAL                       The event source was the approval framework that's used with
                                moderated recipients. For more information, see Manage message
                                approval.

 BOOTLOADER                     The event source was unprocessed messages that exist on the server at
                                boot time. This is related to the LOAD event type.

 DNS                            The event source was DNS.

 DSN                            The event source was a delivery status notification (also known as a
                                DSN, bounce message, non-delivery report, or NDR).

 GATEWAY                        The event source was a Foreign connector. For more information, see
                                Foreign Connectors.

 MAILBOXRULE                    The event source was an Inbox rule. For more information, see Inbox
                                rules   .

 MEETINGMESSAGEPROCESSOR        The event source was the meeting message processor, which updates
                                calendars based on meeting updates.

 ORAR                           The event source was an Originator Requested Alternate Recipient
                                (ORAR). You can enable or disable support for ORAR on Receive
                                connectors using the OrarEnabled parameter on the New-
                                ReceiveConnector or Set-ReceiveConnector cmdlets.

<!-- p.1723 -->

 Source value                  Description

 PICKUP                        The event source was the Pickup directory. For more information, see
                               Pickup Directory and Replay Directory.

 POISONMESSAGE                 The event source was the poison message identifier. For more
                               information about poison messages and the poison message queue,
                               see Queues and messages in queues

 PUBLICFOLDER                  The event source was a mail-enabled public folder.

 QUEUE                         The event source was a queue.

 REDUNDANCY                    The event source was Shadow Redundancy. For more information, see
                               Shadow redundancy in Exchange Server.

 RESOLVER                      The event source was the recipient resolution component of the
                               categorizer in the Transport service. For more information, see
                               Recipient resolution in Exchange Server.

 ROUTING                       The event source was the routing resolution component of the
                               categorizer in the Transport service.

 SAFETYNET                     The event source was Safety Net. For more information, see Safety Net
                               in Exchange Server.

 SMTP                          The message was submitted by the SMTP send or SMTP receive
                               component of the transport service.

 STOREDRIVER                   The event source was a MAPI submission from a mailbox on the local
                               server.

Example entries in the message tracking log
An uneventful message sent between two users generates several entries in the message
tracking log. You can see the results using the Get-MessageTrackingLog cmdlet. For more
information, see Search message tracking logs.

This is an example of the message tracking log entries created when the user
chris@contoso.com successfully sends a test message to the user michelle@contoso.com. Both
users have mailboxes on the same server.

  EventId    Source      Sender            Recipients             MessageSubject
  -------    ------      ------            ----------             --------------
  NOTIFYMAPI STOREDRIVER                   {}
  RECEIVE    STOREDRIVER chris@contoso.com {michelle@contoso.com} test
  SUBMIT     STOREDRIVER chris@contoso.com {michelle@contoso.com} test

<!-- p.1724 -->

  HAREDIRECT SMTP        chris@contoso.com {michelle@contoso.com} test
  RECEIVE    SMTP        chris@contoso.com {michelle@contoso.com} test
  AGENTINFO AGENT        chris@contoso.com {michelle@contoso.com} test
  SEND       SMTP        chris@contoso.com {michelle@contoso.com} test
  DELIVER    STOREDRIVER chris@contoso.com {michelle@contoso.com} test

Security concerns for the message tracking log
No message content is stored in the message tracking log. By default, the subject line of an
email message is stored in the message tracking log. You might need to disable subject
logging to comply with increased security or privacy requirements. For instructions on how to
disable subject logging, see Configure message tracking.

<!-- p.1725 -->

Configure message tracking in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Message tracking records the message activity as mail flows through the transport pipeline on
Mailbox servers and Edge Transport servers. You can use message tracking logs for message
forensics, mail flow analysis, reporting, and troubleshooting.

You use the Set-TransportService cmdlet in the Exchange Management Shell on Mailbox
servers and Edge Transport servers for all message tracking configuration tasks. For example:

      Enable or disable message tracking. The default is enabled.

      Specify the location of the message tracking log files. The default location is
      %ExchangeInstallPath%TransportRoles\Logs\MessageTracking .

      Specify a maximum size for the individual message tracking log files. The default is 10 MB.

      Specify a maximum size for the directory that contains the message tracking log files: The
      default is 1000 MB.

      Specify maximum age for the message tracking log files: The default is 30 days.

      Enable or disable message subject logging in the message tracking logs. The default is
      enabled.

  ７ Note

  On Mailbox servers, you can also use the Exchange admin center (EAC) to enable or
  disable message tracking, and to specify the location of the message tracking log files.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Transport service" entries in the
      Mail flow permissions topic.

<!-- p.1726 -->

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online       , or Exchange Online Protection .

Use the EAC to configure message tracking on
Mailbox servers
   1. Open the EAC and navigate to Servers > Servers > select the Mailbox server that you
     want to configure > and click Edit      .

   2. On the server properties page, click Transport Logs. In the Message tracking log section,
     change any of the following settings:

           Enable message tracking log: To disable message tracking on the server, clear the
           check box. To enable message tracking on the server, select the check box.

           Message tracking log path: The value you specify must be on the local Exchange
           server. If the folder doesn't exist, it's created for you when you click Save.

   3. When you're finished, click Save.

Use the Exchange Management Shell to configure
message tracking
As previously explained, you can use the Set-TransportService cmdlet to perform all message
tracking configuration tasks on Mailbox servers and Edge Transport servers. To configure
message tracking in the Exchange Management Shell, use the following syntax:

  PowerShell

  Set-TransportService [<ServerIdentity>] -MessageTrackingLogEnabled <$true |
  $false> -MessageTrackingLogMaxAge <dd.hh:mm:ss> -
  MessageTrackingLogMaxDirectorySize <Size> -MessageTrackingLogMaxFileSize <Size> -
  MessageTrackingLogPath <LocalFilePath> -MessageTrackingLogSubjectLoggingEnabled
  <$true | $false>

<!-- p.1727 -->

Note that you don't need to specify the Exchange server when you run the command on the
server that you want to configure.

This example configures the following message tracking log settings on the server named
Mailbox01:

     Sets the location of the message tracking log files to D:\Message Tracking Log. Note that
     if the folder doesn't exist, it's created for you.

     Sets the maximum size of a message tracking log file to 20 MB.

     Sets the maximum size of the message tracking log directory to 1.5 GB.

     Sets the maximum age of a message tracking log file to 45 days.

  PowerShell

  Set-TransportService Mailbox01 -MessageTrackingLogPath "D:\Message Tracking Log" -
  MessageTrackingLogMaxFileSize 20MB -MessageTrackingLogMaxDirectorySize 1.5GB -
  MessageTrackingLogMaxAge 45.00:00:00

  ７ Note

        Setting the MessageTrackingLogPath parameter to the value $null , effectively
        disables message tracking. However, if the value of the MessageTrackingLogEnabled
        parameter is $true , event log errors are generated.
        Setting the MessageTrackingLogMaxAge parameter to the value 00:00:00 prevents
        the automatic removal of message tracking log files because of their age.
        The maximum size of the message tracking log directory is three times the value of
        the MessageTrackingLogMaxDirectorySize parameter. Although the message tracking
        log files that are generated by the four different services have four different name
        prefixes, the amount and frequency of data written to the moderated transport log
        (MSGTRKMA) is negligible compared to the other three logs. For more information,
        see Structure of the message tracking log files.

This example disables message subject logging in the message tracking log on the server
named Mailbox01:

  PowerShell

  Set-TransportService Mailbox01 -MessageTrackingLogSubjectLoggingEnabled $false

<!-- p.1728 -->

This example disables message tracking on the Mailbox server named Mailbox01:

  PowerShell

  Set-TransportService Mailbox01 -MessageTrackingLogEnabled $false

How do you know this worked?

To verify that you have successfully configured message tracking, run the following command
in the Exchange Management Shell:

  PowerShell

  Get-TransportService [<ServerIdentity>] | Format-List MessageTrackingLog*

You can also open the location of the message tracking log in Windows Explorer or File
Explorer to verify that the log files exist, that data is being written to the files, and that they're
being recycled based on the maximum file size and maximum directory size values that you
configured.

<!-- p.1729 -->

Exchange Server: Search message tracking
logs
Article • 04/30/2025

APPLIES TO:        2016       2019       Subscription Edition

Message tracking records the message activity as mail flows through the transport pipeline on
Mailbox servers and Edge Transport servers. You can use the Get-MessageTrackingLog cmdlet
in the Exchange Management Shell to search for entries in the message tracking log by using
specific search criteria. For example:

      Find out what happened to a message that was sent by a user to a specific recipient.

      Find out if a mail flow rule (also known as a transport rule) acted on a message.

      Find out if a message sent from an Internet sender made it into your Exchange
      organization.

      Find all messages sent by a specified user during a specified time period.

What do you need to know before you begin?
      Estimated time to complete: 10 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Message tracking" entry in the
      Mail flow permissions topic.

      Searching the message tracking logs requires that the Microsoft Exchange Transport Log
      Search service is running. If you disable or stop this service, you can't search the message
      tracking logs or run delivery reports. However, stopping this service does not affect other
      features in Exchange.

      The field names displayed in the results from the Get-MessageTrackingLog cmdlet are
      similar to the actual field names found in the message tracking log files. The biggest
      differences are:

         Dashes are removed from the field names. For example, internal-message-id is
         displayed as InternalMessageId .

         The date-time field is displayed as Timestamp .

         The recipient-address field is displayed as Recipients .

<!-- p.1730 -->

        The sender-address field is displayed as Sender .

     The date-time field in the message tracking log stores information in Coordinated
     Universal Time (UTC). However, you need to enter your date-time search criteria for the
     Start or End parameters in the regional date-time format of the computer that you're
     using to perform the search.

     You can't copy the message tracking log files from another Exchange server and then
     search them by using the Get-MessageTrackingLog cmdlet. Also, if you manually save an
     existing message tracking log file, the change in the file's date-time stamp breaks the
     query logic that Exchange uses to search the message tracking logs.

     In Exchange 2016, the Get-MessageTrackingLog cmdlet is able to search the message
     tracking logs on Exchange 2013 Mailbox servers and Exchange 2010 Hub Transport
     servers in the same Active Directory site. In Exchange 2019, the Get-MessageTrackingLog
     cmdlet is able to search the message tracking logs on Exchange 2016 and Exchange 2013
     Mailbox servers in the same Active Directory site.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Use the Exchange Management Shell to search the
message tracking logs
To search the message tracking log entries for specific events, use the following syntax.

  PowerShell

  Get-MessageTrackingLog [-Server <ServerIdentity>] [-ResultSize <Integer> |
  Unlimited] [-Start <DateTime>] [-End <DateTime>] [-EventId <EventId>] [-
  InternalMessageId <InternalMessageId>] [-MessageId <MessageId>] [-MessageSubject
  <Subject>] [-Recipients <RecipientAddress1,RecipientAddress2...>] [-Reference
  <Reference>] [-Sender <SenderAddress>]

To view the 1000 most recent message tracking log entries on the server, run the following
command:

<!-- p.1731 -->

  PowerShell

  Get-MessageTrackingLog

This example searches the message tracking logs on the local server for all entries from
3/28/2015 8:00 AM to 3/28/2015 5:00 PM for all FAIL events where the message sender was
pat@contoso.com.

  PowerShell

  Get-MessageTrackingLog -ResultSize Unlimited -Start "3/28/2015 8:00AM" -End
  "3/28/2015 5:00PM" -EventId "Fail" -Sender "pat@contoso.com"

Use the Exchange Management Shell to control the
output of a message tracking log search
Use the following syntax.

  PowerShell

  Get-MessageTrackingLog <SearchFilters> | <Format-Table | Format-List>
  [<FieldNames>] [<OutputFileOptions>]

This example searches the message tracking logs using the following search criteria:

     Return results for the first 1,000 Send events.

     Display the results in the list format.

     Display only those field names that begin with Send or Recipient .

     Write the output to a new file named D:\Send Search.txt

  PowerShell

  Get-MessageTrackingLog -EventId Send | Format-List Send*,Recipient* | Set-Content
  -Path "D:\Send Search.txt"

Use the Exchange Management Shell to search the
message tracking logs for message entries on
multiple servers

<!-- p.1732 -->

Typically, the value in the MessageID: header field remains constant as the message travels
throughout the Exchange organization. This property is named InternetMessageId in queue
viewing utilities, and MessageId in the message tracking log viewing utilities. After you have
determined the MessageID: value of a specific message, you can search for information about
that message in the message tracking logs on every Mailbox server in your Exchange
organization.

To search all message tracking log entries for a specific message across all Mailbox servers and
Exchange 2010 Hub Transport servers, use the following syntax.

  PowerShell

  $Servers = Get-ExchangeServer; $Servers | where {$_.isHubTransportServer -eq
  $true -or $_.isMailboxServer -eq $true} | Get-MessageTrackingLog -MessageId
  <MessageID> | Select-Object <CommaSeparatedFieldNames> | Sort-Object -Property
  <FieldName>

This example searches the message tracking logs on all Mailbox servers and Exchange 2010
Hub Transport server by using the following search criteria:

     Find any entries related to a message that has a MessageID: value of <ba18339e-8151-
     4ff3-aeea-87ccf5fc9796@mailbox01.contoso.com> . Note that you can omit the angle

     bracket characters ( < > ). If you don't, you need to enclose the entire MessageID: value in
     quotation marks.

     For each entry, display the fields date-time, server-hostname, client-hostname, source,
     event-id, and recipient-address.

     Sort the results by the date-time field.

  PowerShell

  $Servers = Get-ExchangeServer; $Servers | where {$_.isHubTransportServer -eq $true
  -or $_.isMailboxServer -eq $true} | Get-MessageTrackingLog -MessageId ba18339e-
  8151-4ff3-aeea-87ccf5fc9796@mailbox01.contoso.com | Select-Object
  Timestamp,ServerHostname,ClientHostname,Source,EventId,Recipients | Sort-Object -
  Property Timestamp

Use the EAC to search the message tracking logs
You can use the Delivery Reports for administrators feature in the Exchange admin center (EAC)
to search the message tracking logs for information about messages sent by or received by a
specific mailbox in your organization. For more information, see Track messages with delivery
reports.

<!-- p.1733 -->

<!-- p.1734 -->

Delivery reports for administrators in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

With delivery reports for administrators, you can track delivery information about messages
sent by or received from any specific mailbox in your organization. Specifically, delivery reports
for administrators uses the Exchange admin center (EAC) to perform a targeted search of the
message tracking logs. The search is always scoped to a specific mailbox. You can search for
messages sent by the mailbox, or sent to the mailbox, and you can filter the search results by
the message subject.

The content of the message body isn't returned in a delivery report, but the subject line is
displayed in the results. If you want to search the mailboxes in your organization for specific
email messages based on message content, see In-Place eDiscovery in Exchange Server.

You may find delivery report searches useful in the following situations:

      A manager gives a poor review for a trainee because the trainee didn't turn in an
      assignment on time. The trainee insists he sent a message with the assignment attached.
      The manager asks you to verify the status of the message.

      A security bulletin has been sent to users asking that they reply immediately, but no one
      has replied. Are they ignoring the message or did they just not receive it?

      Users complain that no one is receiving their messages. They check delivery status for
      their mail but can't figure out what is going on. This may be because a rule is being
      applied to messages at the organization level.

After you create a delivery report search, the resulting delivery report will show the following
information: Who the message was sent from and to, the subject line, and when the message
was sent. The delivery report also shows message delivery status and reasons why delivery may
be delayed or failed.

More about delivery reports
      Here's how administrators in on-premises Exchange organizations create delivery reports:
      Track messages with delivery reports.

      A more powerful option for administrators in on-premises Exchange organizations is to
      use the Exchange Management Shell to query the message tracking logs directly. For

<!-- p.1735 -->

more information, see Search message tracking logs.

Exchange 2016 or Exchange 2019 delivery reports can track messages across Exchange
2019, Exchange 2016, and Exchange 2013 servers in the same Active Directory site.

<!-- p.1736 -->

Exchange Server: Track messages with
delivery reports
Article • 04/30/2025

APPLIES TO:        2016       2019    Subscription Edition

Delivery Reports is a message tracking tool in the Exchange admin center (EAC) that you can
use to search for delivery status on email messages that were sent to or from users in your
organization's address book. You can track delivery information about messages sent by or
received from any specific mailbox in your organization. The message's content isn't returned
in the delivery report, but the subject line is displayed in the results. You can track messages for
up to 14 days after they were sent or received.

  ７ Note

  Delivery Reports tracks messages that were sent by people using Microsoft Outlook or
  Outlook on the web. It doesn't track messages sent from POP3 or IMAP4 email clients,
  such as Windows Live Mail or Mozilla Thunderbird.

What do you need to know before you begin?
      Estimated time to complete each procedure: Time to complete will vary based on the
      scope of your search.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Message tracking" entry in the
      Mail flow permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

      Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
      Server   , Exchange Online, or Exchange Online Protection     .

Use the EAC to track messages
   1. In the EAC, navigate to Mail Flow > Delivery Reports.

   2. Enter the following information:

<!-- p.1737 -->

           Mailbox to search: Click Browse to select the mailbox from the address book and
           then click OK. Selecting the mailbox to search is required.

           Select one of the following:

           Search for messages sent to: Use this option to search for messages that were sent
           to specific users from the mailbox you selected in Mailbox to search. Click Select
           users and then pick users from the address book by selecting a user from the list
           and clicking Add. You can select more than one user here. When you're finished
           selecting users, click OK to return to the Delivery Reports page. If you select this
           option, you can also leave the field blank to find messages sent to anyone.

           Search for messages received from: Use this option to search for messages that
           were sent by specific user to the mailbox you selected in Mailbox to search. Again,
           select the user from the address book and click OK to return to the Delivery Reports
           page. If you select this option, you have to specify a sender.

           Search for these words in the subject line: Enter subject line information here, or
           leave it blank.

   3. When you're finished, click Search. If you want to start over, click Clear.

Use the EAC to review a delivery report
To view delivery information, select a message in the Search results pane and click Details       .

The delivery report shows delivery status and detailed delivery information for the message
you have selected from the Search results pane. At the top of the report, you'll see the
following fields:

     Subject: The subject line of the message appears as the heading of the report.

     From: Alias, display name, or email address of the person who sent the message.

     To: Alias, display name, or email address for each recipient of the message.

     Sent: Date and time the message was sent.

Summary to date section
This section appears in the delivery report if a message was sent to more than one recipient.
The top of this section tells you the total number of recipients that the message was sent to
and gives brief delivery information for each recipient.

<!-- p.1738 -->

     Summary to date: Displays total number of recipients, and if there are messages
     Pending, Delivered, or Unsuccessful. Click the hyperlinks to sort by status.

     Search box: The search box is useful if you sent the message to a group of more than 30
     recipients. In the search box, type an email address that you want to get delivery
     information about and click the magnifying glass     .

     To: Shows the email address of the recipient.

     Status: This column displays the status of the message for each recipient.

Detailed report information
This section contains detailed delivery information for a message sent to the recipient you
select in the Summary to date section.

     Delivery Report for: The email address of the selected recipient is shown here.

     Submitted: Date and time that the message was submitted for delivery by the system.

Depending on the delivery status of the message, you may see a variety of status states,
including:

     Delivered: Indicates successful delivery.

     Deferred: Indicates that a message is delayed.

     Pending: If message delivery is pending because a message meets the criteria for an
     organization-wide rule or policy or because it's subject to message approval, the status
     message explains what action a rule is performing or that the message must be approved
     by a moderator before delivery.

     Moderator: The status indicates whether the message was approved or rejected by the
     moderator.

     Groups Expanded: If a message was sent to a group, the individual users are shown in the
     Summary to date section so you can see the delivery status for each recipient. If you
     need to remove or add a user to a group during a delivery report investigation, you can
     modify a group by clicking Edit Groups.

     Failed: Shows the date, time, and reason for a message delivery failure. For example, an
     organization-wide rule may be blocking message delivery or the message couldn't be
     delivered.

<!-- p.1739 -->

When you're done reviewing the report, click Close. Delivery reports aren't saved, but you can
re-run a report at any time. Remember there is a two-week search window.

How do you know this worked?
If your search was successful, messages that fit the search criteria are listed in the Search
results pane. To view the delivery information for a specific message, select it and then click
Details   . If no messages are displayed in the Search results pane, change the search criteria
and then re-run the search.

<!-- p.1740 -->

Connectivity logging in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019         Subscription Edition

Connectivity logging records the outbound connection activity that's used to transmit
messages on Exchange servers. In Exchange Server, the following services transmit messages,
so they have connectivity logs:

      The Transport service on Mailbox servers and Edge Transport servers.

      The Front End Transport service on Mailbox servers.

      The Mailbox Transport Submission service on Mailbox servers.

      The Mailbox Transport Delivery service on Mailbox servers.

For more information about these transport services, and where they can transmit messages,
see Mail flow and the transport pipeline.

Connectivity logging doesn't track the transmission of individual messages. Instead, it tracks
the number and size of messages that were transmitted over a connection, DNS resolution
information for the destination, and informational messages that are related to the connection.

By default, connectivity logging is enabled, and Exchange uses circular logging to limit the
connectivity log files based on size and age to help control the hard disk space that's used. To
configure connectivity logging, see Configure connectivity logging in Exchange Server.

Note: If you're interested in a detailed record of the entire SMTP protocol conversation from
start to finish, see Protocol logging.

Structure of the connectivity log files
By default, the connectivity log files exist in these locations:

      Mailbox servers:

         Transport service: %ExchangeInstallPath%TransportRoles\Logs\Hub\Connectivity

         Front End Transport service:
         %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\Connectivity

         Mailbox Transport Delivery service:
         %ExchangeInstallPath%TransportRoles\Logs\Mailbox\Connectivity\Delivery

<!-- p.1741 -->

          Mailbox Transport Submission service:
           %ExchangeInstallPath%TransportRoles\Logs\Mailbox\Connectivity\Submission

        Edge Transport servers

The naming convention for the connectivity log files is CONNECTLOGyyymmdd-nnnn.log . The
placeholders represent the following information:

        yyyyMMdd is the Coordinated Universal Time (UTC) when the log file was created. yyyy =
        year, MM = month, and dd = day.

        nnnn is an instance number that starts at the value of 1 for each day.

Information is written to the log file until the file reaches its maximum size. Then, a new log file
that has an incremented instance number is opened (the first log file is -1, the next is -2, and so
on). Circular logging deletes the oldest log files when either of the following conditions are
true:

        A log file reaches its maximum age.

        The connectivity log folder reaches its maximum size.

The connectivity log files are text files that contain data in the comma-separated value file
(CSV) format. Each connectivity log file has a header that contains the following information:

        #Software: The value is Microsoft Exchange Server .

        #Version: The value is 15.0.0.0 .

        #Log-Type: The value is Transport Connectivity Log .

        #Date: The UTC date-time when the log file was created. The UTC date-time is
        represented in the ISO 8601 date-time format: yyyy-MM-ddThh:mm:ss.fffZ, where yyyy =
        year, MM = month, dd = day, T indicates the beginning of the time component, hh =
        hour, mm = minute, ss = second, fff = fractions of a second, and Z signifies Zulu, which is
        another way to denote UTC.

        #Fields: Comma delimited field names that are used in the connectivity log files. These
        values are described in the next section.

Fields in the connectivity log files
Connectivity logging stores each outbound connection event on a single line in the log. The
information on each line is organized by fields, and these fields are separated by commas. The
following table describes the fields that are used to classify each outgoing connection event.

<!-- p.1742 -->

                                                                                         ﾉ   Expand table

Field         Description
name

date-time     UTC date-time of the connection event. The UTC date-time is represented in the ISO 8601
              date-time format: yyyy-MM-ddThh:mm:ss.fffZ, where yyyy = year, MM = month, dd = day, T
              indicates the beginning of the time component, hh = hour, mm = minute, ss = second, fff =
              fractions of a second, and Z signifies Zulu, which is another way to denote UTC.

session       A GUID value. The value is the same for every event that's associated with the session, but
              different for each session.

source        One of these values:
                    SMTP for SMTP connections.
                    MapiDelivery for connections from the local mailbox database by the Mailbox
                    Transport Delivery service.
                    MapiSubmission for connections from the local mailbox database by the Mailbox
                    Transport Submission service.

destination   These are some examples of values you'll see here:
                    In the Transport service:
                       The FQDN of the destination messaging server
                       shadowredundancy (on Mailbox servers only)
                    In the Front End Transport service:
                        internalproxy
                        client proxy
                    In the Mailbox Transport Delivery service:
                        The GUID of the destination mailbox database.
                    In the Mailbox Transport Submission service:
                       The GUID of the destination mailbox database.
                        mailboxtransportsubmissioninternalproxy

direction     Single character that represents the start, middle, or end of the connection. The values
              you'll see here are:
                    + : Connect
                    - : Disconnect
                    > : Send

description   Text information that's associated with the connection event. For example:
                     Number and size of messages that were transmitted.
                     DNS MX resource record resolution information for destination domains.
                    DNS resolution information for destination Mailbox servers.
                    Connection establishment messages.
                    Connection failure messages.

<!-- p.1743 -->

The transport services connect to and transmit messages to multiple destinations
simultaneously. Entries in the log file from different connection events are interlaced (they
typically aren't grouped together as one uninterrupted series of connection events). However
you can use the fields (in particular, the unique session field value for a connection) to organize
and arrange the log entries for each separate connection from start to finish.

<!-- p.1744 -->

Configure connectivity logging in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019        Subscription Edition

Connectivity logging records outbound connection activity (source, destination, number and
size of messages, and connection information) for the transport services on Exchange servers.
For more information about connectivity logging, see Connectivity logging in Exchange Server.

What do you need to know before you begin?
      Estimated time to complete: 15 minutes

      You can use the Exchange admin center (EAC) to enable or disable connectivity logging
      and set the log path for the Transport service on Mailbox servers only. For all other
      connectivity logging options in the other transport services, you need to use the
      Exchange Management Shell. For more information about the EAC, see Exchange admin
      center in Exchange Server. To learn how to open the Exchange Management Shell in your
      on-premises Exchange organization, see Open the Exchange Management Shell.

      The folder for connectivity logging needs the following permissions:

         Network Service: Full Control

         System: Full Control

         Administrators: Full Control

      If the folder doesn't exist, but the parent folder has these permissions, the new folder is
      created automatically.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Transport service", "Front End
      Transport service", and "Mailbox Transport service" entries in the Mail flow permissions
      topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

<!-- p.1745 -->

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online       , or Exchange Online Protection .

Use the EAC to configure connectivity logging in
the Transport service on Mailbox servers
   1. In the EAC, go to Servers > Servers.

   2. Select the Mailbox server you want to configure, and then click Edit       .

   3. On the server properties page that opens, click Transport Logs.

   4. In the Connectivity log section, change any of these settings:

           Enable connectivity log: To disable connectivity logging for the Transport service on
           the server, clear the check box. To enable connectivity logging for the Transport
           service on the server, select the check box.

           Connectivity log path: The value you specify must be on the local Exchange server.
           If the folder doesn't exist, it will be created for if the parent folder has the required
           permissions.

     When you're finished, click Save.

Use the Exchange Management Shell to configure
connectivity logging
On Mailbox servers, connectivity logging is available on the following transport services:

     The Transport service (use the Set-TransportService cmdlet).

     The Front End Transport service (use the Set-FrontEndTransportService cmdlet).

     The Mailbox Transport Delivery and Mailbox Transport Submission services (use the Set-
     MailboxTransportService cmdlet to configure both).

On Edge Transport servers, connectivity logging is available on the Transport service (use the
Set-TransportService cmdlet).

To configure connectivity logging, use the following syntax:

  PowerShell

<!-- p.1746 -->

  <Set-TransportService | Set-MailboxTransportService | Set-
  FrontEndTransportService> -Identity <ServerIdentity> -ConnectivityLogEnabled
  <$true | $false> -ConnectivityLogMaxAge <dd.hh:mm:ss> -
  ConnectivityLogMaxDirectorySize <Size> -ConnectivityLogMaxFileSize <Size> -
  ConnectivityLogPath <LocalFilePath>

This example sets the following connectivity log settings in the Transport service on the
Mailbox server named Mailbox01:

     Location of the connectivity log: D:\Connectivity Log\Hub. Note that if the folder doesn't
     exist, it will be created for you if the parent folder has the required permissions.

     Maximum size of a connectivity log file: Sets the maximum size of a connectivity log file
     to 20 MB.

     Maximum size of the connectivity log folder: Sets the maximum size of the connectivity
     log directory to 1.5 GB.

     Maximum age of a connectivity log file: Sets the maximum age of a connectivity log file
     to 45 days.

  PowerShell

  Set-TransportService -Identity Mailbox01 -ConnectivityLogPath "D:\Connectivity
  Log\Hub" -ConnectivityLogMaxFileSize 20MB -ConnectivityLogMaxDirectorySize 1.5GB -
  ConnectivityLogMaxAge 45.00:00:00

For detailed syntax and parameter information, see Set-TransportService, Set-
FrontendTransportService, and Set-MailboxTransportService.

Notes:

     Setting the ConnectivityLogPath parameter to the value $null , effectively disables
     connectivity logging. However, this value generates event log errors if the value of the
     ConnectivityLogEnabled parameter is also $true .

     When you use the ConnectivityLogPath parameter on the Set-MailboxTransportService
     cmdlet, two subfolders are automatically created in the folder you specify:

         Delivery for the Mailbox Transport Delivery service.

         Submission for the Mailbox Transport Submission service.

     Setting the ConnectivityLogMaxAge parameter to the value 00:00:00 prevents the
     automatic removal of connectivity log files because of their age.

<!-- p.1747 -->

How do you know this worked?
To verify that you've successfully configured connectivity logging, use these steps:

   1. Run the following command in the Exchange Management Shell to verify the connectivity
     log settings on the Exchange servers:

        PowerShell

        Write-Host "Front End Transport service:" -ForegroundColor yellow; Get-
        FrontEndTransportService | Format-List Name,ConnectivityLog*; Write-Host
        "Mailbox Transport Submission and Mailbox Transport Delivery services:" -
        ForegroundColor yellow; Get-MailboxTransportService | Format-List
        Name,ConnectivityLog*; Write-Host "Transport service:" -ForegroundColor
        yellow; Get-TransportService | Format-List Name,ConnectivityLog*

   2. Open the location of the connectivity log in Windows Explorer or File Explorer to verify
     that the log files exist, that data is being written to the files, and that the files are being
     recycled based on the maximum file size and maximum directory size values that you
     configured. If you disabled connectivity logging, verify that the log files aren't being
     updated.

<!-- p.1748 -->

Pipeline tracing
Article • 04/30/2025

APPLIES TO:        2016    2019        Subscription Edition

Pipeline tracing captures copies of email messages from a specific sender as they move through the Transport service on Mailbox
servers, the Mailbox Transport Delivery service on Mailbox servers, and through Edge Transport servers. Pipeline tracing captures
verbose information about the changes that each transport agent applies to messages in the transport pipeline in message
snapshot files. By examining the contents of the message snapshot files, you can determine whether the transport agents have
applied the changes to the messages in the transport pipeline that you expected. If you are troubleshooting a problem, you
should determine which transport agent is at fault. Then you can focus your troubleshooting efforts on that agent to resolve the
problem. You can then view the message snapshot files again to verify that your solution is successful.

  ２ Warning

        Pipeline tracing copies the complete contents of email messages that are sent from the sender's email address. To
        avoid unwanted exposure of confidential information, you need to set appropriate security permissions on the pipeline
        tracing folder.
        Don't enable pipeline tracing for long periods of time. Pipeline tracing creates files that can accumulate quickly. Always
        monitor available disk space when pipeline tracing is enabled.

Configure pipeline tracing
Before you enable pipeline tracing, you need to specify the sender's email address you want to monitor. Pipeline tracing is
designed to log messages sent from a specific email address. The sender's email address can be internal or external to your
Exchange organization. Alternatively, you can enable pipeline tracing for system messages generated by the transport service on
the specified Mailbox or Edge Transport server, such as automatic replies, delivery status notification (DSN) messages, journal
reports, and other system-generated messages. You can also modify the location of the pipeline tracing folder.

The parameters that you use to configure pipeline tracing are summarized in the following table:

                                                                                                                         ﾉ   Expand table

 Cmdlet                    Parameter                      Default value                                                      Description

 Set-TransportService      PipelineTracingSenderAddress   Blank ( $null )                                                    Specify the email
                                                                                                                             address of the
 Set-                                                                                                                        sender you want
 MailboxTransportService                                                                                                     to monitor.
                                                                                                                             Specify the value
                                                                                                                             " <> " to monitor
                                                                                                                             system-
                                                                                                                             generated
                                                                                                                             messages sent by
                                                                                                                             the specified
                                                                                                                             transport service
                                                                                                                             on the server.

 Set-TransportService      PipelineTracingPath            Transport service:                                                 The path must be
                                                          %ExchangeInstallPath%TransportRoles\Logs\Hub\PipelineTracing       on the local
 Set-                                                                                                                        server. UNC
 MailboxTransportService                                  Mailbox Transport service:                                         paths aren't
                                                          %ExchangeInstallPath%TransportRoles\Logs\Mailbox\PipelineTracing   supported.
                                                                                                                             The specified
                                                                                                                             path contains the
                                                                                                                             MessageSnapshots
                                                                                                                             folder where

<!-- p.1749 -->

 Cmdlet                        Parameter                Default value                                                  Description

                                                                                                                       pipeline tracing
                                                                                                                       files are stored.

 Set-TransportService          PipelineTracingEnabled   $false                                                         You can only
                                                                                                                       enable pipeline
 Set-                                                                                                                  tracing for the
 MailboxTransportService                                                                                               specified
                                                                                                                       transport service
                                                                                                                       on the server
                                                                                                                       after you
                                                                                                                       configure the
                                                                                                                       sender address
                                                                                                                       you want to
                                                                                                                       monitor.

For more information about how to enable pipeline tracing and configure the sender address for pipeline tracing, see Configure
pipeline tracing.

Message snapshot files
Message snapshots are files that capture any changes made to a message by transport agents in the Transport service or the
Mailbox Transport Delivery service. These files are stored in the MessageSnapshots folder in the corresponding pipeline tracing
path for the transport service.

In the MessageSnapshots folder, Exchange creates one folder for each message sent by the monitored sender that flows through
the specified transport service. Each folder is named after a GUID that's assigned to the message. If you enable pipeline tracing
for the Transport service and the Mailbox Transport service on the same Mailbox server, a different GUID is assigned to the same
message by each transport service, so the folder name for a message in the MessageSnapshots folder for the Transport service is
different than the folder name for the same message in the MessageSnapshots folder for the Mailbox Transport service. If you
enable pipeline tracing on more than one Exchange server, a different GUID is assigned to the same message as it travels through
the specified transport service on each Exchange server.

In each message folder, Exchange creates several message snapshot files that have .eml file extensions. These message snapshot
files contain the contents of the message as it encounters each SMTP event and transport agent.

If a transport agent is registered on an SMTP event, Exchange creates a message snapshot of the message before the message
encounters any transport agents. This gives you a copy of the message before the message encounters transport agents that are
registered on that event. Then, a new message snapshot is created for each transport agent that the message encounters,
regardless of whether a transport agent modifies the contents of the message. However, if no agents are registered on an event,
Exchange doesn't create any message snapshots for that event.

For example, if three agents are registered on the OnEndofData event but only two of the transport agents modify a message,
four message snapshots are created. The first message snapshot captures the message as it encounters the OnEndofData event
before any modifications that are made by the transport agents that registered on that event. Then, one message snapshot is
created for each transport agent regardless of whether a transport agent modifies the message.

The message snapshot files that are created are described in the following list:

        Original.eml: This file contains the original unmodified contents of the email message before it encounters any SMTP events
        or transport agents.

        Routingnnnn.eml: These files contain the contents of the email message as it encounters the transport SMTP events and
        transport agents registered on those events in the categorization part of the Transport service. The placeholder nnnn
        represents an integer value that starts with 0001 . The value is incremented for every SMTP event and transport agent
        registered on those events in the order in which the events and agents act on the message. The Mailbox Transport Delivery
        service doesn't generate these Routing snapshot files.

<!-- p.1750 -->

     SmtpReceivennnn.eml: These files contain the contents of the email message as it encounters the OnEndofData and
     OnEndOfHeaders SMTP events and transport agents registered on those events during the SMTP receive part of the
     Transport service or the Mailbox Transport Delivery service. The placeholder nnnn represents an integer value that starts
     with 0001 . The value is incremented for every SMTP event and transport agent registered on those events in the order in
     which the events and agents act on the message.

You can open the message snapshot files by using Notepad or any text editor.

Each message snapshot file starts with headers that are added to the message contents and list the SMTP event and transport
agent that the message snapshot file relates to. These headers start with X-CreatedBy: MessageSnapshot-Begin injected headers
and end with X-EndOfInjectedXHeaders: MessageSnapshot-End injected headers . These headers are replaced in each message
snapshot file by each subsequent transport agent and SMTP event. The following is an example of the headers that are added to
an email message file:

  Console

  X-CreatedBy: MessageSnapshot-Begin injected headers
  X-MessageSnapshot-UTC-Time: 2013-01-23T23:20:18.138Z
  X-MessageSnapshot-Record-Id: 21474836486
  X-MessageSnapshot-Source: OnSubmittedMessageX-Sender: michelle@nwtraders.com
  X-Receiver: chris@contoso.com
  X-EndOfInjectedXHeaders: MessageSnapshot-End injected headers

After the message snapshot headers, the file contains the contents of the message including all the original message headers. If a
transport agent modifies the contents of the message, the changes appear integrated with the message. As the message is
processed by each transport agent, the changes that are made by each agent are applied to the message contents. If a transport
agent makes no changes to the message contents, the message snapshot that is created by that agent will be identical to the
message snapshot created by the previous transport agent.

<!-- p.1751 -->

Exchange Server: Configure pipeline
tracing
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Pipeline tracing captures copies of email messages as they move through the transport
pipeline in the Transport service or the Mailbox Transport service on Mailbox server and on
Edge Transport servers.

What do you need to know before you begin?
      Estimated time to complete this procedure: 15 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Transport Service" and "Mailbox
      Transport Service" entries in the Mail flow permissions topic.

      You can only use the Exchange Management Shell to perform this procedure.

      Pipeline tracing copies the complete contents of email messages that are sent from the
      sender's email address. To avoid unwanted exposure of confidential information, you
      need to set appropriate security permissions on the location of the pipeline tracing folder.

      Don't enable pipeline tracing for long periods of time. Pipeline tracing creates multiple
      message snapshot files that accumulate quickly. Always monitor available disk space
      when pipeline tracing is enabled.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server .

Enable and configure pipeline tracing

<!-- p.1752 -->

Step 1: Use the Exchange Management Shell to
configure the pipeline tracing sender address
Use the following syntax to configure the pipeline tracing sender address.

  PowerShell

  <Set-TransportService | Set-MailboxTransportService> <ServerIdentity> -
  PipelineTracingSenderAddress <SMTPAddress | "<>">

This example configures pipeline tracing to capture snapshots of all messages sent by the
sender chris@contoso.com in the Transport service on the Mailbox server named Mailbox01.

  PowerShell

  Set-TransportService Mailbox01 -PipelineTracingSenderAddress chris@contoso.com

This example configures pipeline tracing to capture snapshots of all the system-generated
messages received by the Transport service on the Mailbox server named Mailbox02.

  PowerShell

  Set-TransportService Mailbox02 -PipelineTracingSenderAddress "<>"

  ２ Warning

  Configuring pipeline tracing to capture all server-generated messages in a transport
  service may place a significant load on the server and may quickly consume available disk
  space. Always monitor available disk space when pipeline tracing is enabled.

Step 2: (Optional) Use the Exchange Management
Shell to specify a custom pipeline tracing folder
The default pipeline tracing folder doesn't exist until after you enable pipeline tracing, and
messages that meet the criteria you specify using the PipelineTracingSenderAddress parameter
flow through the transport service on the server. For the Transport service on a Mailbox server,
the default location is %ExchangeInstallPath%TransportRoles\Logs\Hub\PipelineTracing . For the
Mailbox Transport service on a Mailbox server, the default location is

<!-- p.1753 -->

%ExchangeInstallPath%TransportRoles\Logs\Mailbox\PipelineTracing . If you specify a custom

path, the path must be on the local Exchange server.

Use the following syntax to configure the pipeline tracing folder.

  PowerShell

  <Set-TransportService | Set-MailboxTransportService> <ServerIdentity> -
  PipelineTracingPath <LocalFilePath>

This example sets the pipeline tracing folder for the Transport service on the server named
Mailbox01 to D:\\Hub\\Pipeline Tracing .

  PowerShell

  Set-TransportService Mailbox01 -PipelineTracingPath "D:\Hub\Pipeline Tracing"

Step 3: Use the Exchange Management Shell to
enable pipeline tracing
By default, pipeline tracing is disabled on all Exchange servers. When you enable pipeline
tracing, you are enabling pipeline tracing in the specified transport service on the specified
Exchange server only. Before you enable pipeline tracing, you need to specify the sender
address as described in Step 1.

Use the following syntax to enable pipeline tracing.

  PowerShell

  <Set-TransportService | Set-MailboxTransportService> <ServerIdentity> -
  PipelineTracingEnabled $true

This example enables pipeline tracing in the Transport service on the Mailbox server named
Mailbox01.

  PowerShell

  Set-TransportService Mailbox01 -PipelineTracingEnabled $true

How do you know this worked?

To verify that you have successfully configured pipeline tracing, do the following:

<!-- p.1754 -->

   1. Run the following command:

        PowerShell

        <Get-TransportService | Get-MailboxTransportService> <ServerIdentity> |
        Format-List PipelineTracing*

   2. Verify the values displayed are the values you configured.

   3. Check the pipeline tracing folder for the Transport service or the Mailbox Transport
     service, and verify message snapshot files are being created in the folder.

Disable pipeline tracing
Because of the disk space and security concerns associated with pipeline tracing, pipeline
tracing is a temporary action for diagnostic or troubleshooting purposes. Whenever you enable
pipeline tracing, always remember to disable it when you are finished.

Use the following syntax to disable pipeline tracing.

  PowerShell

  <Set-TransportService | Set-MailboxTransportService> <ServerIdentity> -
  PipelineTracingEnabled $false

This example disables pipeline tracing in the Transport service on the Mailbox server named
Mailbox01.

  PowerShell

  Set-TransportService Mailbox01 -PipelineTracingEnabled $false

How do you know this worked?

To verify that you have successfully disabled pipeline tracing, do the following:

   1. Run the following command:

        PowerShell

        <Get-TransportService | Get-MailboxTransportService> <ServerIdentity> |
        Format-List PipelineTracingEnabled

   2. Verify the value of the PipelineTracingEnabled parameter is $false.

<!-- p.1755 -->

3. Check the pipeline tracing folder, and verify message snapshot files are no longer being
  created in the folder.

<!-- p.1756 -->

Queues and messages in queues in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

A queue is a temporary holding location for messages that are waiting to enter the next stage of processing or delivery to a destination. Each
queue represents a logical set of messages that the Exchange server processes in a specific order. In Exchange 2016 and Exchange 2019, queues
hold messages before, during, and after delivery. Queues exist in the Transport service on Mailbox servers and on Edge Transport servers. Mailbox
servers and Edge Transport servers are called transport servers throughout this topic.

Like all previous versions of Exchange, a single Extensible Storage Engine (ESE) database is used for queue storage.

You can manage queues and messages in queues by using the Exchange Management Shell and Queue Viewer in the Exchange Toolbox. You can
use these interfaces to view the status and contents of queues and detailed message properties. You can also perform actions that modify queues
or the messages in queues. For more information, see Procedures for queues and Procedures for messages in queues.

Types of queues
The following types of queues are used in Exchange 2016 and Exchange 2019, which are the same as Exchange 2013:

                                                                                                                                                   ﾉ   Expand table

 Queue             Server role         Description

 Delivery          Mailbox servers     Holds messages that are being delivered to all internal and external destinations.
 queues            and Edge            Delivery queues are dynamically created when they're required, and are automatically deleted when the queue is empty and
                   Transport servers   the expiration time has passed. The queue expiration time is controlled by the QueueMaxIdleTime parameter on the Set-
                                       TransportService cmdlet. The default value is three minutes.

                                       On Edge Transport servers, there's a queue for every unique destination SMTP domain or smart host.

                                       On Mailbox servers, there's a queue for every unique destination as indicated by the NextHopSolutionKey property. For
                                       more information, see the NextHopSolutionKey section later in this topic.

                                       All messages are transmitted between Exchange 2016 and Exchange 2013 servers by using SMTP. Non-SMTP destinations
                                       also use delivery queues if the destination is serviced by a Delivery Agent connector. For more information, see Delivery
                                       Agents and Delivery Agent Connectors.

 Poison            Mailbox servers     Isolates messages that contain errors and are determined to be harmful to Exchange after a server or service failure. The
 message           and Edge            messages may be genuinely harmful in their content and format, or the messages might have been the victims of a poorly
 queue             Transport servers   written transport agent or a software bug that crashed the Exchange server while it was processing the otherwise valid
                                       messages.
                                       The poison message queue is typically empty. If the poison message queue contains no messages, then it doesn't appear in
                                       the queue management tools. Messages in the poison message queue are never automatically resumed or expired.
                                       Messages remain in the poison message queue until they're manually resumed or removed by an administrator.

                                       Every Mailbox server or Edge Transport server has only one poison message queue.

 Shadow            Mailbox servers     Shadow queues hold redundant copies of messages while the messages are in transit. For more information, see Shadow
 queues                                redundancy in Exchange Server.

 Submission        Mailbox servers     Holds messages that have been accepted by the Transport service, but haven't been processed. Messages in the Submission
 queue             and Edge            queue are either waiting to be processed, or are actively being processed.
                   Transport servers   On Mailbox servers, messages are received by a Receive connector, the Pickup or Replay directories, or the Mailbox
                                       Transport Submission service. On Edge Transport servers, messages are typically received by a Receive connector, but the
                                       Pickup and Replay directories are also available.

                                       The categorizer retrieves messages from this queue and, among other things, determines the location of the recipient and
                                       the route to that location. After categorization, the message is moved to a delivery queue or to the Unreachable queue. For
                                       more information about the categorizer and the transport pipeline, see Mail flow and the transport pipeline.

                                       Every Mailbox server or Edge Transport server has only one Submission queue.

 Unreachable       Mailbox servers     Contains messages that can't be routed to their destinations. Typically, an unreachable destination is caused by
 queue             and Edge            configuration changes that have modified the routing path for delivery. Regardless of destination, all messages that have
                   Transport servers   unreachable recipients reside in this queue.
                                       Every Mailbox server or Edge Transport server has only one Unreachable queue.

Queue database files

<!-- p.1757 -->

All the different queues are stored in a single ESE database. By default, this queue database is located on the transport server at
%ExchangeInstallPath%TransportRoles\data\Queue .

Like any ESE database, the queue database uses log files to accept, track, and maintain data. To enhance performance, all message transactions
are written first to log files and memory, and then to the database file. The checkpoint file tracks the transaction log entries that have been
committed to the database. During an ordinary shutdown of the Microsoft Exchange Transport service, uncommitted database changes that are
found in the transaction logs are committed to the database.

Circular logging is used for the queue database. This means that transaction logs that are older than the current checkpoint are immediately and
automatically deleted. Therefore, the transaction logs can't be replayed for queue database recovery from backup.

The following table lists the files that constitute the queue database.

                                                                                                                                                           ﾉ    Expand table

 File              Description

 Mail.que          This queue database file stores all the queued messages.

 Tmp.edb           This temporary database file is used to verify the queue database schema on startup.

 Trn*.log          Transaction logs record all changes to the queue database. Changes to the database are first written to the transaction log and then committed to
                   the database. Trn.log is the current active transaction log file. Trntmp.log is the next provisioned transaction log file that's created in advance. If the
                   existing Trn.log transaction log file reaches its maximum size, Trn.log is renamed to Trn nnnn.log, where nnnn is a sequence number. Trntmp.log is
                   then renamed Trn.log and becomes the current active transaction log file.

 Trn.chk           This checkpoint file tracks the transaction log entries that have been committed to the database. This file is always in the same location as the
                   mail.que file.

 Trnres00001.jrs   These reserve transaction log files act as placeholders. They're only used when the hard disk that contains the transaction log runs out of space to
 Trnres00002.jrs   stop the queue database cleanly.

Exchange uses generation tables for storage and clean-up of messages in the queue database. Instead of processing and deleting individual
message records from one large table, the queue database stores messages in time-based tables, and only deletes the entire table after all the
messages in the table have been successfully processed. For example, consider the following example:

        All messages queued from 1:00 PM to 2:00 PM, regardless of the queue or destination, are stored in the 1p-2p_msgs table.

        At 2:00 PM, new messages are stored in the 2p-3p_msgs table.

        At 4:00 PM, a new table named 4p-5p_msgs is created. The entire 1p-2p_msgs table is deleted, but only if all messages in the table have been
        successfully processed.

This approach of deleting entire messages tables instead of individual messages helps improves the I/O performance of the drive that holds the
queue database.

Options for configuring the queue database
You configure the queue database by adding or modifying keys in the %ExchangeInstallPath%Bin\EdgeTransport.exe.config XML application
configuration file. This file is associated with the Microsoft Exchange Transport service. Changes you make to the EdgeTransport.exe.config file take
effect after you restart the Microsoft Exchange Transport service.

  ７ Note

  Any customized per-server Exchange or Internet Information Server settings you make in exExchangeNoVersion XML application
  configuration files (for example, web.config files or the EdgeTransport.exe.config file) will be overwritten when you install an
  exExchangeNoVersion Cumulative Update (CU). Make sure that you save this information so that you can easily re-configure your server after
  the install. You must re-configure these settings after you install an exExchangeNoVersion CU.

The <appSettings> section of the EdgeTransport.exe.config file is where you can add new keys or modify existing keys. If a specific key doesn't
exist, you can add it manually to change its value.

The keys for the queue database that are available in the EdgeTransport.exe.config file are described in the following table.

                                                                                                                                                           ﾉ    Expand table

<!-- p.1758 -->

 Key                                         Default value                                    Description

 QueueDatabaseBatchSize                      40                                               Specifies the number of database I/O operations that can be
                                                                                              grouped together before they're executed.
                                                                                              By default, this key doesn't exist in the EdgeTransport.exe.config
                                                                                              file.

 QueueDatabaseBatchTimeout                   100                                              Specifies the maximum time in milliseconds that the database
                                                                                              will wait for multiple database I/O operations to group before it
                                                                                              executes them. The database I/O operations are executed
                                                                                              without waiting for any more if the following conditions are true:
                                                                                                   The number of database I/O operations that's specified by
                                                                                                      the QueueDatabaseBatchSize key hasn't been reached.
                                                                                                      The time specified by the QueueDatabaseBatchTimeout
                                                                                                      key has passed.

                                                                                              By default, this key doesn't exist in the EdgeTransport.exe.config
                                                                                              file.

 QueueDatabaseMaxConnections                 4                                                Specifies the number of ESE database connections that can be
                                                                                              open.

 QueueDatabaseLoggingBufferSize              5MB                                              Specifies the memory that's used to cache the transaction
                                                                                              records before they're written to the transaction log file.

 QueueDatabaseLoggingFileSize                5MB                                              Specifies the maximum size of a transaction log file. When the
                                                                                              maximum log file size is reached, a new log file is opened.

 QueueDatabaseLoggingPath                    %ExchangeInstallPath%TransportRoles\data\Queue   Specifies the default directory for the queue database log files.
                                                                                              For instructions on how to change the location of the queue
                                                                                              database, see Change the location of the queue database.

 QueueDatabaseMaxBackgroundCleanupTasks      32                                               Specifies the maximum number of background cleanup work
                                                                                              items that can be queued to the database engine thread pool at
                                                                                              any time.

 QueueDatabaseOnlineDefragEnabled            True                                             Enables or disables scheduled online defragmentation of the
                                                                                              mail queue database.
                                                                                              By default, this key doesn't exist in the EdgeTransport.exe.config
                                                                                              file.

 QueueDatabaseOnlineDefragSchedule           1:00:00 or 1:00 A.M.                             Specifies the time of day in 24 hour format to start the online
                                                                                              defragmentation of the mail queue database. To specify a value,
                                                                                              enter the value as a time span: hh:mm:ss, where h = hours, m =
                                                                                              minutes, and s = seconds.

 QueueDatabaseOnlineDefragTimeToRun          3:00:00 or 3 hours                               Specifies the length of time the online defragmentation task is
                                                                                              allowed to run. Even if the defragmentation task doesn't finish in
                                                                                              the time specified, the queue database is left in a consistent
                                                                                              state. To specify a value, enter the value as a time span:
                                                                                              hh:mm:ss, where h = hours, m = minutes, and s = seconds.

 QueueDatabasePath                           %ExchangeInstallPath%TransportRoles\data\Queue   Specifies the default directory for the queue database files. For
                                                                                              instructions on how to change the location of the queue
                                                                                              database, see Change the location of the queue database.

Queue properties
A queue has many properties that describe the purpose and status of the queue. Some queue properties are applied to the queue when the
queue is created, and don't change. Other properties contain status, size, time, or other indicators that are updated frequently.

NextHopSolutionKey
The routing component of the categorizer in the Microsoft Exchange Transport service selects the destination for a message, and this destination
is used to create the delivery queue. The destination is stamped on every recipient as the NextHopSolutionKey property. Every unique value of
the NextHopSolutionKey property corresponds to a separate delivery queue.

The NextHopSolutionKey property contains the following fields:

       DeliveryType: Represents the results of the categorization of the message, and how the Transport service intends to transmit the message to
       the next hop, which could be the ultimate destination of the message, or an intermediate hop along the way. The Transport service uses a
       predefined list of values for DeliveryType.

<!-- p.1759 -->

     Based on the value of DeliveryType, the NextHopCategory property is added to the queue:

          The value External indicates the next hop for the queue is outside the Exchange organization.

          The value Internal indicates the next hop for the queue is inside the Exchange organization.

          Note that a message for an external recipient may require one or more internal hops before the message is delivered externally.

     NextHopDomain: Uses specific values based on the value of the DeliveryType field. For delivery queues, the value of this field is effectively
     the name of the queue.

     The value of NextHopDomain isn't always a domain name. For example, the value could be the name of the target Active Directory site or
     database availability group (DAG). Think of this field as the next hop name.

     NextHopConnector: Uses specific values based on the value of the DeliveryType field. The value is always expressed as a GUID. If this field
     isn't used, the value is a GUID with all zeroes.

     The value of NextHopConnector isn't always the GUID of a connector. For example, the value could be the GUID of the target Active
     Directory site or DAG. Think of this field as the next hop GUID.

The values of DeliveryType, NextHopCategory, NextHopDomain and NextHopConnector are described in the following table.

                                                                                                                                          ﾉ   Expand table

 Delivery Type in Queue        DeliveryType in the Exchange         Description             NextHopCategory   NextHopDomain
 Viewer                        Management Shell

 Delivery Agent                DeliveryAgent                        The queue holds         External          This value is the destination address space that's
                                                                    messages for                              configured on the Delivery Agent connector. For
                                                                    delivery to                               example, MOBILE .
                                                                    recipients in a non-
                                                                    SMTP address
                                                                    space that's
                                                                    serviced by a
                                                                    delivery agent and a
                                                                    Delivery Agent
                                                                    connector. The
                                                                    connector has the
                                                                    local Mailbox server
                                                                    configured as a
                                                                    source server. For
                                                                    more information,
                                                                    see Delivery Agents
                                                                    and Delivery Agent
                                                                    Connectors.

 DnsConnectorDelivery          DnsConnectorDelivery                 The queue holds         External          This value is the destination address space that's
                                                                    messages for                              configured on the Send connector. For example,
                                                                    delivery to                               contoso.com .
                                                                    recipients in an
                                                                    SMTP domain. The
                                                                    Send connector that
                                                                    services the domain
                                                                    has the local
                                                                    transport server
                                                                    configured as
                                                                    source server, and
                                                                    the Send connector
                                                                    is configured to use
                                                                    DNS routing.

 Heartbeat                     Heartbeat                            This value is           n/a               n/a
                                                                    reserved for internal
                                                                    Microsoft use. For
                                                                    more information
                                                                    about heartbeat,
                                                                    see Shadow
                                                                    redundancy in
                                                                    Exchange Server.

 MapiDelivery                  MapiDelivery                         Note: This value        n/a               n/a
                                                                    isn't used by
                                                                    Exchange 2013 or
                                                                    later. It's included

<!-- p.1760 -->

Delivery Type in Queue       DeliveryType in the Exchange   Description             NextHopCategory   NextHopDomain
Viewer                       Management Shell

                                                            for backwards
                                                            compatibility with
                                                            Exchange 2010.

                                                            The queue holds
                                                            messages for
                                                            delivery by an
                                                            Exchange 2010 Hub
                                                            Transport server to
                                                            a mailbox on an
                                                            Exchange 2010
                                                            Mailbox server in
                                                            the local Active
                                                            Directory site.

NonSmtpGatewayDelivery       NonSmtpGatewayDelivery         The queue holds         External          This value is the destination address space that's
                                                            messages for                              configured on the Foreign connector. For example,
                                                            delivery to                               FAX .
                                                            recipients in a non-
                                                            SMTP address
                                                            space that's
                                                            serviced by a
                                                            Foreign connector.
                                                            The connector has
                                                            the local Mailbox
                                                            server configured as
                                                            a source server. For
                                                            more information,
                                                            see Foreign
                                                            Connectors.

Shadow Redundancy            ShadowRedundancy               The queue holds         Internal          This value is the FQDN of the primary transport
                                                            messages in a                             server for which the shadow queue is holding
                                                            shadow queue. A                           redundant copies of the primary messages. For
                                                            shadow queue                              example, mailbox01.contoso.com .
                                                            holds redundant
                                                            copies messages in
                                                            transit in case the
                                                            primary messages
                                                            aren't successfully
                                                            delivered. For more
                                                            information, see
                                                            Shadow
                                                            redundancy in
                                                            Exchange Server.

SmartHostConnectorDelivery   SmartHostConnectorDelivery     The queue holds         External          This value is the list of smart hosts that are
                                                            messages for                              configured on the Send connector. Smart hosts can
                                                            delivery to                               be configured as FQDNs, IP addresses or both. The
                                                            recipients in an                          values can be one of the following:
                                                            SMTP domain. The                          FQDN: The syntax is <FQDN1,FQDN2,...> . For
                                                            Send connector that                       example, smarthost01.contoso.com or
                                                            services the domain                       smarthost01.contoso.com,smarthost02.fabrikam.com
                                                            has the local
                                                            transport server                          IP address: The syntax is <[IPAddress1],
                                                            configured as                             [IPAddress2],...> . For example, [10.10.10.100] o
                                                            source server, and                        [10.10.10.100],[10.10.10.101] .
                                                            the Send connector
                                                            is configured to use                      FQDN and IP address: The syntax is
                                                            smart host routing.                       <[IPAddress1],FQDN1,...> , and depends on how
                                                                                                      the smart hosts are listed on the Send connector.
                                                                                                      For example,
                                                                                                      [172.17.17.7],relay.tailspintoys.com or
                                                                                                      mail.contoso.com,[192.168.1.50] .

SMTP Delivery to Ex Online   SmtpDeliveryToExo              This value isn't used   n/a               n/a
                                                            in on-premises
                                                            Exchange.

SMTP Delivery to Mailbox     SmtpDeliveryToMailbox          The queue holds         Internal          This value is the name of the destination mailbox
                                                            messages for                              database. For example, Mailbox Database
                                                            delivery to                               0471695037 .
                                                            Exchange 2013 or
