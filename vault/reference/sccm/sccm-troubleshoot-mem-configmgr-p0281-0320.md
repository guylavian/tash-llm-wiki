---
title: "Welcome — pages 281-320"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0281-0320
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0281-0320
family: sccm
documentKind: "doc"
abstract: "Check if reinit isn't finished for site replication SQL SELECT * FROM RCM_DrsInitializationTracking dt INNER JOIN ReplicationData rg ON dt.ReplicationGroup = rg.ReplicationGroup WHERE dt.InitializationStatus NOT IN (6,7) Get the TrackingGuid & Status from subscriber site SQL SEL"
---

# Welcome — pages 281-320

<!-- p.281 -->

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

<!-- p.282 -->

  it.ReplicationGroup
  WHERE it.RequestTrackingGUID=@trackingGuid

Then use the InitializeData method on the SMS_ReplicationGroup WMI class with the
following values:

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

<!-- p.283 -->

Troubleshoot database replication service
issues in Configuration Manager
This guide helps administrators diagnose and resolve database replication service (DRS)
problems in Configuration Manager.

Original product version: Microsoft Endpoint Configuration Manager (current branch),
Microsoft System Center 2012 R2 Configuration Manager, Microsoft System Center 2012
Configuration Manager
Original KB number: 20033

When you experience a DRS problem in Configuration Manager, the beginning investigative
phase is the most critical point. Any type of change or fix should be made only after careful
study and understanding of the problem at hand.

Get started
Start by gathering information related to the history of the problem. Many times DRS problems
can ultimately be traced back to a recent change made in the environment. Keep in mind that
you should not focus solely on Configuration Manager, as changes to Windows or SQL Server
can cause DRS problems as well. Having a clear understanding of any recent changes in the
environment can provide important clues as to the source of the problem.

Once you've investigated environmental changes and made sure that your updates are in
order, the next step is to run the Replication Link Analyzer (RLA). To launch RLA, open the
Monitoring workspace and select the Database Replication node, then right-click the link that
is having a problem and select Replication Link Analyzer, as shown in the following example:

<!-- p.284 -->

  ７ Note

  RLA runs within the context of whomever launches it from the console, so be sure that the
  account you use has administrative privileges on both SQL Server and site servers.

RLA will check the following on both sites:

     The SMS service is running.
     SMS Replication Configuration Monitor component is running.
     Ports required for SQL Server replication are enabled.
     SQL Server version is supported.
     Network is available between the two sites.
     There's enough space for the SQL Server database.
     SQL Server Broker service configuration exists.
     SQL Server Broker service certificate exists.
     Known errors in SQL Server log files.
     Whether the replication queues are disabled.
     Time is in sync.
     Is the transmission of data stuck?
     Does a key conflict exist?

If RLS finds known problems, it will offer to fix them for you. The RLA output report is also
straightforward. It tells you what it checked and what rules were run in addition to whether
they passed or failed. Here is an example:

<!-- p.285 -->

Get details with SPDiagDRS
If Replication Link Analyzer can't detect and resolve the problem, run SPDiagDRS and see if it
can offer any clues to what may be failing.

To run SPDiagDRS , open SQL Server Management Studio and connect to the two servers on
each side of the link having the problem. On each CM_xxx database, run the Exec SPDiagDRS
command.

The following is a breakdown of the various SPDiagDRS sections and some common places to
look for problems. A simple search for error messages and codes found here often guides you
to the source of the problem.

                                                                                           

<!-- p.286 -->

Section 1
     SiteStatus: This tells us whether the site is replicating or not. Anything other than ACTIVE
     is not good.

     CertificateThumbprint: The thumbprint of the certificate used for authentication that
     contains the site's public key (local DB trusts remote DB).

Section 2
     IncomingMessageInQueue: This tells us the incoming backlog that a site has. If the
     backlog is high due to the number of sites reporting to it, you may see the links going to
     a degraded or failed state because the heartbeat synchronizations are not processed in
     time.

     OutgoingMessageInQueue: This tells us the backlog that has yet to clear as we wait for
     the sites to receive the messages. This generally fluctuates, however if it continues to
     grow then this can represent a problem. Further troubleshooting should be performed to
     determine which site is not getting the messages.

Section 3
This is simply the detailed view of the Initialization Detail in the console.

<!-- p.287 -->

Section 4
This is the detailed view of Replication Detail in the console. It provides more information
about the flow between each replication group.

<!-- p.288 -->

Section 5
This section has some important and useful information about the sites we are connecting to.
In this example we are on primary site server 002, and 001 is the central administration site. If
we had a secondary site under 002, it would be shown here. On a central administration site, all
primary sites would be reflected but not the secondary sites.

Primary site 002 example:

Central administration site 001 example:

Section 6
This provides the general information of the sites in the hierarchy, the SiteServerName and
DBServer names, as well as the status and version. You can see here that a different primary

site (003) is showing as being in Maintenance Mode. On working systems, Section 6 should be
identical between the central administration site and all primary sites in the hierarchy.

<!-- p.289 -->

Section 7
The bottom two sections contain detailed information on the heartbeat or LastSentStatus for
each group as well as conversationIDs and so on, and the built-in replication options
configured for each group.

Check RCMCtrl.log for errors
Next you will want to check RCMCtrl.log on each site for errors, as this will often provide
valuable clues regarding the source of the problem. For example, you may find that replication
is in a Failed state for a site and that replication hasn't occurred for some time. In this scenario,
you may find that RCMCtrl.log contains entries similar to the following:

 Output

 7/4/2016 1:25:36 PM: ReplicationLinkAnalysis Information: 1 : Completed replication
 link analysis thread.
 7/4/2016 1:25:37 PM: ReplicationLinkAnalysis Error: 1 : Unable to find SiteCode or
 SiteNumber
 7/4/2016 1:25:37 PM: ReplicationLinkAnalysis Error: 1 :
 Microsoft.ConfigurationManager.ManagedBase.LocalServerDataNotFoundException: Unable
 to find SiteCode or SiteNumber
 at Microsoft.ConfigurationManager.ManagedBase.SiteData.Refresh()
 at
 Microsoft.ConfigurationManager.ReplicationLinkAnalyzer.ReplicationLinkAnalysisEngin
 e.Initialize()
 at
 Microsoft.ConfigurationManager.ReplicationLinkAnalyzer.ReplicationLinkAnalysisEngin
 e.RunRulesInBackground(Object sender, DoWorkEventArgs e)
 at System.ComponentModel.BackgroundWorker.WorkerThreadStart(Object argument)

If you see entries similar to these, make sure that the SMS Executive and the Site Component
Manager services are running on the site in question. If not, this may be why replication is in a
Failed state. If not running, start the SMS Executive and/or Site Component Manager services
manually and troubleshoot the services if they fail to start.

Another example of an error you might find in RCMCtrl.log is the following:

 Output

<!-- p.290 -->

  07/04/2016 12:33:34 PM 6352 (0x18D0)CSqlBCP::ReadRowCount: Can't open file
  [F:\Program Files\Microsoft Configuration
  Manager\inboxes\rcm.box\GUID\INSTALLED_EXECUTABLE_DATA.bcp.rowcount].
  SMS_REPLICATION_CONFIGURATION_MONITOR
  07/04/2016 12:33:34 PM 6352 (0x18D0) CSqlBCP::DRS_Init_BCPIN: ReadRowCount failed.
  SMS_REPLICATION_CONFIGURATION_MONITOR
  07/04/2016 12:33:34 PM 6352 (0x18D0)*** DRS_Init_BCPIN() failed
  SMS_REPLICATION_CONFIGURATION_MONITOR
  07/04/2016 12:33:34 PM 6352 (0x18D0) CBulkInsert::DRS_Init_BCPIN : Failed to BCP in
  SMS_REPLICATION_CONFIGURATION_MONITOR
  07/04/2016 12:33:34 PM 6352 (0x18D0) BCP in result is 2147500037.
  SMS_REPLICATION_CONFIGURATION_MONITOR
  07/04/2016 12:33:34 PM 6352 (0x18D0) ERROR: **Failed to BCP in for table
  INSTALLED_EXECUTABLE_DATA with error code 2147500037**.
  SMS_REPLICATION_CONFIGURATION_MONITOR
  07/04/2016 12:33:34 PM 6352 (0x18D0) ERROR: Failed to apply BCP for all articles in
  publication Hardware_Inventory_7. SMS_REPLICATION_CONFIGURATION_MONITOR
  07/04/2016 12:33:34 PM 6352 (0x18D0) Will try to apply BCP files again on next run.

What's happening here is that while the .cab file sent from the parent was unpacked by the
despooler, the space on the drive was exhausted, so it was only able to uncompress some of
the files. If you view despool.log, it will have a 2147024784 failure that refers to insufficient disk
space. To resolve this type of issue, free up disk space on the drive.

Check for BCP problems
If you still haven't found the source of the problem, it could be that the replication process was
interrupted because the bulk copy program (BCP) was going too slow.

Is sender throttled to this site and perhaps this is slowing down the BCP transfer?

To verify, open the console and go to Administration > Overview > Hierarchy Configuration >
File Replication, then right-click the site that would be sending the data. Verify that the
schedule availability is set to Open for all Priorities, and that Rate Limits is set to Unlimited to
this Site.

<!-- p.291 -->

If things are working but the data set from the BCP process is large and taking a long time to
send, you can increase the number of sender threads to speed things up. The defaults are
listed below. If your sender log is consistently advising no more threads available or Using 5
or 5 or Using 3 of 3 , this is a good indication that you may want to increase the sender

threads.

  ７ Note

  If increased, the setting takes effect in real time with no restart of anything required.

<!-- p.292 -->

Also if you have a rate limit set to Limited to specified maximum transfer rates by hour (as
shown in the following screenshot), Configuration Manager will only use one sender thread at
a time when transferring to that site regardless of what the number of sender threads are set
to. The default setting of Unlimited When Sending to this destination will use all the
configured sender threads.

More information
For more information about DRS, see the following articles:

      DRS Initialization In Configuration Manager 2012
      Data transfers between sites
      Database replication

 Last updated on 03/30/2026

<!-- p.293 -->

A log that has a line exceeding 8000
characters is truncated in the CMTrace log
viewer
This article provides workarounds for the issue that a line of a log that exceeds 8000 characters
causes the log to be truncated in the CMTrace log viewer.

Original product version: Microsoft System Center 2012 Configuration Manager
Original KB number: 2716956

Symptoms
In Microsoft System Center 2012 Configuration Manager, when you use the CMTrace log
viewer to review any log that contains a line exceeding 8000 characters, the log is truncated at
that line.

Workaround
There are two workarounds to this issue. First, you can view the log file in Notepad. Viewing
the log file in Notepad will allow you to see all of the content. Second, if you prefer to view the
log in CMTrace you can edit the offending lines in Notepad (making them less than 8000
characters long) and then view the edited log in CMTrace.

 Last updated on 02/04/2026

<!-- p.294 -->

[SDP 3][5ee487a8-b2ed-4bc8-80ea-
457f9b683c77] System Center
Configuration Manager diagnostic
This diagnostic package is designed to collect information used to troubleshoot most System
Center 2012 Configuration Manager and Configuration Manager current branch issues.

Original product version: Microsoft System Center 2012 Configuration Manager, Configuration
Manager (current branch)
Original KB number: 2704781

Configuration Manager client
                                                                                       ﾉ   Expand table

 Description                                              File name

 Summary of information gathered about the                {ComputerName}__CMClient_Summary.txt
 Configuration Manager client

 Application enforcement status                           {ComputerName}_CMClient_AppHistory.txt

 Configuration Manager client cache information           {ComputerName}_CMClient_CacheInfo.txt

 Configuration Manager client file version list           {ComputerName}_CMClient_FileVersions.txt

 Configuration Manager client inventory version           {ComputerName}_CMClient_InventoryVersions.txt
 information

 Software distribution execution history                  {ComputerName}_CMClient_ExecutionHistory.txt

 State Messages from CCM_StateMsg WMI class               {ComputerName}_CMClient_StateMessages.txt

 Update Status from CCM_UpdateStatus WMI class            {ComputerName}_CMClient_CCMUpdateStatus.txt

Configuration Manager logs
                                                                                       ﾉ   Expand table

 Description                                                    File name

 SQL Server error logs                                          {ComputerName}_Logs_SQLError.zip

 Configuration Manager client, site server, and site system     {ComputerName}_Logs_ConfigMgr.zip
 logs

 Windows logs (CBS, Temp, WindowsUpdate, and so on) and         {ComputerName}_Logs_Windows+OSD.zip
 Configuration Manager OSD-related logs (SMSTS, INF,
 Panther, DISM, UDI, Netsetup and so on)

<!-- p.295 -->

Configuration Manager site database
                                                                                      ﾉ   Expand table

Description                                                  File name

Summary of information gathered about the SQL Server         {ComputerName}__CMServer_Summary.txt
and Configuration Manager site database.

Blocked transactions, sp_who2 output and active              {ComputerName}_SQL_Transactions.txt
Snapshot transactions.

Configuration Manager maintenance tasks.                     {ComputerName}_SQL_CMDBInfo.txt

Configuration Manager site control file for the current      {ComputerName}_SQL_SiteControlFile.xml.txt
Site.

DRS replication troubleshooting information                  {ComputerName}_SQL_DRSData.zip

List of Configuration Manager site systems and               {ComputerName}_SQL_SiteSystems.txt
distribution points from SysResList and
DistributionPoints tables.

Results of the configuration checks performed against the    {ComputerName}_SQL_ConfigCompliance.txt
site database.

Software update point synchronization status.                {ComputerName}_SQL_SUPSync.txt

SQL Server version, security role members, and database      {ComputerName}_SQL_Basic.txt
information.

Top stored procedure calls by CPU, elapsed time, and so      {ComputerName}_SQL_TopQueries.txt
on.

Update servicing troubleshooting information                 {ComputerName}_SQL_UpdateServicing.zip

Configuration Manager site server
                                                                                      ﾉ   Expand table

Description                                               File name

Summary of information gathered about the                 {ComputerName}__CMServer_Summary.txt
Configuration Manager site server

Boundaries configured in Configuration Manager            {ComputerName}_CMServer_Boundaries.txt

Configuration Manager hierarchy information               {ComputerName}_CMServer_Hierarchy.txt

Configuration Manager site server file versions           {ComputerName}_CMServer_FileVersions.txt

Directory listing of RCM.box inbox                        {ComputerName}_CMServer_RCMFileList.txt

SMS_Executive service thread status from registry         {ComputerName}_CMServer_SMSExecThreads.txt

SPN information for the site database                     {ComputerName}_CMServer_SQLSPN.txt

Custom uploads

<!-- p.296 -->

                                                                                             ﾉ   Expand table

Description                                                       File name

Compressed copy of file specified by user                         {ComputerName}_filename.zip

General information
                                                                                             ﾉ   Expand table

Description                                                    File name

Summary of information gathered about the operating            {ComputerName}__OS_Summary.txt
system

List of running tasks                                          {ComputerName}_OS_TaskList.txt

Basic system information including machine name,               resultreport.xml
service pack, computer model, and processor name and
speed

Environment variables                                          {ComputerName}_OS_EnvironmentVariables.txt

Event logs for last 14 days (Application, System, and          {ComputerName}_OS_EventLogs.zip
Security)

List of installed certificates (Computer and User stores)      {ComputerName}_OS_Certificates.txt

List of installed services                                     {ComputerName}_OS_Services.txt

List of installed updates and hotfixes installed               {ComputerName}_Hotfixes.*

List of user rights (privileges) using showpriv.exe tool       {ComputerName}_UserRights.txt

Reboot pending flag from Windows Update, CBS,                  {ComputerName}_OS_RebootPending.txt
ConfigMgr client, and so on

Resultant set of Group Policies                                {ComputerName}_OS_GPResult.*

System information                                             {ComputerName}_OS_MSInfo.nfo

SystemInfo output                                              {ComputerName}_OS_SysInfo.txt

WMI quota configuration and loaded providers                   {ComputerName}_OS_WMIProviderConfig.txt

IIS information
                                                                                             ﾉ   Expand table

Description                                                File name

IIS configuration information                              {ComputerName}_IISConfiguration.zip

IIS logs (last 5 days)                                     {ComputerName}_Logs_IIS.zip

Virtual directory list and configuration                   {ComputerName}_IIS_VDirInfo.txt

<!-- p.297 -->

Networking basic information
                                                                                         ﾉ   Expand table

Description                                                 File name

Summary of networking information collected                 {ComputerName}__NET_Summary.txt

Active BITS jobs                                            {ComputerName}_OS_BITSTransfers.txt

Basic SMB configuration information, such as output of      {ComputerName}_OS_SMB-Info.txt
net.exe subcommands, such as net share , net sessions ,
net use , net accounts , net config

Basic TCP/IP and networking configuration information,      {ComputerName}_OS_TCPIP-Info.txt
such as TCP/IP registry key and outputs from ipconfig ,
netstat , nbtstat and netsh commands

Enabled Windows Firewall rules                              {ComputerName}_OS_EnabledFirewallRules.txt

Proxy configuration                                         {ComputerName}_OS_ProxyInfo.txt

Registry keys
                                                                                         ﾉ   Expand table

Description                                                                         File name

HKEY_CURRENT_USER\Software\Policies                                                 {ComputerName}_RegistryKey_HKCUP

HKEY_LOCAL_MACHINE\Software\Microsoft\CCM                                           {ComputerName}_RegistryKey_CCM.tx

HKEY_LOCAL_MACHINE\Software\Microsoft\OLE                                           {ComputerName}_RegistryKey_DCOM.

HKEY_LOCAL_MACHINE\Software\Microsoft\SMS                                           {ComputerName}_RegistryKey_SMS.txt

HKEY_LOCAL_MACHINE\Software\Microsoft\Update Services                               {ComputerName}_RegistryKey_WSUS.t

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall              {ComputerName}_RegistryKey_Uninsta

HKEY_LOCAL_MACHINE\Software\Policies                                                {ComputerName}_RegistryKey_HKLMP

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services                                {ComputerName}_RegistryKey_Service

Server manager and server roles information
                                                                                         ﾉ   Expand table

Description                                                                              File name

List of roles and features installed on server media (Windows Server 2008 R2 and later   resultreport.xml
versions)

Windows Update Agent information

<!-- p.298 -->

                                                                                        ﾉ   Expand table

 Description                                                        File name

 Windows Update Agent version, service security descriptors and     {ComputerName}__WUA_Summary.txt
 registry settings.

 File list in SoftwareDistribution directory                        {ComputerName}_WUA_FileList.txt

 File version of Windows Update Agent related EXE/DLL files         {ComputerName}_WUA_FileVersions.txt

WSUS server information
                                                                                        ﾉ   Expand table

 Description                                                File name

 Summary of WSUS server information collected.              {ComputerName}__WSUS_Summary.txt

 File list of WSUS content directory (only collected with   {ComputerName}_WSUS_FileList_ContentDir.txt
 WSUS diagnostics)

 File list of WSUS installation directory (only collected   {ComputerName}_WSUS_FileList_InstallDir.txt
 with WSUS diagnostics)

 File versions of EXE/DLL files in WSUS installation        {ComputerName}_WSUS_FileVersions.txt
 directory (only collected with WSUS diagnostics)

 List of approved updates (not collected for WSUS 4.0)      {ComputerName}_WSUS_ApprovedUpdates.xml

 WSUS basic information (not collected for WSUS 4.0)        {ComputerName}_WSUS_BasicInfo.txt

 WSUS logs                                                  {ComputerName}_Logs_WSUS.zip

 WSUS setup logs (if available)                             {ComputerName}_Logs_WSUSSetup.zip

Detect symptoms
In addition to collecting the information, this diagnostic package can detect one or more of the
following symptoms:

      Configuration Manager database: Database owner is not set to SA.
      Configuration Manager database: User Access mode is not set to MULTI_USER.
      Configuration Manager database: Database is marked as READ_ONLY.
      Configuration Manager database: Database is not ONLINE.
      Configuration Manager database: Recovery Model is not set to SIMPLE.
      Configuration Manager database: SQL Server Broker is disabled.
      Configuration Manager database: Recursive triggers are disabled.
      Configuration Manager database: Trustworthy property is disabled.
      Configuration Manager database: Honor Broker Priority is set to False.
      Configuration Manager database: Snapshot Isolation State is set to False.
      Configuration Manager database: Read Committed Snapshot is set to False.
      Configuration Manager database: Nested triggers are disabled.

<!-- p.299 -->

     Configuration Manager database: SQL Server change tracking backlog.
     Configuration Manager database: DBSchemaChangeHistory Excessive Growth.
     root\CCM WMI namespace connection failure.
     %ServiceName% service is stopped.
     %ServiceName% service is disabled.
     Configuration Manager client is in provisioning mode.

References
Microsoft Support Diagnostic Tool resources

Last updated on 03/30/2026

<!-- p.300 -->

Delta AD Group Discovery doesn't detect
group membership changes in nested OUs
Applies to: Supported versions of Configuration Manager

Summary
Active Directory Group Discovery (AD Group Discovery) in Configuration Manager uses
different algorithms for delta and full discovery cycles. During the delta discovery process,
Configuration Manager might miss group membership changes when groups belong to nested
OUs within your discovery scopes.

This article helps you identify this issue in your environment, and provides workarounds to
make sure that Configuration Manager detects all group membership changes.

Symptoms
You set up discovery scopes for AD Group Discovery to target specific Active Directory Domain
Services (AD DS) groups, as described in Configure Active Directory Group Discovery. The initial
full discovery cycle correctly discovers groups in all the in-scope OUs.

Some time after the initial full discovery cycle finishes, you change the membership of a group
that belongs to a child OU of another OU. After the delta discovery cycle runs, you notice that
Configuration Manager didn't detect your changes. However, if you force a full discovery cycle
to run, the issue resolves as the full discovery cycle discovers changes in all groups in the in-
scope OUs.

In particular, the issue occurs when you define scopes that resemble the following example:

     Scope A: Group A, in organizational unit OU-A
     Scope B: Group B, in organizational unit OU-B
     OU-B is a child OU of OU-A

In this example, the delta cycle of AD Group Discovery doesn't detect changes in Group B's
membership.

If you want to review log entries to verify this behavior in your system, see More information.

Cause

<!-- p.301 -->

During the delta cycle of AD Group Discovery, Configuration Manager identifies the target
groups in the discovery scopes, and the OUs to which those groups belong. It builds a tree
structure of those OUs. However, that tree doesn't include any child OUs of those OUs.

During the full discovery cycle of AD Group Discovery, Configuration Manager uses a different
algorithm that doesn't ignore child OUs. Therefore, the discovery process works as expected.

Workaround
Microsoft is aware of this issue. To work around this issue, use any of the following methods:

     Move the affected groups to higher-level OUs. For the earlier example, this action means
     moving Group B to another OU that isn't a child of OU-A (or of any other OU in the
     discovery scopes).
     Reconfigure the discovery scopes to include the child OUs as target OUs. For the previous
     example, this action means including OU-B in the discovery scopes as an Organizational
     Unit.
     Use only the full discovery process for AD Group Discovery.

More information
To see what this behavior looks like in the ADSGDis.log file, follow these steps:

   1. Open ADSGDis.log in a tool such as CMTrace, and then review the log entries to identify
     any discovery cycle.

   2. For that discovery cycle, create a list of the discovery scopes that appear in the log
     entries.

   3. Verify the Lightweight Directory Access Protocol (LDAP) path of each scope. In particular,
     check that the affected group is in a child OU of another one in the list. In the example
     that this article uses, the scopes and paths resemble the following example:

       Output

       !!!!Valid Search Scope Name: Unaffected Group      Search Path: LDAP://CN=GROUP-
       A,OU=OU-A,DC=FOURTHCOFFEE,DC=COM     IsValidPath: TRUE
       !!!!Valid Search Scope Name: Affected Group      Search Path: LDAP://CN=GROUP-
       B,OU=OU-B,OU=OU-A,DC=FOURTHCOFFEE,DC=COM      IsValidPath: TRUE

   4. Review the log entries to identify any delta discovery cycle. Look for an entry that
     resembles the following example, and then use the thread ID to filter log entries.

<!-- p.302 -->

      Output

      INFO: CADSource::incrementalSync returning 0x00000000~

  5. Review the log entries for the delta discovery cycle. The entries should resemble the
     following examples:

     a. Delta discovery processes the list of scopes.

          Output
          INFO: -------- Starting to process search scope (Unaffected Group) --------
          INFO: -------- Finished to process search scope (Unaffected Group) --------
          INFO: -------- Starting to process search scope (Affected Group) --------
          INFO: -------- Finished to process search scope (Affected Group) --------

     b. Delta discovery processes the LDAP search paths, starting at immediate search base .

          Output

          INFO: -------- Starting to process search scope (Immediate search base) -----
          ---
          INFO: Processing search path: 'LDAP://OU=OU-A,DC=FOURTHCOFFEE,DC=COM'.~

      c. Delta discovery identifies the search path for the child OU (OU-B in the example) as an
        invalid path, and skips it to process the next path.

          Output

          INFO: Found invalid Search Path: LDAP://OU=OU-B,OU=OU-
          A,DC=FOURTHCOFFEE,DC=COM. Probably it's sub search path of other search path
          and will be covered by them.
          INFO: -------- Finished to process search scope (Immediate search base) -----
          ---

Last updated on 01/20/2026

<!-- p.303 -->

The lastLogonTimestamp attribute in
System Center 2012 Configuration Manager
may not be accurate
This article describes a by design behavior that the lastLogonTimestamp attribute may not be
updated as expected in Configuration Manager.

Original product version: Microsoft System Center 2012 Configuration Manager
Original KB number: 2679653

Symptoms
Consider the following scenario in System Center 2012 Configuration Manager:

      Active Directory User Discovery is enabled in Configuration Manager.
      You use the lastLogonTimestamp attribute to determine the last logon for a user.

In this scenario, the exact time at which a particular user last logged on may not be accurate.

Cause
This behavior occurs because the design and default configuration of Active Directory may
result in the value of the lastLogonTimestamp attribute being updated only when the current
value in Active Directory is 9 to 14 days older than the time of logon.

References
For more information about the lastLogonTimestamp attribute, see the following articles:

      Last-Logon-Timestamp attribute
      "The LastLogonTimeStamp Attribute" - "What it was designed for and how it works"

 Last updated on 03/30/2026

<!-- p.304 -->

Domain name of resource is changed after
installing January 2022 Windows updates
This article describes how to identify and resolve an issue in which resource domain is changed
after you install January 2022 Windows updates.

Applies to: Configuration Manager (current branch)

Symptoms
After you install January 2022 or later Windows cumulative updates on a Configuration
Manager site server, the domain name that is associated with users, groups, or devices may be
changed. This issue occurs when the NetBIOS domain name (also known as the pre-Windows
2000 domain name) is different from the first element of the fully qualified domain name
(FQDN).

For example, a resource is in a domain with the NetBIOS domain name AAA , but with the FQDN
BBB.contoso.com . The resource is discovered as AAA\User1 or AAA\Computer1 . After you install

January 2022 Windows updates and the discovery runs, the resource name may be changed to
BBB\User1 or BBB\Computer1 .

The domain name of the resource may alternate between AAA and BBB , which removes or adds
devices to collections that have query rules based on a domain membership.

  ７ Note

  Direct membership rules are not affected.

Cause
January 2022 Windows updates introduced an NTLM fallback that may block NTLM
authentication if Kerberos authentication isn't successful , which changes the behavior in
Configuration Manager current branch.

Resolution
This issue is fixed in Configuration Manager current branch, version 2203.

<!-- p.305 -->

If the issue still occurs after upgrading to version 2203 and later versions, make sure that you
meet the requirements for establishing the Kerberos connection from the site server to the
domain controllers of the target domain. For example:

     TCP traffic on port 88 (Kerberos) is allowed.

     TCP and UDP traffic on port 389 (LDAP and CLDAP) is allowed.

     The site server can resolve service location (SRV) records for Kerberos services. For
     example:

       Output

       _kerberos._tcp.contoso.com
       _kerberos._udp.contoso.com
       _kerberos._tcp.dc._msdcs.contoso.com

Workaround
To work around this issue, change collection rules to include both the NetBIOS domain name
and the DNS domain name. For example:

select * from SMS_R_System where SMS_R_System.SystemGroupName in

("AAA\\Group1","BBB\\Group1")

Identify the issue
Here are the steps to check logs and identify the issue:

   1. Increase the size of the ADSgDis.log file to 100 megabytes (MB) or more to accommodate
     a full Active Directory group discovery. Under the following registry key, change the
     MaxFileSize registry value to 104857600 (the default value is 2621440 ).

     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\SMS_AD_SECURITY_GROUP_DISCOVERY_AG

     ENT

   2. Enable verbose logging for the ADSgDis.log file. Under the following registry key, change
     the Verbose Logs registry value to 1 (the default value is 0 ).

     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\COMPONENTS\SMS_AD_SECURITY_GROUP_DISCOVERY

     _AGENT

<!-- p.306 -->

 3. Run a full Active Directory group discovery and make sure the following message is
   logged in the ADSgDis.log file upon completion.

   INFO: Succeeded running full sync stored procedure

 4. Filter by the thread ID that logged the above message and find the following message in
   the filtered logs.

   VERBOSE : Could not get Domain Name using DSCrackNames, will parse ADs Path to get

   it

 5. Check the following lines around. You'll find a group and its member are from different
   domains.

     Output

     INFO: DDR was written for group 'contoso\ParentGroup' -
     C:\ConfigMgr\inboxes\auth\ddm.box\userddrsonly\asg1607o.DDR at <Date Time>.~
     VERBOSE: group has 1 members~
     ...
     VERBOSE: Domain controller name for the SID is: \\DC.fourthcoffee.local
     VERBOSE: full ADs path of member:
     LDAP://DC.fourthcoffee.local/CN=ChildGroup,CN=Users,DC=fourthcoffee,DC=local~
     ...
     VERBOSE: Could not get Domain Name using DSCrackNames, will parse ADs Path to
     get it
     VERBOSE: ParentGroup: "contoso\ParentGroup" ChildGroup:
     "fourthcoffee\ChildGroup"

 6. Check the Windows system event logs of the time-correlated event ID 40970 as follows.
   You'll find the domain controller of the Service Principal Name (SPN) and the realm are
   from different domains. This event may not occur if the Kerberos authentication attempt
   is cached.

     Output

     The Security System has detected a downgrade attempt when contacting the 3-
     part SPN LDAP/DC.contoso.local/fourthcoffee.LOCAL
     with error code "The SAM database on the Windows Server does not have a
     computer account for this workstation trust relationship. (0xc000018b)".
     Authentication was denied.

 7. If so, you've identified the issue successfully.

Additional information

<!-- p.307 -->

This issue can also occur if the Discover objects within Active Directory groups option is
enabled in System or User Discovery scope settings. In this case, here are the steps to check
logs and identify the issue. You can also temporarily disable the option for the discovery scopes
in which you have groups with members from other domains.

   1. Increase the size of the ADSysDis.log or ADUsrDis.log file to 100 megabytes (MB) or more
     to accommodate a full Active Directory system or user discovery. Under one of the
     following registry keys, change the MaxFileSize registry value to 104857600 (the default
     value is 2621440 ).

            HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\SMS_AD_SYSTEM_DISCOVERY_AGEN

            T

            HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\SMS_AD_USER_DISCOVERY_AGENT

   2. Enable verbose logging for the ADSysDis.log or ADUsrDis.log file. Under one of the
     following registry keys, change the Verbose Logs registry value to 1 (the default value is
     0 ).

            HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\COMPONENTS\SMS_AD_SYSTEM_DISCOVERY_AG

            ENT

            HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\COMPONENTS\SMS_AD_USER_DISCOVERY_AGEN

            T

   3. Run a full Active Directory system or user discovery and make sure the following message
     is logged in the ADSysDis.log or ADUsrDis.log file upon completion.

     INFO: CADSource::fullSync returning 0x00000000~

   4. Filter by the thread ID that logged the above message and find the following message in
     the filtered logs.

     VERBOSE : Could not get Domain Name using DSCrackNames, will parse ADs Path to get

     it

   5. Check the following lines around. You'll find a group and its member are from different
     domains.

       Output

       INFO: Processing discovered group object with ADsPath =
       'LDAP://DC1.CONTOSO.COM/CN=GROUP1,OU=OU,DC=CONTOSO,DC=COM'~

<!-- p.308 -->

       VERBOSE: group not found in discovered group list~
       VERBOSE: Bound to group.~
       VERBOSE: group has 3 members~
       ...
       VERBOSE: full ADs path of member:
       LDAP://DC2.fourthcoffee.com/CN=Machine1,OU=US,DC=fourthcoffee,DC=com~
       ...
       VERBOSE: Could not get Domain Name using DsCrackNames, will parse ADs Path to
       get it
       VERBOSE: domain = 'FourthCoffee' full domain name = 'fourthcoffee.com'
       INFO: DDR was written for system 'Machine1' -
       C:\ConfigMgr\inboxes\auth\ddm.box\adsqznjr.DDR at <Date Time>.~

  6. If so, you've identified the issue successfully.

Last updated on 03/30/2026

<!-- p.309 -->

Clients don't update with the latest
antimalware definition files after the
Endpoint Protection point role is installed
This article introduces a workaround for the issue that clients are not updated with the latest
antimalware definition files after you install the Endpoint Protection point site system role in
Configuration Manager.

Original product version: Microsoft System Center 2012 Configuration Manager
Original KB number: 2688242

Symptoms
You install the Endpoint Protection point site system role in Configuration Manager and set the
Manage Endpoint Protection client on client computers setting to True on the Endpoint
Protection page. In this scenario, client computers are not updated with the latest antimalware
definition files.

Cause
This problem occurs because the Disable alternate sources (such as Microsoft Windows
Update, Microsoft Windows Server Update Services, or UNC shares) for the initial definition
update on client computers option is set to True which is the default setting.

Workaround
To work around this problem, set the Disable alternate sources (such as Microsoft Windows
Update, Microsoft Windows Server Update Services, or UNC shares) for the initial definition
update on client computers option to False. After you change this setting, the clients can
download and install antimalware definition file updates immediately after installation as long
as the client has access to one of the sources that hosts the files.

 Last updated on 03/30/2026

<!-- p.310 -->

Microsoft Network Inspection service
started by Configuration Manager may be
stopped by AD Group Policy
This article describes a by-design behavior where the Microsoft Network Inspection service
may be stopped by Active Directory Group Policy.

Original product version: Microsoft System Center 2012 Configuration Manager
Original KB number: 2688238

Symptoms
Consider the following scenario:

     A Microsoft System Center 2012 Configuration Manager administrator sets the Enable
     protection against network-based exploits option to True and then deploys the policy to
     a collection of devices. This option is part of the real-time protection item on the
     Antimalware tab for the Microsoft Forefront Endpoint Protection (FEP) policies in the
     Configuration Manager console.
     Then, the Configuration Manager client sets the start of the Microsoft Network Inspection
     service to Automatic on all devices in the target collection.
     An Active Directory administrator configures Group Policy to set the start for the
     Microsoft Network Inspection service to Disabled.

In this scenario, when the Group Policy settings are applied, the Microsoft Network Inspection
service is stopped, and the start of the service is set to Disabled. When the Configuration
Manager client evaluates client health and determines that the service is disabled, it remediates
the problem by setting the start of the service to Automatic and starts the service again.
However, the service soon stops again because the service is stopped by the Active Directory
Group Policy.

Status
This behavior is by design. Group Policy settings to disable services should be carefully
evaluated together with the Configuration Manager group or the System Center 2012 Endpoint

<!-- p.311 -->

Protection group to make sure that these settings don't disable services for required
functionalities.

 Last updated on 03/30/2026

<!-- p.312 -->

Configuration Manager console displays
out-of-date Endpoint Protection Definition
version and last update time
This article provides a solution for the issue that Configuration Manager console displays out-
of-date Endpoint Protection Definition version and last update time while the clients have the
latest version of definition installed.

Original product version: Configuration Manager
Original KB number: 4528414

Symptoms
When you use Endpoint Protection together with Configuration Manager, you experience the
following issues:

        In the Configuration Manager console, you open the Assets and Compliance workspace
        under the Devices node. In that workspace, you notice that the Endpoint Protection
        Definition Last Version and Endpoint Protection Last Update Time columns display out-
        of-date values for some devices. However, the clients show that they have the latest
        versions applied.
        Topic type 1901 (State_Topictype_Ep_Am_Health) isn't logged in StateMessage.log on the
        clients.
        The following error messages are logged in ExternalEventAgent.log on the clients:

  PARSE XML to get the query String SELECT * FROM MSFT_MPComputerStatus
  ...
  Execute all initialization actions for policy change from CCM_ExternalEventConfig.
  Could not open the registry key
  SOFTWARE\Microsoft\CCM\ExternalEventAgent\Criterias\Differentiation\ComputerStatu
  sStateMessage\SyncStatus with error 0x80070002.​
  Could not open the registry key
  SOFTWARE\Microsoft\CCM\ExternalEventAgent\Criterias\Differentiation\ComputerStatu
  sStateMessage with error 0x80070002.​
  Failed to load previous values of Differentiation criteria ComputerStatusStateMessage with
  error 0x80070002.​

<!-- p.313 -->

  Could not open the registry key
  SOFTWARE\Microsoft\CCM\ExternalEventAgent\Criterias\Differentiation\InfectionStatus
  StateMessage\SyncStatus with error 0x80070002.​
  Could not open the registry key
  SOFTWARE\Microsoft\CCM\ExternalEventAgent\Criterias\Differentiation\InfectionStatus
  StateMessage with error 0x80070002.​
  Failed to load previous values of Differentiation criteria InfectionStatusStateMessage with
  error 0x80070002.​

Additionally, the following registry keys don't exist on the client:

      HKLM\SOFTWARE\Microsoft\CCM\ExternalEventAgent\Criterias\Differentiation\ComputerSta

     tusStateMessage

      HKLM\SOFTWARE\Microsoft\CCM\ExternalEventAgent\Criterias\Differentiation\InfectionSt

     atusStateMessage

Cause
This issue occurs because the instance of the MSFT_MpComputerStatus class doesn't exist in the
root\Microsoft\ProtectionManagement namespace. The client queries this instance to populate

the related registry keys.

Resolution
To fix the issue, run the following command on the affected client computers to re-register the
ProtectionManagement provider:

 Console

 Register-CimProvider -ProviderName ProtectionManagement -Namespace
 root\Microsoft\protectionmanagement -Path <path of ProtectionManagement.dll> -
 Impersonation True -HostingModel LocalServiceHost -SupportWQL -ForceUpdate

  ７ Note

  In this command, <path of ProtectionManagement.dll> is the placeholder for the path of
  ProtectionManagement.dll. For example:
  C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.1907.4-
  0\ProtectionManagement.dll

<!-- p.314 -->

After you run this command, the following conditions are true:

      The instance of MSFT_MpComputerStatus is populated in the
      root\Microsoft\ProtectionManagement namespace.

      Topic type 1901 is logged in StateMessage.log.
      The affected values in the Configuration Manager console are updated.

More information
Windows Defender logs can help you identify the root cause of this issue. For example, the
following log snippet indicates the presence of a different antivirus solution:

  2019-09-04T08:00:11.166Z [Mini-filter] Denied access to file:
  \ProgramData\Microsoft\Windows Defender\Platform\4.18.1907.4-
  0\Powershell\MSFT_MpComputerStatus.cdxml, from process
  '\Device\HarddiskVolume2\Program Files (x86)\Symantec\Symantec Endpoint
  Protection\14.0.3929.1200.105\Bin\ccSvcHst.exe' (PID: 3408)

To collect diagnostic logs for Windows Defender, follow the steps in Collect Update
Compliance diagnostic data for Windows Defender AV Assessment.

Third-party information disclaimer

The third-party products that this article discusses are manufactured by companies that are
independent of Microsoft. Microsoft makes no warranty, implied or otherwise, about the
performance or reliability of these products.

 Last updated on 03/30/2026

<!-- p.315 -->

Recommended antivirus exclusions for
Configuration Manager site servers, site
systems, and clients
This article contains recommendations that may help an administrator determine the cause of
potential instability on a computer that's running a supported version of Configuration
Manager site servers, site systems, and clients when it's used together with antivirus software.

Original product version: Microsoft System Center 2012 Configuration Manager, Microsoft
System Center 2012 R2 Configuration Manager, Configuration Manager (current branch)
Original KB number: 327453

Summary
We recommend you temporarily apply these procedures to evaluate a system. If your system
performance or stability is improved by the recommendations that are made in this article,
contact your vendor for instructions or an updated version of the antivirus software.

  ） Important

  This article contains information that shows how to help lower security settings or how to
  temporarily turn off security features on a computer. You can make these changes to
  understand the nature of a specific problem. Before you make these changes, we
  recommend that you evaluate the risks that are associated with implementing this
  workaround in your particular environment.

Antivirus real-time protection can cause many problems on Configuration Manager site
servers, site systems, and clients.

Possible symptoms include:

     Remote site system components aren't installed. SiteComp.log, Distmgr.log, hman.log, or
     other Configuration Manager log files may contain errors such as error 80070005.

     The Configuration Manager client cannot be installed through client push.

     Client inventory information is inaccurate, missing, or out-of-date.

<!-- p.316 -->

      Backlogs occur in the Install_Directory\Inboxes folders on site servers.

      Backlogs occur in the Install_Directory\MP\Outboxes subfolders on management points
      (MP).

      Software Center isn't populated by deployed software on client systems, or doesn't start.
      Also, the CCMRepair.log file may contain an error similar to the following example:

          Output

          Database verification failed with result: 0x80004005 but DB:
          C:\Windows\CCM\filename.sdf could be opened, skipping DB repair.

      Software that is deployed to clients cannot be installed.

      Compliance data for software deployments is inaccurate.

Default installation folders
Use the following installation folder paths as variables for the recommended exclusions that
are provided in this article.

  ７ Note

  The following paths are the default installation paths and may vary depending on the
  environment. We recommend that you review the environment and configuration to
  ensure you have the correct paths in place.

                                                                                         ﾉ    Expand table

 Folder                              Path

 ConfigMgr installation folder       %ProgramFiles%\Microsoft Configuration Manager

 MP installation folder              %ProgramFiles%\SMS_CCM

 Client installation folder          %Windir%\CCM

 ContentLib_drive                    The path will vary. The default path is the C:\ drive.

Exclusions

<!-- p.317 -->

We recommend that you add the following real-time protection exclusions to prevent these
problems.

Folder exclusions for site servers
     ConfigMgr installation folder\Inboxes

     ConfigMgr installation folder\Logs

     ConfigMgr installation folder\EasySetupPayload

     ContentLib_drive\SCCMContentLib

       ７ Note

       If you have a remote content library, this folder isn't on the site server. For more
       information, see Configure a remote content library for the site server.

Folder exclusions for site systems
     Management points
        MP installation folder\ServiceData
        Either of the following folders:
            ConfigMgr installation folder\MP\OUTBOXES
            Installation drive\SMS\MP\OUTBOXES
     Distribution points
        Client installation folder\ServiceData
        ContentLib_drive\SCCMContentLib
        ContentLib_drive\SMS_DP$
        ContentLib_drive\SMSPKGDrive_Letter$
        ContentLib_drive\SMSPKG
        ContentLib_drive\SMSPKGSIG
        ContentLib_drive\SMSSIG$
     Site database servers
        How to choose antivirus software to run on computers that are running SQL Server

Folder exclusions for clients
     Client installation folder\*.sdf

<!-- p.318 -->

      Client installation folder\ServiceData
      Client installation folder\ScriptStore
      C:\Windows\CCMCache
      C:\Windows\CCMSetup
      Client installation folder\Logs
      C:\Windows\Setup\Scripts
      C:\Windows\SMSTSPostUpgrade
      C:\Program Files\Microsoft Policy Platform\authorityDb\*.sdf
      Client installation folder\temp

File exclusions for MPs
      POL00000.pol in MP installation folder\PolReqStaging

Don't scan outgoing files on MPs
      Most antivirus software has an option to scan files that are copied to a remote location
      (outgoing files). This option should be disabled on management points.

      For Windows Defender, the policy name is Configure monitoring for incoming and
      outgoing file and program activity. And it should be set to Scan only incoming files.

      For more information, see Enable and configure Windows Defender Antivirus always-on
      protection in Group Policy.

Process exclusions
Process exclusions are necessary only if aggressive antivirus programs consider Configuration
Manager executables (.exe) to be high-risk processes.

Site and site systems:

      ConfigMgr installation folder\bin\x64\Smsexec.exe
      ConfigMgr installation folder\bin\x64\Sitecomp.exe
      ConfigMgr installation folder\bin\x64\Smswriter.exe (site server only)
      ConfigMgr installation folder\bin\x64\Cmupdate.exe (site server only)
      ConfigMgr installation folder\bin\x64\Smssqlbkup.exe, or
      SQLFQDN\bin\x64\Smssqlbkup.exe (site database server only)
      MP installation folder\Ccmexec.exe

Client:

<!-- p.319 -->

     Client installation folder\Ccmexec.exe
     Client installation folder\Ccmrepair.exe
     Client installation folder\ScClient.exe
     Client installation folder\CcmAADBroker.exe
     Client installation folder\RemCtrl\CmRcService.exe
     %windir%\CCMSetup\Ccmsetup.exe
     %windir%\CCMSetup\autoupgrade\Ccmsetup*.exe

 ７ Note

 Starting in Configuration Manager current branch version 1910, this file name has been
 changed to Ccmsetup.<Packageid>.<PackageVersion>.exe.

References
     Configuration Manager Current Branch Antivirus Exclusions
     Updated System Center 2012 Configuration Manager Antivirus Exclusions with more
     details on OSD and Boot Images
     How to choose antivirus software to run on computers that are running SQL Server
     Virus scanning recommendations for Enterprise computers that are running currently
     supported versions of Windows

Last updated on 03/30/2026

<!-- p.320 -->

Microsoft Deployment Toolkit (MDT) -
immediate retirement notice
Applies to: Windows 11, Windows 10, Windows Server

Summary
Microsoft is announcing the immediate retirement of Microsoft Deployment Toolkit (MDT).
MDT will no longer receive updates, fixes, or support. Existing installations will continue to
function as is. However, we encourage customers to transition to modern deployment
solutions.

Impact
     MDT is no longer supported, and won't receive future enhancements or security updates.
     MDT download packages might be removed or deprecated from official distribution
     channels.
     No future compatibility updates for new Windows releases will be provided.

Alternative deployment solutions

Windows Autopilot (recommended)
Windows Autopilot provides a modern, cloud-based deployment and provisioning experience
that's designed to simplify device setup and reduce operational overhead.

Learn more: Overview of Windows Autopilot

Configuration Manager operating system deployment (OSD)
For customers who have on-premises infrastructure and existing Configuration Manager
environments, operating system deployment (OSD) remains a fully supported option.

Learn more: Deploy Windows with Configuration Manager

Recommended next steps
   1. Begin planning a transition from MDT to Windows Autopilot or Configuration Manager
     OSD.
