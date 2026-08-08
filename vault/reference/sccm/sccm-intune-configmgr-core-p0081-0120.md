---
title: "Core infrastructure documentation — pages 81-120"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0081-0120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0081-0120
family: sccm
documentKind: "doc"
abstract: "Enhanced code editor (Introduced in version 2107) Starting in Configuration Manager 2107, you can edit scripts in an enhanced editor. The new editor supports syntax highlighting, code folding, word wrap, line numbers, and find and replace. The new editor is available in the cons"
---

# Core infrastructure documentation — pages 81-120

<!-- p.81 -->

Enhanced code editor
(Introduced in version 2107)

Starting in Configuration Manager 2107, you can edit scripts in an enhanced editor. The
new editor supports syntax highlighting, code folding, word wrap, line numbers, and
find and replace. The new editor is available in the console wherever scripts and queries
can be viewed or edited. The enhanced editor improves the syntax highlighting and
code folding that was first introduced in version 2010.

Open the new code editor to view or edit scripts and queries from the following
locations:

<!-- p.82 -->

     Configuration item
        Scripts
        SQL and WQL queries
        Detection methods
     Application detection scripts
     Query statement properties
     Create script wizard
     Script properties
     Orchestration group
        pre-installation scripts
        post-installation scripts
     Task sequence
        PowerShell scripts
        Query WMI option

The new code editor supports the following features:

     Editor mode with syntax highlighting and plain text toggle
     Toggle word wrap and line numbers
     Code folding
     Language selection
     Find, Find and Replace, and Go To line number
     Font type and size selection
     Zoom using buttons or with Ctrl + mouse wheel.
     The information bar at the bottom displays:
        Number of lines and characters in the script
        Cursor position
        If the script is read-only
     Persistent settings across instances for the code window, such as code folding,
     word wrap, and window size.

Syntax highlighting for scripting languages
(Introduced in version 2010)

To assist you when creating scripts and queries in the Configuration Manager console,
you'll now see syntax highlighting and code folding, where available.

<!-- p.83 -->

                                                                                 

Supported scripting languages for syntax highlighting
Supported languages for syntax highlighting include PowerShell, JavaScript/JScript,
VBScript, and SQL/WQL. The below chart shows which languages are supported for
syntax highlighting in each area of the console:

                                                                        ﾉ   Expand table

 Console area                 PowerShell    VBScript   JavaScript/JScript    SQL/WQL

 Application scripts          Yes           Yes        Yes                   -

 Collection query             -             -          -                     Yes

 Configuration item scripts   Yes           Yes        Yes                   Yes

<!-- p.84 -->

 Console area                  PowerShell    VBScript   JavaScript/JScript    SQL/WQL

 Task sequence scripts         Yes           -          -                     -

 Create scripts                Yes           -          -                     -

Fixed-width font now used in some console areas
(Introduced in version 2010)

Various areas in the Configuration Manager console now use the fixed-width font
Consolas. This font provides consistent spacing and makes it easier to read. You'll see
the Consolas font in the following places:

     Application scripts
     Configuration item scripts
     WMI-based collection membership queries
     CMPivot queries
     Scripts
     Run PowerShell Script
     Run Command Line

<!-- p.85 -->

                                                                                

Shortcuts to status messages
(Introduced in version 2010)

You now have an easier way to view status messages for the following objects:

     Devices
     Users
     Content
     Deployments
        Monitoring workspace
             Phased deployments (select Show Deployments from the Phased
             Deployments node)

<!-- p.86 -->

        Deployments tab in the details pane for:
            Packages
            Task sequences

Select one of these objects in the Configuration Manager console, and then select Show
Status Messages from the ribbon. Set the viewing period, and then the status message
viewer opens. The viewer filters the results to the object you selected.

Your user account needs at least Read permission to these objects.

For more information, see Use the status system.

Improvements to console search
(Introduced in version 2403)

We have added a new Global Search bar where users can search from anywhere in the
console with an option to quickly see and execute the 5 most recent searches. The
default search will now include all workspaces that are when you search to any node in
the console, by default, search results will include items from that workspace as well as
from all nodes folders and subfolders.

Global search view

     Open the console.
     Global Search bar will be visible at the top.
     Enter your string and press enter.
     Search execution will start and you will start seeing the search results.
     Whenever the Search Box is active, you can see a dropdown which contains the
     Recent Searches with a limit of 5.
     Search should work from all across the console be it any child node, parent node
     etc.
     Search should also work when switching from Parent Node to child node.
        Search for any string say "Devices" from any node n1 (Assume n1 is a parent
        node containing other nodes)
        Search for any string say "Computer" from any node n2 (Assume n2 is a child
        node with no node inside it)

<!-- p.87 -->

  ７ Note

  Recent searches dropdown can be collapsed by clicking outside on the window

Note: The path criteria are not editable and they just show the search criteria.

(Introduced in version 2203)

     The default search will now include all subfolders. That is when you navigate to any
     node in the console, by default, search results will include items from that node as
     well as from all subfolders.
     If you want to search only current node, select the Current Node button in the
     ribbon. The search results will then include items from current node only.
     If you want to search all subfolders, select the All Subfolders button in the ribbon.
     The search results will then include items from current node as well as from all
     subfolders.

(Introduced in version 1910)

     You can use the All Subfolders search option from the Driver Packages and
     Queries nodes. Starting in version 2002, also use this option from the
     Configuration Items and Configuration Baselines nodes.

     When a search returns more than 1,000 results, select the OK button on the notice
     bar to view more results.

         Tip

<!-- p.88 -->

        The default limit on search results is 1,000. You can change this default value.
        In the Configuration Manager console, go to the Search tab of the ribbon. In
        the Options group, select Search Settings. Change the Search Results value.
        A larger number of search results might take longer to display.

        By default, the upper maximum limit is 100,000. To change this limit, set the
        DWORD value QueryResultCountMaximum in the following registry key:

        HKEY_CURRENT_USER\Software\Microsoft\ConfigMgr10\AdminUI

        The in-console setting corresponds to the QueryResultCountLimit value in
        the same key. An administrator can configure these values in the HKLM hive
        for all users of the device. The HKCU value overrides the HKLM setting.

Role-based administration for folders
(Introduced in version 1906)

You can set security scopes on folders. If you have access to an object in the folder but
don't have access to the folder, you'll be unable to see the object. Similarly, if you have
access to a folder but not an object within it, you won't see that object. Right-click a
folder, choose Set Security Scopes, then choose the security scopes you want to apply.

Views sort by integer values
We've made improvements to how various views sort data. For example, in the
Deployments node of the Monitoring workspace, the following columns now sort as
numbers instead of string values:

     Number Errors
     Number In Progress
     Number Other
     Number Success
     Number Unknown

Move the warning for a large number of results
When you select a node in the console that returns more than 1,000 results,
Configuration Manager displays the following warning:

  Configuration Manager returned a large number of results. You can narrow your
  results by using search. Or, click here to view a maximum of 100000 results.

<!-- p.89 -->

There's now additional blank space in between this warning and the search field. This
move helps to prevent inadvertently selecting the warning to display more results.

Send feedback
Submit product feedback from the console.

     Send a smile: Send feedback on what you liked

     Send a frown: Send feedback on what you didn't like

     Send a suggestion: Takes you to the product feedback site to share your idea

For more information, see Product Feedback.

Assets and Compliance workspace

Co-management Eligible Devices collection
(Introduced in version 2111)

There's a new built-in device collection for Co-management Eligible Devices. The Co-
management Eligible Devices collection uses incremental updates and a daily full
update to keep the collection up to date.

Collections tab
(Introduced in version 2111)

When you show the members of a device collection, and select a device in the list,
switch to the Collections tab in the details pane. This new view shows the list of
collections of which the selected device is a member. It makes it easier for you to see
this information.

<!-- p.90 -->

Navigate to collection
(Introduced in version 2107)

You can now navigate to a collection from the Collections tab in the Devices node.
Select View Collection from either the ribbon or the right-click menu in the tab.

<!-- p.91 -->

Added maintenance window column
(Introduced in version 2107)

A Maintenance window column was added to the Collections tab in the Devices node.

Display assigned users
(Introduced in version 2107)

If a collection deletion fails due to scope assignment, the assigned users are displayed.

Copy discovery data from the console
(Introduced in version 2010)

Copy discovery data from devices and users in the console. Copy the details to the
clipboard, or export them all to a file. These actions make it easier for you to quickly get
this data from the console. For example, copy the MAC address of a device before you
reimage it.

<!-- p.92 -->

  1. In the Configuration Manager console, go to the Assets and Compliance
    workspace. Open the properties for a user or device.

  2. On the General tab, in the Discovery data list, select one or more properties.

  3. Right-click the selection, and choose one of the following actions:

         Copy value: Copies just the value. You can also use the keyboard shortcut Ctrl
         + C.

         Copy property and value: Copies both the property name and the
         corresponding value. You can also use the keyboard shortcut Ctrl + Shift + C.

         Select all: Selects all properties and values. You can also use the keyboard
         shortcut Ctrl + A.

         Save results as: Saves all properties and values to a comma-separated values
         (CSV) file that you specify.

                                                                           

Real-time actions from device lists

<!-- p.93 -->

(Introduced in version 1906)

There are various ways to display a list of devices under the Devices node in the Assets
and Compliance workspace.

     In the Assets and Compliance workspace, select the Device Collections node.
     Select a device collection, and choose the action to Show members. This action
     opens a subnode of the Devices node with a device list for that collection.
        When you select the collection subnode, you can now start CMPivot from the
        Collection group of the ribbon.

     In the Monitoring workspace, select the Deployments node. Select a deployment,
     and choose the View Status action in the ribbon. In the deployment status pane,
     double-click the total assets to drill-through to a device list.
        When you select a device in this list, you can now start CMPivot and Run Scripts
        from the Device group of the ribbon.

Collections tab in devices node
(Introduced in version 1906)

In the Assets and Compliance workspace, go to the Devices node, and select a device.
In the details pane, switch to the new Collections tab. This tab lists the collections that
include this device.

  ７ Note

  This tab currently isn't available from a devices subnode under the Device
  Collections node. For example, when you select the option to Show Members on a
  collection.

  This tab may not populate as expected for some users. To see the complete list of
  collections a device belongs to, you must have the Full Administrator security role.
  This is a known issue.

Add SMBIOS GUID column to device and device
collection nodes
(Introduced in version 1906)

In both the Devices and Device Collections nodes, you can now add a new column for
SMBIOS GUID. This value is the same as the BIOS GUID property of the System

<!-- p.94 -->

Resource class. It's a unique identifier for the device hardware.

Search device views using MAC address
You can search for a MAC address in a device view of the Configuration Manager
console. This property is useful for OS deployment administrators while troubleshooting
PXE-based deployments. When you view a list of devices, add the MAC Address column
to the view. Use the search field to add the MAC Address search criteria.

View users for a device
The following columns are available in the Devices node:

     Primary user(s)

     Currently logged on user

        ７ Note

        Viewing the currently logged on user requires user discovery and user device
        affinity.

For more information on how to show a non-default column, see How to use the admin
console.

Improvement to device search performance
When searching in a device collection, it doesn't search the keyword against all object
properties. When you're not specific about what to search, it searches across the
following four properties:

     Name
     Primary user(s)
     Currently logged on user
     Last logon user name

This behavior significantly improves the time it takes to search by name, especially in a
large environment. Custom searches by specific criteria are unaffected by this change.

Software Library workspace

<!-- p.95 -->

Folder support for software update nodes
(Introduced in version 2203)

You can organize software update groups and packages by using folders. This change
allows for better categorization and management of software updates. For more
information, see Deploy software updates.

Improvements to console search
(Introduced in version 2107)

You can use the All Subfolders search option for the following nodes:

     Boot Images node
     Operating System Upgrade Packages node
     Operating System Images node

Run software updates evaluation from deployment status
(Introduced in version 2107)

You can right-click and notify devices to run a software updates evaluation cycle from
the software update deployment status. You can target a single device under the Asset
Details pane or select a group of devices based on their deployment status.

<!-- p.96 -->

   1. In the Configuration Manager console, navigate to Monitoring > Overview >
     Deployments.
   2. Select the software update group or software update for which you want to
     monitor the deployment status.
   3. On the Home tab, in the Deployment group, select View Status.
   4. Right-click on either a specific deployment status for the devices, or on a single
     device under Asset Details pane.
   5. Select Evaluate Software Update Deployments to send a notification to the
     selected devices to run an evaluation cycle for software update deployments.

Import objects to current folder
(Introduced in version 2010)

When you import an object in the Configuration Manager console, it now imports to the
current folder. Previously, Configuration Manager always put imported objects in the
root node. This new behavior applies to applications, packages, driver packages, and
task sequences.

See task sequence size in the console
(Introduced in version 2010)

When you view the list of task sequences in the Configuration Manager console, add the
Size (KB) column. Use this column to identify large task sequences that can cause
problems. For more information, see Reduce the size of task sequence policy.

Order by program name in task sequence
(Introduced in version 1906)

In the Software Library workspace, expand Operating Systems, and select the Task
Sequences node. Edit a task sequence, and select or add the Install Package step. If a
package has more than one program, the drop-down list now sorts the programs
alphabetically.

Task sequences tab in applications node
(Introduced in version 1906)

In the Software Library workspace, expand Application Management, go to the
Applications node, and select an application. In the details pane, switch to the new Task

<!-- p.97 -->

sequences tab. This tab lists the task sequences that reference this application.

Drill through required updates
(Introduced in version 1906)

   1. Go to one of the following places in the Configuration Manager console:

           Software Library > Software Updates > All Software Updates
           Software Library > Windows Servicing > All Windows Updates
           Software Library > Office 365 Client Management > Office 365 Updates

   2. Select any update that is required by at least one device.

   3. Look at the Summary tab and find the pie chart under Statistics.

   4. Select the View Required hyperlink next to the pie chart to drill down into the
     device list.

   5. This action takes you to a temporary node under Devices where you can see the
     devices requiring the update. You can also take actions for the node such as
     creating a new collection from the list.

  ７ Note

  Starting on April 21, 2020, Office 365 ProPlus is being renamed to Microsoft 365
  Apps for enterprise. For more information, see Name change for Office 365
  ProPlus. You may still see references to the old name in the Configuration Manager
  console and supporting documentation while the console is being updated.

Maximize the browse registry window
   1. In the Software Library workspace, expand Application Management, and select
     the Applications node.
   2. Select an application that has a deployment type with a detection method. For
     example, a Windows Installer detection method.
   3. In the details pane, switch to the Deployment Types tab.
   4. Open the properties of a deployment type, and switch to the Detection Method
     tab. Select Add Clause.
   5. Change the Setting Type to Registry and select Browse to open the Browse
     Registry window. You can now maximize this window.

<!-- p.98 -->

Edit a task sequence by default
In the Software Library workspace, expand Operating Systems, and select the Task
Sequences node. Edit is now the default action when opening a task sequence.
Previously the default action was Properties.

Go to the collection from an application deployment
   1. In the Software Library workspace, expand Application Management, and select
     the Applications node.
   2. Select an application. In the details pane, switch to the Deployments tab.
   3. Select a deployment, and then choose the new Collection option in the ribbon on
     the Deployment tab. This action switches the view to the collection that's the
     target of the deployment.

           This action is also available from the right-click context menu on the
           deployment in this view.

Monitoring workspace

Collection evaluation time
(Introduced in version 2111)

When viewing a collection, you could previously see the amount of time the site took to
evaluate the collection membership. This data is now also available in the Monitoring
workspace. When you select a collection in either subnode of the Collection Evaluation
node, the details pane displays this collection evaluation time data.

Correct names for client operations

<!-- p.99 -->

(Introduced in version 1906)

In the Monitoring workspace, select Client Operations. The operation to Switch to next
Software Update Point is now properly named.

Show collection name for scripts
(Introduced in version 1906)

In the Monitoring workspace, select the Script Status node. It now lists the Collection
Name and the ID.

Remove content from monitoring status
   1. In the Monitoring workspace, expand Distribution Status, and select Content
     Status.
   2. Select an item in the list, and choose the View Status option in the ribbon.
   3. In the Asset Details pane, right-click a distribution point, and select the new option
     Remove. This action removes this content from the selected distribution point.

Copy details in monitoring views
Copy information from the Asset Details pane for the following monitoring nodes:

     Content Distribution Status

     Deployment Status

<!-- p.100 -->

Administration workspace

Status message shortcuts
(Introduced in version 2107)

Shortcuts to status messages were added to the Administrative Users node and the
Accounts node. Select an account, then select Show Status Messages.

Enable some security nodes to use the administration
service
Starting in version 1906, you can enable some nodes under the Security node to use the
administration service. This change allows the console to communicate with the SMS
Provider over HTTPS instead of via WMI. For more information, see Set up the
administration service.

Next steps
     Use the console
     Console notifications
     Accessibility features

<!-- p.101 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.102 -->

Fundamentals of Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If you're new to Configuration Manager current branch, start with the fundamentals.
Before you run setup to install your first site, learn about the basic concepts of
Configuration Manager. If you're already familiar with System Center 2012 Configuration
Manager, then start with What's changed from System Center 2012 Configuration
Manager.

For information about supported operating systems and supported environments,
hardware requirements, and capacity information, see Supported configurations for
Configuration Manager.

See the following articles to learn about fundamental concepts for Configuration
Manager:

      Fundamentals of sites and hierarchies

      About upgrade, update, and install

      Fundamentals of managing devices

      Fundamentals of client management tasks

      Fundamentals of security

      Fundamentals of role-based administration

      Fundamentals of content management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.103 -->

Fundamentals of sites and hierarchies
for Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

A Configuration Manager deployment must be installed in an Active Directory domain.
The foundation of this deployment includes one or more Configuration Manager sites
that form a hierarchy of sites. From a single site to a multi-site hierarchy, the type and
location of sites you install provide the ability to scale up (expand) your deployment
when necessary, and deliver key services to managed users and devices.

Hierarchies of sites
When you install Configuration Manager for the first time, the first Configuration
Manager site that you install determines the scope of your hierarchy. The first
Configuration Manager site is the foundation from which you will manage devices and
users in your enterprise. This first site must be either a central administration site or a
stand-alone primary site.

A central administration site is suitable for large-scale deployments, provides a central
point of administration, and provides the flexibility to support devices that are
distributed across a global network infrastructure. After you install a central
administration site, you will need to install one or more primary sites as child sites. This
configuration is necessary because a central administration site does not directly
support management of devices, which is the function of a primary site. A central
administration site supports multiple child-primary sites. The child-primary sites are
used to directly manage devices, and to control network bandwidth when your
managed devices are in different geographical locations.

A stand-alone primary site is suitable for smaller deployments, and can be used to
manage devices without having to install additional sites. Although a stand-alone
primary site can limit the size of your deployment, it does support a scenario to expand
your hierarchy at a later time by installing a new central administration site. With this
site expansion scenario, your stand-alone primary site becomes a child-primary site, and
you can then install additional child-primary sites below your new central administration
site. You can then expand your initial deployment for future growth of your enterprise.

   Tip

<!-- p.104 -->

  A stand-alone primary site and a child-primary site are really the same type of site:
  a primary site. The difference in name is based on the hierarchy relationship that is
  created when you also use a central administration site. This hierarchy relationship
  can also limit the installation of certain site system roles that extend Configuration
  Manager functionality. This limitation of roles occurs because certain site system
  roles can only be installed on the top-tier site of the hierarchy, a central
  administration site, or a stand-alone primary site.

After you install your first site, you can install additional sites. If your first site was a
central administration site, then you can install one or more child-primary sites. After
you install a primary site (stand-alone, or child-primary), you can then install one or
more secondary sites.

A secondary site can only be installed as a child site below a primary site. This site type
extends the reach of a primary site to manage devices in locations that have a slow
network connection to the primary site. Even though a secondary site extends the
primary site, the primary site manages all of the clients. The secondary site provides
support for devices in the remote location. It provides support by compressing and then
managing the transfer of information across your network that you send (deploy) to
clients, and that clients send back to the site.

The following diagrams show some example site designs.

<!-- p.105 -->

For more information, see the following topics:

     Introduction to Configuration Manager

     Design a hierarchy of sites for Configuration Manager

     Install Configuration Manager sites

Site system servers and site system roles
Each Configuration Manager site installs site system roles that support management
operations. The following roles are installed by default when you install a site:

     The site server role is assigned to the computer where you install the site.

     The site database server role is assigned to the SQL Server that hosts the site
     database.

Other site system roles are optional, and are only used when you want to use the
functionality that is active in a site system role. Any computer that hosts a site system
role is referred to as a site system server.

<!-- p.106 -->

For a smaller deployment of Configuration Manager, you might initially run all of your
site system roles directly on the site server computer. Then, as your managed
environment and needs grow, you can install additional site system servers to host
additional site system roles to improve the site's efficiency in providing services to more
devices.

For information about the different site system roles, see Site system roles in Plan for
site system servers and site system roles for Configuration Manager.

Publishing site information to Active Directory
Domain Services
To simplify management of Configuration Manager, you can extend the Active Directory
schema to support details that are used by Configuration Manager, and then have sites
publish their key information to Active Directory Domain Services (AD DS). Then the
computers that you want to manage can securely retrieve site-related information from
the trusted source of AD DS. The information clients can retrieve identifies available
sites, site system servers, and the services that those site system servers provide.

Extending the Active Directory schema is done only one time for each forest, and can be
done before or after you install Configuration Manager. When you extend the schema,
you must create a new Active Directory container named System Management in each
domain. The container contains a Configuration Manager site that will publish data for
clients to find. For more information, see Prepare Active Directory for site publishing.

Publishing site data improves the security of your Configuration Manager hierarchy and
reduces administrative overhead, but is not required for basic Configuration Manager
functionality.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.107 -->

About upgrade, update, and install for
site and hierarchy infrastructure
Article • 01/12/2024

Applies to: Configuration Manager (current branch)

When managing Configuration Manager sites and hierarchy infrastructure, the terms
upgrade, update, and install are used to describe three separate concepts.

Upgrade
Upgrade or in-place upgrade, is used when converting your Configuration Manager 2012
site or hierarchy to one that runs Configuration Manager current branch.

When you upgrade System Center 2012 Configuration Manager to Configuration
Manager current branch, you continue to use the same servers to host your sites and
site servers, and you retain your existing data and configurations for Configuration
Manager. This is different from Migration which is a way to retain your configurations
and data about managed devices while using new Configuration Manager current
branch sites installed to new hardware.

For more information, see Upgrade to Configuration Manager.

Update
Update is used for installing in-console updates for Configuration Manager, and for out-
of-band updates which are updates that can't be delivered from within the
Configuration Manager console. In-console updates can modify the version of your
Current Branch site (or Technical Preview site) so that it runs a higher version. For
example, if your site runs version 1806, you can install an update for version 1810.
Updates can also install fixes for a known issue, without modifying the site version.

Typically, updates add security fixes, quality improvements, and new features to your
existing deployment. If you use the Technical Preview branch, an update can install a
newer version of the Technical Preview.

      You choose when to install the in-console update, starting at the top-tier site of
      your hierarchy.
      You can install any update that is available from within the console. For example, if
      your site runs version 1802 and both 1806 and 1810 are offered, you should

<!-- p.108 -->

     consider installing version 1810 because each version includes the features that
     were first made available in previously released versions.
     After a new update completes installation at your top-tier site, child primary sites
     automatically start the process to update. However, you can set Service Windows
     to control the timing of updates.
     Secondary sites don't automatically install updates. Instead, you manually start the
     update from within the Configuration Manager console.

For more, see Updates for Configuration Manager, and Technical Preview for
Configuration Manager.

Install
Install is used when creating a new Configuration Manager hierarchy from scratch, or
adding more sites to an existing hierarchy.

When you install a new primary site or central administration site, the location of
setup.exe and its related source files that you use depend on your installation scenario.

For more, see Prepare to install sites.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.109 -->

Fundamentals of managing devices with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager can manage two broad categories of devices:

      Clients are devices like workstations, laptops, servers, and mobile devices where
      you install the Configuration Manager client software. Some management
      functions, like hardware inventory, require this client software.

      Managed devices can include clients, but typically it's a mobile device where the
      Configuration Manager client software isn't installed. On this kind of device, you
      manage by using the built-in on-premises mobile device management in
      Configuration Manager.

You can also group and identify devices based on the user, not just the client type.

Managing devices with the Configuration
Manager client
There are two ways to use the Configuration Manager client software to manage a
device. The first way is to discover the device on your network, and then deploy the
client software to that device. The other way is to manually install the client software on
a new computer, and then have that computer join your site when it joins your network.
To discover devices where the client software is not installed, run one or more of the
built-in discovery methods. After a device is discovered, use one of several methods to
install the client software. For information on using discovery, see Run discovery for
Configuration Manager.

After discovering the devices that are supported to run the Configuration Manager
client software, you can use one of several methods to install the software. After the
software is installed and the client is assigned to a primary site, you can begin to
manage the device. Common installation methods include:

      Client push installation

      Software update-based installation

      Group policy

<!-- p.110 -->

     Manual installation on a computer

     Including the client as part of an OS image that you deploy

After the client is installed, you can simplify the tasks of managing devices by using
collections. Collections are groups of devices or users that you create so that you can
manage them as a group. For example, you might want to install a mobile device
application on all mobile devices that Configuration Manager enrolls. If this is the case,
you can use the All Mobile Devices collection.

For more information, see these articles:

     Choose a device management solution

     Client installation methods

     Introduction to collections

Client settings
When you first install Configuration Manager, all clients in the hierarchy are configured
by using the default client settings that you can change. The client settings include these
configuration options:

     How frequently the devices communicate with the site.

     Whether the client is set up for software updates and other management
     operations.

     Whether users can enroll their mobile devices so they're managed by
     Configuration Manager.

You can create custom client settings and then assign them to collections. Members of
the collection are configured to have the custom settings, and you can create multiple
custom client settings that are applied in the order that you specify (by numerical order).
If there are conflicting settings, the setting that has the lowest order number overrides
the other settings.

The following diagram shows an example of how you create and apply custom client
settings.

<!-- p.111 -->

To learn more about client settings, see the following articles:

     How to configure client settings
     About client settings

Managing devices without the Configuration
Manager client
Configuration Manager supports the management of some devices that have not
installed the client software, and aren't managed by Intune. For more information, see
Manage mobile devices with on-premises infrastructure in Configuration Manager and
Manage mobile devices with Configuration Manager and Exchange.

User-based management
Configuration Manager supports collections of Microsoft Entra ID and Active Directory
Domain Services users. When you use a user collection, you can install software on all
computers that members of the collection use. To make sure that the software you

<!-- p.112 -->

deploy only installs on the devices that are specified as a user's primary device, set up
user device affinity. A user can have one or more primary devices.

One of the ways that users can control their software deployment experience is to use
the Software Center client interface. The Software Center is automatically installed on
client computers and is run from the Windows Start menu. The Software Center lets
users manage their own software and do the following tasks:

     Install software

     Schedule software to automatically install outside working hours

     Configure when Configuration Manager can install software on a device

     Configure the access settings for remote control, if remote control is set up in
     Configuration Manager

     Configure options for power management, if an administrator sets up this option

     Browse for, install, and request software

     Configure preference settings

     When it's set up, specify a primary device for user device affinity

For more information, see the following articles:

     Plan for Software Center
     Link users and devices with user device affinity
     Software Center user guide

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.113 -->

Fundamentals of client management
tasks for Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you install the Configuration Manager clients, there are several tasks that you run
to manage the clients. Some of the tasks are run from the Configuration Manager
console. Other tasks are run from the Configuration Manager client application. The
Configuration Manager client application is installed with the Configuration Manager
client software.

Configuration Manager console tasks
In the Configuration Manager console, you can perform various client management
tasks:

      Deploy applications, software updates, maintenance scripts, and operating
      systems. Configure installation for a specific date and time, make the software
      available for users to install when they are requested, or configure applications to
      be uninstalled.

      Help protect computers from malware and security threats, and notify you when
      problems are detected.

      Define client configuration settings that you want to monitor, and remediate if
      they are out of compliance.

      Collect hardware and software inventory information, which includes monitoring
      and reconciling license information from Microsoft.

      Troubleshoot computers by using remote control.

      Implement power management settings to manage and monitor the power
      consumption of computers.

The Configuration Manager console monitors the previous tasks in near real time.
Notification and status information for each task is available in the Configuration
Manager console. To capture data and historical trending, use the integrated reporting
capabilities of SQL Server Reporting Services. Clients submit details to the site as client
status. Client status information provides data about the health of the client and client

<!-- p.114 -->

activity, and is viewed in the console or by using the built-in reports for Configuration
Manager. This data helps identify computers that are not responding and in some cases,
problems are automatically remediated.

For more information about management tasks for clients, see How to manage clients.
To learn about using reports, see Introduction to reporting.

Configuration Manager client application
When you install the Configuration Manager client software, the Configuration Manager
client application is installed too. Unlike Software Center, the Configuration Manager
client application is designed for the help desk rather than for the end user. Some
configuration options require local administrative permissions, and most options require
technical knowledge about how the Configuration Manager client application works.
You can use this application to perform the following tasks on a client:

     View properties about the client, such as the build number, its assigned site, the
     management point it is communicating with, and whether the client is using a
     public key infrastructure (PKI) certificate or a self-signed certificate.

     Confirm that the client has successfully downloaded a client policy after the client
     is installed for the first time. Also confirm that the client settings are enabled or
     disabled as expected, according to the client settings that are configured in the
     Configuration Manager console.

     Start client actions. For example, download the client policy if there was a recent
     configuration change in the Configuration Manager console, and you do not want
     to wait until the next scheduled time.

     Manually assign a client to a Configuration Manager site or try to find a site. Then
     specify the Domain Name System (DNS) suffix for management points that publish
     to DNS.

     Configure the client cache that temporarily stores files. Then delete files in the
     cache if you require more disk space to install software.

     Configure settings for Internet-based client management.

     View configuration baselines that were deployed to the client, initiate compliance
     evaluation, and view compliance reports.

Feedback

<!-- p.115 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.116 -->

Fundamentals of security for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article summarizes the following fundamental security components of any
Configuration Manager environment:

      Security layers
      Role-based administration
      Securing client endpoints
      Configuration Manager accounts and groups
      Privacy

Security layers
Security for Configuration Manager consists of the following layers:

      Windows OS and network security
      Network infrastructure: firewalls, intrusion detection, public key infrastructure (PKI)
      Configuration Manager security controls
      SMS Provider
      Site database permissions

Windows OS and network security
The first layer is provided by Windows security features for both the OS and the
network. This layer includes the following components:

      File sharing to transfer files between Configuration Manager components.

      Access Control Lists (ACLs) to help secure files and registry keys.

      Internet Protocol Security (IPsec) to help secure communications.

      Group policy to set security policy.

      Distributed Component Object Model (DCOM) permissions for distributed
      applications, like the Configuration Manager console.

      Active Directory Domain Services to store security principals.

<!-- p.117 -->

     Windows account security, including some groups that Configuration Manager
     creates during setup.

Network infrastructure
Network security components, like firewalls and intrusion detection, help provide
defense for the whole environment. Certificates issued by industry standard public key
infrastructure (PKI) implementations help provide authentication, signing, and
encryption.

Configuration Manager security controls
By default, only local administrators have rights to the files and registry keys that the
Configuration Manager console requires on computers where you install it.

SMS Provider
The next layer of security is based on access to the SMS Provider. The SMS Provider is a
Configuration Manager component that grants a user access to query the site database
for information. The SMS Provider primarily exposes access through Windows
Management Instrumentation (WMI), but also a REST API called the administration
service.

By default, access to the provider is restricted to members of the local SMS Admins
group. This group at first contains only the user who installed Configuration Manager.
To grant other accounts permission to the Common Information Model (CIM) repository
and the SMS Provider, add the other accounts to the SMS Admins group.

You can specify the minimum authentication level for administrators to access
Configuration Manager sites. This feature enforces administrators to sign in to Windows
with the required level. For more information, see Plan for the SMS Provider.

Site database permissions
The final layer of security is based on permissions to objects in the site database. By
default, the Local System account and the user account that you used to install
Configuration Manager can administer all objects in the site database. Grant and restrict
permissions to other administrative users in the Configuration Manager console by
using role-based administration.

<!-- p.118 -->

Role-based administration
Configuration Manager uses role-based administration to help secure objects like
collections, deployments, and sites. This administration model centrally defines and
manages hierarchy-wide security access settings for all sites and site settings.

An administrator assigns security roles to administrative users and group permissions.
The permissions are connected to different Configuration Manager object types, for
example, to create or change client settings.

Security scopes include specific instances of objects that an administrative user is
responsible to manage. For example, an application that installs the Configuration
Manager console.

The combination of security roles, security scopes, and collections define the objects
that an administrative user can view and manage. Configuration Manager installs some
default security roles for typical management tasks. Create your own security roles to
support your specific business requirements.

For more information, see Fundamentals of role-based administration.

Securing client endpoints
Configuration Manager secures client communication to site system roles by using
either self-signed or PKI certificates, or Microsoft Entra tokens. Some scenarios require
the use of PKI certificates. For example, internet-based client management, and for
mobile device clients.

You can configure the site system roles to which clients connect for either HTTPS or
HTTP client communication. Client computers always communicate by using the most
secure method that's available. Client computers only fall back to using the less secure
communication method if you have site systems roles that allow HTTP communication.

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP client
  communication are deprecated. Configure the site for HTTPS or Enhanced HTTP.
  For more information, see Enable the site for HTTPS-only or enhanced HTTP.

For more information, see Plan for security.

<!-- p.119 -->

Configuration Manager accounts and groups
Configuration Manager uses the Local System account for most site operations. Some
site operations allow the use of a service account, instead of using the domain computer
account of the site server. Some management tasks might require you to create and
maintain other accounts. For example, to join the domain during an OS deployment task
sequence.

Configuration Manager creates several default groups and SQL Server roles during
setup. You might have to manually add computer or user accounts to the default groups
and SQL Server roles.

For more information, see Accounts used in Configuration Manager.

Privacy
Before you implement Configuration Manager, consider your privacy requirements.
Although enterprise management products offer many advantages because they can
effectively manage lots of clients, this software might affect the privacy of users in your
organization. Configuration Manager includes many tools to collect data and monitor
devices. Some tools might raise privacy concerns in your organization.

For example, when you install the Configuration Manager client, it enables many
management settings by default. This configuration causes the client software to send
information to the Configuration Manager site. The site stores client information in the
site database. The client information isn't directly sent to Microsoft. For more
information, see Diagnostics and usage data.

Next steps
Fundamentals of role-based administration

Plan for security

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.120 -->

Fundamentals of role-based
administration for Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

With Configuration Manager, you use role-based administration to secure the access
that administrative users need to use Configuration Manager. You also secure access to
the objects that you manage, like collections, deployments, and sites.

The role-based administration model centrally defines and manages hierarchy-wide
security access. This model is for all sites and site settings by using the following items:

      Security roles are assigned to administrative users to give them permission to
      Configuration Manager objects. For example, permission to create or change client
      settings.

      Security scopes are used to group specific instances of objects that an
      administrative user is responsible to manage. For example, an application that
      installs the Configuration Manager console.

      Collections are used to specify groups of users and devices that the administrative
      user can manage in Configuration Manager.

With the combination of roles, scopes, and collections, you segregate the administrative
assignments that meet your organization's requirements. Used together, they define the
administrative scope of a user. This administrative scope controls the objects that an
administrative user views in the Configuration Manager console, and it controls the
permissions that a user has on those objects.

Benefits
The following items are benefits of role-based administration in Configuration Manager:

      Sites aren't used as administrative boundaries. In other words, don't expand a
      standalone primary site to a hierarchy with a central administration site to separate
      administrative users.

      You create administrative users for a hierarchy and only need to assign security to
      them one time.
