---
title: "Welcome — pages 121-160"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0121-0160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0121-0160
family: sccm
documentKind: "doc"
abstract: "CContentDefinition::TotalFileSizes failed; 0x8007052e Date Time SMS_PACKAGE_TRANSFER_MANAGER 4892 (0x131c) CSendFileAction::SendFiles failed; 0x8007052e Date Time SMS_PACKAGE_TRANSFER_MANAGER 4892 (0x131c) CSendFileAction::SendContent failed; 0x8007052e Additionally, event 4625"
---

# Welcome — pages 121-160

<!-- p.121 -->

  CContentDefinition::TotalFileSizes failed; 0x8007052e
  Date Time SMS_PACKAGE_TRANSFER_MANAGER 4892 (0x131c) CSendFileAction::SendFiles
  failed; 0x8007052e
  Date Time SMS_PACKAGE_TRANSFER_MANAGER 4892 (0x131c)
  CSendFileAction::SendContent failed; 0x8007052e

Additionally, event 4625 is logged on the server that hosts the content library:

  Log Name:       Security
  Source:        Microsoft-Windows-Security-Auditing
  Event ID:      4625
  Task Category: Logon
  Level:      Information
  Keywords:      Audit Failure
  User:       N/A
  Computer:       STORAGE.CONTOSO.COM
  Description:
  An account failed to log on.

  Account For Which Logon Failed:
  Security ID: NULL SID
  Account Name: <AccountName>
  Account Domain: FABRIKAM

  ７ Note

  FABRIKAM\<AccountName> represents the Site System Installation Account for the
  remote DP.

Cause
This issue occurs because Configuration Manager incorrectly uses the Site System Installation
Account for the remote site system to connect to the remote content library.

Workaround
To work around this issue, follow these steps:

<!-- p.122 -->

   1. Create a local account on the server that hosts the content library.
   2. Assign the new account the same name as the Site System Installation Account that is
      configured for the remote site system.
   3. Grant the new account access to the content library folder.

This action enables pass-through authentication to work around the distribution failure that
occurs because Configuration Manager incorrectly uses the Site System Installation Account.

If you notice error entries for Microsoft SQL Server authentication in the DistMgr.log file, follow
the steps in Site system installation account is incorrectly used for a remote site system to
connect to SQL Server database to work around the issue.

 Last updated on 03/30/2026

<!-- p.123 -->

Content distribution in Configuration
Manager
This guide is intended to help administrators understand the content distribution process and
serves to build a foundation for diagnosing and resolving general content distribution related
problems.

Original product version: Configuration Manager current branch, Microsoft System Center
2012 Configuration Manager, Microsoft System Center 2012 R2 Configuration Manager
Original KB number: 4482728

Summary
This guide is divided up into the following articles:

      Components and threads for content distribution
      Distribution points installation, upgrade, and configuration
      Content library in Configuration Manager
      Package actions in content distribution
      Troubleshoot content distribution
      Advanced troubleshooting tips for content distribution

More Information
For more information regarding content distribution in Configuration Manager, see the
following articles:

      Fundamental concepts for content management in Configuration Manager
      Configuration Manager Tools

You can also post a question in our Configuration Manager support forum .

Visit our blog     for all the latest news, information, and tech tips on Configuration Manager.

 Last updated on 03/30/2026

<!-- p.124 -->

Components and threads for content
distribution
This article helps you understand components and threads for content distribution.

Original product version: Configuration Manager current branch, Microsoft System Center
2012 Configuration Manager, Microsoft System Center 2012 R2 Configuration Manager

The components used for content distribution
Here's a quick list of the primary components used for content distribution:

                                                                                 ﾉ   Expand table

 Name           Component name                         Friendly     Description
                                                       name

 Distribution   SMS_DISTRIBUTION_MANAGER               DistMgr      Manages content and creates
 Manager                                                            jobs for PkgXferMgr

 Package        SMS_PACKAGE_TRANSFER_MANAGER           PkgXferMgr   Transfers packages to
 Transfer                                                           distribution points
 Manager

 Hierarchy      SMS_HIERARCHY_MANAGER                  Hman         Processes and replicates
 Manager                                                            changes to the site hierarchy

 Sender         SMS_SENDER                             Sender       Initiates inter-site
                                                                    communications across
                                                                    TCP/IP networks

 Despooler      SMS_DESPOOLER                          Despooler    Processes incoming
                                                                    replication files from parent
                                                                    or child sites

 Scheduler      SMS_SCHEDULER                          Scheduler    Creates sender jobs

 Database       SMS_DATABASE_NOTIFICATION_MONITOR      SmsDbMon     Watches the database for
 Notification                                                       changes to certain tables and
 Monitor                                                            creates files in the inboxes of
                                                                    components responsible for
                                                                    processing those changes

 SMS Provider   SMS Provider                           SMSProv      Windows Management
                                                                    Instrumentation (WMI)

<!-- p.125 -->

 Name            Component name                        Friendly     Description
                                                       name

                                                                    Provider that assigns read
                                                                    and write access to the
                                                                    Configuration Manager
                                                                    database at a site

 SMS DP          SMS DP Provider                       SMSDPProv    Windows Management
 Provider                                                           Instrumentation (WMI)
                                                                    Provider that manages
                                                                    Content Library operations
                                                                    on the DP

 SMS Agent       SMS Agent Host                        CcmExec      SMS Agent Host is the
 Host                                                               Configuration Manager client
                                                                    agent service that also hosts
                                                                    server-side components such
                                                                    as Management Point and
                                                                    Pull Distribution Point

 Data Transfer   DataTransferService                   DTS          Data Transfer Service is a
 Service                                                            component of CcmExec
                                                                    responsible for download
                                                                    files via BITS.

Distribution Manager (DistMgr) threads
Distribution Manager (DistMgr) performs a variety of operations to distribute content to the
distribution points (DPs). These operations are handled by the different types of threads, and
the diagram below explains the DistMgr thread hierarchy for the default thread configuration:

<!-- p.126 -->

                                                                                      

Main DistMgr thread

Log entry for identification: SMS_EXECUTIVE started SMS_DISTRIBUTION_MANAGER as thread
ID 3648 (0xE40)

This thread is started by SMS_Executive on service startup. The main DistMgr thread starts
the replication processing, DP Manager, content cleanup, DP certificate monitoring,
content library move, IIS config change processing, DP reassignment and upgrade
processing threads when it starts. It also starts package processing threads on-demand
when a package change occurs

In addition to managing these threads, this thread also handles changes to the Site
Control File and updates DP settings (configure DP/PXE, update registry settings, create
monitoring/usage tasks on the DP, and so on).

Replication processing thread

Log entry for identification: Starting thread for processing replication, thread ID =
0x1A14 (6676)

<!-- p.127 -->

This thread is started by the main DistMgr thread and processes the following files in the
DistMgr.box\incoming directory:

                                                                                    ﾉ   Expand table

 File     Description

 .STA     Updates package status in the PkgStatus table in the database.

 .FWD     Forwards the specified package to the specified destination site by creating a mini-job to
          send the package.

 .DMD     Distributes on-demand requests. Targets the specified package to the specified DP.

 .PUL     Updates pull DP package response in the PullDPResponse table in the DB.

  ７ Note

  This thread is single-threaded and doesn't create more threads to process any of
  these files.

DP Manager thread

Log entry for identification: Starting the DP Manager thread, thread ID = 0x5D8 (1496)

This thread is started by the main DistMgr thread and processes removal of DPs when
detecting a Site Control File change. When an appropriate Site Control File change occurs,
SMSDBMON drops a DPN (DP Notification) file in DistMgr.box that's processed by this
thread.

DPN files are used to notify a DP change, which involves DP removal (detected by Action
= 3 in the DistributionPoints table).

  ７ Note

  This thread is single-threaded and doesn't create more threads to perform work.

Content cleanup thread

Log entry for identification: Starting the content cleanup thread, thread ID = 0x1604
(5636)

<!-- p.128 -->

This thread is started by the main DistMgr thread, and runs content cleanup. It
determines if content cleanup is required by detecting orphaned content from the
database. This thread uses default batch size of 50 for the number of contents it can
instruct a remote DP to delete at a time. However, this value can be overridden by setting
the following registry key:

SMS\Components\SMS_DISTRIBUTION_MANAGER\RemoteContentCleanupBatchSize

DWORD value can be between 1 and 500.

  ７ Note

  Do not change this value without consulting Microsoft support professional. This
  thread is single-threaded and doesn't create more threads to perform work.

DP certificate monitoring thread

Log Entry for identification: Starting the DP cert monitoring thread, thread ID = 0x7290
(29328)

This thread is started by the main DistMgr thread. This thread processes .CER files and
configures the certificate binding in IIS when enhanced HTTP mode is enabled. This mode
requires use of Configuration Manager generated certificates in IIS.

  ７ Note

  This thread is single-threaded and doesn't create more threads to perform work.

Content library move thread

Log Entry for identification: Starting the content library move thread, thread ID =
0x11D6C (73068)

This thread is started by the main DistMgr thread, and moves content library to the new
location after a .CML file is dropped in DistMgr.box .

  ７ Note

  This thread is single-threaded and doesn't create more threads to perform work.

<!-- p.129 -->

IIS config change processing thread

Log Entry for identification: Starting the IIS config change processing thread, thread
ID = 0x408C (16524)

This thread is started by the main DistMgr thread, and handles configuring IIS virtual
directories for standard and pull distribution points after IIS files are dropped in
DistMgr.box . This thread reads the IISConfigChangeThreadLimit Site Control File (SCF)

property for SMS_DISTRIBUTION_MANAGER component to determine the number of threads it
can start for performing IIS changes simultaneously. The default value of
IISConfigChangeThreadLimit SCF Property is 50, but it can be changed if necessary.

However, if this SCF property doesn't exist for some reason, the default value of 50 is
used for IISConfigChangeThreadLimit .

  ７ Note

  This thread does create more threads to perform DP IIS config changes. Each worker
  thread handles configuration of IIS virtual directories of a specific DP.

DP reassignment thread

Log Entry for identification: Starting the shared DP reassignment thread, thread ID =
0x9C0C (39948)

This thread is started by the main DistMgr thread, and handles DP reassignments for
standard and pull distribution points when a .DPU file is dropped in DistMgr.box . This
thread reads the SharedDPImportThreadLimit Site Control File (SCF) property for
SMS_DISTRIBUTION_MANAGER component to determine the number of threads it can start for

performing DP reassignments simultaneously. The default value of
SharedDPImportThreadLimit SCF Property is 50, but it can be changed if necessary.

However, if this SCF property doesn't exist for some reason, the default value of 50 is
used for SharedDPImportThreadLimit .

  ７ Note

  This thread does create more threads to perform DP reassignments. Each worker
  thread handles reassignment of a specific DP.

Upgrade processing thread

<!-- p.130 -->

Log entry for identification: Starting the DP upgrade processing thread, thread ID =
0x1968 (6504)

This thread is started by the main DistMgr thread, and handles DP installations and
upgrades for standard and pull distribution points. It calls spGetDPsForUpgrade to get a list
of DPs that need to be upgraded. This thread reads the DPUpgradeThreadLimit Site
Control File (SCF) property for SMS_DISTRIBUTION_MANAGER component to determine the
number of threads it can start for performing DP Installations/Upgrades simultaneously.
The default value of DPUpgradeThreadLimit SCF Property is 50, but it can be changed if
necessary. However, if this SCF property doesn't exist for some reason, the default value
of 5 is used for DPUpgradeThreadLimit .

  ７ Note

  This thread does create more threads to perform DP installation/upgrade work. Each
  worker thread handles installation/upgrade of a specific DP.

Package processing thread

Log entry for identification: Started package processing thread for package 'PKGID',
thread ID = 0x8E8 (2280)

These threads are started by the main DistMgr thread. The number of package processing
threads is determined by the Maximum number of packages thread setting in the
Software Distribution Component Configuration properties. Each package processing
thread performs the hashing of the package content and creates a compressed copy of
the content.

  ７ Note

  Although all package processing threads run simultaneously, they are responsible for
  hashing and compressing package source. There is a Critical Section around the
  compression, meaning only one thread can be compressing content at a time. If a
  bunch of new, large packages are created and distributed, the per-package threads
  can block in a chain waiting for their turn to get the compression lock.

Depending on the package actions (add/update/delete), each package processing thread
also creates:

<!-- p.131 -->

        DP threads to create a Package Transfer Manager job for adding/updating content on
        a DP.
        DP threads to instruct a remote distribution point to remove content from the content
        library.

     The number of DP threads each package processing thread can create is determined by
     the Maximum threads per package setting in the Software Distribution Component
     Configuration properties.

        ７ Note

        Package processing threads are multi-threaded and each package processing thread
        creates more threads to perform work. Each worker thread handles
        add/update/remove operations for the DPs.

Distribution Manager thread configuration
All Configuration Manager sites (including the central administration site) allow configuring the
number of threads that can be used for distributing content to the distribution points (DPs).
This configuration is specific to each site and can be accessed by right-clicking the site under
the Sites node and selecting Configure Site Components > Software Distribution. Here's a
look at the default configuration:

<!-- p.132 -->

In most cases, you would only be concerned with the Maximum number of packages and
Maximum threads per package settings.

     Maximum number of packages: Specifies the maximum number of packages that
     ConfigMgr can send to the DPs simultaneously. The specified value should be between 1
     and 50.
     Maximum threads per package: Specifies the maximum number of threads assigned to
     each package during distribution. Specified value should be between 1 and 999.

The default configuration of Maximum number of packages=3 and Maximum threads per
package=5 can also be referred to 3x5. This is how the thread configuration will be often
denoted in the workflow.

What this really means
Effect on Distribution Manager (DistMgr)

With the default thread configuration of 3x5, DistMgr can simultaneously process three
packages and use up to five threads for each package, allowing it to use up to a total of 15

<!-- p.133 -->

threads to perform work. Here's how this breaks down assuming we have more than three
packages that need to get distributed to more than 5 DPs:

                                                                                             

To process each individual package, a package processing thread is spawned by the main
DistMgr thread. This package processing thread uses one out of three package processing slots
from the Maximum number of packages setting. There is a unique package processing thread
per package - DistMgr does not start multiple package processing threads for the same
package. This means that three unique packages will utilize three unique package processing
threads. Each of these package processing threads can spawn up to five DP threads to
distribute the package to five DPs simultaneously.

Effect on Package Transfer Manager (PkgXferMgr)

For each PkgXferMgr job created by DistMgr, PkgXferMgr uses one thread. Thread
configuration of 3x5 means that the sending capacity for PkgXferMgr is set to 15, which means
that PkgXferMgr can't work on more than 15 jobs simultaneously, limiting it to a maximum of
15 threads.

How long a thread runs
DistMgr threads

The purpose of a DP thread is to create a job for Package Transfer Manager, which then does
the actual content copy to the DP. DP threads finish after creating the PkgXferMgr job, and as a
result, the lifetime of a DP thread is short. Due to this nature, most of the time there is no need

<!-- p.134 -->

to set up aggressive thread configuration to speed up content distribution. Instead of setting
aggressive values, look towards Choosing the right values (more information below).

PkgXferMgr threads

For standard DPs, since PkgXferMgr threads perform the real work of sending the content, the
lifetime of these threads depends on the size of the packages. For larger packages, these
threads can take a long time depending on the package size and network speed. While these
threads can take a long time to complete, the lifetime of DistMgr threads is much shorter,
which means that DistMgr can queue a large number of jobs for PkgXferMgr, creating a
backlog of jobs in the queue.

For pull DPs, PkgXferMgr threads notify the pull DP, asking the pull DP to download the
content. As a result, the lifetime of PkgXferMgr threads for pull DPs is short. PkgXferMgr does
start another thread to perform pull DP polling (based on the configured polling interval) to
check on the progress of the job. However, this is also a quick operation and these threads do
have a short lifetime as well.

Choosing the right values
To determine the appropriate values for these settings, you first need to understand the
Configuration Manager hierarchy. Let's consider the following hypothetical Configuration
Manager environment:

     Central administration site: CS1
     Primary site: PS1
     Number of regular distribution points reporting to PS1: 200
     Total number of packages: 1000

In this environment, the default thread configuration (3x5) means that if a new package needs
to get distributed to all 200 DPs, we will only process 5 DPs at a time. Once a DP thread exits,
another DP thread will then spawn and the process will continue until all the DPs are
processed. This process will take some time to loop through all 200 DPs.

To optimize this, we first need to ask a couple of questions:

   1. How many packages do you foresee getting added/updated/distributed simultaneously
     on an average?
   2. How many DPs do you have in the site? How is the network configuration between the
     site server and these DPs?

<!-- p.135 -->

Assuming the answer to the first question is 5, and the answer to the second question is 200
with good network connectivity, you could theoretically set Maximum number of packages to
5 and Maximum threads per package to 200, allowing Configuration Manager to send up to
five packages to all 200 DPs simultaneously. However, this means that when there is more than
the average load we can create up to 1000 threads, which is many threads. More threads are
usually good, but not always since the work being performed also relies on hardware and
network configurations. Too many threads can sometimes cause bottlenecks and slow things
down instead of improving them.

The most important thing to remember when configuring these settings is to find a balance.
For the example above, a reasonable option would be to set the thread configuration to 5x100
(or even 5x50 depending on hardware/network) which still allows Configuration Manager to
process up to 100 DPs simultaneously for five different packages. With these settings, the
maximum number of threads that can spawn during high load will not exceed 500.

  ７ Note

  As a general guideline, it is recommended that the total number of threads not exceeds
  750. This means you could set the thread configuration to 3x250, 5x150, 10x75 and so on.

In the same hierarchy, you may run into a situation where you are bringing a new DP in the
environment and you need to distribute all 1000 packages to the DP. In this case, thread
configuration of 5x100 is not going to be effective since we can only process 5 packages at a
time, and processing a 1000 packages will take a considerable amount of time. In this scenario,
you could choose to either:

     Temporarily set the thread configuration to something like 50x10 that is more suitable for
     the current requirement, but is not a good option in the long run considering we have
     200 DPs.
     Permanently set the thread configuration to something like 20x25 that provides a far
     better balance and will offer similar performance in a scenario where more packages need
     to go to handful of DPs as well as a scenario where a handful of packages need to go to
     many DPs.

  ） Important

  There isn't a set recommendation on values for thread configuration; it varies for each
  environment and should be set after understanding your environment and requirements.

<!-- p.136 -->

  Always remember to find a balance!

Sender thread configuration
Each Configuration Manager site (including the central administration site and secondary sites)
has one sender. The sender manages the network connection from one site to a destination
site, and can establish connections to multiple sites at the same time. To connect to a site, the
sender uses the file replication route to the site to identify the account to use to establish the
network connection. The sender also uses this account to write data to the destination site's
SMS_SITE share.

By default, sender writes data to a destination site by using multiple concurrent threads. Each
concurrent thread can transfer a different file-based object to the destination site. By default,
when the sender begins to send an object, it continues to write blocks of data for that object
until the entire object is sent.

All Configuration Manager sites allow you to configure the number of threads that can be used
by the Sender component to send data concurrently to other sites. This configuration is
specific to each site, and can be accessed from the Site Properties under the Sites node by
selecting the Sender tab. Here's a look at the default configuration:

<!-- p.137 -->

All sites: The maximum number of simultaneous communications allowed for this sender. The
default value is 5. These communications can be destined for different sites or all for the same
site, except as restricted by the maximum value specified in Per site.

Per site: The maximum number of simultaneous communications allowed to any single
destination site. The default value is 3.

  ７ Note

  When configuring the total number of concurrent sending threads to be used when
  communicating with other sites, the total number of sending threads should be
  configured as a greater number than the threads configured for the per site setting. If the
  total number of sending threads is equal to the number configured to be used per site
  and a receiving site is unavailable, it could cause all sending threads to become used

<!-- p.138 -->

  when attempting to communicate with the unavailable site and prevent site-to-site
  communication to other sites.

What this means
The value specified under All sites defines the total number of threads that Sender can use for
sending data concurrently to other sites. Out of the total number of threads for All sites, you
can allot a maximum number of threads under Per site that can be used for sending data to
any one destination site. By default, each site is configured to use five concurrent threads, with
three available for use when sending data to any one destination site. When you increase this
number, you can increase the throughput of data between sites by enabling Configuration
Manager to transfer more files at the same time. Increasing this number also increases the
demand for network bandwidth between sites.

Choose the right values
To determine appropriate values for these settings, you first need to understand the
Configuration Manager hierarchy. Let's consider the following hypothetical Configuration
Manager environment:

     Central administration site: CS1
     Primary site: PS1
     Primary site: PS2
     Primary site: PS3
     Primary site: PS4

In this environment, the default Sender thread configuration will allow using a total of 5
threads. Out of those 5 threads, 3 can be used for any one of the 4 destination primary sites. If
an administrator sends 3 to all of these sites, it is possible that sender will end up using three
threads for one of these sites (let's say PS1), leaving only 2 threads for the remaining sites. Out
of the remaining 2 threads, sender may use 1 for PS2 and the other for PS3 utilizing all five
allowed threads leaving no room for sending data concurrently to PS4. At this point, Sender
will have to wait for one of the existing 5 threads to finish before it can send more data. Once
an existing thread finishes, Sender will then be able to use another thread for sending more
data to the PS2/PS3/PS4 sites.

It is recommended to set aside 10 threads for each site that Sender will communicate with. In
this case, the CS1 site can communicate with four other sites, which means that a Per site value
of 10 for four sites will require setting the All sites value to 40.

<!-- p.139 -->

  ７ Note

  This is a general recommendation and these values may require further tweaking
  depending on the number of packages a site needs to send concurrently to other sites.

Bandwidth control and threads
In Configuration Manager, you can configure a schedule and set specific throttling settings for
remote distribution points as well as for file replication routes for sites. The controls for
scheduling and throttling to the remote distribution point are similar to the settings for a
standard sender address, but in this case, the settings are used by a component called Package
Transfer Manager.

For the Package Transfer Manager component (for Site Server - > DP), the throttling settings
are configured in the properties for a standard distribution point that is not on a site server.

For the Sender component (for Site Server <-> Site Server), the throttling settings are
configured in the properties of the file replication route under Hierarchy Configuration > File
Replication.

  ７ Note

  The time settings are based on the time zone from the sending site, not the distribution
  point.

Schedule options
To restrict data, select the time period, and then select one of the following settings for
availability:

      Open for all priorities: Specifies that Configuration Manager sends data to the
      distribution point with no restrictions.

      Allow medium and high priority: Specifies that Configuration Manager sends only
      medium and high priority data to the distribution point.

      Allow high priority only: Specifies that Configuration Manager sends only high priority
      data to the distribution point.

<!-- p.140 -->

     Closed: Specifies that Configuration Manager does not send any data to the distribution
     point.

     You can restrict data by priority or close the connection for selected time periods.

Rate limit options
This is used to configure rate limits to control the network bandwidth that is in use when
transferring content to the distribution point. You can choose from the following options:

     Unlimited when sending to this destination: Specifies that Configuration Manager sends
     content to the distribution point with no rate limit restrictions.
     Pulse mode: Specifies the size of the data blocks that are sent to the distribution point.
     You can also specify a time delay between sending each data block. Use this option when
     you must send data across a low-bandwidth network connection to the distribution point.
     For example, you might have constraints to send 1 KB of data every five seconds,
     regardless of the speed of the link or its usage at a given time.
     Limited to specified maximum transfer rates by hour: Specify this setting to have a site
     send data to a distribution point by using only the percentage of time that you configure.
     When you use this option, Configuration Manager does not identify the networks
     available bandwidth, but instead divides the time it can send data into slices of time. Then
     data is sent for a short block of time, which is followed by blocks of time when data is not
     sent. For example, if the maximum rate is set to 50%, Configuration Manager transmits
     data for a period of time followed by an equal period of time when no data is sent. The
     actual size amount of data, or size of the data block, is not managed. Instead, only the
     amount of time during which data is sent is managed.

For more information on these settings, see Configuring Content Management in
Configuration Manager.

How this affects Sender and PkgXferMgr threads
When bandwidth control is enabled for a site, the sender component will ignore the Sender
thread configuration for the site and will only use one thread for that site. Similarly, when
bandwidth control is enabled for a DP, PkgXferMgr will ignore the thread configuration and will
only use one thread for the DP.

  ７ Note

<!-- p.141 -->

  This applies even when the Limit available bandwidth (%) is set to 100%.

When bandwidth control is in effect, PkgXferMgr.log will log one of these lines:

Scheduling:

  ~Address to DPNAME.CONTOSO.COM is currently under bandwidth control, therefore only
  one connection is allowed, returning send request to the pool.

Pulse Mode:

  ~Addres to DPNAME.CONTOSO.COM is currently in pulse mode, therefore only one
  connection is allowed.
  ~Abandoning send request because only one connection is allowed in pulse mode.

Sender.log will show similar entries when bandwidth throttling is configured.

 Last updated on 03/30/2026

<!-- p.142 -->

Distribution points installation, upgrade,
and configuration
This article describes distribution points installation, upgrade, configuration changes, removal
and how these operations work. It's important to understand these flows to properly identify
and diagnose the issue.

Original product version: Configuration Manager current branch, Microsoft System Center
2012 Configuration Manager, Microsoft System Center 2012 R2 Configuration Manager

Introduction
When troubleshooting DP installation and upgrade issues, it is important to remember that DP
installation/upgrade is performed by a thread from the DP upgrade processing thread pool.
Review the DP installation/upgrade process flow to understand how to identify the thread
performing the DP installation/upgrade and filter the DistMgr.log for the identified thread.
Review the filtered DistMgr.log to identify whether the DP installation/upgrade
failed/succeeded and proceed accordingly.

When troubleshooting DP removal issues, it is important to remember that the DP removal is
performed by the DP Manager thread, which is single-threaded. This means that if multiple DPs
are removed at the same time, the DP removal will be performed one by one and can take a
long time if a large number of DPs are removed. Review the DP Removal process to understand
how to identify the DP Manager thread and filter the DistMgr.log for the identified thread.

DP installation
The DP installation involves the steps listed below. These steps cover a typical DP installation
initiated from the Configuration Manager console after the administrator has finished the DP
installation wizard. Each step is described, followed by an example of how the step can be
monitored by examination of the associated log file. If you have a problem with DP installation,
the log files should show you exactly where in the process the problem is occurring and
provide vital clues to why the process is failing.

Step 1: The admin console creates an instance of the
SMS_SCI_SysResUse WMI class for the new DP

<!-- p.143 -->

After the administrator completes the DP installation wizard, the admin console creates an
instance of the SMS_SCI_SysResUse WMI class within the SMS Provider namespace.
SMSProv.log shows the creation of this instance and contains other useful entries such as the
SMSAppName, MachineName, UserName, ApplicationName, which can be helpful when
investigating problems.

  SMS Provider 4180 (0x1054) ~
  SMS Provider 4180 (0x1054) CExtUserContext::EnterThread : User=CONTOSO\Admin Sid=
  <SID> Caching IWbemContextPtr=00000000046687B0 in Process 0x540 (1344)~
  SMS Provider 4180 (0x1054) Context: SMSAppName =Configuration Manager
  Administrator console~
  SMS Provider 4180 (0x1054) Context: MachineName =PS1SITE.CONTOSO.COM~
  SMS Provider 4180 (0x1054) Context: UserName =CONTOSO\Admin~
  SMS Provider 4180 (0x1054) Context: ObjectLockContext=<ContextID>~
  SMS Provider 4180 (0x1054) Context: ApplicationName
  =Microsoft.ConfigurationManagement.exe~
  SMS Provider 4180 (0x1054) Context: ApplicationVersion=5.0.8355.1000~
  SMS Provider 4180 (0x1054) Context: LocaleID=MS\0x409~
  SMS Provider 4180 (0x1054) Context: __ProviderArchitecture=32 ~
  SMS Provider 4180 (0x1054) Context: __RequiredArchitecture=0 (Bool)~
  SMS Provider 4180 (0x1054) Context: __ClientPreferredLanguages=en-US,en~
  SMS Provider 4180 (0x1054) Context: __CorrelationId={CorrelationID}~
  SMS Provider 4180 (0x1054) Context: __GroupOperationId=170804 ~
  SMS Provider 4180 (0x1054) CExtUserContext : Set ThreadLocaleID OK to: 1033~
  SMS Provider 4180 (0x1054) CSspClassManager::PreCallAction, dbname=CM_PS1~
  SMS Provider 4180 (0x1054) PutInstanceAsync SMS_SCI_SysResUse~
  SMS Provider 4180 (0x1054) CExtProviderClassObject::DoPutInstanceInstance~
  SMS Provider 4180 (0x1054) INFO: 'PS1DP1.CONTOSO.COM' is a valid FQDN.
  SMS Provider 4180 (0x1054) Auditing: User CONTOSO\Admin created an instance of class
  SMS_SCI_SysResUse.~
  SMS Provider 4180 (0x1054) CExtUserContext::LeaveThread : Releasing
  IWbemContextPtr=73828272~
  SMS Provider 4180 (0x1054) ~

When this WMI instance is created, SMS Provider also inserts a row in the database:

 SQL

<!-- p.144 -->

 insert into vSMS_SC_SysResUse (SiteNumber, RoleName, NALPath, NALResType) values
 (1, N'SMS Site System', N'["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
 ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\', N'Windows NT Server')

Step 2(optional): SMS Provider adds the newly created DP to a
boundary group if specified during the wizard
During the DP installation wizard, the administrator has the option to specify whether the new
DP should be added to an existing or a new boundary group. SMS Provider is responsible for
making these changes and logs the following entries:

  SMS Provider 4180 (0x1054) AddSiteSystem~~
  SMS Provider 4180 (0x1054) Adding site system
  ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\ to the boundary group PS1 Assignment And
  Content ~
  SMS Provider 4180 (0x1054) Successfully added 1 servers to boundary group PS1
  Assignment And Content~
  SMS Provider 4180 (0x1054) Auditing: User CONTOSO\Admin modified an instance of class
  SMS_BoundaryGroup.~
  SMS Provider 4180 (0x1054) CExtUserContext::LeaveThread : Releasing
  IWbemContextPtr=73828272~
  SMS Provider 4180 (0x1054) ~

Step 3: SMSDBMON detects a site control change and notifies
HMAN to process site control file
SMSDBMON constantly monitors various tables in the database and thus detects a change to
the site control file related tables (in step 1). On receiving (denoted as RCV in the log) a
change, SMSDBMON notifies the appropriate components by dropping/sending (denoted as
SND in the log) files in the component inbox. In this case, SMSDBMON notifies HMAN to
process the site control file for changes:

  SMS_DATABASE_NOTIFICATION_MONITOR 2580 (0xa14) RCV: UPDATE on SiteControl for
  SiteControl_AddUpd_HMAN [PS1 ][1027921]
  SMS_DATABASE_NOTIFICATION_MONITOR 2580 (0xa14) SND: Dropped
  E:\ConfigMgr\inboxes\HMAN.box\PS1.SCU [1027921]

<!-- p.145 -->

Step 4: HMAN processes the site control file and processes all
distribution points
HMAN wakes up to process the SCU file dropped by SMSDBMON, and then starts processing
the site control file. During this process, HMAN will look at all distribution points to determine
if any DPs are new or changed.

4a: For the new DPs, HMAN detects that there is a new site system and inserts data in the
DistributionPoints table:

  SMS_HIERARCHY_MANAGER 2448 (0x990) ~Processing site control file: Site PS1
  SMS_HIERARCHY_MANAGER 2448 (0x990) New site system: PS1 PS1DP1.CONTOSO.COM
  SMS Distribution Point
  SMS_HIERARCHY_MANAGER 2448 (0x990) New site system: PS1 PS1DP1.CONTOSO.COM
  SMS Site System
  SMS_HIERARCHY_MANAGER 2448 (0x990) ~Server Info of site PS1 has changed. Update
  the DPInfo table in the database.
  SMS_HIERARCHY_MANAGER 2448 (0x990) ~ Distribution Points of site PS1 have changed.
  Update the DistributionPoints table in the database.
  SMS_HIERARCHY_MANAGER 2448 (0x990) ~Inserted DP
  ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\. CRC:439BCA34,PDP:0,PullDP:0
  SMS_HIERARCHY_MANAGER 2448 (0x990) SQL>>>insert DistributionPoints ( ServerName,
  NALPath, ShareName, SMSSiteCode, IsPullDP, IsPeerDP, IsBITS, PreStagingAllowed,
  IsMulticast, AnonymousEnabled, TokenAuthEnabled, SslState, DPType, Priority,
  TransferRate, DPFlags, IsProtected, DPDrive, Type, MinFreeSpace, IsPXE, IsActive,
  ResponseDelay, UdaSetting, BindPolicy, SupportUnknownMachines, CertificateType,
  IdentityGUID, BindExcept, PXEPassword, Action, Account, Description, DPCRC ) values (
  N'PS1DP1.CONTOSO.COM', N'["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\', N'', N'PS1', 0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 0, 0, 1,
  N'', N'Windows NT Server', 50, 0, 0, 0, 0, 0, 0, 0, N'23a72b6c-eace-4218-929c-
  4c80638c031e', N'', N'', 0, N'', N'PS1 Standard DP', N'439BCA34' )

4b: In addition to inserting a new row for the DP in the DistributionPoints table, HMAN also
distributes the default client packages to the DP:

  SMS_HIERARCHY_MANAGER 2448 (0x990) Loaded client upgrade settings from DB
  successfully. FullClientPackageID=CS100002, StagingClientPackageID=CS100024,

<!-- p.146 -->

  ClientUpgradePackageID=CS100003, PilotingUpgradePackageID=CS100025,
  ClientUpgradeAdvertisementID=CS120000, ClientPilotingAdvertisementID=(null)
  SMS_HIERARCHY_MANAGER 2448 (0x990) INFO: Successfully added client package
  (ID=CS100002) to DP ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\~
  SMS_HIERARCHY_MANAGER 2448 (0x990) INFO: Successfully added client package
  (ID=CS100003) to DP ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\~
  SMS_HIERARCHY_MANAGER 2448 (0x990) INFO: Successfully added client package
  (ID=CS100024) to DP ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\~
  SMS_HIERARCHY_MANAGER 2448 (0x990) INFO: Successfully added client package
  (ID=CS100025) to DP ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\~

4c: HMAN updates the DP certificate (self-signed or PKI) information in the database by calling
the spUpdateDPCert stored procedure:

  SMS_HIERARCHY_MANAGER 2448 (0x990) DP cert query: EXEC spUpdateDPCert
  N'PS1DP1.CONTOSO.COM', N'23a72b6c-eace-4218-929c-4c80638c031e', ... ...

Note that for any distribution points that haven't changed, HMAN logs an entry:

  SMS_HIERARCHY_MANAGER 2448 (0x990) ~Will not update DP
  ["Display=\\PS1SITE.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1SITE.CONTOSO.COM\.
  DBCRC:13639BB,NewCRC:13639BB,Action:0,PDP:0,PullDP:0
  SMS_HIERARCHY_MANAGER 2448 (0x990) ~Will not update DP
  ["Display=\\PS1SQL.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1SQL.CONTOSO.COM\.
  DBCRC:DB8F08DA,NewCRC:DB8F08DA,Action:0,PDP:0,PullDP:1
  SMS_HIERARCHY_MANAGER 2448 (0x990) ~Will not update DP
  ["Display=\\PS1SYS.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1SYS.CONTOSO.COM\.
  DBCRC:B65C605F,NewCRC:B65C605F,Action:0,PDP:0,PullDP:0

  ７ Note

<!-- p.147 -->

  If HMAN encounters a failure trying to insert or update any of the DPs, the entire
  transaction is rolled back and none of the DPs are processed. If this continues, you will see
  issues where DPs do not get installed or DP property changes do not take effect.

Step 5: HMAN finishes processing the site control file and
raises a status message
When HMAN finishes processing the site control file, it raises a status message with ID 3306
which means Hierarchy Manager successfully processed
E:\ConfigMgr\inboxes\hman.box\PS1.SCU , which in our example represents the site control file

for site ConfigMgr Primary Site 1 (PS1):

  SMS_HIERARCHY_MANAGER 2448 (0x990) STATMSG: ID=3306 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_HIERARCHY_MANAGER"
  SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=1956 TID=2448 GMTDATE=Wed May 11
  18:33:34.813 2016 ISTR0="E:\ConfigMgr\inboxes\HMAN.box\PS1.SCU" ISTR1="ConfigMgr
  Primary Site 1" ISTR2="PS1" ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8=""
  ISTR9="" NUMATTRS=0

Step 6: SMSDBMON detects a change in DistributionPoints
table, and notifies DistMgr to install the DP
SMSDBMON detects a change in the DistributionPoints table (from step 4a) and instructs
DistMgr to begin the DP installation by dropping a <DPID>.INS file into the DistMgr.box
folder:

  SMS_DATABASE_NOTIFICATION_MONITOR RCV: INSERT on DistributionPoints for
  DistributionPoints_Ins [32 ][1027928]
  SMS_DATABASE_NOTIFICATION_MONITOR SND: Dropped
  E:\ConfigMgr\inboxes\distmgr.box\32.INS [1027928]

In this example, 32 is the distribution point ID. You can find the DP name from the DPID by
running the following SQL query against the database:

  SQL

  SELECT * FROM DistributionPoints WHERE DPID = 32

<!-- p.148 -->

Step 7: DistMgr wakes up to process the INS file and starts a
DP upgrade worker thread to install the DP
DistMgr wakes up to process the .INS file that was dropped by SMSDBMON. DP installations
and upgrades are handled by the main DP upgrade processing thread. To perform the DP
installation, the DP upgrade processing thread uses a thread from the DP upgrade processing
thread pool which is set to use a maximum of 50 threads by default. In the following log
entries, the main DP upgrade processing thread ID is 2860, which creates a new worker thread
with ID 4788 (0x12b4) for the DP installation:

  SMS_DISTRIBUTION_MANAGER 2860 (0xb2c) DP upgrade processing thread: Upgrading
  DP with ID 32. Thread 0x12b4. Used 1 threads out of 50.

Next, DP processing worker thread 4788 (0x12b4) starts the installation process for DPID 32,
which is our new DP:

  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) ~Processing 32.INS
  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) ~DPID 32 - NAL Path
  ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\ , ServerName = PS1DP1.CONTOSO.COM,
  DPDrive = , IsMulticast = 0, PXE = 0, RemoveWDS = 0

Step 8: DistMgr DP upgrade worker thread installs the DP
Here, DistMgr thread 4788 starts the actual DP installation where it completes the following:

     Copies necessary files to the DP
     Installs IIS (if specified during the installation wizard)
     Installs MSXML and the Visual C++ Redistributable components
     Installs the DP WMI Provider
     Creates virtual directories and configures IIS
     Updates the registry settings on the DP server
     Installs the PXE Role (if configured)

Note that the log entries below are truncated to only show relevant information:

  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) Installed ISAPI on PS1DP1.CONTOSO.COM,
  copied E:\ConfigMgr\bin\x64\..\x64\smsfileisapi.dll to
  \\PS1DP1.CONTOSO.COM\ADMIN$\system32\inetsrv\smsfileisapi.dll

<!-- p.149 -->

  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) ~Successfully created share SMS_DP$ on
  server PS1DP1.CONTOSO.COM
  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) ~OS version 6.3.9600: installed IIS on
  remote server PS1DP1.CONTOSO.COM.
  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) MSXML 6.0 is configured on DP
  PS1DP1.CONTOSO.COM successfully
  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) Run command
  'C:\SMS_DP$\sms\bin\vcredist_x64.exe /q /norestart /log
  "C:\SMS_DP$\sms\bin\vcredist.log"' to install VC redist
  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) ~Successfully installed DP WMI provider on
  the remote distribution point
  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) Configure IIS virtual directories successfully
  on the distribution point PS1DP1.CONTOSO.COM
  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) ConfigureDP
  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) DP registry settings have been successfully
  updated on PS1DP1.CONTOSO.COM
  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) ConfigurePXE
  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) ~
  ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\ is a Pull DP

   Tip

  Once you reach step 8, it's a lot easier to monitor the installation progress by filtering the
  log for the worker thread ID (4788 in this example).

Step 9 (optional): PXE Provider Role and Windows
Deployment Services is installed on the DP (if enabled)
If the DP is enabled for PXE, PXE installation is initiated when ConfigurePXE is logged in
DistMgr.log. At this time, SMSDPProv.log on the distribution point will show the PXE/WDS
installation progress:

  CcmInstallPXE
  Running: C:\SMS_DP$\sms\bin\vcredist_x64.exe /q /norestart /log
  "C:\SMS_DP$\sms\bin\vcredist.log"
  Waiting for the completion of: C:\SMS_DP$\sms\bin\vcredist_x64.exe /q /norestart /log

<!-- p.150 -->

"C:\SMS_DP$\sms\bin\vcredist.log"
Run completed for: C:\SMS_DP$\sms\bin\vcredist_x64.exe /q /norestart /log
"C:\SMS_DP$\sms\bin\vcredist.log"
Created the DP mutex key for WDS.
Finding Wimgapi.Dll
MsiEnumRelatedProducts failed
FindProduct failed; 0x80070103
Found C:\Windows\system32\wimgapi.dll
Wimgapi.dll is already installed.
Path to smsdp.dll is 'C:\SMS_DP$\sms\bin\smsdp.dll' 05-11-2016 14:36:57.000 PXE
performance counters have been initialized
Failed to open WDS service.
WDS is NOT INSTALLED
Installing WDS.
Running: ServerManagerCmd.exe -i WDS -a
Failed (2) to run: ServerManagerCmd.exe -i WDS -a
Running: PowerShell.exe -Command Import-Module ServerManager; Get-WindowsFeature
WDS; Add-WindowsFeature WDS
Waiting for the completion of: PowerShell.exe -Command Import-Module ServerManager;
Get-WindowsFeature WDS; Add-WindowsFeature WDS
Run completed for: PowerShell.exe -Command Import-Module ServerManager; Get-
WindowsFeature WDS; Add-WindowsFeature WDS
Successfully installed WDS.
Machine is running Windows Server. (NTVersion=0X603, ServicePack=0)
WDS is INSTALLED
Setting TFTP config key as:
System\CurrentControlSet\Services\WDSSERVER\Providers\WDSTFTP
Configuring TFTP read filters
SetupComplete is set to 0
REMINST not set in WDS
WDS is NOT Configured
Share (REMINST) does not exist. (NetNameNotFound) (0x00000906)
GetFileSharePath failed; 0x80070906
REMINST share does not exist. Need to create it.
Enumerating drives A through Z for the NTFS drive with the most free space.
Drive 'C:' is the best drive for the SMS installation directory.
Creating REMINST share to point to: C:\RemoteInstall

<!-- p.151 -->

  Succesfully created share REMINST
  Removing existing PXE related directories
  Registering WDS provider: SourceDir: C:\SMS_DP$\sms\bin
  Registering WDS provider: ProviderPath: C:\SMS_DP$\sms\bin\smspxe.dll
  DoPxeProviderRegister 05-11-2016 14:37:10.000 PxeLoadWdsPxe
  Loading wdspxe.dll from C:\Windows\system32\wdspxe.dll
  wdspxe.dll is loaded
  PxeProviderRegister has suceeded (0x00000000)
  Disabling WDS/RIS functionality
  Found privilege otifyPrivilege on service WDSServer
  Found privilege SeRestorePrivilege on service WDSServer
  Found privilege SeBackupPrivilege on service WDSServer
  Found privilege SeSecurityPrivilege on service WDSServer
  Privilege SeTakeOwnershipPrivilege NOT found service WDSServer
  ChangeServiceConfig2 succeeded for WDSServer. Added privilege
  SeTakeOwnershipPrivilege
  ChangeServiceConfig succeeded for WDSServer. StartType: 0x2
  WDSServer status is 1
  WDSServer is NOT STARTED
  Failed to restart WDS service
  Running: WDSUTIL.exe /Initialize-Server /REMINST:"C:\RemoteInstall"
  Waiting for the completion of: WDSUTIL.exe /Initialize-Server /REMINST:"C:\RemoteInstall"
  Run completed for: WDSUTIL.exe /Initialize-Server /REMINST:"C:\RemoteInstall"
  Machine is running Windows Server. (NTVersion=0X603, ServicePack=0)
  ProcessBootImages failed; 0x80070003
  CcmInstallPXE: Deleting the DP mutex key for WDS.
  Installed PXE

Step 10: DP installation finishes successfully
Once the DP installation finishes successfully, the worker thread raises a status message with ID
2399 which means 'Successfully completed the installation or upgrade of the distribution point
on computer <DPNALPath>':

  SMS_DISTRIBUTION_MANAGER 4788 (0x12b4) STATMSG: ID=2399 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
  SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=1956 TID=4788 GMTDATE=Wed May 11

<!-- p.152 -->

  18:36:58.062 2016 ISTR0="["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\" ISTR1="PS1DP1.CONTOSO.COM" ISTR2=""
  ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1
  AID0=404 AVAL0="["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\"

Step 11 (for Pull DPs only): DistMgr upgrade processing thread
instructs DP WMI Provider to install pull DP by running
pulldp.msi
If the DP is configured to be a pull DP, the DistMgr upgrade processing thread starts another
DP upgrade worker thread to perform the pull DP installation. This DP upgrade worker thread
instructs the SMS DP Provider to run pulldp.msi to install the pull DP.

  SMS_DISTRIBUTION_MANAGER 2188 (0x88c) Upgrading PullDP with ID 33. Thread 0x9c0.
  Used 1 threads out of 50.
  SMS_DISTRIBUTION_MANAGER 2496 (0x9c0) ~DPID 33 - NAL Path
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\ , ServerName = PS1DP2.CONTOSO.COM,
  DPDrive = , IsMulticast = 0, PXE = 1, RemoveWDS = 0
  SMS_DISTRIBUTION_MANAGER 2496 (0x9c0) ConfigurePullDP
  SMS_DISTRIBUTION_MANAGER 2496 (0x9c0) ~NAL Path
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\ is a Pull DP
  SMS_DISTRIBUTION_MANAGER 2496 (0x9c0) For server PS1DP2.CONTOSO.COM processor
  architecture is x64~
  SMS_DISTRIBUTION_MANAGER 2496 (0x9c0) File
  '\\PS1DP2.CONTOSO.COM\SMS_DP$\sms\bin\pulldp.msi' is signed and trusted.
  SMS_DISTRIBUTION_MANAGER 2496 (0x9c0) File
  '\\PS1DP2.CONTOSO.COM\SMS_DP$\sms\bin\pulldp.msi' is signed with MS root cert.
  SMS_DISTRIBUTION_MANAGER 2496 (0x9c0) Installing PullDP, check
  \\PS1DP2.CONTOSO.COM\SMS_DP$\sms\logs\smsdpprov.log and
  \\PS1DP2.CONTOSO.COM\SMS_DP$\sms\logs\pulldp_install.log
  SMS_DISTRIBUTION_MANAGER 2496 (0x9c0) PullDP
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\ is marked Installed

<!-- p.153 -->

At this time, the SMSDPProv.log file on the pull DP will show that the installation of pull DP has
been initiated:

  2020 (0x7e4) Started process C:\SMS_DP$\sms\bin\vcredist_x64.exe /q /norestart /l
  C:\SMS_DP$\sms\logs\vcredist.log
  2020 (0x7e4) Run completed for: C:\SMS_DP$\sms\bin\vcredist_x64.exe /q /norestart /l
  C:\SMS_DP$\sms\logs\vcredist.log
  2020 (0x7e4) Started process msiexec.exe /quiet /i C:\SMS_DP$\sms\bin\pulldp.msi /log
  C:\SMS_DP$\sms\logs\pulldp_install.log

When pull DP is installed on a server which has the ConfigMgr client installed, the command
used for installation is:

  4744 (0x1288) Started process E:\SMS_DP$\sms\bin\ccmsetup.exe /autoupgrade
  /upgradetolatest
  /postinstallmsi:"E:\SMS_DP$\sms\bin\pulldp.msi;E:\SMS_DP$\sms\logs\pulldp_install.log"

Pull DP installation progress can be reviewed and monitored by looking at the MSI log file
pulldp_install.log.

DP upgrade
Distribution point upgrade involves the steps listed below. These steps cover a typical DP
upgrade that is initiated after upgrading a ConfigMgr 1511 site to ConfigMgr 1602. Note that
the process is similar when installing a service pack or cumulative update on various
Configuration Manager 2012 versions.

Step 1: Upgrade results in a site reset, which reinstalls DistMgr
component and drops resetdps.trn file in DistMgr.box
After the site upgrade finishes successfully, a site reset is initiated to re-install all the
Configuration Manager components. As part of this process, Site Component Manager
(SiteComp) reinstalls Distribution Manager and while reinstalling DistMgr, it creates
resetdps.trn file in DistMgr.box to instruct DistMgr to upgrade all the DPs.

  SMS_SITE_COMPONENT_MANAGER 4364 (0x110c) Reinstalling component
  SMS_DISTRIBUTION_MANAGER...
  SMS_SITE_COMPONENT_MANAGER 4364 (0x110c) Updating DistributionPoints table

<!-- p.154 -->

  SMS_SITE_COMPONENT_MANAGER 4364 (0x110c) Creating
  E:\ConfigMgr\inboxes\distmgr.box\resetdps.trn file.

Step 2: DistMgr starts upgrade of all the DPs after detecting
the resetdps.trn file
DistMgr starts up after reinstallation and detects the resetdps.trn file:

  SMS_DISTRIBUTION_MANAGER 3048 (0xbe8) SMS_EXECUTIVE started
  SMS_DISTRIBUTION_MANAGER as thread ID 4984 (0x1378).
  SMS_DISTRIBUTION_MANAGER 4984 (0x1378) Found file resetdps.trn, will upgrade all the
  Distribution Points

Step 3: DistMgr upgrade processing thread starts DP upgrade
worker threads to perform the DP upgrade
DistMgr upgrade processing thread starts and starts DP upgrade worker threads to upgrade all
the DPs. Each of these worker threads work simultaneously and upgrade multiple DPs at once.
For DP upgrade processing, we can start up to 50 threads by default, however this is a
configurable site control value and is governed by the DPUpgradeThreadLimit property for
SMS_DISTRIBUTION_MANAGER component.

  SMS_DISTRIBUTION_MANAGER 4984 (0x1378) ~Starting the DP upgrade processing
  thread, thread ID = 0x7C (124)
  SMS_DISTRIBUTION_MANAGER 124 (0x7c) DP upgrade processing thread: Started, will
  perform any pending work then will wait for additional work.
  SMS_DISTRIBUTION_MANAGER 124 (0x7c) DP upgrade processing thread: Upgrading DP
  with ID 1. Thread 0x13d0. Used 1 threads out of 50.
  SMS_DISTRIBUTION_MANAGER 124 (0x7c) DP upgrade processing thread: Upgrading DP
  with ID 5. Thread 0x8c8. Used 2 threads out of 50.
  SMS_DISTRIBUTION_MANAGER 124 (0x7c) DP upgrade processing thread: Upgrading DP
  with ID 14. Thread 0x100c. Used 3 threads out of 50.

Each individual DP upgrade worker thread starts upgrading a distribution point. In this
example, we will focus on thread 2248 (0x8c8) which is going to upgrade DP with DPID 5:

  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) ~Processing 5.INS
  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) ~DPID 5 - NAL Path

<!-- p.155 -->

  ["Display=\\PS1SYS.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1SYS.CONTOSO.COM\ , ServerName = PS1SYS.CONTOSO.COM,
  DPDrive = , IsMulticast = 0, PXE = 1, RemoveWDS = 0

Step 4: DP upgrade worker thread performs the DP Upgrade
DP upgrade worker thread performs the upgrade of the DP. This process is identical to the DP
installation process step 8.

  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) Installed ISAPI on PS1SYS.CONTOSO.COM,
  copied E:\ConfigMgr\bin\x64\..\x64\smsfileisapi.dll to
  \\PS1SYS.CONTOSO.COM\ADMIN$\system32\inetsrv\smsfileisapi.dll
  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) DP share SMS_DP$ already exist on the
  remote DP~
  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) Install Internet server= 2
  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) Skipping OS configuration for distribution
  point ["Display=\\PS1SYS.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1SYS.CONTOSO.COM\. You should install and configure IIS manually.
  Please ensure RDC is also enabled.
  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) MSXML 6.0 is configured on DP
  PS1SYS.CONTOSO.COM successfully
  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) Run command
  'C:\SMS_DP$\sms\bin\vcredist_x64.exe /q /norestart /log
  "C:\SMS_DP$\sms\bin\vcredist.log"' to install VC redist
  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) ~Successfully installed DP WMI provider on
  the remote distribution point
  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) Configure IIS virtual directories successfully
  on the distribution point PS1SYS.CONTOSO.COM
  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) ConfigureDP
  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) DP registry settings have been successfully
  updated on PS1SYS.CONTOSO.COM
  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) ConfigurePXE

Step 5: DP upgrade worker threads resets the pull DP installation state

DP upgrade worker thread resets the installation state for the pull DP so that it can be updated.
Note that this is logged even for Standard DPs but isn't relevant for standard DPs.

<!-- p.156 -->

  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) PullDP
  ["Display=\\PS1SYS.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1SYS.CONTOSO.COM\ is marked Uninstalled

Step 6: DP Upgrade finishes successfully
Once the DP installation finishes successfully, the worker thread raises a status message with ID
2399 which means 'Successfully completed the installation or upgrade of the distribution point
on computer <DPNALPath>'.

  SMS_DISTRIBUTION_MANAGER 2248 (0x8c8) STATMSG: ID=2399 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
  SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=3444 TID=2248 GMTDATE=Fri Apr 08
  22:31:56.637 2016 ISTR0="["Display=\\PS1SYS.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1SYS.CONTOSO.COM\" ISTR1="PS1SYS.CONTOSO.COM" ISTR2=""
  ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1
  AID0=404 AVAL0="["Display=\\PS1SYS.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1SYS.CONTOSO.COM\"

Step 7(Pull DPs only): DP worker thread starts instructs DP
WMI Provider to upgrade the pull DP
After the pull DP is marked uninstalled, DP upgrade worker thread instructs DP WMI Provider
to perform the pull DP upgrade.

  SMS_DISTRIBUTION_MANAGER 2032 (0x7f0) ConfigurePullDP
  SMS_DISTRIBUTION_MANAGER 2032 (0x7f0) ~NAL Path
  ["Display=\\PS1SYS.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1SYS.CONTOSO.COM\ is a Pull DP
  SMS_DISTRIBUTION_MANAGER 2032 (0x7f0) For server PS1SYS.CONTOSO.COM processor
  architecture is x64~
  SMS_DISTRIBUTION_MANAGER 2032 (0x7f0) File
  '\\PS1SYS.CONTOSO.COM\SMS_DP$\sms\bin\pulldp.msi' is signed and trusted.
  SMS_DISTRIBUTION_MANAGER 2032 (0x7f0) File
  '\\PS1SYS.CONTOSO.COM\SMS_DP$\sms\bin\pulldp.msi' is signed with MS root cert.
  SMS_DISTRIBUTION_MANAGER 2032 (0x7f0) Installing PullDP, check
  \\PS1SYS.CONTOSO.COM\SMS_DP$\sms\logs\smsdpprov.log and
  \\PS1SYS.CONTOSO.COM\SMS_DP$\sms\logs\pulldp_install.log

<!-- p.157 -->

  SMS_DISTRIBUTION_MANAGER 2032 (0x7f0) PullDP
  ["Display=\\PS1SYS.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1SYS.CONTOSO.COM\ is marked Installed

At this time, the SMSDPProv.log on the pull DP will show that the installation of pull DP has
been initiated:

  2920 (0xb68) Started process F:\SMS_DP$\sms\bin\vcredist_x64.exe /q /norestart /l
  F:\SMS_DP$\sms\logs\vcredist.log
  2920 (0xb68) Run completed for: F:\SMS_DP$\sms\bin\vcredist_x64.exe /q /norestart /l
  F:\SMS_DP$\sms\logs\vcredist.log
  2920 (0xb68) Started process msiexec.exe /quiet /i F:\SMS_DP$\sms\bin\pulldp.msi /log
  F:\SMS_DP$\sms\logs\pulldp_install.log

When pull DP is installed on a server which has the ConfigMgr client installed, the command
used for installation is:

  4744 (0x1288) Started process E:\SMS_DP$\sms\bin\ccmsetup.exe /autoupgrade
  /upgradetolatest
  /postinstallmsi:"E:\SMS_DP$\sms\bin\pulldp.msi;E:\SMS_DP$\sms\logs\pulldp_install.log"

Pull DP installation progress can be reviewed and monitored by looking at the MSI log file
pulldp_install.log.

DP change
The following steps explain what happens when you change properties of a DP in the console.
These steps cover a scenario where DP description was modified in the DP Properties >
General tab from PS1 Standard DP to PS1 Standard DP - TestPropertyChange1.

Step 1: Admin console changes the instance of
SMS_SCI_SysResUse WMI class for the modified DP
After the administrator modifies the DP properties, admin console updates the instance of the
SMS_SCI_SysResUse WMI class within the SMS Provider namespace for the modified DP.

SMSProv.log shows:

<!-- p.158 -->

  SMS Provider 4460 (0x116c) PutInstanceAsync SMS_SCI_SysResUse~
  SMS Provider 4460 (0x116c) CExtProviderClassObject::DoPutInstanceInstance~
  SMS Provider 4460 (0x116c) INFO: 'PS1DP1.CONTOSO.COM' is a valid FQDN.
  SMS Provider 4460 (0x116c) Auditing: User CONTOSO\Admin modified an instance of class
  SMS_SCI_SysResUse.~

When this WMI instance is modified, SMS Provider also updates the database:

 SQL

 update vSMS_SC_SysResUse_Properties set ID = 72057594037928006, Name =
 N'Description', Value1 = N'PS1 Standard DP - TestPropertyChange1', Value2 = N'',
 Value3 = 0 where ID = 72057594037928006 and Name = N'Description'

Step 2: SMSDBMON detects the site control change and
notifies HMAN to process the site control file
SMSDBMON detects a change to the site control file related tables (step 1). On receiving
(denoted as RCV in the log) a change, SMSDBMON takes appropriate action and notifies
appropriate components by dropping/sending (denoted as SND in the log) files in the
component inbox. In this case, SMSDBMON notifies HMAN to process the site control file for
changes.

  SMS_DATABASE_NOTIFICATION_MONITOR 3120 (0xc30) RCV: UPDATE on Sites for
  Sites_AddUpd_HMAN [PS1 ][1031575]
  SMS_DATABASE_NOTIFICATION_MONITOR 3120 (0xc30) SND: Dropped
  E:\ConfigMgr\inboxes\hman.box\PS1.SSU [1031575]

Step 3: HMAN processes the site control file and processes all
DPs
HMAN wakes up to process the SCU file dropped by SMSDBMON, and starts processing the
site control file. During this process, HMAN will look at all distribution points and determine if
any DPs are new or changed. For more details on this step, see step 4 in DP installation.

  SMS_HIERARCHY_MANAGER 4912 (0x1330) ~Processing site control file: Site PS1
  SMS_HIERARCHY_MANAGER 4912 (0x1330) ~Server Info of site PS1 has not
  changed.HMAN will not update the DPInfo table in the database.
  SMS_HIERARCHY_MANAGER 4912 (0x1330) ~Distribution Points of site PS1 have changed.

<!-- p.159 -->

Update the DistributionPoints table in the database.
SMS_HIERARCHY_MANAGER 4912 (0x1330) ~Updated DP
["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\.
DBCRC:151AC30,NewCRC:5EAEB9DF,Action:0,PDP:0,PullDP:0
SMS_HIERARCHY_MANAGER 4912 (0x1330) SQL>>>update DistributionPoints set IsPullDP
= 0, IsPeerDP = 0, SMSSiteCode = 'PS1', IsBITS = 0, PreStagingAllowed = 0, IsMulticast = 0,
AnonymousEnabled = 0, TokenAuthEnabled = 0, SslState = 0, DPType = 0, Priority = 200,
TransferRate = 3972, DPFlags = 0, IsProtected = 1, MinFreeSpace = 50, DPDrive = N'', IsPXE
= 0, IsActive = 0, ResponseDelay = 0, UdaSetting = 0, BindPolicy = 0,
SupportUnknownMachines = 0, CertificateType = 0, IdentityGUID = N'23a72b6c-eace-
4218-929c-4c80638c031e', BindExcept = N'', PXEPassword = N'', Account = N'', Description
= N'PS1 Standard DP - TestPropertyChange1', DPCRC = N'5EAEB9DF', Action = 0 where
NALPath = N'["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\' ~
SMS_HIERARCHY_MANAGER 4912 (0x1330) DP cert query: EXEC spUpdateDPCert
N'PS1DP1.CONTOSO.COM', N'23a72b6c-eace-4218-929c-4c80638c031e', …
SMS_HIERARCHY_MANAGER 4912 (0x1330) ~Will not update DP
["Display=\\PS1SITE.CONTOSO.COM\"]MSWNET:
["SMS_SITE=PS1"]\\PS1SITE.CONTOSO.COM\.
DBCRC:13639BB,NewCRC:13639BB,Action:0,PDP:0,PullDP:0
SMS_HIERARCHY_MANAGER 4912 (0x1330) ~Will not update DP
["Display=\\PS1SQL.CONTOSO.COM\"]MSWNET:
["SMS_SITE=PS1"]\\PS1SQL.CONTOSO.COM\.
DBCRC:DB8F08DA,NewCRC:DB8F08DA,Action:0,PDP:0,PullDP:1
SMS_HIERARCHY_MANAGER 4912 (0x1330) ~Will not update DP
["Display=\\PS1SYS.CONTOSO.COM\"]MSWNET:
["SMS_SITE=PS1"]\\PS1SYS.CONTOSO.COM\.
DBCRC:D9EAF006,NewCRC:D9EAF006,Action:0,PDP:0,PullDP:0

７ Note

If HMAN encounters a failure trying to insert or update any of the DPs, the entire
transaction is rolled back and none of the DPs gets processed. If this continues, you would
see issues where DPs do not get installed, or DP property changes do not take effect.

<!-- p.160 -->

Step 4: HMAN finishes processing the site control file
When HMAN finishes the site control file processing, it raises a status message with ID 3306
which means 'Hierarchy Manager successfully processed
E:\ConfigMgr\inboxes\hman.box\PS1.SCU ', which represented the site control file for site

ConfigMgr Primary Site 1 (PS1).

  SMS_HIERARCHY_MANAGER 4912 (0x1330) STATMSG: ID=3306 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_HIERARCHY_MANAGER"
  SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=4224 TID=4912 GMTDATE=Fri May 13
  16:41:55.881 2016 ISTR0="E:\ConfigMgr\inboxes\hman.box\PS1.SCU" ISTR1="ConfigMgr
  Primary Site 1" ISTR2="PS1" ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8=""
  ISTR9="" NUMATTRS=0

DP removal
The following steps explain what happens after you remove the Distribution Point role for a site
system from the console:

Step 1: Admin console deletes the instance of
SMS_SCI_SysResUse WMI class for the deleted DP

After the administrator removes the Distribution Point role, admin console deletes the instance
of the SMS_SCI_SysResUse WMI class within the SMS Provider namespace for the deleted DP.
SMSProv.log shows:

  SMS Provider 3652 (0xe44) DeleteInstanceAsync
  SMS_SCI_SysResUse.FileType=2,ItemName="
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\,SMS Distribution Point",ItemType="System
  Resource Usage",SiteCode="PS1"~
  SMS Provider 3652 (0xe44) Requested class =SMS_SCI_SysResUse~
  SMS Provider 3652 (0xe44) CExtProviderClassObject::DoDeleteInstance~
  SMS Provider 3652 (0xe44) Auditing: User CONTOSO\Admin deleted an instance of class
  SMS_SCI_SysResUse.~

When this WMI instance is modified, SMS Provider also deletes the DP from the database:
