---
title: "Core infrastructure documentation — pages 1721-1760"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1721-1760
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1721-1760
family: sccm
documentKind: "doc"
abstract: "Confirm version and restart (if necessary) Make sure each site server and site system role is updated to version 2409. In the console, add the Version column to the Sites and Distribution Points nodes in the Administration workspace. When necessary, a site system role automatica"
---

# Core infrastructure documentation — pages 1721-1760

<!-- p.1721 -->

Confirm version and restart (if necessary)
Make sure each site server and site system role is updated to version 2409. In the
console, add the Version column to the Sites and Distribution Points nodes in the
Administration workspace. When necessary, a site system role automatically reinstalls to
update to the new version.

Consider restarting remote site systems that don't successfully update at first. Review
your site infrastructure and make sure that applicable site servers and remote site
system servers successfully restarted. Typically, site servers restart only when
Configuration Manager installs .NET as a prerequisite for a site system role.

Confirm site-to-site replication is active
In the Configuration Manager console, go to the following locations to view the status,
and make sure that replication is active:

     Monitoring workspace, Site Hierarchy node

     Monitoring workspace, Database Replication node

For more information, see the following articles:

     Monitor hierarchy and replication infrastructure
     About the Replication Link Analyzer

Update Configuration Manager consoles
Update all remote Configuration Manager consoles to the same version. You're
prompted to update the console when:

     You open the console.

     You go to a new node in the console.

Reconfigure database replicas for management points
After you update a primary site, reconfigure the database replica for management
points that you uninstalled before you updated the site. For more information, see
Database replicas for management points.

Reconfigure availability groups

<!-- p.1722 -->

If you use an availability group, reset the failover configuration to automatic. For more
information, see Prepare to use an availability group.

Reconfigure any disabled maintenance tasks
If you disabled database maintenance tasks at a site before installing the update,
reconfigure those tasks. Use the same settings that were in place before the update.

Restore hardware inventory customizations
If you changed the state of hardware inventory classes in client settings, when you
update the site, some classes can revert to a default state. For example, if you disable
the SMS_Windows8Application or SMS_Windows8ApplicationUserInfo classes, they're
enabled after installing a Configuration Manager update.

When you customize hardware inventory classes, review their configuration after you
install the update to make sure they're configured as you intend.

Update clients
Update clients per the plan you created, especially if you configured client piloting
before installing the update. For more information, see How to upgrade clients for
Windows computers.

Partner extensions
If you use any extensions to Configuration Manager, update them to the latest version
to support Configuration Manager version 2409.

Update boot images and media
Use the Update Distribution Points action for any boot image that you use, whether it's
a default or custom boot image. This action makes sure that clients can use the latest
version. Even if there isn't a new version of the Windows ADK, the Configuration
Manager client components can change with an update. If you don't update boot
images and media, task sequence deployments can fail on devices.

When you update the site, Configuration Manager automatically updates the default
boot images. It doesn't automatically distribute the updated content to distribution
points. Use the Update Distribution Points action on specific boot images when you're
ready to distribute this content across your network.

<!-- p.1723 -->

  ７ Note

  For default boot images, the site always uses the current version of the
  Configuration Manager client that matches the site's version. Even if you configure
  automatic client upgrades to use a pre-production collection, that feature doesn't
  apply to boot images.

After updating the site, manually update any custom boot images. This action updates
the boot image with the latest client components if necessary, optionally reloads it with
the current Windows PE version, and redistributes the content to the distribution points.

For more information, see Update distribution points with the boot image.

Update PowerShell help content
To get the latest information for the Configuration Manager PowerShell module, use the
Update-Help cmdlet. Run this cmdlet on all computers with the Configuration Manager
console. This help content is the same as the content published for the
ConfigurationManager module.

For more information, see Configuration Manager PowerShell cmdlets: Update help.

Next steps
Review the release notes. This article can be updated regularly, especially right after a
new current branch release. You can use RSS to be notified when this page is updated.
For more information, see How to use the docs.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1724 -->

Support for Configuration Manager current
branch versions
Applies to: Configuration Manager (current branch)

Microsoft plans to release updates for Configuration Manager current branch a few times per
year. Each update version remains in support for 18 months from its general availability release
date. Microsoft provides technical support for the entire period of support. There are two
distinct servicing phases that depend on the availability of the latest current branch version:

     Security and Critical Updates servicing phase - When running the latest current branch
     version of Configuration Manager, you receive both Security and Critical Updates.

     Security Updates (Only) servicing phase - After the release of a new current branch
     version, Microsoft only supports security updates to older versions for the remainder of
     that version's support lifecycle.

  ７ Note

  The latest current branch version is always in the Security and Critical Updates servicing
  phase. This support statement means that if you encounter a code defect that warrants a
  critical update, you must have the latest current branch version installed in order to
  receive a fix. All other supported current branch versions are eligible to receive only
  security updates.

  All support ends after the 18-month lifecycle has expired for a current branch version.

  Update your Configuration Manager environment to the latest version before support for
  your current version expires.

For example, version 2203 releases in April 2022. Microsoft provides security and critical
updates to that version for four months, through July 2022. It then switches to only security
updates for the remaining 14 months of its support lifecycle, through September 2023.

  ７ Note

  A Critical Update specifies a widely released fix for a specific problem that addresses a
  critical, non-security-related bug. Security updates provide a severity rating for the
  updates, which includes the Critical rating. To understand the different uses for the term
  Critical and for more information about each, see update classifications and Security
  update severity.

<!-- p.1725 -->

For a list of the current branch supported versions*, see Version details.

  ７ Note

   * Supported Versions in Configuration Manager: In the context of Configuration

  Manager, the term supported encompasses both engineering and assisted technical
  support. While no further engineering development will occur for the versions that phase
  out of support, users will not have access to phone or online assisted technical support for
  these versions. However, Technical Support will assist with upgrading to a supported
  version of Configuration Manager. Users will resume their regular assisted technical
  support once Configuration Manager is upgraded to a supported version.

For more information about version numbers, and availability as an in-console update or as a
baseline, see Baseline and update versions.

 Last updated on 12/31/2025

<!-- p.1726 -->

Back up a Configuration Manager site
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Prepare backup and recovery approaches to avoid data loss. For Configuration Manager
sites, a backup and recovery approach can help you to recover sites and hierarchies
more quickly, and with the least data loss.

The sections in this article can help you back up your sites. To recover a site, see
Recovery for Configuration Manager.

  ２ Warning

  The two backup methods supported for Configuration Manager site recovery are:

        A successful backup from the Backup Site Server maintenance task
        A manually recovered site database backup

Considerations before creating a backup
      If you use a SQL Server Always On availability group to host the site database:
      Modify your backup and recovery plans as described in Prepare to use an
      availability group.

      Configuration Manager can recover the site database from the Configuration
      Manager backup task. It can also use a backup of the site database that you create
      with another process.

      For example, you can restore the site database from a backup that's created as
      part of a SQL Server maintenance plan. You can also use a backup that's created by
      using Data Protection Manager to back up your site database.

      You can also install an additional site server in passive mode. The site server in
      passive mode is in addition to your existing site server in active mode. A site server
      in passive mode is available for immediate use, when needed. For more
      information, see Site server high availability. While this role doesn't remove the
      need to plan for and practice backup and recovery operations, it significantly
      reduces the effort to recover a site when necessary.

<!-- p.1727 -->

Using Data Protection Manager to back up your site
database
You can use System Center Data Protection Manager (DPM) to back up your
Configuration Manager site database.

Create a new protection group in DPM for the site database computer. On the Select
Group Members page of the Create New Protection Group Wizard, you select the SMS
Writer service from the data source list. Then select the site database as an appropriate
member. For more information about using DPM, see the Data Protection Manager
documentation library.

  ） Important

  Configuration Manager doesn't support DPM backup for a SQL Server Always On
  failover cluster instance that uses a named instance. It does support DPM backup
  on a failover cluster instance that uses the default instance of SQL Server.

After you restore the site database, follow the steps in setup to recover the site. To use
the site database that you backed up with Data Protection Manager, select the recovery
option to Use a site database that has been manually recovered.

Backup maintenance task
You can automate backup for Configuration Manager sites by scheduling the predefined
Backup Site Server maintenance task. This task has the following features:

     Runs on a schedule
     Backs up the site database
     Backs up specific registry keys
     Backs up specific folders and files
     Backs up the CD.Latest folder

Plan to run the default site backup task at a minimum of every five days. This schedule is
because Configuration Manager uses a SQL Server change tracking retention period of
five days. For more information, see SQL Server change tracking retention period.

To simplify the backup process, you can create an AfterBackup.bat file. This script
automatically runs post-backup actions after the backup task completes successfully.
Use the AfterBackup.bat file to archive the backup snapshot to a secure location. You

<!-- p.1728 -->

can also use the AfterBackup.bat file to copy files to your backup folder, or to start other
backup tasks.

You can back up a central administration site and primary site. Secondary sites or site
system servers don't have backup tasks.

When the Configuration Manager backup service runs, it follows the instructions defined
in the backup control file:
<ConfigMgrInstallationFolder>\Inboxes\Smsbkup.box\Smsbkup.ctl . You can modify the

backup control file to change the behavior of the backup service.

  ７ Note

  Modifications of Smsbkup.ctl will apply after a restart of the service
  SMS_SITE_VSS_WRITER on the Site Server.

Site backup status information is written to the Smsbkup.log file. This file is created in
the destination folder that you specify in the properties of the Backup Site Server
maintenance task.

To enable the site backup maintenance task
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. Select the site for which you want to enable the site backup maintenance task.

   3. Select Site Maintenance Tasks in the ribbon.

   4. Select the Backup Site Server task, and select Edit.

   5. Select the option to Enable this task. Select Set Paths to specify the backup
     destination. You have the following options:

        ） Important

        To help prevent tampering of the backup files, store the files in a secure
        location. The most secure backup path is to a local drive, so you can set NTFS
        file permissions on the folder. Configuration Manager doesn't encrypt the
        backup data that's stored in the backup path.

<!-- p.1729 -->

       Local drive on site server for site data and database: Specifies that the task
       stores the backup files for the site and site database in the specified path on
       the local disk drive of the site server. Create the local folder before the
       backup task runs. The Local System account on the site server must have
       Write NTFS file permissions to the local folder for the site server backup. The
       Local System account on the computer that's running SQL Server must have
       Write NTFS permissions to the folder for the site database backup.

       Network path (UNC name) for site data and database: Specifies that the task
       stores the backup files for the site and site database in the specified network
       path. Create the share before the backup task runs. The computer account of
       the site server must have Write NTFS and share permissions to the shared
       network folder. If SQL Server is installed on another computer, the computer
       account of the SQL Server must have the same permissions.

       Local drives on site server and SQL Server: Specifies that the task stores the
       backup files for the site in the specified path on the local drive of the site
       server. The task stores the backup files for the site database in the specified
       path on the local drive of the site database server. Create the local folders
       before the backup task runs. The computer account of the site server must
       have Write NTFS permissions to the folder that you create on the site server.
       The computer account of the SQL Server must have Write NTFS permissions
       to the folder that you create on the site database server. This option is
       available only when the site database isn't installed on the site server.

    ７ Note

    The option to browse to the backup destination is only available when you
    specify the network path of the backup destination.

    The folder name or share name that's used for the backup destination doesn't
    support the use of Unicode characters.

6. Configure a schedule for the site backup task. Consider a backup schedule that's
  outside active working hours. If you have a hierarchy, consider a schedule that runs
  at least two times a week. If the site fails, this schedule ensures maximum data
  retention.

  When you run the Configuration Manager console on the same site server that
  you're configuring for backup, the backup task uses local time for the schedule.
  When you run the Configuration Manager console from another computer, the
  backup task uses Coordinated Universal Time (UTC) for the schedule.

<!-- p.1730 -->

   7. Choose whether to create an alert if the site backup task fails. When selected,
     Configuration Manager creates a critical alert for the backup failure. You can review
     these alerts in the Alerts node of the Monitoring workspace.

Verify that the Backup Site Server maintenance task is running
     Check the timestamp on the files in the backup destination folder that the task
     created. Verify that the timestamp updates to the time when the task was last
     scheduled to run.

     Go to the Component Status node of the Monitoring workspace. Review the
     status messages for SMS_SITE_BACKUP. When site backup completes successfully,
     you see message ID 5035. This message indicates that the site backup completed
     without any errors.

     When you configure the backup task to create an alert when it fails, look for
     backup failure alerts in the Alerts node of the Monitoring workspace.

     Open Windows Explorer on the site server and browse to
     <ConfigMgrInstallationFolder>\Logs . Review Smsbkup.log for warnings and

     errors. When site backup completes successfully, the log shows Backup completed
     with message ID STATMSG: ID=5035 .

         Tip

        When the backup maintenance task fails, restart the backup task by stopping
        and restarting the SMS_SITE_BACKUP Windows service.

Archive the backup snapshot
The backup task creates a backup snapshot the first time it runs. You can use this
snapshot to recover your site server if it fails. When the backup task runs again on
schedule, it creates a new backup snapshot that overwrites the previous snapshot. As a
result, the site has only a single backup snapshot, and you've no way of retrieving an
earlier backup snapshot.

Keep multiple archives of the backup snapshot for the following reasons:

     It's common for backup media to fail, get misplaced, or include only a partial
     backup. Recovering a failed stand-alone primary site from an older backup is
     better than recovering without any backup. For a site server in a hierarchy, the

<!-- p.1731 -->

     backup must be in the SQL Server change tracking retention period, or the backup
     isn't required.

     A corruption in the site can go undetected for several backup cycles. You might
     have to use a backup snapshot from before the site became corrupted. This reason
     applies to a stand-alone primary site and to sites in a hierarchy where the backup
     is in the SQL Server change tracking retention period.

     The site might have no backup snapshot at all. For example, if the Backup Site
     Server maintenance task fails. Because the backup task removes the previous
     backup snapshot before it starts to back up the current data, there won't be a valid
     backup snapshot.

Use the AfterBackup.bat file
After successfully backing up the site, the backup task automatically tries to run a script
named AfterBackup.bat. Manually create the AfterBackup.bat file on the site server in
<ConfigMgrInstallationFolder>\Inboxes\Smsbkup.box . If an AfterBackup.bat file exists in

the correct folder, it automatically runs after the backup task completes.

The AfterBackup.bat file lets you archive the backup snapshot at the end of every
backup operation. It can automatically perform other post-backup tasks that aren't part
of the Backup Site Server maintenance task. The AfterBackup.bat file integrates the
archive and the backup operations, thereby ensuring that every new backup snapshot is
archived.

If the AfterBackup.bat file isn't present, the backup task skips it without effect on the
backup operation. To verify that the backup task successfully ran this script, go to the
Component Status node in the Monitoring workspace, and review the status messages
for SMS_SITE_BACKUP. When the task successfully starts the AfterBackup.bat command
file, you see message ID 5040.

   Tip

  To archive your site server backup files with AfterBackup.bat, you must use a copy
  command tool in the batch file. One such tool is Robocopy in Windows Server. For
  example, create the AfterBackup.bat file with the following command: Robocopy
  E:\ConfigMgr_Backup \\ServerName\ShareName\ConfigMgr_Backup /MIR

Although the intended use of the AfterBackup.bat is to archive backup snapshots, you
can create an AfterBackup.bat file to run additional tasks at the end of every backup

<!-- p.1732 -->

operation.

Supplemental backup tasks
The Backup Site Server maintenance task provides a backup snapshot for the site server
files and site database. There are other items not backed up that you must consider
when you create your backup strategy. Use these sections to help you complete your
Configuration Manager backup strategy.

Back up custom reports
If you modify predefined or created custom reports in SQL Server Reporting Services,
create a backup for the report server database files. The report server backup must
include the following components:

     The source files for reports and models
     Encryption keys
     Custom assemblies or extensions
     Configuration files
     Custom SQL Server views used in custom reports
     Custom stored procedures

  ） Important

  When Configuration Manager updates to a newer version, the predefined reports
  might be overwritten by new reports. If you modify a predefined report, make sure
  to back up the report and then restore it in Reporting Services.

For more information about backing up your custom reports in Reporting Services, see
Backup and Restore Operations for Reporting Services.

Back up content files
The content library in Configuration Manager is the location where all content files are
stored for all software deployments. The content library is located on the site server and
on each distribution point. The Backup Site Server maintenance task doesn't back up the
content library or package source files. When a site server fails, the information about
the content library is restored to the site database, but you must restore the content
library and package source files.

<!-- p.1733 -->

     The content library must be restored before you can redistribute content to
     distribution points. When you start content redistribution, Configuration Manager
     copies the files from the site server's content library to the distribution points. For
     more information, see The content library.

     The package source files must be restored before you can update content on
     distribution points. When you start a content update, Configuration Manager
     copies new or modified files from the package source to the content library. It then
     copies the files to associated distribution points. Run the following SQL query
     against the site database to find the package source location for all packages and
     applications: SELECT * FROM v_Package . You can identify the package source site by
     looking at the first three characters of the package ID. For example, if the package
     ID is CEN00001, the site code for the source site is CEN. When you restore the
     package source files, they must be restored to the same location where they were
     before the failure.

Verify that you include both the content library and package source files in your file
system backup for the site server.

Back up custom software updates
System Center Updates Publisher is a stand-alone tool that lets you manage custom
software updates. Updates Publisher uses a local database for its software update
repository. When you use Updates Publisher to manage custom software updates,
determine whether you should include the Updates Publisher database in your backup
plan. For more information, see System Center Updates Publisher.

Use the following procedure to back up the Updates Publisher database.

Back up the Updates Publisher database
   1. On the computer that runs Updates Publisher, browse to the Updates Publisher
     database file Scupdb.sdf in %USERPROFILE%\AppData\Local\Microsoft\System Center
     Updates Publisher 2011\5.00.1727.0000\ . There's a different database file for each

     user that runs Updates Publisher.

   2. Copy the database file to your backup destination. For example, if your backup
     destination is E:\ConfigMgr_Backup , you could copy the Updates Publisher
     database file to E:\ConfigMgr_Backup\SCUP .

         Tip

<!-- p.1734 -->

        When there's more than one database file on a computer, consider storing
        the file in a subfolder that indicates the user profile associated with the
        database file. For example, you could have one database file in
        E:\ConfigMgr_Backup\SCUP\User1 and another database file in

        E:\ConfigMgr_Backup\SCUP\User2 .

User state migration data
You can use Configuration Manager task sequences to capture and restore the user
state data in OS deployment scenarios. The properties of the state migration point list
the folders that store the user state data. This data isn't backed up as part of the Site
Server Backup maintenance task. As part of your backup plan, you must manually back
up the folders that you specify to store the user state migration data.

Determine the folders used to store user state migration
data
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Servers and Site System Roles node.

   2. Select the site system that hosts the state migration role. Then select State
     migration point in the Site System Roles pane.

   3. Select Properties in the ribbon.

   4. The folders that store the user state migration data are listed in the Folder details
     section on the General tab.

About the SMS Writer service
The SMS Writer is a service that interacts with the Windows Volume Shadow Copy
Service (VSS) during the backup process. The SMS Writer service must be running for
the Configuration Manager site back up to complete successfully.

Process
   1. SMS Writer registers with the VSS service and binds to its interfaces and events.

   2. When VSS broadcasts events, or if it sends specific notifications to the SMS Writer,
     the SMS Writer responds to the notification and takes the appropriate action.

<!-- p.1735 -->

   3. The SMS Writer reads the backup control file smsbkup.ctl located in
     <ConfigMgrInstallationPath>\inboxes\smsbkup.box , and determines the files and

     data to back up.

   4. The SMS Writer builds metadata, which consists of various components including
     specific data from the SMS registry key and subkeys.

      a. It sends the metadata to VSS when it's requested.

     b. VSS then sends the metadata to the requesting application, the Configuration
        Manager Backup Manager.

   5. Backup Manager selects the data to back up, and sends this data to the SMS
     Writer via VSS.

   6. The SMS Writer takes the appropriate steps to prepare for the backup.

   7. Later, when VSS is ready to take the snapshot:

      a. It sends an event

     b. The SMS Writer stops all Configuration Manager services

      c. It ensures that the Configuration Manager activities are frozen while the
        snapshot is created.

   8. After the snapshot is complete, the SMS Writer restarts services and activities.

The SMS Writer service is installed automatically. It must be running when the VSS
application requests a backup or restore.

Writer ID
The writer ID for the SMS Writer is 03ba67dd-dc6d-4729-a038-251f7018463b.

Permissions
The SMS Writer service must run under the Local System account.

Volume Shadow Copy service
The VSS is a set of COM APIs that implements a framework to allow volume backups to
be performed while applications on a system continue to write to the volumes. The VSS
provides a consistent interface that allows coordination between user applications that

<!-- p.1736 -->

update data on disk (the SMS Writer service) and those that back up applications (the
Backup Manager service). For more information, see the Volume Shadow Copy Service.

Next steps
After you create a backup, practice site recovery with that backup. This practice can help
you become familiar with the recovery process before you need to rely on it. It can also
help confirm the backup was successful for its intended purpose.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1737 -->

Recover a Configuration Manager site
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Run a Configuration Manager site recovery after a site fails or data loss occurs in the site
database. Repairing and resynchronizing data are the core tasks of a site recovery and
are required to prevent interruption of operations.

The sections in this article can help you recover a Configuration Manager site. To create
a backup, see Backup for Configuration Manager.

Considerations before recovering a site

  ） Important

  This information applies only to site recovery scenarios. When you're upgrading
  your on-premises infrastructure and not actively recovering a failed site, review the
  information in the following articles:

        Upgrade on-premises infrastructure
        Modify your infrastructure

Prepare the server hardware
Make sure existing configurations aren't present on the site server. Any previous
configurations can cause conflicts during the site recovery process. Use one of the
following options for the server hardware:

      Use a new server, that meets the general and recovery requirements.

      Format the disks, and reinstall the OS on the existing server. Make sure it meets
      the general and recovery requirements.

      Reuse an existing server that you've cleaned

Use one of the following procedures to clean an existing server:

Clean an existing server for site server recovery only

<!-- p.1738 -->

  1. Delete SMS registry keys: HKLM\Software\Microsoft\SMS
  2. Delete any registry entries starting with SMS from
     HKLM\System\CurrentControlSet\Services . For example:

          SMS_DISCOVERY_DATA_MANAGER
          SMS_EXECUTIVE
          SMS_INBOX_MONITOR
          SMS_INVENTORY_DATA_LOADER
          SMS_LAN_SENDER
          SMS_MP_FILE_DISPATCH_MANAGER
          SMS_SCHEDULER
          SMS_SITE_BACKUP
          SMS_SITE_COMPONENT_MANAGER
          SMS_SITE_SQL_BACKUP
          SMS_SITE_VSS_WRITER
          SMS_SOFTWARE_METERING_PROCESSOR
          SMS_STATE_SYSTEM
          SMS_STATUS_MANAGER
          SMS_WSUS_SYNC_MANAGER
          SMSvcHost 3.0.0.0
          SMSvcHost 4.0.0.0

  3. Uninstall the Configuration Manager console
  4. Restart the server
  5. Confirm that all of the above registry keys are deleted.

The server is now ready for the Configuration Manager restore procedure.

Clean an existing server for site database recovery only

  1. Back up the site database. Also back up any other supporting databases, like
     WSUS.
  2. Make sure to note the SQL Server name and instance name
  3. Manually delete the site database from the SQL Server
  4. Restart the SQL Server

The server is now ready for the Configuration Manager restore procedure.

Clean an existing server for full recovery

  1. Back up the site database. Also back up any other supporting databases, like
     WSUS.

<!-- p.1739 -->

   2. Make a copy of the content library

  ２ Warning

  The following step - Uninstall the Configuration Manager site - should only be
  performed on a standalone Primary site, or a child Primary site that is unable to
  communicate over the network with the Central Administration Site (CAS).
  Uninstalling the site in a hierarchy results is the CAS losing the ability to
  communicate with that child primary and the restore process will fail. For child
  Primary sites, instead follow the Clean an existing server for site server recovery
  only steps above.

   3. Manually delete the site database from the SQL Server
   4. Uninstall the Configuration Manager site
   5. Manually delete the Configuration Manager installation folder, related registries
     and any other Configuration Manager folders
   6. Restart the server
   7. Restore the content library and other databases like WSUS.

The server is now ready for the Configuration Manager restore procedure.

Use a supported version and same edition of SQL Server
If possible, use the same version of SQL Server. However, it's supported to restore a
database to a newer version.

Don't change the SQL Server edition. Restoring a site database from Standard edition to
Enterprise edition isn't supported.

Other SQL Server configuration requirements:

     SQL Server can't be set to single-user mode.
     Make sure the MDF and LDF files are valid. When you recover a site, there's no
     check for the state of the files.

SQL Server Always On availability groups
If you use SQL Server Always On availability groups to host the site database, modify
your recovery plans as described in Prepare to use SQL Server Always On.

Database replicas

<!-- p.1740 -->

After you restore a site database that you configured for database replicas, reconfigure
each replica. Before you can use the database replicas, recreate both the publications
and subscriptions.

Determine your recovery options
There are two main areas to consider for Configuration Manager primary site server and
central administration site (CAS) recovery: the site server and the site database. The
following sections can help you select the best options for your recovery scenario.

  ７ Note

  When Configuration Manager setup detects an existing site on the server, you can
  start a site recovery, but the recovery options for the site server are limited. For
  example, if you run Setup on an existing site server, when you choose recovery, you
  can recover the site database server, but the option to recover the site server is
  disabled.

Site server recovery options
Start Configuration Manager setup from a copy of the CD.Latest folder that you created
outside of the Configuration Manager installation folder.

      If you run setup from the Start menu on the site server, the Recover a site option
      isn't available.

      If you installed any updates from within the Configuration Manager console before
      you made your backup, you can't reinstall the site by using setup from the
      following locations:
         Installation media
         The Configuration Manager installation path

Then select the Recover a site option. You have the following recovery options for the
failed site server:

Recover the site server using an existing backup

Use this option when you have a Configuration Manager backup of the site server from
before the site failure. The site creates this backup as part of the Backup Site Server
maintenance task. The site is reinstalled, and the site settings are configured based on
the site that was backed up.

<!-- p.1741 -->

Reinstall the site server
Use this option when you don't have a backup of the site server. The site server is
reinstalled, and you must specify the site settings as you would during an initial
installation.

      Use the same site code and site database name that you used when the failed site
      was first installed.

      You can reinstall the site on a new computer that runs a new OS version.

      The server must use the same hostname and fully qualified domain name (FQDN)
      of the original site server.

Site database recovery options
When you run Configuration Manager setup, you have the following recovery options
for the site database:

Recover the site database using a backup set

Use this option when you have a Configuration Manager backup of the site database
from before the database failure. The site creates this backup as part of the Backup Site
Server maintenance task. In a hierarchy, when restoring a primary site, the recovery
process retrieves from the CAS any changes made to the site database after the last
backup. When restoring the CAS, the recovery process retrieves these changes from a
reference primary site. When you recover the site database for a standalone primary site,
you lose site changes after the last backup.

When you recover the site database for a site in a hierarchy, the recovery behavior is
different for a CAS and primary site. The behavior is also different when the last backup
is inside or outside of the SQL Server change tracking retention period. For more
information, see the Site database recovery scenarios section in this article.

  ７ Note

  If you select to restore the site database by using a backup set, but the site
  database already exists, the recovery fails.

Create a new database for this site

<!-- p.1742 -->

Use this option when you don't have a backup of the site database. In a hierarchy, the
recovery process creates a new site database. When restoring a child primary site, it
recovers the data by replicating from the CAS. When restoring the CAS, it replicates data
from a reference primary site. This option isn't available when you're recovering a
standalone primary site or a CAS that doesn't have primary sites.

Use a site database that has been manually recovered
Use this option when you've already recovered the Configuration Manager site
database, but need to complete the recovery process.

     Configuration Manager can recover the site database from any of the following
     processes:

        The Configuration Manager backup maintenance task

        A site database backup using Data Protection Manager (DPM)

        Another backup process

        After you restore the site database by using a method outside Configuration
        Manager, run Setup, and select this option to complete the site database
        recovery.

           ７ Note

           When you use DPM to back up your site database, use the DPM
           procedures to restore the site database to a specified location before you
           continue the restore process in Configuration Manager. For more
           information about DPM, see the Data Protection Manager documentation
           library.

     In a hierarchy, when you recover a primary site database, the recovery process
     retrieves from the CAS any changes made to the site database after the last
     backup. When restoring the CAS, the recovery process retrieves these changes
     from a reference primary site. When you recover the site database for a standalone
     primary site, you lose site changes after the last backup.

Skip database recovery
Use this option when no data loss has occurred on the Configuration Manager site
database server. This option is only valid when the site database is on a different

<!-- p.1743 -->

computer than the site server that you're recovering.

SQL Server change tracking retention period
Configuration Manager enables change tracking for the site database in SQL Server.
Change tracking lets Configuration Manager query for information about the changes
made to database tables after a previous point in time. The retention period specifies
how long change tracking information is kept. By default, the site database is configured
to have a retention period of five days. When you recover a site database, the recovery
process proceeds differently if your backup is inside or outside the retention period. For
example, if your SQL Server fails, and your last backup is seven days old, it's outside the
retention period.

For more information about SQL Server change tracking internals, see the following
blog posts from the SQL Server team: Change Tracking Cleanup - part 1 and Change
Tracking Cleanup - part 2.

Reinitialization of site or global data
The process to reinitialize site or global data replaces existing data in the site database
with data from another site database. For example, when site ABC reinitializes data from
site XYZ, the following steps occur:

     The data is copied from site XYZ to site ABC.
     The existing data for site XYZ is removed from the site database on site ABC.
     The copied data from site XYZ is inserted into the site database for site ABC.

Example scenario 1: The primary site reinitializes the global data
from the CAS
The recovery process removes the existing global data for the primary site in the
primary site database and replaces the data with the global data copied from the CAS.

Example scenario 2: The CAS reinitializes the site data from a
primary site

The recovery process removes the existing site data for that primary site in the CAS
database. It replaces the data with the site data copied from the primary site. The site
data for other primary sites isn't affected.

Site database recovery scenarios

<!-- p.1744 -->

After a site database is restored from a backup, Configuration Manager tries to restore
the changes in site and global data after the last database backup. Configuration
Manager starts the following actions after a site database is restored from backup:

Recovered site is a CAS
     Database backup within change tracking retention period

        Global data: The changes in global data after the backup are replicated from all
        primary sites.

        Site data: The changes in site data after the backup are replicated from all
        primary sites.

     Database backup older than change tracking retention period

        Global data: The CAS reinitializes the global data from the reference primary
        site if you specify it. Then all other primary sites reinitialize the global data from
        the CAS. If you don't specify a reference site, all primary sites reinitialize the
        global data from the CAS. This data is what you restored from backup.

        Site data: The CAS reinitializes the site data from each primary site.

Recovered site is a primary site
     Database backup within change tracking retention period

        Global data: The changes in global data after the backup are replicated from
        the CAS.

        Site data: The CAS reinitializes the site data from the primary site. Changes after
        the backup are lost. Clients regenerate most data when they send information
        to the primary site.

     Database backup older than change tracking retention period

        Global data: The primary site reinitializes the global data from the CAS.

        Site data: The CAS reinitializes the site data from the primary site. Changes after
        the backup are lost. Clients regenerate most data when they send information
        to the primary site.

Site recovery procedures

<!-- p.1745 -->

Use one of the following procedures to help you recover your site server and site
database:

Start a site recovery in the setup wizard
   1. Copy the CD.Latest folder to a location outside the Configuration Manager
     installation folder. From the copy of the CD.Latest folder, run the Configuration
     Manager setup wizard.

   2. On the Getting Started page, select Recover a site, and then select Next.

   3. Complete the wizard by using the options that are appropriate for your site
     recovery.

            During the recovery, setup identifies the SQL Server Service Broker (SSB) port
            used by the SQL Server. Don't change this port setting during recovery or
            data replication won't work properly after the recovery completes.

            You can specify the original or a new path to use for the Configuration
            Manager installation in the setup wizard.

Start an unattended site recovery
   1. Prepare the unattended installation script for the options that you require for the
     site recovery. For more information, see Unattended site recovery.

   2. Run Configuration Manager setup by using the /script command-line option. For
     example, you create a setup initialization file ConfigMgrUnattend.ini. You save it in
     the C:\Temp directory of the computer on which you're running setup. Use the
     following command:

     setup.exe /script C:\temp\ConfigMgrUnattend.ini

  ７ Note

  After you recover a CAS, replication of some site data from child sites can fail to be
  established. This data can include hardware inventory, software inventory, and
  status messages.

  If this issue occurs, reinitialize the ConfigMgrDRSSiteQueue for database
  replication. Use SQL Server Manager to run the following query against the site
  database for the CAS:

<!-- p.1746 -->

     SQL

     IF EXISTS (SELECT * FROM sys.service_queues WHERE name =
     'ConfigMgrDRSSiteQueue' AND is_receive_enabled = 0)

     ALTER QUEUE [dbo].[ConfigMgrDRSSiteQueue] WITH STATUS = ON

Post-recovery tasks
After you recover your site, there are several post-recovery tasks to consider before your
site recovery is complete. Use the following sections to help you complete your site
recovery process.

Reenter user account passwords
After a site server recovery, reenter the passwords for any user accounts in the site.
These passwords are reset during the site recovery. The accounts are listed on the
Finished page of the setup wizard after site recovery is completed. The list is also saved
to C:\ConfigMgrPostRecoveryActions.html on the recovered site server.

Reenter user account passwords after site recovery
   1. Open the Configuration Manager console and connect to the recovered site.

   2. Go to the Administration workspace, expand Security, and then select Accounts.

   3. For each account, do the following steps to reenter the password:

      a. Select the account from the list identified after site recovery.

      b. Select Properties in the ribbon.

      c. On the General tab, select Set, and then reenter the password for the account.

      d. Select Verify, choose the appropriate data source for the selected user account,
           and then select Test connection. This step tests that the user account can
           connect to the data source, and verifies the credentials.

      e. Select OK to save the password changes, and then select OK to close the
           account properties page.

Reenter PXE passwords

<!-- p.1747 -->

   1. In the Configuration Manager console, go to the Administration workspace, and
     select the Distribution Points node. Any on-premises distribution point with Yes in
     the PXE column is enabled for PXE and may have a password to reenter.

   2. Select a PXE-enabled distribution point, and select Properties in the ribbon.

   3. Switch to the PXE tab.

   4. If the option to Require a password when computers use PXE is enabled, enter
     and confirm the password.

   5. Select OK to save and close the properties.

Repeat this process for any other PXE-enabled on-premises distribution point.

Reenter task sequence passwords

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Operating Systems, and select the Task Sequences node.

   2. Select a task sequence, and then in the ribbon, select Edit.

   3. Review the following steps for passwords to reenter:

           Apply Windows Settings: If you enable and specify the local administrator
           password, reenter and confirm the password.

           Apply Network Settings: For the account that has permission to join the
           domain, select Set. Enter and confirm the password, and then select Verify.

           Capture Operating System Image: For the account used to access the
           destination, select Set. Enter and confirm the password, and then select
           Verify.

           Connect to Network Folder: For the account used to connect a network
           folder, select Set. Enter and confirm the password, and then select Verify.

           Enable BitLocker: If you use the key management option TPM and PIN,
           reenter the PIN.

           Join Domain or Workgroup: For the account that has permission to join the
           domain, select Set. Enter and confirm the password, and then select Verify.

           Run Command Line: If you use the option to Run this step as the following
           account, select Set. Enter and confirm the password, and then select Verify.

<!-- p.1748 -->

           Run PowerShell Script: If you use the option to Run this step as the
           following account, select Set. Enter and confirm the password, and then
           select Verify.

Repeat this process for all task sequences.

Recreate bootable media and prestaged media in non-PKI
environments
In non-PKI environments, self-signed certs in bootable media and prestaged media are
based on the machine keys of the server where the media was created. For this reason, if
the hardware changes or the OS is reinstalled as part of a recovery, any bootable media
and prestaged media created on that server need to be recreated. For more information
on how to create bootable media and prestaged media, see Create bootable media and
Create prestaged media.

Reenter sideloading keys
After a site server recovery, reenter Windows sideloading keys specified for the site.
These keys are reset during site recovery. After you reenter the sideloading keys, the site
resets the count in the Activations used column for Windows sideloading keys.

For example, before the site failure the Total activations count shows as 100. The
number of keys that devices have used, or Activations used, is 90. After the site
recovery, the Total activations value still displays 100, but the Activations used column
incorrectly displays 0. After 10 new devices use a sideloading key, there are no more
sideloading keys, and the 11th device fails to apply a sideloading key.

Recreate Azure services
After site recovery, you may see the following error in the cloudmgr.log:

Index (zero-based) must be greater than or equal to zero

To resolve this issue, Renew the secret key for each Azure tenant connection.

Delete and recreate subscriptions for external
notifications on the CAS
After you recover the CAS, you need to delete and recreate any subscriptions for
external notifications. For more information, see External notifications.

<!-- p.1749 -->

Configure HTTPS for site system roles that use IIS
When you recover site systems that run IIS and you configured for HTTPS, reconfigure
IIS to use the web server certificate.

Reinstall hotfixes
After a site recovery, you must reinstall any out-of-band hotfixes that were applied to
the site server. After site recovery, view the list of the previously installed hotfixes on the
Finished page of the setup wizard. This list is also saved to
C:\ConfigMgrPostRecoveryActions.html on the recovered site server.

Recover custom reports
Some customers create custom reports in SQL Server Reporting Services. When this
component fails, recover the reports from a backup of the report server. For more
information about restoring your custom reports in Reporting Services, see Backup and
Restore Operations for Reporting Services.

Recover content files
The site database tracks where the site server stores the content files. The content files
themselves aren't backed up or restored as part of the backup and recovery process. To
fully recover content files, restore the content library and package source files to the
original location. There are several methods for recovering your content files. The easiest
method is to restore the files from a file system backup of the site server.

If you don't have a file system backup for the package source files, manually copy or
download them. This process is similar to when you originally created the package. Run
the following query in SQL Server to find the package source location for all packages
and applications: SELECT * FROM v_Package . Identify the package source site by looking
at the first three characters of the package ID. For example, if the package ID is
CEN00001, the site code for the source site is CEN. When you restore the package
source files, they must be restored to the same location in which they were before the
failure.

If you don't have a file system backup that includes the content library, you have the
following restore options:

      Import a prestaged content file: In a Configuration Manager hierarchy, you can
      create a prestaged content file with all packages and applications from another

<!-- p.1750 -->

     location. Then import the prestaged content file to recover the content library on
     the site server.

     Update content: Configuration Manager copies the content from the package
     source to the content library. For this action to finish successfully, the package
     source files must be available in the original location. Do this action on each
     package and application.

Recover custom software updates
When you've included System Center Updates Publisher database files in your backup
plan, you can recover the databases if the Updates Publisher computer fails. For more
information about Updates Publisher, see System Center Updates Publisher.

Restore the Updates Publisher database

   1. Reinstall Updates Publisher on the recovered computer.

   2. Copy the database file Scupdb.sdf from your backup destination to
      %USERPROFILE%\AppData\Local\Microsoft\System Center Updates Publisher
     2011\5.00.1727.0000\ on the computer that runs Updates Publisher.

   3. When more than one user runs Updates Publisher on the computer, copy each
     database file to the appropriate user profile location.

User State Migration data
As part of the state migration point properties, you specify the folders that store user
state data. After you recover a state migration point, manually restore the user state
data on the server. Restore it to the same folders that stored the data before the failure.

Regenerate the certificates for distribution points
After you restore a site, the distmgr.log might list the following entry for one or more
distribution points: Failed to decrypt cert PFX data . This entry indicates that the
distribution point certificate data can't be decrypted by the site. To resolve this issue,
regenerate or reimport the certificate for affected distribution points. Use the Set-
CMDistributionPoint PowerShell cmdlet.

Restore database encryption certificates

<!-- p.1751 -->

If you use SQL Server encryption for the entire database or for specific tables, you may
need to restore the certificates after you restore the site database. For example, if you
encrypt recovery data for BitLocker management. For more information, see Restore
certificate for BitLocker management.

Recover a secondary site
Configuration Manager doesn't support the backup of the database at a secondary site,
but does support recovery by reinstalling the secondary site. Secondary site recovery is
required when a Configuration Manager secondary site fails.

Requirements
        The server must meet all secondary site prerequisites and have appropriate
        security rights configured.

        Use the same installation path that was used for the failed site.

        Use a server with the same configuration as the failed server. This configuration
        includes its fully qualified domain name (FQDN).

        The server must have the same SQL Server configuration as the failed site.

          During a secondary site recovery, Configuration Manager doesn't install SQL
          Server Express if it's not already installed on the computer.

          Use the same version of SQL Server and the same instance of SQL Server that
          you used for the secondary site database before the failure.

Procedure
Use the Recover Secondary Site action from the Sites node in the Configuration
Manager console. Unlike with other types of sites, recovery for a secondary site doesn't
use a backup file. This process reinstalls the secondary site files on the failed server.
After the site reinstalls, the secondary site data is reinitialized from the parent primary
site.

During the recovery process, Configuration Manager verifies if the content library exists
on the secondary site server. It also checks that the appropriate content is available. The
secondary site uses the existing content library, if it includes the appropriate content.
Otherwise, to recover the content library of a secondary site, redistribute or prestage the
content to the server.

<!-- p.1752 -->

When you have a distribution point that isn't on the secondary site server, you aren't
required to reinstall the distribution point during a recovery of the secondary site. After
the secondary site recovery, the site automatically synchronizes with the distribution
point.

You can verify the status of the secondary site recovery by using the Show Install Status
action from the Sites node in the Configuration Manager console.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1753 -->

Unattended site recovery for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To recover a Configuration Manager central administration site (CAS) or primary site
without user interaction, create an unattended installation script to use with the /script
setup command-line option. The script provides the same type of information that the
setup wizard prompts for, except that there are no default settings. Specify all values for
the setup keys that apply to the type of recovery.

To use the /script setup command-line option, first create an answer file. Then specify
this file name on the command line. The name of the file is your decision, but it requires
the .ini file extension. When you reference this answer file from the command line,
provide the full path to the file. For example, if your setup answer file is named
setup.ini , and it's stored in the C:\setup folder, your command line would be:

setup.exe /script c:\setup\setup.ini

  ） Important

  You need Administrator rights to run Configuration Manager setup. When you run
  setup with the unattended script, open the command prompt with the option to
  Run as administrator.

The script contains section names, key names, and values. Required section key names
vary depending on the recovery type that you need. The order of the keys within
sections and the order of sections within the file aren't important. The keys aren't case-
sensitive. When you provide values for keys, the name of the key is followed by an equal
sign ( = ) and the value for the key. For example, Action=RecoverCCAR .

For more information, see the following articles:

Command-line options for setup

Unattended setup script file keys

Feedback

<!-- p.1754 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1755 -->

Site failure impacts in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The site server and any of the other site systems can fail and cause a loss of the services
they regularly provide. If you install multiple site systems on the same computer, and
that computer fails, all services regularly provided by those site systems are no longer
available.

Part of your planning process should include understanding the impact on the service
that you provide your organization. Because each site system in the site provides
different functionality, the impact of a failure on the site differs, depending on the role
of the site system that failed.

Use high availability options to help mitigate the failure of any single system. Also plan
for and practice a backup and recovery strategy to reduce the amount of time the
service is unavailable.

The following sections describe the impact when the specified site system isn't
operational:

Site server
      No site administration is possible. You can't connect the console to the site.

      The management point collects client information and caches it until the site server
      is back online.

      Users can run existing deployments, and clients can download content from
      distribution points.

Site database
      No site administration is possible.

      If the Configuration Manager client already has a policy assignment with new
      policies, and if the management point has cached the policy body, the client can
      make a policy body request and receive the policy body reply. However, the site
      can't service any new policy assignment requests.

<!-- p.1756 -->

     Clients can run deployments, only if they've already received the policy, and the
     associated source files are already cached locally at the client.

Management point
     Although you can create new deployments, clients don't receive them until a
     management point is online.

     Clients still collect inventory, software metering, and status information. They store
     this data locally until the management point is available.

     Clients can run deployments, only if they've already received the policy, and the
     associated source files are already cached locally at the client.

Distribution point
     Configuration Manager clients can run deployments, only if the associated source
     files have already been downloaded locally or are available on a peer source.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1757 -->

Monitor the hierarchy
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To monitor your hierarchy in Configuration Manager, use the Monitoring workspace in
the Configuration Manager console.

  ７ Note

  The exception to this location is when migrating sites. Monitored this process in the
  Migration node of the Administration workspace. For more information, see
  Operations for migrating to Configuration Manager current branch.

Along with using the Configuration Manager console for monitoring, use the following
features:

      Introduction to reporting
      Log files.

When you monitor sites, look for signs that indicate problems that require you to take
action. For example:

      A backlog of files on site servers and site systems.

      Status messages that indicate an error or a problem.

      Failing intrasite communication.

      Error and warning messages in the system event log on servers.

      Error and warning messages in the Microsoft SQL Server error log.

      Sites or clients that haven't reported status in a long time.

      Sluggish response from the SQL Server database.

      Signs of hardware failure.

If monitoring tasks reveal any signs of problems, investigate the source of the problem.
Then quickly repair it to minimize the risk of a site failure.

Monitor common management tasks

<!-- p.1758 -->

Configuration Manager provides built-in monitoring from within the Configuration
Manager console.

Alerts
For more information, see Monitor alerts.

Compliance settings
For more information, see How to monitor compliance settings.

Content
For general information about monitoring content, see Manage content and content
infrastructure.

For more information about monitoring specific types of content:

     Monitor applications

     Monitor packages and programs

     Monitor content for software updates

     Monitor content for OS deployments

Endpoint Protection
For more information, see How to monitor Endpoint Protection.

OS deployment
For more information, see Monitor OS deployments.

Monitor power management
For more information, see How to monitor and plan for power management.

Monitor software metering
For more information, see Monitor app usage with software metering.

<!-- p.1759 -->

Monitor software updates
For more information, see Monitor software updates.

Monitor the site hierarchy
The Site Hierarchy node of the Monitoring workspace provides you with an overview of
your Configuration Manager hierarchy and intersite links.

Use the Site Hierarchy node to monitor the health of each site. Also monitor the
intersite replication links and their relationship to external factors, such as a
geographical location.

Both site status and intersite link status replicate as site data and not global data. When
you connect your Configuration Manager console to a child primary site, you can't view
the site or link status for other primary sites or their child secondary sites. For example,
in a hierarchy with multiple primary sites, when you connect the console to a primary
site, you can view the status of child secondary sites, the primary site, and the central
administration site. From this view, you can't see the status for other sites below the
central administration site.

To control the display in the Site Hierarchy node, use the Configure Settings action. The
hierarchy replicates the settings that you configure in this node.

Hierarchy diagram
The hierarchy diagram displays your sites in a topology map. Select a site, and view a
status message summary from that site. Drill through to view status messages, and
access the site Properties.

To view high-level status for a site or replication link between sites, hover your mouse
pointer over the object. Replication link status doesn't replicate globally. To view the
replication link details between all primary sites in a hierarchy, connect the console to
the central administration site.

The following options modify the hierarchy diagram:

Groups
Configure the number of primary sites and secondary sites that trigger a change in the
hierarchy diagram. This change in the display combines the sites into a single object.

<!-- p.1760 -->

Then you see the total number of sites and a high-level rollup of status messages and
site status.

Favorite sites

Specify individual sites to be a favorite site. A star icon identifies a favorite site in the
hierarchy diagram. Favorite sites aren't combined with others sites when you use
groups. They're always displayed individually.

Geographical view

  ） Important

  Starting in August 2020, this feature is deprecated. Use the Hierarchy Diagram
  option.

The geographical view displays the location of each site on a geographical map. It only
displays sites that you configure with a location. When you select a site in this view, it
shows replication links to parent or child sites. Unlike the hierarchy diagram view, you
can't display site status message or replication link details in this view.

  ７ Note

  To use the geographical view, the computer to which your Configuration Manager
  console connects must have Internet Explorer installed and be able to access Bing
  Maps by using the HTTP protocol.

The following option modifies the geographical view:

Site Location

Specify a geographical location for each site using one of the following types:

      A street address
      A place name such as the name of a city
      By latitude and longitude coordinates

For example, to use the latitude and longitude of Redmond, Washington, specify N 47
40 26.3572 W 122 7 17.4432 as the location of the site. You don't need to specify the
symbols for the degree, minutes, or seconds of latitude or longitude. Configuration
