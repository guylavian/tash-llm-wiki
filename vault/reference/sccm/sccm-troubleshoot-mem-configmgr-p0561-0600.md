---
title: "Welcome — pages 561-600"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0561-0600
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0561-0600
family: sccm
documentKind: "doc"
abstract: "TARGET.[FamilyName] != SOURCE.[FamilyName] OR ~ TARGET.[VersionSequence] != SOURCE.[VersionSequence] OR ~ TARGET.[VersionCode] != SOURCE.[VersionCode] OR ~ TARGET.[SourceSite] != SOURCE.[SourceSite]) ~ then ~ UPDATE SET ~ [ProductPool] = SOURCE.[ProductPool], ~ [ProductName] = S"
---

# Welcome — pages 561-600

<!-- p.561 -->

  TARGET.[FamilyName] != SOURCE.[FamilyName] OR ~         TARGET.[VersionSequence] !=
 SOURCE.[VersionSequence] OR ~         TARGET.[VersionCode] != SOURCE.[VersionCode]
 OR ~         TARGET.[SourceSite] != SOURCE.[SourceSite]) ~    then ~    UPDATE SET ~
         [ProductPool] = SOURCE.[ProductPool], ~        [ProductName] = SOURCE.
      *** [23000][515][Microsoft][ODBC Driver 18 for SQL Server][SQL Server]Cannot
 insert the value NULL into column 'VersionCode', table
 'CM_TS1.dbo.LU_LicensedProduct'; column does not allow nulls. UPDATE fails.
 ...
      ERROR: FAILED to import data to table LU_LicensedProduct
      ERROR: Failed to import data from CSV files
      ERROR: Failed to import Asset Intelligence data into the site database.

Symptom 2: Client Notification stops working
In existing environments, the Currently Logged on User column in the Configuration Manager
console doesn't populate. You also see the following error entry in the BGBMgr.log file on the
Site Server:

 Output

 BCP queued 18 rows for currently logged on users
 *** [23000][515][Microsoft][ODBC Driver 18 for SQL Server][SQL Server]Cannot insert
 the value NULL into column 'CurrentLogonUser', table
 'CM_P01.dbo.BGB_LiveDataLogonUsersPending'; column does not allow nulls. INSERT
 fails.
 *** [01000][3621][Microsoft][ODBC Driver 18 for SQL Server][SQL Server]The
 statement has been terminated.
 *** bcp_batch() failed
 ERROR: Failed to send batched rows
 ERROR: Failed to execute task class LiveDataBcp
 ERROR: Failed to bcp file
 ERROR: Failed to execute task class LiveDataProcessTask
 WARNING: Failed to process file Bgbtdhs3.BLD, move it to bad inbox
 Begin to move file from E:\Microsoft Configuration
 Manager\inboxes\bgb.box\Bgbtdhs3.BLD to E:\Microsoft Configuration
 Manager\inboxes\bgb.box\bad\Bgbtdhs3.BLD

Cause
ODBC Driver for SQL Server version 18.6.1.1 includes a change that enforces stricter handling
of NULL values for non-nullable columns. This change can cause failures in Configuration
Manager operations that try to insert NULL values into such columns. Such failures generate
errors during Site Installation and "Currently Logged on User" reporting.

Resolution

<!-- p.562 -->

To resolve this issue, upgrade the ODBC Driver for SQL Server to version 18.6.2.1.

Alternatively, downgrade the driver to version 18.4.1.1. Configuration Manager version 2503
and later versions include this version of the driver as redistributable content.

  ７ Note

  ODBC Driver for SQL Server version 18.6.1.1 doesn't contain security updates. Therefore,
  rolling back the driver doesn't introduce vulnerabilities.

 Last updated on 04/06/2026

<!-- p.563 -->

Description of state messaging in
Configuration Manager
This article describes the state messaging system in Configuration Manager.

Original product version: Configuration Manager (current branch)
Original KB number: 4459394

Understanding state messaging
State messaging in Configuration Manager is a mechanism that reflects a client condition at a
certain point in time. Status messages, by contrast, work to help administrators track the
workflow of data through various Configuration Manager components.

A status message viewer is built right into the console so that status messages can be viewed
and tracked. There's no equivalent viewer for state messages. The result of state messages is
seen in:

     reports
     various data in the console, such as the number of systems that have to be updated
     client logs

State messages contain concise information about conditions in-place on the client. The state
messaging system is used by specific components of Configuration Manager, including:

     software updates
     desired configuration management
     network access protection

Critical software update data relies on the state messaging system in Configuration Manager.
Understanding state messaging will become even more important in future versions of
Configuration Manager as more components take advantage of it.

The following diagram provides a good description of how the state messaging system works.

<!-- p.564 -->

The green box represents the state messaging system. The components inside the box are
components that feed information to the system.

When state messages are received, two things occur:

   1. State messages are stored in the Windows Management Instrumentation (WMI) provider.
   2. The state system scrapes WMI on a 15-minute cycle (default) for any state messages that
     haven't been sent, and then forwards them to the management point. The cycle period
     can be changed.

In the diagram, the client installation piece is shown separately for clarity. During the client
installation, the management point is located and targeted for state messages. State messages
about the client installation are forwarded to the fallback status point (FSP) (if it's configured)
under one of the following conditions:

     The management point isn't reached.
     The management point is down for some reason.

For everything else, traffic goes directly to the management point.

State messages that arrive at the management point are processed into the .smx files by the
MP Relay component, and put into the auth\statesys.box\incoming folder on the site server.
Then, they're processed into the database to complete the workflow.

Digging deeper

<!-- p.565 -->

We have to make sure that verbose logging is enabled for:

      the client
      the management point
      the state messaging components on the site server

To set verbose or debug logging on a Configuration Manager client or management point, edit
or create the following registry entries:

                                                                                    ﾉ   Expand table

 Registry subkey                                                         DWORD name      Value data

 HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/CCM/Logging/@Global               LogLevel        0

 KEY_LOCAL_MACHINE/SOFTWARE /Microsoft/CCM/Logging/DebugLogging          Enabled         True

On the site server, edit the following registry entry to enable verbose logging, and then restart
the SMS_Executive service (or the state system component):

                                                                                    ﾉ   Expand table

 Registry subkey                                                          DWORD name         Value
                                                                                             data

 HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/SMS/Components/SMS_STATE_SYSTEM    Verbose            1
                                                                          Logging

Tracing SQL commands requires that SQL tracing is enabled for Configuration Manager
components. But not much useful data can be obtained directly from the tracing. It's true even
if Profiler is enabled. So we'll examine the Updatesdeployment.log and Statemessage.log files
on the client. By interpreting the state messages in these logs, we can get a clear picture of
what's occurring at the various steps in the process.

Before we examine log code examples, we have to understand the state message format. The
state message itself consists of several parts, including Topic Type and State Message ID. At
some locations in the logs, the Topic Type seems to already be interpreted for you.

You won't always see Topic Type and State Message ID together in the same log. One type of
data without the other doesn't really help you determine what's needed. However, even if you
have both Topic Type and State Message ID, the information isn't helpful unless you can
interpret it.

The following chart can help you to interpret the combination of TopicType and StateID to
obtain meaningful data.

<!-- p.566 -->

SQL

select * from v_StateNames

 ７ Note

 The following chart includes the 300, 400, and 500 series Topic Type codes.

State messaging data

                                                                                          ﾉ   Expand table

TopicType      StateID    StateName

300            0          Compliance state unknown

300            1          Compliant

300            2          Non-compliant

300            3          Conflict detected

301            0          Enforcement state unknown

301            1          Installing update(s)

301            2          Waiting for restart

301            3          Waiting for another installation to complete

301            4          Successfully installed update(s)

301            5          Pending system restart

301            6          Failed to install update(s)

301            7          Downloading update(s)

301            8          Downloaded update(s)

301            9          Failed to download update(s)

301            10         Waiting for maintenance window before installing

301            11         Waiting for third-party orchestrator to initiate installation

302            0          Evaluation state unknown

302            1          Evaluation activated

<!-- p.567 -->

TopicType   StateID   StateName

302         2         Evaluation succeeded

302         3         Evaluation failed

400         0         Detection state unknown

400         1         Not Required

400         2         Not Detected

400         3         Detected

401         0         Compliance state unknown

401         1         Compliant

401         2         Non-Compliant

401         3         Conflict Detected

401         4         Error

401         5         Not Applicable

401         6         Not Detected

401         7         Enforced

402         0         Enforcement state unknown

402         1         Enforcement started

402         2         Enforcement waiting for content

402         3         Waiting for another installation to complete

402         4         Waiting for maintenance window before installing

402         5         Restart required before installing

402         6         General failure

402         7         Pending installation

402         8         Installing update

402         9         Pending system restart

402         10        Successfully installed update

402         11        Failed to install update

<!-- p.568 -->

 TopicType       StateID     StateName

 402             12          Downloading update

 402             13          Downloaded update

 402             14          Failed to download update

 500             0           Detection state unknown

 500             1           Update is not required

 500             2           Update is required

 500             3           Update is installed

 501             0           Scan state unknown

 501             1           Scan is waiting for catalog location

 501             2           Scan is running

 501             3           Scan completed

 501             4           Scan is pending retry

 501             5           Scan failed

 501             6           Scan completed with errors

For more information, see State messages in Configuration Manager.

The following example aligns and compares the Updatesdeployment.log and Statemessage.log
files. Make sure that the logs refer to the same state message by aligning the same TopicID
(green text). It clearly indicates that the two logs are referring to the same state message. The
TopicType is shown in light blue text. Notice that one log might show the actual number that

can be interpreted from the State messaging data chart. The other might show a generic value
(already interpreted). The State Message ID ( StateId ) is shown in purple text.

<!-- p.569 -->

By combining the TopicType and State Message ID ( StateId ) from the chart, you can track
exactly what's occurring in the logs. In this example, these code examples show the following
information:

     Update evaluation
     The result of the evaluation
     The update being downloaded
     The update being installed
     A pending system restart

It's just one example of how state messages are sent into the state system.

State messaging data flow
The following image is an actual example of how state messaging data makes its way to the
management point and is processed to the database.

This example uses a test client. It starts by forcing the client to scrape WMI for all state
messaging information, and then sends that information to the management point on its next
polling cycle.

<!-- p.570 -->

In WMI, state messages are stored in the root\ccm\statemsg namespace. In that namespace,
there are two classes of interest: CCM_StateMsg_SerialNum and CCM_StateMsg .

The CCM_StateMsg_SerialNum class is used to record the last serial number that's used for a
state message. Every state message has a unique serial number, similar to the hardware
inventory. In this manner, the site server can keep track of whether it's missing any state
messages from the system. It's important because missing state messages may cause
incomplete or inaccurate state reporting.

The CCM_StateMsg class contains the state messages themselves. In the class instance, you can
find all the state messages that are recorded.

If you open one of these messages, you'll find the details of the state message and some data
that we previously discussed, as shown in the following example.

<!-- p.571 -->

We can resend the data to the management point, and track its progress by using the
following resync scripts.

 vbs
 RefreshServerComplianceState()

 Sub RefreshServerComplianceState()
 dim newCCMUpdatesStore
 set newCCMUpdatesStore = CreateObject ("Microsoft.CCM.UpdatesStore")
 newCCMUpdatesStore.RefreshServerComplianceState
 wscript.echo "Ran RefreshServerComplianceState."
 End Sub

 PowerShell
 $UpdatesStore = New-Object -ComObject Microsoft.CCM.UpdatesStore
 $UpdatesStore.RefreshServerComplianceState()

This script can be found on the web in various locations. It uses the Configuration Manager
SDK to cause the client to resend its data to the management point.

Typically, a Visual Basic script (VBScript) is run by using cscript . Notice that the script may fail
if you try to run it yourself. The problem is that Configuration Manager is a 32-bit application
that's running on a 64-bit server. The default version of cscript is the 64-bit version and
generally works fine with any VBScript. However, in this case, the call that's being made
requires the 32-bit version of cscript that you must run out of the syswow64 folder.

<!-- p.572 -->

When the next state message polling cycle occurs, all state messages are sent to the
management point.

In the Statemessage.log file, you can see that the state message information is pulled,
formatted into XML, and then sent to the management point. The state message information
should resemble the following example:

  <![LOG[StateMessage body: <?xml version="1.0" encoding="UTF-16"?>
  <Report><ReportHeader><Identification><Machine>
  <ClientInstalled>1</ClientInstalled><ClientType>1</ClientType>
  <ClientID>GUID:GUID</ClientID>
  <ClientVersion>client_version_number</ClientVersion>
  <NetBIOSName>name</NetBIOSName><CodePage>437</CodePage>
  <SystemDefaultLCID>1033</SystemDefaultLCID></Machine></Identification>
  <ReportDetails><ReportContent>State Message Data</ReportContent>
  <ReportType>Full</ReportType><Date>date</Date><Version>1.0</Version>
  <Format>1.0</Format></ReportDetails></ReportHeader><ReportBody><StateMessage
  MessageTime="time" SerialNumber="serial_number"><Topic ID="21e49ac6-a273-4a61-
  9794-eb675bc743e5" Type="500" IDType="3"/><State ID="2" Criticality="0"/>
  <UserParameters Flags="0" Count="1"><Param>102</Param></UserParameters>
  </StateMessageserParameters></StateMessage></ReportBody></Report>
  ]LOG<![LOG[CStateMsgManager::GetSignEncyptMode]LOG]!><time="time" date="date"
  component="StateMessage" context="" type="1" thread="3592"
  file="statemsg.cpp:1820">
  <![LOG[Successfully forwarded State Messages to the management point]LOG]!>
  <time="time" date="date" component="StateMessage" context="" type="1"
  thread="3592" file="statemsg.cpp:1527">

  ７ Note

<!-- p.573 -->

  This example is truncated to a single state message because of the size of the XML file.

Although the Statemessage.log file records that the messages are dispatched to the
management point, the state messaging system doesn't actually move data to the
management point. In the following example, you can see that CCMMessaging does this
operation. There's more that go on behind the scenes at this point. However, it's sufficient to
know that CCMMessaging sends the data to the management point (in this case, the MP_Relay
component).

  <![LOG[OutgoingMessage(Queue='mp_mp_relayendpoint', ID={A9E7A07D-223D-4F5D-
  93D5-15AF5B72E05C}): Delivered successfully to host 'host_name'.]LOG]!>

When the data arrives for processing at MP_Relay , it's processed and translated to the .smx file
format, and then put into the auth\statesys.box\incoming folder.

  Inv-Relay Task: Processing message body
  Relay: FileType= SMX
  Relay: Outbox dir: C:\Program Files (x86)\Microsoft Configuration
  Manager\inboxes\auth\statesys.box\incoming
  Relay: Received 0 attachments
  Relay: 0 of 0 attachments successfully processed
  Inv-Relay: Task completed successfully

In the auth\statesys.box\incoming folder, you can see the .smx files being processed.
Typically, you won't see them here. But if the files remain in this folder, you need to investigate
what the messages are and why they aren't being processed. If you find an .smx file, you can
open it by using a text editor such as Notepad to see the details. However, the formatting of
the file may be unreadable, as in the following example:

<!-- p.574 -->

If you rename the .smx file by adding the .xml extension so that the file is named
file_name.smx.xml, and then you double-click the new file name, the XML file is opened in
Internet Explorer and is much easier to read.

The following image is an example of an XML file opened in Internet Explorer. The details of
the computer and state message are highlighted. It contains the information that we've
previously discussed, combined with the unique State Message ID value.

  ７ Note

  If you rename these files, first copy them to a different folder so that you don't affect the
  Statesys.box folder.

<!-- p.575 -->

Finally, the state messages must be processed into the database. In the Statesys.log file, you
can see such messages similar to the following example:

  Found new state messages to process, starting processing thread
  Thread "State Message Processing Thread #0" id:5076 started
  CMessageProcessor - Detected parent site 'site_name'
  CMessageProcessor - Processing file: mdlbp169.SMW
  CMessageProcessor - Processed 1 records with 0 invalid records.
  CMessageProcessor - Successfully replicated file "mdlbp169.SMW" to parent site
  site_name.
  CMessageProcessor - Processed 1 message files in this batch, with 0 bad files.
  Thread "State Message Processing Thread #0" id:5076 terminated normally

The database processing component can be made visible by enabling SQL tracing, but it
doesn't help much. We must use the SQL profiler instead. The profiler gives us a hint of what's
occurring behind the scenes, but not completely. Several SQL stored procedures are
responsible for processing state messages. Besides, several tables in the database store the
state messaging data. The stored procedures that do state message processing generally start
with the name spProcess . There are many of such procedures.

The site server tracks state messages as they arrive, so it can flag any missing messages and
periodically request a resync when necessary. State messages are important. You don't want to

<!-- p.576 -->

miss any.

As state messages arrive, the unique ID is read and stored in the database. As processing
continues, the data is regularly updated. If a gap is detected, that data is flagged and stored as
missing state messages in the SR_MissingMessageRanges table. Ideally, this table will be empty.
However, in production, you may see data in the table. This table helps track state messages
that require a resync.

The site control file is located in the database. To obtain the specific settings for
STATE_MESSAGE_SYSTEM , run the following query on a primary or CAS site:

 SQL
 select * from SC_Component_Property where ComponentID in (select ID from
 SC_Component where ComponentName like 'SMS_STATE_SYSTEM') and sitenumber in (select
 SiteNumber from SC_SiteDefinition where Sitecode = (Select ThisSiteCode from
 SMSData))

STATE_MESSAGE_SYSTEM settings

                                                                                    ﾉ   Expand table

 Name               Value1    Value2                                                         Value3

 Heartbeat Msg                                                                               60
 Interval

 Inbox Polling                                                                               900
 Interval

 Loader Chunk                                                                                256
 Size

 Loader Threads                                                                              4

 Max Chunks                                                                                  100
 Fetched

 Min Missing                                                                                 2880
 Message Age

 Resync Check                                                                                15
 Interval

 Retry Config       REG_SZ    <Config><Retry PatternID="0"                                   0
                              RetryQueue="0">7200,28800,86400</Retry></Config>

<!-- p.577 -->

 ７ Note

        Resync Check Interval is set to 60 minutes. This is the schedule for checking systems
        that require state message resyncs.
        Min Missing Message Age is set to 2880. This is how long a message must be
        missing before a resync is requested.

Last updated on 02/04/2026

<!-- p.578 -->

Troubleshoot state message processing
performance issues
Applies to: Configuration Manager

State messaging is one of the most important reporting mechanisms in Configuration
Manager. It's responsible for application and update deployment statistics, and many other
flows.

In this article, we focus on the SMS_STATE_SYSTEM component (also referred to as StateSys)
that processes the incoming state messages and updates the database.

For more information about the state messaging system, see Description of state messaging in
Configuration Manager.

Symptoms
A Configuration Manager administrator notices a significant delay in reporting Software
Update compliance and application deployment. In this situation, the <Configuration Manager
Installation Directory>\Inboxes\auth\statesys.box\incoming folder contains a large number

of files. For example, there are millions of files.

Here's a sample output when you filter the InboxMon.log file by StateSys :

  Output

  06-11-2021 08:53:35.276    SMS_INBOX_MONITOR    8972 (0X230C)          FILE COUNT FOR
  DIRECTORY F:\PROGRAM FILES\MICROSOFT CONFIGURATION
  MANAGER\INBOXES\AUTH\STATESYS.BOX\INCOMING\HIGH IS 13360.~
  06-11-2021 08:53:35.401    SMS_INBOX_MONITOR    8972 (0X230C)          FILE COUNT FOR
  DIRECTORY F:\PROGRAM FILES\MICROSOFT CONFIGURATION
  MANAGER\INBOXES\AUTH\STATESYS.BOX\INCOMING\LOW IS 347.~
  06-11-2021 08:53:36.556    SMS_INBOX_MONITOR    8972 (0X230C)          FILE COUNT FOR
  DIRECTORY F:\PROGRAM FILES\MICROSOFT CONFIGURATION
  MANAGER\INBOXES\AUTH\STATESYS.BOX\INCOMING IS 1087076.~
  06-11-2021 09:00:00.785    SMS_INBOX_MONITOR    8972 (0X230C)          FILE COUNT FOR
  DIRECTORY F:\PROGRAM FILES\MICROSOFT CONFIGURATION
  MANAGER\INBOXES\AUTH\STATESYS.BOX\INCOMING\HIGH IS 7.~
  06-11-2021 09:00:01.170    SMS_INBOX_MONITOR    8972 (0X230C)          FILE COUNT FOR
  DIRECTORY F:\PROGRAM FILES\MICROSOFT CONFIGURATION
  MANAGER\INBOXES\AUTH\STATESYS.BOX\INCOMING\LOW IS 213.~
  06-11-2021 09:00:02.885    SMS_INBOX_MONITOR    8972 (0X230C)          FILE COUNT FOR
  DIRECTORY F:\PROGRAM FILES\MICROSOFT CONFIGURATION

<!-- p.579 -->

 MANAGER\INBOXES\AUTH\STATESYS.BOX\INCOMING IS 1099177.~
 06-11-2021 09:15:00.135    SMS_INBOX_MONITOR    8972 (0X230C)               FILE COUNT FOR
 DIRECTORY F:\PROGRAM FILES\MICROSOFT CONFIGURATION
 MANAGER\INBOXES\AUTH\STATESYS.BOX\INCOMING\HIGH IS 23.~
 06-11-2021 09:15:00.240    SMS_INBOX_MONITOR    8972 (0X230C)               FILE COUNT FOR
 DIRECTORY F:\PROGRAM FILES\MICROSOFT CONFIGURATION
 MANAGER\INBOXES\AUTH\STATESYS.BOX\INCOMING\LOW IS 0.~
 06-11-2021 09:15:01.130    SMS_INBOX_MONITOR    8972 (0X230C)               FILE COUNT FOR
 DIRECTORY F:\PROGRAM FILES\MICROSOFT CONFIGURATION
 MANAGER\INBOXES\AUTH\STATESYS.BOX\INCOMING IS 1117189.~

The number of files might continue to grow, or it might decrease too slowly for the files to be
processed within a reasonable time frame. This issue might occur after a long server outage or
a large-scale deployment.

Cause
The incoming files are plain text XML files that usually have a file name extension of .smx or
.smw . These files contain the client ID (known as SMS GUID) and payload. Typically, every file

contains multiple messages. It's because a client will batch the messages before it sends them
(the default is 15 minutes).

StateSys is designed to pick up files in batches, parse XML files, and update the database.
When it updates the database, it runs some SQL stored procedures and CLR assemblies that
are provided by Configuration Manager. Therefore, it mainly depends on the SQL Server back-
end performance. When SQL Server is saturated with other tasks for a long time, this condition
can cause state messages to accumulate.

At the same time, StateSys has some designs that may prevent it from catching up with a
backlog of nearly millions of files:

     Files are processed in alphabetical order, not in "first in first out (FIFO)" order. Because the
     management point generates random names for the files, new messages might be
     processed before old messages. StateSys is resilient to this situation.
     Each message contains a sequence number. StateSys maintains a list of missing ranges
     that are stored in the SR_MissingRanges table. When a missing range becomes older than
     two days (default), StateSys issues a resynchronization for the client. The
     resynchronization causes the client to send a large XML file that goes to the same queue
     as all other messages. If new state messages are always processed two days earlier than
     old messages, this condition can become a vicious cycle for some clients and cause
     frequent resynchronization.

<!-- p.580 -->

Resolution
To troubleshoot the performance issue, follow these steps:

   1. Identify and eliminate the issue that causes the backlog.

     If the issue is a massive deployment, disable the deployment temporarily, or reconsider
     the deployment strategy. For example, if you deploy a software update group of 1,000
     updates, it might generate enforcement state messages for each update, each state (by
     default), each client, and the entire group. This can create millions of state messages.

     If the issue is poor SQL Server performance, work with your database administrator to
     resolve the issue. If there are many files that can't be processed, investigate the root
     cause first.

   2. Establish a Configuration Manager performance baseline to understand the usual
     processing rate of your environment. Particular performance counters for StateSys include
     "Message Records Processed/min" and "Message File Records PreProcessed/min."
     Typically, these average tens of thousands. If there are no files to be processed, both
     counters will decrease to 0.

     If your usual processing rate isn't enough to handle the backlog, go to the next step.

   3. Change the internal settings of the SMS_STATE_SYSTEM component.

<!-- p.581 -->

  ２ Warning

  Serious problems might occur if you change these settings incorrectly. Microsoft
  can't guarantee that these problems can be solved, and doesn't support this
  scenario. Modify the settings at your own risk. We recommend that you restore these
  settings after you resolve the backlog.

You must have at least Configuration Manager infrastructure administrator permissions to
be able to modify these settings.

a. Use the Windows Management Instrumentation Tester tool (Wbemtest) to connect to
  the SMS Provider. Select Connect, enter the site server under Namespace, and then
  select Connect. Enter root\SMS\site_<site code> for a local connection, or enter
   \\MachineName\root\SMS\site_<site code> for a remote connection.

b. Select Query, enter the following query, and then select Apply:

<!-- p.582 -->

    SQL

    SELECT * FROM SMS_SCI_COMPONENT WHERE ITEMNAME = 'SMS_STATE_SYSTEM|SMS SITE
    SERVER'

  This query returns the list of Configuration Manager sites that have the
  SMS_STATE_SYSTEM component installed.

c. Double-click the site whose settings you want to change, and then double-click Props
  from the list of properties of the <site>/StateSys instance.

d. To see the list of embedded properties of this instance, select View Embedded.

<!-- p.583 -->

e. Double-click each embedded property to check the property name and value. Look for
  the property that has the name Loader Threads and the value 4.

f. Double-click Value, increase the value to 16. Select Save Property, and then select Save
  Object.

<!-- p.584 -->

g. Look for another embedded property that has the name Min Missing Message Age
  and the value 2,880 (minutes).

h. Double-click Value, and increase the value to 10,080 (seven days) to prevent
  unnecessary resynchronization. Select Save Property, and then select Save Object.

<!-- p.585 -->

i. In the Property Editor dialog of Props, select Save Property.

j. In the Object Editor dialog of the StateSys instance, select Save Object.

k. Close Wbemtest.

l. Use Configuration Manager Service Manager to stop and then restart the
  SMS_STATE_SYSTEM component.

  After the SMS_STATE_SYSTEM component is restarted, the new settings are logged in
  StateSys.log, as follows.

    Output

    08-24-2021 21:24:16.574    SMS_STATE_SYSTEM    19380 (0X4BB4)              USING THE
    FOLLOWING CONFIGURATION PROPERTIES FROM THE SITEF CONTROL FILE:
    08-24-2021 21:24:16.575    SMS_STATE_SYSTEM    19380 (0X4BB4)                SITE CODE
    CB1
    08-24-2021 21:24:16.575    SMS_STATE_SYSTEM    19380 (0X4BB4)                PARENT
    SITE CODE
    08-24-2021 21:24:16.576    SMS_STATE_SYSTEM    19380 (0X4BB4)                LOADER
    THREADS                         16
    08-24-2021 21:24:16.576    SMS_STATE_SYSTEM    19380 (0X4BB4)                INBOX
    POLLING INTERVAL (SECS)          900
    08-24-2021 21:24:16.577    SMS_STATE_SYSTEM    19380 (0X4BB4)                LOADER

<!-- p.586 -->

           CHUNK SIZE (KB)                  256
           08-24-2021 21:24:16.578    SMS_STATE_SYSTEM     19380 (0X4BB4)           MAX
           CHUNKS FETCHED                       100
           08-24-2021 21:24:16.578    SMS_STATE_SYSTEM     19380 (0X4BB4)           VERBOSE
           LOGGING                         NO
           08-24-2021 21:24:16.579    SMS_STATE_SYSTEM     19380 (0X4BB4)           MIN
           RESYNC PERIOD (HOURS)                72
           08-24-2021 21:24:16.579    SMS_STATE_SYSTEM     19380 (0X4BB4)           RESYNC
           CHECK INTERVAL (MIN)             15
           08-24-2021 21:24:16.580    SMS_STATE_SYSTEM     19380 (0X4BB4)           MIN
           MISSING MESSAGE AGE (MIN)            10880
           08-24-2021 21:24:16.581    SMS_STATE_SYSTEM     19380 (0X4BB4)           HEARTBEAT
           MESSAGE INTERVAL (MIN)       60
           08-24-2021 21:24:16.581    SMS_STATE_SYSTEM     19380 (0X4BB4)        ===
           STATESYS HAS BEEN SUCCESSFULLY INITIALIZED. ===

     m. Monitor the processing rate improvement through performance counters and SQL
         Server CPU load. If the CPU load continues to exceed 80 percent, consider reducing the
         Loader Threads value to avoid saturating other Configuration Manager activities.
         Conversely, if you see an increase in the processing speed at almost no CPU cost,
         increase the number of threads.

More information
Microsoft Premier Services provides the following proactive delivery:

      On-demand Assessment for Configuration Manager

Contact the Customer Success Account Manager (CSAM) for your Premier Support contract to
plan these engagements.

 Last updated on 03/30/2026

<!-- p.587 -->

Can't create a software update package or
application after moving the site database
This article provides a solution for the issue that you cannot create a software update group,
software update package, or application after you move the Configuration Manager SQL Server
site database.

Original product version: Microsoft System Center 2012 Configuration Manager
Original KB number: 2709082

Symptoms
After you move the Configuration Manager SQL Server site database to a different drive, and
then you try to create a software update group, software update package, or application, the
operation fails, and these log entries are logged in the SMSProv.log file:

  *** *** Unknown SQL Error! SMS Provider 14-03-2012 07:56:47 2016 (0x07E0)
  *~*~*** Unknown SQL Error! ThreadID : 2016 , DbError: 50000 , Sev: 16~*~* SMS Provider
  14-03-2012 07:56:47 2016 (0x07E0)
  *** [24000][0][Microsoft][SQL Server Native Client 10.0]Invalid cursor state SMS Provider
  14-03-2012 07:56:48 2016 (0x07E0)
  *~*~[24000][0][Microsoft][SQL Server Native Client 10.0]Invalid cursor state *** Unknown
  SQL Error! ThreadID : 2016 , DbError: 0 , Sev: 0~*~* SMS Provider 14-03-2012 07:56:48
  2016 (0x07E0)

SQL Server Profiler provides the following additional details:

  An error occurred in the Microsoft .NET Framework while trying to load assembly id 65539.
  The server may be running out of resources, or the assembly may not be trusted with
  PERMISSION_SET = EXTERNAL_ACCESS or UNSAFE. Run the query again, or check
  documentation to see how to solve the assembly trust issues. For more information about
  this error:
  System.IO.FileLoadException: Could not load file or assembly 'cryptoutility, Version=5.0.0.0,
  Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. An error
  relating to security occurred. (Exception from HRESULT: 0x8013150A)
  System.IO.FileLoadException:

<!-- p.588 -->

  at System.Reflection.Assembly._nLoad(AssemblyName fileName, String codeBase, Evidence
  assemblySecurity, Assembly locationHint, StackCrawlMark& stackMark, Boolean
  throwOnFileNotFound, Boolean forIntrospection)
  at System.Reflection.Assembly.InternalLoad(AssemblyName assemblyRef, Evidence
  assemblySecurity, StackCrawlMark& stackMark, Boolean forIntrospection)
  at System.Reflection.Assembly.InternalLoad(String assemblyString, Evidence
  assemblySecurity, StackCrawlMark& stackMark, Boolean forIntrospection)
  at System.Reflection.Assembly.Load(String assemblyString)

Cause
This problem may occur if the SQL Server site database MDF and LDF files are moved to a
different drive. For example, this problem may occur if the Configuration Manager site
database is created on C:\Program files\MSSQL server\data , and then the MDF and LDF files
are moved to D:\CM2012DB to save space.

  ７ Note

  This is a supported SQL Server operation. For more information, see Move a Database
  Using Detach and Attach (Transact-SQL).

This problem occurs because the TRUSTWORTHY database property of the site database that is
set to ON by default is reset to OFF when you detach and reattach the database. When the
database is not configured to have the property set to ON,
<ConfigMgr_Install>\bin\x64\CryptoUtility.dll fails to load into SQL Server, and you receive the
invalid cursor state error message that is mentioned in the Symptoms section.

Resolution
To resolve this problem, follow these steps:

   1. Manually reset the property to ON by running this command against your Configuration
     Manager database:

       SQL

        ALTER DATABASE <ConfigMgr DB>
        SET TRUSTWORTHY ON

<!-- p.589 -->

   2. Make sure that the database that was moved is owned by the SA account.

   3. Make sure that the Isolation Level value is set to READ_COMMITTED_SNAPSHOT. To
     check this value, run this command:

       SQL

        DBCC USEROPTIONS

   4. If the Isolation Level value is set to anything other than READ COMMITTED SNAPSHOT,
     run the following commands in the given order:

       SQL

       ALTER DATABASE <ConfigMgr DB>
       SET ALLOW_SNAPSHOT_ISOLATION ON

       ALTER DATABASE <ConfigMgr DB>
       SET READ_COMMITTED_SNAPSHOT ON

  ７ Note

  You may have to change the SQL Server database to Single User mode before you run the
  commands in step 4. For more information about how to detach and attach a database in
  SQL Server, see Database Detach and Attach (SQL Server).

More information
An iDNA (Time Travel) trace of the SQL Server process shows the following exception:

  Number of exceptions of this type: 3
  Exception MethodTable: 000007fef2524e30
  Exception object: 0000000201027798
  Exception type: System.IO.FileLoadException
  Message: Could not load file or assembly 'cryptoutility, Version=5.0.0.0, Culture=neutral,
  PublicKeyToken=31bf3856ad364e35' or one of its dependencies. An error relating to
  security occurred. (Exception from HRESULT: 0x8013150A)
  InnerException: <none>
  StackTrace (generated):
  SP IP Function

<!-- p.590 -->

 00000000204F8DC0 0000000000000001
 System.Reflection.Assembly._nLoad(System.Reflection.AssemblyName, System.String,
 System.Security.Policy.Evidence, System.Reflection.Assembly,
 System.Threading.StackCrawlMark ByRef, Boolean, Boolean)
 00000000204F8DC0 000007FEF23DBF61
 System.Reflection.Assembly.InternalLoad(System.Reflection.AssemblyName,
 System.Security.Policy.Evidence, System.Threading.StackCrawlMark ByRef, Boolean)
 00000000204F8E50 000007FEF23DC127
 System.Reflection.Assembly.InternalLoad(System.String, System.Security.Policy.Evidence,
 System.Threading.StackCrawlMark ByRef, Boolean)
 00000000204F8EB0 000007FEF2443A54 System.Reflection.Assembly.Load(System.String)
 00000000204F8EF0 000007FF002D9FF7
 System.Data.SqlServer.Internal.SqlAppDomain.LoadRawAssembly(Char*, Int32, IntPtr ByRef,
 System.Data.SqlServer.Internal.EClrReturnCode ByRef

Last updated on 03/30/2026

<!-- p.591 -->

Support policies for manual database
changes in a Configuration Manager
environment
This article describes Microsoft support policies for changes that are made to the site database
(SQL Server database) in Configuration Manager (all versions).

Original product version: Microsoft System Center 2012 R2 Configuration Manager, Microsoft
System Center 2012 Configuration Manager, Configuration Manager (current branch)
Original KB number: 3106512

Support policies for manual database changes
Additions or changes that are made to the schema, structure, views, or objects in the site
database are not supported if they are made outside the Software Development Kit (SDK) or the
Configuration Manager product.

This includes changes that are made under the guidance of Microsoft Customer Support,
Microsoft Consulting Services, or other partner organizations to help troubleshoot problems or
performance issues.

In this context, not supported is defined as follows:

     Changes are made at your own risk. The Configuration Manager product team doesn't offer
     testing of database changes.
     Updates or upgrades to the product may revert your changes.
     Servicing support is not available for issues that are caused by custom changes to the
     database. Servicing support is defined as requests for out-of-band (hotfix or cumulative
     update) changes that are made to resolve problems or alter the product design.

This definition doesn't prevent you from contacting Microsoft Customer Support, and it doesn't
automatically exempt the whole environment from support. Changes that are made by using the
guidance of official documentation are supported. However, such changes are not guaranteed to
persist after updates or upgrades are applied.

  ７ Note

<!-- p.592 -->

  Microsoft Customer Support cannot build, rebuild, troubleshoot, or maintain custom
  changes to the database. When you contact Support, you may be asked to revert the
  changes to resolve a problem. Additionally, you may be asked to reproduce the same
  problem independent of those changes to help Support agents escalate your case and work
  toward a resolution.

Because of the diverse nature of Configuration Manager installations, some unsupported changes
(such as adding a new index) are still desirable to optimize performance for a given environment.
We recommend that you test such changes thoroughly in your environment to make sure that
they meet your business needs and do not introduce unintended side effects. Remember that
these changes may be reverted during an update or upgrade of the product.

If you believe that product changes that you have made in your environment would be
appropriate to include in a future version of the product, we encourage you to send feedback
directly to the Microsoft product group.

Last updated on 06/25/2026

<!-- p.593 -->

Error when downloading
ConfigMgr.AdminUIContent.cab by using
SMS_DMP_DOWNLOADER or
ServiceConnectionTool.exe
When you use service connection point online mode or the service connection tool to
download updates in Configuration Manager, you receive an AdminUIContentDownload error
message.

Original product version: Configuration Manager (current branch)
Original KB number: 4561945

Symptoms
     If you have the service connection point (SMS_DMP_DOWNLOADER) set to online mode,
     you may notice that no new Configuration Manager releases appear in the console. Also,
     the following error entry is logged in the DmpDownloader.log file:

       Redirected to URL
       https://configmgrbits.azureedge.net/adminuicontent/ConfigMgr.AdminUIContent.cab

       ~~
       Got fwdlink and recreating the httprequest/response~~
       ERROR: Failed to download Admin UI content payload with exception: The underlying
       connection was closed: An unexpected error occurred on a send.~~
       Failed to call AdminUIContentDownload. error = Error -2146233079~

     You have the service connection point set to offline mode. You use the service connection
     tool (ServiceConnectionTool.exe) to download and import updates in Configuration
     Manager. Also, the following error entry is logged in the ServiceConnectionTool.log file:

       ERROR:AdminUIContentDownloadDownload:DownloadManifestCab exception: The
       underlying connection was closed: An unexpected error occurred on a send. There
       may be an issue with internet connection or the download link.

Cause

<!-- p.594 -->

This issue occurs in one of the following situations:

     TLS 1.2 isn't enabled for .NET Framework on the computer that's running the online
     service connection point or service connection tool. TLS 1.2 is required to download the
     .cab file.
     The specific URLs that are required by the service connection point aren't included in the
     allowlist on your firewall or proxy server.

Resolution

  ７ Note

          If you haven't already, consider upgrading the server that hosts the service
          connection point to Windows Server 2016 or later versions.
          Make sure you have all internet rules and exceptions set up for your proxy or firewall
          to allow the service connection point to access internet endpoints. For more
          information, see Internet Access Requirement and Configuration Manager proxy
          exceptions.
          Make sure the following cipher suites are enabled on the server that hosts the
          service connection point:
            TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xc030)
            TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)
            TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 (0x9f)
            TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 (0x9e)

On the computer that runs the online service connection point or service connection tool,
enable TLS 1.2. In particular, if .NET Framework updates are installed, set the following registry
values, and then restart the computer:

Subkey: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v4.0.30319

Values:

      SystemDefaultTlsVersions = DWORD:00000001

      SchUseStrongCrypto = DWORD:00000001

For more information about the specific URLs that are required by the service connection point,
see Service connection point.

<!-- p.595 -->

Workaround
  1. From the error in the DMPDownloader.log file, copy the URL and manually download the
     .cab file.
  2. Copy the .cab file to the <ConfigMgr Install Dir>\Inboxes\HMAN.box\CFD folder.
  3. Monitor the HMAN.log file for processing details.

Last updated on 03/30/2026

<!-- p.596 -->

Configuration Manager in-console update
fails at the Install Files stage because
required files are missing
Original product version: Configuration Manager (current branch)

Summary
This article helps you resolve an issue in which a Configuration Manager in-console update fails
at the Install Files stage. This failure occurs if required redistributable files are missing from the
EasySetupPayload or CMUStaging folders on the service connection point or site server. Follow
the steps in this article to identify which files are missing, and restore them so that the update
can complete successfully.

Symptoms
When you install an in-console update package in Configuration Manager, the update fails at the
Install Files stage. The CMUpdate.log file contains entries that resemble one of the following
examples.

     Example 1:

       Output

       ERROR: Failed to find folder that stores msi file SQLSysClrTypes.msi
       Failed to find SQLSysClrTypes.msi
       Failed to install SQLSysClrTypes.msi
       Failed to install SQL redist

     Example 2:

       Output

       ERROR: File hash check failed: 0x80070002
       ERROR: VerifyExternalFile failed: 0x80070002
       ERROR: Failed to find valid source for required external file
       ERROR: Failed to find valid source for required file 'MMASetup-AMD64.exe'.
       Aborting setup.
       Setup has encountered fatal errors while performing file operations.
       Failed to install update files.

<!-- p.597 -->

Cause
This issue occurs because the update operation can't find required redistributable files (for
example, SQLSysClrTypes.msi or MMASetup-AMD64.exe`) in one or both of the following
locations:

     Service connection point source content (EasySetupPayload folder):
        Location for online mode:
        \\ServiceConnectionPoint\EasySetupPayload\PackageGuid\Redists
        Location for offline mode:
        \\ServiceConnectionPoint\EasySetupPayload\Offline\PackageGuid\Redists

     Site server staging content (CMUStaging folder):
        ConfigMgrInstallPath\CMUStaging\PackageGuid\redist

        ７ Note

        The placeholders in these paths represent the following items:
             ServiceConnectionPoint: The name of the SCP.
             ConfigMgrInstallPath: The path to the Site server installation information.
             PackageGuid: GUID of the affected update package.

Resolution
The steps to resolve this issue depend on which folder is missing files (or whether files are
missing from both folders). To identify the affected folders, follow these steps:

   1. Identify the update package GUID.
   2. Check whether the required files exist in the EasySetupPayload folder, in either the online
     mode or offline mode locations.
   3. Check whether the required files exist in the CMUStaging folder.

After you finish these steps, continue to the scenario that matches your findings:

     Scenario 1: Files are missing from the EasySetupPayload folder
     Scenario 2: Files exist in the EasySetupPayload folder but are missing from the CMUStaging
     folder

Scenario 1: Files are missing from the EasySetupPayload folder

<!-- p.598 -->

If files are missing from the EasySetupPayload folder, restore the update payload source first.

Restore the update payload for an online service connection point (SCP)

For an online SCP, follow these steps:

   1. Verify that the SCP can connect to the internet and to the required endpoints.

   2. Because the update has passed the Replication stage, you have to change its state before
     you can download it again. To change the update state, on a server that hosts the SMS
     Provider, open a Windows PowerShell Command Prompt window. Then run the following
     cmdlets:

       PowerShell

       $CMUpdateGUID = '<PackageGuid>' # e.g.: 94727833-903B-49EF-9CF7-A43D2BC8826D
       $Flag = 1
       $DesiredState = "0x0004FFFF" #DOWNLOAD_FAILED
       $CMUpdatePackage = Get-WmiObject -Namespace "root\SMS\site_<SiteCode>" -Class
       SMS_CM_UpdatePackages -Filter ("PackageGuid = '$($CMUpdateGUID)'")
       Invoke-WmiMethod -InputObject $CMUpdatePackage -Name UpdatePrereqAndStateFlags -
       ArgumentList @($Flag,[convert]::ToInt32('{0:x}' -f $DesiredState, 16)) | Out-Null

        ７ Note

        In these cmdlets, <PackageGuid> represents the GUID of the update package file, and
        <SiteCode> is the identifier of the site to be updated.

     The update status should now be "Download failed."

   3. Try again to download the package. You can download the package manually from the
     console, or use the Update reset tool (CMUpdateReset.exe).

   4. After the download finishes, review the following log files:

           dmpdownloader.log. Look for entries that were recorded during the download
           attempt that resemble the following examples:

             Output

             Check if there is redist to download for update, aa928926-5c76-4de0-b51f-
             0fe4d365dfe2~~
             Download redist for update aa928926-5c76-4de0-b51f-0fe4d365dfe2~~
             Successfully download redist for aa928926-5c76-4de0-b51f-0fe4d365dfe2~~

<!-- p.599 -->

            ConfigMgrSetup.log. Look for entries that indicate that the file hash was calculated
            successfully, such as the following example:

              Output

              INFO: Downloading https://go.microsoft.com/fwlink/?LinkId=2115685 as
              SQLSysClrTypes.msi
              INFO: set additional flag.
              No proxy information is specified. Connect without proxy.
              INFO: WinHttpQueryHeaders() in Download() returned OK (200)
              INFO: Verifying hash for file 'E:\ConfigMgr\EasySetupPayload\aa928926-5c76-
              4de0-b51f-0fe4d365dfe2\redist\SQLSysClrTypes.msi'
              INFO: Verifying signature for file 'E:\ConfigMgr\EasySetupPayload\aa928926-
              5c76-4de0-b51f-0fe4d365dfe2\redist\SQLSysClrTypes.msi'

After the download operation finishes, verify that the required files exist in the
EasySetupPayload\PackageGuid\Redists folder. At this point, try again to install the in-console
update package.

Restore the update payload for an offline SCP

For an offline SCP, use the service connection tool to download and import the update files
again.

  ７ Note

  In service connection tool version 2509 or later, if the tool can't download the required
  redistributable files, the operation fails at the Connect step.

While the tool runs, review the ServiceConnectionTool.log and ConfigMgrSetup.log files to verify
that the required files download successfully.

     ServiceConnectionTool.log. Look for entries that resemble the following examples:

         Output

         INFO:ConfigMgr.Update.Manifest.cab (size = 15741046) downloaded successfully
         INFO:Downloading Payload 248DC1EB-4B98-4483-BAF3-08C678C1CD0A version
         5.0.9058.1000. More information: https://go.microsoft.com/fwlink/?LinkId=2166085
         INFO:Downloaded Payload 248DC1EB-4B98-4483-BAF3-08C678C1CD0A size = 967280807
         INFO:Downloading Redists for 248DC1EB-4B98-4483-BAF3-08C678C1CD0A
         INFO:Successfully downloaded Redists for 248DC1EB-4B98-4483-BAF3-08C678C1CD0A

     ConfigMgrSetup.log. Look for entries that resemble the following examples:

<!-- p.600 -->

       Output

       INFO: Downloading https://go.microsoft.com/fwlink/?LinkId=2115685 as
       SQLSysClrTypes.msi
       INFO: set additional flag.
       No proxy information is specified. Connect without proxy.
       INFO: WinHttpQueryHeaders() in Download() returned OK (200)
       INFO: Verifying hash for file 'E:\ServiceConnectionTool\Update\248DC1EB-4B98-
       4483-BAF3-08C678C1CD0A\Redist\SQLSysClrTypes.msi'
       4580 (0x11e4)    INFO: Verifying signature for file
       'E:\ServiceConnectionTool\Update\248DC1EB-4B98-4483-BAF3-
       08C678C1CD0A\Redist\SQLSysClrTypes.msi'

After the download operation finishes, verify that the required files exist in the
EasySetupPayload\Offline\PackageGuid\Redists folder. At this point, try again to install the in-
console update package.

Scenario 2: Files exist in the EasySetupPayload folder but are
missing from the CMUStaging folder
If files exist in the EasySetupPayload folder but are missing from the CMUStaging folder, you have
to replicate the update content again. To retrigger the update content replication process, open a
PowerShell Command Prompt window on a server that hosts the SMS Provider role for the top-
level site. Then, run the following cmdlet:

 PowerShell

 (Get-WmiObject -Namespace "ROOT\SMS\site_<SiteCode>" -Query "select * from
 SMS_CM_UpdatePackages where PackageGuid =
 '<PackageGuid>'").RetryContentReplication($true)

  ７ Note

  In this cmdlet, <PackageGuid> represents the GUID of the update package file, and
  <SiteCode> is the identifier of the site to be updated.

After the replication process finishes, try again to install the in-console update package.

More information
For end-to-end information about the update workflow and extra troubleshooting guidance, see
Understand and troubleshoot Updates and Servicing in Configuration Manager.
