---
title: "Exchange Server — pages 1921-1960"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1921-1960
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1921-1960
family: exchange
documentKind: "doc"
abstract: "Number of uncommitted message queue database transactions in memory Resource: UsedVersionBuckets[%ExchangeInstallPath%TransportRoles\\data\\Queue\\mail.queue] Description: Monitors the number of uncommitted transactions for the message queue database that exist in memory. Pressure"
---

# Exchange Server — pages 1921-1960

<!-- p.1921 -->

Number of uncommitted message queue database transactions in
memory
Resource: UsedVersionBuckets[%ExchangeInstallPath%TransportRoles\data\Queue\mail.queue]

Description: Monitors the number of uncommitted transactions for the message queue database that exist
in memory.

Pressure transitions:

     LowToMedium: 999
     MediumToHigh: 1500
     HighToMedium: 1000
     MediumToLow: 800

Comments::

A list of changes that are made to the message queue database is kept in memory until those changes can
be committed to a transaction log. Then the list is committed to the message queue database itself. These
outstanding message queue database transactions that are kept in memory are known as version buckets.
The number of version buckets may increase to unacceptably high levels because of an unexpectedly high
volume of incoming messages, spam attacks, problems with the message queue database integrity, or hard
drive performance.

When version buckets are under pressure, the Exchange server throttles incoming connections by delaying
acknowledgment of incoming messages. Exchange reduces the rate of incoming message flow by tarpitting,
which delays the acknowledgment of the SMTP MAIL FROM command to the sending server. If the resource
pressure condition continues, Exchange gradually increases the tarpitting delay. After the resource utilization
returns to normal, Exchange gradually reduces the acknowledgement delay and eases back into normal
operation. By default, Exchange delays message acknowledgments for 10 seconds when under resource
pressure. If the pressure continues, the delay is increased in 5-second increments up to 55 seconds.

When the version buckets are under high pressure, the Exchange server also stops processing outgoing
messages.

Exchange keeps a history of version bucket resource utilization. If the resource utilization doesn't go down to
the low level for a specific number of polling intervals, known as the history depth, Exchange stops the
tarpitting delay and rejects incoming messages until the resource utilization goes back to the low level. By
default, the history depth for version buckets is in 10 polling intervals.

Actions taken by back pressure when resources are
under pressure
The following table summarizes the actions taken by back pressure when a monitored resource is under
pressure.

                                                                                              ﾉ   Expand table

<!-- p.1922 -->

Resource under pressure        Utilization   Actions taken
                               level

DatabaseUsedSpace              Medium        Reject incoming messages from non-Exchange servers.
                                             Reject message submissions from the Pickup directory and the
                                             Replay directory.

                                             Message resubmission is paused.

                                             Shadow Redundancy rejects messages. For more information
                                             about Shadow Redundancy, see Shadow redundancy in
                                             Exchange Server.

DatabaseUsedSpace              High          All actions taken at the medium utilization level.
                                             Reject incoming messages from other Exchange servers.

                                             Reject message submissions from mailbox databases by the
                                             Microsoft Exchange Mailbox Transport Submission service on
                                             Mailbox servers.

PrivateBytes                   Medium        Reject incoming messages from non-Exchange servers.
                                             Reject message submissions from the Pickup directory and the
                                             Replay directory.

                                             Message resubmission is paused.

                                             Shadow Redundancy rejects messages.

                                             Processing messages after a server or Transport service restart
                                             (also known as boot scanning) is paused.

                                             Start message dehydration.

PrivateBytes                   High          All actions taken at the medium utilization level.
                                             Reject incoming messages from other Exchange servers.

                                             Reject message submissions from mailbox databases by the
                                             Microsoft Exchange Mailbox Transport Submission service on
                                             Mailbox servers.

QueueLength[SubmissionQueue]   Medium        Introduce or increment the tarpitting delay to incoming
                                             messages. If normal level isn't reached for the entire
                                             Submission queue history depth, take the following actions:
                                                   Reject incoming messages from non-Exchange servers.
                                                   Reject message submissions from the Pickup directory
                                                   and the Replay directory.
                                                   Message resubmission is paused.
                                                   Shadow Redundancy rejects messages.
                                                   Boot scanning is paused.

QueueLength[SubmissionQueue]   High          All actions taken at the medium utilization level.
                                             Reject incoming messages from other Exchange servers.

                                             Reject message submissions from mailbox databases by the
                                             Microsoft Exchange Mailbox Transport Submission service on
                                             Mailbox servers.

                                             Flush enhanced DNS cache from memory.

<!-- p.1923 -->

Resource under pressure              Utilization   Actions taken
                                     level

                                                   Start message dehydration.

SystemMemory                         Medium        Start message dehydration.
                                                   Flush caches.

SystemMemory                         High          All actions taken at the medium utilization level.

UsedDiskSpace (message queue         Medium        Reject incoming messages from non-Exchange servers.
database transaction logs)                         Reject message submissions from the Pickup directory and the
                                                   Replay directory.

                                                   Message resubmission is paused.

                                                   Shadow Redundancy rejects messages.

UsedDiskSpace (message queue         High          All actions taken at the medium utilization level.
database transaction logs)                         Reject incoming messages from other Exchange servers.

                                                   Reject message submissions from mailbox databases by the
                                                   Microsoft Exchange Mailbox Transport Submission service on
                                                   Mailbox servers.

UsedDiskSpace (content conversion)   Medium        Reject incoming messages from non-Exchange servers.
                                                   Reject message submissions from the Pickup directory and the
                                                   Replay directory.

UsedDiskSpace (content conversion)   High          All actions taken at the medium utilization level.
                                                   Reject incoming messages from other Exchange servers.

                                                   Reject message submissions from mailbox databases by the
                                                   Microsoft Exchange Mailbox Transport Submission service on
                                                   Mailbox servers.

UsedVersionBuckets                   Medium        Introduce or increment the tarpitting delay to incoming
                                                   messages. If normal level isn't reached for the entire version
                                                   bucket history depth, take the following actions:
                                                         Reject incoming messages from non-Exchange servers.
                                                         Reject message submissions from the Pickup directory
                                                         and the Replay directory.

UsedVersionBuckets                   High          All actions taken at the medium utilization level.
                                                   Reject incoming messages from other Exchange servers.

                                                   Reject message submissions from mailbox databases by the
                                                   Microsoft Exchange Mailbox Transport Submission service on
                                                   Mailbox servers.

                                                   Stop processing outgoing messages.

                                                   Remote delivery is paused.

View back pressure resource thresholds and utilization
levels

<!-- p.1924 -->

You can use the Get-ExchangeDiagnosticInfo cmdlet in the Exchange Management Shell to view the
resources that are being monitored, and the current utilization levels. To learn how to open the Exchange
Management Shell in your on-premises Exchange organization, see Open the Exchange Management Shell.

To view the back pressure settings on an Exchange server, run the following command:

  PowerShell

  [xml]$bp=Get-ExchangeDiagnosticInfo [-Server <ServerIdentity> ] -Process EdgeTransport -
  Component ResourceThrottling;
  $bp.Diagnostics.Components.ResourceThrottling.ResourceTracker.ResourceMeter

To see the values on the local server, you can omit the Server parameter.

Back pressure configuration settings in the
EdgeTransport.exe.config file
All configuration options for back pressure are done in the
%ExchangeInstallPath%Bin\EdgeTransport.exe.config XML application configuration file. However, few of the

settings exist in the file by default.

  Ｕ Caution

  These settings are listed only as a reference for the default values. We strongly discourage any
  modifications to the back pressure settings in the EdgeTransport.exe.config file. Modifications to these
  settings might result in poor performance or data loss. We recommend that you investigate and correct
  the root cause of any back pressure events that you may encounter.

General back pressure settings

                                                                                                   ﾉ   Expand table

 Key name                                                                Default value

 ResourceMeteringInterval                                                   00:00:02 (2 seconds)

 DehydrateMessagesUnderMemoryPressure                                    true

DatabaseUsedSpace settings

                                                                                                   ﾉ   Expand table

 Key name                                                               Default value (%)

 DatabaseUsedSpace.LowToMedium                                          96

 DatabaseUsedSpace.MediumToHigh                                         99

<!-- p.1925 -->

Key name                                              Default value (%)

DatabaseUsedSpace.HighToMedium                        97

DatabaseUsedSpace.MediumToLow                         94

PrivateBytes settings

                                                                               ﾉ    Expand table

Key name                                    Default value (%)

PrivateBytes.LowToMedium                    72

PrivateBytes.MediumToHigh                   75

PrivateBytes.HighToMedium                   73

PrivateBytes.MediumToLow                    71

PrivateBytesHistoryDepth                    30

QueueLength[SubmissionQueue] settings

                                                                               ﾉ    Expand table

Key name                                                   Default value

QueueLength[SubmissionQueue].LowToMedium                   9999

QueueLength[SubmissionQueue].MediumToHigh                  15000

QueueLength[SubmissionQueue].HighToMedium                  10000

QueueLength[SubmissionQueue].MediumToLow                   2000

SubmissionQueueHistoryDepth                                300 (after 10 minutes)

SystemMemory settings

                                                                               ﾉ    Expand table

Key name                                         Default value (%)

SystemMemory.LowToMedium                         88

SystemMemory.MediumToHigh                        94

SystemMemory.HighToMedium                        89

SystemMemory.MediumToLow                         84

<!-- p.1926 -->

UsedDiskSpace settings (message queue database transaction logs)

                                                                                                ﾉ   Expand table

Key name                                                                                   Default value (%)

UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data\Queue].LowToMedium                  89

UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data\Queue].MediumToHigh                 99

UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data\Queue].HighToMedium                 90

UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data\Queue].MediumToLow                  80

 ７ Note

 Values that contain only UsedDiskSpace (for example, UsedDiskSpace.MediumToHigh ) apply to the
 message queue database transaction logs and to content conversion.

UsedDiskSpace settings (content conversion)

                                                                                                ﾉ   Expand table

Key name                                                               Default value (%)

UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data].LowToMedium    89

UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data].MediumToHigh   99

UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data].HighToMedium   90

UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data].MediumToLow    80

TemporaryStoragePath                                                   %ExchangeInstallPath%TransportRoles\data\Temp

UsedVersionBuckets settings

                                                                                                ﾉ   Expand table

Key name                                                                       Default value

UsedVersionBuckets.LowToMedium                                                 999

UsedVersionBuckets.MediumToHigh                                                1500

UsedVersionBuckets.HighToMedium                                                1000

UsedVersionBuckets.MediumToLow                                                 800

VersionBucketsHistoryDepth                                                     10

<!-- p.1927 -->

Back pressure logging information
The following list describes the event log entries that are generated by specific back pressure events in
Exchange:

     Event log entry for an increase in any resource utilization level

     Event Type: Error

     Event Source: MSExchangeTransport

     Event Category: Resource Manager

     Event ID: 15004

     Description: Resource pressure increased from <Previous Utilization Level> to <Current Utilization
     Level>.

     Event log entry for a decrease in any resource utilization level

     Event Type: Information

     Event Source: MSExchangeTransport

     Event Category: Resource Manager

     Event ID: 15005

     Description: Resource pressure decreased from <Previous Utilization Level> to <Current Utilization
     Level>.

     Event log entry for critically low available disk space

     Event Type: Error

     Event Source: MSExchangeTransport

     Event Category: Resource Manager

     Event ID: 15006

     Description: The Microsoft Exchange Transport service is rejecting messages because available disk
     space is below the configured threshold. Administrative action may be required to free disk space for
     the service to continue operations.

     Event log entry for critically low available memory

     Event Type: Error

     Event Source: MSExchangeTransport

     Event Category: Resource Manager

     Event ID: 15007

<!-- p.1928 -->

Description: The Microsoft Exchange Transport service is rejecting message submissions because the
service continues to consume more memory than the configured threshold. This may require that this
service be restarted to continue normal operation.

<!-- p.1929 -->

Use Telnet to test SMTP communication on
Exchange servers
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

You can use Telnet to test Simple Mail Transfer Protocol (SMTP) communication between
messaging servers. SMTP is the protocol that's used to send email messages from one
messaging server to another. Using Telnet can be helpful if you're having trouble sending or
receiving messages because you can manually send SMTP commands to a messaging server. In
return, the server will reply with responses that would be returned in a typical connection.
These results can sometimes help you to figure out why you can't send or receive messages.

You can use Telnet to test SMTP communication to:

      Test mail flow from the Internet into your Exchange organization.

      Test mail flow from your Exchange to another messaging server on the Internet.

   Tip

  Did you know that, instead of using Telnet to test SMTP connectivity, you can use the
  Microsoft Remote Connectivity Analyzer at https://testconnectivity.microsoft.com/ ?
  With the Remote Connectivity Analyzer, you can choose the connectivity test you want to
  do, in this case Inbound SMTP Email, and follow the instructions shown. It'll step you
  through the information you need to enter, run the test for you, and then give you the
  results. Give it a try!

What do you need to know before you begin?
      Estimated time to complete: 15 minutes

      Exchange permissions don't apply to the procedures in this topic. These procedures are
      performed in the operating system of the Exchange server or a client computer.

      This topic shows you how to use Telnet Client, which is included with Windows. Third-
      party Telnet clients might require syntax that's different from what's shown in this topic.

      The steps in this topic show you how to connect to an Internet-facing server that allows
      anonymous connections using TCP port 25. If you're trying to connect to this server from
      the Internet, you need to ensure your Exchange server is reachable from the Internet on

<!-- p.1930 -->

      TCP port 25. Similarly, if you're trying to reach a server on the Internet from your
      Exchange server, you need to ensure your Exchange server can open a connection to the
      Internet on TCP port 25.

      You might notice some Receive connectors that use TCP port 2525. These are internal
      Receive connectors and aren't used to accept anonymous SMTP connections.

      If you're testing a connection on a remote messaging server, you should run the steps in
      this topic on your Exchange server. Remote messaging servers are often set up to make
      sure the IP address where the SMTP connection is coming from matches the domain in
      the sender's email address.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online           , or Exchange Online Protection .

Step 1: Install the Telnet Client on your computer
On most versions of Windows, you'll need to install the Telnet client before you can use it. To
install it, see Install Telnet Client.

Step 2: Find the FQDN or IP address of the
destination SMTP server
To connect to an SMTP server by using Telnet on port 25, you need to use the fully qualified
domain name (FQDN) (for example, mail.contoso.com) or the IP address of the SMTP server. If
you don't know the FQDN or IP address, you can use the Nslookup command-line tool to find
the MX record for the destination domain.

  ７ Note

  Network policies might prevent you from using the Nslookup tool to query public DNS
  servers on the Internet. As an alternative, you can use one of the freely-available DNS
  lookup or MX record lookup web sites on the Internet.

<!-- p.1931 -->

   1. At a command prompt, type nslookup , and then press Enter. This command opens the
     Nslookup session.

   2. Type set type=mx , and then press Enter.

   3. Type the name of the domain for which you want to find the MX record. For example, to
     find the MX record for the fabrikam.com domain, type fabrikam.com. , and then press
     Enter.

       ７ Note

       When you use a trailing period ( . ), you prevent any default DNS suffixes from being
       unintentionally added to the domain name.

     The output of the command looks like this:

       dos

        fabrikam.com mx preference=10, mail exchanger = mail1.fabrikam.com
        fabrikam.com mx preference=20, mail exchanger = mail2.fabrikam.com
        mail1.fabrikam.com internet address = 192.168.1.10
        mail2 fabrikam.com internet address = 192.168.1.20

     You can use any of the host names or IP addresses that are associated with the MX
     records as the destination SMTP server. A lower value for preference (preference = 10 vs.
     20) indicates a preferred SMTP server. Multiple MX records and different values of
     preference are used for load balancing and fault tolerance.

   4. When you're ready to end the Nslookup session, type exit , and then press Enter.

Step 3: Use Telnet on Port 25 to test SMTP
communication
In this example, we're going to use the following values. When you run the commands on your
server, replace these values with ones for your organization's SMTP server, domain, etc.

     Destination SMTP server: mail1.fabrikam.com
     Source domain: contoso.com
     Sender's e-mail address: chris@contoso.com
     Recipient's e-mail address: kate@fabrikam.com
     Message subject: Test from Contoso
     Message body: This is a test message

<!-- p.1932 -->

 Tip

The commands in the Telnet Client aren't case-sensitive. The SMTP command verbs in this
example are capitalized for clarity. You can't use the backspace key in the Telnet session
after you connect to the destination SMTP server. If you make a mistake as you type an
SMTP command, you need to press Enter, and then type the command again.
Unrecognized SMTP commands or syntax errors result in an error message that looks like
this: 500 5.3.3 Unrecognized command .

 1. Open a Command Prompt window, type telnet , and then press Enter.

   This command opens the Telnet session.

 2. Type set localecho , and then press Enter.

   This optional command lets you view the characters as you type them, and it might be
   required for some SMTP servers.

 3. Type set logfile <filename> , and then press Enter.

   This optional command enables logging and specifies the log file for the Telnet session. If
   you only specify a file name, the log file is located in the current folder. If you specify a
   path and file name, the path needs to be on the local computer, and you might need to
   enter the path and file name in the Windows DOS 8.3 format (short name with no spaces).
   The path needs to exist, but the log file is created automatically.

 4. Type OPEN mail1.fabrikam.com 25 , and then press Enter.

 5. Type EHLO contoso.com , and then press Enter.

 6. Type MAIL FROM:<chris@contoso.com> , and then press Enter.

 7. Type RCPT TO:<kate@fabrikam.com> NOTIFY=success,failure , and then press Enter.

   The optional NOTIFY command specifies the particular delivery status notification (DSN)
   messages (also known as bounce messages, nondelivery reports, or NDRs) that the SMTP
   is required to provide. In this example, you're requesting a DSN message for successful or
   failed message delivery.

 8. Type DATA , and then press Enter.

 9. Type Subject: Test from Contoso , and then press Enter.

10. Press Enter again.

<!-- p.1933 -->

        A blank line is needed between the Subject: field and the message body.

 11. Type This is a test message , and then press Enter.

 12. Type a period ( . ), and then press Enter.

 13. To disconnect from the SMTP server, type QUIT , and then press Enter.

 14. To close the Telnet session, type quit , and then press Enter.

Here's what a successful session using the steps above looks like:

  dos

  C:\Windows\System32> telnet
  Microsoft Telnet> set localecho
  Microsoft Telnet> set logfile c:\TelnetTest.txt
  Microsoft Telnet> OPEN mail1.fabrikam.com 25
  220 mail1.fabrikam.com Microsoft ESMTP MAIL Service ready at Fri, 5 Aug 2016
  16:24:41 -0700
  EHLO contoso.com
  250-mail1.fabrikam.com Hello [172.16.0.5]
  250-SIZE 37748736
  250-PIPELINING
  250-DSN
  250-ENHANCEDSTATUSCODES
  250-STARTTLS
  250-X-ANONYMOUSTLS
  250-AUTH NTLM
  250-X-EXPS GSSAPI NTLM
  250-8BITMIME
  250-BINARYMIME
  250-CHUNKING
  250 XRDST
  MAIL FROM: <chris@contoso.com>
  250 2.1.0 Sender OK
  RCPT TO: <kate@fabrikam.com> NOTIFY=success,failure
  250 2.1.5 Recipient OK
  DATA
  354 Start mail input; end with <CRLF>.<CRLF>
  Subject: test

  This is a test message.
  .
  250 2.6.0 <c89b4fcc-3ad1-4758-a1ab-1e820065d622@mail1.fabrikam.com>
  [InternalId=5111011082268, Hostname=mail1.fabrikam.com] Queued mail for delivery
  QUIT
  221 2.0.0 Service closing transmission channel

<!-- p.1934 -->

Step 4: Success and error messages in the Telnet
Session
This section provides information about the success and failure responses to the commands
that were used in the previous example.

  ７ Note

  The three-digit SMTP response codes that are defined in RFC 5321 are the same for all
  SMTP messaging servers, but the text descriptions in the responses might be slightly
  different.

SMTP reply codes
SMTP servers respond to commands with a variety of numerical reply codes in the format of
x.y.z where:

         X indicates whether the command was good, bad, or incomplete.
         Y indicates the kind of response that was sent.
         Z provides additional information about the command

When a response is received by the server that opened the connection, it can tell whether the
remote server accepted the command and is ready for the next one, or if an error occurred.

The first digit (X) is particularly important to understand because it indicates the success or
failure of the command that was sent. Here are its possible values, and their meanings.

                                                                                            ﾉ   Expand table

 Reply       Meaning
 code

 2.y.z       The command that was sent was successfully completed on the remote server. The remote
             server is ready for the next command.

 3.y.z       The command was accepted but the remote server needs more information before the
             operation can be completed. The sending server needs to send a new command with the
             needed information.

 4.y.z       The command wasn't accepted by the remote server for a reason that might be temporary. The
             sending server should try to connect again later to see if the remote server can successfully
             accept the command. The sending server will continue to retry the connection until either a
             successful connection is completed (indicated by a 2.y.z code) or fails permanently (indicated by
             a 5.y.z code).

<!-- p.1935 -->

 Reply       Meaning
 code

             An example of a temporary error is low storage space on the remote server. Once more space is
             made available, the remote server should be able to successfully accept the command.

 5.y.z       The command wasn't accepted by the remote server for a reason that's not recoverable. The
             sending server won't retry the connection and will send a non-delivery report back to the user
             who sent the message.
             An example of an unrecoverable error is a message that's sent to an email address that doesn't
             exist.

The table above is based on information provided by RFC 5321 (Simple Mail Transfer Protocol),
section 4.2.1 . Additional information, including descriptions of the second (Y) and third (Z)
digits of SMTP reply codes is included in this section, and in sections 4.2.2            and 4.2.3 .

OPEN command
Successful response: 220 mail1.fabrikam.com Microsoft ESMTP MAIL Service ready at <day-
date-time>

Failure response: Connecting to mail1.fabrikam.com...Could not open connection to the
host, on port 25: Connect failed

Possible reasons for failure:

         The destination SMTP service is unavailable.
         Restrictions on the destination firewall.
         Restrictions on the source firewall.
         Incorrect FQDN or IP address for the destination SMTP server.
         Incorrect port number.

EHLO command
Successful response: 250 mail1.fabrikam.com Hello [<sourceIPaddress>]

Failure response: 501 5.5.4 Invalid domain name

Possible reasons for failure:

         Invalid characters in the domain name.
         Connection restrictions on the destination SMTP server.

  ７ Note

<!-- p.1936 -->

  EHLO is the Extended Simple Message Transfer Protocol (ESMTP) verb that's defined in
  RFC 5321. ESMTP servers can advertise their capabilities during the initial connection.
  These capabilities include the maximum accepted message size and supported
  authentication methods. HELO is the older SMTP verb that is defined in RFC 821. Most
  SMTP messaging servers support ESMTP and EHLO. If the non-Exchange server that you're
  trying to connect to doesn't support EHLO, you can use HELO instead.

MAIL FROM command
Successful response: 250 2.1.0 Sender OK

Failure response: 550 5.1.7 Invalid address

Possible reasons for failure: A syntax error in the sender's e-mail address.

Failure response: 530 5.7.1 Client was not authenticated

Possible reasons for failure: The destination server doesn't accept anonymous message
submissions. You receive this error if you try to use Telnet to submit a message directly to a
Mailbox server that doesn't have a Receive connector that's configured to accept anonymous
connections.

RCPT TO command
Successful response: 250 2.1.5 Recipient OK

Failure response: 550 5.1.1 User unknown

Possible reasons for failure: The specified recipient doesn't exist.

<!-- p.1937 -->

Selection of Outbound Anonymous TLS
Certificates
Article • 05/09/2025

APPLIES TO:        2016     2019      Subscription Edition

  ） Important

  Microsoft Exchange Server 2016 and Microsoft Exchange Server 2019 will reach end of
  support on Oct 14, 2025. To stay supported, you need to upgrade. For more information,
  see End of Support for Exchange 2016 and Exchange Server 2019 .

The selection of an outbound anonymous Transport Layer Security (TLS) certificate occurs in
the following scenarios:

      Simple Mail Transfer Protocol (SMTP) sessions between Microsoft Edge Transport servers
      and Mailbox servers for authentication
      SMTP sessions between Mailbox servers

For communication between Mailbox servers, anonymous TLS and the public keys from
certificates are used to encrypt the session. Once the session is encrypted, Kerberos
Authentication takes place between the servers. When an SMTP session is established, the
Receiving server initiates a certificate selection process to determine which certificate to use in
the TLS negotiation. The Sending server also performs a certificate selection process. For more
information about that process, see Selection of Inbound Anonymous TLS Certificates.

This article describes the steps involved in the selection process for outbound anonymous TLS
certificates. These steps are performed on the Sending server which can vary depending on
whether the Sending server is a Microsoft Edge Transport server or a Mailbox server. The
following image depicts the steps for Mailbox server and Microsoft Edge Transport server as
the Sending servers:

<!-- p.1938 -->

                                                                  

The steps depicted in the preceding diagram are explained here:

<!-- p.1939 -->

1. When an SMTP session is established from a Mailbox server or Microsoft Edge Transport
  server to send emails, Microsoft Exchange calls a process to load the certificates. In the
  process of the certificate getting loaded, a few mandatory checks are to be implemented
  on the Sending server, depending on whether the Sending server is the Mailbox server or
  Microsoft Edge Transport server.

       Checks to do on a Mailbox server

        a. InternalTransportCertificateThumbprint isn't NULL: By default, the Exchange
          Self-signed certificate is enabled for an SMTP service, and the Transport Service
          uses this certificate for TLS communication. By running the following command,
          you can ensure that the InternalTransportCertificateThumbprint attribute isn't
          null and contains information, and verify the specific certificate-related
          information the Exchange uses for internal communication:

             PowerShell

             Get-TransportService <ServerName> | FL Name,
             InternalTransportCertificateThumbprint

             ７ Note

             When you assign an SMTP service to a new exchange certificate, exchange
             prompts you to overwrite the existing Internal Transport Certificate. Due to 5
             years validity, it's preferable to continue using default self-signed certificate
             for internal TLS communication.

        b. DeliveryType attribute's value is set to SmtpRelayWithinAdSitetoEdge: To ensure
          this, you can run the following command:

             PowerShell

             Get-FrontendTransportService | Get-Queue

             ７ Note

             The preceding conditions must be met. Else, the Sending Mailbox server
             doesn't use anonymous TLS, and no certificate is loaded. Hence, these
             conditions must be met for the process to move to the next step (querying
             of Active Directory service by Microsoft Exchange).

<!-- p.1940 -->

Checks to do on a Microsoft Edge Transport server

a. InternalTransportCertificateThumbprint isn't NULL: By default, the Exchange
  Self-signed certificate is enabled for an SMTP service, and the Transport Service
  uses this certificate for TLS communication. By running the following command,
  you can ensure that the InternalTransportCertificateThumbprint attribute isn't
  null and contains information, and verify the specific certificate-related
  information the Exchange uses for internal communication:

        PowerShell

        Get-TransportService <ServerName> | FL Name,
        InternalTransportCertificateThumbprint

        ７ Note

        When you assign an SMTP service to a new exchange certificate, exchange
        prompts you to overwrite the existing Internal Transport Certificate. Due to 5
        years validity, it's preferable to continue using default self-signed certificate
        for internal TLS communication.

b. ExchangeServer AuthMechanism is enabled on the Send connector of the
  Microsoft Edge Transport server. To ensure this, you can run the following
  command:

        PowerShell

        Get-SendConnector <Name of the Send Connector> | FL Name,
        SmartHostAuthMechanism

c. Send connector to which the SMTP session is connected: The Send connector is
  checked to determine whether the SmartHost address space property contains "-
  -".

        ７ Note

        The preceding checks/conditions must be met. Else, the Sending Microsoft
        Edge Transport server doesn't use anonymous TLS, and no certificate is
        loaded. Hence, these conditions must be met for the process to move to the
        next step (querying of Active Directory service by Microsoft Exchange).

<!-- p.1941 -->

   2. Microsoft Exchange queries the Active Directory service to retrieve the thumbprint of the
     certificate on the server. The msExchServerInternalTLSCert attribute on the server object
     stores the certificate thumbprint. If the msExchServerInternalTLSCert attribute cannot be
     read or if the value is null during the SMTP session, Microsoft Exchange doesn't advertise
     X-ANONYMOUSTLS, and no certificate is loaded. If the msExchServerInternalTLSCert
     attribute cannot be read or if the value is null during the startup of the Microsoft
     Exchange Transport service, Event ID 12012 is logged in the Application log.

   3. If a thumbprint is found, the certificate selection process searches the local computer
     certificate store for a certificate that matches the thumbprint. If the certificate isn't found,
     the server doesn't advertise X-ANONYMOUSTLS, no certificate is loaded, and Event ID
     12013 is logged in the Application log.

   4. After a certificate is loaded from the certificate store, it's checked to see whether it has
     expired. The Valid to field on the certificate is compared to the current date and time. If
     the certificate has expired, Event ID 12015 is logged in the Application log. But the
     certificate selection process doesn't fail, and it advertises Anonymous TLS.

        ） Important

        If the certificate has expired, you must renew the certificate irrespective of the
        certificate selection process failing or getting completed successfully. For information
        on how to renew the certificate, see Renew an Exchange Server certificate.

More information
For more information about how certificates are selected for other TLS scenarios, see the
following articles:

     Selection of Inbound Anonymous TLS Certificates
     Selection of Inbound STARTTLS Certificates
     Set-SendConnector
     Enable-ExchangeCertificate

<!-- p.1942 -->

Selection of Inbound Anonymous TLS
Certificates
Article • 05/09/2025

APPLIES TO:        2016     2019      Subscription Edition

  ） Important

  Microsoft Exchange Server 2016 and Microsoft Exchange Server 2019 will reach end of
  support on Oct 14, 2025. To stay supported, you need to upgrade. For more information,
  see End of Support for Exchange 2016 and Exchange Server 2019 .

The selection of an inbound anonymous Transport Layer Security (TLS) certificate occurs in the
following scenarios:

      Simple Mail Transfer Protocol (SMTP) sessions between Microsoft Edge Transport servers
      and Mailbox servers for authentication.
      SMTP sessions between mailbox servers.

For communication between Mailbox servers, the X-anonymous TLS and the public keys from
certificates are used to encrypt the session. After the session encryption, Kerberos
Authentication takes place between the servers. When an SMTP session is established, the
Receiving server initiates a certificate selection process to determine which certificate to use in
the TLS negotiation. The Sending server also performs a certificate selection process. For more
information about the certificate selection process by Sending server, see Selection of
Outbound Anonymous TLS Certificates.

This article describes the selection process for inbound anonymous TLS certificates. All the
steps are performed on the Receiving server. The following figure shows the steps of this
process:

<!-- p.1943 -->

                                                                  

The steps depicted in the preceding diagram are explained here:

<!-- p.1944 -->

1. When the SMTP session is established, Microsoft Exchange calls a process to load the
  certificates.

2. In the "load certificate" function, the Receive connector, to which the session is
  connected, is checked to see whether the AuthMechanism property is set to a value of
  ExchangeServer. Prior to this check, the value ExchangeServer must be enabled as an
  authentication mechanism. If ExchangeServer isn't enabled as an authentication
  mechanism, you can enable it by selecting Exchange Server authentication on the
  Authentication tab. If the ExchangeServer isn't enabled as an authentication mechanism,
  the Mailbox server doesn't advertise X-ANONYMOUSTLS to the Sending server in the
  SMTP session, which then prevents the certificate from loading.

    ７ Note

    If the AuthMechanism property isn't set to a value of ExchangeServer, you can set
    the AuthMechanism property on the Receive connector to the value
    ExchangeServer using the Set-ReceiveConnector command.

3. Microsoft Exchange queries the Active Directory service to retrieve the thumbprint of the
  certificate on the server. The msExchServerInternalTLSCert attribute on the server object
  stores the certificate thumbprint.

        If the msExchServerInternalTLSCert attribute can't be read or if the value is null,
        Microsoft Exchange doesn't advertise X-ANONYMOUSTLS and no certificate is
        loaded.

           If the msExchServerInternalTLSCert attribute can't be read, you can view the
           current value of the msExchServerInternalTLSCert attribute by running the
           following command:

              PowerShell

              Get-TransportService -Identity <Mailbox Server Name> | ft
              InternalTransportCertificateThumbprint

           If the msExchServerInternalTLSCert attribute's value is null, you can update its
           value by assigning/reassigning SMTP service to the certificate you want to use as
           an Internal Transport Certificate. To assign/re-assign SMTP service, run the
           following command:

              PowerShell

<!-- p.1945 -->

                 Enable-ExchangeCertificate -thumbprint <Certificate thumbprint> -
                 Services SMTP

                 ７ Note

                 For more information about the Enable-ExchangeCertificate command, see
                 Enable-ExchangeCertificate.

           If the msExchServerInternalTLSCert attribute can't be read or if the value is null
           during startup of the Microsoft Exchange Transport service, instead of during the
           SMTP session, Event ID 12012 is logged in the Application log.

   4. If a thumbprint is found, the certificate selection process searches the local computer
     certificate store for a certificate that matches the thumbprint. If the certificate isn't found,
     the server doesn't advertise X-ANONYMOUSTLS, no certificate is loaded, and Event ID
     12013 is logged in the Application log.

   5. After a certificate is loaded from the certificate store, it's checked to see whether it has
     expired. The Valid to field on the certificate is compared to the current date and time. If
     the certificate has expired, Event ID 12015 is logged in the Application log. But the
     certificate selection process doesn't fail, and it advertises AnonymousTLS.

        ） Important

        If the certificate has expired, you must renew the certificate irrespective of the
        certificate selection process failing or getting completed successfully. For information
        on how to renew the certificate, see Renew an Exchange Server certificate.

More information
For more information about how certificates are selected for other TLS scenarios, see the
following articles:

     Selection of Outbound Anonymous TLS Certificates
     Selection of Inbound STARTTLS Certificates

<!-- p.1946 -->

Selection of Inbound STARTTLS Certificates
Article • 05/09/2025

APPLIES TO:        2016     2019      Subscription Edition

  ） Important

  Microsoft Exchange Server 2016 and Microsoft Exchange Server 2019 will reach end of
  support on Oct 14, 2025. To stay supported, you need to upgrade. For more information,
  see End of Support for Exchange 2016 and Exchange Server 2019 .

This article describes the certificate selection process for inbound STARTTLS that is performed
on the Receiving server. The inbound STARTTLS certificate selection process is triggered when a
Simple Mail Transfer Protocol (SMTP) server tries to open a secure SMTP session with Microsoft
Exchange Mailbox server or Microsoft Edge transport server so that either of these servers
serve as the Receiving server and initiate a certificate selection process to determine which
certificate to use in the TLS negotiation.

The following figure depicts the steps of the certificate selection process for inbound
STARTTLS:

<!-- p.1947 -->

                                                                                            

The steps depicted in the preceding diagram are explained here:

  1. When the SMTP session is established, Microsoft Exchange calls a process to load the
     certificates.

  2. In the "load certificate" function, the Receiving connector, to which the session is
     connected, is checked to see whether the AuthMechanism property is set to a value of
     TLS by running the following command:

       PowerShell

       Get-ReceiveConnector -Identity <Receive Connector Identity> | fl
       AuthMechanism

     If the AuthMechanism property's value is null, you can set the value to TLS by running
     the following command:

<!-- p.1948 -->

    PowerShell

     $AuthMechanism = (Get-ReceiveConnector -Identity <Receive Connector
     Identity>).AuthMechanism
     $AuthMechanism += "TLS"
     Set-ReceiveConnector -Identity <Receive Connector Identity> -AuthMechanism
     $AuthMechanism

  You can also set the AuthMechanism property's value to TLS by selecting Transport
  Security Layer (TLS) on the Authentication tab of a given Receive connector.

  If TLS isn't enabled as an authentication mechanism, the server doesn't advertise X-
  STARTTLS to the Sending server in the SMTP session, and no certificate is loaded.

3. The certificate selection process retrieves the TlsCertificateName value from the Receive
  connector configuration when you run the following command:

    PowerShell

     Get-ReceiveConnector -Identity <Receive Connector Identity> | fl
     TlsCertificateName

  You can also set the TlsCertificateName value on the Receive connector by performing
  the following steps:

   a. Retrieving Thumbprint of a valid SMTP-enabled third-party certificate.

  b. Running the following command:

       PowerShell

        $TLSCert = Get-ExchangeCertificate -Thumbprint <thumbprint retrieved in the
        previous step>
        $TLSCertName = "<I>$($TLSCert.Issuer)<S>$($TLSCert.Subject)"
        Set-ReceiveConnector -Identity <Receive Connector Identity> -
        TlsCertificateName $TlsCertName

4. If the TlsCertificateName value on the Receive connector is null, the fully qualified
  domain name (FQDN) is retrieved. If the FQDN is null, you can set the FQDN value.

  To retrieve or set the FQDN value, perform the following steps:

   a. Retrieve the FQDN value by running the following command:

       PowerShell

<!-- p.1949 -->

        Get-ReceiveConnector -Identity <Receive Connector Identity> | fl fqdn

  b. Set the FQDN value by running the following command:

        PowerShell

        Set-ReceiveConnector -Identity <Receive Connector Identity> -fqdn <fqdn
        value>

5. If the FQDN value on the Receive connector is null, the server's physical FQDN is
  retrieved.

6. The local computer certificate store is searched for certificates that match
  TlsCertificateName/FQDN. If a certificate isn't found, the server doesn't advertise X-
  STARTTLS, no certificate is loaded, and Event ID 12014 is logged in the Application log.

7. In the certificate store, a search is implemented for all certificates that have a matching
  TlsCertificateName/FQDN. From this list, a list of eligible certificates are identified. These
  eligible certificates must meet the following criteria:

        The certificate is an X.509 version 3 or a later-version certificate.

        The certificate has an associated private key.

        The Subject or Subject Alternate Name field contains the
        TlsCertificateName/FQDN that was retrieved in earlier steps.

        The certificate is enabled for Secure Sockets Layer (SSL)/TLS use; specifically, the
        SMTP service has been enabled for this certificate by using the Enable-
        ExchangeCertificate cmdlet. You can verify whether the SMTP service is enabled by
        running the following command to retrieve their values:

          PowerShell

           Get-ExchangeCertificate -Thumbprint <value of the thumbprint> | fl
           Services

        If you find that the SMTP service hasn't been enabled, you can manually enable the
        SMTP service by running the following command:

          PowerShell

           Enable-ExchangeCertificate -Thumbprint <value of the thumbprint> -

<!-- p.1950 -->

               Services "SMTP"

               ７ Note

               If the TlsCertificateName/FQDN-matched certificate doesn't have SMTP service
               enabled, Exchange will still choose that certificate for STARTTLS, but TLS
               communication will fail at later stage.

  8. If no eligible certificates are found after these checks, it results in the server not being
     able to advertise X-STARTTLS with no certificate being loaded, and Event ID 12014 is
     logged in the Application log.

  9. If eligible certificates are found, the best certificate is selected based on the following
     sequence:
      a. Sort eligible certificates by most recent Valid from date. Valid from is a "Version 1"
        field on the certificate.
     b. The first valid public key infrastructure (PKI) certificate that is found in this list is used.
      c. If no valid PKI certificates are found, the first self-signed certificate is used.

          i. The certificate is checked to see whether it has expired. The Valid to field in the
           certificate properties is compared to the current date and time. If the certificate
           hasn't expired, STARTTLS is advertised. If the certificate has expired, Event ID 12016
           is logged in the Application log but STARTTLS is still advertised.

               ） Important

               If the certificate has expired, you must renew the certificate irrespective of
               whether STARTTLS is advertised or not. For information on how to renew the
               certificate, see Renew an Exchange Server certificate.

Setting the value for FQDN property
To set the value for the FQDN property, run the following command:

  PowerShell

  Set-ReceiveConnector -Identity <Receive Connector Identity> -fqdn <fqdn value>

More information

<!-- p.1951 -->

For more information about how certificates are selected for other TLS scenarios, see the
following articles:

     Selection of Outbound Anonymous TLS Certificates
     Selection of Inbound TLS Certificates

<!-- p.1952 -->

Collaboration features in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

Exchange Server provides the following rich features that can help your end users collaborate
in email:

      Site mailboxes (deprecated in SharePoint 2019)
      Public folders
      Shared mailboxes
      Distribution groups

Each of these features has a different user experience and feature set and should be used
based on what the user needs to accomplish and what your organization can provide. For
example, site mailboxes provide great documentation collaboration features. However site
mailboxes rely on SharePoint Server, so if you aren't planning on deploying SharePoint, you
should use public folders to share documents.

This topic compares these collaboration features to help you decide which features to offer
your users.

Site mailboxes
A site mailbox is functionally comprised of a SharePoint 2013 or later site membership (owners
and members), shared storage through an Exchange 2016 or later mailbox for email messages,
and a SharePoint site to store and share information. Essentially, site mailboxes bring Exchange
email and SharePoint documents together. For users, a site mailbox serves as a central filing
cabinet for the project, providing a place to file project email and documents that can be
accessed and edited only by site members. In addition, site mailboxes have a specified lifecycle
and are optimized to be used for projects that have set start and end dates. To fully implement
site mailboxes, end users must use Outlook 2013 or later.

To learn more, see Site mailboxes.

Public folders
Public folders are designed for shared access and provide an easy and effective way to collect,
organize, and share information with other people in your workgroup or organization.

Public folders organize content in a deep hierarchy that's easy to browse. Users discover
interesting and relevant content by browsing through branches of the hierarchy that are

<!-- p.1953 -->

relevant to them. Users always see the full hierarchy in their Outlook folder view. Public folders
are a great technology for distribution group archiving. A public folder can be mail-enabled
and added as a member of the distribution group. Email sent to the distribution group is
automatically added to the public folder for later reference. Public folders also provide simple
document sharing and don't require SharePoint Server to be installed in your organization.
Finally, end users can use public folders with Outlook 2007 or later.

To learn more, see Public folders.

Shared mailboxes
A shared mailbox is a mailbox that multiple designated users can access to read and send
email messages and to share a common calendar. Shared mailboxes can provide a generic
email address (such as info@contoso.com or sales@contoso.com) that customers can use to
inquire about your company. If the shared mailbox has the Send As permission assigned when
a delegated user responds to the email message, it can appear as though the mailbox (for
example, sales@contoso.com) is responding, not the actual user.

To learn more, see Shared mailboxes.

Groups
Groups (also called distribution groups) are a collection of two or more recipients that appears
in the shared address book. When an email message is sent to a group, it's received by all
members of the group. Distribution groups can be organized by a particular discussion subject
(such as "Dog Lovers") or by users who share a common work structure that requires them to
communicate frequently.

To learn more, see Recipients.

Which one to use?
The following table gives you a quick glance at each of the collaboration features to help you
decide which one to use.

                                                                                    ﾉ   Expand table

 Scenario     Site           Public folders      Shared mailboxes                   Groups
              mailboxes

 Type of      Users who      With the proper     Delegates working on behalf of     Users who need
 group        work           permissions,        a virtual identity, and they can   to send email to a

<!-- p.1954 -->

Scenario      Site             Public folders         Shared mailboxes                    Groups
              mailboxes

              together as a    everyone in your       respond to email as that shared     group of
              team on a        organization can       mailbox identity. Example:          recipients with a
              specific         access and search      support@tailspintoys.com            common interest
              project with     public folders.                                            or characteristic.
              definitive       Public folders are
              start and end    ideal for
              dates.           maintaining history
                               or distribution
                               group
                               conversations.

Ideal group   Small            Large                  Small                               Large
size

Access        Site mailbox     Accessible by          Users can be granted Full           For distribution
              owners and       anyone in your         Access and/or Send As               groups, members,
              members.         organization.          permissions. If granted Full        must be manually
                                                      Access permissions, users must      added. For
                                                      also add the shared mailbox to      dynamic
                                                      their Outlook profile to access     distribution
                                                      the shared mailbox.                 groups, members
                                                                                          are added based
                                                                                          on filtering
                                                                                          criteria.

Shared        No               Yes                    Yes                                 No
calendar?

Email         No. Email        No. Email arrives in   No. Email arrives in the Inbox of   Yes. Email arrives
arrives in    arrives in the   the public folder.     the shared mailbox.                 in the Inbox of a
user's        site mailbox.                                                               distribution
personal                                                                                  group member.
Inbox?

Supported     Outlook 2013     Outlook 2007 or        Outlook 2007 or later               Outlook 2007 or
clients       or later         later                  Outlook Web App                     later
              SharePoint                                                                  Outlook Web App
              2013

<!-- p.1955 -->

Site mailboxes in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

Email and documents are traditionally kept in two unique and separate data repositories. Most
organizations collaborate using both mediums. The challenge is that both email and
documents are accessed using different clients. This usually results in a reduction in user
productivity and a degraded user experience.

The site mailbox, first introduced in Exchange 2013, is a solution for this problem. Site
mailboxes improve collaboration and user productivity by allowing access to both Microsoft
SharePoint documents and Exchange email using the same client interface. A site mailbox is
functionally comprised of SharePoint site membership (owners and members), shared storage
through an Exchange 2016 or Exchange 2019 mailbox for email messages and a SharePoint site
for documents, and a management interface that addresses provisioning and lifecycle needs.

Site mailboxes require Exchange 2016 or later and SharePoint Server 2013 or later integration
and configuration. For more information about how to configure your Exchange Server
organization to work with your SharePoint organization, see the following topics:

      Configure site mailboxes in SharePoint Server.

      Plan Exchange Server integration with SharePoint and Skype for Business

For more information about collaboration features in Exchange Server, see Collaboration.

How do site mailboxes work?
When one project member files mail or documents using the site mailbox, any project member
can then access the content. Site mailboxes are surfaced in Outlook 2013 or later and give
users easy access to the email and documents for the projects they care about. Additionally,
the same set of content can be accessed directly from the SharePoint site itself. With site
mailboxes, the content is kept where it belongs. Exchange stores the email, providing users
with the same message view for email conversations that they use every day for their own
mailboxes. Meanwhile, SharePoint stores the documents, bringing document coauthoring and
versioning to the table. Exchange synchronizes enough metadata from SharePoint to create the
document view in Outlook (for example, document title, last modified date, last modified
author, size).

<!-- p.1956 -->

Site mailbox provisioning policies
Site mailbox quotas can be set by using the SiteMailboxProvisioningPolicy cmdlets in the
Exchange Management Shell. The Site mailbox provisioning policies only apply to the email
that is sent to and from the site mailbox and the size of the site mailbox on the Exchange
server. The document repository settings are configured in SharePoint. Although you can
create multiple site mailbox provisioning policies using the New-
SiteMailboxProvisioningPolicy cmdlet, only the default provisioning policy will be applied to
all site mailboxes. You can't apply multiple policies within your organization. The provisioning
policies allow you to set the following quotas:

                                                                                   ﾉ    Expand table

 Quota                     Description                                                    Default
                                                                                          setting

 IssueWarningQuota         The IssueWarningQuota parameter specifies the site mailbox     4.5 GB
                           size that triggers a warning message to the site mailbox

 MaxReceiveSize            The MaxReceiveSize parameter specifies the maximum size of     36 MB
                           email messages that can be received by the site mailbox.

<!-- p.1957 -->

 Quota                      Description                                                    Default
                                                                                           setting

 ProhibitSendReceiveQuota   The ProhibitSendReceiveQuota parameter specifies the size at   5 GB
                            which the site mailbox can no longer send or receive
                            messages.

For more information about how to configure site mailbox provisioning policies, see Manage
site mailbox provisioning policies.

Lifecycle policy and retention
The lifecycle of a site mailbox is managed through SharePoint. It is through SharePoint that you
should perform all site mailbox tasks such as creating and removing site mailboxes. In addition,
you can create a SharePoint Lifecycle policy to manage the lifecycle of a site mailbox. For
example, you can create a lifecycle policy in SharePoint that automatically closes all site
mailboxes after 6 months. If the user still requires the use of the site mailbox, the user can
reactivate the site mailbox through SharePoint. We recommend that you use the Lifecycle
application is in the farm. Manually deleting active site mailboxes from Exchange will result in
orphaned site mailboxes.

When the lifecycle application in SharePoint closes a site mailbox, the site mailbox is retained
for the period stated in the lifecycle policy in the closed state. The mailbox can then be
reactivated by an end user or by an administrator from SharePoint. After the retention period,
the Exchange site mailbox that is housed in the mailbox database will have its name prepended
with MDEL: to indicate that it has been marked for deletion. You will need to manually remove
these site mailboxes from the mailbox database in order to free storage space and the alias. If
you don't have the SharePoint Lifecycle Policy enabled, you'll lose the ability to determine
which site mailboxes are marked for deletion. Until the site mailbox has been removed by an
administrator, the content of the mailbox is still recoverable.

You can use the following command to search for and remove site mailboxes that have been
marked for deletion.

  PowerShell

  Get-Mailbox MDEL:* | ?{$_.RecipientTypeDetails -eq "TeamMailbox"} | Remove-Mailbox
  -Confirm:$false

Site mailboxes don't support retention at the item-level. Retention works on a project-level for
site mailboxes, so when the entire site mailbox is deleted, the retained items will be deleted.

<!-- p.1958 -->

Compliance
Using the eDiscovery Console in SharePoint, site mailboxes can be part of the In-Place
eDiscovery scope as you can do keyword searches against user mailboxes or site mailboxes. In
addition, you can put a site mailbox on legal hold. For more info, see In-Place eDiscovery in
Exchange Server.

Backup and restore
Backup and Restore for the Exchange site mailboxes housed on the mailbox server will use the
same backup and restore method that you use for all Exchange mailboxes. For more
information, see Database availability groups.

For SharePoint documents, you should back up and restore into the same place. If you restore
your SharePoint content to same URLs, then the site mailbox will continue to work and no
further configuration is needed. If you restore to a different URL, then you'll need to run Set-
SiteMailbox cmdlet to update the SharePointURL property. We recommend that you don't
restore SharePoint to a new forest.

<!-- p.1959 -->

Public folders in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Public folders are designed for shared access and provide an easy and effective way to collect,
organize, and share information with other people in your workgroup or organization. Public
folders help make content in a deep hierarchy easier to browse. Users will see the full hierarchy
in Outlook, which makes it easy for them to find the content they're interested in.

Public folders are available in the following Outlook clients:

      Outlook on the web (formerly known as Outlook Web App) for Exchange 2016 or later

      Supported versions of Outlook for Exchange Server.

      Outlook for Mac 2016 and Outlook for Mac for Office 365.

Public folders can also be used as an archiving method for distribution groups. When you mail-
enable a public folder and add it as a member of the distribution group, email sent to the
group is automatically added to the public folder for later reference.

Public folders aren't designed to do the following:

      Data archiving: Users who have mailbox limits sometimes use public folders instead of
      mailboxes to archive data. This practice isn't recommended because it affects storage in
      public folders and undermines the goal of mailbox limits. Instead, we recommend that
      you use In-Place Archiving in Exchange 2016 as your archiving solution.

      Document sharing and collaboration: Public folders don't provide versioning or other
      document management features, such as controlled check-in and check-out functionality
      and automatic notifications of content changes. Instead, we recommend that you use
      SharePoint as your documentation sharing solution.

To learn more about public folders and other collaboration methods in Exchange, see
Collaboration.

To browse some frequently asked questions about public folders in Exchange, see FAQ: Public
folders.

For more information about the limits and quotas for public folders, see Limits for public
folders.

Public folder architecture

<!-- p.1960 -->

Public folders use a mailbox infrastructure to take advantage of the existing high availability
and storage technologies of the mailbox database. Public folder architecture uses specially
designed mailboxes to store both the public folder hierarchy and the content. This also means
that there's no longer a public folder database as there was in earlier version of Exchange. High
availability for the public folder mailboxes is provided by a database availability group (DAG).
To learn more about DAGs, see Database availability groups.

The main architectural components of public folders are the public folder mailboxes, which can
reside in one or more mailbox databases.

Public folder mailboxes
There are two types of public folder mailboxes: the primary hierarchy mailbox and secondary
hierarchy mailboxes. Both types of mailboxes can contain content:

     Primary hierarchy mailbox: The primary hierarchy mailbox is the one writable copy of the
     public folder hierarchy. The public folder hierarchy is copied to all other public folder
     mailboxes, but these will be read-only copies.

     Secondary hierarchy mailboxes: Secondary hierarchy mailboxes contain public folder
     content as well and a read-only copy of the public folder hierarchy.

  ７ Note

  Retention policies aren't supported for public folder mailboxes.

There are two ways you can manage public folder mailboxes:

     In the Exchange admin center (EAC), navigate to Public folders > Public folder
     mailboxes.

     In the Exchange Management Shell, use the *-Mailbox set of cmdlets. The following
     parameters have been added to the New-Mailbox cmdlet to support public folder
     mailboxes:

        PublicFolder: This parameter is used with the New-Mailbox cmdlet to create a public
        folder mailbox. When you create a public folder mailbox, a new mailbox is created with
        the mailbox type of PublicFolder . For more information, see Create a public folder
        mailbox.

        HoldForMigration: This parameter is used only if you're migrating public folders from
        Exchange 2010 to Exchange 2016. For more information, see Migrate public folders
        later in this topic.
