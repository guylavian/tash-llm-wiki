---
title: "Core infrastructure documentation — pages 841-880"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0841-0880
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0841-0880
family: sccm
documentKind: "doc"
abstract: "You can migrate configuration items and configuration baselines. ７ Note Uninterpreted configuration items from Configuration Manager 2007 source hierarchies aren't supported for migration. You can't migrate or import these configuration items to the destination hierarchy. You ca"
---

# Core infrastructure documentation — pages 841-880

<!-- p.841 -->

You can migrate configuration items and configuration baselines.

  ７ Note

  Uninterpreted configuration items from Configuration Manager 2007 source
  hierarchies aren't supported for migration. You can't migrate or import these
  configuration items to the destination hierarchy.

You can import Configuration Manager 2007 Configuration Packs. The import process
automatically converts the configuration packs to be compatible with Configuration
Manager current branch.

Plan to migrate boundaries
You can migrate boundaries between hierarchies. When you migrate boundaries from
Configuration Manager 2007, each boundary from the source site migrates at the same
time and is added to a new boundary group that is created in the destination hierarchy.
When you migrate boundaries from a System Center 2012 Configuration Manager or
Configuration Manager current branch hierarchy, each boundary you select is added to
a new boundary group in the destination hierarchy.

Each automatically created boundary group is enabled for content location but not for
site assignment. This prevents overlapping boundaries for site assignment between the
source and destination hierarchies. When you migrate from a Configuration Manager
2007 source site, this helps prevent new Configuration Manager 2007 clients that install
from incorrectly assigning to the destination hierarchy. By default, Configuration
Manager current branch clients do not automatically assign to Configuration Manager
2007 sites.

During migration, if you share a distribution point with the destination hierarchy, any
boundaries that are associated with that distribution automatically migrate to the
destination hierarchy. In the destination hierarchy, migration creates a new read-only
boundary group for each shared distribution point. If you change the boundaries for the
distribution point in the source hierarchy, the boundary group in the destination
hierarchy updates with these changes during the next data gathering cycle.

Plan to migrate reports
Configuration Manager does not support the migration of reports. Instead, use SQL
Server Reporting Services Report Builder to export reports from the source hierarchy,

<!-- p.842 -->

and then import them to the destination hierarchy.

  ７ Note

  Because there are schema changes for reports between Configuration Manager
  2007 and Configuration Manager current branch, test each report that you import
  from a Configuration Manager 2007 hierarchy to ensure that it functions as
  expected.

For more about reporting, see Introduction to reporting.

Plan to migrate organizational and search
folders
You can migrate organizational folders and search folders from a supported source
hierarchy to a destination hierarchy. In addition, from a System Center 2012
Configuration Manager or Configuration Manager current branch source hierarchy, you
can migrate the criteria for a saved search to a destination hierarchy.

By default, the migration process maintains your search folder and administrative folder
structures for objects and collections when you migrate. However, in the Create
Migration Job wizard, on the Settings page, you can set up a migration job to not
migrate the organizational structure for objects by unchecking the box for this option.
The organizational structures of collections are always maintained.

One exception to this is a search folder that contains virtual applications. When an App-
V package is migrated, the App-V package is transformed into an application in
Configuration Manager. After migration of the search folder, only the remaining
packages are found, and the search folder cannot locate an App-V package because of
this conversion to an application when the App-V package migrates.

When you migrate a saved search from a System Center 2012 Configuration Manager or
Configuration Manager current branch source hierarchy, you migrate the criteria for the
search, and not the information about the search results. Migration of a saved search is
not applicable from a Configuration Manager 2007 source site.

Plan to migrate Asset Intelligence
customizations

<!-- p.843 -->

You can migrate customizations for Asset Intelligence from a supported source hierarchy
to a destination hierarchy. There are no significant changes to the structure of Asset
Intelligence customizations between Configuration Manager 2007 and Configuration
Manager current branch.

  ７ Note

  Configuration Manager current branch doesn't support the migration of Asset
  Intelligence objects from a Configuration Manager 2007 site that is using Asset
  Intelligence Service 2.0 (AIS 2.0).

Plan to migrate software metering rules
customizations
There are no significant changes to software metering between Configuration Manager
2007 and Configuration Manager current branch. You can migrate your software
metering rules from a supported source hierarchy to a destination hierarchy.

By default, software metering rules that you migrate to a destination hierarchy are not
associated with a specific site in the destination hierarchy and instead apply to all clients
in the hierarchy. To apply a software metering rule to clients at a specific site, you must
edit the metering rule after it migrates.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.844 -->

Planning to monitor migration activity
in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

With Configuration Manager, you can monitor migration in the Configuration Manager
console that connects to the destination hierarchy. In the Configuration Manager
console in the Administration workspace, you can use the Migration node to monitor
the progress and success of migration jobs. You can view summary information for each
migration job that identifies objects that have migrated, those objects that have not yet
migrated, and the number of objects that are excluded from a migration job. You will
also see details about any migration problems.

View Migration Progress
To view the progress of a migration job, use any of the following actions:

      In the Administration workspace of the Configuration Manager console, expand
      the Migration Jobs node, select a migration job, and then select the Objects in
      Job tab.

      Use the Configuration Manager log files to review the migration progress or to
      identify any problems. Migration Manager is the Configuration Manager process
      that tracks migration actions and records these in the migmctrl.log file in the
      &lt;InstallationPath>\LOGS folder on the site server.

        ７ Note

        If a migration job fails, review the details in the migmctrl.log file as soon as
        possible. The migration log entries are continually added to the file and
        overwrite old details. If the entries are overwritten, you might not be able to
        identify whether any problems that you might encounter with the migrated
        objects relate to migration issues. Migration activity is logged at the top-level
        site of the hierarchy regardless of the site your Configuration Manager
        console connects to when you configure migration.

      Use Configuration Manager reporting. Configuration Manager provides several
      built-in reports for migration, or you can edit those reports to fit your

<!-- p.845 -->

     requirements. For more information about Configuration Manager reports, see
     Introduction to reporting.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.846 -->

Plan to complete migration in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

With Configuration Manager, you can complete the process of migration when a source
hierarchy no longer has data that you want to migrate to your destination hierarchy.
Completing migration includes the following general steps:

      Ensure that data you require has migrated. Before you complete migration from a
      source hierarchy, make sure that you have successfully migrated all of the
      resources from the source hierarchy that you require in the destination hierarchy.
      This can include data and clients.

      Stop gathering data from source sites. To complete migration from a source
      hierarchy, you must first stop gathering data from source sites.

      Clean up migration data. After you stop gathering data from all source sites in a
      source hierarchy, you can remove data about the migration process and source
      hierarchy from the database of the destination hierarchy.

      Decommission the source hierarchy. After you complete migration from a source
      hierarchy and that hierarchy no longer has resources that you manage, you can
      decommission the sites in the source hierarchy and remove the related
      infrastructure from your environment. For information about how to decommission
      sites and source hierarchies, consult the documentation for that version of
      Configuration Manager.

Use the following sections to help you plan to complete migration from a source
hierarchy by stopping data gathering and cleaning up migration data:

      Plan to stop gathering data

      Plan to clean up migration data

Plan to stop gathering data
Before you complete migration and clean up migration data, you must stop gathering
data from each source site in the source hierarchy. To stop gathering data from each
source site, you must perform the Stop Gathering Data command on the bottom tier

<!-- p.847 -->

source sites, and then repeat the process at each parent site. The top-level site of the
source hierarchy must be the last site on which you stop gathering data. You must stop
data gathering at each child site before performing this command on a parent site.
Typically, you only stop gathering data when you are ready to finish the migration
process.

After you stop gathering data from a source site, shared distribution points from that
site are no longer available as content locations for clients in the destination hierarchy.
Therefore, ensure that any migrated content that the clients in the destination hierarchy
require access to remains available by using one of the following options:

     In the destination hierarchy, distribute the content to at least one distribution
     point.

     Before you stop gathering data from a source site, upgrade or reassign shared
     distribution points that have the required content. For more about upgrading or
     reassigning shared distribution points, see the applicable sections in Planning a
     content deployment migration strategy.

After you stop gathering data from each source site in the source hierarchy, you can
clean up migration data. Until you clean up migration data, each migration job that has
run or that is scheduled to run remains accessible in the Configuration Manager
console.

For more about source sites and data gathering, see Planning a source hierarchy
strategy.

Plan to clean up migration data
The last step required to finish migration is to clean up migration data. You can use the
Clean Up Migration Data command after you have stopped gathering data for each
source site in the source hierarchy. This optional action removes data about the current
source hierarchy from the database of the destination hierarchy.

When you clean up migration data, most data about the migration is removed from the
database of the destination hierarchy. However, details about migrated objects are
retained. With these details, you can use the Migration workspace to reconfigure the
source hierarchy that has the data that was migrated to resume migration from that
source hierarchy, or to review the objects and site ownership of the objects that
previously migrated.

<!-- p.848 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.849 -->

Configure source hierarchies and source
sites for migration to Configuration
Manager current branch
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To enable migration of data to your Configuration Manager current branch
environment, you must configure a supported Configuration Manager source hierarchy
and one or more source sites in that hierarchy that contain data that you want to
migrate.

  ７ Note

  Operations for migration are run at the top-level site in the destination hierarchy. If
  you configure migration when you use a Configuration Manager console that is
  connected to a primary child site, you must allow time for the configuration to
  replicate to the central administration site, start, and then replicate status back to
  the primary site to which you are connected.

Use the information and procedures in the following sections to specify the source
hierarchy and add additional source sites. After you finish these procedures, you can
create migration jobs and start to migrate data from the source hierarchy to the
destination hierarchy.

      Specify a source hierarchy for migration

      Identify additional source sites of the source hierarchy

Specify a source hierarchy for migration
To migrate data to your destination hierarchy, you must specify a supported source
hierarchy that has the data that you want to migrate. By default, the top-level site of
that hierarchy becomes a source site of the source hierarchy. If you migrate from a
Configuration Manager 2007 hierarchy, you can then set up additional source sites for
migration after data is gathered from the initial source site. If you migrate from a System
Center 2012 Configuration Manager or Configuration Manager current branch hierarchy,
you do not have to set up additional source sites to migrate data from the source
hierarchy. This is because these versions of Configuration Manager use a shared

<!-- p.850 -->

database that is available at the top-level site of the source hierarchy. The shared
database has all the information that you can migrate.

Use the following procedures to specify a source hierarchy for migration and to identify
additional source sites in a Configuration Manager 2007 hierarchy.

Run this procedure with a Configuration Manager console that is connected to the
destination hierarchy:

To configure a source hierarchy
   1. In the Configuration Manager console, click Administration.

   2. In the Administration workspace, expand Migration, and then click Source
     Hierarchy.

   3. On the Home tab, in the Migration group, click Specify Source Hierarchy.

   4. In the Specify Source Hierarchy dialog box, for Source Hierarchy, select New
     source hierarchy.

   5. For Top-level Configuration Manager site server, enter the name or IP address of
     the top-level site of a supported source hierarchy.

   6. Specify source site access accounts that have the following permissions:

           Source Site Account: Read permission to the SMS Provider for the specified
           top-level site in the source hierarchy. Distribution point sharing and upgrades
           require Modify and Delete permissions to the site in the source hierarchy.

           Source Site Database Account: Read and Execute permission to the SQL
           Server database for the specified top-level site in the source hierarchy.

           If you specify the use of the computer account, Configuration Manager uses
           the computer account of the top-level site of the destination hierarchy. For
           this option, ensure that this account is a member of the security group
           Distributed COM Users in the domain where the top-level site of the source
           hierarchy resides.

   7. To share distribution points between the source and destination hierarchies, select
     the Enable distribution point sharing for the source site server check box. If you
     do not enable distribution point sharing at this time, you can do so by editing the
     credentials of the source site after data gathering has finished.

<!-- p.851 -->

   8. Click OK to save the configuration. This opens the Data Gathering Status dialog
     box, and data gathering starts automatically.

   9. When data gathering finishes, click Close to close the Data Gathering Status
     dialog box and complete the configuration.

Identify additional source sites of the source
hierarchy
When you configure a supported source hierarchy, the top-level site of that hierarchy is
automatically configured as a source site, and data is automatically gathered from that
site. The next action that you take depends on the version of Configuration Manager
that is run by the source hierarchy:

     For a Configuration Manager 2007 source hierarchy, you can begin migration from
     that initial source site or set up additional source sites from the source hierarchy
     after the data gathering finishes for the initial source site. To migrate data that is
     only available from a child site, set up additional source sites for a Configuration
     Manager 2007 hierarchy. For example, you might configure additional source sites
     to gather data about content that you want to migrate when it's created at a child
     site in the source hierarchy and is not available at the top site of the source
     hierarchy.

     For a System Center 2012 Configuration Manager or Configuration Manager
     current branch source hierarchy, you do not need to configure additional source
     sites. This is because these versions of Configuration Manager use a shared
     database that is available at the top-level site of the source hierarchy. The shared
     database has all the information that you can migrate from all of the sites in that
     source hierarchy. This makes the data that you can migrate available from the top-
     level site of the source hierarchy.

When you configure additional source sites for a Configuration Manager 2007 source
hierarchy, you must configure the additional source sites from the top of the source
hierarchy to the bottom. You must configure a parent site as a source site before you
configure any of its child sites as source sites.

Use the following procedure to configure additional source sites for Configuration
Manager 2007 source hierarchies:

To identify additional source sites in the source hierarchy
   1. In the Configuration Manager console, click Administration.

<!-- p.852 -->

   2. In the Administration workspace, expand Migration, and then click Source
     Hierarchy.

   3. Choose the site that you want to configure as a source site.

   4. On the Home tab, in the Source Site group, click Configure.

   5. In the Source Site Credentials dialog box, for the source site access accounts,
     specify accounts that have the following permissions:

             Source Site Account: Read permission to the SMS Provider for the specified
           top-level site in the source hierarchy. Distribution point sharing and upgrades
           require Modify and Delete permissions to the site in the source hierarchy.

           Source Site Database Account: Read and Execute permission to the SQL
           Server database for the specified top-level site in the source hierarchy.

     If you specify the use of the computer account, Configuration Manager uses the
     computer account of the top-level site of the destination hierarchy. For this option,
     ensure that this account is a member of the security group Distributed COM Users
     in the domain where the top-level site of the source hierarchy resides.

   6. To share distribution points between the source and destination hierarchies, select
     the Enable distribution point sharing for the source site server check box. If you
     do not enable distribution point sharing at this time, you can do so by editing the
     credentials for the source site after data gathering has finished.

   7. Click OK to save the configuration. This opens the Data Gathering Status dialog
     box, and data gathering starts automatically.

   8. When data gathering finishes, click Close to complete the configuration.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.853 -->

Operations for migrating to
Configuration Manager current branch
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

For migration in Configuration Manager, you can migrate data and clients after you
successfully gather data from a source site in a supported source hierarchy. Use the
information in the following sections to create and run migration jobs to migrate data
and clients, and then finish the migration process.

      Create and edit migration jobs

      Run migration jobs

      Upgrade or reassign a shared distribution point

      Monitor migration activity in the Migration workspace

      Migrate clients

      Finish migration

Create and edit migration jobs
Use the following procedures to create data migration jobs, edit the exclusion list for
collection-based migration jobs, set up shared distribution points, and edit migration
job schedules.

  ７ Note

  The following procedure for creating a migrating job that migrates by collections
  applies only to source hierarchies that run a supported version of Configuration
  Manager 2007. The collection-based migration job type is not available when you
  migrate from a System Center 2012 Configuration Manager or Configuration
  Manager current branch source hierarchy.

Create a migration job to migrate by collections

   1. In the Configuration Manager console, choose Administration.

<!-- p.854 -->

 2. In the Administration workspace, expand Migration, and then choose Migration
   Jobs.

 3. On the Home tab, in the Create group, choose Create Migration Job.

 4. On the General page of the Create Migration Job wizard, set up the following and
   then choose OK:

           Specify a name for the migration job.

           In the Job type drop-down list, select Collection migration.

 5. On the Select Collections page, set up the following and then choose Next:

           Select the collections that you want to migrate.

           If you want to migrate only collections and not the objects that are
           associated with those collections, uncheck Migrate objects that are
           associated with the specified collections. If you uncheck this option, no
           associated objects are migrated in this job, and you can skip steps 6 and 7.

 6. On the Select Objects page, uncheck any object types or specific available objects
   that you do not want to migrate. By default, all associated object types and
   available objects are selected. Choose Next.

 7. On the Content Ownership page, assign the ownership of content from each listed
   source site to a site in the destination hierarchy, and then choose Next.

 8. On the Security Scope page, select one or more role-based administration security
   scopes to assign to the objects to migrate in this migration job, and then choose
   Next.

 9. On the Collection Limiting page, set up a collection from the destination hierarchy
   to limit the scope of each listed collection, and then choose Next. If no collections
   are listed, choose Next.

10. On the Site Code Replacement page, assign a site code from the destination
   hierarchy to replace the Configuration Manager 2007 site code for each listed
   collection, and then choose Next. If no collections are listed, choose Next.

11. On the Review Information page, choose Save To File to save the displayed
   information for later viewing. When you are ready to continue, choose Next.

12. On the Settings page, set up when the migration job will run, choose any
   additional settings that you need for this migration job, and then choose Next.

<!-- p.855 -->

 13. Confirm the settings and finish the wizard.

Create a migration Job to migrate by objects
  1. In the Configuration Manager console, choose Administration.

  2. In the Administration workspace, expand Migration, and then choose Migration
    Jobs.

  3. On the Home tab, in the Create group, choose Create Migration Job.

  4. On the General page of the Create Migration Job wizard, set up the following, and
    then choose Next:

            Specify a name for the migration job.

            In the Job type drop-down list, select Object migration.

  5. On the Select Objects page, select the object types that you want to migrate. By
    default, all available objects are selected for each object type that you select.

  6. On the Content Ownership page, assign the ownership of content from each listed
    source site to a site in the destination hierarchy, and then choose Next. If no
    source sites are listed, choose Next.

  7. On the Security Scope page, select one or more role-based administration security
    scopes to assign to the objects in this migration job, and then choose Next.

  8. On the Review Information page, choose Save To File to save the displayed
    information for later viewing. When you are ready to continue, choose Next.

  9. On the Settings page, set up when the migration job will run and choose any
    additional settings that you need for this migration job. Then choose Next.

 10. Confirm the settings and finish the wizard.

Create a migration job to migrate changed objects
  1. In the Configuration Manager console, choose Administration.

  2. In the Administration workspace, expand Migration, and then choose Migration
    Jobs.

  3. On the Home tab, in the Create group, choose Create Migration Job.

<!-- p.856 -->

  4. On the General page of the Create Migration Job wizard, set up the following and
    then choose Next:

           Specify a name for the migration job.

           In the Job type drop-down list, select Objects modified after migration.

  5. On the Select Objects page, select the object types that you want to migrate. By
    default, all available objects are selected for each object type that you select.

  6. On the Content Ownership page, assign the ownership of content from each listed
    source site to a site in the destination hierarchy, and then choose Next. If no
    source sites are listed, choose Next.

  7. On the Security Scope page, select one or more role-based administration security
    scopes to assign to the objects in this migration job, and then choose Next.

  8. On the Review Information page, choose Save To File to save the displayed
    information for later viewing. When you are ready to continue, choose Next.

  9. On the Settings page, set up when the migration job will run and choose any
    additional settings that you require for this migration job. Unlike the other
    migration job types, this migration job must overwrite the previously migrated
    objects in the Configuration Manager database. Choose Next.

 10. Confirm the settings and then finish the wizard.

Modify the exclusion list for migration
  1. In the Configuration Manager console, choose Administration.

  2. In the Administration workspace, choose Migration to gain access to the exclusion
    list. You can also access the exclusion list from the Source Hierarchy or Migration
    Jobs node.

  3. On the Home tab, in the Migration group, choose Edit Exclusion List.

  4. In the Edit Exclusion List dialog box, select the excluded object that you want to
    remove from the exclusion list, and then choose Remove.

  5. Choose OK to save the changes and finish the edit. To cancel current changes and
    restore all the objects that you have removed, choose Cancel, and then choose No.
    This will cancel the removal of the objects, and close the Edit Exclusion List dialog
    box.

<!-- p.857 -->

Share distribution points from the source hierarchy
   1. In the Configuration Manager console, choose Administration.

   2. In the Administration workspace, expand Migration, choose Source Hierarchy,
     and then select the source site that you want to set up.

   3. On the Home tab, in the Source Site group, choose Configure.

   4. On the Source Site Credentials dialog box, select Enable distribution point
     sharing for the source site server, and then choose OK.

   5. When data gathering finishes, choose Close.

Change the schedule of a migration job
   1. In the Configuration Manager console, choose Administration.

   2. In the Administration workspace, expand Migration, and then choose Migration
     Jobs.

   3. Choose the migration job that you want to change. On the Home tab, in the
     Properties group, choose Properties.

   4. In the properties of the migration job, select the Settings tab, change the run time
     for the migration job, and then choose OK.

Run migration jobs
Use the following procedure to run a migration job that has not yet started.

   1. In the Configuration Manager console, choose Administration.

   2. In the Administration workspace, expand Migration, and then choose Migration
     Jobs.

   3. Choose the migration job that you want to run. On the Home tab, in the Migration
     Job group, choose Start.

   4. Choose Yes to start the migration job.

Upgrade or reassign a shared distribution point

<!-- p.858 -->

You can upgrade a supported distribution point that is shared from a Configuration
Manager 2007 source site (or reassign a supported distribution point that is shared from
a Configuration Manager source site) to be a distribution point in the destination
hierarchy.

  ） Important

  Before you upgrade a Configuration Manager 2007 branch distribution point, you
  must uninstall the Configuration Manager 2007 client software from the branch
  distribution point computer. If the Configuration Manager 2007 client software is
  installed when you attempt to upgrade the distribution point, the upgrade fails and
  content that was previously deployed to the branch distribution point is removed
  from the computer.

  Ｕ Caution

  When you upgrade or reassign a shared distribution point, the distribution point
  site system role and site system computer are removed from the source site and
  added as a distribution point to the site in the destination hierarchy that you select.

Upgrade or reassign a shared distribution point
   1. In the Configuration Manager console, choose Administration.

   2. In the Administration workspace, expand Migration, and then choose Source
     Hierarchy.

   3. Select the site that owns the distribution point you want to upgrade, choose the
     Shared Distribution Points tab, and select the eligible distribution point that you
     want to upgrade or reassign.

   4. On the Distribution Point tab, in the Distribution Point group, choose Reassign.

   5. Specify settings in the Reassign Shared Distribution Point wizard like you are
     installing a new distribution point for the destination hierarchy, with the following
     addition:

             On the Content Conversion page, review the guidance about the space
             required to convert the existing content. Then, on the Drive Settings page of
             the wizard, ensure that the drive of the distribution point computer that is
             selected has the required amount of free disk space.

<!-- p.859 -->

   6. Confirm the settings and then finish the wizard.

Monitor migration activity in the Migration
workspace
Use the Configuration Manager console to monitor migration.

   1. In the Configuration Manager console, choose Administration.

   2. In the Administration workspace, expand Migration, and then choose Migration
     Jobs.

   3. Choose the migration job that you want to monitor.

   4. View details and status about the selected migration job on the tabs for Summary
     and Objects in Job.

Migrate clients
After you migrate data for clients between hierarchies but before you finish migration,
plan to migrate clients to the destination hierarchy. The migration of clients between
hierarchies involves uninstalling the Configuration Manager client software from
computers that are assigned to the source hierarchy, and then installing the
Configuration Manager client software from the destination hierarchy. When you install
the client from the destination hierarchy you also assign the client to a primary site in
that hierarchy. For more about migrating clients, see Planning a client migration
strategy.

Finish migration
Use this procedure to finish migration from the source hierarchy.

   1. In the Configuration Manager console, choose Administration.

   2. In the Administration workspace, expand Migration, and then choose Source
     Hierarchy.

   3. For a Configuration Manager 2007 source hierarchy, select a source site that is at
     the bottom level of the source hierarchy. For a System Center 2012 Configuration
     Manager or Configuration Manager current branch source hierarchy, select the
     available source site.

<!-- p.860 -->

   4. On the Home tab, in the Clean Up group, choose Stop Gathering Data.

   5. Choose Yes to confirm the action.

   6. For a Configuration Manager 2007 source hierarchy, before you continue to the
     next step, repeat steps 3, 4, and 5. Go through these steps at each site in the
     hierarchy, from the bottom of the hierarchy to the top. For a System Center 2012
     Configuration Manager or Configuration Manager current branch source hierarchy,
     continue to the next step.

   7. On the Home tab, in the Clean Up group, choose Clean Up Migration Data.

   8. On the Clean Up Migration Data dialog box, from the Source hierarchy drop-
     down list, select the site code and site server of the top-level site of the source
     hierarchy, and then choose OK.

   9. Choose Yes to finish the migration process for the source hierarchy.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.861 -->

Security and privacy for migration to
Configuration Manager current branch
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic contains security best practices and privacy information for migration to your
Configuration Manager current branch environment.

Security Best Practices for Migration
Use the following security best practice for migration.

                                                                                    ﾉ   Expand table

 Security best practice                  More information

 Use the computer account for the        If you must use a user account for migration, remove the
 Source Site SMS Provider Account        account details when migration is completed.
 and the Source Site SQL Server
 Account rather than a user account.

 Use IPsec when you migrate content      Although the migrated content is hashed to detect
 from a distribution point in a source   tampering, if the data is modified while it is transferred,
 site to a distribution point in your    the migration will fail.
 destination site.

 Restrict and monitor the                The integrity of the database of the destination hierarchy
 administrative users who can create     depends upon the integrity of data that the administrative
 migration jobs.                         user chooses to import from the source hierarchy. In
                                         addition, this administrative user can read all data from
                                         the source hierarchy.

Security Issues for Migration
Migration has the following security issues:

      Clients that are blocked from a source site might successfully assign to the
      destination hierarchy before their client record is migrated.

      Although Configuration Manager retains the blocked status of clients that you
      migrate, the client can successfully assign to the destination hierarchy if
      assignment occurs before the migration of the client record is completed.

<!-- p.862 -->

     Audit messages are not migrated.

When you migrate data from a source site to a destination site, you lose any auditing
information from the source hierarchy.

Privacy Information for Migration
Migration discovers information from the site databases that you identify in a source
infrastructure and stores this data to the database in the destination hierarchy. The
information that Configuration Manager can discover from a source site or hierarchy
depends upon the features that were enabled in the source environment, as well as the
management operations that were performed in that source environment.

For more information about security and privacy information, see Security and privacy
for Configuration Manager.

You can migrate some or all of the supported data from a source site to a destination
hierarchy.

Migration is not enabled by default and requires several configuration steps. Migration
information is not sent to Microsoft.

Before you migrate data from a source hierarchy, consider your privacy requirements.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.863 -->

Deploy servers and roles
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you plan out your Configuration Manager site and hierarchy topology and are
ready to get sites installed or upgraded, use the information in the following articles:

      Install Configuration Manager sites

      Upgrade to Configuration Manager

      Scenarios to streamline your installation of Configuration Manager

      Configure sites and hierarchies

      Migrate data between hierarchies

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.864 -->

Where to get installation media for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If you have Configuration Manager volume licenses with Software Assurance, or if you
have purchased licenses for Configuration Manager volume licenses, you can download
baseline source media to install Configuration Manager from the Volume Licensing
Service Center    .

If you have a Configuration Manager license from EMS, Microsoft 365, or a Cloud
Solution Provider (CSP), please see the Product and Licensing FAQ.

If you would like to purchase volume licenses for Configuration Manager, contact your
preferred Microsoft Reseller or see How to purchase through Volume Licensing      . You
can also download media to install an evaluation edition of Configuration Manager from
the Evaluation Center       website.

To learn about baseline media for Configuration Manager, see Baseline and update
versions.

Feedback
Was this page helpful?      Yes        No

Provide product feedback

<!-- p.865 -->

Reference for Configuration Manager
Setup
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager Setup provides links to several topics that are detailed in the
following sections. The information presented here can help you prepare to install a
Configuration Manager site or hierarchy, and help prepare you for some of the decisions
you must make during the installation.

Before you begin
Before you install new Configuration Manager sites, make sure you have reviewed the
following information, which can help set the stage for a successful deployment design:

      Fundamentals of Configuration Manager
      Plan for Configuration Manager infrastructure
      Prepare to install Configuration Manager sites

Assess server readiness
Before you begin the installation of a new site, make sure that the site server and the
remote site system servers you plan to use for the site (for example, the server that
hosts the site database) meet all prerequisite configurations. These topics in the
documentation library can help:

      Supported configurations for Configuration Manager
      Prerequisite Checker

Usage data levels and settings
When you install your first Configuration Manager site, Configuration Manager
automatically installs and configures a new site system role, the service connection
point, on the site server. The service connection point has these default settings:

      Online mode (an offline mode also is available)
      Enhanced data collection level (two other data collection levels, Basic and Full, also
      are available)

<!-- p.866 -->

When the service connection point site system role is online, Microsoft can
automatically collect diagnostics and usage information over the Internet. Information
that is collected helps us:

     Identify and troubleshoot problems
     Improve our products and service
     Identify updates for Configuration Manager that apply to the version of
     Configuration Manager you use

Levels of data collection
Data collection includes these three levels:

     Basic includes data about setup and upgrade, like the number of sites and which
     Configuration Manager features are enabled. No personally identifiable
     information is transmitted.

     Enhanced includes the data in the Basic level setting, plus it transmits data about
     the hierarchy, how each feature is used (frequency and duration), and enhanced
     diagnostic information like the memory state of your server when a system or app
     crash occurs. No personally identifiable data is transmitted.

     Full includes the data in the Basic and Enhanced level settings, and it also sends
     advanced diagnostic information like system files and memory snapshots. This
     option might include personally identifiable information, but we won't use that
     information to identify or contact you, or to target advertising to you.

For more information, including disclosure of the details collected by each level, see
Diagnostics and usage data for Configuration Manager.

For more information, see the Microsoft Privacy Statement     .

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.867 -->

Setup Downloader for Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before you run Configuration Manager setup to install or upgrade a site, you can use
the setup downloader standalone tool to download updated setup files. Run the tool
from the version of Configuration Manager that you want to install. Use updated setup
files to make sure your site installation uses current versions of key installation files.

When you use setup downloader, you specify a folder to contain the files. The account
you use to run the tool must have Full Control permissions to the download folder.
When you run setup to install or upgrade a site, you can specify this local copy of files
you previously downloaded. This behavior prevents setup from connecting to Microsoft
when you start the site install or upgrade. You can use the same local copy of setup files
for other site installations or upgrades of the same version.

The setup downloader tool downloads the following types of files:

      Required prerequisite redistributable files
      Language packs
      The latest product updates for setup

You have two options to run setup downloader:

      Run the application with the user interface
      Run the application at a command prompt for additional command-line options

If your organization restricts network communication with the internet using a firewall or
proxy device, you need to allow the tool to access internet endpoints. The device where
you'll run the tool requires internet access the same as the service connection point. For
more information, see Internet access requirements.

Run setup downloader with the user interface
   1. On a computer that has internet access, browse to the installation media for the
      version of Configuration Manager that you want to install.

   2. In the SMSSETUP\BIN\X64 subfolder, run Setupdl.exe.

<!-- p.868 -->

  3. Specify the path for the folder to store the updated installation files, and then
     select Download. Setup downloader verifies the files that are currently in the
     download folder. It downloads only files that are missing or that are newer than
     existing files. It creates subfolders for downloaded languages, and other required
     components.

  4. To review the download results, see C:\ConfigMgrSetup.log.

Run setup downloader from a command
prompt
  1. Open a command prompt, and change directory to the installation media for the
     version of Configuration Manager that you want to install.

  2. Change directory to the SMSSETUP\BIN\X64 subfolder, and run Setupdl.exe with
     the necessary options.

  3. To review the download results, see C:\ConfigMgrSetup.log.

Command-line options
You can use the following command-line options with Setupdl.exe:

     /VERIFY : Verify the files in the download folder, which include language files. For

     the list of outdated files, review C:\ConfigMgrSetup.log. When you use this option,
     it doesn't download any files.

     /VERIFYLANG : Only verify the language files in the download folder. For the list of

     outdated language files, review C:\ConfigMgrSetup.log.

     /LANG : Download only the language files to the download folder.

     /NOUI : Start setup downloader without the user interface. When you use this

     option, the download path is required.

     Download path: To automatically start the verification or download process,
     specify the path to the download folder. When you use the /NOUI option, the
     download path is required. If you don't specify a download path, setup
     downloader prompts you to specify the path. If the folder doesn't exist, setup
     downloader creates it.

Example commands

<!-- p.869 -->

Example 1
Setup downloader verifies the files in the specified download folder, and then
downloads files.

setupdl.exe C:\Download

Example 2

Setup downloader only verifies the files in the specified download folder.

setupdl.exe /VERIFY C:\Download

Example 3
Setup downloader verifies the files in the specified download folder, and then
downloads files. The tool doesn't show any user interface.

setupdl.exe /NOUI C:\Download

Example 4

Setup downloader verifies the language files in the specified download folder, and then
downloads only the language files.

setupdl.exe /LANG C:\Download

Copy setup downloader files to another
computer
   1. In Windows Explorer, go to either one of the following locations:

          <Configuration Manager installation media>\SMSSETUP\BIN\X64

          <Configuration Manager installation path>\BIN\X64

   2. Copy the following files to the same destination folder on the other computer:

          setupdl.exe

          .\<language>\setupdlres.dll

             ７ Note

<!-- p.870 -->

              This file is in the subfolder for the install language. For instance, English
              is in the 00000409 subfolder.

     The destination folders on your device should look like the following example:

            C:\ConfigManInstall\setupdl.exe

            C:\ConfigManInstall\00000409\setupdlres.dll

   3. Run the setup downloader from the destination computer. Use either the user
     interface or the command prompt.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.871 -->

Prerequisite Checker for Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before you run Setup to install or upgrade a Configuration Manager site, or before you
install a site system role on a new server, you can use this stand-alone application
(Prereqchk.exe) from the version of Configuration Manager that you want use to verify
server readiness. Use Prerequisite Checker to identify and fix problems that would block
a site or site system role installation.

  ７ Note

  Prerequisite Checker always runs as part of Setup.

By default, when Prerequisite Checker runs:

      It validates the server where it runs.
      The local computer is scanned for an existing site server, and only the checks that
      are applicable to the site are run.
      If no existing sites are detected, all prerequisite rules are run.
      It checks rules to verify that software and settings required for setup are installed.
      It's possible that some prerequisites require other configurations or software
      updates that the tool doesn't check.
      It logs its results in the ConfigMgrPrereq.log file on the system drive of the
      computer. The log file might contain more information that doesn't appear in the
      tool.

When you run Prerequisite Checker at a command prompt and specify specific
command-line options:

      Prerequisite Checker only runs the checks that are associated with the site server or
      site systems that you specify in the command line.
      To check a remote computer, your user account must have Administrator rights to
      the remote computer.

For more information, see List of prerequisite checks.

Source folders

<!-- p.872 -->

By default, the prerequisite checker tool is in one of the following locations:

      <Configuration Manager installation media>\SMSSETUP\BIN\X64

      <Configuration Manager installation path>\BIN\X64

Copy to another computer
   1. In Windows Explorer, go to one of the X64 source folders.

   2. Copy the following files to the destination folder on the other computer:

           prereqchk.exe
           prereqcore.dll
           prereqchkres.dll This file is in the subfolder for the install language. For
           example, English is in the 00000409 subfolder.
           basesql.dll
           basesvr.dll
           baseutil.dll

Run with default checks
   1. In Windows Explorer, go to one of the X64 source folders.

   2. Run prereqchk.exe to start Prerequisite Checker.

  ７ Note

  The tool requires administrative permissions on the local computer.

Prerequisite Checker detects existing sites, and if found, runs the checks for upgrade
readiness. If no sites are found, it runs all checks. The Site Type column provides
information about the site server or site system with which the rule is associated.

In the Prerequisite Checker user interface, Prerequisite Checker creates a list of
discovered problems in the Prerequisite result section.

     Select an item in the list for details about how to resolve the problem.
     Before you install the component, resolve all items in the list that have an Error
     status.
     To review results after you close the tool, open the ConfigMgrPrereq.log file in the
     root of the system drive. The log file might contain more information that's not

<!-- p.873 -->

        displayed in the tool.

Run from a command prompt
   1. Open a Windows command prompt as an administrator and change directory to
        one of the X64 source folders.

   2. To start Prerequisite Checker and run all prerequisite checks on the server, run the
        following command: prereqchk.exe /LOCAL

You can also run it with other command-line options. For example, to check a primary
site:

prereqchk.exe /PRI /SQL sql01.contoso.com /SDK cmprov01.contoso.com /JOIN

cas.contoso.com /MP mp01.contoso.com /DP dp01.contoso.com

Command-line options
There are four installation scenarios. The following list summarizes all of the command-
line options for each scenario:

        Central administration site (CAS)
          Required

<!-- p.874 -->

           /CAS
           /SDK

           /SQL

        Optional
           /EXPAND

           /INSTALLDIR
           /NOUI

           /SCP
           /SSBPORT

     Primary site
        Required
           /PRI

           /SDK
           /SQL

        Optional
           /DP
           /INSTALLDIR

           /JOIN
           /MP

           /NOUI

           /SCP
           /SSBPORT

     Secondary site
        Required
           /SEC

        Optional
           /INSTALLDIR

           /INSTALLSQLEXPRESS
           /NOUI

           /SECUPGRADE
           /SOURCEDIR

           /SQLPORT

           /SSBPORT

     Configuration Manager console
        /ADMINUI

For more information on these options, see the following sections.

<!-- p.875 -->

/AdminUI

Applies to: Console

Required. This option verifies that the local computer meets the requirements for
installing the Configuration Manager console. It doesn't check any server requirements.
You can't combine this option with any other option.

/CAS

Applies to: CAS

Required. This option verifies that the local server meets the requirements for the CAS.
You can't combine it with the /PRI or /SEC options.

/DP

Applies to: Primary

Optional. Specify the FQDN of the server to host the distribution point role, for example:
/PRI /DP dp01.contoso.com

This option verifies that the specified server meets the requirements for the distribution
point site system role. This option can be used alone or with the /PRI option.

/Expand

Applies to: CAS

Optional. Specify the FQDN of a primary site, for example: /CAS /EXPAND
cmprimary.contoso.com

This option verifies that the referenced primary site meets the requirements to expand a
hierarchy with a CAS.

/InstallDir

Applies to: CAS, Primary, Secondary

Optional. Specify the local installation path, for example /InstallDir C:\ConfigMgr

This option verifies the minimum disk space for site installation.

<!-- p.876 -->

/InstallSQLExpress

Applies to: Secondary

Optional. This option verifies that SQL Server Express can be installed on the specified
secondary site server.

/Join

Applies to: Primary

Optional. Specify the FQDN of the CAS server, for example, /PRI /JOIN cas.contoso.com

This option verifies that the local server meets the requirements for connecting to the
CAS server.

/MP

Applies to: Primary

Optional. Specify the FQDN of the server to host the management point role, for
example: /PRI /MP mp01.contoso.com

This option verifies that the specified server meets the requirements for the
management point site system role. This option can be used alone or with the /PRI
option.

/NoUI

Applies to: CAS, Primary, Secondary

Optional. This option starts the prerequisite checker without displaying the user
interface. Specify this option before any other option in the command line.

/Pri

Applies to: Primary

Required. This option verifies that the local server meets the requirements for a primary
site. You can't combine it with the /CAS or /SEC options.

/SCP

<!-- p.877 -->

Applies to: CAS, Primary

Optional. Specify the FQDN of the server to host the service connection point. This
server may be the same as the site server.

Starting in version 2111, this option verifies that the specified computer meets the
requirements for the service connection point site system role. You can use this option
alone or with the /PRI or /CAS options.

/SDK

Applies to: CAS, Primary

Required. Specify the FQDN of the server to host the SMS Provider role. This server may
be the same as the site server.

This option verifies that the specified server meets the requirements for the SMS
Provider.

/Sec

Applies to: Secondary

Required. Specify the FQDN of the secondary site server, for example: /SEC
sec01.contoso.com

This option verifies that the specified server meets the requirements for the secondary
site. You can't combine it with the /CAS or /PRI options.

/SecUpgrade

Applies to: Secondary

Optional. Specify the FQDN of the secondary site server, for example: /SECUPGRADE
sec01.contoso.com

This option verifies that the specified server meets the requirements for the secondary
site upgrade. You can't combine it with the /CAS , /PRI , or /SEC options.

/SourceDir

Applies to: Secondary

<!-- p.878 -->

Optional. This option verifies that the computer account of the secondary site can access
the folder that hosts the source files for Configuration Manager setup.

/SQL

Applies to: CAS, Primary

Required. Specify the fully qualified domain name (FQDN) of the SQL Server, for
example /SQL sql01.contoso.com

This option verifies that the specified server meets the requirements for SQL Server to
host the Configuration Manager site database.

/SQLPort

Applies to: Secondary

Optional. This option verifies that a firewall exception exists to allow communication for
the SQL Server service port. It also checks that the port isn't in use by another named
instance of SQL Server. The default port is 1433.

/SSBPort

Applies to: CAS, Primary, Secondary

Optional. This option verifies that a firewall exception exists to allow communication on
the SQL Server Service Broker (SSB) port. The default SSB port is 4022.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.879 -->

List of prerequisite checks for
Configuration Manager
Article • 03/28/2024

Applies to: Configuration Manager (current branch)

This article details the prerequisite checks that run when you install or update
Configuration Manager. For more information, see Prerequisite checker.

Errors

Active migration mappings on the target primary site
Applies to: Central administration site

There are no active migration mappings to primary sites.

Active replica MP
Applies to: Primary site

There's an active management point replica.

Administrative rights on expand primary site
Applies to: Central administration site

When you expand a primary site to a hierarchy, the user account that runs setup has
Administrator rights on the standalone primary site server.

Administrative rights on site system
Applies to: Central administration site, primary site, secondary site

The user account that runs Configuration Manager setup has Administrator rights on
the site server.

Administrator rights on central administration site
Applies to: Primary site

<!-- p.880 -->

The user account that runs Configuration Manager setup has Administrator rights on
the central administration site server.

Application catalog rules are unsupported
Applies to: Primary site

Starting in version 2107, this error happens if the site has either of the following site
system roles:

     Application catalog website point
     Application catalog web service point

Support for the application catalog was removed in version 1910. For more information,
see Remove the application catalog.

Asset Intelligence synchronization point on the expanded
primary site

  ） Important

  Starting in November 2021, this feature of Configuration Manager is deprecated.
  For more information, see Asset intelligence deprecation.

Applies to: Central administration site

When you expand a primary site to a hierarchy, the Asset Intelligence synchronization
point role isn't installed on the standalone primary site.

BITS enabled
Applies to: Management point

Background Intelligent Transfer Service (BITS) is installed on the management point. This
check can fail for one of the following reasons:

     BITS isn't installed

     The IIS 6.0 WMI compatibility component for IIS 7.0 isn't installed on the server or
     remote IIS host
