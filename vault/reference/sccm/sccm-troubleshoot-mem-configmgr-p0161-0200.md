---
title: "Welcome — pages 161-200"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0161-0200
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0161-0200
family: sccm
documentKind: "doc"
abstract: "SQL delete vSMS_SC_SysResUse from vSMS_SC_SysResUse where SiteNumber = 1 and RoleName = N'SMS Distribution Point' and NALPath = N'[\"Display=\\\\PS1DP2.CONTOSO.COM\\\"]MSWNET: [\"SMS_SITE=PS1\"]\\\\PS1DP2.CONTOSO.COM\\' Step 2: SMSDBMON detects the Site Control change and notifies HMAN to"
---

# Welcome — pages 161-200

<!-- p.161 -->

 SQL

 delete vSMS_SC_SysResUse from vSMS_SC_SysResUse where SiteNumber = 1 and RoleName =
 N'SMS Distribution Point' and NALPath = N'["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
 ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\'

Step 2: SMSDBMON detects the Site Control change and
notifies HMAN to process the site control file
SMSDBMON detects a change to the site control file related tables (step 1). On receiving
(denoted as RCV in the log) a change, SMSDBMON takes appropriate action and notifies
appropriate components by dropping/sending (denoted as SND in the log) files in the
component inbox. In this case, SMSDBMON notifies HMAN to process the site control file for
changes.

  SMS_DATABASE_NOTIFICATION_MONITOR 3120 (0xc30) RCV: UPDATE on SiteControl for
  SiteControl_AddUpd_HMAN [PS1 ][1031673]
  SMS_DATABASE_NOTIFICATION_MONITOR 3120 (0xc30) SND: Dropped
  E:\ConfigMgr\inboxes\hman.box\PS1.SCU [1031673]

Step 3: HMAN processes the site control file and marks the DP
as deleted in DistributionPoints table
HMAN wakes up to process the SCU file dropped by SMSDBMON, and starts processing the
site control file. During this process, HMAN detects that the DP role was removed and marks
the DP as Deleted (Action = 3) in the DistributionPoints table, in addition to removing the DP
from the SysResList table. HMAN also inserts a row in the DPNotification table, in order to
provide a DP change notification to SMSDBMON.

  SMS_HIERARCHY_MANAGER 4912 (0x1330) ~Processing site control file: Site PS1
  SMS_HIERARCHY_MANAGER 4912 (0x1330) Site system no longer in use: PS1
  PS1DP2.CONTOSO.COM SMS Distribution Point
  SMS_HIERARCHY_MANAGER 4912 (0x1330) SQL>>> DELETE FROM SysResList WHERE
  SiteCode=N'PS1' AND RoleName=N'SMS Distribution Point' AND
  NALPath=N'["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\'
  SMS_HIERARCHY_MANAGER 4912 (0x1330) ~Distribution Points of site PS1 have changed.
  Update the DistributionPoints table in the database.
  SMS_HIERARCHY_MANAGER 4912 (0x1330) SQL>>>update DistributionPoints set Action =

<!-- p.162 -->

  3, State = 0 where DPID = 34
  SMS_HIERARCHY_MANAGER 4912 (0x1330) SQL>>>delete vSMS_SC_Address from
  vSMS_SC_Address where SiteNumber = 1 and DestinationSiteCode =
  N'PS1DP2.CONTOSO.COM' and AddressType = N'MS_LAN'~
  SMS_HIERARCHY_MANAGER 4912 (0x1330) SQL>>>insert DPNotification (DPID, TimeKey)
  values (34, GetDate())

  ７ Note

  If HMAN encounters a failure trying to insert/update any of the DPs, the entire transaction
  is rolled back and none of the DPs gets processed. If this continues, you would see issues
  where DPs do not get installed, or DP property changes do not take effect.

When HMAN finishes the site control file processing, it raises status message with ID 3306:

  SMS_HIERARCHY_MANAGER 4912 (0x1330) STATMSG: ID=3306 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_HIERARCHY_MANAGER"
  SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=4224 TID=4912 GMTDATE=Fri May 13
  17:43:17.607 2016 ISTR0="E:\ConfigMgr\inboxes\hman.box\PS1.SCU" ISTR1="ConfigMgr
  Primary Site 1" ISTR2="PS1" ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8=""
  ISTR9="" NUMATTRS=0

Step 4: SMSDBMON notifies DistMgr that a DP has changed
for required processing by dropping a DPN file
SMSDBMON detects the change in the DPNotification table and instructs DistMgr to process
the DP change by dropping a <DPID>.DPN file.

  SMS_DATABASE_NOTIFICATION_MONITOR 3120 (0xc30) RCV: INSERT on DPNotification for
  DPNotify_ADD [34 ][1031679]
  SMS_DATABASE_NOTIFICATION_MONITOR 3120 (0xc30) SND: Dropped
  E:\ConfigMgr\inboxes\distmgr.box\34.DPN [1031679]

Step 5: DistMgr uses the DP Manager thread to uninstall the
DP

<!-- p.163 -->

DistMgr uses the DP Manager thread to process the DP change notification and starts
uninstallation of the DP.

DP Manager thread is single-threaded, so if multiple DPs are removed, DistMgr will remove
them one at a time. DP removal consists of the following steps:

     Removal of DP from the database, except DistributionPoints table

     Removal of PXE role (if needed)

     Removal of Monitoring and Usage Scheduled tasks

     Removal of PDP (if needed)

     Removal of DP WMI Provider

     Removal of DP files: SMS_DP$, SCCMContentLib$ and SMSDIG$ shares

     This can take a long time if there's a lot of content in content library.

     Removal of DP virtual directories from IIS

     Removal of DP registry from the DP

  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) ~Created policy provider trigger for ID 34
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) ConfigurePXE
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) ~
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\ is NOT a Pull DP
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Uninstalling distribution point files from
  server PS1DP2.CONTOSO.COM~
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Deleting DP provider classes from server
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Deleted provider classes on distribution point
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Uninstalling distribution point files from
  server PS1DP2.CONTOSO.COM~
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) ~Uninstalling DP provider from remote
  distribution point.
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Unregistering DPProvider on server
  PS1DP2.CONTOSO.COM.
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Removed share SMS_DP$ from server

<!-- p.164 -->

  PS1DP2.CONTOSO.COM
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Failed to remove SMS_DP$ directory with
  error 5, will try to unload distribution point provider and try again.
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Successfully unloaded provider
  SMSDPProvider - root\SCCMDP
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Waiting for provider to be released by COM.
  Timeout is 300 seconds.
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Successfully removed SMS_DP$ directory.
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Removed share SCCMContentLib$ from
  server PS1DP2.CONTOSO.COM
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Removed share SMSSIG$ from server
  PS1DP2.CONTOSO.COM
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) ~Completed uninstalling distribution on the
  remote distribution point
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Deleting DP registry on NAL Path =
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\ , ServerName = PS1DP2.CONTOSO.COM

5a: (Pull DPs only) If the DP being removed is a pull DP, DistMgr detects that and initiates
removal of the pull DP component as well.

  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) ~NAL Path
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\ is a Pull DP
  SMS_DISTRIBUTION_MANAGER 3848 (0xf08) Uninstalling PullDP, check
  \\PS1DP2.CONTOSO.COM\SMS_DP$\sms\logs\smsdpprov.log and
  \\PS1DP2.CONTOSO.COM\SMS_DP$\sms\logs\pulldp_install.log

Finally, the DP is removed from the DistributionPoints table.

 Last updated on 03/30/2026

<!-- p.165 -->

Content library in Configuration Manager
The content library is a new concept that was introduced in System Center 2012 Configuration
Manager. In a nut-shell, the content library stores all of the Configuration Manager content
efficiently on the disk. The content library optimizes disk storage to avoid redistributing a file
that already exists on the distribution points.

For more information, see Understanding the Configuration Manager Content Library .

Original product version: Configuration Manager current branch, Microsoft System Center
2012 Configuration Manager, Microsoft System Center 2012 R2 Configuration Manager

Content Library Explorer
The Content Library Explorer is included in the Configuration Manager Tools. It allows for
exploration of the content library on a specific distribution point. This tool can be used to
troubleshoot issues with the content library, as well as explore its contents. Using the tool,
packages, contents, folders, and files can all be copied out of the content library. Packages can
be redistributed to the distribution point, and on remote distribution points, packages can be
validated.

Usage
ContentLibraryExplorer.exe must be run using an account that has administrative access to the
target distribution point, and access to the WMI provider on the site server and the
Configuration Manager provider. In particular, only the RBAC roles Full Administrator and
Read-Only Analyst have sufficient rights to view all information from this tool. Other roles,
such as Application Administrator, can view partial information (see note below on disabled
packages). The Read-Only Analyst can't redistribute packages from this tool.

The tool can be run from any machine, as long as it can connect to the distribution point, the
primary site server, and the Configuration Manager provider. If the distribution point is
colocated with the site server, it is still necessary to have administrative access to the site
server.

When the application is started, you must enter in the fully qualified domain name (FQDN) of
the target distribution point. The application then connects to the distribution point. If the

<!-- p.166 -->

distribution point is part of a secondary site, you will also be prompted for the FQDN of the
primary site server, and the primary site code.

In the left pane, the packages distributed to this distribution point are visible. They can be
expanded, and their folder structure explored. This will match the folder structure from which
the package was created. When a folder is selected, if it contains any files, these will be listed in
the right pane. Information is provided about file name, file size, the drive it's present on, other
packages that use the same file on the drive, and when the file was last changed on the
distribution point.

The application also connects to the Configuration Manager provider machine, in order to
determine which packages are distributed to the distribution point, whether or not they are
actually in the distribution point's content library. For instance, a package that is pending
distribution may not yet exist in the content library. Such a package would appear as PENDING
in the tool, and no actions will be enabled for this package.

Disabled packages: Some packages are present on the distribution point but not visible in the
Configuration Manager console. These packages are marked with an asterisk (*). No actions
may be done on these packages. Other packages may also be marked with an asterisk and
have actions disabled. Three primary reasons for which might occur:

     The package is the Configuration Manager client upgrade package. This would contain
     ccmsetup.exe.
     The package is not accessible by the running user's RBAC rights. For instance, the
     Application Author role cannot see driver packages in the console, so any driver
     packages on the distribution point will be marked.
     The package is orphaned on the distribution point.

Packages can be validated by using Package > Validate on the tool strip. A package node must
be selected in the left pane, not a content or folder. The tool connects to the WMI provider on
the distribution point to do this. When the tool starts, packages that are missing one or more
contents will be marked invalid. Validating the package will reveal which contents are missing.
If all contents are present but the data is corrupted, validation will detect the corruption.

Additionally, packages can be redistributed using Package > Redistribute on the tool strip.
Again, a package node must be selected in the left pane. This requires permission to
redistribute packages.

Using Edit > Copy, packages, contents, folders, and files can be copied out of the content
library to a specified folder. The content library itself can't be copied. Multiple files can be

<!-- p.167 -->

selected (using Ctrl + click or Shift + click), but multiple folders can't.

Packages can be searched using Edit > Find Package. This will search for your query in the
package name and package ID.

Limitations
     The tool cannot manipulate the content library directly in any way. Changes to the
     content library may result in malfunctions.
     The tool can redistribute packages, but only to the target distribution point.
     When the distribution point is colocated with the site server, package data cannot be
     validated. Use the Configuration Manager console. (It will still inspect to make sure that
     all the package contents are present, though not necessarily intact).
     Content cannot be deleted using this tool.

Content Library Transfer tool
The Content Library Transfer tool transfers content from one disk drive to another. It is
designed to run on distribution point site systems. The tool supports distribution points
colocated with a site or they can be remote.

The tool is useful for the scenario when the disk drive hosting the content library becomes full.
After a hard disk is installed (or identified) with sufficient space to host the content library,
ContentLibraryTransfer.exe is used transfer content from the old filled hard disk to the new
(empty) drive.

Once the transfer is complete, content is now accessible to client computers from the new
location without admin intervention.

Usage
ContentLibraryTransfer.exe must be run as using an account that has administrative
permissions on the distribution point site system.

Syntax

ContentLibraryTransfer.exe -SourceDrive <drive letter of source drive> -TargetDrive

<drive letter of destination drive>

Example

<!-- p.168 -->

ContentLibraryTransfer -SourceDrive E -TargetDrive G

Limitations
     The tool must run locally on the distribution point; it cannot be run from a remote
     machine.
     The tool must run only when the distribution point is not actively being accessed by client
     computers. If the tool is run while client computers are accessing the content, the content
     library on the destination drive may have incomplete data or the data transfer might fail
     altogether leading to an unusable content library.
     The tool must only run when no content is being distributed to the distribution point. If
     the tool is run while content is being written to the distribution point, the content library
     on the destination drive may have incomplete data or the data transfer might fail
     altogether leading to an unusable content library.

Last updated on 03/30/2026

<!-- p.169 -->

Package actions in content distribution
This article helps you understand package actions in content distribution.

Original product version: Configuration Manager current branch, Microsoft System Center
2012 Configuration Manager, Microsoft System Center 2012 R2 Configuration Manager

Introduction
Package actions in content distribution are divided into the following:

     Distribute

     The first major action pertaining to content distribution is the Distribute action. This refers
     to the initial distribution of a package to a distribution point. This is triggered by the
     Distribute Content wizard in the Configuration Manager console. This will transfer all files
     in a package to the target distribution points, excluding those which are already present
     in the content library of the DP as part of another package. If the package contains any
     files that are already in the content library on the distribution point, those files are shared
     between multiple packages.

     Update

     The second major action is the Update action. This is typically used when a package has
     been changed and all distribution points to which it is distributed need the updated
     content. This is triggered with Update Distribution Points action in the console. This will
     transfer the changed files to all distribution points. Unchanged files will not be
     transferred. If a file is removed from the package in the updated version, it will be deleted
     from the package on the distribution point (as long as no other packages that share the
     file are on the DP).

     Redistribute

     The third major action is the Redistribute action, triggered with Redistribute in the
     Configuration Manager console. This will transfer the entire content to a specific
     distribution point. Files will be transferred and overwritten even if they are already present
     in the content library on the distribution point. The primary purpose of the Redistribute
     action is to correct any inconsistencies that may exist in the content library.

<!-- p.170 -->

Create a package
The following steps explain the flow of events when you create a new package from the
administrator console that hasn't been distributed to any DPs yet:

Step 1: Admin console creates an instance of the
SMS_PackageWMI class

After the administrator creates the package in the console, admin console creates an instance
of the SMS_Package WMI class within the SMS Provider namespace for the newly created
package. SMSProv.log shows the following:

  SMS Provider 4680 (0x1248) CExtProviderClassObject::DoPutInstanceInstance~
  SMS Provider 4680 (0x1248) Auditing: User CONTOSO\Admin created an instance of class
  SMS_Package.~
  SMS Provider 816 (0x330) Processed insert instance notification for:
  SMS_Package.PackageID="PackageID"~

When this WMI instance is created, SMS Provider inserts a row in the SMSPackages view in the
database:

 SQL

 insert SMSPackages (PkgID, Name, Version, Language, Manufacturer, Description,
 ISVString, Hash, NewHash, Source, SourceSite, StoredPkgPath, RefreshSchedule,
 LastRefresh, StoredPkgVersion, ShareName, PreferredAddress, StorePkgFlag,
 ShareType, HashVersion,Architecture, ImagePath,Permission, UseForcedDisconnect,
 ForcedRetryDelay, DisconnectDelay, IgnoreSchedule, Priority, PkgFlags, MIFFilename,
 MIFPublisher, MIFName, MIFVersion, SourceVersion, SourceDate, SourceSize,
 SourceCompSize, ImageFlags, PackageType, AlternateContentProviders, SourceLocaleID,
 TransformReadiness, TransformAnalysisDate, UpdateMask, UpdateMaskEx, Action,
 DefaultImage) values (N'PackageID', N'Dummy1', N'',
 N'',N'',N'',N'',N'',N'',N'\\CS1SITE\SOURCE\Packages\Dummy1',N'CS1',N'',N'',N'04/10/
 1970 06:35:00', 0, N'',N'', 2, 1, 1, N'', N'', 15, 0, 2, 5, 0, 2, 16777216,
 N'',N'',N'',N'', 1, N'05/16/2016 15:22:12', 0, 0, 0, 0, N'', 1033, 0, N'1980/01/01
 00:00:00', 0, 0, 2, 0)

After the row is inserted, a trigger on the view inserts a row in SMSPackages_G and
SMS_Packages_L tables. This in turn causes a trigger on the SMSPackages_G table to insert a row

in PkgNotification table. The row in the PkgNotification table is used to notify DistMgr to
process the package, and this notification is provided to DistMgr by the SMSDBMON component.

<!-- p.171 -->

 SQL

 insert PkgNotification (PkgID, Priority, Type, TimeKey) values (N'PackageID', 2, 2,
 GetDate())

Step 2: SMSDBMON detects a change and notifies DistMgr to
process the package by dropping a <PackageID>.PKN file
SMSDBMON detects a change in the PkgNotification table, which causes it to drop a
<PackageID>.PKN file in DistMgr.box to instruct DistMgr to process the package:

  SMS_DATABASE_NOTIFICATION_MONITOR 3240 (0xca8) RCV: INSERT on PkgNotification
  for PkgNotify_Add [<PackageID>][850902]
  SMS_DATABASE_NOTIFICATION_MONITOR 3240 (0xca8) SND: Dropped
  E:\ConfigMgr\inboxes\distmgr.box\<PackageID>.PKN [850902]

Step 3: DistMgr processes the package on the package source
site
DistMgr processes the package after detecting the PKN file in DistMgr.box . DistMgr processing
is performed by multiple threads.

   1. The main DistMgr thread creates a package processing thread.

     Main DistMgr thread wakes up, adds the package to the package processing queue and
     creates a package processing thread to process the package:

       SMS_DISTRIBUTION_MANAGER 2624 (0xa40) Found package properties updated
       notification for package 'PackageID'
       SMS_DISTRIBUTION_MANAGER 2624 (0xa40) Adding package 'PackageID' to package
       processing queue.
       SMS_DISTRIBUTION_MANAGER 2624 (0xa40) ~Currently using 0 out of 3 allowed
       package processing threads.
       SMS_DISTRIBUTION_MANAGER 2624 (0xa40) ~Started package processing thread for
       package 'PackageID', thread ID = 0x16A8 (5800)

   2. The package processing thread creates a package snapshot and writes content in the
     content library.

<!-- p.172 -->

The package processing thread (thread ID 5800 in this case) starts processing the package
and creates a package snapshot. After creating the package snapshot, this thread also
writes the package content to the content library on the site server.

  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) STATMSG: ID=2300 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
  SYS=CS1SITE.CONTOSO.COM SITE=CS1 PID=1904 TID=5800 GMTDATE=Mon May 16
  14:33:55.691 2016 ISTR0="Dummy1" ISTR1="<PackageID>" ISTR2="" ISTR3=""
  ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=400
  AVAL0="<PackageID>"
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) ~Processing package <PackageID>
  (SourceVersion:1;StoredVersion:0)
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) Start adding package <PackageID>...
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) ~The Package Action is 2, the Update
  Mask is 0 and UpdateMaskEx is 0.
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8)
  ~CDistributionSrcSQL::UpdateAvailableVersion PackageID=<PackageID>, Version=1,
  Status=2300
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) Taking package snapshot for package
  <PackageID> from source \\CS1SITE\SOURCE\Packages\Dummy1
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) The size of package <PackageID>,
  version 1 is 204800 KBytes
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) Writing package definition for
  <PackageID>
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) ~Successfully created RDC signatures
  for package PackageID version 1
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) Creating hash for algorithm 32780
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) The hash for algorithm 32780 is
  <HashString>
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) The RDC signature hash for algorithm
  32780 is <HashString>
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) ~Adding these contents to the
  package PackageID version 1.
  SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) STATMSG: ID=2376 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
  SYS=CS1SITE.CONTOSO.COM SITE=CS1 PID=1904 TID=5800 GMTDATE=Mon May 16
  14:34:04.611 2016 ISTR0="<PackageID>" ISTR1="" ISTR2="" ISTR3="" ISTR4=""

<!-- p.173 -->

    ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=400 AVAL0="
    <PackageID>"

3. The package processing thread replicates the package to other sites.

  The package processing thread then replicates the package to the other sites in the
  hierarchy. Package metadata information is replicated to other sites via database
  replication, while package files are replicated using file replication. However, package files
  are only sent to a site if at least one DP in that site is added to the package. Package files
  are compressed before they are sent to another site. In this case, since no DPs are
  targeted, only package metadata is replicated to other sites but package files are not
  replicated.

    SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) ~Package <PackageID> does not have
    a preferred sender.
    SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) A program for package <PackageID>
    has been added or removed, therefore it needs to be replicated to all child sites.
    SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) Package <PackageID> is new or has
    changed, replicating to all applicable sites.
    SMS_DISTRIBUTION_MANAGER 5800 (0x16a8)
    ~CDistributionSrcSQL::UpdateAvailableVersion PackageID=<PackageID>, Version=1,
    Status=2301
    SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) ~StoredPkgVersion (1) of package
    <PackageID>. StoredPkgVersion in database is 1.
    SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) ~SourceVersion (1) of package
    <PackageID>. SourceVersion in database is 1.
    SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) ~Adding these contents to the
    package <PackageID> version 1.

4. The package processing thread exits.

  The package processing thread exits after the package processing is complete and raises
  a status message with ID 2301 which means 'Distribution Manager successfully processed
  package <PACKAGENAME> (package ID = <PKGID>).'

    SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) STATMSG: ID=2301 SEV=I LEV=M
    SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
    SYS=CS1SITE.CONTOSO.COM SITE=CS1 PID=1904 TID=5800 GMTDATE=Mon May 16
    14:34:06.736 2016 ISTR0="Dummy1" ISTR1="<PackageID>" ISTR2="" ISTR3=""

<!-- p.174 -->

       ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=400
       AVAL0="<PackageID>"
       SMS_DISTRIBUTION_MANAGER 5800 (0x16a8) ~Exiting package processing thread
       for package <PackageID>.

Step 4: (If applicable) DRS replicates the package to other
sites
If there are other sites in the hierarchy, package metadata information is replicated to other
sites via database replication. After the package information is replicated, a row in the
SMSPackages_G table is inserted which triggers an insert in the PkgNotification table.

Step 5: (If applicable) SMSDBMON on the receiving site notifies DistMgr
by dropping a <PackageID>.PKN file

On the receiving site, SMSDBMON detects a change in the PkgNotification table which causes
it to drop a <PackageID>.PKN file in DistMgr.box to instruct DistMgr to process the package:

  SMS_DATABASE_NOTIFICATION_MONITOR 3120 (0xc30) RCV: INSERT on PkgNotification
  for PkgNotify_Add [<PackageID> ][1035019]
  SMS_DATABASE_NOTIFICATION_MONITOR 3120 (0xc30) SND: Dropped
  E:\ConfigMgr\inboxes\distmgr.box\<PackageID>.PKN [1035019]

Step 6: (If applicable) DistMgr on the receiving site processes
the package
On the receiving site, after receiving the .PKN file, DistMgr wakes up to process the package.

   1. The main DistMgr thread creates a package processing thread.

     The main DistMgr thread adds the package to the package processing queue and creates
     a package processing thread:

       SMS_DISTRIBUTION_MANAGER 3648 (0xe40) Found package properties updated
       notification for package '<PackageID>'
       SMS_DISTRIBUTION_MANAGER 3648 (0xe40) Adding package '<PackageID>' to
       package processing queue.
       SMS_DISTRIBUTION_MANAGER 3648 (0xe40) ~Currently using 0 out of 3 allowed
       package processing threads.

<!-- p.175 -->

    SMS_DISTRIBUTION_MANAGER 3648 (0xe40) ~Started package processing thread for
    package '<PackageID>', thread ID = 0x1378 (4984)

2. The package processing thread processes the package.

  In this case, there's nothing for this thread to do since no DPs have been targeted.

    SMS_DISTRIBUTION_MANAGER 4984 (0x1378) STATMSG: ID=2300 SEV=I LEV=M
    SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
    SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=4224 TID=4984 GMTDATE=Mon May 16
    14:36:08.809 2016 ISTR0="Dummy1" ISTR1="<PackageID>" ISTR2="" ISTR3=""
    ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=400
    AVAL0="<PackageID>"
    SMS_DISTRIBUTION_MANAGER 4984 (0x1378) ~Processing package <PackageID>
    (SourceVersion:1;StoredVersion:0)
    SMS_DISTRIBUTION_MANAGER 4984 (0x1378) Start adding package <PackageID>...
    SMS_DISTRIBUTION_MANAGER 4984 (0x1378) ~The Package Action is 2, the Update
    Mask is 0 and UpdateMaskEx is 0.
    SMS_DISTRIBUTION_MANAGER 4984 (0x1378) ~Successfully created/updated the
    package <PackageID>
    SMS_DISTRIBUTION_MANAGER 4984 (0x1378) STATMSG: ID=2311 SEV=I LEV=M
    SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
    SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=4224 TID=4984 GMTDATE=Mon May 16
    14:36:09.486 2016 ISTR0="PackageID" ISTR1="" ISTR2="" ISTR3="" ISTR4="" ISTR5=""
    ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=400 AVAL0="
    <PackageID>"
    SMS_DISTRIBUTION_MANAGER 4984 (0x1378) ~Created policy provider trigger for ID
    <PackageID>
    SMS_DISTRIBUTION_MANAGER 4984 (0x1378) ~Package <PackageID> does not have
    a preferred sender.
    SMS_DISTRIBUTION_MANAGER 4984 (0x1378)
    ~CDistributionSrcSQL::UpdateAvailableVersion PackageID=<PackageID>, Version=1,
    Status=2301
    SMS_DISTRIBUTION_MANAGER 4984 (0x1378) ~StoredPkgVersion (0) of package
    <PackageID>. StoredPkgVersion in database is 0.
    SMS_DISTRIBUTION_MANAGER 4984 (0x1378) ~SourceVersion (1) of package
    <PackageID>. SourceVersion in database is 1.
    SMS_DISTRIBUTION_MANAGER 4984 (0x1378) STATMSG: ID=2301 SEV=I LEV=M

<!-- p.176 -->

         SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
         SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=4224 TID=4984 GMTDATE=Mon May 16
         14:36:10.061 2016 ISTR0="Dummy1" ISTR1="<PackageID>" ISTR2="" ISTR3=""
         ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=400
         AVAL0="<PackageID>"
         SMS_DISTRIBUTION_MANAGER 4984 (0x1378) ~Exiting package processing thread
         for package <PackageID>.

Distribute a package to DP across sites
The following steps outline the flow of events when a package is distributed to a DP in the
primary site but the primary site server in question does not contain a copy of this package in
the content library. This package was created on the central administration site and as a result,
the central administration site is the package source site:

On the package source site
Step 1: The admin console adds the DP to the package by calling the
AddDistributionPoints method on the SMS_PackageWMI class

After the administrator distributes the package to a DP from the console, the admin console
calls the AddDistributionPoints method of the SMS_Package class to add the specified DP to
the package. SMSProv.log shows the following:

  SMS Provider 4616 (0x1208) Context: SMSAppName=Configuration Manager
  Administrator console~
  SMS Provider 4616 (0x1208) ExecMethodAsync : SMS_Package.PackageID="
  <PackageID>"::AddDistributionPoints~
  SMS Provider 4616 (0x1208) CExtProviderClassObject::DoExecuteMethod
  AddDistributionPoints~
  SMS Provider 4616 (0x1208) Auditing: User CONTOSO\Admin called an audited method of
  an instance of class SMS_Package.~

When this method is called, SMS Provider inserts a row in PkgServers with Action set to 2
(ADD).

 SQL

 insert PkgServers (PkgID, NALPath, SiteCode, SiteName, SourceSite, LastRefresh,
 RefreshTrigger, UpdateMask, Action) select N'PackageID',

<!-- p.177 -->

 N'['Display=\\PS1SITE.CONTOSO.COM\']MSWNET:['SMS_SITE=PS1']\\PS1SITE.CONTOSO.COM\',
 N'PS1', Sites.SiteName, N'CS1', N'04/10/1970 06:35:00', 0, 0, 2 from Sites where
 SiteCode = N'PS1'

After a row is inserted in PkgServers , SMS Provider also inserts a row in the PkgNotification
table. The row in the PkgNotification table is used to notify DistMgr to process the package,
and this notification is provided to DistMgr by the SMSDBMON component.

 SQL

 insert PkgNotification (PkgID, Priority, Type, TimeKey) values (N'PackageID', 2, 4,
 GetDate())

Step 2: SMSDBMON detects the package change and notifies DistMgr by
dropping a <PackageID>.PKN file in DistMgr.box

SMSDBMON detects a change in the PkgNotification table that causes it to drop a
<PackageID>.PKN file in DistMgr.box to instruct DistMgr to process the package.

  SMS_DATABASE_NOTIFICATION_MONITOR 4944 (0x1350) RCV: INSERT on PkgNotification
  for PkgNotify_Add [<PackageID> ][850967]
  SMS_DATABASE_NOTIFICATION_MONITOR 4944 (0x1350) SND: Dropped
  E:\ConfigMgr\inboxes\distmgr.box\<PackageID>.PKN [850967]

Step 3: DistMgr wakes up to process the package after receiving the
PKN file

   1. The main DistMgr thread creates the package processing thread.

     The main DistMgr thread adds the package to the package processing queue and creates
     a package processing thread.

       SMS_DISTRIBUTION_MANAGER 2496 (0x9c0) Adding package '<PackageID>' to
       package processing queue.
       SMS_DISTRIBUTION_MANAGER 2496 (0x9c0) ~Currently using 0 out of 3 allowed
       package processing threads.
       SMS_DISTRIBUTION_MANAGER 2496 (0x9c0) ~Started package processing thread for
       package '<PackageID>', thread ID = 0x1164 (4452)

   2. The package processing thread processes the package actions.

<!-- p.178 -->

  The package processing thread processes the package actions to add/update/remove the
  package from the DP. In this case, the package source site is the central administration
  site and there are no package actions to process because the central administration site
  contains no DPs. On a site where there are package actions to process, the package
  processing thread creates DP threads for performing these actions and waits for the DP
  threads to exit before moving on to Step 3-3.

    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) ~Processing package <PackageID>
    (SourceVersion:1;StoredVersion:1)
    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) No action specified for the package
    <PackageID>, however there may be package server changes for this package.

3. The package processing thread creates a mini-job to send the compressed copy of the
  package to the destination site.

  This mini-job is processed by the scheduler to create a send request for Sender to
  transfer the compressed copy of the package to the destination site:

    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) ~Package <PackageID> does not have
    a preferred sender.
    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) ~Needs to send the compressed
    package for package <PackageID> to site PS1
    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) ~Sending a copy of package
    <PackageID> to site PS1
    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) ~The reporting site of site PS1 is this
    site.
    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) ~Use drive E for storing the
    compressed package.
    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) ~Setting CMiniJob transfer root to
    E:\SMSPKG\<PackageID>.PCK.1
    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) Incremented ref count on file
    E:\SMSPKG\<PackageID>.PCK.1, count = 2
    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) Decremented ref count on file
    E:\SMSPKG\<PackageID>.PCK.1, count = 1
    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) ~Created minijob to send
    compressed copy of package <PackageID> to site PS1. Transfer root = E:\SMSPKG\
    <PackageID>.PCK.1.
    SMS_DISTRIBUTION_MANAGER 4452 (0x1164) The package and/or program

<!-- p.179 -->

       properties for package <PackageID> have not changed, need to determine which
       site(s) need updated package info.
       SMS_DISTRIBUTION_MANAGER 4452 (0x1164) A distribution point has been changed
       at this site, adding site PS1 to the list of sites to which we are sending package
       <PackageID>.
       SMS_DISTRIBUTION_MANAGER 4452 (0x1164) Parent site of PS1 is CS1

   4. The package processing thread exits after processing the package:

       SMS_DISTRIBUTION_MANAGER 4452 (0x1164) ~StoredPkgVersion (1) of package
       <PackageID>. StoredPkgVersion in database is 1.
       SMS_DISTRIBUTION_MANAGER 4452 (0x1164) ~SourceVersion (1) of package
       <PackageID>. SourceVersion in database is 1.
       SMS_DISTRIBUTION_MANAGER 4452 (0x1164) ~Exiting package processing thread
       for package <PackageID>.

Step 4: The scheduler component processes the mini-job created by the
package processing thread and creates a send request

The scheduler component wakes up after receiving a job to transfer the compressed copy of
the package, and creates a send request for Sender so that Sender can send the compressed
copy to the destination site.

  SMS_SCHEDULER 5492 (0x1574) ======== Processing Jobs ========
  SMS_SCHEDULER 5492 (0x1574) <Activating JOB JOBID>[Software Distribution for
  Dummy1, Package ID = <PackageID>]~
  SMS_SCHEDULER 5492 (0x1574) Destination site: PS1, Preferred Address: *, Priority: 2
  SMS_SCHEDULER 5492 (0x1574) Instruction type:
  MICROSOFT|SMS|MINIJOBINSTRUCTION|PACKAGE~
  SMS_SCHEDULER 5492 (0x1574) Creating instruction file:
  \\CS1SITE.CONTOSO.COM\SMS_CS1\inboxes\schedule.box\tosend\JOBID.Icl~
  SMS_SCHEDULER 5492 (0x1574) Transfer root: E:\SMSPKG\<PackageID>.PCK.1~
  SMS_SCHEDULER 5492 (0x1574) <Updating JOB JOBID>[Software Distribution for
  Dummy1, Package ID = <PackageID>]~
  SMS_SCHEDULER 5492 (0x1574) Created new send request ID: 202SQCS1~

The scheduler will periodically update the send requests and will log useful information about
the send requests which includes total size and remaining size:

<!-- p.180 -->

  SMS_SCHEDULER 5492 (0x1574) ====== Updating Send Request List =======
  SMS_SCHEDULER 5492 (0x1574) Send Request 202SQCS1 JobID: JOBID DestSite: PS1
  FinalSite: State: Pending Status: Action: None Total size: 204864k Remaining: 204864k
  Heartbeat: 12:23 Start: 12:00 Finish: 12:00 Retry: SWD PkgID: <PackageID> SWD Pkg
  Version: 1

Step 5: The sender component starts working on the send request

The sender component processes the send request and sends the compressed copy of the
package to the destination site.

   1. The main sender thread starts a sending thread which is the thread that will perform all
     the work for this send request.

       SMS_LAN_SENDER 6700 (0x1a2c) Found send request. ID: 202SQCS1, Dest Site: PS1~
       SMS_LAN_SENDER 6700 (0x1a2c) Checking for site-specific sending capacity. Used 0
       out of 3.~
       SMS_LAN_SENDER 6700 (0x1a2c) ~Created sending thread (Thread ID = 1150)

   2. The sending thread processes the send request and copies the compressed package file
     (PCK file) to the destination site along with the package instruction file (SNI file).

       SMS_LAN_SENDER 4432 (0x1150) ~Trying the No. 1 address (out of 1)
       SMS_LAN_SENDER 4432 (0x1150) ~Passed the xmit file test, use the existing
       connection
       SMS_LAN_SENDER 4432 (0x1150) ~Package file = E:\SMSPKG\<PackageID>.PCK.1
       SMS_LAN_SENDER 4432 (0x1150) ~Instruction file =
       E:\ConfigMgr\inboxes\schedule.box\tosend\00000E2A.Icl
       SMS_LAN_SENDER 4432 (0x1150) ~Checking for remote file
       \\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.PCK
       SMS_LAN_SENDER 4432 (0x1150) ~Checking for remote file
       \\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.SNI
       SMS_LAN_SENDER 4432 (0x1150) ~Checking for remote file
       \\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.TMP …
       SMS_LAN_SENDER 4432 (0x1150) ~Attempt to create/open the remote file
       \\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.PCK
       SMS_LAN_SENDER 4432 (0x1150) ~Created/opened the remote file
       \\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.PCK

<!-- p.181 -->

     SMS_LAN_SENDER 4432 (0x1150) ~Sending Started [E:\SMSPKG\<PackageID>.PCK.1]
     SMS_LAN_SENDER 4432 (0x1150) ~Attempt to write 1024 bytes to
     \\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.PCK at position 0
     SMS_LAN_SENDER 4432 (0x1150) ~Wrote 1024 bytes to
     \\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.PCK at position 0 …
     SMS_LAN_SENDER 4432 (0x1150) ~Attempt to write 380731 bytes to
     \\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.PCK at position 209398784
     SMS_LAN_SENDER 4432 (0x1150) ~Wrote 380731 bytes to
     \\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.PCK at position 209398784
     SMS_LAN_SENDER 4432 (0x1150) ~Sending completed [E:\SMSPKG\
     <PackageID>.PCK.1]
     SMS_LAN_SENDER 4432 (0x1150) ~Finished sending SWD package <PackageID>
     version 1 to site PS1 …
     SMS_LAN_SENDER 4432 (0x1150) ~Sending Started
     [E:\ConfigMgr\inboxes\schedule.box\tosend\00000E2A.Icl]
     SMS_LAN_SENDER 4432 (0x1150) ~Sending completed
     [E:\ConfigMgr\inboxes\schedule.box\tosend\00000E2A.Icl]
     SMS_LAN_SENDER 4432 (0x1150) ~Finished sending SWD package <PackageID>
     version 1 to site PS1 …
     SMS_LAN_SENDER 4432 (0x1150) ~Renaming remote file
     \\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.TMP to
     \\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.SNI
     MS_LAN_SENDER 4432 (0x1150) ~Rename completed
     [\\PS1SITE.CONTOSO.COM\SMS_SITE\202SQCS1.TMP]
     SMS_LAN_SENDER 4432 (0x1150) ~Sending completed successfully

   The sending thread copies these files to the SMS_SITE share on the receiving site.

      Tip

     The sender.log file continuously logs the position it's writing to. For example, the
     position is 209398784 in the above log. This position is the byte offset it's writing to,
     and you can find how much data has been copied by converting this value. For
     example, 209398784 bytes = 199.69 MB.

Step 6: The scheduler component marks the job as completed and
deletes the send request

<!-- p.182 -->

The scheduler component monitors the send requests, and after Sender has finished
processing the send request, Scheduler marks the job as complete and deletes the send
request:

  SMS_SCHEDULER 5492 (0x1574) ====== Checking Status of All Send Requests ======
  SMS_SCHEDULER 5492 (0x1574) ~==== Checking send requests for outbox
  \\CS1SITE.CONTOSO.COM\SMS_CS1\inboxes\schedule.box\outboxes\LAN.~~
  SMS_SCHEDULER 5492 (0x1574) Checking send request 202SQCS1~
  SMS_SCHEDULER 5492 (0x1574) Sending completed (13985442 bytes/sec).~
  SMS_SCHEDULER 5492 (0x1574) <Updating JOB JOBID>[Software Distribution for
  Dummy1, Package ID = <PackageID>]~
  SMS_SCHEDULER 5492 (0x1574) Send request has successfully completed.~
  SMS_SCHEDULER 5492 (0x1574) <JOB STATUS - COMPLETE>~
  SMS_SCHEDULER 5492 (0x1574) Deleting instruction file
  \\CS1SITE.CONTOSO.COM\SMS_CS1\inboxes\schedule.box\tosend\00000E2A.Icl.~
  SMS_SCHEDULER 5492 (0x1574) Deleting job package source [E:\SMSPKG\
  <PackageID>.PCK.1].~
  SMS_SCHEDULER 5492 (0x1574) Deleted reference counted file E:\SMSPKG\
  <PackageID>.PCK.1
  SMS_SCHEDULER 5492 (0x1574) Decremented ref count on file E:\SMSPKG\
  <PackageID>.PCK.1, count = 0
  SMS_SCHEDULER 5492 (0x1574) Deleting send request with ID: 202SQCS1.~
  SMS_SCHEDULER 5492 (0x1574) Deleted job JOBID.~

After this step, the sending site has no more work to do and the receiving site starts the
processing of the package.

On the destination site
Step 7: Despooler processes the PCK and SNI files

During Step 5, PCK and SNI files were copied to the SMS_SITE share on the receiving site. On
each Configuration Manager site, the \inboxes\despoolr.box\receive folder is shared as
SMS_SITE . When these files arrive in the despoolr.box\receive folder, the despooler component

wakes up to process the SNI file which is an instruction file.

   1. The main despooler thread creates a despooling thread.

<!-- p.183 -->

  Main Despooler finds the instruction file and creates a despooling thread to process the
  instruction file:

    SMS_DESPOOLER 6128 (0x17f0) ~Found ready instruction 202sqcs1.sni
    SMS_DESPOOLER 6128 (0x17f0) ~Used 0 out of 3 despooling threads
    SMS_DESPOOLER 6128 (0x17f0) ~Created a new despooling thread EE8

2. (Sporadically) Despooling thread sometimes fails to process instruction on first attempt
  and retries after 5 minutes.

  The despooling thread processes the instruction file, however in many cases, the first-
  time despooler tries to process an instruction file for a package it will fail with a 'package
  information hasn't arrived yet for this version' message because the package metadata
  information hasn't yet replicated to the receiving site. When this happens, despooler.log
  shows 'error code = 12' but retries this instruction after five minutes, which is successful as
  the package information replicates during this time. Step 7-3 shows the successful
  processing of the instruction on retry.

    SMS_DESPOOLER 3816 (0xee8) ~Verifying signature for instruction
    E:\ConfigMgr\inboxes\despoolr.box\receive\ds_s76nc.ist of type
    MICROSOFT|SMS|MINIJOBINSTRUCTION|PACKAGE
    SMS_DESPOOLER 3816 (0xee8) ~Signature checked out OK for instruction coming
    from site CS1, proceed with the instruction execution.
    SMS_DESPOOLER 3816 (0xee8) ~Executing instruction of type
    MICROSOFT|SMS|MINIJOBINSTRUCTION|PACKAGE
    SMS_DESPOOLER 3816 (0xee8) ~Received package PackageID version 1. Compressed
    file - E:\SMSPKG\<PackageID>.PCK.1 as
    E:\ConfigMgr\inboxes\despoolr.box\receive\ds_s76nc.pkg
    SMS_DESPOOLER 3816 (0xee8) ~Old package storedUNC path is .
    SMS_DESPOOLER 3816 (0xee8) ~This package[<PackageID>]'s information hasn't
    arrived yet for this version [1]. Retry later ...
    SMS_DESPOOLER 3816 (0xee8) ~Created retry instruction for job JOBID
    SMS_DESPOOLER 3816 (0xee8) ~Despooler failed to execute the instruction, error
    code = 12 …
    SMS_DESPOOLER 6128 (0x17f0) ~Instruction
    E:\ConfigMgr\inboxes\despoolr.box\receive\ds_3kyyh.sni won't be processed till
    5/16/2016 12:29:11 PM Eastern Daylight Time

<!-- p.184 -->

  If this happens, DistMgr will try to process the package, however since the compressed
  copy of the package hasn't been processed and extracted into the content library, the
  package processing thread will log the following and exit:

    SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) ~Started package processing thread
    for package '<PackageID>', thread ID = 0xAAC (2732)
    SMS_DISTRIBUTION_MANAGER 2732 (0xaac) ~Processing package <PackageID>
    (SourceVersion:1;StoredVersion:0)
    SMS_DISTRIBUTION_MANAGER 2732 (0xaac) ~The contents for the package
    <PackageID> hasn't arrived from site CS1 yet, will retry later.
    SMS_DISTRIBUTION_MANAGER 2732 (0xaac) ~All DP threads have completed for
    package <PackageID> processing thread.
    SMS_DISTRIBUTION_MANAGER 2732 (0xaac) ~Exiting package processing thread for
    package <PackageID>.

3. The despooling thread processes the instruction and writes content to the content library.

  The despooling thread processes the instruction, uncompresses the PCK file to a temp
  location, then writes the content to the content library.

    SMS_DESPOOLER 4072 (0xfe8) ~Received package <PackageID> version 1.
    Compressed file - E:\SMSPKG\<PackageID>.PCK.1 as
    E:\ConfigMgr\inboxes\despoolr.box\receive\PKGj3uib.TRY
    SMS_DESPOOLER 4072 (0xfe8) ~Old package storedUNC path is .
    SMS_DESPOOLER 4072 (0xfe8) ~Use drive E for storing the compressed package.
    SMS_DESPOOLER 4072 (0xfe8) No branch cache registry entries found.
    SMS_DESPOOLER 4072 (0xfe8) Uncompressing E:\SMSPKG\<PackageID>.PCK to
    E:\SMSPKG\<PackageID>.PCK.temp
    SMS_DESPOOLER 4072 (0xfe8) Content Library: E:\SCCMContentLib
    SMS_DESPOOLER 4072 (0xfe8) Extracting from E:\SMSPKG\<PackageID>.PCK.temp
    SMS_DESPOOLER 4072 (0xfe8) Extracting package <PackageID>
    SMS_DESPOOLER 4072 (0xfe8) Extracting content <PackageID>.1
    SMS_DESPOOLER 4072 (0xfe8) Writing package definition for <PackageID>
    SMS_DESPOOLER 4072 (0xfe8) ~Package <PackageID> (version 0) exists in the
    distribution source, save the newer version (version 1).
    SMS_DESPOOLER 4072 (0xfe8) ~Stored Package <PackageID>. Stored Package
    Version = 1

<!-- p.185 -->

     After successfully extracting the content to the content library, despooler updates
     StoredPkgVersion in the SMSPackages_L table and inserts a row in the PkgNotification

     table so that DistMgr can be notified to process the package.

      SQL

      update SMSPackages_L set StoredPkgPath = N'\\PS1SITE.CONTOSO.COM\E$\SMSPKG\
      <PackageID>.PCK', StoredPkgVersion = 1, UpdateMask = 160, UpdateMaskEx = 0,
      Action = 1 where PkgID = N'<PackageID>'
      insert PkgNotification (PkgID, Priority, Type, TimeKey) values
      (N'<PackageID>', 2, 1, GetDate())

  4. The despooling thread updates the Type 1 row for the receiving site in PkgStatus , raises a
     status message with ID 4400 and then exits.

      SQL

      update PkgStatus set Status = 2, UpdateTime = N'Date Time', Location =
      N'\\PS1SITE.CONTOSO.COM\E$\SMSPKG\PackageID.PCK', ShareName = N'', HTTPUrl =
      N'', SourceVersion = 1, Personality = 0, State = 0, SigURL = N'', SigLocation
      = N'' where ID = N'PackageID' and Type = 1 and SiteCode = N'PS1' and PkgServer
      = N'PS1SITE.CONTOSO.COM'

       SMS_DESPOOLER 4072 (0xfe8) STATMSG: ID=4400 SEV=I LEV=M SOURCE="SMS
       Server" COMP="SMS_DESPOOLER" SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428
       TID=4072 GMTDATE=Mon May 16 16:31:21.400 2016 ISTR0="<PackageID>"
       ISTR1="\\PS1SITE.CONTOSO.COM\E$\SMSPKG\<PackageID>.PCK" ISTR2="" ISTR3=""
       ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=400
       AVAL0="<PackageID>"
       SMS_DESPOOLER 4072 (0xfe8) ~Despooler successfully executed one instruction.

Step 8: SMSDBMON notifies DistMgr to process the package

SMSDBMON detects a change in the PkgNotification table and drops a PKN file in
DistMgr.box to instruct DistMgr to process the package.

  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) RCV: INSERT on PkgNotification
  for PkgNotify_Add [<PackageID> ][1035289]
  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) SND: Dropped
  E:\ConfigMgr\inboxes\distmgr.box\<PackageID>.PKN [1035289]

Step 9: DistMgr wakes up to process the package

<!-- p.186 -->

DistMgr wakes up after detecting the PKN file and processes the package.

  1. The main DistMgr thread creates a package processing thread.

     The main DistMgr thread adds the package to the package processing queue and creates
     a package processing thread.

       SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) Found package properties updated
       notification for package '<PackageID>'
       SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) Adding package '<PackageID>' to
       package processing queue.
       SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) ~Currently using 0 out of 3 allowed
       package processing threads.
       SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) ~Started package processing thread
       for package '<PackageID>', thread ID = 0x93C (2364)

  2. The package processing thread creates DP threads to process package actions and waits
     for them to exit.

     The package processing thread (TID 2364) processes the package actions
     (add/update/remove) for the DPs. In this case, the package was distributed to a DP and
     the package processing thread creates a DP thread to add the package to the DP. After
     creating the DP thread, the package processing thread waits for all the DP threads to exit
     before moving further.

       SMS_DISTRIBUTION_MANAGER 2364 (0x93c) ~Processing package <PackageID>
       (SourceVersion:1;StoredVersion:1)
       SMS_DISTRIBUTION_MANAGER 2364 (0x93c) Start updating the package
       <PackageID>...
       SMS_DISTRIBUTION_MANAGER 2364 (0x93c) ~The Package Action is 1, the Update
       Mask is 160 and UpdateMaskEx is 0.
       SMS_DISTRIBUTION_MANAGER 2364 (0x93c) ~Use drive E for storing the compressed
       package.
       SMS_DISTRIBUTION_MANAGER 2364 (0x93c) ~Successfully created/updated the
       package <PackageID> …
       SMS_DISTRIBUTION_MANAGER 2364 (0x93c) Start adding package <PackageID> to
       server ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\...
       SMS_DISTRIBUTION_MANAGER 2364 (0x93c) ~Created DP processing thread 5204

<!-- p.187 -->

    for addition or update of package <PackageID> on server
    ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\ …
    SMS_DISTRIBUTION_MANAGER 2364 (0x93c) ~Waiting for all DP threads to
    complete for package <PackageID> processing thread.

3. The DP threads create a PkgXferMgr job to transfer content to the DPs and then exits.

  The DP thread (TID 5204) starts working on adding the package to the DP. DP threads do
  not copy the package contents to the DP directly, but instead create a job for Package
  Transfer Manager (PkgXferMgr) instructing it to copy the package contents to the DP. The
  following log entries show the DP thread creating a PkgXferMgr job. After the job is
  created, the DP thread's work is done and the DP thread exits.

    SMS_DISTRIBUTION_MANAGER 5204 (0x1454) DP Thread: Attempting to add or
    update package <PackageID> on DP
    ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\
    SMS_DISTRIBUTION_MANAGER 5204 (0x1454) STATMSG: ID=2342 SEV=I LEV=M
    SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
    SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=5204 GMTDATE=Mon May 16
    16:31:37.364 2016 ISTR0="Dummy1" ISTR1="
    ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\" ISTR2="" ISTR3="" ISTR4="" ISTR5=""
    ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=2 AID0=400 AVAL0="
    <PackageID>" AID1=404 AVAL1="["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\"
    SMS_DISTRIBUTION_MANAGER 5204 (0x1454) The current user context will be used
    for connecting to ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\.~
    SMS_DISTRIBUTION_MANAGER 5204 (0x1454) ~Created package transfer job to
    send package <PackageID> to distribution point
    ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\.
    SMS_DISTRIBUTION_MANAGER 5204 (0x1454) STATMSG: ID=2357 SEV=I LEV=M
    SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
    SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=5204 GMTDATE=Mon May 16
    16:31:46.670 2016 ISTR0="PackageID" ISTR1="

<!-- p.188 -->

      ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
      ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\" ISTR2="" ISTR3="" ISTR4="" ISTR5=""
      ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=2 AID0=400 AVAL0="
      <PackageID>" AID1=404 AVAL1="["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
      ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\"
      SMS_DISTRIBUTION_MANAGER 5204 (0x1454) Performing cleanup prior to returning.
      SMS_DISTRIBUTION_MANAGER 5204 (0x1454) Cancelling network connection to
      \\PS1DP1.CONTOSO.COM\ADMIN$.

    When the DP thread creates a PkgXferMgr job, it does so by inserting a row in
    DistributionJobs table.

      SQL

      insert into DistributionJobs
      (DPID,PkgID,PackageVersion,State,CreationTime,Action)
      values(32,N'PackageID',1,0,N'Date Time',1)

    After creating the job, the DP thread also resets the Action for the DP in the PkgServers_L
    table.

      SQL

      update PkgServers_L set UpdateMask = 0, Action = 0, RefreshTrigger = 0,
      LastRefresh = N'Date Time' where PkgID = N'PackageID' and NALPath =
      N'["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
      ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\' and SiteCode = N'PS1' and Action <> 3

  4. The package process thread exits after all DP threads exit.

    After all the DP threads exit, the package processing thread exits as well:

      SMS_DISTRIBUTION_MANAGER 2364 (0x93c) ~DP thread for package <PackageID>
      with thread handle 000000000000218C and thread ID 5204 ended.
      SMS_DISTRIBUTION_MANAGER 2364 (0x93c) ~All DP threads have completed for
      package <PackageID> processing thread.
      SMS_DISTRIBUTION_MANAGER 2364 (0x93c) ~ Exiting package processing thread
      for package <PackageID>.

Step 10: SMSDBMON notifies PkgXferMgr to process the job created in
step 9-3

<!-- p.189 -->

After the PkgxferMgr job is created in step 9-3, SMSDBMON detects a change in the
DistributionJobs table and drops a PKN file in PkgTransferMgr.box to instruct PkgXferMgr to

process the job:

  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) RCV: UPDATE on DistributionJobs
  for DistributionJob_Creation [<PackageID>][1035292]
  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) SND: Dropped
  E:\ConfigMgr\inboxes\PkgTransferMgr.box\<PackageID>.PKN [1035292]

Step 11: PkgXferMgr wakes up to process the job

   1. The main PkgXferMgr thread creates a sending thread to the specified DP:

       SMS_PACKAGE_TRANSFER_MANAGER 5392 (0x1510) Found send request with ID:
       577, Package: <PackageID>, Version:1, Priority: 2, Destination:
       PS1DP1.CONTOSO.COM, DPPriority: 200
       SMS_PACKAGE_TRANSFER_MANAGER 5392 (0x1510) ~Created sending thread
       (Thread ID = 0x12EC)

   2. The sending thread copies the content to the DP.

     The sending thread starts copying the package contents to the DP. This process involves
     copying all of the files in the package to the DP in the SMS_DP$ directory. Since the
     package was not redistributed to the DP, the Redistribute action is set to 0, which means
     that if a file already exists in the content library on the DP, it does not get recopied.

       SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) Sending thread starting for Job:
       577, package: <PackageID>, Version: 1, Priority: 2, server: PS1DP1.CONTOSO.COM,
       DPPriority: 200
       SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) Sent status to the distribution
       manager for pkg <PackageID>, version 1, status 0 and distribution point
       ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\~
       SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) Sending legacy content
       <PackageID>.1 for package <PackageID>
       SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) Redistribute=0, Related=
       SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) Sending file
       '\\PS1DP1.CONTOSO.COM\SMS_DP$\73E055438D4731F41DB6C3BCB90919F6000022

<!-- p.190 -->

    6B330C73942454A174D7E26533-PackageID.1.temp'
    SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) Adding Dummy1.txt file in
    <PackageID>.1.
    SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) Completed post-actions for
    remote DP PS1DP1.CONTOSO.COM
    SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) ~Sending completed
    successfully
    SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) user(NT AUTHORITY\SYSTEM)
    runing application(SMS_PACKAGE_TRANSFER_MANAGER) from machine
    (PS1SITE.CONTOSO.COM) is submitting SDK changes from site(PS1)
    SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) ~Finished sending SWD
    package <PackageID> version 1 to distribution point PS1DP1.CONTOSO.COM
    SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) STATMSG: ID=8200 SEV=I
    LEV=M SOURCE="SMS Server" COMP="SMS_PACKAGE_TRANSFER_MANAGER"
    SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=4844 GMTDATE=Mon May 16
    16:34:27.614 2016 ISTR0="<PackageID>" ISTR1="1" ISTR2="PS1DP1.CONTOSO.COM"
    ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=2
    AID0=400 AVAL0="<PackageID>" AID1=410 AVAL1="1"

3. The sending thread sends a status message to DistMgr.

  After the sending thread finishes sending the content (success/failure), it sends the status
  to DistMgr so that DistMgr can process and update the status in the database. This status
  is sent to DistMgr by dropping an STA file containing the package status in the
  DistMgr.box\incoming directory.

    SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) Sent status to the distribution
    manager for pkg <PackageID>, version 1, status 3 and distribution point
    ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\~
    SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) STATMSG: ID=8210 SEV=I
    LEV=M SOURCE="SMS Server" COMP="SMS_PACKAGE_TRANSFER_MANAGER"
    SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=4844 GMTDATE=Mon May 16
    16:34:27.614 2016 ISTR0="<PackageID>" ISTR1="1" ISTR2="PS1DP1.CONTOSO.COM"
    ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=3
    AID0=400 AVAL0="<PackageID>" AID1=410 AVAL1="1" AID2=404 AVAL2="
    ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:

<!-- p.191 -->

        ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\"
        SMS_PACKAGE_TRANSFER_MANAGER 4844 (0x12ec) Sending thread complete~

Step 12: SMS DP Provider adds the content copied in step 11-2 to the
content library

During step 11-2, after copying each file, PkgXferMgr instructs the DP to add the file to the
content library by executing methods against the SMS_DistributionPoint WMI class in the SMS
DP Provider namespace (root\SCCMDP). When the content is successfully added to the content
library, SMSDPProv.log shows the following:

  2996 (0xbb4) Content '<PackageID>.1' for package '<PackageID>' has been added to
  content library successfully

Step 13: DistMgr processes the status message sent in step 11-3

To process the incoming STA file (sent in step 11-3), DistMgr uses the replication processing
thread. This thread wakes up to process the STA file, updates the Type 2 row in the
PkgStatus tables in the database and raises a status message with ID 2330 which means

'Distribution Manager successfully distributed package to distribution point.'

  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) ~Processing incoming file
  E:\ConfigMgr\inboxes\distmgr.box\INCOMING\1R7IEEHU.STA.
  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) ~Processing STA for regular DP
  ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\
  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) ~Processing status update for package
  <PackageID>
  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) ~Successfully updated the package server
  status for ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\ for package <PackageID>, Status 3
  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) STATMSG: ID=2330 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
  SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=6116 GMTDATE=Mon May 16
  16:34:31.679 2016 ISTR0="<PackageID>" ISTR1="
  ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM" ISTR2="" ISTR3="" ISTR4="" ISTR5=""
  ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=2 AID0=400 AVAL0="<PackageID>"
  AID1=404 AVAL1="["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:

<!-- p.192 -->

  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\"
  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) ~Successfully delete package status file
  E:\ConfigMgr\inboxes\distmgr.box\INCOMING\1R7IEEHU.STA

This thread runs the following query to update the status in the database.

  SQL

  update PkgStatus set Status = 3, UpdateTime = N'Date Time', Location = N'MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\SMSPKGC$\PackageID\', ShareName = N'', HTTPUrl
  = N'http://PS1DP1.CONTOSO.COM/SMS_DP_SMSPKG$/\PackageID', SourceVersion = 1,
  Personality = 0, State = 0, SigURL =
  N'http://PS1DP1.CONTOSO.COM/SMS_DP_SMSSIG$/\PackageID', SigLocation = N'MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\SMSSIG$\\PackageID.1.tar' where ID =
  N'\PackageID' and Type = 2 and SiteCode = N'PS1' and PkgServer =
  N'["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\'

Step 14: Package status changes are replicated to other sites via
database replication

After the package status is updated in the database, it is replicated to other sites via database
replication.

Distribute a package to standard DP
The following steps outline the flow of events when a package is distributed to a DP in the
primary site, and this primary site server in question already has a copy of the package in the
content library:

Step 1: The administrator distributes the package to the DP.
The administrator can do so from the admin console
connected directly to the primary site in question or the
central administration site, or a different primary site
After the administrator distributes the package to a DP from the console, the admin console
calls the AddDistributionPoints method of the SMS_Package class to add the specified DP to
the package. SMSProv.log shows the following:

  SMS Provider 4416 (0x1140) Context: SMSAppName=Configuration Manager
  Administrator console~
  SMS Provider 4416 (0x1140) ExecMethodAsync : SMS_Package.PackageID="

<!-- p.193 -->

  <PackageID>"::AddDistributionPoints~
  SMS Provider 4416 (0x1140) CExtProviderClassObject::DoExecuteMethod
  AddDistributionPoints~
  SMS Provider 4416 (0x1140) Auditing: User CONTOSO\Admin called an audited method of
  an instance of class SMS_Package.~

When this method is called, SMS Provider inserts a row in PkgServers with Action set to 2
(ADD):

  SQL

  insert PkgServers (PkgID, NALPath, SiteCode, SiteName, SourceSite, LastRefresh,
  RefreshTrigger, UpdateMask, Action) select N'<PackageID>',
  N'["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\',
  N'PS1', Sites.SiteName, N'PS1', N'04/10/1970 06:35:00', 0, 0, 2 from Sites where
  SiteCode = N'PS1'
  insert PkgNotification (PkgID, Priority, Type, TimeKey) values (N'<PackageID>', 2,
  4, GetDate())

Step 2: If the administrator distributes the package from a
different primary site or the central administration site,
Database Replication Service (DRS) replicates changes to the
site in question
If the administrator distributes this package with the console connected to the central
administration site or a different primary site, DRS replicates the changes in PkgServers to
other sites.

Step 3: SMSDBMON notifies DistMgr to process the package
After the change is replicated to the site where the DP resides, SMSDBMON detects a change
in the PkgNotification table and drops a PKN file in DistMgr.box to instruct DistMgr to
process the package:

  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) RCV: INSERT on PkgNotification
  for PkgNotify_Add [<PackageID>][1035417]
  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) SND: Dropped
  E:\ConfigMgr\inboxes\distmgr.box\<PackageID>.PKN [1035417]

Step 4: DistMgr wakes up to process the package

<!-- p.194 -->

DistMgr wakes up after detecting the PKN file and processes the package.

  1. The main DistMgr thread starts a package processing thread.

     The main DistMgr thread adds the package to the package processing queue and creates
     a package processing thread.

       SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) Adding package '<PackageID>' to
       package processing queue.
       SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) ~Currently using 0 out of 3 allowed
       package processing threads.
       SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) ~Started package processing thread
       for package '<PackageID>', thread ID = 0xB58 (2904)

  2. The package processing thread creates DP threads to process package actions, then waits
     for them to exit.

     The package processing thread (TID 2904) processes the package actions
     (add/update/remove) for the DP. In this case, the package was added to a DP and the
     package processing thread creates a DP thread to add the package to the DP. After
     creating the DP thread, the package processing thread waits for all the DP threads to exit
     before moving further:

       SMS_DISTRIBUTION_MANAGER 2904 (0xb58) ~Processing package <PackageID>
       (SourceVersion:1;StoredVersion:1)
       SMS_DISTRIBUTION_MANAGER 2904 (0xb58) No action specified for the package
       <PackageID>, however there may be package server changes for this package.
       SMS_DISTRIBUTION_MANAGER 2904 (0xb58) Start adding package <PackageID> to
       server ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\...
       SMS_DISTRIBUTION_MANAGER 2904 (0xb58) ~Created DP processing thread 3792
       for addition or update of package <PackageID> on server
       ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\ SMS_DISTRIBUTION_MANAGER 2904
       (0xb58) ~Waiting for all DP threads to complete for package <PackageID> processing
       thread.

  3. The DP threads create a Package Transfer Manager (PkgXferMgr) job to transfer content
     to the DPs and then exits.

<!-- p.195 -->

The DP thread (TID 3792) starts the work of adding the package to the DP. The DP
threads do not copy the package contents to the DP directly, but instead create a job for
PkgXferMgr instructing it to copy the package contents to the DP. The following log
entries show the DP thread creating a PkgXferMgr job. After the job is created, the DP
thread's work is done and the DP thread exits.

  SMS_DISTRIBUTION_MANAGER 3792 (0xed0) DP Thread: Attempting to add or
  update package <PackageID> on DP
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\
  SMS_DISTRIBUTION_MANAGER 3792 (0xed0) ~Created package transfer job to send
  package <PackageID> to distribution point
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\.
  SMS_DISTRIBUTION_MANAGER 3792 (0xed0) STATMSG: ID=2357 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
  SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=3792 GMTDATE=Mon May 16
  19:26:58.642 2016 ISTR0="<PackageID>" ISTR1="
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\" ISTR2="" ISTR3="" ISTR4="" ISTR5=""
  ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=2 AID0=400 AVAL0="
  <PackageID>" AID1=404 AVAL1="["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\"

When the DP thread creates a PkgXferMgr job, it does so by inserting a row in
DistributionJobs table.

  SQL

  insert into DistributionJobs
  (DPID,PkgID,PackageVersion,State,CreationTime,Action)
  values(35,N'PackageID',1,0,N'2016/05/16 15:26:58',1)

After creating the job, the DP thread also resets the Action for the DP in PkgServers_L
table:

  SQL

  update PkgServers_L set UpdateMask = 0, Action = 0, RefreshTrigger = 0,
  LastRefresh = N'05/16/2016 19:26:58' where PkgID = N'PackageID' and NALPath =

<!-- p.196 -->

       N'["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\' and SiteCode = N'PS1' and Action <> 3

   4. The package processing thread exits after all DP threads exit.

     After all of the DP threads exit, the package processing thread exits as well.

       SMS_DISTRIBUTION_MANAGER 2904 (0xb58) ~DP thread for package <PackageID>
       with thread handle 0000000000002524 and thread ID 3792 ended.
       SMS_DISTRIBUTION_MANAGER 2904 (0xb58) ~All DP threads have completed for
       package <PackageID> processing thread.
       SMS_DISTRIBUTION_MANAGER 2904 (0xb58) ~Exiting package processing thread for
       package <PackageID>.

Step 5: SMSDBMON notifies PkgXferMgr to process the job
After the PkgxferMgr job is created, SMSDBMON this time detects a change in the
DistributionJobs table and drops a PKN file in PkgTransferMgr.box to instruct PkgXferMgr to

process the job:

  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) RCV: UPDATE on DistributionJobs
  for DistributionJob_Creation [<PackageID>][1035419]
  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) SND: Dropped
  E:\ConfigMgr\inboxes\PkgTransferMgr.box\<PackageID>.PKN [1035419]

Step 6: PkgXferMgr wakes up to process the job
   1. The main PkgXferMgr thread creates a sending thread.

     The main PkgXferMgr thread creates a sending thread to send the package to the
     specified DP.

       SMS_PACKAGE_TRANSFER_MANAGER 5392 (0x1510) Found send request with ID:
       582, Package: <PackageID>, Version:1, Priority: 2, Destination:
       PS1DP2.CONTOSO.COM, DPPriority: 200
       SMS_PACKAGE_TRANSFER_MANAGER 5392 (0x1510) ~Created sending thread
       (Thread ID = 0xBCC)

   2. The sending thread copies content to the DP.

<!-- p.197 -->

  The sending thread (TID 3020) starts copying the package contents to the DP. This
  process involves copying all the files in the package to the DP in the SMS_DP$ directory.
  Since the package was not redistributed to the DP, the redistribute action is set to 0,
  which means that if a file already exists in the content library on the DP, it does not get
  re-copied.

    SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) Sending thread starting for Job:
    582, package: <PackageID>, Version: 1, Priority: 2, server: PS1DP2.CONTOSO.COM,
    DPPriority: 200
    SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) Sent status to the distribution
    manager for pkg <PackageID>, version 1, status 0 and distribution point
    ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\~
    SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) Sending legacy content
    <PackageID>.1 for package <PackageID>
    SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) Redistribute=0, Related=
    SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) Sending file
    '\\PS1DP2.CONTOSO.COM\SMS_DP$\73E055438D4731F41DB6C3BCB90919F6000022
    6B330C73942454A174D7E26533-PackageID.1.temp'
    SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) Adding Dummy1.txt file in
    <PackageID>.1
    SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) Completed post-actions for
    remote DP PS1DP2.CONTOSO.COM
    SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) ~Sending completed successfully
    SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) ~Finished sending SWD package
    <PackageID> version 1 to distribution point PS1DP2.CONTOSO.COM
    SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) STATMSG: ID=8200 SEV=I LEV=M
    SOURCE="SMS Server" COMP="SMS_PACKAGE_TRANSFER_MANAGER"
    SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=3020 GMTDATE=Mon May 16
    19:28:12.991 2016 ISTR0="<PackageID>" ISTR1="1" ISTR2="PS1DP2.CONTOSO.COM"
    ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=2
    AID0=400 AVAL0="<PackageID>" AID1=410 AVAL1="1"

3. The sending thread sends a status message to DistMgr.

  After the sending thread finishes sending the content (success/failure), it sends the status
  to DistMgr so that DistMgr can process and update the status in the database. This status

<!-- p.198 -->

     is sent to DistMgr by dropping an STA file containing the package status in the
      DistMgr.box\incoming directory:

       SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) Sent status to the distribution
       manager for pkg PackageID, version 1, status 3 and distribution point
       ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\~
       SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) STATMSG: ID=8210 SEV=I LEV=M
       SOURCE="SMS Server" COMP="SMS_PACKAGE_TRANSFER_MANAGER"
       SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=3020 GMTDATE=Mon May 16
       19:28:13.003 2016 ISTR0="<PackageID>" ISTR1="1" ISTR2="PS1DP2.CONTOSO.COM"
       ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=3
       AID0=400 AVAL0="<PackageID>" AID1=410 AVAL1="1" AID2=404 AVAL2="
       ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\"
       SMS_PACKAGE_TRANSFER_MANAGER 3020 (0xbcc) Sending thread complete~

Step 7: SMS DP Provider adds the content to the content
library
After copying each file, PkgXferMgr instructs the DP to add the file to the content library by
executing methods against the SMS_DistributionPoint WMI class in the SMS DP Provider
namespace (root\SCCMDP). When the content is successfully added to the content Library,
SMSDPProv.log shows the following:

  1304 (0x518) Content '<PackageID>.1' for package '<PackageID>' has been added to
  content library successfully

Step 8: DistMgr processes the status messages sent by PkgXferMgr

To process the incoming STA file (sent in step 6-3), DistMgr uses the replication processing
thread. This thread wakes up to process the STA file, updates the Type 2 row in the PkgStatus
tables in the database and raises a status message with ID 2330 which means 'Distribution
Manager successfully distributed package to distribution point.'

  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) ~Processing incoming file
  E:\ConfigMgr\inboxes\distmgr.box\INCOMING\FV8S6B6M.STA.
  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) ~Processing STA for regular DP
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:

<!-- p.199 -->

  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\
  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) ~Processing status update for package
  <PackageID>
  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) ~Successfully updated the package server
  status for ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\ for package <PackageID>, Status 3
  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) STATMSG: ID=2330 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
  SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=6116 GMTDATE=Mon May 16
  19:28:16.577 2016 ISTR0="<PackageID>" ISTR1="
  ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\" ISTR2="" ISTR3="" ISTR4="" ISTR5=""
  ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=2 AID0=400 AVAL0="<PackageID>"
  AID1=404 AVAL1="["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\"
  SMS_DISTRIBUTION_MANAGER 6116 (0x17e4) ~Successfully delete package status file
  E:\ConfigMgr\inboxes\distmgr.box\INCOMING\FV8S6B6M.STA

This thread runs the following query to update the status in the database.

  SQL

  update PkgStatus set Status = 3, UpdateTime = N'Date Time', Location = N'MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\SMSPKGC$\\PackageID\', ShareName = N'',
  HTTPUrl = N'http://PS1DP2.CONTOSO.COM/SMS_DP_SMSPKG$/\PackageID', SourceVersion =
  1, Personality = 0, State = 0, SigURL =
  N'http://PS1DP2.CONTOSO.COM/SMS_DP_SMSSIG$/\PackageID', SigLocation = N'MSWNET:
  ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\SMSSIG$\\PackageID.1.tar' where ID =
  N'\PackageID' and Type = 2 and SiteCode = N'PS1' and PkgServer =
  N'["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\'

Step 9: Package status changes are replicated to other sites
via DRS
After the package status is updated in the database, it is replicated to other sites via database
replication.

Distribute a package to pull DP

<!-- p.200 -->

The following steps outline the flow of events when a Package is distributed to a pull DP in the
primary site and this primary site server in question already has a copy of the package in the
content library.

Step 1: Administrator distribute the package to the DP. The
administrator can do so from the admin console connected
directly to the primary site in question or the central
administration site or a different Primary Site
After the administrator distributed the package to a DP from the console, console calls the
AddDistributionPoints method of the appropriate derived class of SMS_Package

( SMS_ContentPackage for applications in the example below) class to add the specified DP to the
package. SMSProv.log shows:

  SMS Provider 22172 (0x569c) Context: SMSAppName=Configuration Manager
  Administrator console~
  SMS Provider 22172 (0x569c) ExecMethodAsync :
  SMS_ContentPackage.PackageID='P010000F'::AddDistributionPoints~
  SMS Provider 22172 (0x569c) CExtProviderClassObject::DoExecuteMethod
  AddDistributionPoints~
  SMS Provider 22172 (0x569c) Auditing: User CONTOSO\Admin called an audited method
  of an instance of class SMS_ContentPackage.~

When this method is called, SMS Provider inserts a row in PkgServers with Action set to 2
(ADD) and a notification is created in the PkgNotification table.

Step 2: If administrator distributes the package from a
different primary site or the central administration site, DRS
replicates changes to the site in question
If the administrator distributed this package with the console connected to the central
administration site or a different primary site, DRS replicates the changes in PkgServers to
other sites.

Step 3: SMSDBMON notifies DistMgr to process the package
After this change is replicated to the site where the DP resides, SMSDBMON detects a change
in PkgNotification table, and drops a PKN file in DistMgr.box to instruct DistMgr to process
