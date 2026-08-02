---
title: "Welcome — pages 681-720"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0681-0720
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0681-0720
family: sccm
documentKind: "doc"
abstract: "3. WSUS maintenance can be performed simultaneously on multiple servers in the same tier. When doing so, ensure that one tier is done before moving onto the next one. The cleanup and reindex steps described below should be run on all WSUS servers, regardless of whether they are"
---

# Welcome — pages 681-720

<!-- p.681 -->

  3. WSUS maintenance can be performed simultaneously on multiple servers in the same tier.
     When doing so, ensure that one tier is done before moving onto the next one. The
     cleanup and reindex steps described below should be run on all WSUS servers, regardless
     of whether they are a replica WSUS server or not. For more information about
     determining if a WSUS server is a replica, see Decline superseded updates.

  4. Ensure that SUPs don't sync during the maintenance process, as it may cause a loss of
     some work already done. Check the SUP sync schedule and temporarily set it to manual
     during this process.

  5. If you have multiple SUPs of the primary site or central administration sit (CAS) which
     don't share the SUSDB, consider the WSUS server that syncs with the first SUP on the site
     as residing in a tier below the site. For example, my CAS site has two SUPs:

          The one named New syncs with Microsoft Update, it would be my top tier (Tier1).
          The server named 2012 syncs with New, and it would be considered in the second
          tier. It can be cleaned up at the same time I would do all my other Tier2 servers,
          such as my primary site's single SUP.

Perform WSUS maintenance
The basic steps necessary for proper WSUS maintenance include:

<!-- p.682 -->

   1. Back up the WSUS database
   2. Create custom indexes
   3. Reindex the WSUS database
   4. Decline superseded updates
   5. Run the WSUS Server Cleanup Wizard

Back up the WSUS database
Back up the WSUS database (SUSDB) by using the desired method. For more information, see
Create a Full Database Backup.

Create custom indexes
This process is optional but recommended, it greatly improves performance during subsequent
cleanup operations.

If you are using Configuration Manager current branch version 1906 or a later version, we
recommend that you use Configuration Manager to create the indexes. To create the indexes,
configure the Add non-clustered indexes to the WSUS database option in the software
update point configuration for the top-most site.

If you use an older version of Configuration Manager or standalone WSUS servers, follow these
steps to create custom indexes in the SUSDB database. For each SUSDB, it's a one-time
process.

   1. Make sure that you have a backup of the SUSDB database.

<!-- p.683 -->

   2. Use SQL Management Studio to connect to the SUSDB database, in the same manner as
     described in the Reindex the WSUS database section.

   3. Run the following script against SUSDB, to create two custom indexes:

       SQL

       -- Create custom index in tbLocalizedPropertyForRevision
       USE [SUSDB]

       CREATE NONCLUSTERED INDEX [nclLocalizedPropertyID] ON [dbo].
       [tbLocalizedPropertyForRevision]
       (
            [LocalizedPropertyID] ASC
       )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF,
       DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS =
       ON) ON [PRIMARY]

       -- Create custom index in tbRevisionSupersedesUpdate
       CREATE NONCLUSTERED INDEX [nclSupercededUpdateID] ON [dbo].
       [tbRevisionSupersedesUpdate]
       (
            [SupersededUpdateID] ASC
       )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF,
       DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS =
       ON) ON [PRIMARY]

     If custom indexes have been previously created, running the script again results in an
     error similar to the following one:

       Msg 1913, Level 16, State 1, Line 4
       The operation failed because an index or statistics with name 'nclLocalizedPropertyID'
       already exists on table 'dbo.tbLocalizedPropertyForRevision'.

Reindex the WSUS database
To reindex the WSUS database (SUSDB), use the Reindex the WSUS Database T-SQL script.

The steps to connect to SUSDB and perform the reindex differ, depending on whether SUSDB
is running in SQL Server or Windows Internal Database (WID). To determine where SUSDB is
running, check value of the SQLServerName registry entry on the WSUS server located at the
HKEY_LOCAL_MACHINE\Software\Microsoft\Update Services\Server\Setup subkey.

If the value contains just the server name or server\instance, SUSDB is running on a SQL Server.
If the value includes the string ##SSEE or ##WID in it, SUSDB is running in WID, as shown:

<!-- p.684 -->

If SUSDB was installed on WID

If SUSDB was installed on WID, SQL Server Management Studio Express must be installed
locally to run the reindex script. Here's an easy way to determine which version of SQL Server
Management Studio Express to install:

     For Windows Server 2012 or later versions:

          Go to C:\Windows\WID\Log and find the error log that contains the version number.

          Look up the version number in How to determine the version, edition and update level
          of SQL Server and its components    . This value tells you what Service Pack (SP) level
          that WID is running. Include the SP level when searching the Microsoft Download
          Center   for SQL Server Management Studio Express.

     For Windows Server 2008 R2 or previous versions:
          Go to C:\Windows\SYSMSI\SSEE\MSSQL.2005\MSSQL\LOG and open up the last error log
          with Notepad. At the top, there will be a version number (for example 9.00.4035.00
          x64). Look up the version number in How to determine the version, edition and update
          level of SQL Server and its components   . This version number tells you what Service
          Pack level it's running. Include the SP level when searching the Microsoft Download
          Center   for SQL Server Management Studio Express.

After installing SQL Server Management Studio Express, launch it, and enter the server name to
connect to:

     If the OS is Windows Server 2012 or later versions, use
     \\.\pipe\MICROSOFT##WID\tsql\query .

     If the OS is older than Windows Server 2012, enter
     \\.\pipe\MSSQL$MICROSOFT##SSEE\sql\query .

For WID, if errors similar to the following occur when attempting to connect to SUSDB using
SQL Server Management Studio (SSMS), try launching SSMS using the Run as administrator
option.

<!-- p.685 -->

If SUSDB was installed on SQL Server

If SUSDB was installed on full SQL Server, launch SQL Server Management Studio and enter the
name of the server (and instance if needed) when prompted.

   Tip

  Alternatively, a utility called sqlcmd can be used to run the reindex script. For more
  information, see Reindex the WSUS Database.

Running the script

To run the script in either SQL Server Management Studio or SQL Server Management Studio
Express, select New Query, paste the script in the window, and then select Execute. When it's
finished, a Query executed successfully message will be displayed in the status bar. And the
Results pane will contain messages related to what indexes were rebuilt.

<!-- p.686 -->

Decline superseded updates
Decline superseded updates in the WSUS server to help clients scan more efficiently. Before
declining updates, ensure that the superseding updates are deployed, and that superseded
ones are no longer needed. Configuration Manager includes a separate cleanup, which allows
it to expire superseded updates based on specified criteria. For more information, see the
following articles:

     Supersedence rules
     WSUS cleanup behavior starting in version 1810

The following SQL query can be run against the SUSDB database, to quickly determine the
number of superseded updates. If the number of superseded updates is higher than 1500, it
can cause various software update related issues on both the server and client sides.

  SQL

  -- Find the number of superseded updates
  Select COUNT(UpdateID) from vwMinimalUpdate where IsSuperseded=1 and Declined=0

If you are using Configuration Manager current branch version 1906 or a later version, we
recommend that you automatically decline the superseded updates by enabling the Decline
expired updates in WSUS according to supersedence rules option in the software update
point configuration for the top-most site.

<!-- p.687 -->

When you use this option, you can see how many updates were declined by reviewing the
WsyncMgr.log file after the synchronization process finishes. If you use this option, you don't
need to use the script described later in this section (either by manually running it or by setting
up as task to run it on a schedule).

If you are using standalone WSUS servers or an older version of configuration Manager, you
can manually decline superseded updates by using the WSUS console. Or you can run this
PowerShell script. Then, copy and save the script as a Decline-
SupersededUpdatesWithExclusionPeriod.ps1 script file.

  ７ Note

  This script is provided as is. It should be fully tested in a lab before you use it in
  production. Microsoft makes no guarantees regarding the use of this script in any way.
  Always run the script with the -SkipDecline parameter first, to get a summary of how
  many superseded updates will be declined.

If Configuration Manager is set to Immediately expire superseded updates (see below), the
PowerShell script can be used to decline all superseded updates. It should be done on all
autonomous WSUS servers in the Configuration Manager/WSUS hierarchy.

<!-- p.688 -->

You don't need to run the PowerShell script on WSUS servers that are set as replicas, such as
secondary site SUPs. To determine whether a WSUS server is a replica, check the Update
Source settings.

<!-- p.689 -->

If updates are not configured to be immediately expired in Configuration Manager, the
PowerShell script must be run with an exclusion period that matches the Configuration
Manager setting for number of days to expire superseded updates. In this case, it would be 60
days since SUP component properties are configured to wait two months before expiring
superseded updates:

<!-- p.690 -->

The following command lines illustrate the various ways that the PowerShell script can be run:

  ７ Note

  When you run the script on the WSUS server, use LOCALHOST instead of the actual
  SERVERNAME .

 PowerShell

 Decline-SupersededUpdatesWithExclusionPeriod.ps1 -UpdateServer SERVERNAME -Port
 8530 –SkipDecline

 Decline-SupersededUpdatesWithExclusionPeriod.ps1 -UpdateServer SERVERNAME -Port
 8530 –ExclusionPeriod 60

 Decline-SupersededUpdatesWithExclusionPeriod.ps1 -UpdateServer SERVERNAME -Port
 8530

 Decline-SupersededUpdatesWithExclusionPeriod.ps1 -UpdateServer SERVERNAME -UseSSL -
 Port 8531

<!-- p.691 -->

Running the script with a -SkipDecline and -ExclusionPeriod 60 to gather information about
updates on the WSUS server, and how many updates could be declined:

Running the script with -ExclusionPeriod 60, to decline superseded updates older than 60
days:

The output and progress indicators are displayed while the script is running. Note the
SupersededUpdates.csv file, which will contain a list of all updates that are declined by the
script:

<!-- p.692 -->

  ７ Note

  If issues occur when attempting to use the above PowerShell script to decline superseded
  updates, see the section Running the Decline-
  SupersededUpdatesWithExclusionPeriod.ps1 script times out when connecting to the
  WSUS server, or a 401 error occurs while running for troubleshooting steps.

After superseded updates have been declined, for best performance, SUSDB should be
reindexed again. For related information, see Reindex the WSUS database.

Run the WSUS Server Cleanup Wizard
WSUS Server Cleanup Wizard provides options to clean up the following items:

     Unused updates and update revisions (also known as Obsolete updates)
     Computers not contacting the server
     Unneeded update files
     Expired updates
     Superseded updates

In a Configuration Manager environment, Computers not contacting the server and
Unneeded update files options are not relevant because Configuration Manager manages
software update content and devices, unless either the Create all WSUS reporting events or
Create only WSUS status reporting events options are selected under Software Update Sync
Settings. If you have one of these options configured, you should consider automating the
WSUS Server Cleanup to perform cleanup of these two options.

If you are using Configuration Manager current branch version 1906 or a later version, enabling
the Decline expired updates in WSUS according to supersedence rules option handles
declining of Expired updates and Superseded updates based on the supersedence rules that
are specified in Configuration Manager. Enabling the Remove obsolete updates from the
WSUS database option in Configuration Manager current branch version 1906 handles the
cleanup of Unused updates and update revisions (Obsolete updates). It's recommended to
enable these options in the software update point configuration on the top-level site to allow
Configuration Manager to clean up the WSUS database.

<!-- p.693 -->

If you've never cleaned up obsolete updates from WSUS database before, this task may time
out. You can review WsyncMgr.log for more information, and manually run the SQL script that
is specified in HELP! My WSUS has been running for years without ever having maintenance
done and the cleanup wizard keeps timing out once, which would allow subsequent attempts
from Configuration Manager to run successfully. For more information about WSUS cleanup
and maintenance in Configuration Manager, see the docs.

For standalone WSUS servers, or if you are using an older version of Configuration Manager, it
is recommended that you run the WSUS Cleanup wizard periodically. If the WSUS Server
Cleanup Wizard has never been run and the WSUS has been in production for a while, the
cleanup may time out. In that case, reindex with step 2 and step 3 first, then run the cleanup
with only the Unused updates and update revisions option checked.

If you have never run WSUS Cleanup wizard, running the cleanup with Unused updates and
update revisions may require a few passes. If it times out, run it again until it completes, and
then run each of the other options one at a time. Lastly make a full pass with all options
checked. If timeouts continue to occur, see the SQL Server alternative in HELP! My WSUS has
been running for years without ever having maintenance done and the cleanup wizard keeps
timing out. It may take multiple hours or days for the Server Cleanup Wizard or SQL alternative
to run through completion.

The WSUS Server Cleanup Wizard runs from the WSUS console. It is located under Options, as
shown here:

<!-- p.694 -->

For more information, see Use the Server Cleanup Wizard.

After it reports the number of items it has removed, the cleanup finishes. If you do not see this
information returned on your WSUS server, it is safe to assume that the cleanup timed out. In
that case, you will need to start it again or use the SQL alternative.

<!-- p.695 -->

After superseded updates have been declined, for best performance, SUSDB should be
reindexed again. See the Reindex the WSUS database section for related information.

Troubleshooting
HELP! My WSUS has been running for years without ever
having maintenance done and the cleanup wizard keeps
timing out
There are two different options here:

   1. Reinstall WSUS with a fresh database. There are a number of caveats related to this,
     including length of initial sync, and full client scans against SUSDB, versus differential
     scans.

   2. Ensure you have a backup of the SUSDB database, then run a reindex. When that
     completes, run the following script in SQL Server Management Studio or SQL Server
     Management Studio Express. After it finishes, follow all of the above instructions for
     running maintenance. This last step is necessary because the spDeleteUpdate stored
     procedure only removes unused updates and update revisions.

  ７ Note

<!-- p.696 -->

  Before you run the script, follow the steps in The spDeleteUpdate stored procedure runs
  slowly to improve the performance of the execution of spDeleteUpdate .

 SQL

 DECLARE @var1 INT
 DECLARE @msg nvarchar(100)

 CREATE TABLE #results (Col1 INT)
 INSERT INTO #results(Col1) EXEC spGetObsoleteUpdatesToCleanup

 DECLARE WC Cursor
 FOR
 SELECT Col1 FROM #results

 OPEN WC
 FETCH NEXT FROM WC
 INTO @var1
 WHILE (@@FETCH_STATUS > -1)
 BEGIN SET @msg = 'Deleting' + CONVERT(varchar(10), @var1)
 RAISERROR(@msg,0,1) WITH NOWAIT EXEC spDeleteUpdate @localUpdateID=@var1
 FETCH NEXT FROM WC INTO @var1 END

 CLOSE WC
 DEALLOCATE WC

 DROP TABLE #results

Running the Decline-
SupersededUpdatesWithExclusionPeriod.ps1 script times out
when connecting to the WSUS server, or a 401 error occurs
while running
If errors occur when you attempt to use the PowerShell script to decline superseded updates,
an alternative SQL script can be run against SUDB.

   1. If Configuration Manager is used along with WSUS, check Software Update Point
     Component Properties > Supersedence Rules to see how quickly superseded updates
     expire, such as immediately or after X months. Make a note of this setting.

<!-- p.697 -->

2. If you haven't backed up the SUSDB database, do so before proceeding further.

3. Use SQL Server Management Studio to connect to SUSDB.

4. Run the following query. The number 90 in the line that includes DECLARE @thresholdDays
  INT = 90 should correspond with the Supersedence Rules from step 1 of this procedure,

  and the correct number of days that aligns with the number of months that is configured
  in Supersedence Rules. If this is set to expire immediately, the value in the SQL query for
  @thresholdDays should be set to zero.

    SQL

    -- Decline superseded updates in SUSDB; alternative to Decline-
    SupersededUpdatesWithExclusionPeriod.ps1
    DECLARE @thresholdDays INT = 90 -- Specify the number of days between today
    and the release date for which the superseded updates must not be declined
    (i.e., updates older than 90 days). This should match configuration of
    supersedence rules in SUP component properties, if ConfigMgr is being used
    with WSUS.
    DECLARE @testRun BIT = 0 -- Set this to 1 to test without declining anything.
    -- There shouldn't be any need to modify anything after this line.

<!-- p.698 -->

       DECLARE @uid UNIQUEIDENTIFIER
       DECLARE @title NVARCHAR(500)
       DECLARE @date DATETIME
       DECLARE @userName NVARCHAR(100) = SYSTEM_USER

       DECLARE @count INT = 0

       DECLARE DU CURSOR FOR
         SELECT MU.UpdateID, U.DefaultTitle, U.CreationDate FROM vwMinimalUpdate MU
         JOIN PUBLIC_VIEWS.vUpdate U ON MU.UpdateID = U.UpdateId
       WHERE MU.IsSuperseded = 1 AND MU.Declined = 0 AND MU.IsLatestRevision = 1
         AND MU.CreationDate < DATEADD(dd,-@thresholdDays,GETDATE())
       ORDER BY MU.CreationDate

       PRINT 'Declining superseded updates older than ' + CONVERT(NVARCHAR(5),
       @thresholdDays) + ' days.' + CHAR(10)

       OPEN DU
       FETCH NEXT FROM DU INTO @uid, @title, @date
       WHILE (@@FETCH_STATUS > - 1)
       BEGIN
         SET @count = @count + 1
         PRINT 'Declining update ' + CONVERT(NVARCHAR(50), @uid) + ' (Creation Date '
       + CONVERT(NVARCHAR(50), @date) + ') - ' + @title + ' ...'
         IF @testRun = 0
             EXEC spDeclineUpdate @updateID = @uid, @adminName = @userName,
       @failIfReplica = 1
         FETCH NEXT FROM DU INTO @uid, @title, @date
       END

       CLOSE DU
       DEALLOCATE DU

       PRINT CHAR(10) + 'Attempted to decline ' + CONVERT(NVARCHAR(10), @count) + '
       updates.'

  5. To check progress, monitor the Messages tab in the Results pane.

What if I find out I needed one of the updates that I declined?
If you decide you need one of these declined updates in Configuration Manager, you can get it
back in WSUS by right-clicking the update, and selecting Approve. Change the approval to Not
Approved, and then resync the SUP to bring the update back in.

<!-- p.699 -->

If the update is no longer in WSUS, it can be imported from the Microsoft Update Catalog, if it
hasn't been expired or removed from the catalog.

Automating WSUS maintenance

  ７ Note

  If you are using Configuration Manager version1906 or a later version, automate the
  cleanup procedures by enabling the WSUS Maintenance options in the software update
  point configuration of the top-level site. These options handle all cleanup operations that
  are performed by the WSUS Server Cleanup Wizard. However, you should still
  automatically back up and reindex the WSUS database on a schedule.

WSUS maintenance tasks can be automated, assuming that a few requirements are met first.

   1. If you have never run WSUS cleanup, you need to do the first two cleanups manually.
     Your second manual cleanup should be run 30 days from your first since it takes 30 days
     for some updates and update revisions to age out. There are specific reasons for why you
     don't want to automate until after your second cleanup. Your first cleanup will probably
     run longer than normal. So you can't judge how long this maintenance will normally take.
     The second cleanup is a much better indicator of what is normal for your machines. This is

<!-- p.700 -->

     important because you need to figure out about how long each step takes as a baseline (I
     also like to add about 30-minutes wiggle room) so that you can determine the timing for
     your schedule.

   2. If you have downstream WSUS servers, you will need to perform maintenance on them
     first, and then do the upstream servers.

   3. To schedule the reindex of the SUSDB, you will need a full version of SQL Server. Windows
     Internal Database (WID) doesn't have the capability of scheduling a maintenance task
     though SQL Server Management Studio Express. That said, in cases where WID is used
     you can use the Task Scheduler with SQLCMD mentioned earlier. If you go this route, it's
     important that you don't sync your WSUS servers/SUPs during this maintenance period! If
     you do, it's possible your downstream servers will just end up resyncing all of the updates
     you just attempted to clean out. I schedule this overnight before my AM sync, so I have
     time to check on it before my sync runs.

Needed/helpful links:

     Reindex the WSUS Database
     Agent XPs Server Configuration Option
     Weekend Scripter: Use the Windows Task Scheduler to Run a Windows PowerShell Script

WSUS cleanup script

  ７ Note

  When you run the script on the WSUS server, use LOCALHOST instead of the actual
  SERVERNAME . Additionally, replace PORT with the used one.

 PowerShell

 [reflection.assembly]::LoadWithPartialName("Microsoft.UpdateServices.Administration
 ")`
  | out-null
 $wsus =
 [Microsoft.UpdateServices.Administration.AdminProxy]::GetUpdateServer("SERVERNAME",
 $true,PORT);
 $cleanupScope = new-object Microsoft.UpdateServices.Administration.CleanupScope;
 $cleanupScope.DeclineSupersededUpdates = $true
 $cleanupScope.DeclineExpiredUpdates = $true
 $cleanupScope.CleanupObsoleteUpdates = $true
 $cleanupScope.CompressUpdates = $true
 #$cleanupScope.CleanupObsoleteComputers = $true

<!-- p.701 -->

 $cleanupScope.CleanupUnneededContentFiles = $true
 $cleanupManager = $wsus.GetCleanupManager();
 $cleanupManager.PerformCleanup($cleanupScope);

Setting up the WSUS Cleanup task in Task Scheduler

  ７ Note

  As mentioned previously, if you are using Configuration Manager current branch version
  1906 or a later version, automate the cleanup procedures by enabling the WSUS
  Maintenance options in the software update point configuration of the top-level site. For
  standalone WSUS servers or older versions of Configuration Manager, you can continue to
  use the following steps.

The Weekend Scripter     blog post mentioned in the previous section contains basic directions
and troubleshooting for this step. However, I'll walk you through the process in the following
steps.

   1. Open Task Scheduler and select Create a Task. On the General tab, set the name of the
     task, the user that you want to run the PowerShell script as (most people use a service
     account). Select Run whether a user is logged on or not, and then add a description if
     you wish.

   2. Under the Actions tab, add a new action and specify the program/script you want to run.
     In this case, we need to use PowerShell and point it to the PS1 file we want it to run. You
     can use the WSUS Cleanup script. This script performs cleanup options that Configuration
     Manager current branch version 1906 doesn't do. You can uncomment them if you are

<!-- p.702 -->

using standalone WSUS or an older version of Configuration Manager. If you would like a
log, you can modify the last line of the script as follows:

  ７ Note

  When you run the script on the WSUS server, use LOCALHOST instead of the actual
  SERVERNAME . Additionally, replace PORT with the used one.

 PowerShell

 [reflection.assembly]::LoadWithPartialName("Microsoft.UpdateServices.Administr
 ation") | out-null
 $wsus =
 [Microsoft.UpdateServices.Administration.AdminProxy]::GetUpdateServer("SERVERN
 AME",$true,PORT);
 $cleanupScope = new-object
 Microsoft.UpdateServices.Administration.CleanupScope;
 # $cleanupScope.DeclineSupersededUpdates = $true # Performed by CM1906
 # $cleanupScope.DeclineExpiredUpdates    = $true # Performed by CM1906
 # $cleanupScope.CleanupObsoleteUpdates   = $true # Performed by CM1906
 $cleanupScope.CompressUpdates          = $true
 $cleanupScope.CleanupObsoleteComputers = $true
 $cleanupScope.CleanupUnneededContentFiles = $true
 $cleanupManager = $wsus.GetCleanupManager();
 $cleanupManager.PerformCleanup($cleanupScope) | Out-File
 C:\WSUS\WsusClean.txt;

You'll get an FYI/warning in Task Scheduler when you save. You can ignore this warning.

<!-- p.703 -->

3. On the Triggers tab, set your schedule for once a month or on any schedule you want.
  Again, you must ensure that you don't sync your WSUS during the entire cleanup and
  reindex time.

4. Set any other conditions or settings you would like to tweak as well. When you save the
  task, you may be prompted for credentials of the Run As user.

<!-- p.704 -->

 5. You can also use these steps to configure the Decline-
   SupersededUpdatesWithExclusionPeriod.ps1 script to run every three months. I usually
   set this script to run before the other cleanup steps, but only after I have run it manually
   and ensured it completed successfully. I run at 12:00 AM on the first Sunday every three
   months.

Setting up the SUSDB reindex for WID using SQLCMD and
Task Scheduler
 1. Save the Reindex the WSUS database script as a .sql file (for example, SUSDBMaint.sql).

 2. Create a basic task and give it a name:

 3. Schedule this task to start about 30 minutes after you expect your cleanup to finish
   running. My cleanup is running at 1:00 AM every first Sunday. It takes about 30 minutes
   to run and I am going to give it another 30 minutes before starting my reindex. It means I
   would schedule this task for every first Sunday at 2:00 AM, as shown here:

<!-- p.705 -->

  4. Select the action to Start a program. In the Program/script box, type the following
    command. The file specified after the -i parameter is the path to the SQL script you
    saved in step 1. The file specified after the -o parameter is where you would like the log
    to be placed. Here's an example:

    "C:\Program Files\Microsoft SQL Server\110\Tools\Binn\SQLCMD.exe" -S

    \\.\pipe\Microsoft##WID\tsql\query -i C:\WSUS\SUSDBMaint.sql -o

    c:\WSUS\reindexout.txt

  5. You'll get a warning, similar to the one you got when creating the cleanup task. Select Yes
    to accept the arguments, and then select Finish to apply:

  6. You can test the script by forcing it to run and reviewing the log for errors. If you run into
    issues, the log will tell you why. Usually if it fails, the account running the task doesn't
    have appropriate permissions or the WID service isn't started.

Setting up a basic Scheduled Maintenance Task in SQL for non-WID
SUSDBs

 ７ Note

<!-- p.706 -->

You must be a sysadmin in SQL Server to create or manage maintenance plans.

1. Open SQL Server Management Studio and connect to your WSUS instance. Expand
  Management, right-click Maintenance Plans, and then select New Maintenance Plan.
  Give your plan a name.

2. Select subplan1 and then ensure your Toolbox is in context:

3. Drag and drop the task Execute T-SQL Statement Task:

4. Right-click it and select Edit. Copy and paste the WSUS reindex script, and then select OK:

<!-- p.707 -->

   5. Schedule this task to run about 30 minutes after you expect your cleanup to finish
     running. My cleanup is running at 1:00 AM every first Sunday. It takes about 30 minutes
     to run, and I am going to give it another 30 minutes before starting reindex. It means I
     would schedule this task to run every first Sunday at 2:00 AM.

   6. While creating the maintenance plan, consider adding a backup of the SUSDB into the
     plan as well. I usually back up first, then reindex. It may add more time to the schedule.

Putting it all together
When running it in a hierarchy, the WSUS cleanup run should be done from the bottom of the
hierarchy up. However, when using the script to decline superseded updates, the run should be
done from the top down. Declining superseded updates is really a type of addition to an
update rather than a removal. You're actually adding a type of approval in this case.

Since a sync can't be done during the actual cleanup, it's suggested to schedule/complete all
tasks overnight. Then check on their completion via the logging the following morning, before

<!-- p.708 -->

the next scheduled sync. If something failed, maintenance can be rescheduled for the next
night, once the underlying issue is identified and resolved.

These tasks may run faster or slower depending on the environment, and timing of the
schedule should reflect that. Hopefully they are faster since my lab environment tends to be a
bit slower than a normal production environment. I am a bit aggressive on the timing of the
decline scripts. If Tier2 overlaps Tier3 by a few minutes, it will not cause a problem because my
sync isn't scheduled to run.

Not syncing keeps the declines from accidentally flowing into my Tier3 replica WSUS servers
from Tier2. I did give myself extra time between the Tier3 decline and the Tier3 cleanup since I
definitely want to make sure the decline script finishes before running my cleanup.

It brings up a common question: Since I'm not syncing, why shouldn't I run all of the cleanups
and reindexes at the same time?

The answer is that you probably could, but I wouldn't. If my coworker across the globe needs
to run a sync, with this schedule I would minimize the risk of orphaned updates in WSUS. And I
can schedule it to rerun to completion the next night.

                                                                                    ﾉ   Expand table

 Time                Tier                                      Tasks

 12:00 AM            Tier1-Decline

 12:15 AM            Tier2-Decline

 12:30 AM            Tier3-Decline

 1:00 AM             Tier3 WSUS Cleanup

 2:00 AM             Tier3 Reindex                             Tier2 WSUS Cleanup

 3:00 AM             Tier1-Cleanup                             Tier2 Reindex

 4:00 AM             Tier1 Reindex

  ７ Note

  If you're using Configuration Manager current branch version 1906 or a later version to
  perform WSUS Maintenance, Configuration Manager performs the cleanup after
  synchronization using the top-down approach. In this scenario, you can schedule the
  WSUS database backup and reindexing jobs to run before the configured sync schedule

<!-- p.709 -->

  without worrying about any of the other steps, because Configuration Manager will
  handle everything else.

For more information about SUP maintenance in Configuration Manager, see the following
articles:

      Software updates maintenance
      Software updates maintenance in Configuration Manager

 Last updated on 03/30/2026

<!-- p.710 -->

Software updates in Configuration
Manager
Original product version: Configuration Manager (current branch), Microsoft System Center
2012 Configuration Manager, Microsoft System Center 2012 R2 Configuration Manager
Original KB number: 3092358

Software updates in Configuration Manager provide a set of tools and resources that can help
manage the complex task of tracking and applying software updates to client computers in the
enterprise. An effective software update management process is necessary to maintain
operational efficiency, overcome security issues, and maintain the stability of the network
infrastructure. Because of the changing nature of technology and the continual appearance of
new security threats, effective software update management requires consistent and continual
attention.

Summary
Software updates synchronization in Configuration Manager uses Microsoft Update to retrieve
software updates metadata. The top-level site synchronizes with Microsoft Update on a
predetermined schedule or when you manually start synchronization from the Configuration
Manager console. When Configuration Manager finishes software updates synchronization at
the top-level site, software updates synchronization starts at child sites if they exist. When
synchronization is complete at each primary site or secondary site, a site-wide policy is created
that provides client computers with the location of the software update points.

After the client receives the policy, the client starts a scan for software updates compliance and
writes the information to Windows Management Instrumentation (WMI). The compliance
information is then sent to the management point. From there, the information is sent to the
site server. For each software update, a state message is created that contains the compliance
state for the update. The state messages are sent in bulk to the management point and then to
the site server. There, the compliance state is inserted into the site database. The compliance
state for software updates is displayed in the Configuration Manager console. For more
information about compliance assessment, see Software updates compliance assessment.

When you deploy software updates or when an automatic deployment rule runs and deploys
software updates, a deployment assignment policy is added to the machine policy for the site.

<!-- p.711 -->

The software updates are downloaded from the download location, the Internet, or network
shared folder, to the package source. The software updates are copied from the package
source to the content library on the site server, and then copied to the content library on the
distribution point. For more information about software update deployment, see Software
update deployment process.

References
For more information about understanding, maintaining, and troubleshooting the software
update process, see the following resources:

      Track software update synchronization
      Track software update compliance assessment
      Track the software update deployment process
      Troubleshoot software update synchronization
      Troubleshoot software update scan failures
      Troubleshoot software update deployments

 Last updated on 03/30/2026

<!-- p.712 -->

Software updates maintenance in
Configuration Manager
This article describes the maintenance processes for software updates. It also provides
suggestions for how Configuration Manager administrators can maintain optimal performance
of the WSUS database.

For more information about software updates in Configuration Manager, see Software updates
introduction.

Original product version: Microsoft System Center 2012 Configuration Manager, Microsoft
System Center 2012 R2 Configuration Manager
Original KB number: 3090526

Expired updates
As part of the ongoing update revision process, some updates in the Microsoft Update Catalog
are expired. This issue typically occurs when a newer version of the update is available.
However, in rare cases, Microsoft may discover a problem with an update and therefore expire
it. During software updates synchronization, these expired updates are marked as Expired in
the Configuration Manager console. This expired status is indicated by a dimmed icon next to
the update. These expired updates are automatically cleaned up from the Configuration
Manager database on a regular schedule. The WSUS Synchronization Manager component
removes expired updates only if the following conditions are true:

     The update is not referenced in an update assignment.
     The update is older than the value of Updates Cleanup Age. (By default, this value is
     seven days.)

WSUS Synchronization Manager at the top-level Configuration Manager site checks every hour
for updates that must be removed, and it removes expired updates if they match the criteria in
the previous list. When WSUS Synchronization Manager deletes expired updates, you can see
the following entries in the WSyncMgr.log file:

  Deleting old expired updates... SMS_WSUS_SYNC_MANAGER
  Deleted 100 expired updates SMS_WSUS_SYNC_MANAGER

<!-- p.713 -->

  ...
  Deleted 2995 expired updates total SMS_WSUS_SYNC_MANAGER

Content cleanup
As expired updates are removed, content for those expired updates may become orphaned.
WSUS Synchronization Manager also cleans up this orphaned content. As part of the content
cleanup, WSUS Synchronization Manager analyzes the packages that are owned by the current
site, finds content that is no longer referenced, and removes that content from the package
source directory. By default, content is removed only if it has been orphaned for more than one
day.

If any content is removed, the cleanup process also updates the package so that the updated
content is sent to the distribution points (DPs). When WSUS Synchronization Manager removes
orphaned content, you can see the following entries in the WSyncMgr.log file:

  Deleting orphaned content for package CS100006 (EPDefinitions) from source
  <PackageSource> SMS_WSUS_SYNC_MANAGER
  Deleting orphaned content folder \\<PackageSource>\51b6db15-6938-4b37-9fa8-
  caf513e13930... SMS_WSUS_SYNC_MANAGER
  ...
  ...
  Deleting orphaned content folder \\<PackageSource>\526b6a85-a62c-4d54-bc0d-
  b3409223b0df... SMS_WSUS_SYNC_MANAGER
  Deleted 12 orphaned content folders in package CS100006 (EPDefinitions)
  SMS_WSUS_SYNC_MANAGER
  Refreshing package CS100006 (EPDefinitions) SMS_WSUS_SYNC_MANAGER

For more information about the cleanup of expired updates and content, see Software Update
Content Cleanup in System Center 2012 Configuration Manager        .

WSUS server maintenance
To maintain optimal performance of the WSUS database, we recommend that you routinely run
the WSUS Cleanup Wizard tasks on the WSUS database (SUSDB) and also reindex the WSUS
database on each WSUS computer that is hosting a Software Update Point role in the
Configuration Manager environment. When you run WSUS Cleanup Wizard actions in a
multilevel hierarchy, run the cleanup process on the lowest tier of the WSUS chain first and

<!-- p.714 -->

then move up to the next tier to run the Cleanup Wizard tasks. You must continue on up the
hierarchy until you reach the top-tier WSUS computer. You can run this WSUS maintenance
routine at the same time on multiple servers in the same tier.

Although reindexing can be done in any order on any WSUS computer's SUSDB, we
recommend that you run the cleanup and reindexing on each WSUS computer by running the
reindex process first and then run the Cleanup Wizard tasks. If you tune the performance of the
SUSDB first through reindexing, the Cleanup Wizard tasks will finish more quickly.

For more information about WSUS maintenance, see Perform WSUS maintenance.

For more information about WSUS cleanup behavior and log entries in Configuration Manager
(current branch), see Software updates maintenance.

 Last updated on 03/30/2026

<!-- p.715 -->

Software update point installation and
configuration
Applies to: Configuration Manager

The software update point is required on the central administration site and on the primary
sites to enable software updates compliance assessment and to deploy software updates to
clients.

Track software update point installation
When software update point site system role is installed, an instance of the SMS_SCI_SysResUse
class is created, and entries that resemble the following are logged in SMSProv.log:

  PutInstanceAsync SMS_SCI_SysResUse SMS Provider
  CExtProviderClassObject::DoPutInstanceInstance SMS Provider
  INFO: 'PR1SITE.CONTOSO.COM' is a valid FQDN. SMS Provider

Site Component Manager then detects the change in site control information and initiates the
installation of the software update point site system role. Entries that resemble the following
are logged in SiteComp.log:

  Parsed the master site control file, serial number 3559422579.
  SMS_SITE_COMPONENT_MANAGER
  Synchronizing server table and polling servers as needed...
  SMS_SITE_COMPONENT_MANAGER
  Synchronizing component server PR1SITE.CONTOSO.COM...
  SMS_SITE_COMPONENT_MANAGER
  Installing component SMS_WSUS_CONTROL_MANAGER...
  SMS_SITE_COMPONENT_MANAGER
  NFO: 'PR1SITE.CONTOSO.COM' is a valid FQDN. SMS_SITE_COMPONENT_MANAGER
  Creating registry keys Operations Management\SMS Server Role\SMS Software Update
  Point on server PR1SITE.CONTOSO.COM. SMS_SITE_COMPONENT_MANAGER
  Updated WSUS Configuration for PR1SITE.CONTOSO.COM.
  SMS_SITE_COMPONENT_MANAGER
  The component is being installed on the site server, no files need to be installed in the

<!-- p.716 -->

  "E:\ConfigMgr" directory because the files are already there.
  SMS_SITE_COMPONENT_MANAGER
  All files installed. SMS_SITE_COMPONENT_MANAGER
  Starting bootstrap operations... SMS_SITE_COMPONENT_MANAGER
  Installed service SMS_SERVER_BOOTSTRAP_PR1SITE. SMS_SITE_COMPONENT_MANAGER
  Starting service SMS_SERVER_BOOTSTRAP_PR1SITE with command-line arguments "PR1
  E:\ConfigMgr /install E:\ConfigMgr\bin\x64\rolesetup.exe SMSWSUS "...
  SMS_SITE_COMPONENT_MANAGER

When the role installation is started by Site Component Manager, SUPSetup.log is created and
the following are logged:

  <02/09/14 22:53:28>
  ==========================================================
  ==========
  <02/09/14 22:53:28> SMSWSUS Setup Started....
  <02/09/14 22:53:28> Parameters: E:\ConfigMgr\bin\x64\rolesetup.exe /install
  /siteserver:PR1SITE SMSWSUS 0
  <02/09/14 22:53:28> Installing Pre Reqs for SMSWSUS
  <02/09/14 22:53:28> ======== Installing Pre Reqs for Role SMSWSUS ========
  <02/09/14 22:53:28> Found 1 Pre Reqs for Role SMSWSUS
  <02/09/14 22:53:28> Pre Req SqlNativeClient found.
  <02/09/14 22:53:28> SqlNativeClient already installed (Product Code: {D411E9C9-CE62-
  4DBF-9D92-4CB22B750ED5}). Would not install again.
  <02/09/14 22:53:28> Pre Req SqlNativeClient is already installed. Skipping it.
  <02/09/14 22:53:28> ======== Completed Installation of Pre Reqs for Role SMSWSUS
  ========
  <02/09/14 22:53:28> Installing the SMSWSUS
  <02/09/14 22:53:28> Checking for supported version of WSUS (min WSUS 3.0 SP2 +
  KB2720211 + KB2734608)
  <02/09/14 22:53:28> Checking runtime v2.0.50727...
  <02/09/14 22:53:28> Did not find supported version of assembly
  Microsoft.UpdateServices.Administration.
  <02/09/14 22:53:28> Checking runtime v4.0.30319...
  <02/09/14 22:53:28> Found supported assembly Microsoft.UpdateServices.Administration
  version 4.0.0.0, file version 6.2.9200.16384
  <02/09/14 22:53:28> Found supported assembly Microsoft.UpdateServices.BaseApi version

<!-- p.717 -->

  4.0.0.0, file version 6.2.9200.16384
  <02/09/14 22:53:28> Supported WSUS version found
  <02/09/14 22:53:28> Supported WSUS Server version (6.2.9200.16384) is installed.
  <02/09/14 22:53:28> CTool::RegisterManagedBinary: run command line:
  "C:\Windows\Microsoft.NET\Framework64\v2.0.50727\RegAsm.exe"
  "E:\ConfigMgr\bin\x64\wsusmsp.dll"
  <02/09/14 22:53:44> CTool::RegisterManagedBinary: Registered
  E:\ConfigMgr\bin\x64\wsusmsp.dll successfully
  <02/09/14 22:53:44> Registered DLL E:\ConfigMgr\bin\x64\wsusmsp.dll
  <02/09/14 22:53:44> Installation was successful.
  <02/09/14 22:53:44> ~RoleSetup().

After the role is installed, Site Component Manager removes the bootstrap service that's
created to perform the installation, the following are logged in SiteComp.log:

  "E:\ConfigMgr\bin\x64\rolesetup.exe /install /siteserver:PR1SITE.CONTOSO.COM" executed
  successfully on server PR1SITE.CONTOSO.COM. SMS_SITE_COMPONENT_MANAGER
  Bootstrap operation successful. SMS_SITE_COMPONENT_MANAGER
  Deinstalled service SMS_SERVER_BOOTSTRAP_PR1SITE.
  SMS_SITE_COMPONENT_MANAGER
  Bootstrap operations completed. SMS_SITE_COMPONENT_MANAGER

Configure proxy setting for the software update point
When there is a proxy server between the WSUS server and the upstream update source, the
proxy settings must be configured for the site system as well as the software update point role.
The proxy server settings are site system specific, which means that all site system roles use the
proxy server settings that you specify. For more information, see Accounts used in
Configuration Manager.

Check proxy configuration on a computer
     To review the proxy configuration for the logged-on user, run the following command:

       Console

       netsh winhttp show proxy

<!-- p.718 -->

     To review the proxy configuration for the SYSTEM account, open a command prompt by
     running the following command:

       Console

       psexec -s -i cmd

     In the Command Prompt window, run whoami to confirm that the command window is
     running under the System account.

     Run the netsh winhttp show proxy command and review the proxy configuration for the
     System account.

     You can also start Internet Explorer from this command window, and review the proxy
     configured in Internet Explorer. In some cases you may have to clear the Automatically
     Detect Settings check box, and set the correct proxy.

To force WinHTTP to use proxy configuration from Internet Explorer, run the following
command:

 Console

 netsh winhttp import proxy source =ie

For more information about Netsh commands, see Netsh Commands for Windows Hypertext
Transfer Protocol (WINHTTP).

Configure the proxy settings for the Site System
   1. In the Configuration Manager console, go to Administration > Site Configuration >
     Servers and Site System Roles, select the <SiteSystemName> on the right pane.
   2. In the bottom pane, right-click Site System, and then click Properties.
   3. Select the Proxy tab, specify the proxy server name, port, and credentials (if required).

Configure the proxy settings for the software update point
   1. In the Configuration Manager console, go to Administration > Site Configuration >
     Servers and Site System Roles, select <SiteSystemName> on the right pane.
   2. In the bottom pane, right-click Software Update Point, and then click Properties.
   3. Select the Proxy and Account Settings tab, and select Use a proxy server when
     synchronizing software updates.

<!-- p.719 -->

   4. (Optional) To configure automatic deployment rules (ADRs) to use a proxy server, select
     the Proxy And Account Settings tab, and then select Use a proxy server when
     downloading content by using automatic deployment rules.

Verify proxy settings in the WSUS console
   1. Open the WSUS console.
   2. Select Options in the tree pane, and then select Update Source and Proxy Server in the
     display pane.
   3. Select the Proxy Server tab. Verify that the proxy settings match the settings configured
     for the software update point in Configuration Manager. If the settings don't match,
     check WCM.log on the site server.

For more information, see Proxy server settings.

Configure the WSUS Server Connection Account for
the software update point
If the software update point is remote from the site server, and if the site server computer
account doesn't have permissions to connect to the WSUS server, you must specify a WSUS
Server Connection Account that Configuration Manager can use to connect to the WSUS
server.

This account is used by WCM and WSyncMgr. It must be a local administrator on the computer
where WSUS is installed. Additionally, the account must be part of the local WSUS
Administrators group. For more information, see Accounts used in Configuration Manager.

To configure the WSUS Server Connection Account for the software update point:

   1. In the Configuration Manager console, go to Administration > Site Configuration >
     Servers and Site System Roles, select <SiteSystemName> on the right pane.
   2. In the bottom pane, right-click Software Update Point, and then click Properties.
   3. On the Proxy And Account Settings tab, specify the connection account under WSUS
     Server Connection Account.

References
     Install and configure a software update point
     Synchronize software updates
     Configure classifications and products to synchronize

<!-- p.720 -->

Last updated on 03/30/2026
