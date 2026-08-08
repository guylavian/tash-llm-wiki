---
title: "Configuration Manager SDK documentation — pages 201-240"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0201-0240
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0201-0240
family: sccm
documentKind: "doc"
abstract: "For more information about using client objects with WMI or managed code, see About client WMI programming. Classes For more information about the classes that Configuration Manager supports, see Configuration Manager Reference. See Also Configuration Manager Schema View Mapping"
---

# Configuration Manager SDK documentation — pages 201-240

<!-- p.201 -->

For more information about using client objects with WMI or managed code, see About
client WMI programming.

Classes
For more information about the classes that Configuration Manager supports, see
Configuration Manager Reference.

See Also
Configuration Manager Schema View Mapping
Configuration Manager Schema SQL Views
Configuration Manager SQL View Security

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.202 -->

Configuration Manager Schema SQL
Views
Article • 10/10/2022

In Configuration Manager, a number of schema information views are created to get
information about the names of all the available views and the schema for the inventory
and discovery classes. These are particularly useful for determining the names for
custom inventory resource type (architecture) tables. The following table shows a list of
these schema information views.

                                                                                ﾉ   Expand table

 View                     Description                           Sample Query

 v_SchemaViews            Lists all the views in the view       Select ViewName, Type from
                          schema family.                        v_SchemaViews order by
                                                                ViewName

 v_ResourceMap            Lists the resource type views.        select * from v_ResourceMap

 v_ResourceAttributeMap   Lists attributes for each resource    select * from
                          type.                                 v_ResourceAttributeMap

 v_GroupMap               Lists inventory groups for each       select * from v_GroupMap
                          inventory architecture.

 v_GroupAttributeMap      Lists attributes for each inventory   select * from
                          group.                                v_GroupAttributeMap

 v_ReportViewSchema       Parallel to the                       select * from
                          SMS_ReportViewSchema class, this      v_ReportViewSchema
                          view lists all the classes and
                          properties.

For more information about how the SQL views map to their WMI class equivalents, see
Configuration Manager Schema View Mapping

See Also
Configuration Manager Schema Overview
Configuration Manager Schema View Mapping
Configuration Manager SQL View Security

<!-- p.203 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.204 -->

Configuration Manager Schema View
Mapping
Article • 10/10/2022

In Configuration Manager, the names of views and columns are designed to be as close
to the SMS Provider Windows Management Instrumentation (WMI) schema as possible.
Because the views names and view column names must be valid SQL Server identifiers,
there are some discrepancies between WMI and SQL Server names. However, in most
cases the following rules can be applied to convert a WMI class name to its
corresponding SQL Server view:

      Replace SMS_ with v_ for the start of the view name.

      If a view name is longer than 30 characters, it's truncated.

      WMI property names are the same in the SQL Server views for non-inventory or
      discovery classes.

      Beyond this, the following class families have a differing nomenclature for their
      view equivalents:

System Inventory Views
The syntax for the current inventory group is v_GS_<group name> (for example,
v_GS_Tape_Drive).

The syntax for the history inventory group is v_HS_<group name>(for example,
v_HS_Tape_Drive).

  ７ Note

  There is no equivalent Extended History view (WMI class SMS_GEH_System_<group
  name>) because it is implemented as a stored procedure.

Custom Architecture Views
The syntax for the current groups is v_G<resource type number>_<group name> (for
example, v_G6_VendorData).

<!-- p.205 -->

In the previous example, it's assumed that a new inventory architecture, for example
VendingMachine, has been added to the system and assigned the resource type number
6 and VendorData is an inventory group that is associated with the architecture. The
resource type number might be related to the resource type name and its group's
classes using the schema information views.

The corresponding history inventory classes will use the suffix H in place of G.

Discovery Views
The views for discovery data differ from their WMI counterparts in that array properties
in WMI are represented as separate views. For example, for the System resource, all the
scalar properties are contained in the view v_R_System. There are many view tables for
the array values, such as v_RA_System_IPAddresses and v_RA_System_MACAddresses.
The general rules for the syntax of these views are:

     Scalar class: v_R_<resource type name>

     Array class: v_RA<architecture name>\<group name>

     Each array property view has just two columns: ResourceID and a column that
     contains the actual data. For example, for the view v_RA_System_IPAddresses the
     data column is v_RA_System_IPAddresses. As with inventory groups for the
     discovery view, column names differ from those of WMI classes. Each column ends
     with a zero character, ensuring uniqueness with SQL Server reserved words. In
     general, this is the only difference between the WMI and view column names
     although there are exceptions.

     For more information about the classes that Configuration Manager supports, see
     Configuration Manager Reference.

See Also
Configuration Manager Schema Overview
Configuration Manager Schema SQL Views
Configuration Manager SQL View Security

Feedback
Was this page helpful?    Yes    No

<!-- p.206 -->

Provide product feedback

<!-- p.207 -->

Configuration Manager SQL View
Security
Article • 01/05/2024

The Configuration Manager object security mechanism, implemented in the SMS
Provider, facilitates instance (or row) level security on core object classes. By using the
Configuration Manager schema views, an application or user is operating outside of this
security mechanism. This doesn't mean that the views can't be secured from
unauthorized data access; however, security must be configured separately and is less
precise than standard Configuration Manager object security. You can give a user read-
only permission to access only the views and deny access to any internal Configuration
Manager tables. The main security functionality that is lost in the view approach is the
ability to secure specific object instances (such as packages and collections) separately
for members of groups.

See Also
Configuration Manager Schema View Mapping
Configuration Manager Schema SQL Views

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.208 -->

How to See a Configuration Manager
View by Using SQL Server
Article • 10/10/2022

The following examples demonstrate various Microsoft Configuration Manager SQL view
queries.

Examples

To determine the display name of a resource type from the
resource type number

      In SQL Server, query the Configuration Manager database with the following SQL
      statement:

  select DisplayName from v_ResourceMap where ResourceType=5

To determine discovery properties for a particular resource type
      In SQL Server, query the Configuration Manager database with the following SQL
      statement:

  select * from v_ResourceAttributeMap where ResourceType=5

To list the inventory groups for a particular resource type

      In SQL Server, query the Configuration Manager database with the following SQL
      statement:

  select InvClassName from v_GroupMap where ResourceType = 5

<!-- p.209 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.210 -->

Creating custom reports by using SQL
Server views in Configuration Manager
Article • 10/04/2022

Configuration Manager queries SQL Server views in the Configuration Manager site
database to retrieve the information that is displayed in reports. The Configuration
Manager site database contains a large collection of information about the network,
computers, users, user groups, and many other components of the computing
environment. The database also contains objects that represent Configuration Manager
operations, such as deployments, software updates, configuration baselines, reports,
and status messages. Configuration Manager administrators need to understand the
different categories of the SQL views, what information is stored in each view, and how
the SQL views can be joined to one another to create reports that return the required
information. Because Configuration Manager queries and collections retrieve
information from Windows Management Instrumentation (WMI) instead of
Configuration Manager SQL views, it is also helpful to know how the SQL view schema is
related to the WMI schema.

This documentation assumes that you have a basic understanding of
Configuration Manager and SQL statements, that you have a working
Configuration Manager infrastructure in place, and that you have a basic understanding
of Configuration Manager reports. For more information about creating reports in
Configuration Manager, see Introduction to reporting. For more information about how
to write basic SQL statements, see your SQL Server documentation.

This documentation includes an overview of the Configuration Manager SQL view
schema and SQL views, an overview of the existing reports and associated reporting
procedures, sample SQL statements for each Configuration Manager SQL view category,
exercises for creating custom reports, an overview for writing report SQL statements,
and an overview of the Configuration Manager Provider WMI schema.

Product versions used in this document
This document was created using Microsoft SQL Server 2012, Report Builder 3.0 and
Configuration Manager. The available SQL views, options, and commands might vary
depending on the version of each product you are using. For more information, see the
documentation for the products you are using.

<!-- p.211 -->

What's new for reporting in Configuration
Manager
This section lists the changes that have been made since Configuration Manager 2007
for Configuration Manager reporting.

     Configuration Manager no longer uses the reporting point; the reporting services
     point is the only site system role that Configuration Manager now uses for
     reporting.

     Full integration of the Configuration Manager 2007 R2 SQL Server Reporting
     Services solution: In addition to standard report management, Configuration
     Manager 2007 R2 introduced support for SQL Server Reporting Services reporting.
     Configuration Manager integrates the Reporting Services solution, adds new
     functionality, and removes standard report management as a reporting solution.

     Report Builder 2.0 integration: Configuration Manager uses Microsoft SQL
     Server 2008 Reporting Services Report Builder 2.0 as the exclusive authoring and
     editing tool for both model-based and SQL-based reports. Report Builder 2.0 is
     automatically installed when you create or modify a report for the first time.

     Report subscriptions in SQL Server Reporting Services let you configure the
     automatic delivery of specified reports by email or to a file share in scheduled
     intervals.

     You can run Configuration Manager reports in the Configuration Manager console
     by using Report Viewer, or you can run reports from a browser by using Report
     Manager. Both methods for running reports provide a similar experience.

     Reports in Configuration Manager are rendered in the locale of the installed
     Configuration Manager console. Subscriptions are rendered in the locale that SQL
     Server Reporting Services is installed. When you author a report, you can specify
     the assembly and expression.

     When Microsoft SQL Server 2012 or SQL Server 2008 R2 runs on the Reporting
     Services point, Configuration Manager opens Reporting Services Report Builder 3.0
     when you create or modify reports. When Microsoft SQL Server 2008 runs on the
     Reporting Services point, Configuration Manager opens Reporting Services Report
     Builder 2.0 when you create or modify reports.

     The Monitoring workspace in the Configuration Manager console now displays
     links to SQL Server Reporting Services Report Manager from the Reporting node.

<!-- p.212 -->

     Configuration Manager reports are now fully enabled for role-based
     administration. The data for all reports included with Configuration Manager is
     filtered based on the permissions of the administrative user who runs the report.
     Administrative users with specific roles can only view information defined for their
     roles. For more information, see the Planning for Role-Based Administration for
     Reports section in the Planning for Reporting in Configuration Manager article in
     the Configuration Manager Documentation Library.

In this section
     SQL Server views in Configuration Manager
     Provides an overview of the views you can use to create reports in Configuration
     Manager.

     Working with reports in Configuration Manager
     Provides an overview of Configuration Manager reports, the elements of a report
     and procedures that you can use to create and manage reports.

     Technical reference for SQL Server views in Configuration Manager
     Provides sample SQL statements for each Configuration Manager SQL view
     category, exercises for modifying existing Configuration Manager reports and
     creating new reports, information about writing SQL statements and the query
     design tools available in SQL Server that can be used when writing report SQL
     statements, and an overview of the Configuration Manager WMI Provider schema.

See also
     Exploring your Configuration Manager data on Power BI dashboard

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.213 -->

SQL Server views in Configuration
Manager
Article • 10/10/2022

A Microsoft SQL Server view is a virtual table whose contents are based on the result
from a SQL query. A view consists of a set of named columns and rows of data.
However, the contents of a view aren't stored in the SQL Server database. The rows and
columns of data come from tables or other SQL Server views referenced in the query
that defines the view and are produced dynamically when the query is run. The query
that defines the view can be from one or more tables or from other views in one or
more databases. Distributed queries (queries that access data from multiple data
sources) can also be used to define views that pull data from multiple heterogeneous
sources (data stored in multiple formats), such as data stored in a SQL Server database,
a text file, or a Microsoft Excel spreadsheet.

During setup, Configuration Manager creates the following SQL Server view types:

      Views against static (unchanging) tables.

      Views that use data from tables with a dynamic (changing) schema.

For a dynamic schema, setup creates a number of SQL Server stored procedures that
create the views. These stored procedures are run by Configuration Manager to refresh
the views when the schema of underlying tables changes. Collection evaluation,
discovery, and inventory data are examples of data for which new tables or new
properties in existing tables might be created during the operation of a Configuration
Manager site.

Reporting in Configuration Manager
Configuration Manager uses Microsoft SQL Server Reporting Services to allow you to
generate and run reports against the Configuration Manager database, from the
Configuration Manager console. This service now replaces the method used to create
reports in Configuration Manager 2007, and gives the following advantages:

      Uses an industry standard reporting system to query the Configuration Manager
      database.

      SQL Server Reporting Services offers higher performance, availability, and
      scalability over the previous reporting method.

<!-- p.214 -->

     Enables users who aren't familiar with Configuration Manager reporting to
     generate unplanned reports.

     Enables users to subscribe to reports; for example, a manager could automatically
     be e-mailed a report each day, detailing the status of a software update rollout.

     Simplifies the creation of SQL-based reports in Configuration Manager.

     Enables users to export reports in different kinds of popular formats.

For more information about using reports from the Configuration Manager console, see
Introduction to reporting.

Configuration Manager SQL Server view
schema
To create effective reports, accurate SQL statements based on the appropriate
Configuration Manager views need to be used to retrieve the required data and to
display the expected output. Knowing the Configuration Manager database view
schema is an important first step in learning how to create these reports.

Much of the Configuration Manager SQL Server view schema maps to the SMS Provider
WMI schema, which is used when building WQL-based queries and collections in the
Configuration Manager console. However, querying the views directly can be much
faster than using WMI and WQL, which receive a query request and in turn query the
SQL Server database for the information. By using SQL Server views directly, you
eliminate the intermediate step and gain a faster path to the data. For more information
about the SMS Provider WMI schema, see SMS Provider WMI Schema Reference in
Configuration Manager.

Configuration Manager SQL Server view
categories
To effectively create reports with the required output, it's essential to know what data
each of the Configuration Manager SQL Server views contains and how the views are
related to each other. The following topics in this section provide detailed information
about each of the view categories, what kind of data each of the views contains, and
what columns can be used to JOIN views in SQL statements.

See also

<!-- p.215 -->

Create Custom Reports by Using SQL Server Views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.216 -->

Application management views in
Configuration Manager
Article • 10/04/2022

The Configuration Manager application management views can be used to query for
information about applications, packages and programs, deployments, distribution
points, and more. These views will most often be joined to other views by using the
AdvertisementID, PackageID, or CollectionID columns. Many of the status views also
provide information about the status for applications and deployments.

The following sections provide detailed information about application management
views and application management status views.

Application management views
The application management views are described in this section.

v_Advertisement
Lists information about the deployment of packages and programs, including the
deployment ID (AdvertisementID), deployment name (AdvertisementName), package
ID, program name, collection ID, schedule information, and more. The v_Advertisement
view is similar to the v_AdvertisementInfo view, but with additional time and flag data.
The view can be joined to other views by using the AdvertisementID, PackageID, and
CollectionID columns.

v_AdvertisementInfo
Lists information about deployed packages and programs, including the deployment ID
(AdvertisementID), deployment name (AdvertisementName), package ID, program
name, collection ID, schedule information and more. The v_AdvertisementInfo view is
similar to the v_Advertisement view, but with additional package data. The view can be
joined to other views by using the AdvertisementID, PackageID, and CollectionID
columns.

v_CurrentAdvertisementAssignments
Lists the current application deployments, by advertisement ID, and the resource ID that
is assigned the advertisement. The view can be joined to other views by using the

<!-- p.217 -->

AdvertisementID or ResourceID columns.

v_DistributionPoint
Lists the distribution points and the application and software updates packages
contained on each in the Configuration Manager site hierarchy. This view also provides
the package ID, NAL path to the distribution point, site code, site name, source site, last
refresh time, status, and more. The view can be joined to other views by using the
PackageID and ServerNALPath columns.

v_DistributionPointInfo
Lists the distribution points in the Configuration Manager site hierarchy, including server
name, share name, NAL path, site code, whether it is a branch distribution point,
whether it is a pull distribution point and more. The view can be joined to other views by
using the ServerName and NALPath columns.

V_MDMApplications
Lists information about applications created for mobile devices including the application
name, description, publisher and more. It is unlikely that this view will be joined to other
views.

v_OS_Details
Lists the Configuration Manager supported platforms, including operating system,
architecture, and versions, on which each specified software distribution program can
run. The view contains the package ID, program name, operating system name,
platform, and minimum and maximum operating system versions. The view can be
joined to other views by using the PackageID column.

v_SMSPackage
Lists the packages in the Configuration Manager site hierarchy, including package ID,
package name, the path of the package source files, source site, priority, package flags,
last refresh time, and so forth. All packages are listed, including software deployment
packages, boot image packages, and more. The view can be joined to other views by
using the PkgID column.

v_Program

<!-- p.218 -->

Lists the programs for each package in the Configuration Manager site hierarchy,
including program name, package ID, program command line, dependent programs,
program flags, and so forth. The view can be joined to other views by using the
PackageID column.

v_UserTargetedApps
Lists each Configuration Manager application that has been deployed to a user. Includes
the application ID (CI_ID), the collection to which the application has been deployed (if
any), and whether the application requires approval. This view can be joined to other
views by using the CI_ID or CollectionID columns.

v_UserTargetedClassicApps
Lists each package and program that has been deployed to users. Includes the program
ID, the category, the publisher, the package and program name and more. This view can
be joined to other views by using the ProgramID, PackageID, or CollectionID columns.

v_DeploymentSummary
Lists all deployments that are currently active at the site. Includes the collection to which
the deployment was targeted, the name of the deployment, the deployment time,
deployment statistics and more. This view can be joined to other views by using the
CollectionID or PackageID columns.

v_ApplicationModelInfo
Lists the applications, by CI_ID that have been created. Also lists the deployment type
technology and any secured key for the application. This view can be joined to other
views by using the CI_ID column.

v_AppModelTargetingDeploymentInfo
No description.

v_AppModelTargetingInfo
No description.

v_Package

<!-- p.219 -->

Returns all packages that contain content for an application, package and program, or a
task sequences at this site. This view can be joined to other views by using the
PackageID column.

v_ClassicAppTargetingDeploymentInfo
No description.

v_ClassicAppTargetingInfo
No description.

v_ClassicDeploymentAssetDetails
Lists information and status for standard package and program deployments by
deployment ID. This includes the program name, package name, collection to which it
has been deployed, and more. This view can be joined to other views by using the
DeploymentID, PackageID, CollectionID and DeviceID columns.

v_AppDeploymentSummary
Lists deployment statistics for about Configuration Manager applications that have been
deployed to clients. This includes the CI_ID, target collection, localized display name,
description and more. This view can be joined to other views by using the CI_ID,
AssignmentID and TargetCollectionID columns.

v_AppDTDeploymentSummary
Lists information about deployment types that have been deployed to devices, by CI_ID.
This includes the deployment type name, the target collection, and status information
about the deployment. This view can be joined to other views by using the CI_ID,
AssignmentID and TargetCollectionID columns.

v_AppDTLaunchSummary
Lists information, by AppCI, about deployment types that have run on client devices.
This includes the assignment ID, the collection, the deployment type technology and
more. This view can be joined to other views by using the AppCI column.

v_AppEvalErrors

<!-- p.220 -->

Lists all devices, by machine ID where the application evaluation failed, for example, if
the application failed any requirements rules. This view can be joined to other views by
using the MachineID column.

v_AppInTaskSequenceDeployment
Lists, by task sequence name, all deployed task sequences that contain an application
deployment. This includes the collection to which the task sequence was deployed and
the deployment ID. This view can be joined to other views by using the Name column.

v_AppIntentAssetData
Lists for each computer (and each user if deployed to a user), compliance state
information by AssignmentID and Application ID (AppCI). State information includes
ComplianceState, EnforcementState, applicability, and desired compliance state. This
view can be joined to other views by using the ID columns and to vAppStatSummary by
using the AppCI column.

v_AppInTSDeployment
Lists, by name, all applications that are deployed by a task sequence. This view can be
joined to other views by using the Name column.

v_ApplicationAssignment
Lists detailed information about Configuration Manager application deployments, by
AssignmentID. This includes the name of the application, the collection to which it was
deployed, the creation time and more. This view is particularly useful when you want to
examine the status of your cmshort deployments. This view can be joined to other views
by using the AssignmentID and CollectionID columns.

v_CatalogAppModelProperties
No description.

v_CatalogClassicAppProperties
No description.

v_UserAppRequests

<!-- p.221 -->

Lists details about users requests for applications, sorted by CI_UniqueID. This includes
the application ID, the name of the user requesting the application, the display name of
the application and the device from which the request was made. This view can be
joined to other views by using the CI_UniqueID, Unique_User_Name0 and
Netbios_Name0 columns.

v_UserAppsLocalizedPropsForCatalog
No description.

Application management status views
The application management status views contain status and status summary
information about application deployments, applications and packages and programs.
For more information about status views, see Status and Alert Views in Configuration
Manager. The status views that contain application management information are
described in this section.

v_AdvertisementStatusInformation
Lists all advertisement status message IDs, the message state, and the message name,
such as succeeded, expired, failed, and retrying. The view can be joined to other
advertisement status views by using the MessageID column.

v_ClientAdvertisementStatus
Lists all package and program deployments with the associated status for resources that
have been targeted. The view can be joined to other views by using the
AdvertisementID, ResourceID, and LastStatusMessageID columns.

v_ClientOfferSummary
Lists the package and program deployments, by OfferID, the count of Configuration
Manager client computers that have been targeted, and the count of computers
reporting not started, waiting, running, retrying, failed, and succeeded status for the
advertisement. The view can be joined to other views by using the OfferID column,
which is the same as the AdvertisementID column in other views, and PkgID column,
which is the same as the PackageID column in other views.

<!-- p.222 -->

v_PackageStatus
Lists the status for all software distribution and software update deployment packages,
as well as the package server location, last update time, last status and more. The view
can be joined to other views by using the PackageID column.

v_PackageStatusDetailSumm
Lists all applications and packages and programs, by Package ID, the originating site
code, package name, site name, source version, the date for the summary information,
the targeted count for each package, and the count for installed, retrying, and failed
status. The view can be joined to other views by using the PackageID column.

v_PackageStatusDistPointsSumm
Lists all packages, by package ID, and the installation status for the package source files
on all associated distribution points. The view also provides information such as the site
code, path to the distribution point, path to source location, time of last copy, and so
on. The view can be joined to other views by using the PackageID and ServerNALPath
columns.

v_PackageStatusRootSummarizer
Lists all applications and packages and programs, by package ID, the package name,
source version, source date, the source site, size of the source files, the targeted count
for each package, and the count for installed, retrying, and failed status. The view can be
joined to other views by using the PackageID column.

v_PeerDPStatusInfo
Lists the peer distribution point states and associated state names. It is unlikely that this
view will be joined to other views.

v_ProgramOffers
Lists all programs that have been deployed as part of a package and program. This is
sorted by package ID and the program name. The view can be joined to other views by
using the PkgID column.

<!-- p.223 -->

User device affinity views
The user device affinity views contain information about configured relationships
between users and primary devices. The views that contain user device affinity
information are described in this section.

v_UsersPrimaryMachines
Lists, by user resource ID, the primary devices for that user. This view can be joined to
other views by using the MachineID or UserResourceID columns.

v_UserMachineIntelligence
Lists information, by resource ID about user logons to devices. This information can be
used by user device affinity to create automatic affinities. The information collected
includes the user name, device name, client type, number of logons, and time spent for
each session. This view can be joined to other views by using the MachineResourceID
column.

v_UserMachineRelation
Lists detailed information about user device relationships in the Configuration Manager
site including the relationship ID, the user name, the device ID, the creation time and
more. This view can be joined to other views by using the MachineResourceID column.

v_UserMachineRelationship
Lists information about users and their primary devices in the site. Includes the user
name, the device resource ID, the time the relationship was created, and more. This view
can be joined to other views by using the UniqueUserName or MachineResourceID
columns.

v_UserMachineSourceRelation
Lists all user device affinity relationships, by relationship resource ID, when they were
created, and who created them. This view can be joined to other views by using the
RelationshipResourceID column.

v_UserMachineTypeRelation

<!-- p.224 -->

Lists user and device relationships by relationship resource ID, relationship type, and
creation time. It is unlikely that this view will be joined to other views.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.225 -->

Client deployment views in
Configuration Manager
Article • 10/04/2022

There are no primary client deployment views, but there are status views that contain
information about the deployment state of Configuration Manager client computers and
devices. For more information about the status views, see Status and alert views in
Configuration Manager. The status views that contain client deployment information are
described in this section.

Client deployment views

v_ClientDeploymentState
Lists all Configuration Manager clients, by SMSID, and the last client deployment state
reported, as well as the fully qualified domain name (FQDN), NetBIOS name, assigned
site code, client version, and so on.

The view can be joined to other views by using the SMSID, FQDN, NetBiosName, and
LastMessageStateID columns.

      LastMessageStateID: The state ID for topic type 800.

      DeploymentBeginTime: The last message time when the message's state ID is
      STATE_STATEID_CLIENT_DEPLOYMENT_STARTED (100), telling the server that the
      deployment starts. It clears the DeploymentEndTime time.

      DeploymentEndTime: The last message time when the state ID is
      STATE_STATEID_CLIENT_DEPLOYMENT_SUCCEEDED (400) or
      STATE_STATEID_CLIENT_DEPLOYMENT_SUCCEEDED_REBOOT_SUCCEEDED (401).
      This tells the server that the deployment ends.

      AssignmentBeginTime: The time when getting state ID
      STATE_STATEID_CLIENT_ASSIGNMENT_STARTED (500).

      AssignmentEndTime: The time that the assignment was done with ID
      STATE_STATEID_CLIENT_ASSIGNMENT_SUCCEEDED (700).

      The Configuration Manager states are listed in the v_StateNames view.

<!-- p.226 -->

v_DeviceClientDeploymentState
Lists all Configuration Manager mobile device clients that are enrolled by Configuration
Manager, by device client ID, NetBIOS name, and device ID, and the last device
deployment state reported, as well as the assigned site code, device client version, and
so on. This status view is also listed and described in Mobile device management views
in Configuration Manager.

The view can be joined to other views by using the DeviceClientID,
DeviceNetBiosName, and DeviceDeploymentState columns. The
DeviceDeploymentState column contains the state ID for topic type 800. The
DeviceClientID column contains the same information as the SMS_Unique_Identifier0
column in the v_R_System view. The Configuration Manager states are listed in the
v_StateNames view.

v_CombinedDeviceResources
Lists information about all devices in the Configuration Manager site, by machine ID.
The columns in this view display information such as the client name, GUID, operating
system, assigned site code, domain, the client version and whether the device is a virtual
machine. This view can be joined to other views by using the MachineID column.

v_CP_Machine
Lists information about client push attempts to install the client on computers. Includes
the computer name, when the last attempt to install the client occurred, the assigned
site code, the number of attempts made, and the current status. This view can be joined
to other views by using the MachineID column.

Client notification views
Client notification in Configuration Manager lets some client operations be performed
as soon as possible, instead of during the usual client policy polling interval. For
example, you can use the client management task Download Computer Policy to
instruct computers to download policy as soon as possible. Additionally, you can start
some actions for Endpoint Protection, such as a malware scan of a client.

The client notification views are described in this section.

v_BGB_ResTask

<!-- p.227 -->

List information about the tasks performed on devices by Configuration Manager client
notification. This view can be joined to other views by using the ResourceID column.

v_BGB_ResTaskPush
Lists information about the tasks deployed by Configuration Manager client notification,
including the task ID, deployment ID, and status. This view can be joined to other views
by using the ResourceID column.

v_BGB_Task
Lists information about all tasks that have been deployed by client notification. This
includes the task ID, when the task was created and whether it has expired. This view can
be joined to other views by using the TaskID column.

v_BgbMP
List the server name and database IDs of the management points that send out client
notifications. This view can be joined to other views by using the ServerName column.

v_BgbServerCurrent
Lists status information about online and offline clients for each server that sends client
notification requests. This view can be joined to other views by using the ServerID
column.

v_ClientAction
Lists information about client notification actions that were taken. This information
appears in the Client Operations node of the Configuration Manager console. This view
can be joined to other views by using the ID column.

v_ClientActionImportance
Lists information about the priority of client notification tasks as shown in the Client
Operations node of the Configuration Manager console. This view can be joined to
other views by using the ClientOperationID column.

v_ClientActionResult

<!-- p.228 -->

Lists information about the results of client notification actions that are shown in the
Client Operations node of the Configuration Manager console. This view can be joined
to other views by using the MachineID column.

v_ClientOperationInProcessing
Lists the ID number of client notification operations that are currently being processed.
It is unlikely that this view will be joined to other views.

v_ClientOperationLinkedObjects
Lists information about objects that are linked to client notification actions. It is unlikely
that this view will be joined to other views.

v_ClientOperationTargets
Lists information about the computers on which client notification actions took place.
This view can be joined to other views by using the MachineID column.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.229 -->

Client status views in Configuration
Manager
Article • 10/04/2022

Client status views contain information about the client status components on
Configuration Manager client computers and the results of client checks. There are also
status views that contain information about the health of Configuration Manager client
computers, such as when the client last scanned for hardware and software inventory,
the last policy request, and so on. Client status views will most often be joined to other
views by using the MachineID, ResourceID, NetbiosName, HealthStatus, and
HealthType columns.

The following sections provide detailed information about client status views.

Client status views
The client status views contain status and status summary information about the health
of Configuration Manager client computers. For more information about the status
views, see Status and alert views in Configuration Manager. The status views that contain
client status information are described in this section.

v_CH_PolicyRequestHistory
Lists all Configuration Manager client computers and the time of the last policy request,
which can be used to determine how many unique clients have requested policy within
a given number of days. The view can be joined to other views by using the ResourceID
column.

v_CH_ClientSummary
Lists client status information for all Configuration Manager client computers, such as
the last time it was reported as being online, the last management point it contacted,
the last time it reported hardware and software inventory, the last time a client health
evaluation was performed, whether a remediation occurred and more. The view can be
joined to other views by using the ResourceID column.

v_CH_ClientSummaryHistory

<!-- p.230 -->

Lists a summarization of the client status information for all Configuration Manager
client computers, such as total number of clients, total number of clients that are active
based on the last heartbeat discovery, hardware and software inventory scans, and so
on. It is unlikely that this view will be joined to other views.

v_ClientHealthState
Lists all Configuration Manager clients, by SMSID, and the last client health state
reported for each state type, as well as the NetBIOS name, fully qualified domain name
(FQDN), assigned site code, health type, health state, health state name, and so on. The
view can be joined to other views by using the SMSID, NetBiosName, HealthType, and
HealthState columns. The SMSID column contains the same information as the
SMS_UniqueIdentifier0 column in the v_R_System view. The HealthType column in this
view contains the same information as the TopicType column in the v_StateNames view
and the HealthState column in this view contains the same information as the StateID
column in the v_StateNames status view. Client health state messages have a state type
from 1000 to 1004. The Configuration Manager states are listed in the v_StateNames
view.

v_DeviceClientHealthState
Lists all Configuration Manager mobile device clients, by device client ID, NetBIOS name,
and device ID, and the health state of the device, as well as the assigned site code,
owner name, and so on. This status view is also listed and described in the Mobile
device management views in Configuration Manager topic. The view can be joined to
other views by using the DeviceClientID, DeviceNetBiosName, HealthType, and
HealthState columns. The DeviceClientID column in this view contains the same
information as the SMS_Unique_Identifier0 column in the v_R_System view. The
HealthType column in this view contains the same information as the TopicType column
in the v_StateNames view and the HealthState column in this view contains the same
information as the StateID column in the v_StateNames status view. Client health state
messages have a state type from 1000 to 1004. The Configuration Manager states are
listed in the v_StateNames view.

v_CH_ClientSummaryCurrent
For each collection, lists, by collection ID, information about the status of client in that
collection. The view contains information about the number of clients in the collection
and which are active, the number of clients that have requested policy, the number of

<!-- p.231 -->

clients that have been remediated and more. This view can be joined to other views by
using the CollectionID column.

v_CH_EvalResults
Lists the results, by resource ID of client status checks performed on each client in the
site. This includes the NetBIOS name of each client, the last evaluation time, the results
of the evaluation and more. This view can be joined to other views by using the
ResourceID column.

v_CH_HealthCheckInfo
Lists information about each check that client check can perform on client computers,
sorted by the ID number. It is unlikely that this view will be joined to other views.

v_CH_HealthCheckSummary
Lists information about the current client checks being performed by Configuration
Manager, sorted by collection. The view shows the collection, the ID of the health check
being performed (see v_CH_HealthCheckInfo to map this ID to the name of the client
check), the number of computers in the collection that have performed the client check
and the number of computers that still have to perform the client check. This view can
be joined to other views by using the CollectionID column.

v_CH_PendingPolicyRequests
Lists information about pending policy requests including the GUID of the request, the
time of the request and the management point that will process the request. It is
unlikely that this view will be joined to other views.

v_CH_Settings
Lists information about the thresholds for client status reporting. It is unlikely that this
view will be joined to other views.

v_ActiveClients
Lists information, by MachineResourceID about all active client computers in the site.
This includes whether the client is on the Internet, the client version, information about

<!-- p.232 -->

certificates and more. This view can be joined to other views by using the
MachineResourceID column.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.233 -->

Collection views in Configuration
Manager
Article • 10/04/2022

Collection views contain information about the collections, collection rules, and
collection members. Many of the collection views are useful when creating reports on
site data, software update deployments, application deployments, and compliance
settings.

The two types of collection views are as follows:

      The first type lists all members of a specific collection and starts with the
      v_CM_RES_COLL_ view name and ends with the collection ID, with the exception of
      the v_FullCollectionMembership view, which lists all members of all collections.
      This collection type will be used most often when creating reports.

      The second type of collection view has a name that starts with v_ and contains
      general information about the collections but not the member resources within
      each collection.

Collection views
The collection views are described in this section.

v_ClientCollectionMembers
Lists all devices, by resource ID, that are not in an obsolete or decommissioned state,
what collections the device is a member of, and whether the resource is a Configuration
Manager client. The view can be joined to other views by using the CollectionID and
ResourceID columns.

v_CM_RES_COLL_<CollectionID>
Lists all devices that are members of the collection. The device ID, name, client GUID,
site code, whether the computer is assigned to a site, whether the computer has been
approved, whether the computer is an active client, and so on. The view can be joined to
other views by using the CollectionID and ResourceID columns.

v_Collection

<!-- p.234 -->

Lists all collections by collection ID, collection name, and what view the collection maps
to (listed in the v_CM_RES_COLL_<CollectionID> row), the last time the collection
membership changed, as well as other collection information. The view can be joined to
other views by using the CollectionID column.

v_CollectionRuleDirect
Lists the collections that contain direct membership rules. The view can be joined to
other views by using the CollectionID or ResourceID columns.

v_CollectionRuleQuery
Lists the query statement for each query-based collection. The view can be joined to
other views by using the CollectionID and LimitToCollectionID columns.

v_CollectionSettings
Lists the configured settings for each collection, such as restart countdown, polling
interval, collection variable precedence, source site, last modification time, and more.
The view can be joined to other views by using the CollectionID column.

v_CollectionVariable
Lists the collections that have associated task sequence variables. The view can be joined
to other views by using the CollectionID column.

v_FullCollectionMembership
Lists the resources for all collections. Contains the collection ID, resource ID, name,
domain, resource GUID, site code, and other client information. The view can be joined
to other views by using the CollectionID and ResourceID columns.

v_FullCollectionMembership_Valid
Lists the resources that are not in an obsolete or decommissioned state for all
collections and contains a subset of information from the v_FullCollectionMembership
view. The view can be joined to other views by using the CollectionID and ResourceID
columns.

v_ServiceWindow

<!-- p.235 -->

Lists all collections that have a configured maintenance window and information about
the maintenance window, such as the maintenance window name, description, start
time, and duration. The view can be joined to other views by using the CollectionID
column.

v_Collections
Lists all collections by collection ID and collection name. Also contains further
information about each collection, for example:

     The last time the collection was changed (LastChangeTime)
     The last time the collection was re-evaluated (LastRefreshRequest)
     The collections limiting collection (LimitToCollectionID)
     Whether the collection is built-in, or was created by an administrator (IsBuiltIn)

The view can be joined to other views by using the CollectionID column.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.236 -->

Compliance settings views in
Configuration Manager
Article • 10/04/2022

The Configuration Manager compliance settings views contain information about the
compliance of devices with regard to a number of configurations, such as whether the
correct Windows operating system versions are installed and configured appropriately,
whether all required applications are installed and configured correctly, whether
optional applications are configured appropriately, and whether prohibited applications
are installed. The compliance settings views contain information about the configuration
baselines in the site, which configuration baselines store information about
configuration items, software updates, bundles, drivers, and so on. Several of the status
and status summarizer views contain status information for the configuration items and
configuration item assignments.

The following sections provide detailed information about compliance settings views,
compliance settings status views, and compliance settings status summarizer views.

Compliance settings views
There are many compliance settings views, and it can sometimes be difficult to find the
information that you need for your report SQL statement. The following are some of the
key compliance settings views and columns:

      CI_ID column � Commonly used to join compliance settings views

      v_ConfigurationItems view - Used to retrieve information about the configuration
      items in the site.

      v_CategoryInfo and v_LocalizedCIProperties views - Often be used to retrieve
      additional information about the configuration items.

      AssignmentID column and the v_CIAssignment view - Used to retrieve
      information about the configuration item deployments.

      v_CIAssignmentToCI view - Can be used as the link between the
      v_ConfigurationItems and v_CIAssignment views.

      v_CIAssignmentTargetedMachines view - can be used as the link between the
      v_CIAssignment view and the views that contain resource information, such as the
      v_R_System view.

<!-- p.237 -->

The compliance settings views are described in this section.

v_AssignmentTargetedCIs
Lists the assignment ID, CI_ID and unique assignment ID for each deployed
configuration item. This view can be joined to other views by using the CI_ID and
AssignmentID columns.

v_BaselineTargetedComputers
Lists the clients, by ResourceID, to which a configuration baseline has been deployed, by
CI_ID. This view displays only configuration baselines (CI_Type = 2). This view can be
joined to other views by using the CI_ID and ResourceID columns.

v_Categories
Lists the configuration item category instances, by CategoryInstanceID and
CategoryInstance_UniqueID, category type name, date the category instance was last
modified, source site, and the parent category. This view contains the same source data
as the v_CategoryInstances view, but it displays more columns. This view can be joined
to other views by using the CategoryInstanceID and ParentCategoryInstanceID
columns.

v_CategoryInfo
Lists the configuration item category instances, by CategoryInstanceID and
CategoryInstance_UniqueID, category type name, date the category instance was last
modified, source site, parent category, category instance name, and locale ID. This view
contains the same data as the v_Categories view plus two additional columns from the
v_LocalizedCategories_SiteLoc view. This view can be joined to other views by using the
CategoryInstanceID and ParentCategoryInstanceID columns.

v_CategoryInstances
Lists the configuration item category instances, by category instance ID and category
instance unique ID, category type name, date the category instance was last modified,
source site, and parent category. This view contains the same source data as the
v_Categories view, but it displays fewer columns. This view can be joined to other views
by using the CategoryInstanceID and ParentCategoryInstanceID columns.

<!-- p.238 -->

v_CI_ApplicablePlatforms
Lists the configuration items, by CI_ID and CI_UniqueID that have specific applicable
platforms configured, including the operating system name, operating system maximum
and minimum versions, and operating system platform. For example, a configuration
item created in the Configuration Manager console that has All Windows platforms
selected for the Applicability property will not be listed in this view, but the view will
contain a record for each Windows platform for the configuration item when the
Specified Windows platforms is selected. This view can be joined to other views by
using the CI_ID and CI_UniqueID columns.

v_CI_DriverHardwareIDs
Lists the configuration items, by CI_ID and CI_UniqueID, that have a configuration item
type of Driver (CIType_ID=6) and the associated hardware IDs that the driver supports.
For example, a driver added in the Drivers node under the Operating System
Deployment node in the Configuration Manager console will be listed in this view as
well as the hardware IDs that it supports. The view can be joined to other views by using
the CI_ID and CI_UniqueID columns.

v_CI_DriverModels
Lists the configuration items, by CI_ID and CI_UniqueID, that have a configuration item
type of Driver (CIType_ID=6) and the supported model names and driver manufacturer.
The supported models are listed in the Applicability section of the driver properties in
the Configuration Manager console. The view can be joined to other views by using the
CI_ID and CI_UniqueID columns.

v_CI_DriversCIs
Lists the configuration items, by CI_ID and CI_UniqueID, that have a configuration item
type of Driver (CIType_ID=6), as well as the driver type, driver INF file, driver date, driver
version, driver class, driver provider, whether the driver is signed (and if so, the driver
signer), and whether the driver is boot critical. The view can be joined to other views by
using the CI_ID and CI_UniqueID columns.

v_CIAssignment
Lists the configuration item deployments by AssignmentID, Assignment_UniqueID, and
AssignmentName that are active in the Configuration Manager hierarchy, including the

<!-- p.239 -->

deployment description, collection ID and name that is targeted by the deployment,
start time, enforcement deadline, whether the deployment is an update deployment,
and other details about the deployment. The view can be joined to other configuration
items, software updates, and status views by using the AssignmentID and
Assignment_UniqueID columns, and it can be joined to collection views by using the
LocalCollectionID and CollectionID columns.

v_CIAssignmentTargetedCollections
Lists the deployments, by AssignmentID, that are active in the Configuration Manager
hierarchy and the associated target collection, by LocalCollectionID, CollectionID, and
CollectionName. The view can be joined to other configuration items, software updates,
and status views by using the AssignmentID column, and it can be joined to collection
views by using the LocalCollectionID and CollectionID columns.

v_CIAssignmentTargetedMachines
Lists the deployments, by AssignmentID, that are active in the Configuration Manager
hierarchy and the Configuration Manager clients, by ResourceID, that have been
targeted for the assignment. The view can be joined to other views by using the
AssignmentID and ResourceID columns.

v_CIAssignmentToCI
Lists the deployments, by AssignmentID, and the configuration items, by CI_ID, that are
in the deployment. For example, if the deployment is a software update deployment, the
configuration item ID for each software update in the deployment will be listed. The
view can be joined to other views by using the AssignmentID and CI_ID columns.

v_CICategories
Lists the configuration items, by CI_ID, and the configuration item category instances, by
CategoryInstanceID and CategoryInstance_UniqueID, in which they belong, as well as
the category type name, date last modified, source site, and parent category instance ID.
This view contains the same information as the v_CICategories_All view, except that it
does not contain parent categories. The view can be joined to other views by using the
CI_ID, CategoryInstanceID, and ParentCategoryInstanceID columns.

v_CICategories_All

<!-- p.240 -->

Lists the configuration items, by CI_ID, and the configuration item category instances, by
CategoryInstanceID and CategoryInstance_UniqueID, in which they belong, as well as
the category type name, date last modified, source site, and parent category instance ID.
This view contains the same information as the v_CICategories view, except that it also
contains parent categories. The view can be joined to other views by using the CI_ID,
CategoryInstanceID, and ParentCategoryInstanceID columns.

v_CICategoryInfo
Lists the configuration items, by CI_ID, and the configuration item category instances, by
CategoryInstanceID and CategoryInstance_UniqueID, in which they belong, as well as
the category type name, date the category instance was last modified, source site,
parent category, category instance name, and locale ID. This view contains the same
data as the v_CICategories view plus two additional columns from the
v_LocalizedCategories_SiteLoc view, and the same data as the v_CICategoryInfo_All
view, except that it does not contain parent categories. The view can be joined to other
views by using the CI_ID, CategoryInstanceID, and ParentCategoryInstanceID columns.

v_CICategoryInfo_All
Lists the configuration items, by CI_ID, and the configuration item category instances, by
CategoryInstanceID and CategoryInstance_UniqueID, in which they belong, as well as
the category type name, date the category instance was last modified, source site,
parent category, category instance name, and locale ID. This view contains the same
data as the v_CICategories_All view plus two additional columns from the
v_LocalizedCategories_SiteLoc view, and the same data as the v_CICategoryInfo view,
except that it also contains parent categories. The view can be joined to other views by
using the CI_ID, CategoryInstanceID, and ParentCategoryInstanceID columns.

v_CIContents
Lists the configuration items, by CI_ID, that have associated content, which is listed by
ContentID, and whether the content has been provisioned. For example, configuration
items with the Software Updates (CIType_ID = 1) have associated update files, and
Driver configuration types (CIType_ID = 6) have associated driver files. The view can be
joined to other views by using the CI_ID and Content_ID columns.

v_CIContents_All
