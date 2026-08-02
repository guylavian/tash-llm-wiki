---
title: "Core infrastructure documentation — pages 1801-1840"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1801-1840
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1801-1840
family: sccm
documentKind: "doc"
abstract: "View high-level information about the replication of site data and global data between the two sites on a link. Select View reports for historical traffic data to view a report that shows details about the network bandwidth used by replication across the link. Parent Site For th"
---

# Core infrastructure documentation — pages 1801-1840

<!-- p.1801 -->

View high-level information about the replication of site data and global data between
the two sites on a link.

Select View reports for historical traffic data to view a report that shows details about
the network bandwidth used by replication across the link.

Parent Site
For the parent site on a replication link, view details about the database, which include:

     Firewall ports for the SQL Server

     Free disk space

     Database file locations

     Certificates

Child Site
For the child site on a replication link, view details about the database, which include:

     Firewall ports for the SQL Server

     Free disk space

     Database file locations

     Certificates

Initialization Detail
View the initialization status for groups that replicate across the link. This information
can help you identify when initialization of replication data is in progress or has failed.

Use this information to identify when a site might be in interoperability mode.
Interoperability mode is when the child site doesn't run the same version of
Configuration Manager as the parent site.

Replication Detail
View the replication status for each group that replicates across the link. Use this
information to help identify problems or delays for the replication of specific data. It can

<!-- p.1802 -->

help determine the appropriate database replication thresholds for this link. For more
information, see Database replication thresholds.

   Tip

  Replication groups for site data are sent only from the child site to the parent site.
  Replication groups for global data replicate in both directions.

Replication Link Analyzer
Configuration Manager includes the Replication Link Analyzer (RLA), which you use to
analyze and repair replication issues. Use RLA to remediate link failures when replication
fails. It's also useful when replication stops working but the site hasn't yet reported it as
failed.

Use RLA to remediate replication issues between the following computers in the
hierarchy:

      Between a site server and the site database server

      Between a site's database server and another site's database server, otherwise
      known as intersite replication

  ７ Note

  The direction of the replication failure doesn't matter.

Run RLA in either the Configuration Manager console or at a command prompt:

      To run in the Configuration Manager console: Go to the Monitoring workspace,
      and select the Database Replication node. Select the replication link that you want
      to analyze, and then in ribbon, select Replication Link Analyzer.

      To run at a command prompt, type the following command:
      %ProgramFiles(x86)%\Microsoft Endpoint
      Manager\AdminConsole\bin\Microsoft.ConfigurationManager.ReplicationLinkAnalyze

      r.Wizard.exe <source site server FQDN> <destination site server FQDN>

          ） Important

<!-- p.1803 -->

        Starting in version 1910, this path changed to use the Microsoft Endpoint
        Manager folder. Make sure you don't use an older version of the file that might

        exist in another folder.

When you run RLA, it detects problems by using a series of diagnostic rules and checks.
You view the problems that the tool identifies. When it has instructions to resolve an
issue, it displays them. If RLA can automatically remediate a problem, it presents you
with that option.

When RLA finishes, it saves the results in the following XML-based report and a log file
on the desktop of the user who runs the tool:

     ReplicationAnalysis.xml

     ReplicationLinkAnalysis.log

RLA stops the following services while it remediates some problems. It restarts these
services when remediation is complete:

     SMS_SITE_COMPONENT_MANAGER

     SMS_EXECUTIVE

If RLA fails to complete remediation, restart these services on the site server if necessary.

RLA logs all investigation and remediation actions to provide additional details that it
doesn't display in the wizard.

RLA prerequisites
The account that you use to run RLA must have the following permissions:

     Local administrator rights on each computer that's involved in the replication link.

     Sysadmin rights on each SQL Server database that's involved in the replication link.

  ７ Note

  The account doesn't require a specific Configuration Manager role-based
  administration security role. An administrative user with access to the Database
  Replication node can run the tool in the Configuration Manager console. A system
  administrator with sufficient rights to each computer can run the tool at a
  command prompt.

<!-- p.1804 -->

RLA known issue
RLA generates SQL Server Service Broker (SSB) certificate errors for primary sites that
upgraded from System Center 2012 Configuration Manager. This issue is because of
changes in the names of the certificates in Configuration Manager current branch. You
can safely ignore these errors.

Monitoring database replication

Monitor high-level site-to-site database replication status
   1. In the Configuration Manager console, go to the Monitoring workspace.

   2. Select the Site Hierarchy node to open the Hierarchy Diagram view.

   3. Hover the mouse pointer on the line between the two sites. View the status of
     global and site data replication for these sites.

Monitor the status of a replication link
   1. In the Configuration Manager console, go to the Monitoring workspace.

   2. Select the Database Replication node, and then select the replication link that you
     want to monitor. Then select the appropriate tab to view different details about the
     replication status for that link.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1805 -->

Troubleshoot Configuration Manager
Database Replication Service overview
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

To better understand and help troubleshoot issues with Database Replication Service, use these
diagrams.

     Database replication
     DRS configuration
     DRS performance
     DRS reinitialization (reinit)
     Global data reinit
     Site data reinit
     Reinit missing message

These troubleshooting diagrams are interconnected. Use the following diagram to understand
their relationships:

<!-- p.1806 -->

For more information, see the following series of blogs from Microsoft Support:

     ConfigMgr DRS Synchronization Internals
     ConfigMgr 2012 Data Replication Service (DRS) Unleashed
     ConfigMgr 2012 DRS – Troubleshooting FAQs
     ConfigMgr 2012 DRS Initialization Internals
     ConfigMgr 2012: DRS and SQL Server service broker certificate issues

Last updated on 03/27/2026

<!-- p.1807 -->

Troubleshoot Database Replication
Service links
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS replication when a link fails:

                                                       Troubleshoot SQL replication
                                           Replication link failure
                                 Start

  SELECT * FROM
                                 CAS /      Check if the replication group
  RCM_ReplicationLinkStatus
                                Primary     link is in degraded or failed state
  WHERE Status IN (8, 9)

                                             No
                                            Result

                                 Has
                                Result
                                                                                   DECLARE @cutoffTime DATETIME
                                                                                   SELECT @cutoffTime =
                                                                                   DATEADD(minute, -30,
                                                                                   GETUTCDATE())
                                                                                                                               Check if replication group
                                                                                   SELECT * FROM                               link is recently calculated
                                                                                   RCM_ReplicationLinkStatus
                                                                                   WHERE UpdateTime >@cutoffTime

  SELECT * FROM ServerData                                                                                    No
                                          Check SQL maintenance mode
  WHERE Status = 120                                                                                         Result

                                                                                                                       Has
                                                                                                                      Result

                        Has                  No
                       Result               Result

           Continue to                        Continue to                      Continue to
                                                                                                                       End
       SQL replication reinit               SQL performance                  SQL configuration

Queries
This diagram uses the following queries:

Check if the replication group link is in degraded or failed state

<!-- p.1808 -->

 SQL

 SELECT * FROM RCM_ReplicationLinkStatus
 WHERE Status IN (8, 9)

Check if replication group link is recently calculated

 SQL

 DECLARE @cutoffTime DATETIME
 SELECT @cutoffTime = DATEADD(minute, -30, GETUTCDATE())
 SELECT * FROM RCM_ReplicationLinkStatus
 WHERE UpdateTime >@cutoffTime

Check SQL Server maintenance mode

 SQL

 SELECT * FROM ServerData
 WHERE SiteStatus = 120

Next steps
     DRS reinitialization (reinit)
     DRS performance
     DRS configuration

Last updated on 03/27/2026

<!-- p.1809 -->

SQL Server instance configuration
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS configuration related to SQL Server
Service Broker:

                               Troubleshoot SQL configuration
                                                      Troubleshoot SQL configuration
                                           Start
                                                      related to SQL service broker (SSB)

   SELECT
   transmission_status, *
   FROM                                    CAS /
                                                     Check if SQL can deliver SSB messages
   sys.transmission_queue                 Primary
   ORDER BY enqueue_time
   DESC

                                                     No
                                                                                                             End
                                                    Result
                                            Has
                                           Result

                                                    Check transmission_status
                                                    You may need to refresh the
                                                    previous query as it could be blank

                                Has                 Transmission_status
                               Result                    is empty

                            Remediate the issues
                                                                                            Run SQL profiler to
                End         reported from                                      End
                                                                                            trace SSB events
                            transmission_status

Queries
This diagram has the following queries and actions:

Check if SQL Server can deliver SSB messages

<!-- p.1810 -->

  SQL

  SELECT transmission_status, *
  FROM sys.transmission_queue
  ORDER BY enqueue_time DESC

Remediation actions
Remediate the issues reported from transmission_status
Common issues:

      Firewall configuration
      Network configuration
      SSB certificate misconfigured

Run SQL Server profiler to trace SSB events
Run SQL Server profiler on the CAS and primary site database to trace events related to the SQL
Server Service Broker:

      Audit Broker Login
      Audit Broker Conversation
      Events in Broker category

 Last updated on 03/27/2026

<!-- p.1811 -->

Database Replication Service performance
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS performance that can impact replication
status:

<!-- p.1812 -->

                                                           

Queries
This diagram uses the following queries:

Make sure SQL Server change tracking table is cleaned up

<!-- p.1813 -->

 SQL

 DECLARE @RetentionUnit INT = 0;
 DECLARE @RetentionPeriod INT = 0;
 DECLARE @CTCutOffTime DATETIME;
 DECLARE @CTMinTime DATETIME;

 SELECT @RetentionPeriod=retention_period,
     @RetentionUnit=retention_period_units
 FROM sys.change_tracking_databases
 WHERE database_id = DB_ID();

 IF @RetentionUnit = 1
     SET @CTCutOffTime = DATEADD(MINUTE,-@RetentionPeriod,GETUTCDATE())
 ELSE IF @RetentionUnit = 2
     SET @CTCutOffTime = DATEADD(HOUR,-@RetentionPeriod,GETUTCDATE())
 ELSE IF @RetentionUnit = 3
     SET @CTCutOffTime = DATEADD(DAY,-@RetentionPeriod,GETUTCDATE())

 -- give a buffer of two days
 SET @CTCutOffTime = DATEADD(DAY, -2, @CTCutOffTime)
 select top 1 @CTMinTime=commit_time from sys.dm_tran_commit_table order by commit_ts
 asc
 IF @CTMinTime < @CTCutOffTime
     PRINT 'there is change tracking backlog, please contact Microsoft support'

Change current sessions that handle SQL Server service broker
messages are blocked

 SQL

 select
        req.session_id
        ,req.blocking_session_id
        ,req.last_wait_type
        ,req.wait_type
        ,req.wait_resource
        ,t.text
 from sys.dm_exec_sessions s
 inner join sys.dm_exec_requests req on s.Session_id=req.session_id
 cross apply sys.dm_exec_sql_text(sql_handle) t
 where program_name='SMS_data_replication_service'

Check sessions asking too much memory

 SQL

 SELECT * FROM sys.dm_exec_query_memory_grants
 ORDER BY requested_memory_kb DESC

<!-- p.1814 -->

Check sessions taking too many locks

 SQL

 SELECT TOP 10 request_session_id,
 program_name = (SELECT program_name FROM sys.dm_exec_sessions WHERE
 session_id=request_session_id),
 COUNT (*) num_locks
 FROM sys.dm_tran_locks
 GROUP BY request_session_id
 ORDER BY count (*) DESC

See also
SQL Server configuration

Last updated on 03/27/2026

<!-- p.1815 -->

Database Replication Service reinitialization
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS reinitialization (reinit):

<!-- p.1816 -->

                                          Troubleshoot SQL replication reinit
                                                               Start           SQL replication reinitialization (reinit)

                  SELECT * FROM ServerData                    CAS /
                                                                               Check if site is in maintenance mode
                  WHERE SiteStatus = 120                     Primary

                                                                             No
                                                                                                                           End
                                                                            Result
                                                               Has
                                                              Result

                   SELECT * FROM
                   RCM_DrsInitializationTracking                              Check which replication group
                   WHERE InitializationStatus NOT IN                          hasn't completed reinit
                   (6,7)

                                                                                No
                                                                               Result

                                                               Has
                                                              Result

                  SELECT * FROM
                  RCM_DrsInitializationTracking dt
                  INNER JOIN ReplicationData rg
                  ON dt.ReplicationGroup =
                  rg.ReplicationGroup                                         Check global data
                  WHERE dt.InitializationStatus NOT IN
                  (6,7)
                  AND rg.ReplicationPattern=N'GLOBAL'

                                                Has                                No
                                               Result                             Result

                                                   SELECT * FROM
                                                   RCM_DrsInitializationTracking dt
                                                   INNER JOIN ReplicationData rg
                                                   ON dt.ReplicationGroup =
                                                   rg.ReplicationGroup
                                                                                                       Check site data
                                                   WHERE dt.InitializationStatus NOT IN
                                                   (6,7)
                                                   AND rg.ReplicationPattern=N'Site'

        Continue to                                Continue to                     Has                 No                          Continue to
     Global data reinit                           Site data reinit                Result              Result                     SQL configuration

Queries
This diagram uses the following queries:

Check if site is in maintenance mode

<!-- p.1817 -->

 SQL

 SELECT * FROM ServerData
 WHERE Status = 120

Check that reinit isn't completed for which replication group

 SQL

 SELECT * FROM RCM_DrsInitializationTracking
 WHERE InitializationStatus NOT IN (6,7)

Check global data

 SQL

 SELECT * FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N'GLOBAL'

Check site data

 SQL

 SELECT * FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N'Site'

Next steps
     Global data reinit
     Site data reinit
     SQL Server configuration

Last updated on 03/27/2026

<!-- p.1818 -->

Troubleshoot global data reinitialization
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS reinitialization (reinit) for global data in a
Configuration Manager hierarchy:

<!-- p.1819 -->

                                                                   Troubleshoot global data reinit
                                                                        Start            Troubleshoot SQL replication
                                                                                         reinit for global data

 SELECT * FROM                                                                  SELECT * FROM
 RCM_DrsInitializationTracking dt                                               RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg                                                  INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup =
                                            Check if site replication           ON dt.ReplicationGroup =
 rg.ReplicationGroup                 CAS                                        rg.ReplicationGroup                          Primary
 WHERE dt.InitializationStatus NOT          hasn't finished reinit              WHERE dt.InitializationStatus NOT
 IN (6,7)                                                                       IN (6,7)
 AND                                                                            AND
 rg.ReplicationPattern=N'Global'                                                rg.ReplicationPattern=N'Global'

                                                                                      No
                                                                                                                                          End
                                                                                     Result
                                                                         Has
                                                                        Result

                                                                                  SELECT RequestTrackingGUID,
                                                                                  InitializationStatus
                                                                                  FROM RCM_DrsInitializationTracking dt
                                                                                  INNER JOIN ReplicationData rg                        Get the TrackingGuid &
                                                                                  ON dt.ReplicationGroup =
                                                                                  rg.ReplicationGroup                                  Status from the primary site
                                                                                  WHERE dt.InitializationStatus NOT IN
                                                                                  (6,7)
                                                                                  AND rg.ReplicationPattern=N'Global'

                                                                                  SELECT RequestTrackingGUID,
                                                                                  InitializationStatus
                                                                                  FROM RCM_DrsInitializationTracking dt
                                                                                                                                       Get the TrackingGuid &
                                                                                  WHERE                                                Status from the CAS
                                                                                  RequestTrackingGUID=@trackingGuid

                                                                                                                                        No                                Continue to
                                                                                                                                       Result                       Reinit missing message

                                                                                                                               Has
                                                                                                                              Result

                                                                                                                                       Check InitializationStatus

                                                                                                           == 3 or                                                          Continue to
                                                                                                                                            == 99
                                                                                                            == 4                                                            Reinit failed

                                                                                                                               == 5
   SELECT Status FROM
   RCM_InitPackageRequest WHERE
                                           Check request status for
   RequestTrackingGUID=@trackGuid          the tracking ID
                                                                                                                                                                Rcmctrl.log (primary site)

                                                                                                          RCM on primary site is BCP in the data                BcpIn for group <group name>
                                                                                                                                                                …
                                                                                                                                                                Failed to BCP in for table <table name>

                                                                                                                                                                Rcmctrl.log (CAS)
                                                                                                              RCM is preparing the data, check
                                                                           == 1                                                                                 Creating init package for replication
                                                                                                            rcmctrl.log on CAS for BCP progress                 group <replication group> for site
                                                                                                                                                                <CAS>

                                                                                                                                                                Rcmctrl.log (CAS)

                                                                                                                  RCM has finished BCP the data,                Created minijob to send compressed
                                                                          == 2
                                                                                                                   create/compress the package                  copy of DRS INIT BCP Package to site
                                                                                                                                                                <CAS>. Transfer root = <CAB file to
                                                                                                                                                                transfer>

                                                                                                                                                                Sender.log (CAS)
                                                                         == 3                                File replication Job created. Check
                                                                                                             sender.log on primary for progress                 Sending completed [CAB file to transfer]

                                                                                                                                                                Despoolr.log (primary site)

                                                                                                                                                                Verified Package signature
                                                                                                                                                                …
                                                                                                             File replication Job done. Check                   Executing instruction of type
                                                                                                           despoolr.log on Primary for progress                 MICROSOFT|SMS|MINIJOBINSTRUCTION
                                                                                                                                                                |DRSINIT
                                                                                                                                                                ...
                                                                                                                                                                Decompressing snapshot package
                                                                                                                                                                <compressed file> to [rcm inbox]

Queries
This diagram uses the following queries:

<!-- p.1820 -->

Check if reinit isn't finished for global replication

 SQL

 SELECT * FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N`Global'

Get the TrackingGuid & Status from the primary site

 SQL

 SELECT RequestTrackingGUID, InitializationStatus
 FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N`Global'

Get the TrackingGuid & Status from the CAS

 SQL

 SELECT RequestTrackingGUID, InitializationStatus
 FROM RCM_DrsInitializationTracking dt
 WHERE RequestTrackingGUID=@trackingGuid

Check request status for the tracking ID

 SQL

 SELECT Status FROM RCM_InitPackageRequest
 WHERE RequestTrackingGUID=@trackGuid

Next steps
     Reinit missing message

Last updated on 03/27/2026

<!-- p.1821 -->

Troubleshoot site data reinit
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting DRS reinitialization (reinit) for site data in a
Configuration Manager hierarchy:

<!-- p.1822 -->

                                                   Troubleshoot site data reinit
                                                                                  Start

SELECT * FROM                                                                              SELECT * FROM
RCM_DrsInitializationTracking dt                                                           RCM_DrsInitializationTracking dt
INNER JOIN ReplicationData rg                                                              INNER JOIN ReplicationData rg
ON dt.ReplicationGroup =                        Check if site replication                  ON dt.ReplicationGroup =
rg.ReplicationGroup                 CAS                                                    rg.ReplicationGroup                 Primary
                                                hasn't finished reinit
WHERE dt.InitializationStatus NOT                                                          WHERE dt.InitializationStatus NOT
IN (6,7)                                                                                   IN (6,7)
AND rg.ReplicationPattern=N'Site'                                                          AND rg.ReplicationPattern=N'Site'

                                                                                               No
                                                                                                                                            End
                                                                                              Result

                                                                                   Has
                                                                                  Result

                                          SELECT RequestTrackingGUID,
                                          InitializationStatus
                                          FROM RCM_DrsInitializationTracking dt
                                          INNER JOIN ReplicationData rg
                                          ON dt.ReplicationGroup =
                                                                                               Get the TrackingGuid &
                                          rg.ReplicationGroup                                  Status from CAS
                                          WHERE dt.InitializationStatus NOT IN
                                          (6,7)
                                          AND rg.ReplicationPattern=N'Site'

                                          SELECT RequestTrackingGUID,
                                          InitializationStatus
                                          FROM RCM_DrsInitializationTracking dt
                                                                                             Get the TrackingGuid &
                                          WHERE                                              Status from the primary site
                                          RequestTrackingGUID=@trackingGuid

                                                                                              No                                     Continue to
                                                                                             Result                            Reinit missing message

                                                                                   Has
                                                                                  Result

                                                                                              Check InitializationStatus

                                                                                                                                    Continue to
                                                                == 5                             == 99
                                                                        == 4                                                        Reinit failed

                                                                                  == 3

                                          SELECT * FROM ServerData
                                          WHERE SiteStatus = 125                              Check primary site isn't
                                          AND SiteCode=dbo.fnGetSiteCode()                    in maintenance mode
                                          AND ServerRole=N'Peer'

                                                                                                 No                                  Continue to
                                                                                                Result                            Global data reinit

                                                                                   Has
                                                                                  Result

                                          SELECT Status FROM                                Check request status
                                          RCM_InitPackageRequest WHERE
                                          RequestTrackingGUID=@trackGuid                    for the tracking ID

<!-- p.1823 -->

                                                  == 3
                                                  == 2
                                                            == 1

                                                                                     Rcmctrl.log (primary site)
                                              RCM is preparing the data, check
                                           rcmctrl.log on primary for BCP progress   Creating init package for replication
                                                                                     group <replication group> for site <CAS>

                                                                                     Rcmctrl.log (primary site)
                                               RCM has finished BCP the data,
                                                                                     Created minijob to send compressed copy
                                                create/compress the package          of DRS INIT BCP Package to site <CAS>.
                                                                                     Tranfer root = <CAB file to transfer>

                                                                                     Sender.log (primary site)
                                              File replication job created, check
                                             sender.log on primary for progress      Sending completed [CAB file to transfer]

                                                                                     Despoolr.log (CAS)

                                                                                     Verified Package signature
                                                                                     …
                                               File replication job done, check      Executing instruction of type
                                              despoolr.log on CAS for progress       MICROSOFT|SMS|MINIJOBINSTRUCTION|
                                                                                     DRSINIT
                                                                                     ...
                                                                                     Decompressing snapshot package
                                                                                     <compressed file> to [rcm inbox]

                                                                                     Rcmctrl.log (CAS)

                                               RCM on CAS is BCP in the data         BcpIn for group <group name>
                                                                                     …
                                                                                     Failed to BCP in for table <table name>

Queries
This diagram uses the following queries:

Check if reinit isn't finished for site replication

 SQL

 SELECT * FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N`Site'

Get the TrackingGuid & Status from the CAS

 SQL

 SELECT RequestTrackingGUID, InitializationStatus
 FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup

<!-- p.1824 -->

 WHERE dt.InitializationStatus NOT IN (6,7)
 AND rg.ReplicationPattern=N'Site'

Get the TrackingGuid & Status from the primary site

 SQL

 SELECT RequestTrackingGUID, InitializationStatus
 FROM RCM_DrsInitializationTracking dt
 WHERE RequestTrackingGUID=@trackingGuid

Check primary site isn't in maintenance mode

 SQL

 SELECT * FROM ServerData
 WHERE SiteStatus = 125
 AND SiteCode=dbo.fnGetSiteCode()
 AND ServerRole=N'Peer'

Check request status for the tracking ID

 SQL

 SELECT Status FROM RCM_InitPackageRequest
 WHERE RequestTrackingGUID=@trackGuid

Next steps
     Reinit missing message
     Global data reinit

Last updated on 03/27/2026

<!-- p.1825 -->

Reinitialize a missing message
In a multi-site hierarchy, Configuration Manager uses Database Replication Service (DRS) to
transfer data between sites. For more information, see Database replication.

Use the following diagram to start troubleshooting a missing message with DRS reinitialization
(reinit):

                                       Troubleshoot reinit missing message
                                                                                       Start

   SELECT * FROM                                                                                SELECT * FROM
   RCM_DrsInitializationTracking dt                                                             RCM_DrsInitializationTracking dt
   INNER JOIN ReplicationData rg                                                                INNER JOIN ReplicationData rg
   ON dt.ReplicationGroup =            Subscriber    Check if site replication                  ON dt.ReplicationGroup =            Publishing
   rg.ReplicationGroup                    site       hasn't finished reinit                     rg.ReplicationGroup                    site
   WHERE dt.InitializationStatus NOT                                                            WHERE dt.InitializationStatus NOT
   IN (6,7)                                                                                     IN (6,7)

                                                                                                            No
                                                                                                           Result

                                                                                        Has
                                                                                       Result                                         End

                                               SELECT RequestTrackingGUID,
                                               InitializationStatus
                                               FROM RCM_DrsInitializationTracking dt
                                               INNER JOIN ReplicationData rg                         Get the TrackingGuid &
                                               ON dt.ReplicationGroup =                              Status from subscriber site
                                               rg.ReplicationGroup
                                               WHERE dt.InitializationStatus NOT IN
                                               (6,7)

                                               SELECT RequestTrackingGUID,
                                               InitializationStatus
                                               FROM RCM_DrsInitializationTracking dt
                                                                                                      Get the TrackingGuid & Status
                                               WHERE                                                  from the publishing site
                                               RequestTrackingGUID=@trackingGuid

                                                                               Has                      No
                                                                              Result                   Result

                                                    Go to SQL replication reinit                     Take remediation actions

Queries
This diagram uses the following queries:

<!-- p.1826 -->

Check if reinit isn't finished for site replication

 SQL

 SELECT * FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)

Get the TrackingGuid & Status from subscriber site

 SQL

 SELECT RequestTrackingGUID, InitializationStatus
 FROM RCM_DrsInitializationTracking dt
 INNER JOIN ReplicationData rg
 ON dt.ReplicationGroup = rg.ReplicationGroup
 WHERE dt.InitializationStatus NOT IN (6,7)

Get the TrackingGuid & Status from the publishing site

 SQL

 SELECT RequestTrackingGUID, InitializationStatus
 FROM RCM_DrsInitializationTracking dt
 WHERE RequestTrackingGUID=@trackingGuid

Remediation actions
Version 1902 and later
To detect the issue and reinit, run the Replication Link Analyzer.

Version 1810 and earlier
Run the following SQL query to get the ReplicationGroupID :

 SQL

 SELECT rd.ID AS ReplicationGroupID from ReplicationData rd
 INNER JOIN RCM_DrsInitializationTracking it ON rd.ReplicationGroup =
 it.ReplicationGroup
 WHERE it.RequestTrackingGUID=@trackingGuid

<!-- p.1827 -->

Then use the InitializeData method on the SMS_ReplicationGroup WMI class with the following
values:

      ReplicationGroupID: from the preceding SQL query
      SiteCode1: parent site
      SiteCode2: child site

For more information, see InitializeData method in class SMS_ReplicationGroup.

Example

  PowerShell

  Invoke-WmiMethod -Namespace "root\sms\site_CAS" -Class SMS_ReplicationGroup –Name
  InitializeData -ArgumentList "20", "CAS", "PR1"

Next steps
      DRS reinitialization (reinit)

 Last updated on 03/27/2026

<!-- p.1828 -->

Introduction to queries in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can create and run queries to locate objects in a Configuration Manager hierarchy
that match your query criteria. These objects include items like specific types of
computers or user groups. Queries can return most types of Configuration Manager
objects, which include sites, collections, applications, and inventory data.

Query creation overview
When you create a query, you must specify a minimum of two parameters: where you
want to search and what you want to search for. For example, to find the amount of
hard drive space that's available on all computers in a Configuration Manager site, you
can create a query to search the Logical Disk attribute class and the Free Space (MB)
attribute for available hard drive space.

After you create an initial query, you can specify additional query criteria. For example,
you can specify that the query results include only computers that are assigned to a
specified site. You can also change how results are displayed so you can view the results
in an order that's meaningful to you. For example, you can specify that the results are
sorted by the amount of free hard drive space, in either ascending or descending order.

When you create a query, it's stored by Configuration Manager and displayed in the
Queries node in the Monitoring workspace. From this location, you can create new
queries and run, update, and manage existing queries.

You can also import a query into a query rule in a Configuration Manager collection. For
more information, see How to create collections.

Next steps
How to create queries

Feedback

<!-- p.1829 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1830 -->

How to manage queries in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article can help you manage queries in Configuration Manager.

For information about how to create queries, see How to create queries.

Manage queries
In the Monitoring workspace, select Queries, select the query to manage, and then
select a management task.

The following table provides information about the management tasks.

                                                                                       ﾉ   Expand table

 Management            Details
 task

 Run                   Runs the selected query and displays the results in the Configuration Manager
                       console.

 Install Client        Opens the Install Client Wizard, which lets you install the Configuration
                       Manager client on computers returned by the selected query.

                       This option isn't available for queries that return mobile devices, users, or user
                       groups.

                       For more information about how to install Configuration Manager clients by
                       using client push, see Deploy clients to Windows computers.

 Export                Opens the Export Objects Wizard. This wizard lets you export the query to a
                       Managed Object Format (MOF) file that you can then import at another site.

 Move                  Opens the Move Selected Items dialog box. This dialog box lets you move the
                       selected query to a folder that you previously created under the Queries node.

Next steps
Create queries

<!-- p.1831 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1832 -->

Create queries in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article describes how to create and import queries in Configuration Manager.

Create a query
Use this procedure to create a query in Configuration Manager.

   1. In the Configuration Manager console, select Monitoring.

   2. In the Monitoring workspace, select Queries. On the Home tab, in the Create
      group, select Create Query.

   3. On the General tab of the Create Query Wizard, specify a unique name and,
      optionally, a comment for the query.

   4. If you want to import an existing query to use as a basis for the new query, select
      Import Query Statement. In the Browse Query dialog box, select a query that you
      want to import, and then select OK.

   5. In the Object Type list, select the type of object that you want the query to return.
      This table describes some examples of the types of objects you can search for:

                                                                                 ﾉ   Expand table

       Object type     Description

       System          Use to search for typical system attributes, like the NetBIOS name of a
       Resource        device, the client version, the client IP address, and Active Directory
                       Domain Services information.

       User            Use to search for typical user information, like user names, user group
       Resource        names, and security group names.

       Deployment      Use to search for typical attributes of a deployment, like the deployment
                       name, the schedule, and the collection that it was deployed to.

   6. Select Edit Query Statement to open the <Query Name> Statement Properties
      dialog box.

<!-- p.1833 -->

7. On the General tab of the <Query Name> Statement Properties dialog box,
  specify the attributes that the query returns and how they should be displayed.
  Select the New icon to add a new attribute. You can also select Show Query
  Language to enter or edit the query directly in WMI Query Language (WQL). For
  examples of WMI queries, see the Example WQL queries section in this article.

          You can use the following reference documentation to help you construct
          your own WQL queries:
            WQL (SQL for WMI)
            WHERE Clause
            WQL Operators
          Starting in Configuration Manager 2010, you can preview the results when
          you're creating or editing a query for collection membership. In the Query
          Statement Properties, select the green triangle to show the Query Results
          Preview window. Select Stop if you want to stop a long running query.

8. On the Criteria tab of the <Query Name> Statement Properties dialog box,
  specify criteria that are used to refine the results of the query. For example, you
  could return only resources that have a site code of XYZ. You can configure
  multiple criteria for a query.

    ） Important

    If you create a query that contains no criteria, the query will return all devices
    in the All Systems collection.

9. On the Joins tab of the <Query Name> Statement Properties dialog box, you can
  combine data from two different attributes into your query results. Although
  Configuration Manager automatically creates query joins when you choose
  different attributes for your query result, the Joins tab provides more advanced
  options. Configuration Manager supports these attribute classes:

                                                                                 ﾉ   Expand table

   Join         Description
   type

   Inner        Displays only matching results. Always used by joins that are created
                automatically.

   Left         Displays all results for the base attribute and only the matching results for the
                join attribute.

<!-- p.1834 -->

      Join         Description
      type

      Right        Displays all results for the join attribute and only the matching results for the
                   base attribute.

      Full         Displays all results for both the base attribute and the join attribute.

     For more information about how to use join operations, see the SQL Server
     documentation.

 10. Select OK to close the <Query Name> Statement Properties dialog box.

 11. On the General tab of the Create Query Wizard, specify that the results of the
     query aren't limited to the members of a collection, that they are limited to the
     members of a specified collection, or that a prompt for a collection appears each
     time the query is run.

 12. Complete the wizard to create the query. The new query appears in the Queries
     node in the Monitoring workspace.

Import a query
Use this procedure to import a query into Configuration Manager. For information
about how to export queries, see How to manage queries.

   1. In the Configuration Manager console, select Monitoring.

   2. In the Monitoring workspace, select Queries. On the Home tab, in the Create
     group, select Import Objects.

   3. On the MOF File Name page of the Import Objects Wizard, select Browse to
     select the Managed Object Format (MOF) file that contains the query that you
     want to import.

   4. Review the information about the query to be imported and then complete the
     wizard. The new query appears on the Queries node in the Monitoring workspace.

Example WQL queries
This section contains example WQL queries that you can use in your hierarchy or modify
for other purposes. To use these queries, select Show Query Language in the Query
Statement Properties dialog box. Then copy and paste the query into the Query
Statement field.

<!-- p.1835 -->

   Tip

  Use the wildcard character % to signify any string of characters. For example,
  %Visio% returns Microsoft Office Visio 2010.

Computers that run Windows 10
Use the following query to return the NetBIOS name and operating system version of all
computers that run Windows 10.

  WQL

  select SMS_R_System.NetbiosName,
  SMS_R_System.OperatingSystemNameandVersion from
  SMS_R_System where
  SMS_R_System.OperatingSystemNameandVersion like "%Workstation 10%"

Computers with a specific software package installed
Use the following query to return the NetBIOS name and software package name of all
computers that have a specific software package installed. This example returns all
computers with a version of Microsoft Visio installed. Replace Microsoft%Visio% with the
software package that you want to query for.

   Tip

  This query searches for the software package by using the names that are displayed
  in the programs list in Windows Control Panel.

  WQL

  select SMS_R_System.NetbiosName,
  SMS_G_System_ADD_REMOVE_PROGRAMS.DisplayName from
  SMS_R_System inner join SMS_G_System_ADD_REMOVE_PROGRAMS on
  SMS_G_System_ADD_REMOVE_PROGRAMS.ResourceId =
  SMS_R_System.ResourceId where
  SMS_G_System_ADD_REMOVE_PROGRAMS.DisplayName like "Microsoft%Visio%"

Computers in a specific Active Directory Domain Services
organizational unit

<!-- p.1836 -->

Use the following query to return the NetBIOS name and organizational unit (OU) name
of all computers in a specified OU. Replace the text OU Name with the name of the OU
that you want to query for.

  WQL

  select SMS_R_System.NetbiosName,
  SMS_R_System.SystemOUName from
  SMS_R_System where
  SMS_R_System.SystemOUName = "OU Name"

Computers with a specific NetBIOS name
Use the following query to return the NetBIOS name of all computers that begin with a
specific string of characters. In this example, the query returns all computers with a
NetBIOS name that begins with ABC .

  WQL

  select SMS_R_System.NetbiosName from
  SMS_R_System where SMS_R_System.NetbiosName like "ABC%"

Devices of a specific type
Device types are stored in the Configuration Manager database under the resource class
sms_r_system and the attribute name AgentEdition. Use this query to retrieve only the
devices that match the agent edition of the device type that you specify:

  WQL

  Select SMS_R_System.ClientEdition from SMS_R_System where
  SMS_R_System.ClientEdition = <Device ID>

Use one of these values for <Device ID>:

                                                                          ﾉ   Expand table

 Device type                                                   Value of AgentEdition

 Windows desktop or laptop computer                            0

 Windows ARM-based device (running Windows RT)                 1

<!-- p.1837 -->

 Device type                                                   Value of AgentEdition

 Windows Mobile 6.5                                            2

 Nokia Symbian                                                 3

 Windows Phone                                                 4

 Mac computer                                                  5

 Windows Embedded                                              7

 Intel system on a chip                                        12

 Microsoft HoloLens (MDM)                                      15

 Microsoft Surface Hub (MDM)                                   16

  ７ Note

  Values that aren't listed in this table are associated with devices that are no longer
  supported.

For example, if you want to return only Mac computers, use this query:

  WQL

  Select SMS_R_System.ClientEdition from SMS_R_System where
  SMS_R_System.ClientEdition = 5

Devices that are co-managed
  WQL

  select SMS_R_SYSTEM.ResourceID, SMS_R_SYSTEM.ResourceType,
  SMS_R_SYSTEM.Name,
  SMS_R_SYSTEM.SMSUniqueIdentifier, SMS_R_SYSTEM.ResourceDomainORWorkgroup,
  SMS_R_SYSTEM.Client
  from SMS_R_System
  inner join SMS_Client_ComanagementState on
  SMS_Client_ComanagementState.ResourceId = SMS_R_System.ResourceId
  where SMS_Client_ComanagementState.ComgmtPolicyPresent = 1 AND
  SMS_Client_ComanagementState.MDMEnrolled = 1 AND MDMProvisioned = 1

Next steps

<!-- p.1838 -->

How to manage queries

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1839 -->

Security and privacy for queries in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Queries in Configuration Manager let you retrieve information from the site database
according to criteria that you specify. Configuration Manager collects site database
information during standard operation. For example, by using information that's been
collected during discovery or inventory, you can configure a query to identify devices
that meet specified criteria.

For more information about queries, see Introduction to queries. For security best
practices and privacy information about Configuration Manager operations that collect
the data you can retrieve by using queries, see Security and privacy for Configuration
Manager.

Security best practices for queries
Use this security best practice for queries.

                                                                               ﾉ   Expand table

 Security best practice              More information

 When you export or import a         Restrict who can access the network folder.
 query that's saved to a network
 location, secure the location and   Use Server Message Block (SMB) signing or Internet
 the network channel.                Protocol security (IPsec) between the network location and
                                     the site server to prevent an attacker from tampering with
                                     the query data before it's imported.

Next steps
Security and privacy for Configuration Manager

Feedback

<!-- p.1840 -->

Was this page helpful?      Yes    No

Provide product feedback
