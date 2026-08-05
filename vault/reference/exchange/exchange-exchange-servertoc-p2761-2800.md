---
title: "Exchange Server — pages 2761-2800"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2761-2800
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2761-2800
family: exchange
documentKind: "doc"
abstract: "a. Examining the event log for any error or warning events related to the database or the database copy. b. Using the Get-MailboxDatabaseCopyStatus cmdlet to check the health and status of continuous replication for the database copy. c. Using the Test-ReplicationHealth cmdlet t"
---

# Exchange Server — pages 2761-2800

<!-- p.2761 -->

      a. Examining the event log for any error or warning events related to the database or the
        database copy.

     b. Using the Get-MailboxDatabaseCopyStatus cmdlet to check the health and status of
        continuous replication for the database copy.

      c. Using the Test-ReplicationHealth cmdlet to verify the health and status of the database
        availability group and continuous replication.

For detailed syntax and parameter information, see the following topics:

     Get-MailboxDatabase

     Set-MailboxDatabase

     Set-MailboxDatabaseCopy

     Get-MailboxDatabaseCopyStatus

     Test-ReplicationHealth

How do you know this worked?
To verify that you've successfully moved the path for a mailbox database copy, do one of the
following:

     In the EAC, navigate to Servers > Databases. Select the database that was copied. In the
     Details pane, the status of the database copy and its content index are displayed, along
     with the current copy queue length. Verify that the status is Healthy.

     In the Exchange Management Shell, run the following command to verify the mailbox
     database copy was created and is healthy.

       PowerShell

        Get-MailboxDatabaseCopyStatus <DatabaseCopyName>

     The Status and Content Index State should both be Healthy.

<!-- p.2762 -->

Configure activation policy for a mailbox
database copy in Exchange Server
07/23/2025

APPLIES TO:      2016      2019      Subscription Edition

Activation is the process of changing a mailbox database copy from a passive copy to an active
copy. Activation can occur automatically (by the system as part of a database or server failover
operation) or it can be performed manually (by an administrator as part of a database or server
switchover operation). Blocking a database for activation prevents it from becoming the active
copy during a database or server failover.

Looking for other management tasks related to mailbox database copies? Check out Manage
mailbox database copies.

What do you need to know before you begin?
     Estimated time to complete this task: 1 minute

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Mailbox database copies" entry
     in the High availability and site resilience permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the EAC to configure the activation policy for a
mailbox database copy
   1. In the EAC, go to Servers > Databases.

   2. Select the database that you want to configure.

   3. In the Details pane, under Database Copies, locate the database copy you want to
     configure and click Suspend.

<!-- p.2763 -->

   4. Optionally, add a comment, and select the check box that says This copy can only be
     activated by manual intervention.

   5. Click Save to save the configuration changes for the mailbox database copy.

Use the Exchange Management Shell to suspend or
resume a database copy for activation
This example blocks the copy of the database DB1 on the server MBX2 for activation.

  PowerShell

  Suspend-MailboxDatabaseCopy -Identity DB1\MBX2 -ActivationOnly

This example resumes the copy of the database DB1 on the server MBX2 for activation.

  PowerShell

  Resume-MailboxDatabaseCopy -Identity DB1\MBX2

For detailed syntax and parameter information, see Suspend-MailboxDatabaseCopy or
Resume-MailboxDatabaseCopy.

Use the Exchange Management Shell to configure
the activation policy for a server
This example configures the database copies on server MBX2 as blocked for activation.

  PowerShell

  Set-MailboxServer -Identity MBX2 -DatabaseCopyAutoActivationPolicy Blocked

This example configures the database copies on server MBX3 as blocked for out-of-site
activation.

  PowerShell

  Set-MailboxServer -Identity MBX3 -DatabaseCopyAutoActivationPolicy IntrasiteOnly

This example configures the database copies on server MBX4 as unblocked for activation.

<!-- p.2764 -->

  PowerShell

  Set-MailboxServer -Identity MBX4 -DatabaseCopyAutoActivationPolicy Unrestricted

For detailed syntax and parameter information, see Suspend-MailboxDatabaseCopy, Resume-
MailboxDatabaseCopy, or Set-MailboxServer.

How do you know this worked?
To verify that you've successfully configured the activation policy, do one of the following:

     In the Exchange Management Shell, run the following command to verify activation
     settings for a database copy.

        PowerShell

        Get-MailboxDatabaseCopyStatus <DatabaseCopyName> | Format-List
        ActivationSuspended

     In the Exchange Management Shell, run the following command to verify activation
     settings for a DAG member.

        PowerShell

        Get-MailboxServer <ServerName> | Format-List DatabaseCopyAutoActivationPolicy

<!-- p.2765 -->

Update a mailbox database copy in
Exchange Server
07/23/2025

APPLIES TO:      2016     2019      Subscription Edition

Updating, also known as seeding, is the process where a copy of a mailbox database is added
to another Mailbox server in a database availability group (DAG). The newly added copy
becomes the baseline database for the passive copy into which log files copied from the active
copy are replayed. Seeding is required under the following conditions:

     When a new passive copy of a database is created. Seeding can be postponed for a new
     mailbox database copy, but eventually each passive database copy must be seeded to
     function as a redundant database copy.

     A failover occurred where data is lost as a result of the passive database copy becoming
     diverged and unrecoverable.

     The system detected a corrupted log file that can't be replayed into the passive copy of
     the database.

     An offline defragmentation of any copy of the database.

     The log generation sequence for the database was reset back to 1.

You can perform seeding by using the following methods:

     Automatic seeding: An automatic seed produces a passive copy of the active database
     on the target Mailbox server. Automatic seeding occurs during the creation of a database.

     Seeding using the Update-MailboxDatabaseCopy cmdlet: You can use the Update-
     MailboxDatabaseCopy cmdlet in the Exchange Management Shell to seed a database
     copy at any time.

     Seeding using the Update Mailbox Database Copy wizard: You can use the Update
     Mailbox Database Copy wizard in the Exchange admin center (EAC) to seed a database
     copy at any time.

     Manually copying the offline database: You can dismount the active copy of the
     database and copy the database file to the same location on another Mailbox server in
     the same DAG. If you use this method, there's an interruption in service because the
     process requires you to dismount the database.

<!-- p.2766 -->

Updating a database copy can take a long time, especially if the database being copied is large,
or if there's high network latency or low network bandwidth. After the seeding process starts,
don't close the EAC or the Exchange Management Shell until the process is complete. If you do,
the seeding operation is terminated.

A database copy can be seeded using either the active copy or an up-to-date passive copy as
the source for the seed. When seeding from a passive copy, the seed operation terminates with
a network communication error under the following conditions:

     The status of the seeding source copy changes to Failed or FailedAndSuspended.

     The database fails over to another copy.

Multiple database copies can be seeded simultaneously. However, when seeding multiple
copies simultaneously, you must seed only the database file, and omit the content index
catalog. You can achieve this result by using the DatabaseOnly parameter with the Update-
MailboxDatabaseCopy cmdlet.

  ７ Note

  If you don't use the DatabaseOnly parameter when seeding multiple targets from the
  same source, the task fails with SeedInProgressException error FE1C6491 .

Looking for other management tasks related to mailbox database copies? Check out Manage
mailbox database copies.

What do you need to know before you begin?
     Estimated time to complete this task: 2 minutes, plus the time to seed the database copy.
     Database seeding depends on many factors. For example:
        The size of the database.
        The speed, available bandwidth and latency of the network.
        Storage speeds.

     To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
     Management Shell, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Mailbox database copies" entry
     in the High availability and site resilience permissions article.

     The mailbox database copy must be suspended. For detailed steps, see Suspend or
     resume a mailbox database copy.

<!-- p.2767 -->

     The Remote Registry service must be running on the server hosting the passive database
     copy you're updating.

     For information about keyboard shortcuts that might apply to the procedures in this
     article, see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Update a mailbox database copy

Use the EAC to update a mailbox database copy
  1. In the EAC, go to Servers > Databases.

  2. Select the mailbox database whose passive copy you want to update.

  3. In the Details pane, under Database Copies, select Suspend under the passive database
     copy you want to seed. Provide any optional comments, and select save.

  4. In the Details pane, under Database Copies, select Update under the passive database
     copy you want to seed.

  5. By default, the active copy of the database is used as the source database for seeding. If
     you prefer to use a passive copy of the database for seeding, select browse... to select the
     server containing the passive database copy you want to use for the source.

  6. Select save to update the passive database copy.

Use the Exchange Management Shell to update a mailbox
database copy
This example shows how to seed a copy of the database DB1 on MBX1.

  PowerShell

  Update-MailboxDatabaseCopy -Identity DB1\MBX1

<!-- p.2768 -->

This example shows how to seed a copy of the database DB1 on MBX1 using MBX2 as the
source Mailbox server for the seed.

  PowerShell

  Update-MailboxDatabaseCopy -Identity DB1\MBX1 -SourceServer MBX2

This example shows how to seed a copy of the database DB1 on MBX1 without seeding the
content index catalog.

  PowerShell

  Update-MailboxDatabaseCopy -Identity DB1\MBX1 -DatabaseOnly

This example shows how to seed the content index catalog for the copy of the database DB1
on MBX1 without seeding the database file.

  PowerShell

  Update-MailboxDatabaseCopy -Identity DB1\MBX1 -CatalogOnly

Manually copy an offline database
   1. If circular logging is enabled for the database, it must be disabled before proceeding. You
     can disable circular logging for a mailbox database by using the Set-MailboxDatabase
     cmdlet, as shown in this example.

        PowerShell

        Set-MailboxDatabase DB1 -CircularLoggingEnabled $false

   2. Dismount the database. You can use the Dismount-Database cmdlet, as shown in this
     example.

        PowerShell

        Dismount-Database DB1 -Confirm $false

   3. Manually copy the database files (the database file and all log files) to a second location,
     such as an external disk drive or a network share.

   4. Mount the database. You can use the Mount-Database cmdlet, as shown in this example.

<!-- p.2769 -->

       PowerShell

        Mount-Database DB1

   5. On the server that will host the copy, copy the database files from the external drive or
     network share to the same path as the active database copy. For example, if the active
     copy database path is D:\DB1\DB1.edb and log file path is D:\DB1, you would copy the
     database files to D:\DB1 on the server that will host the copy.

   6. Add the mailbox database copy by using the Add-MailboxDatabaseCopy cmdlet with the
     SeedingPostponed parameter, as shown in this example.

       PowerShell

        Add-MailboxDatabaseCopy -Identity DB1 -MailboxServer MBX3 -SeedingPostponed

   7. If circular logging is enabled for the database, enable it again by using the Set-
     MailboxDatabase cmdlet, as shown in this example.

       PowerShell

        Set-MailboxDatabase DB1 -CircularLoggingEnabled $true

How do you know this worked?
To verify that you've successfully seeded a mailbox database copy, do one of the following:

     In the EAC, navigate to Servers > Databases. Select the database that was seeded. In the
     Details pane, the status of the database copy and its content index are displayed, along
     with the current copy queue length.

     In the Exchange Management Shell, run the following command to verify the mailbox
     database copy was seeded successfully and is healthy.

       PowerShell

        Get-MailboxDatabaseCopyStatus <DatabaseCopyName>

     The Status and Content Index State should both be Healthy.

<!-- p.2770 -->

Suspend or resume a mailbox database
copy in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

You may need to suspend or resume a database copy for a variety of reasons, such as
maintenance on the disk that contains the database copy. Or you may need to suspend an
individual database copy from activation for disaster recovery purposes.

Looking for other management tasks related to mailbox database copies? Check out Manage
mailbox database copies.

What do you need to know before you begin?
      Estimated time to complete this task: 1 minute

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mailbox database copies" entry
      in the High availability and site resilience permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online         , or Exchange Online Protection .

Suspend a mailbox database copy

Use the EAC to suspend a mailbox database copy
   1. In the EAC, go to Servers > Databases.

   2. Select the database whose copy you want to suspend.

<!-- p.2771 -->

  3. In the Details pane, under Database Copies, click Suspend under the database copy you
     want to suspend.

  4. In the Comments field, add an optional comment of up to 512 characters specifying the
     reason for the suspension.

  5. To suspend the database copy from automatic activation, select the This copy can only
     be activated by manual intervention check box.

  6. Click save to suspend the database copy.

Use the Exchange Management Shell to suspend a mailbox
database copy
This example suspends continuous replication for a copy of the database DB1 hosted on the
server MBX1. An optional comment has also been specified.

  PowerShell

  Suspend-MailboxDatabaseCopy -Identity DB1\MBX1 -SuspendComment "Maintenance on
  MBX1" -Confirm:$False

This example suspends activation for a copy of the database DB2 hosted on the server MBX2.

  PowerShell

  Suspend-MailboxDatabaseCopy -Identity DB2\MBX2 -ActivationOnly -Confirm:$False

For detailed syntax and parameter information, see Suspend-MailboxDatabaseCopy.

Resume a mailbox database copy

Use the EAC to resume a mailbox database copy
  1. In the EAC, go to Servers > Databases.

  2. Select the database whose copy you want to resume.

  3. In the Details pane, under Database Copies, click Resume under the database copy you
     want to resume.

  4. Click yes to resume the database copy.

<!-- p.2772 -->

Use the Exchange Management Shell to resume a mailbox
database copy
This example resumes a copy of the database DB1 on the server MBX1.

  PowerShell

  Resume-MailboxDatabaseCopy -Identity DB1\MBX1

This example resumes a copy of the database DB2 on the server MBX2 for replication only.

  PowerShell

  Resume-MailboxDatabaseCopy -Identity DB2\MBX2 -ReplicationOnly

For detailed syntax and parameter information, see Resume-MailboxDatabaseCopy.

How do you know this worked?
To verify that you have successfully suspended or resumed a mailbox database copy, do one of
the following:

     In the EAC, navigate to Servers > Databases. Select the appropriate database, and in the
     Details pane, click View details to view the database copy properties:

     In the Exchange Management Shell, run the following command to display status
     information for a database copy:

        PowerShell

        Get-MailboxDatabaseCopyStatus <DatabaseCopyName> | Format-List

<!-- p.2773 -->

Activate a mailbox database copy
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

Activating a mailbox database copy is the process of designating a specific passive copy as the
new active copy of a mailbox database. This process is referred to as a database switchover. A
database switchover involves dismounting the current active database and mounting the
database copy on the specified server as the new active mailbox database copy. The database
copy that will become the active mailbox database must be healthy and current.

Looking for other management tasks related to mailbox database copies? Check out Manage
mailbox database copies.

What do you need to know before you begin?
      Estimated time to complete this task: 1 minute

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mailbox database copies" entry
      in the High availability and site resilience permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online         , or Exchange Online Protection .

Use the EAC to move the active mailbox database
   1. In the EAC, go to Servers > Databases.

   2. Select the database whose copy you want to activate.

   3. In the Details pane, under Database Copies, click Activate under the database copy you
      want to activate.

<!-- p.2774 -->

   4. Click yes to activate the database copy.

Use the Exchange Management Shell to move the
active mailbox database
This example activates and mounts a copy of the database DB4 hosted on MBX3 as the new
active mailbox database. This command makes DB4 the new active mailbox database, and it
doesn't override the database mount dial settings on MBX3.

  PowerShell

  Move-ActiveMailboxDatabase DB4 -ActivateOnServer MBX3 -MountDialOverride:None

This example performs a switchover of the database DB2 to the Mailbox server MBX1. When
the command completes, MBX1 hosts the active copy of DB2. Because the MountDialOverride
parameter is set to None , MBX1 mounts the database using its own defined database auto
mount dial settings.

  PowerShell

  Move-ActiveMailboxDatabase DB2 -ActivateOnServer MBX1 -MountDialOverride:None

This example performs a switchover of the database DB1 to the Mailbox server MBX3. When
the command completes, MBX3 hosts the active copy of DB1. Because the MountDialOverride
parameter is specified with a value of Good Availability , MBX3 mounts the database using a
database auto mount dial setting of GoodAvailability.

  PowerShell

  Move-ActiveMailboxDatabase DB1 -ActivateOnServer MBX3 -
  MountDialOverride:GoodAvailability

This example performs a switchover of the database DB3 to the Mailbox server MBX4. When
the command completes, MBX4 hosts the active copy of DB3. Because the MountDialOverride
parameter isn't specified, MBX4 mounts the database using a database auto mount dial setting
of Lossless.

  PowerShell

  Move-ActiveMailboxDatabase DB3 -ActivateOnServer MBX4

<!-- p.2775 -->

This example performs a server switchover for the Mailbox server MBX1. All active mailbox
database copies on MBX1 will be activated on one or more other Mailbox servers with healthy
copies of the active databases on MBX1.

  PowerShell

  Move-ActiveMailboxDatabase -Server MBX1

This example performs a switchover of the database DB4 to the Mailbox server MBX5. In this
example, the database copy on MBX5 has a replay queue greater than 6. As a result, the
SkipLagChecks parameter must be specified to activate the database copy on MBX5.

  PowerShell

  Move-ActiveMailboxDatabase DB4 MBX5 -SkipLagChecks

This example performs a switchover of the database DB5 to the Mailbox server MBX6. In this
example, the database copy on MBX6 has a ContentIndexState of Failed. As a result, the
SkipClientExperienceChecks parameter must be specified to activate the database copy on
MBX6.

  PowerShell

  Move-ActiveMailboxDatabase DB5 MBX6 -SkipClientExperienceChecks

How do you know this worked?
To verify that you've successfully activated a mailbox database copy, do one of the following:

     In the EAC, navigate to Servers > Databases. Select the appropriate database, and in the
     Details pane, click View details to view the database copy properties.

     In the Exchange Management Shell, run the following command to display status
     information for a database copy.

        PowerShell

        Get-MailboxDatabaseCopyStatus <DatabaseCopyName> | Format-List

For more information

<!-- p.2776 -->

Mailbox database copies

Configure mailbox database copy properties

<!-- p.2777 -->

How to activate lagged mailbox database
copy
Article • 04/30/2025

APPLIES TO:        2016      2019     Subscription Edition

A lagged mailbox database copy is a mailbox database copy configured with a replay lag time
value greater than 0. If you want the database to replay all log files and make the database
copy current, activating and recovering a lagged mailbox database copy is a simple process.
However, if you want to replay log files up to a specific point in time, it's a more difficult
operation because you have to manually manipulate log files and run Eseutil.

Looking for other information related to lagged mailbox database copies? Check out Manage
mailbox database copies

  ７ Note

  The amount of time it takes to activate a lagged mailbox database copy directly depends
  on how many log files need to be replayed and how fast the hardware can replay them. At
  a minimum, you should experience a log replay rate of at least two logs per second per
  database.

What do you need to know before you begin?
      Estimated time to complete this task: 1 minute, plus the time it takes to duplicate the
      lagged copy, replay the necessary log files, and extract the data or mount the database
      for client activity.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mailbox database copies" entry
      in the High availability and site resilience permissions topic.

      The mailbox database copy being activated must be configured with a replay lag time
      greater than 0.

      The mailbox database copy being activated must have all log files to the point in time to
      which you want to recover it. Keep in mind that database transactions can span multiple
      log files when determining the point in time to which you want to recover.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

<!-- p.2778 -->

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online      , or Exchange Online Protection .

Use the Exchange Management Shell to activate a
lagged mailbox database copy to a specific point
in time

 ７ Note

 You can't use the EAC to activate a lagged mailbox database copy to a specific point in
 time. Instead, you perform a series of steps using the Exchange Management Shell and
 the command line.

 1. This example suspends replication for the lagged copy being activated by using the
   Suspend-MailboxDatabaseCopy cmdlet.

      PowerShell

      Suspend-MailboxDatabaseCopy DB1\EX3 -SuspendComment "Activate lagged copy of
      DB1 on Server EX3" -Confirm:$false

 2. Optionally (to preserve a lagged copy), make a copy of the database copy and its log files.

      ７ Note

      At this point, continuing to perform this procedure on the existing volume would
      incur a copy on write performance penalty. As an alternative, you can copy the
      database and log files to another volume to perform the recovery.

 3. Determine which log files are required to replay into the database to meet your point-in-
   time requirement for this recovery (based on log file date and time, as shown in Windows
   Explorer). All logs created after this point should be moved to a different directory, until
   the recovery process is completed, and the logs are no longer needed.

 4. Delete the checkpoint (.chk) file for the database.

 5. This example uses Eseutil to perform the recovery operation.

<!-- p.2779 -->

       PowerShell

       Eseutil.exe /r eXX /a

       ７ Note

             If the database being recovered is "out of place", be sure to specify the log file,
             checkpoint, and database paths in the eseutil command. For example:
             eseutil.exe /R E00 /a /l "c:\DBRecovery" /s "c:\DBRecovery" /d

             "c:\DBRecovery" .

             In the preceding example, e XX is the log generation prefix for the database
             (for example, E00, E01, E02, and so on).

             This step may take a considerable amount of time, depending on several
             factors, such as the length of the replay lag time, the number of log files
             generated during that period, and the speed at which your hardware can replay
             those logs into the database being recovered.

  6. After log replay is finished, the database is in a clean shutdown state and can be copied
     and used for recovery purposes.

  7. After the recovery process is complete, this example resumes replication for the database
     that was used as part of the recovery process.

       PowerShell

       Resume-MailboxDatabaseCopy DB1\EX3

For detailed syntax and parameter information, see Suspend-MailboxDatabaseCopy or
Resume-MailboxDatabaseCopy.

Use the Exchange Management Shell to activate a
lagged mailbox database copy by replaying all
uncommitted log files
  1. Optionally (to preserve a lagged copy), make a copy of the database copy and its log files.

<!-- p.2780 -->

 2. This example suspends replication for the lagged copy being activated by using the
    Suspend-MailboxDatabaseCopy cmdlet.

       PowerShell

       Suspend-MailboxDatabaseCopy DB1\EX3 -SuspendComment "Activate lagged copy of
       DB1 on Server EX3" -Confirm:$false

 3. Optionally (to preserve a lagged copy), make a copy of the database copy and its log files.

       ７ Note

       At this point, continuing to perform this procedure on the existing volume would
       incur a copy on write performance penalty. If this isn't desirable, you can copy the
       database and log files to another volume to perform the recovery.

 4. This example activates the lagged mailbox database copy using the Move-
    ActiveMailboxDatabase cmdlet with the SkipLagChecks parameter.

 PowerShell

 Move-ActiveMailboxDatabase DB1 -ActivateOnServer EX3 -SkipLagChecks

Use the Exchange Management Shell to activate a
lagged mailbox database copy by using SafetyNet
recovery
 1. Optionally (to preserve a lagged copy), take a file system-based (non-Exchange aware)
    Volume Shadow Copy Service (VSS) snapshot of the volumes containing the database
    copy and its log files.

 2. This example suspends replication for the lagged copy being activated by using the
    Suspend-MailboxDatabaseCopy cmdlet.

       PowerShell

       Suspend-MailboxDatabaseCopy DB1\EX3 -SuspendComment "Activate lagged copy of
       DB1 on Server EX3" -Confirm:$false

 3. Optionally (to preserve a lagged copy), make a copy of the database copy and its log files.

<!-- p.2781 -->

       ７ Note

       At this point, continuing to perform this procedure on the existing volume would
       incur a copy-on-write performance penalty. If this isn't desirable, you can copy the
       database and log files to another volume to perform the recovery.

   4. Determine the required logs for the lagged database copy by looking for the "Log
     Required:" value in ESEUTIL database header output

       PowerShell

        Eseutil /mh <DBPath> | findstr /c:"Log Required"

     Take note of the hexadecimal numbers in parentheses. The first number is the lowest
     generation required (referred to as LowGeneration), and the second number is the
     highest generation required (referred to as HighGeneration). Move all log generation files
     that have a generation sequence greater than HighGeneration to a different location so
     that they are not replayed into the database.

   5. On the server hosting the active copy of database, either delete the log files for the
     lagged copy being activated from the active copy, or stop the Microsoft Exchange
     Replication service.

   6. Perform a database switchover and activate the lagged copy. This example activates the
     database by using the Move-ActiveMailboxDatabase cmdlet with several parameters.

       PowerShell

        Move-ActiveMailboxDatabase DB1 -ActivateOnServer EX3 -MountDialOverride
        BestEffort -SkipActiveCopyChecks -SkipClientExperienceChecks -
        SkipHealthChecks -SkipLagChecks

   7. At this point, the database will automatically mount and request redelivery of missing
     messages from SafetyNet.

How do you know this worked?
To verify that you've successfully activated a lagged mailbox database copy, do one of the
following:

     In the EAC, navigate to Servers > Databases. Select the appropriate database, and in the
     Details pane, click View details to view the database copy properties.

<!-- p.2782 -->

In the Exchange Management Shell, run the following command to display status
information for a database copy.

  PowerShell

  Get-MailboxDatabaseCopyStatus <DatabaseCopyName> | Format-List

<!-- p.2783 -->

Remove a mailbox database copy in
Exchange Server
07/23/2025

APPLIES TO:      2016      2019      Subscription Edition

You can use these procedures to remove a copy of a mailbox database, but you can't use them
to remove the last copy of a mailbox database. For detailed steps about how to remove the
last copy of a mailbox database, see Remove a mailbox database or Remove-MailboxDatabase.

Looking for other management tasks related to mailbox database copies? Check out Manage
mailbox database copies.

What do you need to know before you begin?
     Estimated time to complete this task: 1 minute

     Mailbox database copies can only be removed from a healthy database availability group
     (DAG). If the DAG isn't healthy (for example, the DAG's underlying cluster is down because
     quorum was lost), you won't be able to remove any mailbox database copies.

     If you're removing the last passive copy of the database, continuous replication circular
     logging (CRCL) must not be enabled for the specified mailbox database. If CRCL is
     enabled, you must first disable it. After the mailbox database copy has been removed,
     circular logging can be enabled. Once enabled for a non-replicated mailbox database, JET
     circular logging is used instead of CRCL. If you aren't removing the last passive copy of a
     database, CRCL can remain enabled.

     After removing a database copy, you must manually delete any database and transaction
     log files from the server from which the database copy is being removed.

     To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
     Management Shell, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Mailbox database copies" entry
     in the High availability and site resilience permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

<!-- p.2784 -->

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the EAC to remove a mailbox database copy
   1. In the EAC, go to Servers > Databases.

   2. Select the mailbox database whose copy you want to remove.

   3. In the Details pane, locate the passive copy you want to remove and click Remove.

   4. Confirm the removal on the warning dialog box by clicking yes.

   5. Click ok to confirm the removal after reviewing any messages.

   6. Manually delete any database and transaction log files from the server from which the
     database copy is being removed.

Use the Exchange Management Shell to remove a
mailbox database copy
This example removes a copy of the mailbox database DB1 from the Mailbox server MBX1.

  PowerShell

  Remove-MailboxDatabaseCopy -Identity DB1\MBX1 -Confirm:$False

For detailed syntax and parameter information, see Remove-MailboxDatabaseCopy.

How do you know this worked?
To verify that you've successfully removed a mailbox database copy, do one of the following:

     In the EAC, navigate to Servers > Databases. Select the appropriate database, and in the
     Details pane, the removed passive copy is no longer listed.

     In the Exchange Management Shell, run the following command to verify removal of the
     copy.

        PowerShell

<!-- p.2785 -->

  Get-MailboxDatabase <DatabaseName> | Format-List DatabaseCopies

The removed passive copy is no longer listed.

<!-- p.2786 -->

Monitor database availability groups
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

You can use the details in this topic for monitoring mailbox database copies for database
availability groups (DAGs), for gathering diagnostic information, and for configuring the low
disk space monitoring threshold.

Get-MailboxDatabaseCopyStatus cmdlet
Use the Get-MailboxDatabaseCopyStatus cmdlet to view status information about mailbox
database copies. This cmdlet enables you to view information about all copies of a particular
database, information about a specific copy of a database on a specific server, or information
about all database copies on a server. The following table describes possible values for the
copy status of a mailbox database copy.

Database copy status

                                                                                           ﾉ   Expand table

 Database copy status              Description

 Failed                            The mailbox database copy is in a Failed state because it isn't
                                   suspended, and it isn't able to copy or replay log files. While in a
                                   Failed state and not suspended, the system will periodically check
                                   whether the problem that caused the copy status to change to Failed
                                   has been resolved. After the system has detected that the problem is
                                   resolved, and barring no other issues, the copy status will
                                   automatically change to Healthy.

 Seeding                           The mailbox database copy is being seeded, the content index for
                                   the mailbox database copy is being seeded, or both are being
                                   seeded. Upon successful completion of seeding, the copy status
                                   should change to Initializing.

 SeedingSource                     The mailbox database copy is being used as a source for a database
                                   copy seeding operation.

 Suspended                         The mailbox database copy is in a Suspended state as a result of an
                                   administrator manually suspending the database copy by running
                                   the Suspend-MailboxDatabaseCopy cmdlet.

 Healthy                           The mailbox database copy is successfully copying and replaying log
                                   files, or it has successfully copied and replayed all available log files.

<!-- p.2787 -->

Database copy status             Description

ServiceDown                      The Microsoft Exchange Replication service isn't available or running
                                 on the server that hosts the mailbox database copy.

Initializing                     The mailbox database copy is in an Initializing state when a database
                                 copy has been created, when the Microsoft Exchange Replication
                                 service is starting or has just been started, and during transitions
                                 from Suspended, ServiceDown, Failed, Seeding, or SinglePageRestore
                                 to another state. While in this state, the system is verifying that the
                                 database and log stream are in a consistent state. In most cases, the
                                 copy status will remain in the Initializing state for about 15 seconds,
                                 but in all cases, it should generally not be in this state for longer than
                                 30 seconds.

Resynchronizing                  The mailbox database copy and its log files are being compared with
                                 the active copy of the database to check for any divergence between
                                 the two copies. The copy status will remain in this state until any
                                 divergence is detected and resolved.

Mounted                          The active copy is online and accepting client connections. Only the
                                 active copy of the mailbox database copy can have a copy status of
                                 Mounted.

Dismounted                       The active copy is offline and not accepting client connections. Only
                                 the active copy of the mailbox database copy can have a copy status
                                 of Dismounted.

Mounting                         The active copy is coming online and not yet accepting client
                                 connections. Only the active copy of the mailbox database copy can
                                 have a copy status of Mounting.

Dismounting                      The active copy is going offline and terminating client connections.
                                 Only the active copy of the mailbox database copy can have a copy
                                 status of Dismounting.

DisconnectedAndHealthy           The mailbox database copy is no longer connected to the active
                                 database copy, and it was in the Healthy state when the loss of
                                 connection occurred. This state represents the database copy with
                                 respect to connectivity to its source database copy. It may be
                                 reported during DAG network failures between the source copy and
                                 the target database copy.

DisconnectedAndResynchronizing   The mailbox database copy is no longer connected to the active
                                 database copy, and it was in the Resynchronizing state when the loss
                                 of connection occurred. This state represents the database copy with
                                 respect to connectivity to its source database copy. It may be
                                 reported during DAG network failures between the source copy and
                                 the target database copy.

<!-- p.2788 -->

 Database copy status             Description

 FailedAndSuspended               The Failed and Suspended states have been set simultaneously by
                                  the system because a failure was detected, and because resolution of
                                  the failure explicitly requires administrator intervention. An example
                                  is if the system detects unrecoverable divergence between the active
                                  mailbox database and a database copy. Unlike the Failed state, the
                                  system won't periodically check whether the problem has been
                                  resolved, and automatically recover. Instead, an administrator must
                                  intervene to resolve the underlying cause of the failure before the
                                  database copy can be transitioned to a healthy state.

 SinglePageRestore                This state indicates that a single page restore operation is occurring
                                  on the mailbox database copy.

The Get-MailboxDatabaseCopyStatus cmdlet also returns details about the in-use replication
networks, including IncomingLogCopyingNetwork, which is returned for passive database
copies, and OutgoingConnections, which is returned for active databases that have more than
one copy, as well as any database copy being used as a source for a database seeding
operation. Outgoing connection information is provided for database copies that are in file
mode replication. Outgoing connection information is not provided for database copies that
are in block mode replication.

Get-MailboxDatabaseCopyStatus examples
The following examples use the Get-MailboxDatabaseCopyStatus cmdlet. Each example pipes
the results to the Format-List cmdlet to display the output in list format.

This example returns status information for all copies of the database DB2.

  PowerShell

  Get-MailboxDatabaseCopyStatus -Identity DB2 | Format-List

This example returns the status for all database copies on the Mailbox server MBX2.

  PowerShell

  Get-MailboxDatabaseCopyStatus -Server MBX2 | Format-List

This example returns the status for all database copies on the local Mailbox server.

  PowerShell

<!-- p.2789 -->

  Get-MailboxDatabaseCopyStatus -Local | Format-List

For more information about using the Get-MailboxDatabaseCopyStatus cmdlet, see Get-
MailboxDatabaseCopyStatus.

Test-ReplicationHealth cmdlet
You can use the Test-ReplicationHealth cmdlet to view continuous replication status
information about mailbox database copies. This cmdlet can be used to check all aspects of the
replication and replay status to provide a complete overview of a specific Mailbox server in a
DAG.

The Test-ReplicationHealth cmdlet is designed for the proactive monitoring of continuous
replication and the continuous replication pipeline, the availability of Active Manager, and the
health and status of the underlying cluster service, quorum, and network components. It can be
run locally on or remotely against any Mailbox server in a DAG. The Test-ReplicationHealth
cmdlet performs the tests listed in the following table.

Test-ReplicationHealth cmdlet tests

                                                                                        ﾉ   Expand table

 Test name               Description

 ClusterService          Verifies that the Cluster service is running and reachable on the specified DAG
                         member, or if no DAG member is specified, on the local server.

 ReplayService           Verifies that the Microsoft Exchange Replication service is running and
                         reachable on the specified DAG member, or if no DAG member is specified, on
                         the local server.

 ActiveManager           Verifies that the instance of Active Manager running on the specified DAG
                         member, or if no DAG member is specified, the local server, is in a valid role
                         (primary, secondary, or stand-alone).

 TasksRpcListener        Verifies that the tasks remote procedure call (RPC) server is running and
                         reachable on the specified DAG member, or if no DAG member is specified, on
                         the local server.

 TcpListener             Verifies that the TCP log copy listener is running and reachable on the specified
                         DAG member, or if no DAG member is specified, on the local server.

 ServerLocatorService    Verifies the Active Manager client/server processes on DAG members and on
                         the Client Access Server that perform lookups in Active Directory and Active
                         Manager to determine where a user's mailbox database is active.

<!-- p.2790 -->

 Test name               Description

 DagMembersUp            Verifies that all DAG members are available, running, and reachable.

 ClusterNetwork          Verifies that all cluster-managed networks on the specified DAG member, or if
                         no DAG member is specified, the local server, are available.

 QuorumGroup             Verifies that the default cluster group (quorum group) is in a healthy and
                         online state.

 FileShareQuorum         Verifies that the witness server and witness directory and share configured for
                         the DAG are reachable.

 DatabaseRedundancy      Verifies that there is at least one healthy copy available of the databases on the
                         specified DAG member, or if no DAG member is specified, on the local server.

 DatabaseAvailability    Verifies that the databases have sufficient availability on the specified DAG
                         member, or if no DAG member is specified, on the local server.

 DBCopySuspended         Checks whether any mailbox database copies are in a state of Suspended on
                         the specified DAG member, or if no DAG member is specified, on the local
                         server.

 DBCopyFailed            Checks whether any mailbox database copies are in a state of Failed on the
                         specified DAG member, or if no DAG member is specified, on the local server.

 DBInitializing          Checks whether any mailbox database copies are in a state of Initializing on
                         the specified DAG member, or if no DAG member is specified, on the local
                         server.

 DBDisconnected          Checks whether any mailbox database copies are in a state of Disconnected on
                         the specified DAG member, or if no DAG member is specified, on the local
                         server.

 DBLogCopyKeepingUp      Verifies that log copying and inspection by the passive copies of databases on
                         the specified DAG member, or if no DAG member is specified, on the local
                         server, are able to keep up with log generation activity on the active copy.

 DBLogReplayKeepingUp    Verifies that replay activity for the passive copies of databases on the specified
                         DAG member, or if no DAG member is specified, on the local server, is able to
                         keep up with log copying and inspection activity.

Test-ReplicationHealth example
This example uses the Test-ReplicationHealth cmdlet to test the health of replication for the
Mailbox server MBX1.

  PowerShell

<!-- p.2791 -->

  Test-ReplicationHealth -Identity MBX1

Crimson channel event logging
Windows includes two categories of event logs: Windows logs, and Applications and Services
logs. The Windows logs category includes the event logs available in previous versions of
Windows: Application, Security, and System event logs. It also includes two new logs: the Setup
log and the ForwardedEvents log. Windows logs are intended to store events from legacy
applications and events that apply to the entire system.

Applications and Services logs are a new category of event logs. These logs store events from a
single application or component rather than events that might have system-wide impact. This
new category of event logs is referred to as an application's crimson channel.

The Applications and Services logs category includes four subtypes: Admin, Operational,
Analytic, and Debug logs. Events in Admin logs are of particular interest if you use event log
records to troubleshoot problems. Events in the Admin log should provide you with guidance
about how to respond to the events. Events in the Operational log are also useful, but may
require more interpretation. Admin and Debug logs aren't as user friendly. Analytic logs (which
by default are hidden and disabled) store events that trace an issue, and often a high volume
of events are logged. Debug logs are used by developers when debugging applications.

Exchange Server logs events to crimson channels in the Applications and Services logs area.
You can view these channels by performing these steps:

   1. Open Event Viewer.

   2. In the console tree, navigate to Applications and Services Logs > Microsoft > Exchange.

   3. Under Exchange, select a crimson channel, such as HighAvailability or
     MailboxDatabaseFailureItems to see DAG and database copy-related events, or
     ActiveMontoring or ManagedAvailability to see events related to Managed Availability.

The HighAvailability channel contains events related to startup and shutdown of the Microsoft
Exchange Replication service, and the various components that run within the Microsoft
Exchange Replication service, such as Active Manager, the third-party synchronous replication
API, the tasks RPC server, TCP listener, and Volume Shadow Copy Service (VSS) writer. The
HighAvailability channel is also used by Active Manager to log events related to Active
Manager role monitoring and database action events, such as a database mount operation and
log truncation, and to record events related to the DAG's underlying cluster.

<!-- p.2792 -->

The MailboxDatabaseFailureItems channel is used to log events associated with any failures
that affect a replicated mailbox database.

The ActiveMonitoring channel contains definition and result events for Managed Availability
probes, monitors and responders.

The ManagedAvailability channel contains recovery action logs and results and related events.

Low Disk Space Monitor
Exchange Server Managed Availability monitors hundreds of system metrics and components
every minute, including the amount of free disk space on volumes used by the Mailbox server
role. Prior to Exchange 2013 Service Pack 1 (SP1), Exchange monitored available space on all
local volumes, including volumes that don't contain any databases or log files. In Exchange
2016 and Exchange 2019, only volumes that contain Exchange databases and log files are
monitored. The default threshold for the low volume space monitor is 180 GB. You can
configure the threshold by adding the following DWORD registry value (in MB) on each
Mailbox server that you want to customize:

Path: HKEY_LOCAL_MACHINE\Software\Microsoft\ExchangeServer\v15\Replay\Parameters

Value: SpaceMonitorLowSpaceThresholdInMB

For example to configure the threshold to 100 GB, you would configure the following registry
value:

REG_DWORD 186a0 (100000)

After configuring or modifying the above registry value, you must restart the Microsoft
Exchange DAG Management service for the change to take effect.

CollectOverMetrics.ps1 script
Exchange Server includes a script called CollectOverMetrics.ps1, which can be found in the
Scripts folder. CollectOverMetrics.ps1 reads DAG member event logs to gather information
about database operations (such as database mounts, moves, and failovers) over a specific
time period. For each operation, the script records the following information:

     Identity of the database

     Time at which the operation began and ended

     Servers on which the database was mounted at the start and finish of the operation

<!-- p.2793 -->

     Reason for the operation

     Whether the operation was successful, and if the operation failed, the error details

The script writes this information to .csv files with one operation per row. It writes a separate
.csv file for each DAG.

The script supports parameters that allow you to customize the script's behavior and output.
For example, the results can be restricted to a specified subset by using the Database or
ReportFilter parameters. Only the operations that match these filters will be included in the
summary HTML report. The available parameters are listed in the following table.

CollectOverMetrics.ps1 script parameters

                                                                                          ﾉ    Expand table

 Parameter                   Description

 DatabaseAvailabilityGroup   Specifies the name of the DAG from which you want to collect metrics. If this
                             parameter is omitted, the DAG of which the local server is a member will be
                             used. Wildcard characters can be used to collect information from and report
                             on multiple DAGs.

 Database                    Provides a list of databases for which the report needs to be generated.
                             Wildcard characters are supported, for example, -Database:"DB1","DB2" or -
                             Database:"DB*" .

 StartTime                   Specifies the duration of the time period to report on. The script gathers only
                             the events logged during this period. As a result, the script may capture
                             partial operation records (for example, only the end of an operation at the
                             start of the period or vice-versa). If neither StartTime nor EndTime is
                             specified, the script defaults to the past 24 hours. If only one parameter is
                             specified, the period will be 24 hours, either beginning or ending at the
                             specified time.

 EndTime                     Specifies the duration of the time period to report on. The script gathers only
                             the events logged during this period. As a result, the script may capture
                             partial operation records (for example, only the end of an operation at the
                             start of the period or vice-versa). If neither StartTime nor EndTime is
                             specified, the script defaults to the past 24 hours If only one parameter is
                             specified, the period will be 24 hours, either beginning or ending at the
                             specified time.

 ReportPath                  Specifies the folder used to store the results of event processing. If this
                             parameter is omitted, the Scripts folder will be used. When specified, the
                             script takes a list of .csv files generated by the script and uses them as the
                             source data to generate a summary HTML report. The report is the same one
                             that's generated with the -GenerateHtmlReport option. The files can be

<!-- p.2794 -->

Parameter                Description

                         generated across multiple DAGs at many different times, or even with
                         overlapping times, and the script will merge all of their data together.

GenerateHtmlReport       Specifies that the script gather all the information it has recorded, group the
                         data by the operation type, and then generate an HTML file that includes
                         statistics for each of these groups. The report includes the total number of
                         operations in each group, the number of operations that failed, and statistics
                         for the time taken within each group. The report also contains a breakdown
                         of the types of errors that resulted in failed operations.

ShowHtmlReport           Specifies that the HTML-generated report should be displayed in a Web
                         browser after it's generated.

SummariseCsvFiles        Specifies that the script read the data from existing .csv files that were
                         previously generated by the script. This data is then used to generate a
                         summary report similar to the report generated by the GenerateHtmlReport
                         parameter.

ActionType               Specifies the type of operational actions the script should collect. The values
                         for this parameter are Move , Mount , ismount , and Remount . The Move value
                         refers to any time that the database changes its active server, whether by
                         controlled moves or by failovers. The Mount , Dismount , and Remount values
                         refer to times that the database changes its mounted status without moving
                         to another computer.

ActionTrigger            Specifies which administrative operations should be collected by the script.
                         The values for this parameter are Admin or Automatic . Automatic actions are
                         those performed automatically by the system (for example, a failover when a
                         server goes offline). Admin actions are any actions that were performed by
                         an administrator using either the Exchange Management Shell or the
                         Exchange admin center.

RawOutput                Specifies that the script writes the results that would have been written to
                         .csv files directly to the output stream, as would happen with write-output.
                         This information can then be piped to other commands.

IncludedExtendedEvents   Specifies that the script collects the events that provide diagnostic details of
                         times spent mounting databases. This can be a time-consuming stage if the
                         Application event log on the servers is large.

MergeCSVFiles            Specifies that the script takes all the .csv files containing data about each
                         operation and merges them into a single .csv file.

ReportFilter             Specifies that a filter should be applied to the operations using the fields as
                         they appear in the .csv files. This parameter uses the same format as a Where
                         operation, with each element set to $_ and returning a Boolean value. For
                         example: {$_DatabaseName -notlike "Mailbox Database*"} can be used to
                         exclude the default databases from the report.

<!-- p.2795 -->

CollectOverMetrics.ps1 examples
The following example collects metrics for all databases that match DB* (which includes a
wildcard character) in the DAG DAG1. After the metrics are collected, an HTML report is
generated and displayed.

  PowerShell

  CollectOverMetrics.ps1 -DatabaseAvailabilityGroup DAG1 -Database:"DB*" -
  GenerateHTMLReport -ShowHTMLReport

The following examples demonstrate ways that the summary HTML report may be filtered. The
first uses the Database parameter, which takes a list of database names. The summary report
then contains data only about those databases. The next two examples use the ReportFilter
option. The last example filters out all the default databases.

  PowerShell

  CollectOverMetrics.ps1 -SummariseCsvFiles (dir *.csv) -Database
  MailboxDatabase123,MailboxDatabase456

  PowerShell

  CollectOverMetrics.ps1 -SummariseCsvFiles (dir *.csv) -ReportFilter
  {$_.DatabaseName -notlike "Mailbox Database*"}

  PowerShell

  CollectOverMetrics.ps1 -SummariseCsvFiles (dir *.csv) -ReportFilter
  {($_.ActiveOnStart -like "ServerXYZ*") -and ($_.ActiveOnEnd -notlike
  "ServerXYZ*")}

CollectReplicationMetrics.ps1 script
CollectReplicationMetrics.ps1 is another health metric script included in Exchange Server. This
script provides an active form of monitoring because it collects metrics in real time, while the
script is running. CollectReplicationMetrics.ps1 collects data from performance counters related
to database replication. The script gathers counter data from multiple Mailbox servers, writes
each server's data to a .csv file, and then reports various statistics across all of this data (for
example, the amount of time each copy was failed or suspended, the average copy or replay
queue length, or the amount of time that copies were outside of their failover criteria).

<!-- p.2796 -->

You can either specify the servers individually, or you can specify entire DAGs. You can either
run the script to first collect the data and then generate the report, or you can run it to just
gather the data or to only report on data that's already been collected. You can specify the
frequency at which data should be sampled and the total duration to gather data.

The data collected from each server is written to a file named CounterData.<ServerName>.
<TimeStamp>.csv. The summary report will be written to a file named HaReplPerfReport.
<DAGName>.<TimeStamp>.csv, or HaReplPerfReport.<TimeStamp>.csv if you didn't run the
script with the DagName parameter.

The script starts Windows PowerShell jobs to collect the data from each server. These jobs run
for the full period in which data is being collected. If you specify a large number of servers, this
process can use a considerable amount of memory. The final stage of the process, when data is
processed into a summary report, can also be quite time consuming for large amounts of data.
It's possible to run the collection stage on one computer, and then copy the data elsewhere for
processing.

The CollectReplicationMetrics.ps1 script supports parameters that allow you to customize the
script's behavior and output. The available parameters are listed in the following table.

CollectReplicationMetrics.ps1 script parameters

                                                                                          ﾉ    Expand table

 Parameter            Description

 DagName              Specifies the name of the DAG from which you want to collect metrics. If this
                      parameter is omitted, the DAG of which the local server is a member will be used.

 DatabaseNames        Provides a list of databases for which the report needs to be generated. Wildcard
                      characters are supported for use, for example, -DatabaseNames:"DB1","DB2" or -
                      DatabaseNames:"DB*" .

 ReportPath           Specifies the folder used to store the results of event processing. If this parameter
                      is omitted, the Scripts folder will be used.

 Duration             Specifies the amount of time the collection process should run. Typical values
                      would be one to three hours. Longer durations should be used only with long
                      intervals between each sample or as a series of shorter jobs run by scheduled
                      tasks.

 Frequency            Specifies the frequency at which data metrics are collected. Typical values would
                      be 30 seconds, one minute, or five minutes. Under normal circumstances, intervals
                      that are shorter than these won't show significant changes between each sample.

 Servers              Specifies the identity of the servers from which to collect statistics. You can specify
                      any value, including wildcard characters or GUIDs.

<!-- p.2797 -->

 Parameter            Description

 SummariseFiles       Specifies a list of .csv files to generate a summary report. These files are the files
                      named CounterData.<CounterData>* and are generated by the
                      CollectReplicationMetrics.ps1 script.

 Mode                 Specifies the processing stages that the script executes. You can use the following
                      values:
                      CollectAndReport : This is the default value. This value signifies that the script
                      should both collect the data from the servers and then process them to produce
                      the summary report.
                       CollectOnly : This value signifies that the script should just collect the data and not
                      produce the report.
                      ProcessOnly : This value signifies that the script should import data from a set of
                      .csv files and process them to produce the summary report. The SummariseFiles
                      parameter is used to provide the script with the list of files to process.

 MoveFilestoArchive   Specifies that the script should move the files to a compressed folder after
                      processing.

 LoadExchangeSnapin   Specifies that the script should load the Exchange Management Shell commands.
                      This parameter is useful when the script needs to run from outside the Exchange
                      Management Shell, such as in a scheduled task.

CollectReplicationMetrics.ps1 example
The following example gathers one hour's worth of data from all the servers in the DAG DAG1,
sampled at one minute intervals, and then generates a summary report. In addition, the
ReportPath parameter is used, which causes the script to place all the files in the current
directory.

  PowerShell

  CollectReplicationMetrics.ps1 -DagName DAG1 -Duration "01:00:00" -Frequency
  "00:01:00" -ReportPath

The following example reads the data from all the files matching CounterData* and then
generates a summary report.

  PowerShell

  CollectReplicationMetrics.ps1 -SummariseFiles (dir CounterData*) -Mode ProcessOnly
  -ReportPath

<!-- p.2798 -->

Switchovers and failovers
Article • 04/30/2025

APPLIES TO:        2016       2019    Subscription Edition

Switchovers and failovers are the two forms of outages in Microsoft Exchange Server:

      A switchover is a scheduled outage of a database or server that's explicitly initiated by a
      cmdlet or by the managed availability system in Exchange Server. Switchovers are typically
      done to prepare for performing a maintenance operation. Switchovers involve moving the
      active mailbox database copy to another server in the database availability group (DAG). If no
      healthy target is found during a switchover, administrators will receive an error and the
      mailbox database will remain up, or mounted.

      A failover refers to unexpected events that result in the unavailability of services, data, or both.
      A failover involves the system automatically recovering from the failure by activating a passive
      mailbox database copy to make it the active mailbox database copy. If no healthy target is
      found during a failover, the mailbox database will be dismounted.

Exchange Server is designed to handle both switchovers and failovers.

Looking for management tasks related to high availability and site resilience? See Managing high
availability and site resilience.

Switchovers
There are three types of switchovers in Exchange Server:

      Database switchovers

      Server switchovers

      Datacenter switchovers

Database Switchovers
A database switchover is the process by which an individual active database is switched over to
another database copy (a passive copy), and that database copy is made the new active database
copy. Database switchovers can happen both within and across datacenters. A database switchover
can be performed by using the Exchange admin center (EAC) or the Exchange Management Shell.
Regardless of which interface is used, the switchover process is as follows:

   1. The administrator initiates a database switchover to move the current active mailbox database
      copy to another server.

<!-- p.2799 -->

  2. The client used for the task makes an RPC call to the Microsoft Exchange Replication service
        on a DAG member.

  3. If the DAG member doesn't hold the Primary Active Manager (PAM) role, the DAG member
        refers the task to the server that holds the PAM role.

  4. The task makes an RPC call to the Microsoft Exchange Replication service on the server that
        holds the PAM role.

  5. The PAM reads and updates the database location information that's stored in the cluster
        database for the DAG.

  6. The PAM contacts the Microsoft Exchange Replication service on the DAG member whose
        passive copy is being activated as the new active mailbox database copy.

  7. The Microsoft Exchange Replication service on the target server queries the Microsoft
        Exchange Replication services on all other DAG members to determine the best log source for
        the database copy.

  8. The database is dismounted from the current server and the Microsoft Exchange Replication
        service on the target server copies the remaining logs to the target server.

  9. The Microsoft Exchange Replication service on the target server requests a database mount.

 10. The Microsoft Exchange Information Store service on the target server replays the log files
        and mounts the database.

 11. Any error codes are returned to the Microsoft Exchange Replication service on the target
        server.

 12. The PAM updates the database copy state information in the cluster database for the DAG.

 13. Any error codes are returned by the Microsoft Exchange Replication service on the target
        server to the Microsoft Exchange Replication service on the PAM.

 14. The Microsoft Exchange Replication service on the PAM returns any errors to the
        administrative interface where the task was called.

 15. Remote PowerShell returns the results of the operation to the calling administrative interface.

For detailed steps about how to perform a database switchover, see Activate a mailbox database
copy.

Server Switchovers
A server switchover is the process by which all active databases on a DAG member are activated on
one or more other DAG members. Like database switchovers, a server switchover can occur both

<!-- p.2800 -->

within a datacenter and across datacenters, and it can be initiated by using both the EAC and the
Exchange Management Shell. Regardless of which interface is used, the server switchover process is
as follows:

   1. The administrator initiates a server switchover to move all current active mailbox database
     copies to one or more other servers.

   2. The task performs the same steps described earlier in this topic for database switchovers
     (Steps 2 through 4) for each of the active databases on the current server.

   3. The PAM reads and updates the database location information that's stored in the cluster
     database for the DAG.

   4. The PAM contacts the Microsoft Exchange Replication service on each DAG member that has
     a passive copy being activated.

   5. The Microsoft Exchange Replication service on the target servers query the Microsoft
     Exchange Replication services on all other DAG members to determine the best log source for
     the database copy.

   6. The database is dismounted from the current server and the Microsoft Exchange Replication
     service on each target server copies the remaining logs.

   7. The Microsoft Exchange Replication service on each target server requests a database mount.

   8. The Microsoft Exchange Information Store service on each target server replays the log files
     and mounts the database.

   9. Any error codes are returned to the Microsoft Exchange Replication service on the target
     server.

 10. The PAM updates the database copy state information in the cluster database for the DAG.

 11. Any error codes are returned by the Microsoft Exchange Replication service on the target
     server to the Microsoft Exchange Replication service on the PAM.

 12. The Microsoft Exchange Replication service on the PAM returns any errors to the
     administrative interface where the task was called.

 13. Remote PowerShell returns the results of the operation to the calling administrative interface.

For detailed steps about how to perform a server switchover, see Perform a server switchover.

Datacenter Switchovers
In a site resilient configuration, automatic recovery in response to a site-level failure can occur
within a DAG, allowing the messaging system to remain in a functional state. This configuration
