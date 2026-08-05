---
title: "Welcome — pages 721-760"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0721-0760
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0721-0760
family: sccm
documentKind: "doc"
abstract: "WSUS Configuration Manager configures the WSUS server Original product version: Configuration Manager Windows Server Update Services (WSUS) Configuration Manager connects to the WSUS server once every hour and configures the WSUS server with the settings that are defined for the"
---

# Welcome — pages 721-760

<!-- p.721 -->

WSUS Configuration Manager configures
the WSUS server
Original product version: Configuration Manager

Windows Server Update Services (WSUS) Configuration Manager connects to the WSUS server
once every hour and configures the WSUS server with the settings that are defined for the
software update point in the Configuration Manager console.

How it works
WSUS Configuration Manager uses the WSUS APIs to connect to the WSUS server. The WSUS
Administration console must be installed on the Configuration Manager site server, because
the WSUS Administration console installs the APIs that are used to connect to the WSUS server.

The following are logged in WCM.log:

  Checking for supported version of WSUS (min WSUS 3.0 SP2 + KB2720211 + KB2734608)
  SMS_WSUS_CONFIGURATION_MANAGER
  Checking runtime v2.0.50727... SMS_WSUS_CONFIGURATION_MANAGER
  Did not find supported version of assembly Microsoft.UpdateServices.Administration.
  SMS_WSUS_CONFIGURATION_MANAGER
  Checking runtime v4.0.30319... SMS_WSUS_CONFIGURATION_MANAGER
  Found supported assembly Microsoft.UpdateServices.Administration version 4.0.0.0, file
  version 6.2.9200.16384 SMS_WSUS_CONFIGURATION_MANAGER
  Found supported assembly Microsoft.UpdateServices.BaseApi version 4.0.0.0, file version
  6.2.9200.16384 SMS_WSUS_CONFIGURATION_MANAGER
  Supported WSUS version found SMS_WSUS_CONFIGURATION_MANAGER

If the products or classifications defined for the software update point are modified, SMS
Provider makes changes in the appropriate CI_* tables in the database. For example, when a
product is selected for synchronization, SMS Provider updates rows in the
CI_CategoryInstances and CI_UpdateCategorySubscription tables.

SMS Database Monitor monitors these tables for changes. When an update is detected, SMS
Database Monitor drops a CSB file in the WSUSMgr.box folder notifying WCM to update the
WSUS server configuration. The following are logged in SMSDBMon.log:

<!-- p.722 -->

  RCV: UPDATE on CI_CategoryInstances for CategoryNotify_iud [177][14252]
  SMS_DATABASE_NOTIFICATION_MONITOR
  RCV: UPDATE on CI_UpdateCategorySubscription for SubNotify_iu_WCM [177][14253]
  SMS_DATABASE_NOTIFICATION_MONITOR
  SND: Dropped E:\ConfigMgr\inboxes\objmgr.box\177.CTN [14252]
  SMS_DATABASE_NOTIFICATION_MONITOR
  SND: Dropped E:\ConfigMgr\inboxes\WSUSMgr.box\177.CSB [14253]
  SMS_DATABASE_NOTIFICATION_MONITOR

WCM then wakes up and connects to the WSUS server to make sure that it is configured with
the options defined in the Configuration Manager console. The following are logged in
WCM.log:

  File notification triggered WCM Inbox. SMS_WSUS_CONFIGURATION_MANAGER
  Setting new configuration state to 4 (WSUS_CONFIG_SUBSCRIPTION_PENDING)
  SMS_WSUS_CONFIGURATION_MANAGER
  Attempting connection to WSUS server: CE1SITE.CONTOSO.COM, port: 8530, useSSL: False
  SMS_WSUS_CONFIGURATION_MANAGER
  Successfully connected to server: CE1SITE.CONTOSO.COM, port: 8530, useSSL: False
  SMS_WSUS_CONFIGURATION_MANAGER
  Subscribed Update Categories <?xml version="1.0" ?>~~<Categories>~~ <Category
  Id="Product:a105a108-7c9b-4518-bbbe- 73f0fe30012b"><![CDATA[Windows Server
  2012]]></Category>~~ <Category Id="Product:fdfe8200-9d98-44ba-a12a-
  772282bf60ef"><![CDATA[Windows Server 2008 R2]]></Category>~~ <Category
  Id="UpdateClassification:0fa1201d-4330- 4fa8-8ae9-b877473b6441"><![CDATA[Security
  Updates]]></Category>~~ <Category Id="UpdateClassification:28bc880e-0592- 4cbf-
  8f95-c79b17911d5f"><![CDATA[Update Rollups]]></Category>~~ <Category
  Id="UpdateClassification:cd5ffd1e-e932- 4e3a-bf74-18bf0b1bbd83"><![CDATA[Updates]]>
  </Category>~~ <Category Id="UpdateClassification:e6cf1350-c01b-414d- a61f-
  263d14d133b4"><![CDATA[Critical Updates]]></Category>~~</Categories>
  SMS_WSUS_CONFIGURATION_MANAGER
  Configuration successful. Will wait for 1 minute for any subscription or proxy changes
  SMS_WSUS_CONFIGURATION_MANAGER
  Setting new configuration state to 2 (WSUS_CONFIG_SUCCESS)
  SMS_WSUS_CONFIGURATION_MANAGER

<!-- p.723 -->

Using WSUS APIs to connect to the WSUS server works by connecting to the ApiRemoting30
virtual directory on the WSUS website. Therefore, it's important that you specify the correct
port configuration when you install the software update point role.

 Last updated on 03/30/2026

<!-- p.724 -->

Track software update synchronization
Applies to: Configuration Manager

Software updates synchronization in Configuration Manager connects to Microsoft Update to
retrieve software updates metadata.

The top-level site (central administration site or stand-alone primary site) synchronizes with
Microsoft Update on a schedule or when you manually start synchronization from the
Configuration Manager console. When Configuration Manager finishes software updates
synchronization at the top-level site, software updates synchronization starts at child sites, if
they exist. When synchronization is complete at each primary site or secondary site, a site-wide
policy is created that provides to client computers the location of the software update points.

Synchronization on central administration site or
standalone primary site
The software updates synchronization process at the top-level site contacts Microsoft Update
and retrieves software update metadata that meets the criteria specified in the Software
Update Point Component properties. This criteria is specified only at the top-level site. At the
top-level site you can specify a synchronization source other than Microsoft Update, such as an
existing Windows Server Update Services (WSUS) computer that's not in the Configuration
Manager hierarchy.

The synchronization process at the top-level site performs the following steps:

Step 1: Software updates synchronization starts either
manually or on a schedule
When synchronization is initiated on a schedule, WSUS Synchronization Manager (WSyncMgr)
wakes up on the configured schedule and initiates synchronization. The following are logged in
WSyncMgr.log:

  Wakeup for scheduled regular sync SMS_WSUS_SYNC_MANAGER
  Starting Sync SMS_WSUS_SYNC_MANAGER
  Performing sync on regular schedule SMS_WSUS_SYNC_MANAGER

<!-- p.725 -->

When synchronization is initiated manually from the console, WSyncMgr is notified to initiate a
sync by executing the SyncNow method in the SMS_SoftwareUpdate WMI class. This method
updates the Update_SyncStatus table in the site database and sets the value of SyncNow to
SELF. This triggers SMS Database Notification Monitor (SMSDBMON) to place a SELF.SYN file in
WSyncMgr.box, and this awakens WSyncMgr and initiates synchronization.

The following is logged in SMSProv.log:

  ExecMethodAsync : SMS_SoftwareUpdate::SyncNow SMS Provider

In SQL Server Profiler trace:

  update Update_SyncStatus set SyncNow = 'SELF' where SiteCode = dbo.fnGetSiteCode()
  update Update_SyncStatus set SyncNow = null where SiteCode = dbo.fnGetSiteCode()

In SMSDBMON.log:

  RCV: UPDATE on Update_SyncStatus for SyncNotif_WSyncMgr [SELF][47788]
  SMS_DATABASE_NOTIFICATION_MONITOR
  SND: Dropped E:\ConfigMgr\inboxes\WSyncMgr.box\SELF.SYN [47788]
  SMS_DATABASE_NOTIFICATION_MONITOR

In WSyncMgr.log:

  Wakeup by inbox drop SMS_WSUS_SYNC_MANAGER
  Found local sync request file SMS_WSUS_SYNC_MANAGER
  Starting Sync SMS_WSUS_SYNC_MANAGER
  Performing sync on local request SMS_WSUS_SYNC_MANAGER

WSyncMgr then reads the list of software update points (SUPs) from the site control file (SCF).
WSyncMgr first synchronizes the SUP that was installed as the first SUP in the site and then
synchronizes the remaining SUPs. All additional SUPs are configured as replicas of the first SUP.
The following are logged in WsyncMgr.log:

  Read SUPs from SCF for CS1SITE.CONTOSO.COM SMS_WSUS_SYNC_MANAGER
  Found 1 SUPs SMS_WSUS_SYNC_MANAGER
  Found active SUP CS1SITE.CONTOSO.COM from SCF File. SMS_WSUS_SYNC_MANAGER

<!-- p.726 -->

When synchronization starts (either on schedule or manually), WSyncMgr creates status
message ID 6701 to indicate that the WSUS synchronization has started. The following are
logged in WsyncMgr.log:

  STATMSG: ID=6701 SEV=I LEV=M SOURCE="SMS Server"
  COMP="SMS_WSUS_SYNC_MANAGER" SYS=<SERVERFQDN> SITE=CS1 PID=432
  TID=3404 GMTDATE=Thu Jan 16 18:53:52.608 2014 ISTR0="" ISTR1="" ISTR2="" ISTR3=""
  ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=0
  SMS_WSUS_SYNC_MANAGER

   Tip

  To manually initiate a delta site wide synchronization, you can create a zero KB file named
  SELF.SYN in the Program Files\Microsoft Configuration Manager\Inboxes\WSyncMgr.box
  directory on the central administration site or standalone primary site server. Similarly, to
  initiate a full site wide synchronization, you can create a zero KB file named FULL.SYN in
  the same location.

Step 2: WSUS Synchronization Manager sends a request to
WSUS running on the software update point to start
synchronization with Microsoft Update
The first phase of the synchronization process is to synchronize the WSUS server with Microsoft
Update. WSyncMgr instructs the WSUS computer to start a synchronization with Microsoft
Update and creates status message ID 6704 (WSUS Synchronization in progress. Current phase:
Synchronizing WSUS Server). The following are logged in WsyncMgr.log:

  STATMSG: ID=6704 SEV=I LEV=M SOURCE="SMS Server"
  COMP="SMS_WSUS_SYNC_MANAGER" SYS=<SERVERFQDN> SITE=CS1 PID=432
  TID=3404 GMTDATE=Thu Jan 16 18:53:53.698 2014 ISTR0="" ISTR1="" ISTR2="" ISTR3=""
  ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=0
  SMS_WSUS_SYNC_MANAGER
  Synchronizing WSUS server cs1site.contoso.com ... SMS_WSUS_SYNC_MANAGER
  sync: Starting WSUS synchronization SMS_WSUS_SYNC_MANAGER

In SoftwareDistribution.log:

<!-- p.727 -->

  2014-01-16 18:53:54.231 UTC Change w3wp.58
  AdminDataAccess.StartSubscriptionManually Synchronization manually started
  2014-01-16 18:53:56.168 UTC Info WsusService.15 EventLogEventReporter.ReportEvent
  EventId=382,Type=Information,Category=Synchronization,Message=A manual
  synchronization was started.

Step 3: WSUS synchronizes software update metadata from
Microsoft Update. Any changes are inserted or updated in the
WSUS database
WSUS starts synchronizing with Microsoft Update, and WSyncMgr begins monitoring
synchronization progress. The following are logged in WsyncMgr.log:

  sync: WSUS synchronizing categories SMS_WSUS_SYNC_MANAGER
  sync: WSUS synchronizing updates SMS_WSUS_SYNC_MANAGER
  sync: WSUS synchronizing updates, processed 122 out of 130 items (93%), ETA in 00:00:03
  SMS_WSUS_SYNC_MANAGER
  sync: WSUS synchronizing updates, processed 130 out of 130 items (100%)
  SMS_WSUS_SYNC_MANAGER
  sync: WSUS synchronizing updates, processed 130 out of 130 items (100%)
  SMS_WSUS_SYNC_MANAGER

The following entries in the log files indicate that WSUS has finished synchronizing with
Microsoft Update:

     In SoftwareDistribution.log:

       2014-01-16 18:55:05.166 UTC Info WsusService.15
       EventLogEventReporter.ReportEvent
       EventId=384,Type=Information,Category=Synchronization,Message=Synchronization
       completed successfully.
       2014-01-16 18:55:06.307 UTC Info WsusService.31
       CatalogSyncAgent.SetSubscriptionStateWithRetry Firing event SyncFinish...

     In WSyncMgr.log:

       Done synchronizing WSUS Server <SERVERFQDN> SMS_WSUS_SYNC_MANAGER
       Sleeping 2 more minutes for WSUS server sync results to become available

<!-- p.728 -->

       SMS_WSUS_SYNC_MANAGER
       Set content version of update source {C2D17964-BBDD-4339-B9F3-12D7205B39CC}
       for site CS1 to 33 SMS_WSUS_SYNC_MANAGER

Step 4: WSUS Synchronization Manager synchronizes the
software updates metadata
After WSUS has finished synchronization, WSUS Synchronization Manager synchronizes the
software updates metadata. This is done from the WSUS database to the Configuration
Manager database, and any changes after the last synchronization are inserted or updated in
the site database. The software updates metadata is stored in the site database as a
configuration item.

The second phase of the synchronization process is to synchronize the software update
metadata from the WSUS database to the Configuration Manager database. At this point,
WSyncMgr creates status message ID 6705 (WSUS Synchronization in progress. Current phase:
Synchronizing site database).

The following are logged in WsyncMgr.log:

  STATMSG: ID=6705 SEV=I LEV=M SOURCE="SMS Server"
  COMP="SMS_WSUS_SYNC_MANAGER" SYS=<SERVERFQDN> SITE=CS1 PID=432
  TID=3404 GMTDATE=Thu Jan 16 18:57:09.156 2014 ISTR0="" ISTR1="" ISTR2="" ISTR3=""
  ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=0
  SMS_WSUS_SYNC_MANAGER
  Synchronizing SMS database with WSUS server <SERVERFQDN> ...
  SMS_WSUS_SYNC_MANAGER

WSyncMgr reads categories and updates from the WSUS database and inserts or updates the
Configuration Manager database. Software update metadata for each update is stored in the
site database as a configuration item (CI).

The following are logged in WsyncMgr.log:

  sync: SMS synchronizing categories SMS_WSUS_SYNC_MANAGER
  ...<log entries truncated>...
  sync: SMS synchronizing categories, processed 223 out of 223 items (100%)
  SMS_WSUS_SYNC_MANAGER
  sync: SMS synchronizing updates SMS_WSUS_SYNC_MANAGER

<!-- p.729 -->

  ...<log entries truncated>...
  Synchronizing update af5eb87e-cdd6-40bf-984f-5d0630406de8 - Definition Update for
  Microsoft Endpoint Protection - KB2461484 (Definition 1.165.1945.0)
  SMS_WSUS_SYNC_MANAGER
  ...<log entries truncated>...
  sync: SMS synchronizing updates, processed 5 out of 5 items (100%)
  SMS_WSUS_SYNC_MANAGER
  ...<log entries truncated>...
  Done synchronizing SMS with WSUS Server cs1site.contoso.com
  SMS_WSUS_SYNC_MANAGER
  Set content version of update source {C2D17964-BBDD-4339-B9F3-12D7205B39CC} for
  site CS1 to 34 SMS_WSUS_SYNC_MANAGER

After synchronization of the site database is complete, if any changes were made to the site
database, the content version of the update source is updated in the database. After
synchronization finishes successfully, WSyncMgr creates status message ID 6702 (WSUS
Synchronization done). The following are logged in WsyncMgr.log:

  STATMSG: ID=6702 SEV=I LEV=M SOURCE="SMS Server"
  COMP="SMS_WSUS_SYNC_MANAGER" SYS=<SERVEFRFQDN> SITE=CS1 PID=432
  TID=3404 GMTDATE=Thu Jan 16 18:57:46.304 2014 ISTR0="" ISTR1="" ISTR2="" ISTR3=""
  ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=0
  SMS_WSUS_SYNC_MANAGER
  Sync succeeded. Setting sync alert to canceled state on site CS1
  SMS_WSUS_SYNC_MANAGER
  Updated 130 items in SMS database, new update source content version is 34
  SMS_WSUS_SYNC_MANAGER
  Sync time: 0d00h03m53s SMS_WSUS_SYNC_MANAGER

Step 5: WSUS Synchronization Manager sends requests one at
a time to the WSUS component running on other SUPs on the
site
The WSUS computers on the other SUPs are configured as replicas of the WSUS installation
running on the default SUP for the site.

The following are logged in WsyncMgr.log:

<!-- p.730 -->

  Synchronizing replica WSUS servers SMS_WSUS_SYNC_MANAGER
  STATMSG: ID=6706 SEV=I LEV=M SOURCE="SMS Server"
  COMP="SMS_WSUS_SYNC_MANAGER" SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=1840
  TID=2832 GMTDATE=Thu Jan 16 19:17:13.575 2014 ISTR0="" ISTR1="" ISTR2="" ISTR3=""
  ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=0
  SMS_WSUS_SYNC_MANAGER
  Synchronizing WSUS server ps1sys.contoso.com ... SMS_WSUS_SYNC_MANAGER
  sync: Starting Replica WSUS synchronization SMS_WSUS_SYNC_MANAGER
  sync: Replica WSUS synchronizing other items SMS_WSUS_SYNC_MANAGER
  sync: Replica WSUS synchronizing other items, processed 4 out of 4 items (100%)
  SMS_WSUS_SYNC_MANAGER
  Done synchronizing WSUS Server ps1sys.contoso.com SMS_WSUS_SYNC_MANAGER

Step 6: WSUS Synchronization Manager sends a
synchronization request to all child sites
Sync notifications are sent to all child sites to instruct them to start synchronization. These
notifications are sent through file replication and not database replication. The following are
logged in WsyncMgr.log:

  Sending sync notification to child site(s): PS1, PS2 SMS_WSUS_SYNC_MANAGER
  SQL Replication type has not been set for
  E:\ConfigMgr\inboxes\WSyncMgr.box\outbox\CS1.SYN, replicating to (PS1, PS2), inbox:
  E:\ConfigMgr\inboxes\replmgr.box SMS_WSUS_SYNC_MANAGER

Step 7: The software updates configuration items are sent to
child sites by using database replication

Synchronization on child primary site and secondary
sites
During the software update synchronization process on the top-level site, the software update
configuration items are replicated to child sites by using database replication. At the end of the
process, the top-level site sends a synchronization request to the child site, and the child site
then starts the WSUS synchronization process. Because the software update metadata
(configuration items) from the site database is replicated to the primary sites through database

<!-- p.731 -->

replication, the synchronization process on the child primary and secondary sites consists of
only the WSUS synchronization phase.

The synchronization process on a child primary site or secondary site performs the following
steps:

Step 1: WSUS Synchronization Manager receives a
synchronization request from the top-level site
When the sync notification that's sent by the parent site arrives in the WSyncMgr.box folder
through file replication, WSyncMgr wakes up and starts synchronization. The following are
logged in WsyncMgr.log:

  Wakeup by inbox drop SMS_WSUS_SYNC_MANAGER
  Found parent sync notification file CS1.SYN. SMS_WSUS_SYNC_MANAGER
  Starting Sync SMS_WSUS_SYNC_MANAGER
  Performing sync on parent request SMS_WSUS_SYNC_MANAGER

WSyncMgr then reads the list of SUPs from the site control file (SCF). WSyncMgr will first
synchronize the SUP that was installed as the first SUP in the site and then synchronize all
remaining SUPs. All additional SUPs are configured as replicas of the first SUP. The following
are logged in WsyncMgr.log:

  Read SUPs from SCF for PS1SITE.CONTOSO.COM SMS_WSUS_SYNC_MANAGER
  Found 2 SUPs SMS_WSUS_SYNC_MANAGER
  Found active SUP PS1SITE.CONTOSO.COM from SCF File. SMS_WSUS_SYNC_MANAGER
  Found active SUP PS1SYS.CONTOSO.COM from SCF File. SMS_WSUS_SYNC_MANAGER

Step 2: Software updates synchronization begins
The following are logged in WsyncMgr.log:

  STATMSG: ID=6701 SEV=I LEV=M SOURCE="SMS Server"
  COMP="SMS_WSUS_SYNC_MANAGER" SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=1840
  TID=2832 GMTDATE=Thu Jan 16 18:58:37.599 2014 ISTR0="" ISTR1="" ISTR2="" ISTR3=""
  ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=0
  SMS_WSUS_SYNC_MANAGER
  Synchronizing WSUS server PS1SITE.CONTOSO.COM SMS_WSUS_SYNC_MANAGER

<!-- p.732 -->

Step 3: WSUS Synchronization Manager makes a request to
WSUS running on the first SUP to start synchronization
The following are logged in WsyncMgr.log:

  STATMSG: ID=6704 SEV=I LEV=M SOURCE="SMS Server"
  COMP="SMS_WSUS_SYNC_MANAGER" SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=1840
  TID=2832 GMTDATE=Thu Jan 16 18:58:38.909 2014 ISTR0="" ISTR1="" ISTR2="" ISTR3=""
  ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=0
  SMS_WSUS_SYNC_MANAGER
  Synchronizing WSUS server ps1site.contoso.com ... SMS_WSUS_SYNC_MANAGER

Step 4: WSUS running on the SUP on the child site
synchronizes software updates metadata from WSUS running
on the SUP on the parent site
The following are logged in WsyncMgr.log:

  sync: Starting WSUS synchronization SMS_WSUS_SYNC_MANAGER
  sync: WSUS synchronizing categories SMS_WSUS_SYNC_MANAGER
  sync: WSUS synchronizing updates SMS_WSUS_SYNC_MANAGER
  sync: WSUS synchronizing updates, processed 130 out of 130 items (100%)
  SMS_WSUS_SYNC_MANAGER
  Done synchronizing WSUS Server ps1site.contoso.com SMS_WSUS_SYNC_MANAGER
  Sleeping 2 more minutes for WSUS server sync results to become available
  SMS_WSUS_SYNC_MANAGER
  Set content version of update source {C2D17964-BBDD-4339-B9F3-12D7205B39CC} for
  site PS1 to 34 SMS_WSUS_SYNC_MANAGER

Step 5: (For Configuration Manager with no service pack only)
WSUS Synchronization Manager starts the synchronization
process for WSUS running on the remote site system
When there is a remote Internet-based SUP, WSUS Synchronization Manager starts the
synchronization process for WSUS running on the remote site system.

<!-- p.733 -->

Step 6: (For System Center 2012 Configuration Manager SP1
and System Center 2012 R2 Configuration Manager only)
WSUS Synchronization Manager sends requests one at a time
to WSUS running on other SUPs (including Internet-based
SUPs) at the site
The WSUS servers on the other SUPs are configured as replicas of WSUS running on the
default SUP at the site. WSyncMgr then creates status message ID 6706 (WSUS Synchronization
in progress. Current phase: Synchronizing Internet-facing WSUS server). Even though the SUP
may not be Internet-based, the status message will still be 6706.

The following are logged in WsyncMgr.log:

  Synchronizing replica WSUS servers SMS_WSUS_SYNC_MANAGER
  STATMSG: ID=6706 SEV=I LEV=M SOURCE="SMS Server"
  COMP="SMS_WSUS_SYNC_MANAGER" SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=1840
  TID=2832 GMTDATE=Thu Jan 16 19:17:13.575 2014 ISTR0="" ISTR1="" ISTR2="" ISTR3=""
  ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=0
  SMS_WSUS_SYNC_MANAGER
  Synchronizing WSUS server ps1sys.contoso.com ... SMS_WSUS_SYNC_MANAGER
  sync: Starting Replica WSUS synchronization SMS_WSUS_SYNC_MANAGER
  sync: Replica WSUS synchronizing other items SMS_WSUS_SYNC_MANAGER
  sync: Replica WSUS synchronizing other items, processed 4 out of 4 items (100%)
  SMS_WSUS_SYNC_MANAGER
  Done synchronizing WSUS Server ps1sys.contoso.com SMS_WSUS_SYNC_MANAGER

Step 7: When synchronization has finished successfully, WSUS
Synchronization Manager creates status message 6702
The following are logged in WsyncMgr.log:

  STATMSG: ID=6702 SEV=I LEV=M SOURCE="SMS Server"
  COMP="SMS_WSUS_SYNC_MANAGER" SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=1840
  TID=2832 GMTDATE=Thu Jan 16 19:01:35.117 2014 ISTR0="" ISTR1="" ISTR2="" ISTR3=""
  ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=0
  SMS_WSUS_SYNC_MANAGER
  Sync succeeded. Setting sync alert to canceled state on site PS1
  SMS_WSUS_SYNC_MANAGER

<!-- p.734 -->

  Successfully synced site with parent CS1, version 34 SMS_WSUS_SYNC_MANAGER
  Sync time: 0d00h02m57s SMS_WSUS_SYNC_MANAGER

Step 8: From a primary site, WSUS Synchronization Manager
sends a synchronization request to any child secondary sites
The secondary site starts the software updates synchronization with the parent primary site.
The secondary site's SUP is configured as a replica of WSUS running on the parent site.

The following is logged in WsyncMgr.log:

  Sending sync notification to child site(s): SS1 SMS_WSUS_SYNC_MANAGER

Last updated on 03/30/2026

<!-- p.735 -->

Track software update compliance assessment
Applies to: Configuration Manager

Before you can deploy software updates to clients, the clients must run a software updates compliance scan. We recommend that you
allow enough time for clients to complete the scan and report compliance results so that you can review the compliance results and
deploy only the updates that are required on the clients.

When the software update point (SUP) is installed and synchronized, a site-wide machine policy is created that informs client computers
that Configuration Manager Software Updates was enabled for the site. When a client receives the machine policy, a compliance
assessment scan is scheduled to start randomly within the next two hours. When the scan is started, a Software Updates Client Agent
process clears the scan history, submits a request to find the Windows Server Update Services (WSUS) server that should be used for the
scan, and updates the local Group Policy with the WSUS location.

For an overview of the compliance assessment process, see Software updates compliance assessment.

Software update scan policy
Before a client can try to scan for updates, it needs the UpdateSource policy. This policy is created on the site server after a successful
synchronization of the SUP. This section discusses how this policy is created by the following process:

Step 1: After a successful synchronization, WSyncMgr updates the Content
Version and Last Sync Time in the database
After a successful synchronization on a primary site, WSyncMgr updates Last Sync Time and Content Version in the database for the SUP.
This is done by executing the spProcessSUMSyncStateMessage stored procedure. In the following sample SQL Server Profiler trace, this
stored procedure is executed to update the content version to 36:

  declare @Error int; exec spProcessSUMSyncStateMessage N'2014-01-17 17:59:54', N'PS1', N'{C2D17964-BBDD-4339-B9F3-
  12D7205B39CC}', 1, 0, '36', @Error output, N'PS1SITE.CONTOSO.COM'

Step 2: SMSDBMON gets triggered and drops a .STN file in policypv.box
spProcessSUMSyncStateMessage updates the Update_SyncStatus table with the new Content Version and Sync Time. This update to the

Update_SyncStatus table triggers SMSDBMON to drop a <UpdateSource_UniqueID>.STN file (STN stands for Scan Tool Notification) in

policypv.box to indicate a change in the scan tool definition. The following are logged in SMSDBMON.log:

  RCV: UPDATE on Update_SyncStatus for UpdSyncStatus_iu [{C2D17964-BBDD-4339-B9F3-12D7205B39CC}][46680]
  SMS_DATABASE_NOTIFICATION_MONITOR
  SND: Dropped E:\ConfigMgr\inboxes\policypv.box{C2D17964-BBDD-4339-B9F3-12D7205B39CC}.STN (non-zero) [46680]
  SMS_DATABASE_NOTIFICATION_MONITOR

Step 3: Policy Provider creates or updates the UpdateSource policy in the
database
The <UpdateSource_UniqueID>.STN file notifies Policy Provider that it should wake up and update the UpdateSource policy in the
database.

The following are logged in PolicyPv.log:

  Found {C2D17964-BBDD-4339-B9F3-12D7205B39CC}.STN SMS_POLICY_PROVIDER
  Added Scan Tool ID {C2D17964-BBDD-4339-B9F3-12D7205B39CC} SMS_POLICY_PROVIDER
  Adding to delete list: E:\ConfigMgr\inboxes\policypv.box{C2D17964-BBDD-4339-B9F3-12D7205B39CC}.STN SMS_POLICY_PROVIDER

<!-- p.736 -->

In SQL Server Profiler trace:

  select PolicyID, PolicyAssignmentID, SourceCRC, PADBID from SettingsPolicy where SourceID = N'PS1' and SourceType =
  N'UpdateSource'

  select Version from Policy where PolicyID = N'{d0855677-b0a6-4e33-9bd5-7b0d06f0a2be}'
  IF EXISTS (select PolicyID from Policy where PolicyID = N'{d0855677-b0a6-4e33-9bd5-7b0d06f0a2be}') update Policy set Version =
  N'40.00' where PolicyID = N'{d0855677-b0a6-4e33-9bd5-7b0d06f0a2be}' ELSE insert Policy (PolicyID, Version) values (N'{d0855677-
  b0a6-4e33-9bd5-7b0d06f0a2be}', N'40.00')

  exec sp_describe_undeclared_parameters N'UPDATE Policy SET Body = @P1 where PolicyID = N''{d0855677-b0a6-4e33-9bd5-
  7b0d06f0a2be}'''
  IF EXISTS (select PADBID from PolicyAssignment where PADBID = 16777218) update PolicyAssignment set Version = N'40.00',
  InProcess = 1 , BodyHash = null where PADBID = 16777218 ELSE insert PolicyAssignment (PolicyAssignmentID, PADBID, Version,
  PolicyID) values (N'{375c8020-3cae-4736-89ca-ccf1ce6e3709}', 16777218, N'40.00', N'{d0855677-b0a6-4e33-9bd5-7b0d06f0a2be}')

  exec sp_describe_undeclared_parameters N'UPDATE PolicyAssignment SET Body = @P1 where PADBID = 16777218'

  update PolicyAssignment set InProcess = 0, BodySignature = N'<BodySignatureTruncated>', TombstoneBodySignature =
  N'<TombstoneBodySignatureTruncated>', HashAlgOID = N'1.2.840.113549.1.1.11', HashAlgId = 32780, BodyHash =
  N'<BodyHashTruncated>', TombstoneBodyHash = N'<TombstoneBodyHashTruncated>' where PADBID = 16777218

To see this policy in the database, run the following query:

 SQL

 SELECT CONVERT(XML, Body, 1), * FROM Policy WHERE PolicyID = (SELECT PolicyID FROM SettingsPolicy WHERE SourceType =
 'UpdateSource')

This policy contains the content version of the update server which is used to find the location of the WSUS computer that the client can
scan against. After this policy is created or updated in the database, the clients get the new or updated UpdateSource policy during the
next policy evaluation cycle.

Step 4: Policy is downloaded and evaluated on the client
The following are logged in PolicyAgent.log on the client:

  Successfully initiated download of policy 'CCM_Policy_Policy5.PolicyID="{d0855677-b0a6-4e33-9bd5-
  7b0d06f0a2be}",PolicySource="SMS:PS1",PolicyVersion="40.00"' PolicyAgent_ReplyAssignments
  Policy 'CCM_Policy_Policy5.PolicyID="{d0855677-b0a6-4e33-9bd5-7b0d06f0a2be}",PolicyVersion="40.00",PolicySource="SMS:PS1"'
  successfully compiled PolicyAgent_PolicyDownload

In PolicyEvaluator.log on the client:

  Updating policy CCM_Policy_Policy5.PolicyID="{d0855677-b0a6-4e33-9bd5-
  7b0d06f0a2be}",PolicySource="SMS:PS1",PolicyVersion="40.00" PolicyAgent_PolicyEvaluator
  Applied policy CCM_Policy_Policy5.PolicyID="{d0855677-b0a6-4e33-9bd5-
  7b0d06f0a2be}",PolicySource="SMS:PS1",PolicyVersion="40.00" PolicyAgent_PolicyEvaluator
  Policy state for [CCM_Policy_Policy5.PolicyID="{d0855677-b0a6-4e33-9bd5-
  7b0d06f0a2be}",PolicyVersion="40.00",PolicySource="SMS:PS1"] is currently [Active] PolicyAgent_PolicyEvaluator

To find the PolicyID of the UpdateSource policy on a client, run the following WQL query:

     Namespace: ROOT\ccm\Policy\Machine\RequestedConfig
     Query: SELECT * FROM CCM_Policy_Policy5 WHERE PolicyCategory = 'UpdateSource'

Once this policy is compiled on the client, the UpdateSource information is stored in the following WMI Class:

<!-- p.737 -->

  Namespace: ROOT\ccm\Policy\Machine\ActualConfig
  Class: CCM_UpdateSource

   Tip

  If you compare the instance of CCM_UpdateSource class on the client with the XML body retrieved from the policy table, you will notice
  that the content of the XML looks identical to the instance.

Step 5: Scan Agent is notified that the UpdateSource policy is updated
The following are logged in ScanAgent.log on the client:

  Inside CScanAgent::Notify() ScanAgent
  CScanAgent::OnPolicyChange- Policy InstanceModificationEvent notification received ScanAgent

WSUS server location
After receiving the UpdateSource policy, the client has the necessary configuration to initiate a scan. However, policy updates won't initiate
immediate scans. A scan can be triggered manually through the Configuration Manager control panel or occur automatically at the next
scheduled time. At this point, the client locates the WSUS computer with the content version specified in the policy. This process is very
similar to the way that the client finds the location of a distribution point for a specific package and version.

Step 1: Scan Agent creates a scan request based on the available policy
The following are logged in ScanAgent.log:

  CScanAgent::ScanByUpdates- Policy available for UpdateSourceID={C2D17964-BBDD-4339-B9F3-12D7205B39CC} ContentVersion=38
  ScanAgent
  CScanAgent::ScanByUpdates- Added Policy to final ScanRequest List UpdateSourceID={C2D17964-BBDD-4339-B9F3-12D7205B39CC},
  Policy-ContentVersion=38, Required-ContentVersion=38 ScanAgent

Step 2: Scan Agent sends a request for the WSUS location to Location Services
Scan Agent now requests the WSUS location from Location Services and waits for a response. In this example, the location request ID is
{C2BB9710-C548-49D0-9DF8-5F9CFC5F3862}. The following are logged in ScanAgent.log:

  Inside CScanAgent::ProcessScanRequest() ScanAgent
  CScanJobManager::Scan- entered ScanAgent
  ScanJob({4CD06388-D509-46E4-8C00-75909EDD9EE8}): CScanJob::Initialize- entered ScanAgent
  ScanJob({4CD06388-D509-46E4-8C00-75909EDD9EE8}): CScanJob::Scan- entered ScanAgent
  ScanJob({4CD06388-D509-46E4-8C00-75909EDD9EE8}): CScanJob::RequestLocations- entered ScanAgent
  - - - - - -Requesting WSUS Server Locations from LS for {C2D17964-BBDD-4339-B9F3-12D7205B39CC} version 38 ScanAgent
  - - - - - -Location Request ID = {C2BB9710-C548-49D0-9DF8-5F9CFC5F3862} ScanAgent
  CScanAgentCache::PersistInstanceInCache- Persisted Instance CCM_ScanJobInstance ScanAgent
  ScanJob({4CD06388-D509-46E4-8C00-75909EDD9EE8}): - - - - - -Locations requested for ScanJobID={4CD06388-D509-46E4-8C00-
  75909EDD9EE8} (LocationRequestID={C2BB9710-C548-49D0-9DF8-5F9CFC5F3862}), will process the scan request once locations are
  available. ScanAgent

Each scan job is stored in WMI in the CCM_ScanJobInstance class:

  Namespace: root\CCM\ScanAgent
  Class: CCM_ScanJobInstance

<!-- p.738 -->

Step 3: Location Services sends the location request to the management point
Location Services creates a location request and sends it to the management point. The package ID for a WSUS location request is the
UpdateSource unique ID. The following are logged in LocationServices.log:

  CCCMWSUSLocation::GetLocationsAsyncEx LocationServices
  Attempting to persist WSUS location request for ContentID='{C2D17964-BBDD-4339-B9F3-12D7205B39CC}' and ContentVersion='38'
  LocationServices
  Persisted WSUS location request LocationServices
  Attempting to send WSUS Location Request for ContentID='{C2D17964-BBDD-4339-B9F3-12D7205B39CC}' LocationServices
  WSUSLocationRequest : <WSUSLocationRequest SchemaVersion="1.00"><Content ID="{C2D17964-BBDD-4339-B9F3-
  12D7205B39CC}" Version="38"/><AssignedSite SiteCode="PS1"/><ClientLocationInfo OnInternet="0"><ADSite Name="CM12-R2-
  PS1"/><Forest Name="CONTOSO.COM"/><Domain Name="CONTOSO.COM"/><IPAddresses><IPAddress
  SubnetAddress="192.168.2.0" Address="192.168.2.62"/></IPAddresses></ClientLocationInfo></WSUSLocationRequest>
  LocationServices
  Created and Sent Location Request '{C2BB9710-C548-49D0-9DF8-5F9CFC5F3862}' for package {C2D17964-BBDD-4339-B9F3-
  12D7205B39CC} LocationServices

Step 4: CCM Messaging sends the location request message to the
management point
The following are logged in CcmMessaging.log:

  Sending async message '{76453CC6-76BA-4B68-BE30-BA70754570BB}' to outgoing queue 'mp:[http]mp_locationmanager'
  CcmMessaging
  Sending outgoing message '{76453CC6-76BA-4B68-BE30-BA70754570BB}'. Flags 0x200, sender account empty CcmMessaging

Step 5: The management point parses the request, obtains the WSUS location
from the database, and sends a response
The management point parses this request and calls the MP_GetWSUSServerLocations stored procedure to get the WSUS locations from the
database. The following are logged in MP_Location.log:

  MP LM: Message Body : <WSUSLocationRequest SchemaVersion="1.00"><Content ID="{C2D17964-BBDD-4339-B9F3-
  12D7205B39CC}" Version="38"/><AssignedSite SiteCode="PS1"/><ClientLocationInfo OnInternet="0"><ADSite Name="CM12-R2-
  PS1"/><Forest Name="CONTOSO.COM"/><Domain Name="CONTOSO.COM"/><IPAddresses><IPAddress
  SubnetAddress="192.168.2.0" Address="192.168.2.62"/></IPAddresses></ClientLocationInfo></WSUSLocationRequest>
  MP_LocationManager
  MP LM: calling MP_GetWSUSServerLocations MP_LocationManager

In SQL Server Profiler trace:

  exec MP_GetMPSitesFromAssignedSite N'PS1'
  exec MP_GetSiteInfoUnified N'<ClientLocationInfo OnInternet="0"><ADSite Name="CM12-R2-PS1"/><Forest
  Name="CONTOSO.COM"/><Domain Name="CONTOSO.COM"/><IPAddresses><IPAddress SubnetAddress="192.168.2.0"
  Address="192.168.2.62"/></IPAddresses></ClientLocationInfo>'
  exec MP_GetWSUSServerLocations N'{C2D17964-BBDD-4339-B9F3-12D7205B39CC}',N'38',N'PS1',N'PS1',N'0',N'CONTOSO.COM'

After getting the results from the stored procedure, the management point sends a response to the client. The following is logged in
MP_Location.log:

  MP LM: Reply message body:
  <WSUSLocationReply SchemaVersion="1.00"><Sites><Site><MPSite SiteCode="PS1"/><LocationRecords><LocationRecord

<!-- p.739 -->

  WSUSURL=" http://PS1SITE.CONTOSO.COM:8530 " ServerName="PS1SITE.CONTOSO.COM" Version="38"/><LocationRecord
  WSUSURL=" https://PS1SYS.CONTOSO.COM:8531 " ServerName="PS1SYS.CONTOSO.COM" Version="38"/></LocationRecords></Site>
  </Sites></WSUSLocationReply> MP_LocationManager

Step 6: CCM Messaging receives the response and sends it back to Location
Services
The CcmMessaging.log file on the client shows that a reply was received. This message was delivered to Location Services:

  Message '{76453CC6-76BA-4B68-BE30-BA70754570BB}' got reply '{8E6D05EF-B77F-4AD0-AF64-1C6F3069A29C}' to local endpoint
  queue 'LS_ReplyLocations' CcmMessaging
  OutgoingMessage(Queue='mp_[http]mp_locationmanager', ID={76453CC6-76BA-4B68-BE30-BA70754570BB}): Delivered successfully
  to host 'PS1SYS.CONTOSO.COM'. CcmMessaging
  Message '{8E6D05EF-B77F-4AD0-AF64-1C6F3069A29C}' delivered to endpoint 'LS_ReplyLocations' CcmMessaging

Step 7: Location Services parses the response and sends the location back to
Scan Agent
The following are logged in LocationServices.log:

  Processing Location reply message LocationServices 1/20/2014 12:18:09 PM
  WSUSLocationReply : <WSUSLocationReply SchemaVersion="1.00"><Sites><Site><MPSite SiteCode="PS1"/><LocationRecords>
  <LocationRecord WSUSURL=" http://PS1SITE.CONTOSO.COM:8530 " ServerName="PS1SITE.CONTOSO.COM" Version="38"/>
  <LocationRecord WSUSURL=" https://PS1SYS.CONTOSO.COM:8531 " ServerName="PS1SYS.CONTOSO.COM" Version="38"/>
  </LocationRecords></Site></Sites></WSUSLocationReply> LocationServices
  Calling back with the following WSUS locations LocationServices
  WSUS Path=' http://PS1SITE.CONTOSO.COM:8530 ', Server='PS1SITE.CONTOSO.COM', Version='38' LocationServices
  WSUS Path=' https://PS1SYS.CONTOSO.COM:8531 ', Server='PS1SYS.CONTOSO.COM', Version='38' LocationServices
  Calling back with locations for WSUS request {C2BB9710-C548-49D0-9DF8-5F9CFC5F3862} LocationServices

Step 8: Scan Agent notifies WUAHandler to add the update source to the
registry
Scan Agent now has the policy and the update source location with the appropriate content version. The following are logged in
ScanAgent.log:

  *****WSUSLocationUpdate received for location request guid={C2BB9710-C548-49D0-9DF8-5F9CFC5F3862} ScanAgent
  ScanJob({4CD06388-D509-46E4-8C00-75909EDD9EE8}): CScanJob::OnLocationUpdate- Received
  Location= http://PS1SITE.CONTOSO.COM:8530 , Version=38 ScanAgent
  ScanJob({4CD06388-D509-46E4-8C00-75909EDD9EE8}): CScanJob::Execute- Adding UpdateSource={C2D17964-BBDD-4339-B9F3-
  12D7205B39CC}, ContentType=2, ContentLocation= http://PS1SITE.CONTOSO.COM:8530 , ContentVersion=38 ScanAgent

Scan Agent notifies WUAHandler to add the update source. WUAHandler adds the update source to the registry and initiates a Group
Policy refresh (if the client is in domain) to see whether Group Policy overrides the update server that we just added. The following are
logged in WUAHandler.log on a new client showing a new update source being added:

  Its a WSUS Update Source type ({C2D17964-BBDD-4339-B9F3-12D7205B39CC}), adding it. WUAHandler
  Its a completely new WSUS Update Source. WUAHandler
  Enabling WUA Managed server policy to use server: http://PS1SITE.CONTOSO.COM:8530 WUAHandler
  Policy refresh forced. WUAHandler
  Waiting for 2 mins for Group Policy to notify of WUA policy change... WUAHandler
  Waiting for 30 secs for policy to take effect on WU Agent. WUAHandler
  Added Update Source ({C2D17964-BBDD-4339-B9F3-12D7205B39CC}) of content type: 2 WUAHandler

<!-- p.740 -->

During this time, the Windows Update Agent sees a WSUS configuration change. The following are logged in WindowsUpdate.log:

  2014-01-20 12:18:11:520 968 9d0 Agent * WSUS server: http://PS1SITE.CONTOSO.COM:8530 (Changed)
  2014-01-20 12:18:11:520 968 9d0 Agent * WSUS status server: http://PS1SITE.CONTOSO.COM:8530 (Changed)
  2014-01-20 12:18:11:520 968 9d0 AU Sus server changed through policy.

The following registry keys are checked and set:

                                                                                                                                ﾉ   Expand table

 Registry subkey                                                                       Value name       Type        Data

 HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\WindowsUpdate      WUServer         REG_SZ      The full WSUS server URL
                                                                                                                    including the port. For example,
                                                                                                                    http://PS1Site.Contoso.com:8530

 HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\WindowsUpdate      WUStatusServer   REG_SZ      The full WSUS server URL
                                                                                                                    including the port. For example,
                                                                                                                    http://PS1Site.Contoso.com:8530

 HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\WindowsUpdate\AU   UseWUServer      REG_DWORD   0x1

For an existing client, we could expect to see the following in WUAHandler.log to denote when content version has incremented:

  Its a WSUS Update Source type ({C2D17964-BBDD-4339-B9F3-12D7205B39CC}), adding it. WUAHandler
  WSUS update source already exists, it has increased version to 38. WUAHandler

Step 9: Scan Agent initiates the scan
After the update source is successfully added, Scan Agent raises a state message and initiates the scan. The following are logged in
ScanAgent.log:

  ScanJob({4CD06388-D509-46E4-8C00-75909EDD9EE8}): Raised UpdateSource ({C2D17964-BBDD-4339-B9F3-12D7205B39CC}) state
  message successfully. StateId = 2 ScanAgent
  ScanJob({4CD06388-D509-46E4-8C00-75909EDD9EE8}): CScanJob::Execute - successfully requested Scan, ScanType=1 ScanAgent

Software update scan on clients
After the update source policy and the update source location are available, Scan Agent initiates the scan. Software update scan is actually
performed by the Windows Update Agent. However, the Configuration Manager client interacts with the Windows Update Agent to
perform a scan and obtain the scan results. This interaction is handled by the Windows Update Agent Handler (WUAHandler) component,
which communicates with the Windows Update Agent.

Step 1: Scan Agent requests the scan and WUAHandler initiates the scan
Scan Agent requests the scan from WUAHandler, which uses the Windows Update Agent API to request a software update scan from the
Windows Update Agent. The following is logged in ScanAgent.log:

  ScanJob({4CD06388-D509-46E4-8C00-75909EDD9EE8}): CScanJob::Execute - successfully requested Scan, ScanType=1 ScanAgent

The following are logged in WUAHandler.log:

  Scan results will include superseded updates only when they are superseded by service packs and definition updates. WUAHandler
  Search Criteria is (DeploymentAction=* AND Type='Software') OR (DeploymentAction=* AND Type='Driver') WUAHandler
  Running single-call scan of updates. WUAHandler
  Async searching of updates using WUAgent started. WUAHandler

<!-- p.741 -->

Step 2: Windows Update Agent (WUA) starts the scan against the WSUS
computer
Windows Update Agent starts a scan after receiving a request from the Configuration Manager client (CcmExec). Because the Windows
Update Server value was already set to the SUP server, this scan is performed against the WSUS server that has the SUP role installed. The
following are logged in WindowsUpdate.log:

  2014-01-20 12:18:42:694 3856 708 COMAPI -- START -- COMAPI: Search [ClientId = CcmExec]
  2014-01-20 12:18:42:752 3856 708 COMAPI <<-- SUBMITTED -- COMAPI: Search [ClientId = CcmExec]
  2014-01-20 12:18:47:511 968 f58 PT + ServiceId = {3DA21691-E39D-4DA6-8A4B-B43877BCB1B7}, Server URL =
  http://PS1SITE.CONTOSO.COM:8530/ClientWebService/client.asmx

  2014-01-20 12:18:48:662 968 f58 Agent ** START ** Agent: Finding updates [CallerId = CcmExec]
  2014-01-20 12:18:48:662 968 f58 Agent * Include potentially superseded updates
  2014-01-20 12:18:48:662 968 f58 Agent * Online = Yes; Ignore download priority = Yes
  2014-01-20 12:18:48:662 968 f58 Agent * Criteria = "(DeploymentAction=* AND Type='Software') OR (DeploymentAction=* AND
  Type='Driver')"
  2014-01-20 12:18:48:662 968 f58 Agent * ServiceID = {3DA21691-E39D-4DA6-8A4B-B43877BCB1B7} Managed
  2014-01-20 12:18:48:662 968 f58 Agent * Search Scope = {Machine}

Windows Update Agent now scans against the WSUS server and reports the results to CcmExec (specifically WUAHandler). The following
are logged in WindowsUpdate.log:

  2014-01-20 12:18:49:175 968 f58 PT + ServiceId = {3DA21691-E39D-4DA6-8A4B-B43877BCB1B7}, Server URL =
  http://PS1SITE.CONTOSO.COM:8530/ClientWebService/client.asmx

  2014-01-20 12:18:52:680 968 f58 Agent * Added update {4AE85C00-0EAA-4BE0-B81B-DBD7053D5FAE}.104 tosearch result
  2014-01-20 12:18:52:683 968 f58 Agent * Added update {57260DFE-227C-45E3-9FFC-2FC77A67F95A}.104 to search result
  2014-01-20 12:18:52:694 968 f58 Agent * Found 163 updates and 70 categories in search; evaluated appl. rules of 622 out of 1150
  deployed entities
  2014-01-20 12:18:52:745 968 f58 Agent ** END ** Agent: Finding updates [CallerId = CcmExec]
  2014-01-20 12:18:52:755 3856 708 COMAPI >>-- RESUMED -- COMAPI: Search [ClientId = CcmExec]
  2014-01-20 12:18:53:137 3856 708 COMAPI - Updates found = 163
  2014-01-20 12:18:53:137 3856 708 COMAPI -- END -- COMAPI: Search [ClientId = CcmExec]

Step 3: WUAHandler receives the results from the Windows Update Agent and
marks the scan as complete
The following are logged in WUAHandler.log:

  Async searching completed. WUAHandler
  Finished searching for everything in single call. WUAHandler

Step 4: WUAHandler parses the scan results
WUAHandler then parses the results, which include the applicability state for each update. As part of this process, superseded updates are
pruned out. The following are logged in WUAHandler.log:

  Pruning: update id (70f4f236-0248-4e84-b472-292913576fa1) is superseded by (726b7201-862a-4fde-9b12-f36b38323a6f).
  WUAHandler
  ...
  Update (Installed): Security Update for Windows 7 for x64-based Systems (KB2584146) (4ae85c00-0eaa-4be0-b81b-dbd7053d5fae,
  104) WUAHandler
  Update (Missing): Security Update for Windows 7 for x64-based Systems (KB2862152) (00001111-aaaa-2222-bbbb-3333cccc4444, 200)
  WUAHandler

<!-- p.742 -->

  ...
  Successfully completed scan. WUAHandler

Step 5: Update store records the status and raises a state message for each
update in WMI
Once the scan results are available, these results are stored in the updates store. Update store records the current state of each update and
creates a state message for each update. These state messages are forwarded to the site server in bulk at the end of the status message
reporting cycle (which is 15 minutes, by default).

UpdatesStore.log showing state for missing update (KB2862152) being recorded and a state message being raised:

  Processing update status from update (00001111-aaaa-2222-bbbb-3333cccc4444) with ProductID = 0fa1201d-4330-4fa8-8ae9-
  b877473b6441 UpdatesStore
  Update status from update (00001111-aaaa-2222-bbbb-3333cccc4444) hasn't been reported before, creating new instance.
  UpdatesStore
  Successfully raised state message for update (00001111-aaaa-2222-bbbb-3333cccc4444) with state (Missing). UpdatesStore
  Successfully added WMI instance of update status (00001111-aaaa-2222-bbbb-3333cccc4444). UpdatesStore

StateMessage.log showing state message being recorded with State ID 2 (missing):

  Adding message with TopicType 500 and TopicId 00001111-aaaa-2222-bbbb-3333cccc4444 to WMI StateMessage
  State message(State ID : 2) with TopicType 500 and TopicId 00001111-aaaa-2222-bbbb-3333cccc4444 has been recorded for SYSTEM
  StateMessage

For each update, an instance of the CCM_UpdateStatus class is created or updated, and this stores the current status of the update. The
CCM_UpdateStatus class is located in the ROOT\CCM\SoftwareUpdates\UpdatesStore namespace.

Similarly, an instance of the CCM_StateMsg class is created or updated, and this stores the current state of the update. The CCM_StateMsg
class is located in the ROOT\CCM\StateMsg namespace.

<!-- p.743 -->

Step 6: State messages are sent to the management point
As mentioned earlier, state messages are sent to the management point based on the state message reporting cycle schedule, which is
configured to 15 minutes by default. Once a state message is sent to the management point, the MessageSent property for the state
message instance in the CCM_StateMsg class is set to True.

In StateMessage.log:

  StateMessage body: <XML Report Body Truncated> StateMessage
  Successfully forwarded State Messages to the MP StateMessage

The following is how the state message body looks like for our update. Normally this XML body is too large for the log and is truncated in
CMTrace. However, you can see the whole XML body in Notepad.

  StateMessage body: <?xml version="1.0" encoding="UTF-16"?>
  <Report><ReportHeader><Identification><Machine><ClientInstalled>1</ClientInstalled><ClientType>1</ClientType>
  <ClientID>GUID: 00001111-aaaa-2222-bbbb-3333cccc4444</ClientID><ClientVersion>5.00.7958.1000</ClientVersion>
  <NetBIOSName>PS1WIN7X64</NetBIOSName><CodePage>437</CodePage><SystemDefaultLCID>1033</SystemDefaultLCID>
  <Priority>5</Priority></Machine></Identification><ReportDetails><ReportContent>State Message Data</ReportContent>
  <ReportType>Full</ReportType><Date>20140120194656.903000+000</Date><Version>1.0</Version><Format>1.0</Format>
  </ReportDetails></ReportHeader><ReportBody><StateMessage MessageTime="20140120171855.573000+000"
  SerialNumber="232"><Topic ID="00001111-aaaa-2222-bbbb-3333cccc4444" Type="500" IDType="3" User="" UserSID=""/><State
  ID="2" Criticality="0"/><UserParameters Flags="0" Count="1"><Param>200</Param></UserParameters></StateMessage>
  </ReportBody></Report> StateMessage
  Successfully forwarded State Messages to the MP StateMessage

State message processing flow
We now know how a state message is recorded and the WMI location where these state messages are stored. We also know that unsent
state messages on a client are sent to the management point every 15 minutes by default, per the state message reporting cycle. This
schedule can be modified in the State Messaging of the custom or default client settings.

Although StateMessage.log reports Successfully forwarded State Messages to the MP, the State Message component isn't actually
sending these messages itself. All messages sent and received from the management point are handled by the CCM Messaging
component on the client. CCM Messaging is the actual component that communicates with the management point for sending and
receiving data. The management point has various queues defined to handle different kinds of incoming traffic. For state messages, the
queue that handles this traffic is the MP_RelayEndpoint queue.

<!-- p.744 -->

Step 1: The State Message component starts sending messages to the
management point
In StateMessage.log:

  StateMessage body: <?xml version="1.0" encoding="UTF-16"?> <Report><ReportHeader><Identification><Machine>
  <ClientInstalled>1</ClientInstalled><ClientType>1</ClientType><ClientID>GUID: 00001111-aaaa-2222-bbbb-
  3333cccc4444</ClientID><ClientVersion>5.00.7958.1000</ClientVersion><NetBIOSName>PS1WIN7X64</NetBIOSName>
  <CodePage>437</CodePage><SystemDefaultLCID>1033</SystemDefaultLCID><Priority>5</Priority></Machine></Identification>
  <ReportDetails><ReportContent>State Message Data</ReportContent><ReportType>Full</ReportType>
  <Date>20140120194656.903000+000</Date><Version>1.0</Version><Format>1.0</Format></ReportDetails></ReportHeader>
  <ReportBody><StateMessage MessageTime="20140120171855.573000+000" SerialNumber="232"><Topic ID="00001111-aaaa-
  2222-bbbb-3333cccc4444" Type="500" IDType="3" User="" UserSID=""/><State ID="2" Criticality="0"/><UserParameters Flags="0"
  Count="1"><Param>200</Param></UserParameters></StateMessage></ReportBody></Report> StateMessage
  Successfully forwarded State Messages to the MP StateMessage

Step 2: CCM Messaging sends a message containing the state message XML
body to the management point
CCM Messaging sends a message to the MP_RelayEndpoint queue successfully. This message doesn't have a reply, unlike the one we
noticed earlier in the WSUS Location Request section where the message with the Location Request received a reply.

In CcmMessaging.log:

  Sending async message '{95F79010-D0EB-49A6-8A1E-3897883105F2}' to outgoing queue 'mp:mp_relayendpoint' CcmMessaging
  Sending outgoing message '{95F79010-D0EB-49A6-8A1E-3897883105F2}'. Flags 0x200, sender account empty CcmMessaging
  POST: Host=PS1SYS.CONTOSO.COM, Path=/ccm_system/request, Port=443, Protocol=https, Flags=512, Options=480 CcmMessaging
  Message '{95F79010-D0EB-49A6-8A1E-3897883105F2}' doesn't have reply CcmMessaging
  OutgoingMessage(Queue='mp_mp_relayendpoint', ID={95F79010-D0EB-49A6-8A1E-3897883105F2}): Delivered successfully to host
  'PS1SYS.CONTOSO.COM'. CcmMessaging

Step 3: The message is received on the management point, and then MP_Relay
processes the message and creates an SMX file
As all messages are sent using HTTP/HTTPS and are received by IIS. In this example, this request is made to the CCM_System virtual
directory.

In IIS log:

  192.168.2.12 CCM_POST /ccm_system/request - 443 - 192.168.2.62 ccmhttp - 200 0 0 542 31

Once the message is received successfully on the management point, the MP_Relay component processes this message, converts the
message into an SMX file, and moves the SMX file to the appropriate location depending on whether the management point is colocated
on the site server or not.

      On a remote management point: \SMS\mp\outboxes\StateMsg.box
      On a management point colocated on the site server: \inboxes\auth\StateSys.box\incoming

In MP_Relay.log on a management point co-located on the site server:

  Mp Message Handler: start message processing for Relay----------------------- MP_RelayEndpoint
  Mp Message Handler: FileType=SMX MP_RelayEndpoint
  Message Body : <XML Body Truncated> MP_RelayEndpoint
  Relay: Outbox dir: E:\ConfigMgr\inboxes\auth\statesys.box\incoming MP_RelayEndpoint
  Priority in the message = 5 MP_RelayEndpoint

<!-- p.745 -->

  State Priority Directory = E:\ConfigMgr\inboxes\auth\statesys.box\incoming MP_RelayEndpoint
  Inv-Relay: Task completed successfully MP_RelayEndpoint

In MP_Relay.log on a remote management point:

  Mp Message Handler: start message processing for Relay------------------------------ MP_RelayEndpoint
  Mp Message Handler: FileType=SMX MP_RelayEndpoint
  Message Body :
  <?xml version="1.0" encoding="UTF-16"?>
  <Report><ReportHeader><Identification><Machine><ClientInstalled>1</ClientInstalled><ClientType>1</ClientType>
  <ClientID>GUID: 00001111-aaaa-2222-bbbb-3333cccc4444</ClientID><ClientVersion>5.00.7958.1000</ClientVersion>
  <NetBIOSName>PS1WIN7X64</NetBIOSName><CodePage>437</CodePage><SystemDefaultLCID>1033</SystemDefaultLCID>
  <Priority>5</Priority></Machine></Identification><ReportDetails><ReportContent>State Message Data</ReportContent>
  <ReportType>Full</ReportType><Date>20140120194656.903000+000</Date><Version>1.0</Version><Format>1.0</Format>
  </ReportDetails></ReportHeader><ReportBody><StateMessage MessageTime="20140120171855.573000+000"
  SerialNumber="232"><Topic ID="00001111-aaaa-2222-bbbb-3333cccc4444" Type="500" IDType="3" User="" UserSID=""/><State
  ID="2" Criticality="0"/><UserParameters Flags="0" Count="1"><Param>200</Param></UserParameters></StateMessage>
  </ReportBody></Report> MP_RelayEndpoint
  Inv-Relay Task: Processing message body MP_RelayEndpoint
  Relay: Outbox dir: C:\SMS\mp\outboxes\StateMsg.box MP_RelayEndpoint
  Priority in the message = 5 MP_RelayEndpoint
  State Priority Directory = C:\SMS\mp\outboxes\StateMsg.box MP_RelayEndpoint
  Inv-Relay: Task completed successfully MP_RelayEndpoint

The XML body looks identical to what's logged in StateMessage.log on the client.

Step 4: MP File Dispatch Manager sends the SMX file to the site server (only
when the management point isn't colocated on-site server)
When the management point is remote to the site server, after the file arrives in outboxes\StateMsg.box, MP File Dispatch Manager
(MPFDM) is responsible for moving these files to the StateMsg.box inbox on the site server. When the management point is colocated on
the site server, these files are moved directly to the appropriate Inbox folder, so MPFDM isn't involved.

In MPFDM.log on a remote management point:

  Moved file C:\SMS\MP\OUTBOXES\statemsg.box\TAZGYTSJ.SMX to
  \\PS1SITE.CONTOSO.COM\SMS_PS1\inboxes\auth\statesys.box\incoming\TAZGYTSJ.SMX SMS_MP_FILE_DISPATCH_MANAGER

For MPFDM to move the files to the appropriate inbox, the remote management point must be able to access the registry of the site server
to determine the Inbox source locations. Therefore, the Remote Registry service must be running, and Registry Access should not be
blocked by Group Policy. MPFDM determines the Inbox locations by accessing the following registry key on the site server:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Inbox Source

Step 5: StateSys component on the site server processes the state message to
the database
After the file arrives in \inboxes\auth\StateSys.box on the site server, the State System Manager (StateSys) component wakes up and
processes the SMX file(s).

In StateSys.log with verbose logging enabled:

  Inbox notification triggered, pause for 10 seconds...... SMS_STATE_SYSTEM
  Found new state messages to process, starting processing thread SMS_STATE_SYSTEM
  Thread "State Message Processing Thread #0" id:4316 started SMS_STATE_SYSTEM

<!-- p.746 -->

  total chucks loaded (1) SMS_STATE_SYSTEM
  CMessageProcessor - Processing file: YCE2H3VD.SMX SMS_STATE_SYSTEM
  CMessageProcessor - Processed 1 records with 0 invalid records. SMS_STATE_SYSTEM
  CMessageProcessor - Processed 1 message files in this batch, with 0 bad files. SMS_STATE_SYSTEM
  total chucks loaded (0) SMS_STATE_SYSTEM
  Thread "State Message Processing Thread #0" id:4316 terminated normally SMS_STATE_SYSTEM

In StateSys.log without verbose logging enabled:

  Found new state messages to process, starting processing thread SMS_STATE_SYSTEM
  Thread "State Message Processing Thread #0" id:1988 started SMS_STATE_SYSTEM
  total chucks loaded (1) SMS_STATE_SYSTEM
  total chucks loaded (0) SMS_STATE_SYSTEM
  Thread "State Message Processing Thread #0" id:1988 terminated normally SMS_STATE_SYSTEM

The StateSys.log file doesn't log the file name unless verbose logging is enabled for State System Manager.

The SMX file that's moved to the StateSys.box folder contains the message body XML. When StateSys processes this file, it calls the
spProcessStateReport stored procedure and passes this XML body on to the stored procedure as a parameter.

In SQL Server Profiler trace:

  exec dbo.spProcessStateReport N'<?xml version="1.0" encoding="UTF-16"?>
  <Report><ReportHeader><Identification><Machine><ClientInstalled>1</ClientInstalled><ClientType>1</ClientType>
  <ClientID>GUID: 00001111-aaaa-2222-bbbb-3333cccc4444</ClientID><ClientVersion>5.00.7958.1000</ClientVersion>
  <NetBIOSName>PS1WIN7X64</NetBIOSName><CodePage>437</CodePage><SystemDefaultLCID>1033</SystemDefaultLCID>
  <Priority>5</Priority></Machine></Identification><ReportDetails><ReportContent>State Message Data</ReportContent>
  <ReportType>Full</ReportType><Date>20140120220131.071000+000</Date><Version>1.0</Version><Format>1.0</Format>
  </ReportDetails></ReportHeader><ReportBody><StateMessage MessageTime="20140120171855.573000+000"
  SerialNumber="239"><Topic ID="00001111-aaaa-2222-bbbb-3333cccc4444" Type="500" IDType="3" User="" UserSID=""/><State
  ID="2" Criticality="0"/><UserParameters Flags="0" Count="1"><Param>200</Param></UserParameters></StateMessage>
  </ReportBody></Report>'

spProcessStateReport is a CLR stored procedure, and the CLR definition has the logic to determine the type of state message being

processed. Depending on the type of state message, it processes the state message appropriately and inserts the data in the database.

You can find friendly names of all state message Topic Types and IDs by querying the SR_StateNames table with the following command:

 SQL

 SELECT * FROM SR_StateNames

Software update summarization
Before software update compliance data can be presented in the console or reports, the software update compliance data must be
summarized. This is necessary because the console and reports usually display only summarized data. The State System component on the
site server performs the software update summarization along with summarization for other components, such as applications, DCM
deployments and client health. You can find information about all the summarization tasks that State System performs by querying the
vSR_SummaryTasks view in the Configuration Manager database. State System runs these tasks on a configured schedule and logs detail

about each task in StateSys.log:

  Started task '<TaskName>' SMS_STATE_SYSTEM
  Task '<TaskName>' completed successfully after running for 15 seconds, with status 8. SMS_STATE_SYSTEM

<!-- p.747 -->

For most of these tasks, the status logged by StateSys.log isn't an error code. Instead, it's the number of rows returned by the appropriate
SQL Server stored procedure that performs the summarization.

Summarization tasks specific to software updates are:

      SUM Assignment Compliance Evaluator

      Summarizes state messages for all software update group assignments (deployments). This task runs every hour by default. It can be
      initiated manually for a specific deployment in Configuration Manager console > Monitoring > Deployments, right-click the
      deployment, and then click Run Summarization.

      SUM Update Group Status Summarizer

      Summarizes status of Update Groups. This task runs every hour by default. It can be initiated manually for a specific Update Group in
      Configuration Manager console > Software Library > Software Updates > Software Update Groups, right-click the update group,
      and then click Run Summarization.

      You can also change the schedule of this task by right-clicking Software Update Groups or by selecting Schedule Summarization in
      the ribbon.

      SUM Update Status Summarizer

      Summarizes status of updates for all clients. This task runs every hour by default. It can be initiated manually in Configuration
      Manager console > Software Library > Software Updates, then click Run Summarization. You can also change the default schedule
      by selecting Schedule Summarization.

      SUM Migrate Update Status

      Migrates update status internally within the database. This task runs every 24 hours by default. It can't be initiated manually from the
      Configuration Manager console.

      SUM Delete Aged Status

      Deletes aged status from software update specific tables in the database. This task runs every 24 hours by default. It can't be initiated
      manually from the Configuration Manager console.

Software update point switching
In System Center 2012 Configuration Manager SP1 and later versions, a site can have multiple SUPs. This provides fault tolerance for
situations when a SUP becomes unavailable. For more information about SUPs' failover and switching, see the following articles:

      Software Update Points in Configuration Manager Service Pack 1
      Software update point switching

 Last updated on 02/04/2026

<!-- p.748 -->

Track the software update deployment
process in Configuration Manager
This article describes how to track the deployment of software updates in Configuration
Manager by using log files.

Original product version: Microsoft System Center 2012 Configuration Manager, Microsoft
System Center 2012 R2 Configuration Manager
Original KB number: 3090265

Summary
When you deploy software updates in Configuration Manager, you typically add the updates to
a software update group and then deploy the software update group to clients. When you
create the deployment, the update policy is sent to client computers. And the update content
files are downloaded from a distribution point to the local cache on the client computer. The
updates are then available for installation on the client. In the following section, we examine
this process in detail and show how the process can be tracked by using log files. This
information may be helpful when you're trying to identify and resolve problems in the software
update process.

For more information about software updates in Configuration Manager, see Software updates
introduction.

  ７ Note

  The log snippets provided in this article apply to Configuration Manager 2012 and 2012
  R2. Log entries for other Configuration Manager versions may be different.

Create a software update group
When you create a software update group in the Configuration Manager console, an instance
of the SMS_AuthorizationList class is created. This instance contains information about the
software update group, and it has relationships with the software updates in the software
update group.

<!-- p.749 -->

The following are logged in SMSProv.log:

 Output

 CSspClassManager::PreCallAction, dbname=CM_PS1    SMS Provider
 PutInstanceAsync SMS_AuthorizationList       SMS Provider
 CExtProviderClassObject::DoPutInstanceInstance    SMS Provider
 Updating SDM content definition.   SMS Provider
 Try to sync permission table : Declare @Ids RBAC_Object_Type;insert into @Ids
 (ObjectKey, ObjectTypeID) values (N'ScopeId_FC8FCC38-4BB1-4245-92F5-
 9CE841775019/AuthList_9D013E6D-EF76-43F6-ACC4-80749AB8D90A',34);exec
 spRBAC_SyncPermissions @ObjectIds=@Ids,@RoleIDs=N'',@AdminIDs=N''     SMS Provider
 Successfully synced permission table              SMS Provider
 Auditing: User CONTOSO\Admin created an instance of class SMS_AuthorizationList.
 SMS Provider

As part of the software update group creation process, SMSProv inserts data in appropriate CI_
tables, including:

     CI_ConfigurationItems
     CI_ConfigurationItemRelations
     CI_ConfigurationItemRElations_Flat
     CI_DocumentStore
     CI_CIDocuments
     CI_LocalizedProperties

SMSDBMON monitors when data is inserted into these tables and drops CI Notification (CIN)
files in objmgr.box. The following are logged in SMSDBMon.log:

 Output

 RCV: INSERT on CI_ConfigurationItems for CINotify_iud [16777264 ][60216]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: UPDATE on CI_ConfigurationItems for CINotify_iud [16777264 ][60217]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on CI_ConfigurationItemRelations_Flat for
 CI_ConfigurationItemRelations_Flat_From_iud [16777264 ][60218]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on CI_ConfigurationItemRelations_Flat for
 CI_ConfigurationItemRelations_Flat_From_iud [16777264 ][60219]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on CI_ConfigurationItemRelations_Flat for
 CI_ConfigurationItemRelations_Flat_From_iud [16777264 ][60220]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on CI_ConfigurationItemRelations_Flat for
 CI_ConfigurationItemRelations_Flat_From_iud [16777264 ][60221]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on CI_ConfigurationItemRelations_Flat for

<!-- p.750 -->

 CI_ConfigurationItemRelations_Flat_From_iud [16777264 ][60222]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on CI_ConfigurationItemRelations_Flat for
 CI_ConfigurationItemRelations_Flat_From_iud [16777264 ][60223]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: UPDATE on CI_ConfigurationItems for CINotify_iud [16777264 ][60224]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: UPDATE on CI_ConfigurationItems for CINotify_iud [16777264 ][60225]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on RBAC_ChangeNotification for Rbac_Sync_ChangeNotification [363 ]
 [60226] SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\objmgr.box\16777264.CIN [60225]
 SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\hman.box\363.RBC [60226]
 SMS_DATABASE_NOTIFICATION_MONITOR

Object Replication Manager wakes up when files are dropped in objmgr.box and processes the
software update group. The following are logged in ObjReplMgr.log:

 Output

 File notification triggered.      SMS_OBJECT_REPLICATION_MANAGER
 +++Begin processing changed CIN objects      SMS_OBJECT_REPLICATION_MANAGER
 ***** Processing AuthorizationList ScopeId_FC8FCC38-4BB1-4245-92F5-
 9CE841775019/AuthList_9D013E6D-EF76-43F6-ACC4- 80749AB8D90A *****
 SMS_OBJECT_REPLICATION_MANAGER
 Deleting notification file E:\ConfigMgr\inboxes\objmgr.box\16777264.CIN
 SMS_OBJECT_REPLICATION_MANAGER
 +++Begin collecting targeting information for Affected CIs
 SMS_OBJECT_REPLICATION_MANAGER
 +++Completed collecting targeting information for Affected CIs
 SMS_OBJECT_REPLICATION_MANAGER
 Affected CIs (1): 16777264            SMS_OBJECT_REPLICATION_MANAGER
 CI 16777264 is NOT Targeted         SMS_OBJECT_REPLICATION_MANAGER
 Successfully processed AuthorizationList ScopeId_FC8FCC38-4BB1-4245-92F5-
 9CE841775019/AuthList_9D013E6D-EF76-43F6-ACC4-80749AB8D90A
 SMS_OBJECT_REPLICATION_MANAGER
 Set last row version for Configuration Item to 0x0000000000296047
 SMS_OBJECT_REPLICATION_MANAGER

The changes to the CI_* tables are then replicated to the child sites through database
replication. This operation allows the software update group to show up on the child site.

Software update groups are configuration items (CIs) themselves, and the CI Type ID for
software update groups is 9. You can view the software update groups by running the
following SQL query:

 SQL

<!-- p.751 -->

 SELECT * FROM vSMS_ConfigurationItems WHERE CIType_ID = 9

To see the relationships from a software update group CI to the software update CIs, run the
following SQL query:

 SQL

 SELECT CIR.* FROM CI_ConfigurationItemRelations CIR
 JOIN CI_ConfigurationItems CI ON CIR.FromCI_ID = CI.CI_ID
 WHERE CI.CIType_ID = 9

Manually create a deployment for software update
group
When a deployment for a software update group is created, an instance of the
SMS_UpdateGroupAssignment class is created. The instance contains information about the

deployment. The following are logged in SMSProv.log:

 Output

 PutInstanceAsync SMS_UpdateGroupAssignment       SMS Provider
 CExtProviderClassObject::DoPutInstanceInstance        SMS Provider
 Auditing: User CONTOSO\Admin created an instance of class
 SMS_UpdateGroupAssignment.    SMS Provider

Updates are then downloaded to the specified package source directory by the Software
Updates Patch Downloader component. The following are logged in PatchDownloader.log in
%TEMP% directory:

 Output

 Trying to connect to the root\SMS namespace on the PS1SITE.CONTOSO.COM machine.
 Software Updates Patch Downloader
 Connected to \\PS1SITE.CONTOSO.COM\root\SMS       Software Updates Patch Downloader
 Trying to connect to the \\\PS1SITE.CONTOSO.COM\root\sms\site_PS1 namespace on the
 PS1SITE.CONTOSO.COM machine.      Software Updates Patch Downloader
 Connected to \\PS1SITE.CONTOSO.COM\root\sms\site_PS1      Software Updates Patch
 Downloader
 Download destination = \\PS1SITE\SOURCE\Updates\Win7\d09e9a92-20e7-455a-a51b-
 aaeca7b7d7e1.1\windows6.1-kb2807986-x86.cab .        Software Updates Patch
 Downloader
 Contentsource =
 http://wsus.ds.download.windowsupdate.com/msdownload/update/software/secu/2013/02/w
 indows6.1-kb2807986-x86_83d5bb38d8c50d924f3dcd024b20fe33afbd9d14.cab.       Software
 Updates Patch Downloader

<!-- p.752 -->

 Downloading content for ContentID = 471, FileName = windows6.1-kb2807986-x86.cab.
 Software Updates Patch Downloader
 Download
 http://wsus.ds.download.windowsupdate.com/msdownload/update/software/secu/2013/02/w
 indows6.1-kb2807986-x86_83d5bb38d8c50d924f3dcd024b20fe33afbd9d14.cab to
 C:\Users\Admin\AppData\Local\Temp\2\CABBA79.tmp returns 0       Software Updates
 Patch Downloader
 Successfully moved C:\Users\Admin\AppData\Local\Temp\2\CABBA79.tmp to
 \\PS1SITE\SOURCE\Updates\Win7\d09e9a92-20e7- 455a-a51b-aaeca7b7d7e1.1\windows6.1-
 kb2807986-x86.cab        Software Updates Patch Downloader
 Renaming \\PS1SITE\SOURCE\Updates\Win7\d09e9a92-20e7-455a-a51b-aaeca7b7d7e1.1 to
 \\\PS1SITE\SOURCE\Updates\Win7\d09e9a92-20e7-455a-a51b-aaeca7b7d7e1      Software
 Updates Patch Downloader
 Successfully moved \\PS1SITE\SOURCE\Updates\Win7\d09e9a92-20e7-455a-a51b-
 aaeca7b7d7e1.1 to \\PS1SITE\SOURCE\Updates\Win7\d09e9a92-20e7-455a-a51b-
 aaeca7b7d7e1      Software Updates Patch Downloader

After the updates are downloaded, SMS Provider adds each update to the specified package.
The following are logged in SMSProv.log:

 Output

 Requested class =SMS_SoftwareUpdatesPackage      SMS Provider
 Requested num keys =1    SMS Provider
 CExtProviderClassObject::DoExecuteMethod AddUpdateContent       SMS Provider
 *** SspPackageInst::AddUpdateContent ***     SMS Provider
 CObjectLock::UserHasLock: ********** User CONTOSO\Admin has lock for object
 SMS_SoftwareUpdatesPackage.PackageID="PS100001" with LockID: DCE6F1B5-1EE8-47CB-
 85A7-3027E51119A7 **********      SMS Provider
 CObjectLock::ReleaseLock: ********** User CONTOSO\Admin has released lock for
 object SMS_SoftwareUpdatesPackage.PackageID="PS100001" with LockID: DCE6F1B5-1EE8-
 47CB-85A7-3027E51119A7 **********      SMS Provider
 SspPackageInst::AddContent() called for these ContentIDs - {471}       SMS Provider
 SspPackageInst::AddContent() called with these CIContentSourcePath -
 {"\\PS1SITE\SOURCE\Updates\Win7"}     SMS Provider
 RefreshDPs value is FALSE. DP(s) will not be updated at the end of the operation
 SMS Provider
 These Contents will be added to Software Updates Package - PS100001 with
 PackageSource - \\PS1SITE\SOURCE\Updates\Win7      SMS Provider
 Adding Content with ID 471, UniqueID d09e9a92-20e7-455a-a51b-aaeca7b7d7e1 and
 ContentSource \\PS1SITE\SOURCE\Updates\Win7 to the Package       SMS Provider
 ContentFileName = windows6.1-kb2807986-x86.cab, SourceURL =
 http://wsus.ds.download.windowsupdate.com/msdownload/update/software/secu/2013/02/w
 indows6.1-kb2807986- x86_83d5bb38d8c50d924f3dcd024b20fe33afbd9d14.cab, ImportPath =
 , ContentFileHash = SHA1:83D5BB38D8C50D924F3DCD024B20FE33AFBD9D14         SMS Provider
 File Source = \\PS1SITE\SOURCE\Updates\Win7\d09e9a92-20e7-455a-a51b-
 aaeca7b7d7e1\windows6.1-kb2807986-x86.cab      SMS Provider
 File Destination = \\PS1SITE\SOURCE\Updates\Win7\d09e9a92-20e7-455a-a51b-
 aaeca7b7d7e1     SMS Provider
 CExtUserContext::LeaveThread : Releasing IWbemContextPtr=57376560         SMS Provider

<!-- p.753 -->

After all the updates are added to the package, SMS Provider updates the package and logs
the following entries:

 Output

 CExtUserContext::EnterThread : User=CONTOSO\Admin
 Sid=0x01050000000000051500000068830AA65AAB72A155BCE9324F040000 Caching
 IWbemContextPtr=00000000036B7E50 in
 Process 0xc68 (3176)    SMS Provider
 Context: SMSAppName=Configuration Manager Administrator console      SMS Provider
 Context: MachineName=PS1SITE.CONTOSO.COM     SMS Provider
 Context: UserName=CONTOSO\Admin     SMS Provider
 Context: ObjectLockContext=c00c315d-b15d-4b0e-9844-017205cc2443      SMS Provider
 Context: ApplicationName=Microsoft.ConfigurationManagement.exe      SMS Provider
 Context: ApplicationVersion=5.0.7958.1000      SMS Provider
 Context: LocaleID=MS\0x409    SMS Provider
 Context: __ProviderArchitecture=32       SMS Provider
 Context: __RequiredArchitecture=0 (Bool)       SMS Provider
 Context: __ClientPreferredLanguages=en-US,en      SMS Provider
 Context: __GroupOperationId=755382      SMS Provider
 Context: __WBEM_CLIENT_AUTHENTICATION_LEVEL=6       SMS Provider
 CExtUserContext : Set ThreadLocaleID OK to: 1033      SMS Provider
 CSspClassManager::PreCallAction, dbname=CM_PS1 SMS Provider
 ExecMethodAsync : SMS_SoftwareUpdatesPackage.PackageID="PS100001"::RefreshPkgSource
 SMS Provider
 Requested class =SMS_SoftwareUpdatesPackage      SMS Provider
 Requested num keys =1    SMS Provider
 CExtProviderClassObject::DoExecuteMethod RefreshPkgSource      SMS Provider
 Auditing: User CONTOSO\Admin called an audited method of an instance of class
 SMS_SoftwareUpdatesPackage.     SMS Provider
 CExtUserContext::LeaveThread : Releasing IWbemContextPtr=57376336      SMS Provider

When the update group assignment is created, SMS Provider inserts information about the
assignment in the CI_Assignments table. This triggers SMSDBMON, which notifies Object
Replication Manager to process the update group assignment by dropping a .CIA file in
objmgr.box. The following are logged in SMSDBMON.log:

 Output

 RCV: INSERT on CI_CIAssignments for CIAssignmentNotify_iu [16777222 ][60916]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on CrpChange_Notify for CrpChange_Notify_ins [14 ][60917]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: UPDATE on CI_CIAssignments for CIAssignmentNotify_iu [16777222 ][60920]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: UPDATE on CI_AssignmentTargetedCIs for CI_AssignmentTargetedCIs_CIAMGR
 [16777222 ][60921] SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: UPDATE on CI_CIAssignments for CIAssignmentNotify_iu [16777222 ][60923]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: UPDATE on CI_AssignmentTargetedCIs for CI_AssignmentTargetedCIs_CIAMGR

<!-- p.754 -->

 [16777222 ][60924] SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: UPDATE on CI_CIAssignments for CIAssignmentNotify_iu [16777222 ][60926]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: UPDATE on CI_AssignmentTargetedCIs for CI_AssignmentTargetedCIs_CIAMGR
 [16777222 ][60927] SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\objmgr.box\16777222.CIA [60916]
 SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\policypv.box\policytargeteval\14.CRP [60917]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on PolicyAssignmentChg_Notify for PolicyAssignmentChg_Notify_iu
 [16786995 ][60929] SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\policypv.box\policytargeteval\16786995.PAC
 [60929] SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on PkgNotification for PkgNotify_Add [PS100001 ][60930]
 SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\distmgr.box\PS100001.PKN [60930]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on PolicyAssignmentChg_Notify for PolicyAssignmentChg_Notify_iu
 [16786995 ][60931] SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: UPDATE on PolicyAssignmentChg_Notify for PolicyAssignmentChg_Notify_iu
 [16786995 ][60932] SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\policypv.box\policytargeteval\16786995.PAC
 [60931] SMS_DATABASE_NOTIFICATION_MONITOR

After Object Replication Manager detects the CIA file in objmgr.box, it processes the file and
creates the policy for the software update assignment. The following are logged in ObjMgr.log:

 Output

 File notification triggered.     SMS_OBJECT_REPLICATION_MANAGER
 +++Begin processing changed CIA objects     SMS_OBJECT_REPLICATION_MANAGER
 ***** Processing Update Group Assignment {aaaabbbb-0000-cccc-1111-dddd2222eeee}
 *****    SMS_OBJECT_REPLICATION_MANAGER
 Deleting notification file
 E:\ConfigMgr\inboxes\objmgr.box\16777222.CIA      SMS_OBJECT_REPLICATION_MANAGER
 CI Assignment {aaaabbbb-0000-cccc-1111-dddd2222eeee} has 3 Targeted
 CI(s)     SMS_OBJECT_REPLICATION_MANAGER
 PolicyID {aaaabbbb-0000-cccc-1111-dddd2222eeee} PolicyVersion 1.00 PolicyHash
 SHA256:63BAFA808F969849B40B2B727B49BC5093B965782716DDE3490528681CF27ACC
   SMS_OBJECT_REPLICATION_MANAGER
 Notifying policy provider about changes in policy
 content/targeting     SMS_OBJECT_REPLICATION_MANAGER
 Successfully created policy for CI Assignment {aaaabbbb-0000-cccc-1111-
 dddd2222eeee}     SMS_OBJECT_REPLICATION_MANAGER
 Notifying policy provider about changes in policy
 content/targeting     SMS_OBJECT_REPLICATION_MANAGER
 Successfully updated Policy Targeting for CI Assignment {aaaabbbb-0000-cccc-1111-
 dddd2222eeee}    SMS_OBJECT_REPLICATION_MANAGER
 No file trigger for E:\ConfigMgr\inboxes\objmgr.box\16777222.CIV - status
 2     SMS_OBJECT_REPLICATION_MANAGER
 Assigned CIs: [ 16777264 ]     SMS_OBJECT_REPLICATION_MANAGER
 Begin processing Assigned CI: [16777264]     SMS_OBJECT_REPLICATION_MANAGER
 Creating VersionInfo policy for CI 16777264     SMS_OBJECT_REPLICATION_MANAGER

<!-- p.755 -->

 Creating VersionInfo policy ScopeId_FC8FCC38-4BB1-4245-92F5-
 9CE841775019/AuthList_9D013E6D-EF76-43F6-ACC4-
 80749AB8D90A/VI     SMS_OBJECT_REPLICATION_MANAGER
 16777264 Referenced CIs: [ 929 930 1041 1042 1132 1133
 ]     SMS_OBJECT_REPLICATION_MANAGER
 VersionInfo policy for CI 16777264 is Machine type
     SMS_OBJECT_REPLICATION_MANAGER
 PolicyID ScopeId_FC8FCC38-4BB1-4245-92F5-9CE841775019/AuthList_9D013E6D-EF76-43F6-
 ACC4-80749AB8D90A/VI PolicyVersion 1.00 PolicyHash
 SHA256:6EFE96F3D67773CA965EC67EC60B602FC78242509A096FCF44C2D5FDD5B2FC76
   SMS_OBJECT_REPLICATION_MANAGER
 Notifying policy provider about changes in policy
 content/targeting     SMS_OBJECT_REPLICATION_MANAGER
 Updated dependent policy references to CIA {aaaabbbb-0000-cccc-1111-dddd2222eeee}
     SMS_OBJECT_REPLICATION_MANAGER
 STATMSG: ID=5800 SEV=I LEV=M SOURCE="SMS Server"
 COMP="SMS_OBJECT_REPLICATION_MANAGER" SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5404
 TID=3380 GMTDATE=Thu Jan 23 20:31:38.889 2014 ISTR0="Microsoft Software Updates -
 2014-01-23 03:30:52 PM" ISTR1="" ISTR2="" ISTR3="" ISTR4="" ISTR5="" ISTR6=""
 ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=414 AVAL0="{aaaabbbb-0000-cccc-1111-
 dddd2222eeee}"     SMS_OBJECT_REPLICATION_MANAGER
 Successfully updated CRCs for CI Assignment {aaaabbbb-0000-cccc-1111-dddd2222eeee}
      SMS_OBJECT_REPLICATION_MANAGER
 Successfully processed Update Group Assignment {aaaabbbb-0000-cccc-1111-
 dddd2222eeee}      SMS_OBJECT_REPLICATION_MANAGER
 Set last row version for CI Assignment to
 0x0000000000296628               SMS_OBJECT_REPLICATION_MANAGER

After being notified by the Object Replication Manager, Policy Provider updates the policy for
the clients. The following are logged in PolicyPv.log:

 Output

 File notification triggered.    SMS_POLICY_PROVIDER
 Found 14.CRP    SMS_POLICY_PROVIDER
 Adding to delete list:
 E:\ConfigMgr\inboxes\policypv.box\policytargeteval\14.CRP     SMS_POLICY_PROVIDER
 Processing any pending PolicyAssignmentChg_Notify    SMS_POLICY_PROVIDER
 Updating ResPolicyMap    SMS_POLICY_PROVIDER
 Policy or Policy Target Change Event triggered.     SMS_POLICY_PROVIDER
 File notification triggered.    SMS_POLICY_PROVIDER
 Building Collection Change List from Collection Member Notification
 files    SMS_POLICY_PROVIDER

 --Handle PolicyAssignment Resigning    SMS_POLICY_PROVIDER
 Completed batch with beginning PADBID = 16786995 ending PADBID =
 16786996.    SMS_POLICY_PROVIDER

 --Process Policy Changes    SMS_POLICY_PROVIDER
 Found some Policy changes, returning New
 LastRowversion=0x000000000029662B    SMS_POLICY_PROVIDER
 Processing Updated Policies    SMS_POLICY_PROVIDER
 Building Collection Change List from New and Targeting Changed

<!-- p.756 -->

 Policies      SMS_POLICY_PROVIDER

 --Update Policy Targeting Map    SMS_POLICY_PROVIDER
 **** Evaluating Collection 14 for targeting changes ****    SMS_POLICY_PROVIDER
 Advanced client policy changes detected for collection 14, ** 5 Added & 0 Deleted
 ***.     SMS_POLICY_PROVIDER

 --Process Policy Targeting Map    SMS_POLICY_PROVIDER
 **** Process notification table to update resultant targeting table
 ****    SMS_POLICY_PROVIDER

SQL Server Profiler covering the entire process displays the following entries:

 Output

 insert into CI_CIAssignments (AssignmentAction, Description, AssignmentName,
 DesiredConfigType, DisableMomAlerts, DPLocality, AssignmentEnabled,
 EnforcementDeadline, EvaluationSchedule, ExpirationTime,
 LimitStateMessageVerbosity, LogComplianceToWinEvent, NonComplianceCriticality,
 NotifyUser, OverrideServiceWindows, PersistOnWriteFilterDevices,
 RaiseMomAlertsOnFailure, RandomizationEnabled, RebootOutsideOfServiceWindows,
 SendDetailedNonComplianceStatus, StartTime, StateMessagePriority,
 StateMessageVerbosity, SuppressReboot, UseBranchCache, UseGMTTimes,
 UserUIExperience, WoLEnabled, TargetCollectionID, LocaleID, Assignment_UniqueID,
 SourceSite, LastModifiedBy, AssignmentType, CreationTime, LastModificationTime,
 IsTombstoned) values (2, N'', N'Microsoft Software Updates - 2014-01-23 03:30:52
 PM', 1, 0, 16, 1,
 '01/30/2014 15:30:00', null, null, 1, 0, null, 1, 0, 1, 0, null, 0, 0, '01/23/2014
 15:31:00', 5, 5, 0, 1, 0, 1, 0, 14, 1033, N'{3ACE84D4-7B2A-
 4D86-81AF-07E2AC255745}', N'PS1', N'CONTOSO\Admin', 5, '01/23/2014 20:31:31',
 '01/23/2014 20:31:31', 0)

 insert into CI_AssignmentTargetedGroups (CI_ID, AssignmentID) values (16777264,
 16777222)

 insert into CI_ContentPackages (Content_ID, ContentSubFolder, ContentVersion,
 Content_UniqueID, MinPackageVersion,PkgID) VALUES ('471', N'd09e9a92-20e7-455a-
 a51b-aaeca7b7d7e1', '1', N'd09e9a92-20e7-455a-a51b-aaeca7b7d7e1', '0', N'PS100001')

 insert Policy(Version, PolicyHash, PolicyFlags, PolicyPriority, DeviceVersion,
 PolicyID)
 values(N'1.00',
 N'SHA256:63BAFA808F969849B40B2B727B49BC5093B965782716DDE3490528681CF27ACC', 16592,
 25, N'''', N'{aaaabbbb-0000-cccc-1111-dddd2222eeee}')

 insert PolicyAssignment(PolicyAssignmentID, PADBID, Version, PolicyID,
 IsTombstoned, LastUpdateTime)
 values(N'{8d9ba949-d038-4c09-a0cc-af3f07c39d71}', 16786995, N'1.00', N'{aaaabbbb-
 0000-cccc-1111-dddd2222eeee}', 0,
 GetUTCDate())

 DECLARE @AssignedCIs TABLE(CI_ID INT)
 BEGIN

<!-- p.757 -->

 INSERT INTO @AssignedCIs
 SELECT DISTINCT ATG.CI_ID FROM CI_AssignmentTargetedGroups ATG
 INNER JOIN vCI_CIAssignments CIA ON CIA.AssignmentID = ATG.AssignmentID
 WHERE CIA.Assignment_UniqueID = '{aaaabbbb-0000-cccc-1111-dddd2222eeee}'
 IF @@ROWCOUNT = 0
 BEGIN
 INSERT INTO @AssignedCIs
 SELECT DISTINCT ATCI.CI_ID FROM vCI_AssignmentTargetedCIs_Actual ATCI
 INNER JOIN vCI_CIAssignments CIA ON CIA.AssignmentID = ATCI.AssignmentID
 WHERE CIA.Assignment_UniqueID = '{aaaabbbb-0000-cccc-1111-dddd2222eeee}'
 END
 END
 SELECT DISTINCT CI_ID FROM @AssignedCIs

 insert Policy(Version, PolicyHash, PolicyFlags, PolicyPriority, DeviceVersion,
 PolicyID)
 values(N'1.00',
 N'SHA256:6EFE96F3D67773CA965EC67EC60B602FC78242509A096FCF44C2D5FDD5B2FC76', 208,
 25, N'''', N'ScopeId_FC8FCC38-4BB1-4245-92F5-9CE841775019/AuthList_9D013E6D-EF76-
 43F6-ACC4-80749AB8D90A/VI')

 UPDATE Policy SET DeviceBody = NULL where PolicyID='ScopeId_FC8FCC38-4BB1-4245-
 92F5-9CE841775019/AuthList_9D013E6D- EF76-43F6-ACC4-80749AB8D90A/VI'

 insert PolicyAssignment(PolicyAssignmentID, PADBID, Version, PolicyID,
 IsTombstoned, LastUpdateTime) values(N'{64ed94a2-ff08-42a7-9e42-b292409c79e8}',
 16786996, N'1.00', N'ScopeId_FC8FCC38-4BB1-4245-92F5-
 9CE841775019/AuthList_9D013E6D-EF76-43F6-ACC4-80749AB8D90A/VI', 0, GetUTCDate())

 insert CI_AssignmentCRCs (AssignmentID, AssignmentCRC, PolicyCRC, ComplianceCRC)
 values (16777222, N'7a2e8acd', N'c10ba7c5', N'5aeb49f4')

 insert into CI_ContentPackages (Content_ID, ContentSubFolder, ContentVersion,
 Content_UniqueID, MinPackageVersion,PkgID) VALUES ('534', N'de62f3b3-615b-4800-
 b6ba-51d7c826dd08', '1', N'de62f3b3-615b-4800-b6ba-51d7c826dd08', '0', N'PS100001')

Create a deployment by using an automatic
deployment rule
Automatic deployment rule (ADR) execution is triggered manually, per a schedule or after
software update synchronization is completed. The Rule Engine component evaluates the rule.
If any software updates match the defined criteria, the Rule Engine will:

     download the updates
     create a software update group
     create a software update group assignment

The following example shows the process of software update group and deployment creation:

<!-- p.758 -->

RuleEngine.log shows beginning of rule processing:

  Output

  Found notification file E:\ConfigMgr\inboxes\RuleEngine.box\1.RUL   SMS_RULE_ENGINE
  RuleSchedulerThred: Change in Rules Object Signalled.   SMS_RULE_ENGINE
  Constructing Rule 1 using Auto Deployment Rule Factory SMS_RULE_ENGINE
  Populating Rule Skeleton            SMS_RULE_ENGINE
  Populating Criterion Skeleton       SMS_RULE_ENGINE
  Populating Action Skeleton          SMS_RULE_ENGINE
  Populating Action Skeleton          SMS_RULE_ENGINE
  CRuleHandler: Need to Process 1 rules           SMS_RULE_ENGINE

RuleEngine.log shows rule processing and query to run to find updates that match the defined
criteria:

  Output

  CRuleHandler: Processing Rule with ID:1, Name:ADR_Test.     SMS_RULE_ENGINE
  Evaluating Update Criteria for AutoDeployment Rule 1     SMS_RULE_ENGINE
  Evaluating Update Criteria...    SMS_RULE_ENGINE
  Rule Criteria is: <UpdateXML xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema" Name="SMS_SoftwareUpdate"
  LocaleId="1033"><UpdateXMLDescriptionItems><UpdateXMLDescriptionItem
  PropertyName="_Product" UIPropertyName=""><MatchRules><string>'Product:a38c835c-
  2950-4e87-86cc- 6911a52c34a3'</string></MatchRules></UpdateXMLDescriptionItem>
  <UpdateXMLDescriptionItem PropertyName="IsSuperseded" UIPropertyName="">
  <MatchRules><string>false</string></MatchRules></UpdateXMLDescriptionItem>
  <UpdateXMLDescriptionIte m PropertyName="_UpdateClassification" UIPropertyName="">
  <MatchRules><string>'UpdateClassification:e0789628-ce08-4437- be74-
  2495b842f43b'</string></MatchRules></UpdateXMLDescriptionItem>
  </UpdateXMLDescriptionItems></UpdateXML>      SMS_RULE_ENGINE
  Inserting PropertyName:_Product, PropertyValue:'Product:a38c835c-2950-4e87-86cc-
  6911a52c34a3'      SMS_RULE_ENGINE
  Inserting PropertyName:IsSuperseded, PropertyValue:false      SMS_RULE_ENGINE
  Inserting PropertyName:_UpdateClassification,
  PropertyValue:'UpdateClassification:e0789628-ce08-4437-be74-2495b842f43b'
  SMS_RULE_ENGINE
  Query to run is: select CI_ID from dbo.fn_ListUpdateCIs(1033) ci~where IsExpired=0~
  and (IsSuperseded=0)~ and (CI_ID in (select CI_ID from v_CICategories_All where
  CategoryInstance_UniqueID in (N'Product:a38c835c-2950-4e87-86cc-6911a52c34a3')))~
  and (CI_ID in (select CI_ID from v_CICategories_All where CategoryInstance_UniqueID
  in (N'UpdateClassification:e0789628-ce08-4437- be74-2495b842f43b')))
  SMS_RULE_ENGINE
  Rule resulted in a total of 1 updates    SMS_RULE_ENGINE
  Evaluation Resultant XML is: <EvaluationResultXML
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"><DefinitionUpdates/><CI_IDs>
  <CI_ID>4514</CI_ID></CI_IDs></EvaluationResultXML>      SMS_RULE_ENGINE

Download is started for actionable updates:

<!-- p.759 -->

 Output

 Enforcing Content Download Action SMS_RULE_ENGINE
 Download Rule Action XML is: <ContentActionXML
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"><PackageID>CS100006</PackageID>
 <ContentLocales><Locale>Locale:9</Locale ><Locale>Locale:0</Locale>
 </ContentLocales><ContentSources><Source Name="Internet" Order="1"/><Source
 Name="WSUS" Order="2"/><Source Name="UNC" Order="3" Location=""/></ContentSources>
 </ContentActionXML>        SMS_RULE_ENGINE
 Criteria Filter Result XML is: <EvaluationResultXML
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema">
 <DefinitionUpdates/><CI_IDs><CI_ID>4514</CI_ID></CI_IDs> </EvaluationResultXML>
 SMS_RULE_ENGINE
 1 update(s) need to be downloaded in package "CS100006"
 (\\CS1SITE\SOURCE\Updates\EPDefinitions)    SMS_RULE_ENGINE
 List of update(s) which match the content rule criteria = {4514} SMS_RULE_ENGINE
 Downloading contents (count = 34) for UpdateID 4514              SMS_RULE_ENGINE
 List of update content(s) which match the content rule criteria =
 {737,738,739,740,741,742,2182,2183,2184,2185,2186,2187,2188,2189,3047,3048,3187,318
 8,3189,3190,3191,3192,3545,3546,3547 ,3548,3549,3550,3551,3552,3553,3554,3555,3556}
 SMS_RULE_ENGINE
 Contents 737 is already present in the package "CS100006". Skipping download.
 SMS_RULE_ENGINE
 Contents 738 is already present in the package "CS100006". Skipping download.    S
 MS_RULE_ENGINE
 1 of 1 updates are downloaded and will be added to the Deployment. SMS_RULE_ENGINE

RuleEngine.log shows creation of update group and deployment:

 Output

 We need to create a new UpdateGroup/Deployment          SMS_RULE_ENGINE
 Associated Update Group: ScopeId_FC8FCC38-4BB1-4245-92F5-
 9CE841775019/AuthList_4d3480d5-de12-4864-b872-187479e2b381 with RBAC Scope SMS00UNA
 SMS_RULE_ENGINE

The following examples illustrate the update group creation process:

In SMSDBMON.log:

 Output

 RCV: INSERT on CI_ConfigurationItems for CINotify_iud [16777275 ][66146]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on CI_ConfigurationItemRelations_Flat for
 CI_ConfigurationItemRelations_Flat_From_iud [16777275 ][66148]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on CI_ConfigurationItemRelations_Flat for
 CI_ConfigurationItemRelations_Flat_From_iud [16777275 ][66149]

<!-- p.760 -->

 SMS_DATABASE_NOTIFICATION_MONITOR
 ...
 SND: Dropped E:\ConfigMgr\inboxes\objmgr.box\16777275.CIN [66148]
 SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\objmgr.box\16777275.CIN [66149]
 SMS_DATABASE_NOTIFICATION_MONITOR

In ObjReplMgr.log:

 Output

 File notification triggered.   SMS_OBJECT_REPLICATION_MANAGER
 ***** Processing AuthorizationList ScopeId_FC8FCC38-4BB1-4245-92F5-
 9CE841775019/AuthList_4d3480d5-de12-4864-b872-187479e2b381 *****
 SMS_OBJECT_REPLICATION_MANAGER
 Deleting notification file E:\ConfigMgr\inboxes\objmgr.box\16777275.CIN
 SMS_OBJECT_REPLICATION_MANAGER
 Added CI with CI_ID=4514 to the deployment       SMS_OBJECT_REPLICATION_MANAGER
 Created file trigger for E:\ConfigMgr\inboxes\objmgr.box\16777228.CIA
 SMS_OBJECT_REPLICATION_MANAGER
 Created file trigger for E:\ConfigMgr\inboxes\objmgr.box\16777228.CIV
 SMS_OBJECT_REPLICATION_MANAGER
 Successfully processed AuthorizationList ScopeId_FC8FCC38-4BB1-4245-92F5-
 9CE841775019/AuthList_4d3480d5-de12-4864-b872- 187479e2b381
 SMS_OBJECT_REPLICATION_MANAGER
 Set last row version for Configuration Item to 0x0000000000487EA9
 SMS_OBJECT_REPLICATION_MANAGER

The following example shows the deployment creation process:

In SMSDBMON.log:

 Output

 RCV: INSERT on CI_CIAssignments for CIAssignmentNotify_iu [16777228 ][66190]
 SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\objmgr.box\16777228.CIA [66190]
 SMS_DATABASE_NOTIFICATION_MONITOR

In ObjReplMgr.log:

 Output

 +++Begin processing changed CIA objects      SMS_OBJECT_REPLICATION_MANAGER
 ***** Processing Update Group Assignment {2ba787b6-4ee9-4b33-b0ff-8663d181c84d}
 *****    SMS_OBJECT_REPLICATION_MANAGER
 Deleting notification file E:\ConfigMgr\inboxes\objmgr.box\16777228.CIA
 SMS_OBJECT_REPLICATION_MANAGER
 CI Assignment {2ba787b6-4ee9-4b33-b0ff-8663d181c84d} has 1 Targeted CI(s)
 SMS_OBJECT_REPLICATION_MANAGER
