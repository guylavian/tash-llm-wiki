---
title: "Core infrastructure documentation — pages 801-840"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0801-0840
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0801-0840
family: sccm
documentKind: "doc"
abstract: "Plan a source hierarchy strategy in Configuration Manager Article • 10/04/2022 Applies to: Configuration Manager (current branch) Before you set up a migration job in your Configuration Manager environment, you must configure a source hierarchy and gather data from at least one"
---

# Core infrastructure documentation — pages 801-840

<!-- p.801 -->

Plan a source hierarchy strategy in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before you set up a migration job in your Configuration Manager environment, you
must configure a source hierarchy and gather data from at least one source site in that
hierarchy. Use the following sections to help you plan for configuring source hierarchies,
configuring source sites, and determining how Configuration Manager gathers
information from the source sites in the source hierarchy.

Source hierarchies
A source hierarchy is a Configuration Manager hierarchy that has data that you want to
migrate. When you set up migration and specify a source hierarchy, you specify the top-
level site of the source hierarchy. This site is also called a source site. Additional sites
that you can migrate data from in the source hierarchy are also called source sites.

      When you set up a migration job to migrate data from a Configuration Manager
      2007 source hierarchy, you configure it to migrate data from one or more specific
      source sites in the source hierarchy.

      When you set up a migration job to migrate data from a source hierarchy that runs
      System Center 2012 Configuration Manager or later, you only need to specify the
      top-level site.

You can set up only one source hierarchy at a time.

      If you set up a new source hierarchy, that hierarchy automatically becomes the
      current source hierarchy replacing the previous source hierarchy.

      When you set up a source hierarchy, you must specify the top-level site of the
      source hierarchy and specify credentials for Configuration Manager to use to
      connect to the SMS Provider and site database of that source site.

      Configuration Manager uses these credentials to run data gathering to retrieve
      information about the objects and distribution points from the source site.

      As part of the data gathering process, child sites in the source hierarchy are
      identified.

<!-- p.802 -->

     If the source hierarchy is a Configuration Manager 2007 hierarchy, you can set up
     those additional sites as source sites with separate credentials for each source site.

Although you can set up multiple source hierarchies in succession, migration is active for
only one source hierarchy at a time.

     If you set up an additional source hierarchy before you complete migration from
     the current source hierarchy, Configuration Manager cancels any active migration
     jobs and postpones any scheduled migration jobs for the current source hierarchy.

     The newly configured source hierarchy then becomes the current source hierarchy,
     and the original source hierarchy is now inactive.

     You can then set up connection credentials, additional source sites, and migration
     jobs for the new source hierarchy.

If you restore an inactive source hierarchy and have not previously used Cleanup
Migration Data, you can view the previously configured migration jobs for that source
hierarchy. However, before you can continue migration from that hierarchy, you must
reconfigure the credentials to connect to applicable source sites in the hierarchy, and
then reschedule any migration jobs that did not finish.

  Ｕ Caution

  If you migrate data from more than a single source hierarchy, each additional
  source hierarchy must contain a unique set of site codes.
  Source and destination hierarchies also requires different set of site codes.

For more about configuring a source hierarchy, see Configuring source hierarchies and
source sites for migration to Configuration Manager current branch

Source sites
Source sites are the sites in the source hierarchy that have the data that you want to
migrate. The top-level site of the source hierarchy is always the first source site. When
migration collects data from the first source site of a new source hierarchy, it discovers
information about additional sites in that hierarchy.

After data gathering completes for the initial source site, the actions you take next
depend on the product version of the source hierarchy.

Source sites that run Configuration Manager 2007 SP2

<!-- p.803 -->

After data is gathered from the initial source site of the Configuration Manager 2007
SP2 hierarchy, you do not have to set up additional source sites before you create
migration jobs. However, before you can migrate data from additional sites, you must
set up additional sites as source sites, and Configuration Manager must successfully
gather data from those sites.

To gather data from additional sites, you individually set up each site as a source site.
This requires you to specify the credentials for Configuration Manager to connect to the
SMS Provider and site database of each source site. After you set up the credentials for
a source site, the data gathering process for that site begins.

When you set up additional source sites in a Configuration Manager 2007 SP2 source
hierarchy, you must set up source sites from the top down, which means you set up the
bottom-tier sites last. You can configure source sites in a branch of the hierarchy at any
time, but you must set up a site as a source site before you set up any of its child sites
as source sites.

  ７ Note

  Only primary sites in a Configuration Manager 2007 SP2 hierarchy are supported
  for migration.

Source sites that run System Center 2012 Configuration
Manager or later
After data is gathered from the initial source site of the System Center 2012
Configuration Manager or later hierarchy, you do not have to set up additional source
sites in that source hierarchy. This is because unlike Configuration Manager 2007, these
versions of Configuration Manager use a shared database, and the shared database lets
you identify and then migrate all available objects from the initial source site.

When you set up the access accounts to gather data, you might need to grant the
Source Site SMS Provider Account access to multiple computers in the source
hierarchy. This might be needed when the source site supports multiple instances of the
SMS Provider, each on a different computer. When data gathering begins, the top-level
site of the destination hierarchy contacts the top-level site in the source hierarchy to
identify the locations of the SMS Provider for that site. Only the first instance of the SMS
provider is identified. If the data gathering process cannot access the SMS Provider at
the location it identifies, the process fails and does not try to connect to additional
computers that run an instance of SMS Provider for that site.

<!-- p.804 -->

Data gathering
Immediately after you specify a source hierarchy, set up credentials for each additional
source site in a source hierarchy, or share the distribution points for a source site,
Configuration Manager starts to gather data from the source site.

The data gathering process then repeats itself on a simple schedule to maintain
synchronization with any changes to data in the source site. By default, the process
repeats every four hours. You can change the schedule for this cycle by editing the
Properties of the source site. The initial data gathering process must review all objects
in the Configuration Manager database and can take a long time to finish. Subsequent
data gathering processes identify only changes to the data and require less time to
finish.

To gather data, the top-level site in the destination hierarchy connects to the SMS
Provider and the site database of the source site to retrieve a list of objects and
distribution points. These connections use the source site access accounts. For
information about required configurations for gathering data, see Prerequisites for
migration.

You can start and stop the data gathering process by using Gather Data Now and Stop
Gathering Data in the Configuration Manager console.

After you use Stop Gathering Data for a source site for any reason, you must
reconfigure credentials for the site before you can gather data from that site again. Until
you reconfigure the source site, Configuration Manager cannot identify new objects or
changes to previously migrated objects at that site.

  ７ Note

  Before you expand a standalone primary site into a hierarchy with a central
  administration site, you must stop all data gathering. You can reconfigure data
  gathering after the site expansion completes.

Gather Data Now
After the initial data gathering process runs for a site, this process repeats itself to
identify objects that have updated since the last data gathering cycle. You can also use
the Gather Data Now action in the Configuration Manager console to immediately start
the process and to reset the start time of the next cycle.

<!-- p.805 -->

After a data gathering process successfully finishes for a source site, you can share the
distribution points from the source site and configure migration jobs to migrate data
from the site. Data gathering is a repeating process for migration, and it continues until
you change the source hierarchy or use Stop Gathering Data to end the data gathering
process for that site.

Stop Gathering Data
You can use Stop Gathering Data to end the data gathering process for a source site
when you no longer want Configuration Manager to identify new or changed objects
from that site. This action also prevents Configuration Manager from offering clients in
the destination hierarchy any shared distribution points from the source as content
locations for the content that you have migrated.

To stop gathering data from each source site, you must run Stop Gathering Data on the
bottom-tier source sites, and then repeat the process at each parent site. The top-level
site of the source hierarchy must be the last site on which you stop gathering data. You
must stop data gathering at each child site before performing this action at a parent
site. Typically, you only stop gathering data when you are ready to complete the
migration process.

After you stop gathering data for a source site, information previously gathered about
objects and collections from that site remain available to use when you set up new
migration jobs. However, you do not see any new objects or collections, nor do you see
changes that were made to existing objects. If you reconfigure the source site and begin
gathering data again, you will see information and status about previously migrated
objects.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.806 -->

Plan a migration job strategy in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use migration jobs to configure the specific data that you want to migrate to your
Configuration Manager current branch environment. Migration jobs identify the objects
that you plan to migrate, and they run at the top-level site in your destination hierarchy.
You can set up one or more migration jobs per source site. This lets you migrate all
objects at one time or limited subsets of data with each job.

You can create migration jobs after Configuration Manager has successfully gathered
data from one or more sites from the source hierarchy. You can migrate data in any
sequence from the source sites that have gathered data. With a Configuration Manager
2007 source site, you can migrate data only from the site where an object was created.
With source sites that run System Center 2012 Configuration Manager or later, all data
that you can migrate is available at the top-level site of the source hierarchy.

Before you migrate clients between hierarchies, ensure that the objects that clients use
have migrated and that these objects are available in the destination hierarchy. For
example, when you migrate from a Configuration Manager 2007 SP2 source hierarchy,
you might have an advertisement for content that is deployed to a custom collection
that has a client. In this scenario, we recommend that you migrate the collection, the
advertisement, and the associated content before you migrate the client. This data
cannot be associated with the client in the destination hierarchy if the content,
collection, and advertisement are not migrated before the client migrates. If a client is
not associated with the data related to a previously run advertisement and content, the
client can be offered the content for installation in the destination hierarchy, which
might be unnecessary. When the client migrates after the data has migrated, the client is
associated with this content and advertisement, and unless the advertisement is
recurring, is not offered this content for the migrated advertisement again.

Some objects require more than the migration of data from the source hierarchy to the
destination hierarchy. For example, to successfully migrate software updates for your
clients to your destination hierarchy, you must deploy an active software update point,
configure the catalog of products, and synchronize the software update point with
Windows Server Update Services (WSUS) in the destination hierarchy.

Types of migration jobs

<!-- p.807 -->

Configuration Manager supports the following types of migration jobs. Each job type is
designed to help define the objects that you can include in that job.

Collection migration (only supported when migrating from Configuration Manager
2007 SP2): Migrate objects that are related to collections you select. By default,
collection migration includes all objects that are associated with members of the
collection. You can exclude specific object instances when you use a collection migration
job.

Object migration: Migrate individual objects that you select. You select only the specific
data that you want to migrate.

Previously migrated object migration: Migrate objects that you previously migrated
when they have updated in the source hierarchy after they were last migrated.

Objects that you can migrate
Not every object can migrate by a specific type of migration job. The following list
identifies the type of objects that you can migrate with each type of migration job.

  ７ Note

  Collection migration jobs are available only when you migrate objects from a
  Configuration Manager 2007 SP2 source hierarchy.

Job types you can use to migrate each object

       Advertisements (available to migrate from supported Configuration Manager 2007
       source sites)
         Collection migration

       Asset Intelligence catalog

         Object migration

         Previously migrated object migration

       Asset Intelligence hardware requirements

         Object migration

         Previously migrated object migration

       Asset Intelligence software list

<!-- p.808 -->

  Object migration

  Previously migrated object migration

Boundaries

  Object migration

  Previously migrated object migration

Configuration baselines

  Collection migration

  Object migration

  Previously migrated object migration

Configuration items

  Collection migration

  Object migration

  Previously migrated object migration

Maintenance windows
  Collection migration

Operating system deployment boot images

  Collection migration

  Object migration

  Previously migrated object migration

Operating system deployment driver packages

  Collection migration

  Object migration

  Previously migrated object migration

Operating system deployment drivers

  Collection migration

  Object migration

<!-- p.809 -->

  Previously migrated object migration

Operating system deployment images

  Collection migration

  Object migration

  Previously migrated object migration

Operating system deployment packages

  Collection migration

  Object migration

  Previously migrated object migration

Software distribution packages

  Collection migration

  Object migration

  Previously migrated object migration

Software metering rules

  Object migration

  Previously migrated object migration

Software update deployment packages

  Collection migration

  Object migration

  Previously migrated object migration

Software update deployment templates

  Collection migration

  Object migration

  Previously migrated object migration

Software update deployments
  Collection migration

<!-- p.810 -->

     Software update lists

        Object migration

        Previously migrated object migration

     Task sequences

        Collection migration

        Object migration

        Previously migrated object migration

     Virtual application packages

        Collection migration

        Object migration

        ） Important

        Although you can migrate a virtual application package by using object
        migration, the packages cannot be migrated by using the migration job type
        of Previously Migrated Object Migration. Instead, you must delete the
        migrated virtual application package from the destination site and then create
        a new migration job to migrate the virtual application.

General planning for all migration jobs
Use the Create Migration Job wizard to create a migration job to migrate objects to your
destination hierarchy. The type of the migration job that you create determines which
objects are available to migrate. You can create and use multiple migration jobs to
migrate data from the same source site or from multiple source sites. The use of one
type of migration job does not block the use of a different type of migration job.

After a migration job runs successfully, its status is listed as Completed and it cannot be
run again. However, you can create a new migration job to migrate any of the objects
that were migrated by the original job, and the new migration job can include additional
objects as well. When you create additional migration jobs, the objects that have been
previously migrated show the state of Migrated. You can select these objects to migrate
them again, but unless the object has been updated in the source hierarchy, migrating
these objects again is not necessary. If the object has been updated in the source

<!-- p.811 -->

hierarchy after it was originally migrated, you can identify that object when you use the
migration job type of Objects modified after migration.

You can delete a migration job before it runs. However, after a migration job finishes, it
remains visible in the Configuration Manager console and cannot be deleted. Each
migration job that has finished or has not yet run remains visible in the Configuration
Manager console until you finish the migration process and clean up migration data.

  ７ Note

  After you have finished migration by using the Clean Up Migration Data action,
  you can reconfigure the same hierarchy as the current source hierarchy to restore
  visibility to the objects you previously migrated.

You can view the objects contained in any migration job in the Configuration Manager
console by selecting the migration job and then choosing the Objects in Job tab.

Use the information in the following sections to help you plan for all migration jobs.

Data selection
When you create a collection migration job, you must select one or more collections.
After you select the collections, the Create Migration Job wizard shows the objects that
are associated with the collections. By default, all objects associated with the selected
collections are migrated, but you can uncheck the objects that you do not want to
migrate with that job. When you uncheck an object that has dependent objects, those
dependent objects are also unchecked. All unchecked objects are added to an exclusion
list. Objects on an exclusion list are removed from automatic selection for future
migration jobs. You must manually edit the exclusion list to remove objects that you
want to have automatically selected for migration in migration jobs you create in the
future.

Site ownership for migrated content
When you migrate content for deployments, you must assign the content object to a
site in the destination hierarchy. This site then becomes the owner for that content in
the destination hierarchy. Although the top-level site of your destination hierarchy is the
site that actually migrates the metadata for content, it is the assigned site that accesses
the original source files for the content across the network.

<!-- p.812 -->

To minimize the network bandwidth that is used during migration, consider transferring
ownership of content to the closest available site. Because information about the
content is shared globally in Configuration Manager, it will be available at every site.

Information about content is shared to all sites in the destination hierarchy by using
database replication. However, any content that you assign to a primary site and then
deploy to distribution points at other primary sites transfers by using file-based
replication. This transfer is routed through the central administration site and then to
each additional primary site. By centralizing packages that you plan to distribute to
multiple primary sites before or during migration when you assign a site as the content
owner, you can reduce data transfers across low-bandwidth networks.

Role-based administration security scopes for migrated
data
When you migrate data to a destination hierarchy, you must assign one or more role-
based administration security scopes to the objects whose data is migrated. This ensures
that only the appropriate administrative users have access to this data after it is
migrated. The security scopes that you specify are defined by the migration job and are
applied to each object that is migrated by that job. If you require different security
scopes to be applied to different sets of objects and you want to assign those scopes
during migration, you must migrate the different sets of objects by using different
migration jobs.

Before you set up a migration job, review how role-based administration works in
Configuration Manager. If necessary, set up one or more security scopes for the data
that you migrate to control who will have access to the migrated objects in the
destination hierarchy.

For more about security scopes and role-based administration, see Fundamentals of
role-based administration for Configuration Manager.

Review migration actions
When you set up a migration job, the Create Migration Job wizard shows a list of actions
that you must take to ensure a successful migration and a list of actions that
Configuration Manager takes during the migration of the selected data. Review this
information carefully to check the expected outcome.

Schedule migration jobs

<!-- p.813 -->

By default, a migration job runs immediately after it is created. However, you can specify
when the migration job runs when you create the job or by editing the properties of the
job. You can schedule the migration job to run as follows:

     Run the job now

     Run the job at a specific start time

     Not run the job

Specify conflict resolution for migrated data
By default, migration jobs do not overwrite data in the destination database unless you
configure the migration job to skip or overwrite data that has previously been migrated
to the destination database.

Plan for collection migration jobs
Collection migration jobs are available only when you migrate data from a source
hierarchy that runs a supported version of Configuration Manager 2007. You must
specify one or more collections to migrate when you migrate by collection. For each
collection that you specify, the migration job automatically selects all related objects for
migration. For example, if you select a specific collection of users, the collection
members are then identified, and you can migrate the deployments associated with that
collection. Optionally, you can select other deployment objects to migrate that are
associated with those members. All these selected items are added to the list of objects
that can be migrated.

When you migrate a collection, Configuration Manager also migrates collection settings,
including maintenance windows and collection variables, but it cannot migrate
collection settings for AMT client provisioning.

Use the information in the following sections to learn about additional configurations
that can apply to collection-based migration jobs.

Exclude objects from collection migration jobs
You can exclude specific objects from a collection migration job. When you exclude a
specific object from a collection migration job, that object is added to a global exclusion
list that has all the objects that you have excluded from migration jobs created for any
source site in the current source hierarchy. Objects on the exclusion list are still available

<!-- p.814 -->

for migration in future jobs but are not automatically included when you create a new
collection-based migration job.

You can edit the exclusion list to remove objects that you have previously excluded.
After you remove an object from the exclusion list, it is then automatically selected when
an associated collection is specified during the creation of a new migration job.

Unsupported collections
Configuration Manager can migrate any of the default user collections, device
collections, and most custom collections from a Configuration Manager 2007 source
hierarchy. However, Configuration Manager cannot migrate collections that contain
users and devices in the same collection.

The following collections cannot be migrated:

     A collection that has users and devices.

     A collection that has a reference to a collection of a different resource type. For
     example, a device-based collection that has either a subcollection or a link to a
     user-based collection. In this example, only the top-level collection migrates.

     A collection that has a rule to include unknown computers. The collection
     migrates, but the rule to include unknown computers does not migrate.

Empty collections
An empty collection is a collection that has no resources associated with it. When
Configuration Manager migrates an empty collection, it converts the collection to an
organizational folder that has no users or devices. This folder is created with the name
of the empty collection under the User Collections or Device Collections node in the
Assets and Compliance workspace in the Configuration Manager console.

Linked collections and subcollections
When you migrate collections that are linked to other collections or that have
subcollections, Configuration Manager creates a folder under the User Collections or
Device Collections node in addition to the linked collections and subcollections.

Collection dependencies and include objects

<!-- p.815 -->

When you specify a collection to migrate in the Create Migration Job wizard, any
dependent collections are automatically selected to be included with the job. This
behavior ensures that all necessary resources are available after migration.

For example: You select a collection for devices that run Windows 10 and is named
Win_10. This collection is limited to a collection that has all your client operating
systems and is named All_Clients. The collection All_Clients will be automatically
selected for migration.

Collection limiting
With Configuration Manager current branch, collections are global data and are
evaluated at each site in the hierarchy. Therefore, plan how to limit the scope of a
collection after it is migrated. During migration, you can identify a collection from the
destination hierarchy to use to limit the scope of the collection that you are migrating
so that the migrated collection does not include unanticipated members.

For example, in Configuration Manager 2007, collections are evaluated at the site that
creates them and at child sites. An advertisement might be deployed to only a child site,
and this would limit the scope for that advertisement to that child site. In comparison,
with Configuration Manager current branch, collections are evaluated at each site and
associated advertisements are then evaluated for each site. Collection limiting lets you
refine the collection members based on another collection to avoid the addition of
unexpected collection members.

Site code replacement
When you migrate a collection that has criteria that identifies a Configuration Manager
2007 site, you must specify a specific site in the destination hierarchy. This ensures that
the migrated collection remains functional in your destination hierarchy and does not
increase in scope.

Specify behavior for migrated advertisements
By default, collection-based migration jobs disable advertisements that migrate to the
destination hierarchy. This includes any programs that are associated with the
advertisement. When you create a collection-based migration job that has
advertisements, you see the Enable programs for deployment in Configuration
Manager after an advertisement is migrated option on the Settings page of the Create
Migration Job wizard. If you select this option, programs that are associated with the
advertisements are enabled after they have migrated. As a best practice, do not select

<!-- p.816 -->

this option. Instead, enable the programs after they have migrated when you can verify
the clients that will receive them.

  ７ Note

  You see the Enable programs for deployment in Configuration Manager after an
  advertisement is migrated option only when you are creating a collection-based
  migration job and the migration job contains advertisements.

To enable a program after migration, clear Disable this program on computers where it
is advertised on the Advanced tab of the program properties.

Plan for object migration jobs
Unlike collection migration, you must select each object and object instance that you
want to migrate. You can select the individual objects (like advertisements from a
Configuration Manager 2007 hierarchy or a publication from a System Center 2012
Configuration Manager or Configuration Manager current branch hierarchy) to add to
the list of objects to migrate for a specific migration job. Any objects that you do not
add to the migration list are not migrated to the destination site by the object migration
job.

Object-based migration jobs do not have any additional configurations to plan for
beyond those applicable to all migration jobs.

Plan for previously migrated object migration
jobs
When an object that you have already migrated to the destination hierarchy is updated
in the source hierarchy, you can migrate that object again by using the Objects
modified after migration job type. For example, when you rename or update the source
files for a package in the source hierarchy, the package version increments in the source
hierarchy. After the package version increments, the package can be identified for
migration by this job type.

This job type is similar to the object migration type except that when you select objects
to migrate, you can only select from objects that have been updated after they were
migrated by a previous migration job.

<!-- p.817 -->

When you select this job type, the conflict resolution behavior on the Settings page of
the Create Migration Job wizard is configured to overwrite previously migrated objects.
This setting cannot be changed.

  ７ Note

  This migration job can identify objects that are automatically updated by the source
  hierarchy and objects that an administrative user updates.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.818 -->

Plan a client migration strategy in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To migrate clients from the source hierarchy to a Configuration Manager current branch
destination hierarchy, you must do two tasks. You must migrate the objects that are
associated with the client and you must then reinstall or reassign the clients from the
source hierarchy to the destination hierarchy. You migrate the objects first so that they
are available when the clients are migrated. The objects associated with the client are
migrated by using migration jobs. For information about how to migrate the objects
that are associated with the client, see Planning a migration job strategy.

Use the following sections to help you plan to migrate clients to the destination
hierarchy.

      Plan to migrate clients to the destination hierarchy

      Plan to handle data maintained on clients during migration

      Plan for inventory and compliance data during migration

Plan to migrate clients to the destination
hierarchy
When you migrate clients from a source hierarchy, the client software on the client
computer upgrades to match the product version of the destination hierarchy.

      A Configuration Manager 2007 source hierarchy: When you migrate clients from
      a source hierarchy that runs a supported version of Configuration Manager, the
      client software upgrades to the client version for the destination hierarchy.

      A System Center 2012 Configuration Manager or later source hierarchy: When
      you migrate clients between hierarchies that are of the same product version, the
      client software does not change or upgrade. Instead, the client reassigns from the
      source hierarchy to a site in the destination hierarchy.

        ７ Note

<!-- p.819 -->

       When the product version of a hierarchy is not supported for migration to
       your destination hierarchy, upgrade all sites and clients in the source hierarchy
       to a compatible product version. After the source hierarchy upgrades to a
       supported product version, you can migrate between the hierarchies. For
       more information, see Versions of Configuration Manager that are
       supported for migration in Prerequisites for migration.

Use the following information to help you plan the client migration:

     To upgrade or reassign clients from a source site to a destination site, you can use
     any client deployment method that is supported for deploying clients in the
     destination hierarchy. Typical client deployment methods include client push
     installation, software distribution, Group Policy, and software update-based client
     installation. For more information, see Client installation methods.

     Ensure that the device that runs the client software in the source hierarchy meets
     the minimum hardware requirements and runs an operating system that is
     supported by the version of Configuration Manager in the destination hierarchy.

     Before you migrate a client, run a migration job to migrate the information that
     the client will use in the destination hierarchy.

     Clients that upgrade retain their run history for deployments. This prevents
     deployments from rerunning unnecessarily in the destination hierarchy.

        For Configuration Manager 2007 clients, advertisement run history is retained.

        For clients from System Center 2012 Configuration Manager or Configuration
        Manager current branch, deployment run history is retained.

     You can migrate clients from sites in the source hierarchy in any order that you
     choose. However, consider migrating limited numbers of clients in phases rather
     than migrating large numbers of clients at a single time. A phased migration
     reduces the network bandwidth requirements and server processing when each
     newly upgraded client submits its initial full inventory and compliance data to its
     assigned site.

     When you migrate Configuration Manager 2007 clients, the existing client software
     is uninstalled from the client computer and the new client software is installed.

     Configuration Manager cannot migrate a Configuration Manager 2007 client that
     has the App-V client installed unless the App-V client version is 4.6 SP1 or later.

<!-- p.820 -->

You can monitor the client migration process in the Migration node of the
Administration workspace in the Configuration Manager console.

After you migrate the client to the destination hierarchy, you can no longer manage that
device by using your source hierarchy, and you should consider removing the client
from the source hierarchy. Although this is not a requirement when you migrate
hierarchies, it can help prevent identification of a migrated client in a source hierarchy
report, or an incorrect count of resources between the two hierarchies during the
migration. For example, when a migrated client remains in the source site database, you
might run a software updates report that incorrectly identifies the computer as an
unmanaged resource when it is now managed by the destination hierarchy.

Plan to handle data maintained on clients
during migration
When you migrate a client from its source hierarchy to the destination hierarchy, some
information is retained on the device, while other information is not available on the
device after migration.

The following information is retained on the client device:

     The unique identifier (GUID), which associates a client with its information in the
     Configuration Manager database.

     The advertisement or deployment history, which prevents clients from
     unnecessarily rerunning advertisements or deployments in the destination
     hierarchy.

The following information is not retained on the client device:

     The files in the client cache. If the client requires these files to install software, the
     client downloads them again from the destination hierarchy.

     Information from the source hierarchy about any advertisements or deployments
     that have not yet run. If you want the client to run the advertisements or
     deployments after it migrates, you must redeploy them to the client in the
     destination hierarchy.

     Information about inventory. The client resends this information to its assigned site
     in the destination hierarchy after the client migrates and the new client data has
     been generated.

<!-- p.821 -->

        Compliance data. The client resends this information to its assigned site in the
        destination hierarchy after the client migrates and the new client data has been
        generated.

When a client migrates, information that is stored in the Configuration Manager client
registry and file path is not retained. After migration, reapply these settings. Typical
settings include the following:

        Power schemes

        Logging settings

        Local policy settings

Additionally, you might have to reinstall some applications.

Plan for inventory and compliance data during
migration
Client inventory and compliance data is not saved when you migrate a client to the
destination hierarchy. Instead, this information is recreated in the destination hierarchy
when a client first sends its information to its assigned site. To help reduce the resulting
network bandwidth requirements and server processing, consider migrating a small
number of clients in phases rather than migrating a large number of clients at a single
time.

Additionally, you cannot migrate customizations for hardware inventory from a source
hierarchy. You must introduce these to the destination hierarchy independently from
migration. For information about how to extend hardware inventory, see How to
configure hardware inventory.

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.822 -->

Plan a content deployment migration
strategy in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

While you actively migrate data to a Configuration Manager current branch destination
hierarchy, Configuration Manager clients in both the source and destination hierarchies
can maintain access to content that you deployed in the source hierarchy. You can also
use migration to upgrade or reassign distribution points from the source hierarchy to
become distribution points in the destination hierarchy. When you share and upgrade or
reassign distribution points, this strategy can help you avoid having to redeploy content
to new servers in the destination hierarchy for the clients that you migrate.

Although you can recreate and distribute content in the destination hierarchy, you can
also use the following options to manage this content:

      Share distribution points in the source hierarchy with clients in the destination
      hierarchy.

      Upgrade standalone Configuration Manager 2007 distribution points or
      Configuration Manager 2007 secondary sites in the source hierarchy to become
      distribution points in the destination hierarchy.

      Reassign distribution points from a Configuration Manager source hierarchy to a
      site in the destination hierarchy.

Share distribution points between source and
destination hierarchies
During migration, you can share distribution points from a source hierarchy with the
destination hierarchy. You can use shared distribution points to make content that you
have migrated from a source hierarchy immediately available to clients in the
destination hierarchy without having to recreate that content, and then distribute it to
new distribution points in the destination hierarchy. When clients in the destination
hierarchy request content that is deployed to distribution points that you have shared,
the shared distribution points can be offered to the clients as valid content locations.

In addition to being a valid content location for clients in the destination hierarchy while
migration from the source hierarchy remains active, it is possible to upgrade or reassign

<!-- p.823 -->

a distribution point to the destination hierarchy. You can upgrade Configuration
Manager 2007 shared distribution points and reassign System Center 2012
Configuration Manager shared distribution points. When you upgrade or reassign a
shared distribution point, the distribution point is removed from the source hierarchy
and becomes a distribution point in the destination hierarchy. After you upgrade or
reassign a shared distribution point, you can continue to use the distribution point in
the destination hierarchy after migration from the source hierarchy is finished. For more
about how to upgrade a shared distribution point, see Plan to upgrade Configuration
Manager 2007 shared distribution points. For more about how to reassign a shared
distribution point, see Plan to reassign Configuration Manager distribution points.

You can choose to share distribution points from any source site in your source
hierarchy. When you share distribution points for a source site, child secondary sites are
shared at each qualifying distribution point at that primary site and at each of the
primary sites. To qualify to be a shared distribution point, the site system server that
hosts the distribution point must be set up with a fully qualified domain name (FQDN).
Any distribution points that are set up with a NetBIOS name are disregarded.

   Tip

  Configuration Manager 2007 does not require you to set up an FQDN for site
  system servers.

Use the following information to help you plan for shared distribution points:

     Distribution points that you share must meet the prerequisites for shared
     distribution points. For more about these prerequisites, see Required
     configurations for migration in Prerequisites for migration.

     The share distribution point action is a site-wide setting that shares all qualifying
     distribution points at a source site and at any direct child secondary sites. You
     cannot select individual distribution points to share when you enable distribution
     point sharing.

     Clients in the destination hierarchy can receive content location information for
     packages that are distributed to distribution points that are shared from the source
     hierarchy. For distribution points from a Configuration Manager 2007 source
     hierarchy, this includes branch distribution points, distribution points on server
     shares, and standard distribution points.

        ２ Warning

<!-- p.824 -->

  If you change the source hierarchy, shared distribution points from the
  original source hierarchy are no longer available and cannot be offered as
  content locations to clients in the destination hierarchy. If you reconfigure
  migration to use the original source hierarchy, the previously shared
  distribution points are restored as valid content location servers.

When you migrate a package that is hosted on a shared distribution point, the
package version must remain the same in the source and destination hierarchies.
When a package version is not the same in the source and destination hierarchy,
clients in the destination hierarchy cannot retrieve that content from the shared
distribution point. Therefore, if you update a package in the source hierarchy, you
must re-migrate the package data before clients in the destination hierarchy can
retrieve that content from a shared distribution point.

  ７ Note

  When you view details for a package that is hosted on a shared distribution
  point, the number of packages that display as Hosted Migrated Packages on
  the source site's Shared Distribution Points tab is not updated until the next
  data gathering cycle is finished.

You can view shared distribution points and their properties in the Source
Hierarchy node of the Administration workspace in the Configuration Manager
console that connects to the destination hierarchy.

You cannot use a shared distribution point from a Configuration Manager 2007
source hierarchy to host packages for Microsoft Application Virtualization (App-V).
App-V packages must migrate and be converted for use by clients in the
destination hierarchy. However, you can use a shared distribution point from a
System Center 2012 Configuration Manager or Configuration Manager current
branch source hierarchy to host App-V packages for clients in a destination
hierarchy.

When you share a protected distribution point from a Configuration Manager 2007
source hierarchy, the destination hierarchy creates a boundary group that includes
the protected network locations of that distribution point. You cannot change this
boundary group in the destination hierarchy. However, if you change the protected
boundary information for the distribution point in the Configuration Manager 2007
source hierarchy, that change is reflected in the destination hierarchy after the next
data gathering cycle finishes.

<!-- p.825 -->

        ７ Note

        System Center 2012 Configuration Manager and Configuration Manager
        current branch sites use the concept of preferred distribution points instead
        of protected distribution points. This condition only applies to distribution
        points that are shared from Configuration Manager 2007 source sites.

The eligible distribution points are not visible in the Configuration Manager console
before you share distribution points from a source site. After you share distribution
points, only the distribution points that are successfully shared are listed.

After you have shared distribution points, you can change the configuration of any
shared distribution point in the source hierarchy. Changes that you make to the
configuration of a distribution point are reflected in the destination hierarchy after the
next data gathering cycle. Distribution points that you updated to qualify for sharing are
shared automatically, while those that no longer qualify stop sharing distribution points.
For example, you might have a distribution point that is not set up with an intranet
FQDN and was not initially shared with the destination hierarchy. After you set up the
FQDN for that distribution point, the next data gathering cycle identifies this
configuration, and the distribution point is then shared with the destination hierarchy.

Plan to upgrade Configuration Manager 2007
shared distribution points
When you migrate from a Configuration Manager 2007 source hierarchy, you can
upgrade a shared distribution point to make it a Configuration Manager current branch
distribution point. You can upgrade distribution points at primary sites and secondary
sites. The upgrade process removes the distribution point from the Configuration
Manager 2007 hierarchy and makes it a site system server in the destination hierarchy.
This process also copies the existing content that is on the distribution point to a new
location on the distribution point computer. The upgrade process then modifies the
copy of the content to create the single instance store for use with content deployment
in the destination hierarchy. Therefore, when you upgrade a distribution point, you do
not have to redistribute migrated content that was hosted on the Configuration
Manager 2007 distribution point.

After Configuration Manager converts the content to the single instance store,
Configuration Manager deletes the original source content on the distribution point
computer to free up disk space. Configuration Manager does not use the original source
content location.

<!-- p.826 -->

Not all Configuration Manager 2007 distribution points that you can share are eligible
for upgrade to Configuration Manager current branch. To be eligible for upgrade, a
Configuration Manager 2007 distribution point must meet the conditions for upgrade.
These conditions include the site system server on which the distribution point is
installed and the type of Configuration Manager 2007 distribution point that is installed.
For example, you cannot upgrade any type of distribution point that is installed on the
site server computer at a primary site, but you can upgrade a standard distribution point
that is installed on the site server computer at a secondary site.

     ７ Note

     You can upgrade only those Configuration Manager 2007 shared distribution points
     that are on a computer that runs an operating system version that is supported for
     distribution points in the destination hierarchy. For example, although you can
     share a Configuration Manager 2007 distribution point that is on a computer that
     runs Windows Vista, you cannot upgrade this shared distribution point because the
     operating system is not supported by Configuration Manager current branch for
     use as a distribution point.

The following table lists the supported locations for each type of Configuration Manager
2007 distribution point that you can upgrade.

                                                                              ﾉ    Expand table

    Type of           Distribution point on   Distribution point on a site   Distribution
    distribution      a site system           system computer other than     point on a
    point             computer other than     the site server and hosting    secondary site
                      the site server         other site system roles        server

    Standard          Yes                     No                             Yes
    distribution
    point

    Distribution      Yes                     No                             No
    point on server
    shares1

    Branch            Yes                     No                             No
    distribution
    point

1
    Configuration Manager current branch does not support server shares for site systems,
but it does support the upgrade of a Configuration Manager 2007 distribution point
that is on a server share. When you upgrade a Configuration Manager 2007 distribution

<!-- p.827 -->

point that is on a server share, the distribution point type is automatically converted to a
server, and you must select the drive on the distribution point computer that will store
the single instance content store.

  ２ Warning

  Before you upgrade a branch distribution point, uninstall the Configuration
  Manager 2007 client software. When you upgrade a branch distribution point that
  has the Configuration Manager 2007 client software installed, the content that was
  previously deployed to the computer is removed from the computer, and the
  upgrade of the distribution point fails.

To identify distribution points that are eligible for upgrade in the Configuration Manager
console in the Source Hierarchy node, select a source site, and then select the Shared
Distribution Points tab. Eligible distribution points display Yes in the Eligible for
Upgrade column.

When you upgrade a distribution point that is installed on a Configuration Manager
2007 secondary site server, the secondary site is uninstalled from the source hierarchy.
Although this scenario is called a secondary site upgrade, this applies only to the
distribution point site system role. The result is that the secondary site is not upgraded
and instead is uninstalled. This leaves a distribution point from the destination hierarchy
on the computer that was the secondary site server. If you plan to upgrade the
distribution point on a secondary site, see Plan to upgrade Configuration Manager 2007
secondary sites in this topic.

Distribution point upgrade process
You can use the Configuration Manager console to upgrade Configuration Manager
2007 distribution points that you have shared with the destination hierarchy. When you
upgrade a shared distribution point, the distribution point is uninstalled from the
Configuration Manager 2007 site. It is then installed as a distribution point that is
attached to a primary or secondary site that you specify in the destination hierarchy. The
upgrade process creates a copy of the migrated content that is stored on the
distribution point, and then converts this copy to the single instance content store.
When Configuration Manager converts a package to the single instance content store, it
deletes that package from the SMSPKG share on the distribution point computer unless
the package has one or more advertisements that are set to Run program from
distribution point.

<!-- p.828 -->

To upgrade the distribution point, Configuration Manager uses the Source Site Access
Account that is set up to gather data from the SMS Provider of the source site. Although
this account requires only Read permission for site objects to gather data from the
source site, it must also have Delete and Modify permission to the Site class to
successfully remove the distribution point from the Configuration Manager 2007 site
during the upgrade.

  ７ Note

  Configuration Manager can convert content to the single instance store on only
  one distribution point at a time. When you set up multiple distribution point
  upgrades, the distribution points are queued for upgrade and processed one at a
  time.

Before you upgrade a shared distribution point, ensure that all content that is deployed
to the distribution point is migrated. Content that you do not migrate before you
upgrade the distribution point is not available in the destination hierarchy after the
upgrade. When you upgrade a distribution point, the content in the migrated packages
is converted into a format that is compatible with the single instance store of the
destination hierarchy.

To upgrade a distribution point from within the Configuration Manager console, the
Configuration Manager 2007 site system server must meet the following conditions:

     The distribution point configuration and location must be eligible for upgrade.

     The distribution point computer must have sufficient disk space for the content to
     be converted from the Configuration Manager 2007 content storage format to the
     single instance store format. This conversion requires available free disk space
     equal to the size of the largest package that is stored on the distribution point.

     The distribution point computer must run an operating system version that is
     supported as a distribution point in the destination hierarchy.

          ７ Note

          When Configuration Manager checks for the eligibility of a distribution point
          for upgrade, it does not validate the operating system version of the
          distribution point computer.

To upgrade a distribution point, in the Administration workspace, expand Migration,
expand the Source Hierarchy node, and then select the site that has the distribution

<!-- p.829 -->

point that you want to upgrade. Next, in the details pane, on the Shared Distribution
Points tab, select the distribution point that you want to upgrade.

You can confirm that the distribution point is ready for upgrade by viewing the status in
the Eligible for Reassignment column. Next, on the Configuration Manager console
ribbon, on the Distribution Points tab, in the Distribution Point group, select Reassign.
This opens a wizard that you use to finish the upgrade of the distribution point.

When you upgrade a shared distribution point, you must assign the distribution point to
a primary or secondary site of your choice in the destination hierarchy. After the
distribution point is upgraded, manage the distribution point as a distribution point in
the destination hierarchy like any other distribution point.

You can monitor the progress of a distribution point upgrade in the Configuration
Manager console by selecting the Distribution Point Migration node under the
Migration node of the Administration workspace. You can also view information in the
Migmctrl.log on the central administration site server of the destination hierarchy, or in
the distmgr.log on the site server in the destination hierarchy that manages the
upgraded distribution point.

  ７ Note

  When you upgrade a distribution point to the destination hierarchy, the
  distribution point site system role is removed from the Configuration Manager
  2007 source site. However, packages that were sent to the distribution point are
  not updated in the Configuration Manager 2007 hierarchy. In the Configuration
  Manager 2007 console, packages that had been sent to the distribution point
  continue to list the site system computer as a distribution point with a Type of
  Unknown. Subsequent updates to the package in Configuration Manager 2007
  result in Distribution Manager reporting errors in the distmgr.log for that site when
  the site attempts to update the package on the unknown site system.

If you decide not to upgrade a shared distribution point, you can still install a
distribution point from the destination hierarchy on a former Configuration Manager
2007 distribution point. Before you can install the new distribution point, you must first
uninstall all Configuration Manager 2007 site system roles from the distribution point
computer. This includes the Configuration Manager 2007 site if it is the site server
computer. When you uninstall a Configuration Manager 2007 distribution point, content
that was deployed to the distribution point is not deleted from the computer.

<!-- p.830 -->

Plan to upgrade Configuration Manager 2007 secondary
sites
When you use migration to upgrade a shared distribution point that is hosted on a
Configuration Manager 2007 secondary site server, Configuration Manager upgrades
the distribution point site system role to be a distribution point in the destination
hierarchy. It also uninstalls the secondary site from the source hierarchy. The result is a
Configuration Manager current branch distribution point, but no secondary site.

For a distribution point on the site server computer to be eligible for upgrade,
Configuration Manager must be able to uninstall the secondary site and each of the site
system roles on that computer. Typically, a shared distribution point on a Configuration
Manager 2007 server share is eligible for upgrade. However, when a server share exists
on the secondary site server, the secondary site and any shared distribution points on
that computer are not eligible for upgrade. This is because the server share is treated as
an additional site system object when the process attempts to uninstall the secondary
site, and this process cannot uninstall this object. In this scenario, you can enable a
standard distribution point on the secondary site server and then redistribute the
content to that standard distribution point. This process does not use network
bandwidth, and when finished, you can uninstall the distribution point on the server
share, remove the server share, and then upgrade the distribution point and secondary
site.

Before you upgrade a shared distribution point, review the distribution point
configuration in Configuration Manager 2007 to avoid upgrading a distribution point on
a secondary site that you still want to use with Configuration Manager 2007. This is a
good practice, because after you upgrade a shared distribution point that is on a
secondary site server, the site system server is removed from the Configuration Manager
2007 hierarchy and is no longer available for use with that hierarchy. When the
secondary site is removed, any remaining distribution points at that secondary site are
orphaned. This means they become unmanaged from Configuration Manager 2007 and
are no longer shared or eligible for upgrade.

   ２ Warning

   When you view shared distribution points in the Configuration Manager console,
   there is no visible indication that a shared distribution point is on a remote site
   system server or on the secondary site server.

When you have a secondary site in a remote network location that is used primarily to
control the deployment of content to that remote location, consider upgrading

<!-- p.831 -->

secondary sites that have a shared distribution point. Because you can set up bandwidth
control for when you distribute content to a Configuration Manager current branch
distribution point, you can often upgrade a secondary site to a distribution point, set up
the distribution point for bandwidth controls, and avoid installing a secondary site in
that network location in the destination hierarchy.

The process to upgrade a shared distribution point on a secondary site server is the
same as any other shared distribution point upgrade. Content is copied and converted
to the single instance store in use by the destination hierarchy. However, when you
upgrade a shared distribution point that is on a secondary site server, the upgrade
process also uninstalls the management point (if present) and then uninstalls the
secondary site from the server. The result is that the secondary site is removed from the
Configuration Manager 2007 hierarchy. To uninstall the secondary site, Configuration
Manager uses the account that is set up to gather data from the source site.

During the upgrade, there is a delay between when the Configuration Manager 2007
secondary site is uninstalled and the when the installation of the distribution point in the
destination hierarchy begins. The data-gathering cycle determines this delay of up to
four hours. The delay is intended to provide time for the secondary site to uninstall
before the new distribution point installation begins.

For more about how to upgrade a shared distribution point, see Plan to upgrade
Configuration Manager 2007 shared distribution points.

Plan to reassign Configuration Manager
distribution points
When you migrate from a supported version of System Center 2012 Configuration
Manager to a hierarchy of the same version, you can reassign a shared distribution point
from the source hierarchy to a site in the destination hierarchy. This is like the concept
of upgrading a Configuration Manager 2007 distribution point to become a distribution
point in the destination hierarchy. You can reassign distribution points from primary
sites and secondary sites. The action to reassign a distribution point removes the
distribution point from the source hierarchy and makes the computer and its
distribution point a site system server of the site that you select in the destination
hierarchy.

When you reassign a distribution point, you do not have to redistribute migrated
content that was hosted on the source site distribution point. Additionally, unlike the
upgrade of a Configuration Manager 2007 distribution point, reassignment of a
distribution point does not require additional disk space on the distribution point

<!-- p.832 -->

computer. This is because beginning with System Center 2012 Configuration Manager,
distribution points use the single instance store format for content. The content on the
distribution point computer does not need to be converted when the distribution point
is reassigned between hierarchies.

For a System Center 2012 Configuration Manager distribution point to be eligible for
reassignment, it must meet the following criteria:

     A shared distribution point must be installed on a computer other than the site
     server.

     A shared distribution point cannot be co-located with any additional site system
     roles.

To identify distribution points that are eligible for reassignment in the Configuration
Manager console in the Source Hierarchy node, select a source site, and then select the
Shared Distribution Points tab. Eligible distribution points display Yes in the Eligible for
Reassignment column (this column is named Eligible for Upgrade prior to System
Center 2012 R2 Configuration Manager).

Distribution point reassignment process
You can use the Configuration Manager console to reassign distribution points that you
have shared from an active source hierarchy. When you reassign a shared distribution
point, the distribution point is uninstalled from its source site and then installed as a
distribution point that is attached to a primary or secondary site that you specify in the
destination hierarchy.

To reassign the distribution point, the destination hierarchy uses the Source Site Access
Account that is set up to gather data from the SMS Provider of the source site. For
information about required permissions and additional prerequisites, see Prerequisites
for migration.

Migrate multiple shared distribution points at
the same time
Beginning with version 1610, you can use Reassign Distribution point to have
Configuration Manager process in parallel the reassignment of up to 50 shared
distribution points at the same time. This includes shared distribution points from
supported source sites that run:

     Configuration Manager 2007

<!-- p.833 -->

        System Center 2012 Configuration Manager
        System Center 2012 R2 Configuration Manager
        Configuration Manager (current branch)

When you reassign distribution points, each distribution point must qualify to be either
upgraded or reassigned. The name of the action and process involved (upgrade or
reassign) depends on which version of Configuration Manager the source site runs. The
end results for both actions are the same: the distribution point is assigned to one of
your Current Branch sites with its content in place.

Prior to version 1610, Configuration Manager could process only one distribution point
at a time. Now you can reassign as many distribution points as you want with the
following caveats:

        Although you cannot multiselect distribution points to be reassigned, when you
        have queued up more than one, Configuration Manager will process them in
        parallel instead of waiting to finish one before starting the next.
        By default, up to 50 distribution points are processed in parallel at a time. After the
        reassignment of the first distribution point is finished, Configuration Manager will
        begin to process the 51st, and so on.
        When you use the Configuration Manager SDK, you can change
        SharedDPImportThreadLimit to adjust the number of reassigned distribution
        points that Configuration Manager can process in parallel.

Assign content ownership when migrating
content
When you migrate content for deployments, you must assign the content object to a
site in the destination hierarchy. This site then becomes the owner for that content in
the destination hierarchy. Although the top-level site of your destination hierarchy is the
site that migrates the metadata for content, it is the assigned site that uses the original
source files for the content across the network.

To minimize the network bandwidth that is used when you migrate content, consider
transferring ownership of content to a site in the destination hierarchy that is close on
the network to the content location in the source hierarchy. Because information about
the content in the destination hierarchy is shared globally, it will be available at every
site.

Although information about content is shared to all sites by using database replication,
any content that you assign to a primary site and then deploy to distribution points at
other primary sites transfers by file-based replication. This transfer is routed through the

<!-- p.834 -->

central administration site and then to the additional primary site. You can reduce data
transfers across low-bandwidth networks by centralizing packages that you plan to
distribute to multiple primary sites before or during migration when you assign a site as
the content owner.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.835 -->

Plan for the migration of Configuration
Manager objects to Configuration
Manager current branch
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

With Configuration Manager current branch, you can migrate many of the different
objects that are associated with different features found at a source site.

Plan to migrate software updates
You can migrate software update objects, like software update packages and software
update deployments.

To successfully migrate software update objects, you must first set up your destination
hierarchy with configurations that match your source hierarchy environment. This
requires the following actions:

      Deploy an active software update point in the destination hierarchy

      Set up the catalog of products and languages to match the configuration of your
      source hierarchy

      Sync the software update point in the destination hierarchy with Windows Server
      Update Services (WSUS)

When you migrate software updates, consider the following:

      Migration of software update objects can fail when you have not synced
      information in your destination hierarchy to match the configuration of your
      source hierarchy.

        ２ Warning

        Configuration Manager does not support use of the WSUSutil tool to sync
        data between a source and destination hierarchy.

      You cannot migrate custom updates that are published by using System Center
      Updates Publisher. Instead, custom updates must be republished to the

<!-- p.836 -->

     destination hierarchy.

When you migrate from a Configuration Manager 2007 source hierarchy, the migration
process modifies some software update objects to the format in use by the destination
hierarchy. Use the following table to help you plan the migration of software update
objects from Configuration Manager 2007.

                                                                             ﾉ   Expand table

 Configuration           Object name after migration
 Manager 2007 object

 Software update lists   Software update lists are converted to software update groups.

 Software update         Software update deployments are converted to deployments and
 deployments             update groups.

                         After you migrate a software update deployment from Configuration
                         Manager 2007, you must enable it in the destination hierarchy before
                         you can deploy it.

 Software update         Software update packages remain software update packages.
 packages

 Software update         Software update templates remain software update templates.
 templates
                         The Duration value in Configuration Manager 2007 deployment
                         templates does not migrate.

When you migrate objects from a System Center 2012 Configuration Manager or
Configuration Manager current branch source hierarchy, the software updates objects
are not modified.

Plan to migrate content
You can migrate content from a supported source hierarchy to your destination
hierarchy. For a Configuration Manager 2007 source hierarchy, this content includes
software distribution packages and programs and virtual applications, like Microsoft
Application Virtualization (App-V). For System Center 2012 Configuration Manager and
Configuration Manager current branch source hierarchies, this content includes
applications and App-V virtual applications. When you migrate content between
hierarchies, the compressed source files migrate to the destination hierarchy.

Packages and programs

<!-- p.837 -->

When you migrate packages and programs, they are not modified by migration.
However, before you migrate them, you must set up each package to use a Universal
Naming Convention (UNC) path for its source file location. As part of the configuration
to migrate packages and programs, you must assign a site in the destination hierarchy
to manage this content. The content is not migrated from the assigned site, but after
migration, the assigned site accesses the original source file location by using the UNC
mapping.

After you migrate a package and program to the destination hierarchy, and while
migration from the source hierarchy remains active, you can make the content available
to clients in that hierarchy by using a shared distribution point. To use a shared
distribution point, the content must remain accessible on the distribution point at the
source site. For more about shared distribution points, see Share distribution points
between source and destination hierarchies in Plan a content deployment migration
strategy.

For content that has migrated, if the content version changes in the source hierarchy or
the destination hierarchy, clients can no longer access the content from the shared
distribution point in the destination hierarchy. In this scenario, you must re-migrate the
content to restore a consistent version of the package between the source hierarchy and
the destination hierarchy. This information syncs during the data gathering cycle.

   Tip

  For each package that you migrate, update the package in the destination
  hierarchy. This action can prevent issues with deploying the package to distribution
  points in the destination hierarchy. However, when you update a package on the
  distribution point in the destination hierarchy, clients in that hierarchy will no
  longer be able to get that package from a shared distribution point. To update a
  package in the destination hierarchy, in the Configuration Manager console, go to
  the Software Library, right-click on the package, and then select Update
  Distribution Points. Do this action for each package that you migrate.

   Tip

  Use Package Conversion Manager to convert packages and programs into
  Configuration Manager applications. For more information, see Package
  Conversion Manager.

Virtual applications

<!-- p.838 -->

When you migrate App-V packages from a supported Configuration Manager 2007 site,
the migration process converts them to applications in the destination hierarchy.
Additionally, based on existing advertisements for the App-V package, the following
deployment types are created in the destination hierarchy:

     If there are no advertisements, one deployment type is created that uses the
     default deployment type settings.

     If one advertisement exists, one deployment type is created that uses the same
     settings as the Configuration Manager 2007 advertisement.

     If multiple advertisements exist, a deployment type is created for each
     Configuration Manager 2007 advertisement by using the settings for that
     advertisement.

  ） Important

  If you migrate a previously migrated Configuration Manager 2007 App-V package,
  the migration fails because virtual application packages do not support the
  overwrite migration behavior. In this scenario, you must delete the migrated virtual
  application package from the destination hierarchy, and then create a new
  migration job to migrate the virtual application.

  ７ Note

  After you migrate an App-V package, you can use the Update Content wizard to
  change the source path for App-V deployment types. For more about how to
  update content for a deployment type, see How to manage deployment types in
  Management tasks for Configuration Manager applications.

When you migrate from a System Center 2012 Configuration Manager or Configuration
Manager current branch source hierarchy, you can migrate objects for the App-V virtual
environment in addition to App-V deployment types and applications. For more about
App-V environments, see Deploying App-V virtual applications.

Advertisements
You can migrate advertisements from a supported Configuration Manager 2007 source
site to the destination hierarchy by using collection-based migration. If you upgrade a
client, it retains the history of previously run advertisements to prevent the client from
rerunning migrated advertisements.

<!-- p.839 -->

  ７ Note

  You cannot migrate advertisements for virtual packages. This is an exception to the
  migration of advertisements.

Applications
You can migrate applications from a supported System Center 2012 Configuration
Manager or Configuration Manager current branch source hierarchy to a destination
hierarchy. If you reassign a client from the source hierarchy to the destination hierarchy,
the client retains the history of previously installed applications to prevent the client
from rerunning a migrated application.

Plan to migrate collections
You can migrate the criteria for collections from a supported System Center 2012
Configuration Manager or Configuration Manager current branch source hierarchy. For
this, you use an object-based migration job. When you migrate a collection, you migrate
the rules for the collection and not information about the members of the collection or
information or objects related to the members of the collection.

Migration of the collection object is not supported when you migrate from a
Configuration Manager 2007 source hierarchy.

Plan to migrate operating system deployments
You can migrate the following operating system deployment objects from a supported
source hierarchy:

     Operating system images and packages. The source path of boot images is
     updated to the default image location for the Windows Administrative Installation
     Kit (Windows AIK) on the destination site. The following are requirements and
     limitations to migrating operating system images and packages:

        To successfully migrate image files, the computer account of the SMS Provider
        server for the destination hierarchy's top-level site must have Read and Write
        permission to the image source files of the source site's Windows AIK location.

        When you migrate an operating system installation package, ensure that the
        configuration of the package on the source site points to the folder that has the

<!-- p.840 -->

    WIM file and not to the WIM file itself. If the installation package points to the
    WIM file, the migration of the installation package will fail.

    When you migrate a boot image package from a Configuration Manager 2007
    source site, the package ID of the package is not maintained in the destination
    site. The result of this is that clients in the destination hierarchy cannot use boot
    image packages that are available on shared distribution points.

  Task sequences. When you migrate a task sequence that has a reference to a client
  installation package, that reference is replaced with a reference to the client
  installation package of the destination hierarchy.

    ７ Note

       Only task sequences with native Configuration Manager tasks can be
       migrated. Task sequences that contain non-native tasks including MDT
       tasks or non-Microsoft tasks can't be migrated. Attempting to migrate task
       sequences with non-native tasks results in the following errors in the log
       Migmctrl.log :

       Type <ts-add-in-package> are not found

       ERROR: [MigMCtrl]: FAILED to EXECUTE job. error = Unknown error

       0x80131500, 80131500~

       To migrate task sequences with non-native Configuration Manager tasks,
       remove the non-native tasks and then migrate the task sequence.

       When migrating a task sequence, Configuration Manager might migrate
       objects that aren't required in the destination hierarchy. These objects
       include boot images and Configuration Manager 2007 client installation
       packages.

  Drivers and driver packages. When you migrate driver packages, the computer
  account of the SMS Provider in the destination hierarchy must have full control to
  the package source.

Plan to migrate desired configuration
management
