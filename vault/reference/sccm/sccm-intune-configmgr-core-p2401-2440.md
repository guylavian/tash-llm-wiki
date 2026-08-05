---
title: "Core infrastructure documentation — pages 2401-2440"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2401-2440
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2401-2440
family: sccm
documentKind: "doc"
abstract: "View collection relationships Article • 10/04/2022 Applies to: Configuration Manager (current branch) You can view dependency relationships between collections in a graphical format. It shows limiting, include, and exclude relationships.  If you want to change or delete collect"
---

# Core infrastructure documentation — pages 2401-2440

<!-- p.2401 -->

View collection relationships
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can view dependency relationships between collections in a graphical format. It
shows limiting, include, and exclude relationships.

                                                                                         

If you want to change or delete collections, view the relationships to understand the
effect of the proposed change. Before you create a deployment, look at the potential
target collection for any include or exclude relationships that might affect the
deployment.

When you select the View Relationships action on a device or user collection:

      To view the relationships with parent collections, select Dependency.

      To view the relationships with child collections, select Dependent.

For example, if you select the All Systems collection to view its relationships, the
Dependency node will be 0 as it has no parent collections.

Use the following tips to navigate the relationship viewer:

      Select the plus ( + ) or minus ( - ) icons next to the collection name to expand or
      collapse members of a node.

      The number in parentheses after the collection name is the number of
      relationships. If the number is 0, then that collection is the final or leaf node in that
      relationship tree.

<!-- p.2402 -->

The style and color of the line between the collections determines the type of
relationship:

If you hover over a specific line, a tooltip shows the relationship type.

The maximum number of child nodes displayed depends upon the level of the
graph:
   First level: five nodes
   Second level: three nodes
   Third level: two nodes
   Fourth level: one node

If there are more objects than the graph can display at that level, you'll see the
More icon.

When the width of the tree is larger than the window, use the green arrows to the
right or the left to view more.

When a node of the relationship tree is larger than the available space, select More
to change the view to just that node.

To navigate to a prior view, select the Back arrow in the upper right corner. Select
the Home icon to return to the main page.

Use the Search box in the upper right corner to locate a collection in the current
tree view.

Use the Navigator in the lower right corner to zoom and pan around the tree. You
can also print the current view.

You can only see relationships between collections to which you have permission:

   If you have permission for All Systems or All Users and User Groups, then you'll
   see all relationships.

<!-- p.2403 -->

         If you don't have permission for a specific collection, you don't see it in the
         graph, and can't view its relationships.

Improvements in version 2103
Starting in version 2103, you can view both dependency and dependent relationships
together in a single graph. This change allows you to quickly see an overview of all the
relationships of a collection at once and then drill down into specific related collections.
It also includes other filtering and navigation improvements.

The following example shows the relationships for the "c1" collection in the center. It's
dependent upon the collections above it (parents), and has dependencies below it
(children).

                                                                                       

To see the relationships of another collection in the graph, select it to open a new
window targeted on that collection.

Other improvements:

     There's a new Filter button in the upper right corner. This action lets you reduce
     the graph to specific relationship types: Limiting, Include, or Exclude.

     If you don't have permissions to all related collections, the graph includes a
     warning message that the graph may be incomplete.

<!-- p.2404 -->

     When the graph is wider than the window can display, use the page navigation
     controls in the upper left corner. The first number is the page for parents (above),
     and the second number is the page for children (below). The window title also
     shows the page numbers.

     The tooltip for a collection displays the count of dependencies it has and the count
     of dependant collections where applicable. This count only includes unique
     subcollections. The count no longer displays in the parentheses next to the
     collection name.

     Previously the Back button took you through your viewing history. Now it takes
     you to the previously selected collection. For example, changing pages for the
     current collection doesn't activate the Back button. When you select a new
     collection, you can select Back to return to the original collection graph.

   Tip

  Hold the Ctrl key and scroll the mouse wheel to zoom the graph.

For more information on how to navigate the collection dependency graph with a
keyboard, see Accessibility features.

Next steps
How to view collection evaluation

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2405 -->

How to view collection evaluation
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Starting in Configuration Manager version 2010, the functionality of Collection
Evaluation Viewer is integrated into the Configuration Manager console. On each
primary site, this functionality provides administrators a central location to view and
troubleshoot the collection evaluation process. The console displays the following
information:

      Historic and live information for full and incremental collection evaluations
      The evaluation queue status
      The time for collection evaluations to complete
      Which collections are currently being evaluated
      The estimated time that a collection evaluation will start and complete

   Tip

  Viewing collection evaluation at the CAS changed in Configuration Manager
  version 2103. For more information, see the Collection evaluation information at
  the CAS section.

  When using the console connected to a CAS using Configuration Manager 2010,
  you'll see the following behavior:

        Evaluation-related columns for device collections won't contain data.
        The Collection Evaluation node under the Monitoring workspace isn't shown.
        Evaluation-related information, such as evaluation status and links to the
        collection evaluation queues, won't be shown in the collection Summary
        group pane.

Collection evaluation queues
The collection evaluation process evaluates the membership rules of a collection to
update its members. A primary site places a collection that it's evaluating into one of
four different queues:

      Full Evaluation Queue: For collections due for full evaluation
      Incremental Evaluation Queue: For collections with incremental evaluation

<!-- p.2406 -->

     Manual Evaluation Queue: For collections that an administrator has manually
     selected for evaluation from the console
     New Evaluation Queue: For newly created collections

Add columns for the Device Collections node
Adding columns to the Device Collections node allows you to view collection evaluation
information for multiple collections.

   1. Connect the Configuration Manager console to a primary site.
   2. Go to Assets and Compliance > Overview > Device Collections.
   3. Add any or all of the following columns prefixed by the type of evaluation:

           Evaluation (Full)
              Last Completion Time: When the last collection evaluation completed
              (default column)
              Run Time: How long the last collection evaluation ran, in seconds
              Next Refresh Time: When the next full evaluation starts
              Member Changes: The member changes in the last collection evaluation.
              Positive numbers mean members were added while negative numbers
              mean members were removed.
              Last Member Change Time: The most recent time that there was a
              membership change in the collection evaluation
           Evaluation (Incremental)
              Last Evaluation Completion Time: When the last collection evaluation
              completed
              Run Time: How long the last collection evaluation ran, in seconds
              Member Changes: The member changes in the last collection evaluation.
              These changes are either plus (members added) or minus (members
              removed).
              Last Member Change Time: The most recent time that there was a
              membership change in the collection evaluation

<!-- p.2407 -->

                                                                                  

View evaluation information from the
collection summary
View the collection summary information to get information specific to the evaluation of
a single collection.

   1. Connect the Configuration Manager console to a primary site.
   2. Go to Assets and Compliance > Overview > Device Collections.
   3. Select a collection from the Device Collections node.
   4. In the Summary group pane for collection, review the evaluation-related
     information for the selected collection.

                                                                                  

<!-- p.2408 -->

   5. The Related Objects give links to view status of the collection in the specific queue.
     These links take you to the queues in the Monitoring workspace under the
     Collection Evaluation node.

           This action creates a new node is created where you can see the evaluation
           status for the specific collection.

Monitoring collection evaluation queues
Monitoring the collection evaluation queues can give you deeper insight into the
collection evaluation process.

   1. Connect the Configuration Manager console to a primary site.
   2. From the Monitoring workspace, go to the Collection Evaluation node. Starting in
     Configuration Manager 2103, go to Monitoring > Collection Evaluation >
     Collection Evaluation Queue. The following queues are summarized and have their
     own nodes:

           Full Evaluation Queue: For collections due for full evaluation
           Incremental Evaluation Queue: For collections with incremental evaluation
           Manual Evaluation Queue: For collections that an administrator has manually
           selected for evaluation from the console
           New Evaluation Queue: For newly created collections

   3. The total number of collections in queue and queue length is listed as a summary.
     Additionally, the following status summaries for the evaluation queues are listed:

           Number of collections in queue
           Queue length
           Current evaluation collection
           Current evaluation started on
           Current evaluation elapsed (seconds)

   4. Starting in Configuration Manager 2103, you can:

           Configure a primary site's refresh interval for the Collection Evaluation
           statistics page to be between 1 minute and 1440 minutes (1 day). Typically,
           collection evaluation occurs over the course of seconds or minutes. However,
           you can change the statistics refresh to accommodate your environment. The
           default Refresh Interval (minutes) is 5.
           Copy collection evaluation statistics as structured text to the clipboard. Use
           the Copy button in the ribbon to copy the statistics. When the text is pasted
           into a text editor, it's structured to make it easy to read.

<!-- p.2409 -->

   5. Selecting the node for a queue brings up detailed status for the queue including:

          Name: Name of the collection
          Collection ID: ID of the collection
          Estimated Completion Time: When the evaluation is estimated to complete
          Estimated Run Time: How long the evaluation is estimated to run, in
          day:hour:minute:second format

                                                                                   

Full and incremental evaluation status nodes
(Introduced in 2103)

The Full Evaluation Status and Incremental Evaluation Status subnodes have been
added to the Collection Evaluation node in the Monitoring workspace.

     On a primary site, Full Evaluation Status and Incremental Evaluation Status show
     the data for the local evaluations.

     On a CAS, Full Evaluation Status and Incremental Evaluation Status shows the
     data from the primary site with the longest run time.
        Using the longest runtime for these nodes is the same logic that's used for the
        collection evaluation columns at the CAS.

<!-- p.2410 -->

                                                                                     

Collection evaluation information at the CAS
(Introduced in 2103)

Since collection evaluation happens at the primary site level, the collection evaluation
view on the CAS is a summary of what's occurring on the primary sites. Starting in
Configuration Manager version 2103, there are two new tabs in the details pane of the
collection view in the console. The following new tabs show collection evaluation
information from all primary sites in hierarchy:

     Evaluation (Full) In Hierarchy
     Evaluation (Incremental) In Hierarchy

                                                                                     

<!-- p.2411 -->

From the Device Collections node at the CAS, the evaluation columns display the
evaluation status from the primary site with the longest run time. The column
information at the CAS for the full evaluation status could be from a different primary
site than the incremental information since the longest runtime for the incremental
might have occurred at a different primary.

For instance, incremental evaluation for the All Systems collection on the WMI primary
site takes longer than the other primary sites. The full evaluation columns on the CAS
display the information from primary site WMI for the All Systems collection in the
Device Collections node.

                                                                                       

Drill through from collection evaluation queue
or status view to a collection
(Introduced in 2103)

You can navigate to a collection in the Assets and Compliance workspace from a
collection evaluation status view or evaluation queue in the Monitoring workspace.
Select a collection from one of the status views or queues, then choose View collection
from the ribbon or right-click menu to open the collection.

Navigation to the collection from queues won't occur if the collection evaluation has
completed. You can only drill though from an item in a queue that's still currently
running its evaluation. If the evaluation has already completed, the View collection
action takes you to the main collection view. Drill though from the evaluation status
views, Full Evaluation Status and Incremental Evaluation Status, will always take you to
the collection.

<!-- p.2412 -->

                                                                   

Next steps
Learn more about Collection evaluation in Configuration Manager.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2413 -->

How to use maintenance windows in
Configuration Manager
07/25/2025

Applies to: Configuration Manager (current branch)

Use maintenance windows to define when Configuration Manager can run impacting tasks on
devices. Maintenance windows help make sure that client configuration changes occur during
times that don't affect productivity. With Software Center, users can see the device's next
maintenance window on the Installation status tab.

The following tasks support maintenance windows:

     Application and package deployments

     Software update deployments

     Compliance settings deployment and evaluation

     OS and custom task sequence deployments

Configure maintenance windows with an effective date, a start and end time, and a recurrence
pattern. The maximum duration of a window has to be less than 24 hours. The console doesn't
allow a single maintenance window longer than 24 hours. For example, if you want to allow
maintenance all day Saturday and Sunday, then create two 24-hour maintenance windows for
each day.

By default, computer restarts caused by a deployment aren't allowed outside of a maintenance
window, but you can override the default. Maintenance windows affect only the time when the
deployment runs. Deployments that you configure to download and run locally can download
content outside of the window.

When a client is a member of a device collection that has a maintenance window, a
deployment runs only if its maximum allowed run time doesn't exceed the duration of the
window. If the deployment fails to run, the client generates an alert. It then reruns the
deployment during the next scheduled maintenance window that has available time.

   Tip

  A maintenance window is for a client. A service window is for a site server. For more
  information, see Service windows for site servers.

<!-- p.2414 -->

Multiple maintenance windows
When a client computer is a member of multiple device collections that have maintenance
windows, these rules apply:

     If the maintenance windows don't overlap, the client treats them as two independent
     maintenance windows.

     If the maintenance windows overlap, the client treats them as a single window for the
     entire time of both windows. For example, you create two maintenance windows on a
     collection. The first is effective from 6:00 to 7:00, and the second is effective from 6:30 to
     7:30. Because they overlap by 30 minutes, the effective duration of the combined
     maintenance window is 90 minutes from 6:00 to 7:30.

When a user installs an application from Software Center, the client starts it immediately. It
prioritizes the user's intent over the administrator's.

If an application deployment with a purpose of Required reaches its installation deadline
during the non-business hours that a user configures in Software Center, the client installs the
application. It prioritizes the administrator's intent over the user's.

By default, with multiple maintenance windows, the client only installs software updates during
Software Update type windows. It ignores any All deployments maintenance windows, unless
they're the only type. You can configure this behavior with the following client setting in the
Software updates group: Enable installation of software updates in "All deployments"
maintenance window when "Software Update" maintenance window is available. For more
information, see About client settings.

  ７ Note

  This setting also applies to maintenance windows that you configure to apply to Task
  sequences.

  If the client only has an All deployments window available, it still installs software updates
  or task sequences in that window.

Configure maintenance windows
   1. In the Configuration Manager console, go to the Assets and Compliance workspace.

   2. Select the Device Collections node, and then select a collection.

<!-- p.2415 -->

    ７ Note

    You can't create maintenance windows for the All Systems collection.

3. On the Home tab of the ribbon, in the Properties group, choose Properties.

4. Switch to the Maintenance Windows tab, and select the New icon.

  a. Specify a Name to uniquely identify this maintenance window for the collection.

  b. Configure the Time settings:

          Effective date: The date when the maintenance windows starts. The default is the
          current date.

          Start and End: The start and end times of the maintenance window. It calculates
          the Duration for the window. The minimum duration is five minutes, and the
          maximum is 24 hours. The default duration is three hours, from 01:00 to 04:00.

          Coordinated Universal Time (UTC): Enable this option for the client to interpret
          the start and end times in the UTC time zone. For regionally or globally
          distributed devices in the same collection, this option sets the maintenance
          window to occur simultaneously on all devices in the collection. Disable this
          option for the client to use the device's local time zone. This option is disabled by
          default.

  c. Configure the recurrence pattern. The default is once per week on the current day of
     the week.

       ７ Note

       Starting in version 2207, you can offset monthly maintenance window schedules
       to better align deployments with the release of monthly security updates. For
       example, using an offset of two days after the second Tuesday of the month, sets
       the maintenance window for Thursday.

  d. Apply this schedule to: By default the window applies to All deployments. You can
     select either Software updates or Task sequences to further control what deployments
     run during this window.

        Tip

<!-- p.2416 -->

           If you configure multiple maintenance windows of different types on the same
           collection, make sure you understand the client behaviors. For more information,
           see Multiple maintenance windows.

   5. Select OK to save and close the window.

The Maintenance Windows tab of the collection properties displays all configured windows.

Use PowerShell
You can use PowerShell to configure maintenance windows. For more information, see the
following articles:

     Get-CMMaintenanceWindow
     New-CMMaintenanceWindow
     Remove-CMMaintenanceWindow
     Set-CMMaintenanceWindow

Known Issues

Using Offset Maintenance Windows in the last week of the
month
Offset Maintenance Windows scheduled in the last week of the month may encounter the
following scheduling discrepancies:

     If the offset value causes the start date to fall in the following month, it will be adjusted to
     the end of the current month.
     If the offset value causes the start date to fall on the last day of the current month, no
     Maintenance Window will be scheduled for that month.

  ７ Note

  The issues with Offset Maintenance Windows scheduled in the last week of the month is
  resolved in version 2503. Offset values that cause the Maintenance Window to be
  scheduled on or after the last day of the current month now schedule as expected.

UTC Maintenance Windows and Daylight Saving Time

<!-- p.2417 -->

When calculating the difference from UTC to local time, the client will use the active bias from
the "Effective date" of the maintenance window to calculate the local time from the UTC time:

     If Daylight Saving Time (DST) is active on the effective date, then this bias from UTC will
     always be used, causing the Maintenance Window to open an hour earlier than expected
     when DST ends.
     If Daylight Saving Time (DST) is not active on the effective date, then this bias from UTC
     will always be used, causing the Maintenance Window to open an hour later than
     expected when DST starts.

<!-- p.2418 -->

Security and privacy for collections in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article contains security recommendations and privacy information for collections in
Configuration Manager.

Security recommendations
When you export or import a collection by using a managed object format (MOF) file
that's saved to a network location, secure the location and the network channel. Restrict
who can access the network folder. Use Server Message Block (SMB) signing or Internet
Protocol security (IPsec) between the network location and the site server. These
mechanisms help prevent an attacker from tampering with the exported collection data.
Use IPsec to encrypt the data on the network to prevent information disclosure.

Security issues
Collections have the following security issues:

      If you use collection variables, local administrators can read potentially sensitive
      information. Collection variables are only used when you deploy an OS. For more
      information, see Collection and device variables.

Privacy information
There's no privacy information specifically for collections in Configuration Manager.
Collections are containers for resources, such as users and devices. Collection
membership often depends on the information that Configuration Manager collects
during standard operation.

Configuration Manager can collect resource information from discovery or inventory.
Using this information, you can configure a collection to contain the devices that meet
your specified criteria. Collections might also be based on the current status information
for client management operations. For example, deploying software or checking for
compliance. Along with query-based collections, you can also directly add resources to
collections.

<!-- p.2419 -->

Next steps
For more information about collections, see Introduction to collections.

For more information about other security features in Configuration Manager, see the
Security documentation hub.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2420 -->

Introduction to hardware inventory
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use hardware inventory in Configuration Manager to collect information about the
hardware configuration of client devices in your organization. To collect hardware
inventory, you must select the Enable hardware inventory on clients setting in client
settings.

After hardware inventory is enabled and the client runs a hardware inventory cycle, the
client sends the information to a management point in the client's site. The
management point then forwards the inventory information to the Configuration
Manager site server, which stores the inventory information in the site database.
Hardware inventory runs on clients according to the schedule that you specify in client
settings.

View hardware inventory
You can use several methods to view the hardware inventory data that Configuration
Manager collects:

      Create queries that return devices that are based on a specific hardware
      configuration.

      Create query-based collections that are based on a specific hardware
      configuration. Query-based collection memberships automatically update on a
      schedule. You can use collections for several tasks, including software deployment.

      Run reports that display specific details about hardware configurations in your
      organization.

      Use Resource Explorer to view detailed information about the hardware inventory
      that's collected from client devices.

When hardware inventory runs on a client device, the first inventory data that the client
returns is always a full inventory. The next set of inventory data contains only delta
inventory information. The site server processes delta inventory information in the order
received. If delta information for a client is missing, the site server rejects more delta
information and directs the client to run a full inventory cycle.

<!-- p.2421 -->

Configuration Manager provides limited support for dual-boot computers.
Configuration Manager can discover dual-boot computers but returns inventory
information only from the OS that's active when the inventory cycle runs.

Extend inventory
To collect more information than what Configuration Manager inventories by default,
you can also use one of these methods to extend hardware inventory:

     Enable, disable, add, and remove inventory classes for hardware inventory from the
     Configuration Manager console.

     Use NOIDMIF files to collect information about client devices that can't be
     inventoried by Configuration Manager. For example, you might want to collect
     device asset number information that exists only as a label on the device. NOIDMIF
     inventory is automatically associated with the client device that it was collected
     from.

     Use IDMIF files to collect information about assets that aren't associated with a
     Configuration Manager client, for example, projectors, photocopiers, and network
     printers.

     Starting in version 2107, you can use the administration service to set custom
     properties on devices. You can then use the custom properties in Configuration
     Manager for reporting or to create collections. For more information, see Custom
     properties for devices.

Next steps
How to configure hardware inventory

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2422 -->

How to extend hardware inventory in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Hardware inventory reads information from Windows PCs by using Windows
Management Instrumentation (WMI). WMI is the Microsoft implementation of web-
based Enterprise Management (WBEM), an industry standard for accessing management
information in an enterprise. In previous versions of Configuration Manager, you
extended hardware inventory by modifying the file sms_def.mof on the site server. This
file contained a list of WMI classes that could be read by hardware inventory. Editing
this file, you could enable and disable existing classes, and also create new classes to
inventory.

The Configuration.mof file is used to define the data classes to be inventoried by
hardware inventory on the client and is unchanged from Configuration Manager 2012.
You can create data classes to inventory existing or custom WMI repository data classes
or registry keys present on client systems.

The Configuration.mof file also defines and registers the WMI providers that access
device information during hardware inventory. Registering providers defines the type of
provider to be used and the classes that the provider supports.

When Configuration Manager clients request policy, the Configuration.mof is attached
to the policy body. This file is then downloaded and compiled by clients. When you add,
modify, or delete data classes from the Configuration.mof file, clients automatically
compile these changes that are made to inventory-related data classes. No further
action is necessary to inventory new or modified data classes on Configuration Manager
clients. This file is located in the Inboxes\clifiles.src\hinv\ folder of the Configuration
Manager installation directory on the primary site server or central administration site
(CAS) server.

In Configuration Manager current branch, you don't edit the sms_def.mof file as with
earlier versions. Instead, make these changes with client settings. Configuration
Manager provides the following methods to extend hardware inventory.

  ７ Note

  If you changed the state of classes in client settings, when you update the site,
  some classes may revert to a default state. For example, if you disable the

<!-- p.2423 -->

  SMS_Windows8Application or SMS_Windows8ApplicationUserInfo classes, they're

  enabled after installing a Configuration Manager update. When you customize
  hardware inventory classes, make sure to review their configuration before and
  after a site update.

  If you've manually changed the Configuration.mof file to add custom inventory
  classes, these changes will be overwritten when you update the site. To keep using
  custom classes after you update, add them to the Added extensions section of the
  Configuration.mof file. Don't modify anything above this section. The other sections
  are reserved for modification by Configuration Manager. The site backs up your
  custom Configuration.mof in the data\hinvarchive\ folder of the Configuration
  Manager installation directory on the site server.

Starting in version 2107, you can use the administration service to set custom properties
on devices. You can then use the custom properties in Configuration Manager for
reporting or to create collections. For more information, see Custom properties for
devices.

Methods

Enable or disable
Enable or disable some of all attributes of a class that already exists on the client. This
action instructs the hardware inventory agent to collect it on clients. You can do this
action in default client settings, or custom device client settings. For more information,
see Enable or disable existing classes.

Add
If a WMI class exists on the client and is known to the site, this action includes it to the
possible set of hardware inventory classes. You can add a new inventory class from the
WMI namespace of another device. This action is only on default client settings. For
more information, see Add a new class.

Extend
Add a new WMI class to the client. To manually extend hardware inventory, edit the
configuration.mof on the top-level site.

<!-- p.2424 -->

If the WMI class doesn't already exist on the client, you need to extend the WMI
schema:

    1. Edit the configuration.mof on the top-level site. Review dataldr.log to see the site
         add it.

    2. Refresh policy on a client, and wait for the new class to compile.

    3. Use default client settings to Add the new class to hardware inventory. You don't
         have to enable this class in default client settings. You can then enable it in a
         custom device client setting.

Import and export
Use the Configuration Manager console to import and export Managed Object Format
(MOF) files that contain inventory classes. For more information, see How to import
classes and How to export classes.

About NOIDMIF files
Use NOIDMIF files to collect information about client devices that Configuration
Manager can't inventory. For example, collect device asset number information that
exists only as a label on the device. NOIDMIF inventory is automatically associated with
the client device that it was collected from. For more information, see Create NOIDMIF
files.

About IDMIF files
Use IDMIF files to collect information about assets in your organization that aren't
associated with a Configuration Manager client. For example, projectors, photocopiers,
and network printers. For more information, see Create IDMIF files.

Procedures
These procedures help you to configure the default client settings for hardware
inventory and they apply to all the clients in your hierarchy. If you want these settings to
apply to only some clients, create a custom client device setting and assign it to a
collection of specific clients. For more information, see How to configure client settings.

Enable or disable existing classes

<!-- p.2425 -->

   1. In the Configuration Manager console, go to the Administration workspace, and
     select the Client Settings node.

   2. Select the Default Client Settings. On the Home tab, in the Properties group,
     choose Properties.

   3. In the Default Client Settings dialog box, choose Hardware Inventory.

   4. In the Device Settings list, select Set Classes.

   5. In the Hardware Inventory Classes dialog box, select or clear the classes and class
     properties to be collected by hardware inventory. You can expand classes to select
     or clear individual properties within that class. Use the Search for inventory classes
     field to search for individual classes.

  ） Important

  When you add new classes to Configuration Manager hardware inventory, the size
  of the inventory file that is collected and sent to the site server will increase. This
  might negatively affect the performance of your network and Configuration
  Manager site. Enable only the inventory classes that you want to collect.

Add a new class
You can only add inventory classes from the hierarchy's top-level server by modifying
the default client settings. This option isn't available when you create custom device
settings.

   1. In the Configuration Manager console, go to the Administration workspace, and
     select the Client Settings node.

   2. Select the Default Client Settings. On the Home tab, in the Properties group,
     choose Properties.

   3. In the Default Client Settings dialog box, choose Hardware Inventory.

   4. In the Device Settings list, choose Set Classes.

   5. In the Hardware Inventory Classes dialog box, choose Add.

   6. In the Add Hardware Inventory Class dialog box, select Connect.

   7. In the Connect to Windows Management Instrumentation (WMI) dialog box,
     specify the name of the computer from which you'll get the WMI classes and the

<!-- p.2426 -->

     WMI namespace to use to get the classes. If you want to get all classes below the
     specified WMI namespace, select Recursive. If the computer you're connecting to
     isn't the local computer, supply credentials for an account that has permission to
     access WMI on the remote computer.

   8. Choose Connect.

   9. In the Add Hardware Inventory Class dialog box, in the Inventory classes list,
     select the WMI classes that you want to add to Configuration Manager hardware
     inventory.

 10. If you want to edit information about the selected WMI class, choose Edit, and in
     the Class qualifiers dialog box, provide the following information:

           Display name: This name will be displayed in Resource Explorer.

           Properties: Specify the units in which each property of the WMI class will be
           displayed.

           You can also set properties as a key property to help uniquely identify each
           instance of the class. If no key is defined for the class, and multiple instances
           of the class are reported from the client, only the latest instance that's found
           is stored in the database.

           When you've finished configuring the properties, select OK to close the Class
           qualifiers dialog box and the other open dialogs.

How to import classes
You can only import inventory classes when you modify the default client settings.
However, you can use custom client settings to import information that doesn't include
a schema change, such as changing the property of an existing class from True to False.

   1. In the Configuration Manager console, go to the Administration workspace, and
     select the Client Settings node.

   2. Select the Default Client Settings. On the Home tab, in the Properties group,
     choose Properties.

   3. In the Default Client Settings dialog box, choose Hardware Inventory.

   4. In the Device Settings list, choose Set Classes.

   5. In the Hardware Inventory Classes dialog box, choose Import.

<!-- p.2427 -->

   6. In the Import dialog box, select the Managed Object Format (MOF) file that you
     want to import, and then choose OK. Review the items that will be imported, and
     then select Import.

How to export classes
   1. In the Configuration Manager console, go to the Administration workspace, and
     select the Client Settings node.

   2. Select the Default Client Settings. On the Home tab, in the Properties group,
     choose Properties.

   3. In the Default Client Settings dialog box, choose Hardware Inventory.

   4. In the Device Settings list, choose Set Classes.

   5. In the Hardware Inventory Classes dialog box, choose Export.

        ７ Note

        When you export classes, all currently selected classes will be exported.

   6. In the Export dialog box, specify the Managed Object Format (MOF) file that you
     want to export the classes to, and then choose Save.

Collect strings larger than 255 characters
You can specify the length of strings to be greater than 255 characters for hardware
inventory properties. This action applies only to newly added classes and for hardware
inventory properties that aren't keys.

   1. In the Administration workspace, select Client Settings. Choose a client device
     setting to edit, then select Properties.

   2. Select Hardware Inventory, then Set Classes, and Add.

   3. Select Connect.

   4. Fill in Computer Name, WMI namespace, select recursive if needed. Provide
     credentials if necessary to connect. Select Connect to view the namespace classes.

   5. Select a new class, then select Edit.

<!-- p.2428 -->

   6. Change the Length of your property that's a string, other than the key, to be
     greater than 255. Select OK.

   7. Make sure that the edited property is selected for Add Hardware Inventory Class,
     and select OK.

Use MIF files
Use Management Information Format (MIF) files to extend hardware inventory
information collected from clients by Configuration Manager. During hardware
inventory, the information stored in MIF files is added to the client inventory report and
stored in the site database, where you can use the data in the same ways that you use
default client inventory data. There are two types of MIF files: NOIDMIF and IDMIF.

  ） Important

  Before you can add information from MIF files to the Configuration Manager
  database, create or import the class. For more information, see Add a new class or
  How to import classes in this article.

Create NOIDMIF files
NOIDMIF files can be used to add information to a client hardware inventory that can't
normally be collected by Configuration Manager and is associated with a particular
client device. For example, many companies label each computer in the organization
with an asset number and then catalog these numbers manually. When you create a
NOIDMIF file, this information can be added to the Configuration Manager database
and be used for queries and reporting.

For more information about creating NOIDMIF files, see About inventory in the
Configuration Manager SDK documentation.

  ） Important

  When you create a NOIDMIF file, save it in an ANSI-encoded format. If you save
  NOIDMIF files in UTF-8 encoded format, Configuration Manager can't read it.

After you create a NOIDMIF file, store it in the %Windir%\CCM\Inventory\noidmifs folder
on each client. Configuration Manager collects information from NODMIF files in this
folder during the next scheduled hardware inventory cycle.

<!-- p.2429 -->

Create IDMIF files
IDMIF files can be used to add information about assets that couldn't normally be
inventoried by Configuration Manager and isn't associated with a particular client
device, to the Configuration Manager database. For example, you could use IDMIFS to
collect information about projectors, DVD players, photocopiers, or other equipment
that doesn't have a Configuration Manager client.

For more information about creating IDMIF files, see About inventory in the
Configuration Manager SDK documentation.

After you create an IDMIF file, store it in the %Windir%\CCM\Inventory\idmifs folder on
client computers. Configuration Manager collects information from this file during the
next scheduled hardware inventory cycle. Declare new classes for information contained
in the file by adding or importing them.

  ７ Note

  MIF files could contain large amounts of data and collecting this data could
  negatively affect the performance of your site. Enable MIF collection only when
  required. Configure the option Maximum custom MIF file size (KB) in the hardware
  inventory settings. For more information, see Introduction to hardware inventory.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2430 -->

How to configure hardware inventory in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This procedure configures the default client settings for hardware inventory and will
apply to all the clients in your hierarchy. If you want these settings to apply to only some
clients, create a custom device client setting and assign it to a collection that contains
the devices that you want to use hardware inventory. See How to configure client
settings.

  ７ Note

  If a client device receives hardware inventory settings from multiple sets of client
  settings, then the hardware inventory classes from each set of settings will be
  merged when the client reports hardware inventory. Additionally, not checking a
  class in a custom client setting with a higher priority doesn't disable the client from
  inventorying that class.

To disable a specific hardware inventory class on a majority of systems except a few, the
class needs to be unchecked in the default client settings. Then create a custom client
setting to enable the class, and deploy it to the target systems.

To configure hardware inventory
   1. In the Configuration Manager console, choose Administration > Client Settings >
      Default Client Settings.

   2. On the Home tab, in the Properties group, choose Properties.

   3. In the Default Settings dialog box, choose Hardware Inventory.

   4. In the Device Settings list, configure the following:

            Enable hardware inventory on clients - Select Yes.

            Hardware inventory schedule - Click Schedule to specify the interval at
            which clients collect hardware inventory.

   5. Configure other hardware inventory client settings that you require.

<!-- p.2431 -->

Client devices will be configured with these settings when they next download client
policy. To initiate policy retrieval for a single client, see How to manage clients.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2432 -->

How to use Resource Explorer to view
hardware inventory in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use Resource Explorer in Configuration Manager to view information about hardware
inventory. The site collects this information from clients in your hierarchy.

   Tip

  Resource Explorer doesn't display any data until a hardware inventory cycle runs on
  the client to which you're connecting.

Overview
Resource Explorer has the following sections related to hardware inventory:

      Hardware: Shows the most recent hardware inventory collected from the specified
      client device.
         The Workstation Status node shows the time and date of the last hardware
         inventory from the device.

      Hardware History: A history of inventoried items that changed since the last
      hardware inventory cycle.
         Expand an item to see a Current node and one or more nodes with the
         historical date. Compare the information in the current node to one of the
         historical nodes to see the items that changed.

  ７ Note

  By default, Configuration Manager deletes hardware inventory data that's been
  inactive for 90 days. Adjust this number of days in the Delete Aged Inventory
  History site maintenance task. For more information, see Maintenance tasks.

How to open Resource Explorer

<!-- p.2433 -->

   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select the Devices node. You can also select any collection in the
     Device Collections node.

   2. Select a device. In the ribbon, on the Home tab and Devices group, click Start, and
     then select Resource Explorer.

   Tip

  In Resource Explorer, right-click an item in the right results pane for additional
  actions. Click Properties to view that item in a different format.

Use of large integer values
In Configuration Manager versions 1802 and prior, hardware inventory has a limit for
integers larger than 4,294,967,296 (2^32). This limit can be reached for attributes such
as hard drive sizes in bytes. The management point doesn't process integer values
above this limit, so no value is stored in the database.

Starting in version 1806, the limit is increased to 18,446,744,073,709,551,616 (2^64).

For a property with a value that doesn't change, like total disk size, you may not
immediately see the value after upgrading the site. Most hardware inventory is a delta
report. The client only sends values that change. To work around this behavior, add
another property to the same class. This action causes the client to update all properties
in the class that changed.

See also
Resource Explorer also shows Software Inventory. For more information, see How to use
Resource Explorer to view software inventory.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2434 -->

Resource Explorer default inventory
classes
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article describes the default inventory classes in Resource Explorer.

These are the default inventory classes:

1394 Controller
Namespace: root\cimv2

class Win32_1394Controller

      (String) DeviceID

      (UInt16) Availability

      (String) Caption

      (UInt32) ConfigManagerErrorCode

      (Boolean) ConfigManagerUserConfig

      (String) Description

      (Boolean) ErrorCleared

      (String) ErrorDescription

      (DateTime) InstallDate

      (UInt32) LastErrorCode

      (String) Manufacturer

      (UInt32) MaxNumberControlled

      (String) Name

      (String) PNPDeviceID

      (UInt16) PowerManagementCapabilities[]

<!-- p.2435 -->

     (Boolean) PowerManagementSupported

     (UInt16) ProtocolSupported

     (String) Status

     (UInt16) StatusInfo

     (String) SystemName

     (DateTime) TimeOfLastReset

Account SID
Namespace: root\cimv2

class Win32_AccountSID

     (String) Element

     (String) Setting

ActiveSync Service
Namespace: root\SmsDm

class SMS_ActiveSyncService

     (UInt32) MajorVersion

     (UInt32) MinorVersion

     (String) LastSyncTime

AMT Agent
Namespace: root\cimv2\sms

class SMS_AMTObject

     (UInt32) DeviceID

     (String) AMT

     (String) AMTApps

<!-- p.2436 -->

     (String) BiosVersion

     (String) BuildNumber

     (String) Flash

     (String) LegacyMode

     (String) Netstack

     (UInt32) ProvisionMode

     (UInt32) ProvisionState

     (String) RecoveryBuildNum

     (String) RecoveryVersion

     (String) Sku

     (UInt32) TLSMode

     (String) VendorID

     (UInt32) ZTCEnabled

AppV Client Application
Namespace: root\AppV

class AppvClientApplication

     (String) ApplicationId

     (String) PackageId

     (String) PackageVersionId

     (Boolean) EnabledForUser

     (Boolean) EnabledGlobally

     (String) Name

     (String) TargetPath

     (String) Version

<!-- p.2437 -->

AppV Client Package
Namespace: root\AppV

class AppvClientPackage

     (String) PackageId

     (String) VersionId

     (String) Assets[]

     (String) DeploymentMachineData

     (String) DeploymentUserData

     (Boolean) HasAssetIntelligence

     (Boolean) InUse

     (Boolean) IsPublishedGlobally

     (Boolean) IsPublishedToUser

     (String) Name

     (UInt64) PackageSize

     (String) Path

     (UInt16) PercentLoaded

     (String) UserConfigurationData

     (String) Version

AutoStart Software
Namespace: root\cimv2\sms

class SMS_AutoStartSoftware

     (String) FilePropertiesHash

     (String) BinFileVersion

     (String) BinProductVersion

<!-- p.2438 -->

    (String) Description

    (String) FileName

    (String) FilePropertiesHashEx

    (String) FileVersion

    (String) Location

    (String) Product

    (String) ProductVersion

    (String) Publisher

    (String) StartupType

    (String) StartupValue

BaseBoard
Namespace: root\cimv2

class Win32_BaseBoard

    (String) Tag

    (String) Caption

    (String) ConfigOptions[]

    (String) Description

    (Boolean) HostingBoard

    (Boolean) HotSwappable

    (DateTime) InstallDate

    (String) Manufacturer

    (String) Model

    (String) Name

    (String) OtherIdentifyingInfo

<!-- p.2439 -->

     (String) PartNumber

     (Boolean) PoweredOn

     (String) Product

     (Boolean) Removable

     (Boolean) Replaceable

     (String) RequirementsDescription

     (Boolean) RequiresDaughterBoard

     (String) SerialNumber

     (String) SKU

     (String) SlotLayout

     (Boolean) SpecialRequirements

     (String) Status

     (String) Version

Battery
Namespace: root\cimv2

class Win32_Battery

     (String) DeviceID

     (UInt16) Availability

     (UInt16) BatteryStatus

     (String) Caption

     (UInt16) Chemistry

     (UInt32) ConfigManagerErrorCode

     (Boolean) ConfigManagerUserConfig

     (String) Description

<!-- p.2440 -->

    (UInt32) DesignCapacity

    (UInt64) DesignVoltage

    (Boolean) ErrorCleared

    (String) ErrorDescription

    (UInt16) EstimatedChargeRemaining

    (UInt32) EstimatedRunTime

    (UInt32) ExpectedLife

    (UInt32) FullChargeCapacity

    (DateTime) InstallDate

    (UInt32) LastErrorCode

    (UInt32) MaxRechargeTime

    (String) Name

    (String) PNPDeviceID

    (UInt16) PowerManagementCapabilities[]

    (Boolean) PowerManagementSupported

    (String) SmartBatteryVersion

    (String) Status

    (UInt16) StatusInfo

    (String) SystemName

    (UInt32) TimeOnBattery

    (UInt32) TimeToFullCharge

BitLocker
Namespace: root\cimv2\security\MicrosoftVolumeEncryption

class Win32_EncryptableVolume
