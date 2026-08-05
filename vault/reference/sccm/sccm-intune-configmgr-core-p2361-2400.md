---
title: "Core infrastructure documentation — pages 2361-2400"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2361-2400
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2361-2400
family: sccm
documentKind: "doc"
abstract: "Operation Example You can also use application requirements to perform this task. For more information, see How to create applications with Configuration Manager. Managing client Although the default client settings in Configuration Manager apply to all settings devices and all"
---

# Core infrastructure documentation — pages 2361-2400

<!-- p.2361 -->

 Operation            Example

                      You can also use application requirements to perform this task. For more
                      information, see How to create applications with Configuration Manager.

 Managing client      Although the default client settings in Configuration Manager apply to all
 settings             devices and all users, you can create custom client settings that apply to a
                      collection of devices or a collection of users.

                      For example, if you want remote control to be available on all but a few
                      devices, configure the default client settings to allow remote control and then
                      configure custom client settings that do not allow remote control, and deploy
                      those to the collection of exceptional clients.

 Power                You can configure specific power settings per collection.
 management

 Role-based           Use collections to control which groups of users have access to various
 administration       functionality in the Configuration Manager console.

 Maintenance          With maintenance windows you can define a time period when various
 Windows              Configuration Manager operations can be carried out on members of a device
                      collection.

Collection types in Configuration Manager
Configuration Manager has built-in collections for common operations, and you can
also create custom collections.

Built-in collections
By default, Configuration Manager includes the following collections, which cannot be
modified.

                                                                                    ﾉ   Expand table

 Collection name        Description

 All User Groups        Contains the user groups that are discovered by using Active Directory
                        Security Group Discovery.

 All Users              Contains the users who are discovered by using Active Directory User
                        Discovery.

 All Users and User     Contains the All Users and the All User Groups collections. This collection
 Groups                 contains the largest scope of user and user group resources.

<!-- p.2362 -->

 Collection name         Description

 All Desktop and         Contains the server and desktop devices that have the Configuration
 Server Clients          Manager client installed. Membership is maintained by Heartbeat Discovery.

 All Mobile Devices      Contains the mobile devices that are managed by Configuration Manager.
                         Membership is restricted to those mobile devices that are successfully
                         assigned to a site or discovered by the Exchange Server connector.

 All Systems             Contains the All Desktop and Server Clients, the All Mobile Devices, and the
                         All Unknown Computers collections, and all mobile devices that are enrolled
                         by Microsoft Intune. This collection contains the largest scope of device
                         resources.

 All Unknown             Contains generic computer records for multiple computer platforms. You
 Computers               can use this collection to deploy an operating system by using a task
                         sequence and PXE boot, bootable media, or prestaged media.

 Co-management           Contains devices that meet the client prerequisites and are eligible for co-
 Eligible Devices        management enrollment (added in version 2111).

Custom collections
When you create a custom collection in Configuration Manager, the membership of that
collection is determined by one or more collection rules, as described in How to create
collections.

Feedback
Was this page helpful?      Yes        No

Provide product feedback

<!-- p.2363 -->

Prerequisites for collections in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Collections in Configuration Manager contain only dependencies within the product.

Configuration Manager dependencies
                                                                                  ﾉ   Expand table

 Dependency                           More information

 Reporting services point             The reporting services point site system role must be
                                      installed before you can run reports for collections. For more
                                      information, see Introduction to reporting.

 Specific security permissions must   You must have the following security permissions to manage
 have been granted to manage          compliance settings:
 collections
                                      - To create and manage collections: Create, Delete, Modify,
                                      Modify Folder, Move Object, Read and Read Resource for
                                      the Collection Object.

                                      - To manage collection settings: Modify Collection Setting
                                      for the Collection Object.

                                      The Modify Folder permission is required for all collection
                                      folders, including the root folder.

Feedback
Was this page helpful?       Yes      No

Provide product feedback

<!-- p.2364 -->

Best practices for collections in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Some collection management guidance can be contradictory. For example, for
performance reasons, you should limit the number of collections that update frequently.
But updating collections frequently is convenient, since most Configuration Manager
functionality is dependent on collections. Carefully consider both performance impacts
and business requirements when you design and configure collections and collection
evaluation.

Use the following best practices for collections in Configuration Manager.

Configure maintenance window for updates
You can configure maintenance windows for device collections to restrict the times that
Configuration Manager can install software on these devices. If you configure the
maintenance window to be too small, the client may not install critical software updates.
This state leaves the client vulnerable to the issues the update mitigates.

Important considerations to keep in mind when planning your maintenance windows:

      The default software update maximum run time is 60 minutes.
      When Configuration Manager calculates whether an update can install, it adds five
      minutes to the maximum run time to account for a restart.
      The remaining duration of a maintenance window must be longer than the
      maximum run time of the software update plus five minutes.

Avoid frequent collection evaluation
A full collection evaluation evaluates not only the targeted collection, but also any
collections that the collection limits if an update occurs. Also, a collection with no
schedule is still evaluated if its limiting collection updates. So it's possible that some
collections may be evaluated more often than you expect.

In a busy Configuration Manager environment, you can improve collection evaluation
performance by scaling back schedules to avoid repeated collection evaluations. In a
deep tree, you can decrease collection evaluation frequency as the collections descend

<!-- p.2365 -->

deeper in the tree, because higher-level collection evaluations will also trigger lower-
level collection evaluations.

Understand the collection evaluation graph
Be aware of how the collection evaluation graph works so you can design an
appropriate collection structure. Don't rely on full collection evaluation to always update
all collections. If an incrementally updated collection updates on a schedule, referencing
collections that aren't enabled for incremental updates may not update. Because
updates likely occurred during incremental evaluations, a full evaluation may not update
the collection, ending the collection evaluation graph for that cycle. In that case, no
referencing collection evaluations occur. For more information, see Collection evaluation
graph.

Limit incremental updates
Enabling incremental updates for many collections might cause evaluation delays. It's
best to limit the number of incrementally updated collections to 200. The exact number
depends on:

     The total number of collections
     The frequency of new resources being added and changed in the hierarchy
     The number of clients in a hierarchy
     The complexity of collection membership rules in a hierarchy

If the incremental evaluation cycle is taking longer than the configured update
frequency, then Configuration Manager is constantly processing collection evaluations,
which could affect system performance. Reduce the number of incrementally updated
collections, or increase the time between incremental evaluation cycles.

Given the potential impacts of incremental collections, it's important to have a policy or
procedure for creating the collections and assigning update schedules. Examples of
policy considerations might be:

     Only use incremental updates for collections that are used for security scoping,
     client settings, and maintenance windows. These collection updates affect client
     behavior and access to resources.
     For applications with no licensing approval, advertise applications to existing
     collections, and use global conditions to restrict availability.
     Outline appropriate periods for other collections that have full collection updates
     scheduled.

<!-- p.2366 -->

Avoid evaluation of large trees from the CAS
In a Configuration Manager environment, the central administration site (CAS) doesn't
evaluate collection membership. Primary sites are the only sites that evaluate collections.
Secondary sites act as proxies that use only data they replicate from their primary site.

To request a collection update, the CAS sends a request to each primary site. The
primary sites evaluate the collection and send the results back to the CAS. The collection
evaluation results appear only after all collection evaluation instructions replicate to all
sites, all sites evaluate all collections, and all data returns to the CAS and is combined.

The following diagram demonstrates the flow when the CAS requests a manual
collection update:

A collection update from a CAS with multiple primary sites can be time consuming. If a
collection doesn't evaluate in a timely fashion, it's tempting to repeat the request.

Once a collection evaluation thread begins and loads the evaluation graph, evaluation
continues until the collection evaluation graph is empty. The thread then terminates and
becomes available for the next evaluation. However, if another collection evaluation
cycle queues while the thread is evaluating collections, the thread immediately restarts
to attempt an evaluation of the "missed" cycle.

Each evaluation method runs in its own thread. It's possible that within the thread,
Configuration Manager may attempt to graph the same collection more than once.
Configuration Manager then drops the second and later requests.

To prevent these scenarios, avoid manual collection evaluations of large trees, especially
when working from the CAS with multiple sites.

<!-- p.2367 -->

Consider collection depth and cross-
referencing
To strike a balance between business requirements and performance, it's important to
understand the collection structure you create, and its dependencies on other
collections. If you create a collection with rules that reference one or more collections
that also refer to other collections, all of those collections are evaluated to create the
membership of the collection.

The include and exclude collection rules in Configuration Manager make referencing
collections easier than writing a custom WQL query. However, if using include and
exclude collections results in a high-performance toll, you can use the WQL query
method instead. Use the following example queries and replace the example collection
ID XYZ0003F with the ID of the collection you want to include or exclude.

Include:

Select * from SMS_R_System where SMS_R_System.ResourceId in (select ResourceID from

SMS_CM_RES_COLL_XYZ0003F)

Exclude:

Select * from SMS_R_System where SMS_R_System.ResourceId not in (select ResourceID

from SMS_CM_RES_COLL_XYZ0003F)

Use CEViewer to monitor collection evaluation
You can use the Collection Evaluation Viewer (CEViewer) to monitor how many
collections are being evaluated and how long each collection is taking to update. The
CEViewer is in the CD.Latest folder on the site server.

   Tip

  Starting in Configuration Manager version 2010, this functionality is built-in to the
  console. For more information, see, How to view collection evaluation.

To manually do a similar check with SQL, you can use the following query:

  SQL

  SELECT [t2].[CollectionName], [t2].[SiteID], [t2].[value] AS [Seconds],
  [t2].[LastIncrementalRefreshTime], [t2].[IncrementalMemberChanges] AS

<!-- p.2368 -->

  [IncChanges], [t2].[LastMemberChangeTime] AS [MemberChangeTime]
  FROM (
      SELECT [t0].[CollectionName], [t0].[SiteID], DATEDIFF(Millisecond, [t1].
  [IncrementalEvaluationStartTime], [t1].[LastIncrementalRefreshTime]) * 0.001
  AS [value], [t1].[LastIncrementalRefreshTime], [t1].
  [IncrementalMemberChanges], [t1].[LastMemberChangeTime], [t1].
  [IncrementalEvaluationStartTime], v1.[RefreshType]
      FROM [dbo].[Collections_G] AS [t0]
      INNER JOIN [dbo].[Collections_L] AS [t1] ON [t0].[CollectionID] = [t1].
  [CollectionID]
      inner join v_Collection v1 on [t0].[siteid] = v1.CollectionID
      ) AS [t2]
  WHERE ([t2].[IncrementalEvaluationStartTime] IS NOT NULL) AND ([t2].
  [LastIncrementalRefreshTime] IS NOT NULL) and (refreshtype='4' or
  refreshtype='6')
  ORDER BY [t2].[value] DESC

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2369 -->

Collection evaluation in Configuration
Manager
Article • 10/12/2022

Applies to: Configuration Manager (current branch)

Configuration Manager uses collection evaluation to update collection membership,
based on the collection rules you define. Collection evaluation scope and timing differ
depending on site and collection configuration and evaluation type.

It's important to understand collection evaluation behavior so you can make appropriate
collection design decisions. For collection evaluation guidance and recommendations,
see Best practices for collections.

Evaluation process
The colleval.log records when the collection evaluator creates, changes, and deletes
collections.

At a high level, each individual collection evaluation and update follows these steps:

   1. Execute the collection query.
   2. Add any systems that are direct members.
   3. Add members specified in the Include collections.
   4. Perform a logical AND between the returned results and the limiting collection.
   5. Remove members specified in the exclude collections.
   6. Compare the result set from evaluating the direct members and include collections
      with the results of the exclude collections.
   7. Write the changes to the database and perform updates.

<!-- p.2370 -->

   8. Trigger any dependent collections to update as well. Dependent collections are
     collections that the current collection limits, or that refer to the current collection
     using include or exclude rules.

   Tip

  You can use management insights in the Configuration Manager console to help
  you manage your collections. There's a group of insights specific to Collections.
  There are also several insights in the Configuration Manager Assessment group for
  collections.

Collection evaluation types and triggers
These types of threads handle collection evaluation, depending on evaluation type:

     Primary for scheduled collection updates
     Auxiliary to manually update collections with dependent collections
     Single to manually update collections with no dependent collections
     Express for incremental collection updates

The following table describes collection evaluation triggers and their corresponding
evaluation types.

                                                                                   ﾉ   Expand table

 Trigger         Evaluation   Description
                 Type

 Manual          Single or    Manual is the highest priority collection evaluation. When an
                 Auxiliary    administrator requests a manual collection evaluation, the collection
                              evaluator assigns the next available evaluation thread to the
                              evaluation.

 Scheduled       Primary      The process of scheduled evaluation is the same as manual
                              evaluation, except the evaluation is time-driven rather than event-
                              driven.

 Staging         Single or    All collections directly or indirectly depend on All Systems or All
                 Auxiliary    Users and User Groups. Both of these collections do a full collection
                              evaluation at 4:00 AM daily. A change to either of these collections
                              triggers updates of dependent collections, based on a full collection
                              graph.

 Incremental     Express      Incremental evaluation uses a collection evaluation graph to
                              evaluate and update dependent collections if an update to the

<!-- p.2371 -->

 Trigger      Evaluation    Description
              Type

                            incremental collection membership changes. Configuration Manager
                            monitors and updates resources objects in all collections that are
                            configured for incremental updates.

                            If a collection query is based on information that will be updated
                            later, like hardware inventory, Configuration Manager only adds or
                            removes the resource from the collection during the scheduled
                            collection update.

Collection evaluation graph
A collection evaluation graph maps all collections that relate to the collection targeted
for evaluation. A collection evaluation involves the targeted collection and any related
collections in the collection evaluation graph.

When collection evaluation starts, Configuration Manager builds a graph that includes
all collections that could possibly need evaluating as a result of changes to the target
collection, starting from the highest level in the cycle. The collection evaluator then
moves through the graph in order, evaluating each collection membership in turn. After
the collection is fully evaluated, the collection evaluator removes lower-level collections
that aren't affected by this cycle from the collection evaluation graph.

If one or more of the collections being evaluated has an include or exclude rule, the
collection evaluator adds the included or excluded collection to the graph, along with
any collections that collection limits. If there are any changes during the evaluation of
the include and exclude collections, the graph continues on that branch before it returns
to the main branch.

Configuration Manager builds two types of evaluation graphs, incremental or full.

Incremental collection evaluation
When table data changes, a SQL Server trigger inserts a row in the
CollectionNotifications table. The next time a collection evaluation schedule fires, it
AND s the resource ID with the existing collection query and triggers updates on

collections that are enabled for incremental collections.

Incremental collection evaluation executes one query per machine. The default site
configuration for incremental collection evaluation is every five minutes.

<!-- p.2372 -->

An incremental collection evaluation graph maps referenced collections only if they're
enabled for incremental evaluation. If an incremental evaluation is limited to a collection
that isn't enabled for incremental evaluation, the graph evaluates the collection based
on the existing membership of the limiting collection.

For example, the following diagram shows newly discovered resources that are
applicable to all collections. However, collection evaluation only updates the All Servers
and All Domain Controllers collections. The collection evaluator doesn't evaluate the
other collections, because the All Member Servers collection isn't enabled for
incremental evaluation.

Full collection evaluation
Manual or scheduled collection evaluations build a full collection evaluation graph of all
dependent collections. The graph includes all collections that reference the collection
that is updating and subsequent collections. Configuration Manager continues to
evaluate down the graph as long as updates occur to the collections being processed.

The following diagram shows how a scheduled or manual collection update request for
the All Servers collection produces a full graph that includes all applicable collections.
The new DNS server and domain controller resources are in scope of the membership
queries of all collections, so all the collections update.

<!-- p.2373 -->

A full evaluation doesn't always evaluate all collections. The collection evaluation graph
only continues to evaluate dependent collections if an update occurs to the current
referenced collection. If an incrementally updated collection updates during scheduled
incremental evaluations, referencing collections that aren't enabled for incremental
updates may not update. A full evaluation doesn't update the collection, ending the
collection evaluation graph and any referencing collection evaluations for that cycle.

In the following example, installing DNS on the existing server makes it a member of the
DNS Servers collection, but because there's no update to its limiting All Member
Servers collection, the full evaluation doesn't evaluate the DNS Servers collection. The
next incremental evaluation cycle will evaluate the DNS Servers collection, because it's
an incremental collection.

<!-- p.2374 -->

Next steps
     How to create collections
     Best practices for collections
     View collection evaluation (starting in version 2010)
     Collection Evaluation Viewer

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2375 -->

How to create collections in
Configuration Manager
Article • 12/05/2022

Applies to: Configuration Manager (current branch)

Collections are groupings of users or devices. Use collections for tasks like managing
applications, deploying compliance settings, or installing software updates. You can also
use collections to manage groups of client settings or use them with role-based
administration to specify the resources that an administrative user can access.
Configuration Manager contains several built-in collections. For more information, see
Introduction to collections.

  ７ Note

  A collection can contain users or devices, but not both.

The information in this article can help you create collections in Configuration Manager.
You can also import collections that were created at the current Configuration Manager
site or at another one. For more information about how to export and import
collections, see How to manage collections.

Collection rules
There are different types of rules that you can use to configure the members of a
collection in Configuration Manager.

Direct rule
Use direct rules to choose the users or computers that you want to add to a collection.
The membership doesn't change unless you remove a resource from Configuration
Manager. Before you can add the resources to a direct rule collection, Configuration
Manager must have discovered them or you must have imported them. Direct rule
collections have more administrative overhead than query rule collections because they
require manual changes.

Query rule

<!-- p.2376 -->

Dynamically update the membership of a collection based on a query that Configuration
Manager runs on a schedule. For example, you can create a collection of users that are a
member of the Human Resources organizational unit in Active Directory Domain
Services. This collection is automatically updated when new users are added to or
removed from the Human Resources organizational unit.

For example queries that you can use to build collections, see How to create queries.

Include collection rule
Include the members of another collection in a Configuration Manager collection. If the
included collection changes, Configuration Manager updates the membership of the
current collection on a schedule.

You can add multiple include collection rules to a collection.

Exclude collection rule
Exclude collection rules let you exclude the members of one collection from another
Configuration Manager collection. If the excluded collection changes, Configuration
Manager updates the membership of the current collection on a schedule.

You can add multiple exclude collection rules to a collection. If a collection includes both
include collection and exclude collection rules and there's a conflict, the exclude
collection rule takes priority.

Example of an exclude collection rule

You create a collection that has one include collection rule and one exclude collection
rule. The include collection rule is for a collection of Dell desktops. The exclude
collection is for a collection of computers that have less than 4 GB of RAM. The new
collection contains Dell desktops that have at least 4 GB of RAM.

Create a collection
   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace.

           To create a device collection, select the Device Collections node. Then, on the
           Home tab of the ribbon, in the Create group, select Create Device Collection.

<!-- p.2377 -->

       To create a user collection, select the User Collections node. Then, on the
       Home tab of the ribbon, in the Create group, select Create User Collection.

2. On the General page of the wizard, provide a Name and a Comment. In the
  Limiting collection section, select Browse, and then select a limiting collection. The
  collection you're creating will contain only members from the limiting collection.

3. On the Membership Rules page, in the Add Rule list, select the type of
  membership rule that you want to use for the collection. You can configure
  multiple rules for each collection. The configuration for each rule varies. For more
  information on configuring each rule, see the following sections of this article:

       Direct rule
       Query rule
       Include collection rule
       Exclude collection rule

4. Also on the Membership Rules page, review the following settings.

       Use incremental updates for this collection: Select this option to periodically
       scan for and update only new or changed resources from the previous
       collection evaluation. This process is independent of a full collection
       evaluation. By default, incremental updates occur at 5-minute intervals.

          ） Important

          Collections with query rules that use the following classes don't support
          incremental updates:
             SMS_G_System_CollectedFile
             SMS_G_System_LastSoftwareScan
             SMS_G_System_AppClientState
             SMS_G_System_DCMDeploymentState
             SMS_G_System_DCMDeploymentErrorAssetDetails
             SMS_G_System_DCMDeploymentCompliantAssetDetails
             SMS_G_System_DCMDeploymentNonCompliantAssetDetails
             SMS_G_User_DCMDeploymentCompliantAssetDetails (for collections
             of users only)
             SMS_G_User_DCMDeploymentNonCompliantAssetDetails (for
             collections of users only)
             SMS_G_System_SoftwareUsageData
             SMS_G_System_CI_ComplianceState

<!-- p.2378 -->

               SMS_G_System_EndpointProtectionStatus
               SMS_GH_System_*
               SMS_GEH_System_*

          Schedule a full update on this collection: Schedule a regular full evaluation
          of the collection membership.

            When you disable this setting, the site clears the schedule. This change
            from previous behavior makes sure that the site doesn't continue to
            evaluate the query. To stop the site evaluating a collection on a schedule,
            disable this option.

            You can't disable the evaluation of built-in collections like All Systems, but
            you can configure the schedule. This behavior allows you to customize this
            action at a time that meets your requirements.

                Tip

               On built-in collections, only change the Time of the custom schedule.
               Don't change the Recurrence pattern. Future versions of
               Configuration Manager might enforce a specific recurrence pattern.

 5. Complete the wizard to create the new collection. The new collection is displayed
    in the Device Collections node of the Assets and Compliance workspace.

 ７ Note

 To see new collection members, refresh or reload the Configuration Manager
 console. They don't appear in the collection until after the first scheduled update.
 You can also manually select Update Membership for the collection. It might take a
 few minutes for a collection update to complete.

Configure a direct rule for a collection
 1. On the Search for Resources page of the Create Direct Membership Rule Wizard,
    specify the following information:

          Resource class: Select the type of resource you want to search for and add to
          the collection. For example:

<!-- p.2379 -->

             System Resource: Search for inventory data returned from client
             computers.
             Unknown Computer: Select from values returned by unknown computers.
             User Resource: Search for user information collected by Configuration
             Manager.
             User Group Resource: Search for user group information collected by
             Configuration Manager.

          Attribute name: Select the attribute associated with the selected resource
          class that you want to search for. For example:

             If you want to select computers by their NetBIOS name, select System
             Resource in the Resource class list and NetBIOS name in the Attribute
             name list.

             If you want to select users by their organizational unit (OU) name, select
             User Resource in the Resource class list and User OU Name in the
             Attribute name list.

          Exclude resources marked as obsolete: If a client computer is marked as
          obsolete, don't include this value in the search results.

          Exclude resources that do not have the Configuration Manager client
          installed: These resources won't be displayed in the search results.

          Value: Enter a value to search the selected attribute name. Use the percent
          character ( % ) as a wildcard. For example:

             To search for computers that have a NetBIOS name beginning with M,
             enter M% in this field.

             To search for users in the Contoso OU, enter Contoso in this field.

   2. On the Select Resources page, select the resources that you want to add to the
     collection in the Resources list, and then select Next.

Configure a query rule for a collection
In the Query Rule Properties dialog box, specify the following information.

     Name: Specify a unique name for the query.

     Import Query Statement: Opens the Browse Query dialog box. Select a
     Configuration Manager query to use as the query rule for the collection.

<!-- p.2380 -->

     Resource class: Select the type of resource you want to search for and add to the
     collection. Select a value from System Resource to search for inventory data
     returned from client computers or from Unknown Computer to select from values
     returned by unknown computers.

     Edit Query Statement: Opens the Query Statement Properties dialog box, where
     you can write a query to use as the rule for the collection. On the General tab, if
     you select the option to Omit duplicate rows (select distinct), it may result in
     fewer rows returned but potentially quicker results. For more information about
     queries, see Introduction to queries.
        Starting in Configuration Manager 2010, you can preview the results when
        you're creating or editing a query for collection membership. For more
        information, see the Preview collection queries section.

Configure an include collection rule
In the Select Collections dialog box, select the collections you want to include in the
new collection, and then select OK.

Configure an exclude collection rule
In the Select Collections dialog box, select the collections you want to exclude from the
new collection, and then select OK.

Preview collection queries
(Introduced in 2010)

Starting in Configuration Manager 2010, you can preview the results when you're
creating or editing a query for collection membership. In the Query Statement
Properties, select the green triangle to show the Query Results Preview window. Select

<!-- p.2381 -->

Stop if you want to stop a long running query.

                                                                                      

Improvements to query preview
(Introduced in 2103)

Starting in Configuration Manager version 2103, you have more options when using the
collection query preview. The following improvements have been made to previewing
collection queries:

     Limit the number of rows returned
        Your limit can be between 1 to 10,000 rows. The default is 5000 rows.
     Omit duplicate rows from the result set
        If the Omit duplicate rows option isn't selected, the original query statement
        will be executed as is, even if the query contains the word distinct.
        When the Omit duplicate rows option is selected, if the query already contains
        the word distinct, then the query runs as it is. When the query doesn't contain
        the word distinct, it's added to the query for the preview (mean override).
     Review statistics for the query preview such as number of rows returned and
     elapsed time.

<!-- p.2382 -->

                                                                                    

  ７ Note

       Elapsed times shown for the query preview may not be the same as actual
       execution of the target query.
       Query execution elapsed time and Displaying results elapsed time shouldn't
       be added for a total elapsed time since these processes run in parallel.

Import a collection
When you export a collection from a site, Configuration Manager saves it as a Managed
Object Format (MOF) file. Use this procedure to import that file into your site database.
To complete this procedure, you need Create permissions on the collections class.

  ） Important

  Make sure the MOF file contains only collection data, is from a trusted source, and
  hasn't been tampered with.

  Also make sure to export the file from a site that's the same version of
  Configuration Manager as the import site.

For more information about exporting collections, see How to manage collections.

<!-- p.2383 -->

   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace. Select either the User Collections or the Device Collections node.

   2. On the Home tab of the ribbon, in the Create group, select Import Collections.

   3. On the General page of the Import Collections Wizard, select Next.

   4. On the MOF File Name page, select Browse. Browse to the MOF file that contains
     the collection information you want to import.

   5. Complete the wizard to import the collection. The new collection is displayed in
     the User Collections or Device Collections node of the Assets and Compliance
     workspace. Refresh or reload the Configuration Manager console to see the
     collection members for the newly imported collection.

Use PowerShell
You can use PowerShell to create and import collections. For more information, see the
following cmdlet articles:

     New-CMCollection

     Set-CMCollection

     Import-CMCollection

Synchronize members to Microsoft Entra
groups
Synchronize collection members to Microsoft Entra groups

Next steps
Manage collections

Synchronize collection members to Microsoft Entra groups

Feedback
Was this page helpful?    Yes    No

<!-- p.2384 -->

Provide product feedback

<!-- p.2385 -->

How to synchronize device collection
members to Microsoft Entra groups
You can enable the synchronization of collection memberships to a Microsoft Entra group. This
synchronization allows you to use your existing on premises grouping rules in the cloud by
creating Microsoft Entra group memberships based on collection membership results. You can
synchronize device or user collections. Only resources with a Microsoft Entra ID record are
reflected in the Microsoft Entra group. Both Microsoft Entra hybrid joined and Microsoft Entra
joined devices are supported. The synchronization of collection memberships is a one-way
process from Configuration Manager to Microsoft Entra ID. Ideally, Configuration Manager
should be the authority for managing the membership for the target Microsoft Entra groups.

Synchronizations can either be full or incremental and they have slightly different behaviors:

     Full synchronization: Occurs on the first synchronization after enabling it. You can force a
     full synchronization by selecting the collection, and then choosing Synchronize
     Membership from the ribbon. A full synchronization will overwrite members of the
     Microsoft Entra group.

     Incremental synchronization: Occurs every 5 minutes. Changes made in Microsoft Entra ID
     aren't reflected in Configuration Manager collections, but they aren't overwritten by
     Configuration Manager.

Example synchronization scenario:

   1. From Microsoft Entra ID, create a group called Group1 and add DeviceA , DeviceB , and
     DeviceC .

           Ideally, objects wouldn't be added from Microsoft Entra ID since Configuration
           Manager should manage the group membership.

   2. From Configuration Manager, create a collection called Collection1 then add DeviceB ,
     and DeviceC .
   3. Enable synchronization for Collection1 to Group1 .
   4. The first synchronization is a full synchronization so, Group1 now contains DeviceB , and
     DeviceC . DeviceA was removed from the group during the full synchronization.

   5. Remove DeviceC from Collection1 and wait for an incremental synchronization.
   6. Group1 now contains only DeviceB .
   7. From Microsoft Entra ID, add DeviceD to Group1 and wait for an incremental
     synchronization.
   8. Group1 now contains DeviceB and DeviceD .

<!-- p.2386 -->

 9. From Configuration Manager, select Collection1 , and choose Synchronize Membership
   from the ribbon to force a full synchronization.
10. Group1 now contains only DeviceB

Prerequisites
   Supported version of Windows 10 (x64) or Windows 11 (x64)

   Windows Server OS 2019 and later (Standard or Datacenter)

   Integration with Microsoft Entra ID for cloud management.

   Microsoft Entra user discovery

   An HTTPS or Enhanced HTTP-enabled management point

   Access to the All Systems collection

     ７ Note

     The option to Disable Microsoft Entra authentication for this tenant, under Azure
     Services for Cloud Management in the console, must not be checked as this prevents
     client registration using Entra ID Authentication.

Create a group and set the owner in Microsoft
Entra ID
 1. Sign in to the Azure portal   .

 2. Navigate to Microsoft Entra ID > Groups > All groups.

 3. Select New group, enter a Group name, and optionally enter a Group description.

 4. Make sure that Membership type is Assigned.

 5. Select Owners, then add the identity that will create the synchronization relationship in
   Configuration Manager.

      Tip

<!-- p.2387 -->

        The Server App (Service Principle) of Microsoft Entra tenant will be the owner for the
        created Microsoft Entra group.

   6. Select Create to finish creating the Microsoft Entra group.

Enable collection synchronization for the Azure
service
   1. In the Configuration Manager console, go to the Administration workspace. Expand
     Cloud Services, and select the Azure Services node.

   2. Select the cloud management service for the Microsoft Entra tenant where you created
     the group. Then in the ribbon, select Properties.

   3. Switch to the Collection Synchronization tab, and select the option to Enable Azure
     Directory Group Sync.

   4. Select OK to save the setting.

Enable the collection to synchronize
   1. In the Configuration Manager console, go to the Assets and Compliance workspace, and
     select either the Device Collections or User Collections node.

   2. Select the collection to sync. Then in the ribbon, select Properties.

   3. Switch to the Cloud Sync tab, and select Add.

   4. If necessary, change the Tenant to where you created the Microsoft Entra group.

   5. Type in your search criteria in the Name starts with field, then select Search. If you leave
     the criteria blank, the search returns all groups from the tenant. If it prompts you to sign
     in, use the identity you specified as the owner for the Microsoft Entra group.

   6. Choose the target group, and then select OK to add the group. Select OK again to exit
     the collection's properties.

Wait about five to seven minutes before you can verify the group memberships in the Azure
portal. To start a full synchronization, select the collection, and then in the ribbon select
Synchronize Membership.

<!-- p.2388 -->

                                                                                                 

Use PowerShell
You can use PowerShell to synchronize collections. For more information, see the following
cmdlet article:

Set-CMCollectionCloudSync

Monitor the collection synchronization status
   1. In the Configuration Manager console, go to the Monitoring workspace

   2. select Collection Cloud Sync and select either the Device Collections or User Collections
     node.

   3. The view lists all the collections that are enabled for cloud sync and relevant details.

   4. Right click on column header and add additional columns to view more information.

   5. On clicking each collection, you can view collection member status in the bottom tab.

   6. The members are categorized based on sync status - Success, Failed, In Progress.

   7. On clicking Failed tab, you can find the reason for failure across each member.

<!-- p.2389 -->

                                                                                          

Default Columns:

     Collection Id – Id of Collection

     Collection Name – Name of Collection

     Microsoft Entra group Id – Configured Microsoft Entra group Id

     Microsoft Entra group Name – Configured Microsoft Entra group Name

     Cloud Sync Status

     Success: If all members are synchronized to target Microsoft Entra group

     Partial Success: If at least one member is synchronized to target Microsoft Entra group

     Failed: If all members failed to synchronize to target Microsoft Entra group

     In Progress: Synchronization is in progress.

     Member Count – Count of members of collection

     Sync Completed – Count of members successfully synchronized

     Sync InProgress – Count of members pending synchronization

     Sync Failed – Count of members failed to synchronize

Optional Columns:

     Cloud Service Id – Azure Service Id which is used for Cloud Sync

     Collection Type – Type of Collection (Device or User)

<!-- p.2390 -->

     Last Full Sync Member Count – Count of members synchronized during last full sync

     Last Full Sync Status – Status of last full sync cycle

     Last Full Sync Time – Time of last full sync cycle

     Last Sync Member Count - Count of members synchronized during last sync

     Last Sync Status - Status of last sync cycle

     Last Sync Time - Time of last sync cycle

Verify the Microsoft Entra group membership
  1. Go to the Azure portal    .

  2. Navigate to Microsoft Entra ID > Groups > All groups.

  3. Find the group you created and select Members.

  4. Confirm that the members reflect the resources in the Configuration Manager collection.
     Only resources with Microsoft Entra identity show in the group.

Last updated on 12/08/2025

<!-- p.2391 -->

How to manage collections in
Configuration Manager
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

Use the overview information in this article to help you run management tasks for
collections in Configuration Manager.

For information about how to create Configuration Manager collections, see How to
create collections.

Collection actions
In the Configuration Manager console, go to the Assets and Compliance workspace.
Select Device Collections or User Collections, select the collection to manage, and then
select a management task.

Manage device collections

Show Members
Displays all of the resources that are members of the selected collection in a temporary
node under the Devices node.

Add Selected Items
Provides the following options:

      Add Selected Items to Existing Device Collection: Opens the Select Collection
      window. Select the collection to which you want to add the members of the
      selected collection. The selected collection is included in this collection by using an
      Include Collections membership rule.

      Add Selected Items to New Device Collection: Opens the Create Device
      Collection Wizard where you can create a new collection. The selected collection is
      included in this collection by using an Include Collections membership rule.

For more information, see How to create collections.

<!-- p.2392 -->

Install Client
Opens the Install Client Wizard. This wizard uses client push installation to install a
Configuration Manager client on all computers in the selected collection. For more
information, see Client push installation.

Run Script

Opens the Run Script wizard to run a PowerShell script on all of the clients in the
collection. For more information, see Create and run PowerShell scripts.

Start CMPivot
Opens CMPivot for this collection. Use CMPivot to query device information and take
action in real time. For more information, see CMPivot for real-time data.

Manage Affinity requests
Opens the Manage User Device Affinity Requests dialog box. Approve or reject
pending requests to establish user device affinities for devices in the selected collection.
For more information, see Link users and devices with user device affinity.

Clear Required PXE deployments
Clears any required PXE boot deployments from all members of the selected collection.
For more information, see Use PXE to deploy Windows over the network.

Update membership
Evaluates the membership for the selected collection. For collections with many
members, this update might take some time to finish. Use the Refresh action to update
the display with the new collections members after the update is completed.

Synchronize membership
If you configured this collection for cloud sync, synchronize the current membership
with a Microsoft Entra group. For more information, see Create collections.

Add resources

<!-- p.2393 -->

Opens the Add Resources to Collection window. Search for new resources to add to the
selected collection. The icon for the selected collection displays an hourglass symbol
while the update is in progress.

Client notification
For more information, see Client notifications.

Client diagnostics
Displays the following options:

     Enable verbose logging
     Disable verbose logging
     Collect client logs

For more information, see Client diagnostics.

Endpoint Protection

For more information, see Client notifications: Endpoint protection.

Export

Opens the Export Collection Wizard that helps you export this collection to a Managed
Object Format (MOF) file. You can then archive this file, or import it to another
Configuration Manager site. When you export a collection, referenced collections aren't
exported. A referenced collection is referenced by the selected collection by using an
Include or Exclude rule.

Copy
Creates a copy of the selected collection. The new collection uses the selected collection
as a limiting collection.

Refresh
Refresh the view.

Delete

<!-- p.2394 -->

Deletes the selected collection. You can also delete all of the resources in the collection
from the site database.

You can't delete the collections that are built into Configuration Manager. For a list of
the built-in collections, see Introduction to collections.

Starting in version 2203, when you delete a collection, you can review and delete its
dependent collections at the same time. For more information, see Delete collection
references.

Simulate deployment

Opens the Simulate Application Deployment Wizard. This wizard lets you test the
results of an application deployment without installing or uninstalling the application.
For more information, see How to simulate application deployments.

Deploy

Displays the following options:

     Application: Opens the Deploy Software Wizard. Select and configure an
     application deployment to the selected collection. For more information, see How
     to deploy applications.

     Program: Opens the Deploy Software Wizard. Select and configure a package and
     program deployment to the selected collection. For more information, see
     Packages and programs.

     Configuration Baseline: Opens the Deploy Configuration Baselines window.
     Configure the deployment of one or more configuration baselines to the selected
     collection. For more information, see How to deploy configuration baselines.

     Task Sequence: Opens the Deploy Software Wizard. Select and configure a task
     sequence deployment to the selected collection. For more information, see Deploy
     a task sequence.

     Software Updates: Opens the Deploy Software Updates Wizard. Configure the
     deployment of software updates to resources in the selected collection. For more
     information, see Deploy software updates.

View relationships

For more information, see View collection relationships.

<!-- p.2395 -->

Move
Move the selected collection to another folder in the Device Collections node.

Properties

For more information, see Collection properties.

Delete collection references
Previously, when you would delete a collection with dependent collections, you first had
to delete the dependencies. The process of finding and deleting all of these collections
could be difficult and time consuming. Starting in version 2203, when you delete a
collection, you can review and delete its dependent collections at the same time.

A new Details window shows more information about the relationship types, and lets
you view collection relationships in a graphical chart.

                                                                                     

   1. Delete a collection that has dependent collections.

   2. In the Delete Collection Error window, select Details.

   3. Once the relationship types finish loading, select View Relationships to see the
     graph.

   4. If all of the dependent collections can be deleted, select Delete all listed
     collections.

   5. Review the list of collections and any software deployments that the site will also
     remove. You also can Delete each collection member from the database.

There are several reasons why the site can't delete a dependent collection:

     Assigned to user: For more information, see Modify the administrative scope of an
     administrative user.

<!-- p.2396 -->

     Used by cloud attach: For more information, see Enable cloud attach for
     Configuration Manager.

     Use for upload to Microsoft Intune: For more information, see Make
     Configuration Manager collections available to assign Endpoint security policies.

The details window lists collections that can't be deleted with the reason why.

Known issue when deleting collection references
Consider the scenario where you're deleting collections with references, and another
administrative user is simultaneously creating a reference to a collection that you're
deleting. When this behavior occurs, the console displays an error, and the collection
isn't deleted.

Manage user collections
The following actions are available on user collections. The behaviors are the same as
with device collections, other than they apply to user collections and the users within.
For more information, see the corresponding action under Manage device collections.

     Show Members
     Add Selected Items
         Add Selected Items to Existing User Collection
         Add Selected Items to New User Collection
     Manage Affinity Requests
     Update Membership
     Synchronize Membership
     Add Resources
     Export
     Copy
     Refresh
     Delete
     Simulate Deployment
     Deploy
         Application
         Program
         Configuration Baseline
     View Relationships
     Move
     Properties

<!-- p.2397 -->

Collection properties
When you view properties for a collection, you can view and configure the following
options:

     General: View and configure general information about the selected collection
     including the collection name, the limiting collection, the collection ID, and last
     update times.

     Membership Rules: Configure the membership rules that define the membership
     of this collection. For more information, see How to create collections.

     Power Management: Configure power management plans that you've assigned to
     computers in the selected collection. For more information, see Introduction to
     power management.

     Deployments: Displays any software that you've deployed to members of the
     selected collection.

     Maintenance Windows: View and configure maintenance windows that are
     applied to members of the selected collection. For more information, see How to
     use maintenance windows.

     Collection Variables: Configure variables that apply to this collection and can be
     used by task sequences. For more information, see How to set task sequence
     variables.

     Distribution Point Groups: Associate one or more distribution point groups to
     members of the selected collection. For more information, see Manage content
     and content infrastructure.

     Cloud Sync: Synchronize collection membership results to Microsoft Entra groups.
     For more information, see Create collections.

     Starting in version 2006, you can also make this collection available to assign
     endpoint security policies when you tenant-attach the site. For more information,
     see Tenant attach: Onboard Configuration Manager clients to Microsoft Defender
     for Endpoint from the admin center.

     Security: Displays the administrative users who have permissions for the selected
     collection from associated roles and security scopes. For more information, see
     Fundamentals of role-based administration.

     Alerts: Configure when alerts are generated for client status and endpoint
     protection. For more information, see How to configure client status and How to

<!-- p.2398 -->

     monitor endpoint protection.

Automate with Windows PowerShell
You can use the following PowerShell cmdlets to manage collections:

Generic cmdlets for all collection types

Basic cmdlets
     Get-CMCollection
     New-CMCollection
     Remove-CMCollection
     Set-CMCollection

Other actions

     Copy-CMCollection
     Export-CMCollection
     Get-CMCollectionMember
     Get-CMCollectionSetting
     Import-CMCollection
     Invoke-CMCollectionUpdate

Get membership rules
     Get-CMCollectionDirectMembershipRule
     Get-CMCollectionExcludeMembershipRule
     Get-CMCollectionIncludeMembershipRule
     Get-CMCollectionQueryMembershipRule

Remove membership rules

     Remove-CMCollectionDirectMembershipRule
     Remove-CMCollectionExcludeMembershipRule
     Remove-CMCollectionIncludeMembershipRule
     Remove-CMCollectionQueryMembershipRule

Device collection-specific cmdlets

<!-- p.2399 -->

Basic actions for device collections
    Get-CMDeviceCollection
    New-CMDeviceCollection

Device collection variables
    Get-CMDeviceCollectionVariable
    New-CMDeviceCollectionVariable
    Remove-CMDeviceCollectionVariable
    Set-CMDeviceCollectionVariable

Add device collection membership rules
    Add-CMDeviceCollectionDirectMembershipRule
    Add-CMDeviceCollectionExcludeMembershipRule
    Add-CMDeviceCollectionIncludeMembershipRule
    Add-CMDeviceCollectionQueryMembershipRule

Get device collection membership rules

    Get-CMDeviceCollectionDirectMembershipRule
    Get-CMDeviceCollectionExcludeMembershipRule
    Get-CMDeviceCollectionIncludeMembershipRule
    Get-CMDeviceCollectionQueryMembershipRule

Remove device collection membership rules

    Remove-CMDeviceCollectionDirectMembershipRule
    Remove-CMDeviceCollectionExcludeMembershipRule
    Remove-CMDeviceCollectionIncludeMembershipRule
    Remove-CMDeviceCollectionQueryMembershipRule

User collection-specific cmdlets
    Get-CMUserCollection
    New-CMUserCollection

Add user collection membership rules

<!-- p.2400 -->

     Add-CMUserCollectionDirectMembershipRule
     Add-CMUserCollectionExcludeMembershipRule
     Add-CMUserCollectionIncludeMembershipRule
     Add-CMUserCollectionQueryMembershipRule

Get user collection membership rules

     Get-CMUserCollectionDirectMembershipRule
     Get-CMUserCollectionExcludeMembershipRule
     Get-CMUserCollectionIncludeMembershipRule
     Get-CMUserCollectionQueryMembershipRule

Remove user collection membership rules

     Remove-CMUserCollectionDirectMembershipRule
     Remove-CMUserCollectionExcludeMembershipRule
     Remove-CMUserCollectionIncludeMembershipRule
     Remove-CMUserCollectionQueryMembershipRule

Next steps
Client notifications

View collection relationships

Feedback
Was this page helpful?      Yes    No

Provide product feedback
