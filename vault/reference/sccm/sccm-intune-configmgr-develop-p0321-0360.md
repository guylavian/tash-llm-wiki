---
title: "Configuration Manager SDK documentation — pages 321-360"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0321-0360
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0321-0360
family: sccm
documentKind: "doc"
abstract: "Object key Object Name 29 Categories 30 Alerts 31 Applications 32 Global conditions 33 User device affinity 34 Authorization settings 36 Device enrollment 37 Software updates 38 Client settings 40 Migration site mapping 41 Migration jobs 42 Distribution points 43 Distribution po"
---

# Configuration Manager SDK documentation — pages 321-360

<!-- p.321 -->

Object key   Object Name

29           Categories

30           Alerts

31           Applications

32           Global conditions

33           User device affinity

34           Authorization settings

36           Device enrollment

37           Software updates

38           Client settings

40           Migration site mapping

41           Migration jobs

42           Distribution points

43           Distribution point groups

44           Inventory reporting

45           Boundaries

46           Boundary groups

47           Endpoint Protection

48           Configuration policies

49           Windows Firewall settings

50           Microsoft Intune subscription

52           User state management

53           Windows Firewall policies

54           Windows Azure subscription

55           Settings for Windows RT side loading keys

56           Wi-Fi profiles

57           VPN profiles

<!-- p.322 -->

 Object key             Object Name

 58                     Client authentication certificate settings

 59                     Remote connection profiles

 60                     Trusted root certificate settings

 200                    Configuration data assignments

 201                    Deployments

 202                    Client settings

 203                    Virtual environments

How to interpret decimal permission values
In the security views, there are decimal values that equate to a specific class or instance
permissions. Each individual permission uses one of 28 bits. The following table lists
each of these permissions, the bit that is used, and the decimal value of that bit.

                                                                                ﾉ   Expand table

 Permission name                  Bit value                          Bit            Decimal
                                                                     position       value

 Read                             1                                  1              1

 Modify                           10                                 2              2

 Delete                           100                                3              4

 Distribute                       1000                               4              8

 Create Child                     10000                              5              16

 Use remote tools                 100000                             6              32

 Advertise                        1000000                            7              64

 Modify resource                  10000000                           8              128

 Administer                       100000000                          9              256

 Delete resource                  1000000000                         10             512

 Create                           10000000000                        11             1024

 View collected files             100000000000                       12             2048

<!-- p.323 -->

 Permission name                 Bit value                      Bit         Decimal
                                                                position    value

 Read resource                   1000000000000                  13          4096

 Delegate                        10000000000000                 14          8192

 Meter                           100000000000000                15          16384

 Manage SQL commands             1000000000000000               16          32768

 Manage status filters           10000000000000000              17          65536

 Manage folders                  100000000000000000             18          131072

 Network access                  1000000000000000000            19          262144

 Import computer entry           10000000000000000000           20          524288

 Create task sequence media      100000000000000000000          21          1048576

 Modify collection setting       1000000000000000000000         22          2097152

 Manage OSD and ISV Proxy        10000000000000000000000        23          4194304
 Certificates

 Recover user state              100000000000000000000000       24          8388608

 Manage management               1000000000000000000000000      25          16777216
 controllers

 View management controllers     10000000000000000000000000     26          33554432

 Manage Asset Intelligence       100000000000000000000000000    27          67108864

 View Asset Intelligence         1000000000000000000000000000   28          134217728

To interpret a permission value, you can convert the decimal value to binary and use the
preceding table to get the specific permissions. To help understand this process, see the
following examples.

Decimal conversion example 1
In the v_SecuredObject view, the SMS_Site secured object has a value of 638983 in the
AvailableInstancePermissions column. To find out what this means, first convert the
decimal number to binary. This equates to 10011100000000000111, in which the 1st,
2nd, 3rd, 15th, 16th, 17th, and 20th bits are used. Use the bit values from the preceding
table to calculate the values in the following table. When the decimal values are added,
they will total the initial 638983 value.

<!-- p.324 -->

                                                                         ﾉ   Expand table

 Permission Name                     Binary Position           Decimal Value

 Read                                1                         1

 Modify                              2                         2

 Delete                              3                         4

 Meter                               15                        16384

 Manage SQL commands                 16                        32768

 Manage status filters               17                        65536

 Import computer entry               20                        524288

Decimal conversion example 2
In the v_SecuredObject view, the SMS_Collection secured object has a value of
52435687 in the AvailableInstancePermissions column. This decimal number results in
11001000000001101011100111 when converted to binary. This is interpreted as shown
in the following table.

                                                                         ﾉ   Expand table

 Permission Name                            Binary Position        Decimal value

 Read                                       1                      1

 Modify                                     2                      2

 Delete                                     3                      4

 Use remote tools                           6                      32

 Advertise                                  7                      64

 Modify resource                            8                      128

 Delete resource                            10                     512

 View collected files                       12                     2048

 Read resource                              13                     4096

 Modify collection setting                  22                     2097152

<!-- p.325 -->

 Permission Name                                Binary Position          Decimal value

 Manage management controllers                  25                       16777216

 View management controllers                    26                       33554432

Role based administration views
This section describes the role based administration views in the Configuration Manager
database.

v_Roles
Lists all available security roles at the Configuration Manager site. Includes information
about whether the role is built-in, who created the role, the role name and description,
and more. It is unlikely that this view will be joined to other views.

v_Admins
Returns all administrative users (that is, those who appear in the Administrative Users
node under Security in the Administration workspace) This view can be joined to other
views by using the AdminID column.

v_SecuredObjectTypes
Lists the various Configuration Manager objects that can be secured by role based
administration. It is unlikely that this view will be joined to other views.

v_SecuredScopePermissions
Lists each user of the Configuration Manager site and the security roles they are
associated with. This view can be joined to other views by using the AdminID column.

See also
SQL Server views in Configuration Manager

Feedback

<!-- p.326 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.327 -->

Site administration views in
Configuration Manager
Article • 10/10/2022

The Configuration�Manager site views contain information such as the site code,
Configuration Manager version, the location of the SMS provider, site server name, site
system names, site boundary information, and more. There are also status views that
contain information about sites, site systems, and components. The site and site status
views will most often be joined to other views by using the SiteCode or ServerName
columns.

The following sections provide detailed information about site views and site status
views.

Site views
The site views contain information about the Configuration Manager site and are
described in this section.

v_BoundarySiteCode
Lists each boundary in the Configuration Manager hierarchy together with the site code
associated with that boundary. This view can be joined to other views by using the
BoundaryID column.

v_BoundarySiteSystems
BoundaryIDServerNALPathSiteSystemName

v_Identification
Lists information about each site in the hierarchy, including site code, site name,
Configuration Manager version, Configuration Manager build number, service account
name, where the SMS provider is located, site server name, and language. The view can
be joined to other views by using the ThisSiteCode column.

v_LocalizedNameLookup

<!-- p.328 -->

Lists the matching English view column names to a string resource in a resource DLL
that contains the localized version of the name. It is unlikely that this view will be joined
to other views.

v_LocalizedNameValue
Lists the matching English name to the localized name. It is unlikely that this view will be
joined to other views.

v_LocalizedSettingType
Lists the matching English view setting type with the localized name for the setting type.
It is unlikely that this view will be joined to other views.

v_ServerComponents
Lists the components for each site, such as SMS_EXECUTIVE,
SMS_SITE_CONTROL_MANAGER, and so on. The site code, server name, and
Configuration Manager components are listed. The view can be joined to other views by
using the SiteCode, MachineName, or ComponentName columns.

v_Site
Lists information about each site in the Configuration Manager hierarchy, including site
code, site name, site version, site server name, installation directory, and more. The view
can be joined to other views by using the SiteCode or ServerName columns.

v_SoftwareConversionRules
Lists all software inventory names that are to be converted to a standard name. For
example, software that is inventoried with the manufacturer name of Microsoft or
Microsoft Corp. is converted to a display name of Microsoft Corporation. It is unlikely
that this view will be joined to other views.

v_SupportedPlatforms
Lists the supported operating systems, including operating system platform, minimum
and maximum version, and operating system name. This list is used by a number of
Configuration Manager operations. It is unlikely that this view will be joined to other
views.

<!-- p.329 -->

v_SystemResourceList
Lists all site system locations for each site in the Configuration Manager hierarchy. The
NAL path, resource type, site code, site system role name, and site system computer
name are listed. The view can be joined to other views by using the SiteCode,
ServerName, or NALPath columns.

v_SiteAndSubsites
List information about each site in the hierarchy, including the site code, site name, site
type, build number, site server name and more. This view can be joined to other views
by using the SiteCode and ServerName columns.

Site status views
The site status views contain status and status summary information about
Configuration Manager components, site servers, site systems, and so on. For more
information about the status views, see Status and Alert Views in Configuration
Manager. The status views that contain site information are described in this section.

v_ComponentSummarizer
Lists summary status information for all Configuration Manager components for
different intervals. The view also provides the site code, server name, component name,
the count of information, warning, and error messages, and so on. The information in
this view contains the same information that is displayed in the Component Status node
of the Configuration Manager console, but the view contains information for all display
intervals. The value in the Status column provides the current status for the component.
A value of 0 indicates that the component is OK, a value of 1 indicates a warning state
for the component, and a value of 2 indicates a critical state for the component. The
view can be joined to other views by using the SiteCode, MachineName, and
ComponentName columns.

v_ServerMessageStatistics
Lists the site system servers, the associated site code, when the last heartbeat occurred,
and how long the heartbeat took to process. The view can be joined to other views by
using the ServerName column.

v_SiteDetailSummarizer

<!-- p.330 -->

Lists status summary information for all Configuration Manager sites, by site code, for
different intervals. The view also provides the site name, site version, interval, the count
of information, warning, and error messages, and so on. The information in this view
contains the same information that is displayed in the Site Status node of the
Configuration Manager console, but the view contains information for all display
intervals. The view can be joined to other views by using the SiteCode column. The
value in the Status column provides the current status for the site. A value of 0 indicates
that the site is OK, a value of 1 indicates a warning state for the site, and a value of 2
indicates a critical state for the site.

v_SiteSystemSummarizer
Lists status summary information for all Configuration Manager sites systems for
different intervals. The view also provides the object location, the site role for the site
system, total disk space, free disk space, and percentage of free disk space for the site
system, the time of the last status reported, and whether the site system is available. The
information in this view contains the same information that is displayed in the Site
System Status node of the Configuration Manager console. The view can be joined to
other views by using the SiteCode column.

v_SummarizerSiteStatus
Lists the site summary status, which is the same status displayed for the <site code> -
<site name> node of the Configuration Manager console. The view can be joined to
other views by using the SiteCode column.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.331 -->

Software metering views in
Configuration Manager
Article • 10/10/2022

The software metering views contain information such as the software metering rules
that are created in the Configuration Manager hierarchy, which files to meter, the
products in which the files belong, the users that have used the metered files, and more.
Several of the status and status summarizer views also provide information about file
usage. Most often, the software metering views can be joined to other views by using
the FileID and ResourceID columns.

The following sections provide detailed information about software metering views and
software metering status views.

Software metering views
The software metering views are described in this section.

v_GS_SoftwareUsageData
Lists the Configuration Manager client computers, by resource ID, that have used
metered files. The view contains the start time, end time, user name, file ID, file name,
file description, file version, file size, product name, product version, and more. The view
can be joined to other views by using the ResourceID, FileID, and UserName columns.

v_MeterData
Lists all software metering data, including the meter data ID, time span for the data, file
ID, resource ID, user ID, and more. The view can be joined to other views by using the
FileID, ResourceID, and MeteredUserID columns.

v_MeteredFiles
Lists all files that are configured in the software metering rules and metered on clients.
The view contains the software metering rule ID, security key, product name, site code,
file name, file version, metered file ID, metered product ID, and more. The view can be
joined to other views by using the RuleID, SecurityKey, MeteredProductID, and
MeteredFileID columns.

<!-- p.332 -->

v_MeteredProductRule
Lists all software metering rules that have been configured in the Configuration
Manager site hierarchy. The view contains the software metering rule ID, security key,
product name, file name, file version, site code, and more. The view can be joined to
other views by using the RuleID and SecurityKey columns.

v_MeteredUser
Lists all users who have used metered files. The view contains the metered user ID, full
user name (domain\user name), domain, and user name. The view can be joined to
other views by using the MeteredUserID and FullName columns.

v_MeterRuleInstallBase
Lists all metered files for system resources that match files by FileID that are also in
software inventory. The view contains the rule ID, product name, metered file ID, and
resource ID. The view can be joined to other views by using the RuleID, MeteredFileID,
and ResourceID columns.

Software metering status views
The software metering status views contain status summary information about the file
usage for metered files. For more information about the status views, see Status and
Alert Views in Configuration Manager. The status views that contain software metering
information are described in this section.

v_FileUsageSummary
Lists software metering summary status information for file usage by site. The view can
be joined to other views by using the FileID column.

v_FileUsageSummaryIntervals
Lists software metering summary interval information for file usage. It is unlikely that
this view will be joined to other views.

v_MonthlyUsageSummary

<!-- p.333 -->

Lists the Configuration Manager client computers, by resource ID, and the usage
summary for metered files, as well as the logged-on user name, usage time, and time of
last usage. The view can be joined to other views by using the ResourceID, FileID, and
MeteredUserID columns.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.334 -->

Software updates views in Configuration
Manager
Article • 10/10/2022

The Configuration Manager software updates views contain information about the
software updates metadata, software update groups, software update bundles, and so
on. Many of the status and status summarizer views provide information about software
updates compliance, software update deployment evaluation and enforcement state,
scan states, compliance status summarization, deployment status summarization, and so
on. The compliance state for clients using an inventory scan tool, such as the Inventory
Tool for Microsoft Updates, are picked up during the hardware inventory cycle and
stored in the inventory views.

The following sections provide detailed information about software updates views,
software updates status views, software updates status summarizer views, and software
updates hardware inventory views.

Software updates views
The software updates views contain information about software updates. When creating
software updates reports for individual software updates or update bundles, the
v_UpdateCIs or v_UpdateInfo views will most often be used in combination with other
views. The software update views are described in this section.

v_AuthListInfo
Lists the software update groups, by CI_ID, for the Configuration Manager hierarchy,
including when the software update group was created, when it was last modified, who
last modified the software update group, source site, title, description, and so on. This
view contains a subset of information from the v_ConfigurationItems view, joins the
v_LocalizedCIProperties view to retrieve software update group title and description
information, and filters the information by CIType=9, which indicates an software
update group configuration item. The view can be joined to other views by using the
CI_ID, CI_UniqueID, and SDMPackage_ID columns.

v_EULAContent
Lists the license terms, by EULAContentID and EULAContentUniqueID, associated with
software updates. The license terms text is in binary format. The view can be joined to

<!-- p.335 -->

the v_CIEULA_LocalizedContent view, which associates the software update
(configuration item) to the license terms, by using the EULAContentUniqueID column.

v_ScannedUpdates
Lists all software updates, by CI_ID, that have been scanned for software updates
compliance on Configuration Manager clients, including Resource ID, scan time, and last
local change time. The view can be joined to other views by using the CI_ID and
ResourceID columns.

v_SoftwareUpdateSource
Lists all sources for the software updates metadata, by UpdateSource_ID, for the site.
Configuration Manager sites should use WSUS Enterprise Server as the update source
and WUA as the scan method. The view can be joined to the v_UpdateScanStatus view
by using the UpdateSource_ID column.

v_UpdateCIs
Lists all of the software updates configuration items, by CI_ID and CI_UniqueID. The
information in this view is a subset of information from the v_ConfigurationItems view,
retrieving all records where the configuration type is Software Updates or Software
Updates Bundle (CIType=1 or 8), including article ID, bulletin ID, severity, date created,
whether the update is deployed, and so on. The view can be joined to other views by
using the CI_ID, CI_UniqueID, and SDMPackage_ID columns.

v_UpdateContents
Lists the software updates configuration items that have associated content, by CI_ID,
the configuration item ID for the software update in which the content is associated, the
content ID, whether the content has been provisioned, the locale for the content, and so
on. The configuration item ID for a software updates bundle is listed multiple times in
the CI_ID column, and the configuration item IDs for the software updates that are part
of the bundle are listed in the ContentCI_ID column. For example, a software update
that is not a bundle would have the same configuration item ID in the CI_ID and
ContentCI_ID columns. A software updates bundle would have one listing with the
configuration item ID in the CI_ID column and the same configuration item ID in the
ContentCI_ID columns, and then would have new listings containing the configuration
item ID for the bundle in the CI_ID column and the configuration item ID for the
bundled software updates in the ContentCI_ID column. The ContentLevel column

<!-- p.336 -->

represents how many times a configuration item ID is listed in the ContentCI_ID column.
The view can be joined to other views by using the CI_ID and Content_ID columns and
to the v_CIContents_All view by using the ContentCI_ID column.

v_UpdateInfo
Lists stand-alone software updates (CIType_ID = 1) or software update groups
(CIType_ID = 9), by CI_ID, and information about the update or bundle, such as
configuration item type, configuration item version, data created, date last modified,
whether the update or bundle has been deployed, associated bulletin ID, article ID,
severity, and so on. Unlike the Configuration Manager console when it displays software
updates, this view does not list the updates that are part of an update bundle. The view
can be joined to other views by using the CI_ID, CI_UniqueID, and SDMPackage_ID
columns.

Software updates status views
The software updates status views provide information about software updates
compliance, deployment evaluation, deployment enforcement, scan state, and so on.
These views can generally be joined to other software updates and desired
configuration management views by using the CI_ID column. For more information
about the status views, see Status and Alert Views in Configuration Manager. The status
views that contain software updates information are described in this section.

v_AssignmentState_Combined
Lists the last state message received from Configuration Manager client computers for
assigned software update deployments, including the assignment ID (deployment ID),
resource ID, state type, and so on. The view can be joined to other views by using the
AssignmentID, ResourceID, StateType, or StateID columns.

v_AssignmentStatePerTopic
Lists the last state message for each state type received from Configuration Manager
client computers for assigned software update deployments, including assignment ID
(deployment ID), resource ID, state type, and so on. The view can be joined to other
views by using the AssignmentID, ResourceID, TopicType, and StateID columns.

v_UpdateAssignmentStatus

<!-- p.337 -->

Lists the software update deployment assignments, the system resources that have been
targeted, the last compliance state for the deployment, the last enforcement state for
the deployments, the last evaluation state for the deployment, and so on. The view can
be joined to other views by using the AssignmentID, ResourceID,
LastComplianceMessageID, LastEnforcementMessageID, and
LastEvaluationMessageID columns. The LastComplianceMessageID column provides
the state ID for state messages with a topic type of 300. The
LastEnforcementMessageID column provides the state ID for state messages with a
topic type of 301. The LastEvaluationMessageID provides the state ID for state
messages with a topic type of 302.

v_UpdateAssignmentStatus_Live
Lists the software update deployments, the system resources that have been targeted,
the last compliance state for the deployment, the last enforcement state for the
deployments, the last evaluation state for the deployment, and so on. The
v_UpdateAssignmentStatus_Live view contains a subset of information from the
v_UpdateAssignmentStatus view. The view can be joined to other views by using the
AssignmentID, ResourceID, LastComplianceMessageID, LastEnforcementMessageID,
and LastEvaluationMessageID columns. The LastComplianceMessageID column
provides the state ID for state messages with a topic type of 300. The
LastEnforcementMessageID column provides the state ID for state messages with a
topic type of 301. The LastEvaluationMessageID provides the state ID for state
messages with a topic type of 302.

v_Update_ComplianceStatus
Lists the detection state for all software updates that have been scanned for compliance
on Configuration Manager clients, as well as the resource ID of the client, last
enforcement state ID, enforcement source, last status check time, and so on. The view
can be joined to other views by using the CI_ID, ResourceID, Status, and
LastEnforcementMessageID columns. The Status column provides the state ID for state
messages with a topic type of 500. The LastEnforcementMessageID column provides
the state ID for state messages with a topic type of 402.

v_UpdateScanStatus
Lists the Configuration Manager client computers, by resource ID, that have scanned for
software updates compliance and the last scan state, as well as the last scan time, last

<!-- p.338 -->

error code, last Windows Update Agent version, and so on. The view can be joined to
other views by using the ResourceID, UpdateSource_ID, and LastScanState columns.

  ７ Note

  The LastScanState column provides the state ID for state messages with a topic
  type of 501.

v_UpdateState_Combined
Lists the detection state for software updates that are not required on Configuration
Manager client computers or the enforcement state for software updates that are
required on Configuration Manager client computers, as well as the state ID, state time,
enforcement source, and so on. The view can be joined to other views by using the
CI_ID and ResourceID columns.

  ７ Note

  A value of 402 in the StateType column is for enforcement state, and a value of 500
  is for compliance state.

Software updates status summarizer views
The software updates status summarizers produce summaries from software updates
state messages in the Configuration Manager site database. Status summaries are
produced in real time as the summarizers receive state messages from Configuration
Manager clients. The software updates status summarizer views provide summary
information about software updates compliance, deployment evaluation, deployment
enforcement, and scan state. For more information about the status summarizer views,
see Status and Alert Views in Configuration Manager. The software update status views
are described in this section.

v_AssignmentEnforcementSummaryPerUpdateAndState
Lists the software update deployments, by assignment ID, the software updates in the
deployment, by CI_ID, the enforcement state name, the count of Configuration Manager
client computers that are in the enforcement state, and the total count of client
computers that have been targeted for the deployment. The view can be joined to other
views by using the AssignmentID and CI_ID columns.

<!-- p.339 -->

  ７ Note

  The enforcement states listed in this view have a state type of 402.

v_Update_ComplianceSummary
Lists all software updates, by CI_ID, the last time summarization was run, the total count
of client computers, the count of client computers reporting unknown, not applicable,
missing (required), and present (already installed) states, and so on. The view can be
joined to other views by using the CI_ID column.

v_Update_ComplianceSummary_Live
Lists all software updates, by CI_ID, the last time summarization was run, the total count
of client computers, the count of client computers reporting unknown, not applicable,
missing (required), and present (already installed) states, and so on. The view can be
joined to other views by using the CI_ID column.

v_Update_DeploymentSummary_Live
Lists all software updates, by CI_ID, in active software update deployments, listed by
AssignmentID, and summarized state reported by targeted clients. The view includes the
target collection ID and name; the time of the last summarization; the total number of
client computers targeted; the count of client computers reporting unknown, not
applicable, missing (required), and present (already installed) states; the number of
clients that have installed the software update or failed to install the update; and so on.
The view can be joined to other views by using the CI_ID, AssignmentID, and
CollectionID columns.

v_UpdateDeploymentSummary
Lists all software updates, by CI_ID, in software update deployments, listed by
assignment ID, and summarized state reported by targeted clients. The view includes the
target collection ID and name; the time of the last summarization; the total number of
client computers targeted; the count of client computers reporting unknown, not
applicable, missing (required), and present (already installed) states; the number of
clients that have installed the software update or failed to install the update; and so on.
The view can be joined to other views by using the CI_ID, AssignmentID, and
CollectionID columns.

<!-- p.340 -->

  ７ Note

  This view has been deprecated, no longer generates summary data, and may be
  removed in the future.

v_UpdateEnforcementSummaryPerCollection
Lists the summary state for all software updates that have been deployed. The view
provides the software update, by CI_ID, target collection, collection name, and
summarized enforcement state reported by clients in the collection. The view can be
joined to other views by using the CI_ID column.

v_UpdateSummaryPerCollection
Lists the summary state for all software updates and the compliance state per collection.
The view includes the software update, by CI_ID; target collection ID and name; the time
of the last summarization; the total number of client computers targeted; the count of
client computers reporting not applicable, missing (required), present (already installed),
and unknown states; and so on. The view can be joined to other views by using the
CI_ID and CollectionID columns.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.341 -->

Status and alert views in Configuration
Manager
Article • 10/10/2022

Configuration�Manager status messages report information about Configuration
Manager component behavior and data flow and are categorized by severity and type.
State messages are sent by Configuration Manager clients to site systems based on
important changes of state, providing a snapshot of the state of a process at a specific
time. Status summarizers produce summaries of the status and state messages and
provide a snapshot of the status and health of site systems, components, software
updates compliance, and so on.

Status message instances consist of properties that are stored in the database, which are
represented primarily by the v_StatusMessage view, and message strings stored in
dynamic-link library (DLL) files. When you view a message by using the Configuration
Manager console, Status Message Viewer, and the Status Message Details page in
Report Viewer, Configuration Manager creates the instance of status messages by
combining the various parts.

The following sections provide detailed information about status message views, state
message views, and status summarizer views.

Status message views
The status views are described in this section.

v_AdvertisementStatusInformation
Lists all deployment status message IDs, the message state, and the message name,
such as succeeded, expired, failed, and retrying. The view is also listed and described in
the Application Management Views in Configuration Manager topic. The view can be
joined to other advertisement status views by using the MessageID column.

v_ClientAdvertisementStatus
Lists all package and program deployments with the associated status for system
resources that have been targeted. The view is also listed and described in the
Application Management Views in Configuration Manager topic. The view can be joined

<!-- p.342 -->

to other views by using the AdvertisementID, ResourceID, and LastStatusMessageID
columns.

v_ClientMessageStatistics
Lists all Configuration Manager clients, by resource ID, the last time the client sent and
processed a status message, and the last time a resynchronization was issued and
completed on the client. This view can be joined to other views by using the ResourceID
column.

v_DCMClientStatusInformation
Lists all possible compliance settings client states. The view is also listed and described
in the Compliance Settings Views in Configuration Manager topic. It is unlikely that this
view will be joined to other views.

v_PackageStatus
Lists the status for all deployments, as well as the package server location, last update
time, and so on. The view is also listed and described in the Application Management
Views in Configuration Manager topic. The view can be joined to other views by using
the PackageID column.

v_PeerDPStatusInfo
Lists the peer distribution point states and associated state names. It is unlikely that this
view will be joined to other views.

v_ServerMessageStatistics
Lists the site system servers, the associated site code, when the last heartbeat occurred,
and how long the heartbeat took to process. The view is also listed and described in the
Site Administration Views in Configuration Manager topic. The view can be joined to
other views by using the ServerName column.

v_StatMsgAttributes
Lists the attributes for all status messages (for example, package ID, collection ID, user
name, object GUID, and so on). The view can be joined to the v_StatusMessage and
v_StatMsgInsStrings views by using the RecordID column.

<!-- p.343 -->

v_StatMsgInsStrings
Lists the status insertion strings for all status messages. The view can be joined to the
v_StatusMessage and v_StatMsgAttributes views by using the RecordID column.

v_StatMsgModuleNames
Lists the status message module names with associated module DLL name. By default,
Configuration Manager has the SMS Client, SMS Provider, and SMS Server module
names. It is unlikely that this view will be joined to other views.

v_StatusMessage
Lists information about all status messages, including status message ID, time of status
message, severity, site code, and so on. The view can be joined to the
v_StatMsgAttributes and v_StatMsgInsStrings views by using the RecordID column, and
to other views by using the MachineName column.

v_TaskExecutionStatus
Lists the status for operating system deployment task sequence steps, as well as the
advertisement ID, resource ID, action name, and so on. The view is also listed and
described in the Operating System Deployment Views in Configuration Manager topic.
The view can be joined to other views by using the AdvertisementID and ResourceID
columns.

v_WOLCommicationErrorStatus
Lists the Wake on LAN error status messages, as well as the time of the error, batch ID,
object type, ID, and error code. The view is also listed and described in the Wake On
LAN Views in Configuration Manager topic. It is unlikely that this view will be joined to
other views.

v_StatusMessagesAlerts
Lists, by record ID, recently generated alerts. This includes the severity of the alert, the
alert text and more. This view can be joined to other views by using the AlertSeverity,
Name, TypeInstanceID or MachineName columns.

<!-- p.344 -->

State views
The state views list the state messages sent by Configuration Manager clients to site
systems and can generally be joined to system data, other state message views,
deployment views, and more. The Configuration Manager states are listed in the
v_StateNames view. When creating reports by using state views, you will likely want to
join the v_StateNames view with another state view by using the StateType and StateID
columns to retrieve the friendly names for the state and to use the v_StateNames view
to determine the criteria to filter the SQL statement. Each state message type has
multiple state IDs, which start at 1 for each message type. When joining to a view that
contains information for more than one state type, you will need to either join to the
other view by using both the StateType and StateID columns or join to the other view
by using the StateID column and filter the query with for the specific StateType. For
example, if you join to another view by using the StateID column, you could filter the
results by StateType=300.

v_AssignmentState_Combined
Lists the last state message received from Configuration Manager client computers for
assigned software update deployments, including the assignment ID (deployment ID),
resource ID, state type, and so on. The view is also listed and described in the Software
Updates Views in Configuration Manager topic. The view can be joined to other views
by using the AssignmentID, ResourceID, StateType, and StateID columns.

v_AssignmentStatePerTopic
Lists the last state message for each state type received from Configuration Manager
client computers for assigned software update deployments, including assignment ID
(deployment ID), resource ID, state type, and so on. The view is also listed and described
in the Software Updates Views in Configuration Manager topic. The view can be joined
to other views by using the AssignmentID, ResourceID, TopicType, and StateID
columns.

v_CIAssignmentStatus
Lists the enforcement and evaluation state messages received from Configuration
Manager client computers for all assigned configuration items, including assigned
software update deployments and assigned configuration baselines. The assignment ID,
resource ID, the last enforcement state message ID, the last evaluation state message ID,
and so on are provided. The view is also listed and described in the Compliance Settings

<!-- p.345 -->

Views in Configuration Manager topic. The view can be joined to other views by using
the AssignmentID, ResourceID, LastEnforcementMessageID, and
LastEvaluationMessageID columns. The LastEnforcementMessageID column provides
the state ID for state messages with a topic type of 402. The LastEvaluationMessageID
column provides the state ID for state messages with a topic type of 400.

v_CIComplianceHistory
Lists the configuration items, by CI_UniqueID and CI_ID, that are configuration baselines
or configuration items within a configuration baseline, that have been assigned to a
Configuration Manager client, listed by ResourceID, and compliance information for the
configuration item. The information includes the compliance start and end dates,
whether the configuration item is applicable to the client, whether the client is
compliant for the configuration item, and so on. The view is also listed and described in
the Compliance Settings Views in Configuration Manager topic. The view can be joined
to other views by using the CI_UniqueID, CI_ID, and ResourceID columns.

v_CIComplianceStatusDetail
Lists the configuration items, by CI_ID and CI_UniqueID, that are in a configuration
baseline, have been assigned to a Configuration Manager client, listed by ResourceID,
and have a state value of Non-Compliant. The view is also listed and described in the
Compliance Settings Views in Configuration Manager topic. The view can be joined to
other views by using the CI_ID, CI_UniqueID, ResourceID, and ModelName columns.

v_CICurrentComplianceStatus
Lists the compliance and enforcement states for configuration items, by configuration
item ID, as well as the resource ID, whether the configuration item is applicable to the
resource, and information related to the compliance and evaluation of the configuration
item. The view is also listed and described in the Compliance Settings Views in
Configuration Manager topic. The view can be joined to other views by using the CI_ID,
ResourceID, CI_UniqueID, ModelName, ComplianceState, and
LastEnforcementMessageID columns. The ComplianceState column provides the state
ID for state messages with a topic type of 401. The LastEnforcementMessageID column
provides the state ID for state messages with a state message topic type of 402.

v_ClientDeploymentState

<!-- p.346 -->

Lists all Configuration Manager clients, by SMSID, and the last client deployment state
reported, as well as the fully qualified domain name (FQDN), NetBIOS name, assigned
site code, client version, and so on. The view is also listed and described in the Client
Deployment Views in Configuration Manager topic. The view can be joined to other
views by using the SMSID, FQDN, NetBiosName, and LastMessageStateID columns. The
LastMessageStateID column contains the state ID for topic type 800. The Configuration
Manager states are listed in the v_StateNames view.

v_ClientHealthState
Lists all Configuration Manager clients, by SMSID, the last client health state reported for
each state type, the fully qualified domain name (FQDN), NetBIOS name, assigned site
code, health type, health state, health state name, and so on. The view is also listed and
described in the Client Status Views in Configuration Manager topic. The view can be
joined to other views by using the SMSID, FQDN, NetBiosName, HealthType, and
HealthState columns. The HealthType column contains the topic type and the
HealthState column contains the state ID. Client health state messages have a state type
from 1000 to 1004. The Configuration Manager states are listed in the v_StateNames
view.

v_DeviceClientDeploymentState
Lists all Configuration Manager mobile device clients, by device client ID, NetBIOS name,
and device ID, and the last device deployment state reported, as well as the assigned
site code, device client version, and so on. The view is also listed and described in the
Mobile Device Management Views in Configuration Manager and Client Deployment
Views in Configuration Manager topics. The view can be joined to other views by using
the DeviceClientID, which contains the same information as the
SMS_Unique_Identifier0 column in the v_R_System view, DeviceNetBiosName, and
DeviceDeploymentState columns. The DeviceDeploymentState column contains the
state ID for topic type 800. The Configuration Manager states are listed in the
v_StateNames view.

v_DeviceClientHealthState
Lists all Configuration Manager mobile device clients, by device client ID, NetBIOS name,
and device ID, and the health state of the device, as well as the assigned site code,
owner name, and so on. The view is also listed and described in the Mobile Device
Management Views in Configuration Manager and Client Status Views in Configuration
Manager topics. The view can be joined to other views by using the DeviceClientID,

<!-- p.347 -->

which contains the same information as the SMS_Unique_Identifier0 column in the
v_R_System view, DeviceNetBiosName, DeviceID, HealthType, and HealthState
columns. The HealthType column contains the topic type and the HealthState column
contains the state ID. Client health state messages have a state type from 1000 to 1004.
The Configuration Manager states are listed in the v_StateNames view.

v_StateNames
Lists all states that can be reported by Configuration Manager clients by topic type, state
ID, state name, and state description. Each state topic type defines a specific function,
and each topic type contains multiple state IDs. The view can be joined to other views
by using the TopicType and StateID columns.

v_Update_ComplianceStatusAll
Lists the detection state for all software updates that have been scanned for compliance
on Configuration Manager clients, as well as the resource ID of the client, last
enforcement state ID, enforcement source, last status check time, and so on. The
v_Update_ComplianceStatusAll view combines information from the
v_Update_ComplianceStatusReported and v_UpdateComplianceStatus_Unknown
views. The view is also listed and described in the Software Updates Views in
Configuration Manager topic. The view can be joined to other views by using the CI_ID,
ResourceID, Status, and LastEnforcementMessageID columns. The Status column
provides the state ID for state messages with a topic type of 500. The
LastEnforcementMessageID column provides the state ID for state messages with a
topic type of 402.

v_Update_ComplianceStatusReported
Lists the detection state for all software updates that have been scanned for compliance
on Configuration Manager clients, as well as the resource ID of the client, last
enforcement state ID, enforcement source, last status check time, and so on. The
v_Update_ComplianceStatusReported view combines information from the
v_UpdateComplianceStatus and v_UpdateComplianceStatus_NotApplicable views. The
view is also listed and described in the Software Updates Views in Configuration
Manager topic. The view can be joined to other views by using the CI_ID, ResourceID,
Status, and LastEnforcementMessageID columns. The Status column provides the state
ID for state messages with a topic type of 500. The LastEnforcementMessageID column
provides the state ID for state messages with a topic type of 402.

<!-- p.348 -->

v_UpdateAssignmentStatus
Lists the software update deployment assignments, the system resources that have been
targeted, the last compliance state for the deployment, the last enforcement state for
the deployments, the last evaluation state for the deployment, and so on. The view is
also listed and described in the Software Updates Views in Configuration Manager topic.
The view can be joined to other views by using the AssignmentID, ResourceID,
LastComplianceMessageID, LastEnforcementMessageID, and
LastEvaluationMessageID columns. The LastComplianceMessageID column provides
the state ID for state messages with a topic type of 300. The
LastEnforcementMessageID column provides the state ID for state messages with a
topic type of 301. The LastEvaluationMessageID provides the state ID for state
messages with a topic type of 302.

v_UpdateAssignmentStatus_Live
Lists the software update deployment assignments, the system resources that have been
targeted, the last compliance state for the deployment, the last enforcement state for
the deployments, the last evaluation state for the deployment, and so on. The
v_UpdateAssignmentStatus_Live view contains a subset of information from the
v_UpdateAssignmentStatus view. The view is also listed and described in the Software
Updates Views in Configuration Manager topic. The view can be joined to other views
by using the AssignmentID, ResourceID, LastComplianceMessageID,
LastEnforcementMessageID, and LastEvaluationMessageID columns. The
LastComplianceMessageID column provides the state ID for state messages with a topic
type of 300. The LastEnforcementMessageID column provides the state ID for state
messages with a topic type of 301. The LastEvaluationMessageID provides the state ID
for state messages with a topic type of 302.

v_UpdateComplianceStatus
Lists the detection state for all software updates that have been scanned for compliance
on Configuration Manager clients, as well as the resource ID of the client, last
enforcement state ID, enforcement source, last status check time, and so on. The view is
also listed and described in the Software Updates Views in Configuration Manager topic.
The view can be joined to other views by using the CI_ID, ResourceID, Status, and
LastEnforcementMessageID columns. The Status column provides the state ID for state
messages with a topic type of 500. The LastEnforcementMessageID column provides
the state ID for state messages with a topic type of 402.

<!-- p.349 -->

v_UpdateScanStatus
Lists the Configuration Manager client computers, by resource ID, that have scanned for
software updates compliance and the last scan state, as well as the last scan time, last
error code, last Windows Update Agent version, and so on. The view is also listed and
described in the Software Updates Views in Configuration Manager topic. The view can
be joined to other views by using the ResourceID, UpdateSource_ID, and LastScanState
columns.

  ７ Note

  The LastScanState column provides the state ID for state messages with a topic
  type of 501.

v_UpdateState_Combined
Lists the detection state for software updates that are not required on Configuration
Manager client computers and the enforcement state for software updates that are
required on Configuration Manager client computers, as well as the state ID, state time,
enforcement source, and so on. The view is also listed and described in the Software
Updates Views in Configuration Manager topic. The view can be joined to other views
by using the CI_ID, ResourceID, StateType, and StateID columns.

  ７ Note

  A value of 402 in the StateType column is for enforcement state, and a value of 500
  is for software update detection state.

Status summarizer views
Status summarizers produce summaries from status messages, state messages, and
other data in the Configuration Manager site database. Status summaries are produced
in real time as the summarizers receive status and state messages from Configuration
Manager components and clients. You can use status summarizers to view a snapshot of
the status and health of the site systems, components, deployments, software updates
compliance, client health, and so on.

Data in a status summary is classified as either a count or a state. A count is a tally of
events that occurs over a specific period of time, such as the number of error status

<!-- p.350 -->

messages reported by a component since the beginning of the week. A state is the last
known condition of something, such as the number of free bytes that is available for the
Configuration Manager site database.

Each of the status summaries contains some state data. Only the component status and
advertisement status summaries contain count data. The status summarizer views
contain data such as the number of information, warning, and error messages for a site
within a specified interval and the state of all components in a site at a specified interval.

Each of the status message summarizer views are listed and described in this section.

v_AssignmentEnforcementSummaryPerUpdateAndState
Lists the software update deployments, by assignment ID, the software updates in the
deployment, by CI_ID, the enforcement state name, the count of Configuration Manager
client computers that are in the enforcement state, and the total count of client
computers that have been targeted for the deployment. The view is also listed and
described in the Software Updates Views in Configuration Manager topic. The view can
be joined to other views by using the AssignmentID and CI_ID columns.

  ７ Note

  The enforcement states listed in this view have a state type of 402.

v_AssignmentSummaryPerTopic
Lists the assignments, by assignment ID, the type of assignment state message, the state
ID for the type, the count of Configuration Manager client computers that are in the
assignment state, and the total count of client computers that have been targeted for
the assignment. The view is also listed and described in the Compliance Settings Views
in Configuration Manager topic. The view can be joined to other views by using the
AssignmentID column.

  ７ Note

  There are three deployment assignment states. State type of 300 is assignment
  compliance, type 301 is assignment enforcement, and type 302 is assignment
  evaluation. You can find a list of the state IDs by looking in the v_StateNames view.

v_CH_ClientSummary

<!-- p.351 -->

Lists summarized client status information for all Configuration Manager client
computers, such as last heartbeat discovery, last hardware and software inventory scan,
last policy request, whether there are possible certificate issues, and so on. The view is
also listed and described in the Client Status Views in Configuration Manager topic. The
view can be joined to other views by using the MachineID, NetBiosName, and SiteCode
columns.

v_CH_ClientSummaryHistory
Lists a summarization of the client status information for all Configuration Manager
client computers, such as total number of clients, total number of clients that are active
based on the last heartbeat discovery, hardware and software inventory scans, and so
on. The view is also listed and described in the Client Status Views in Configuration
Manager topic. It is unlikely that this view will be joined to other views.

v_CIComplianceSummary
Lists the compliance settings configuration baselines, by CI_ID, and the count of
Configuration Manager client computers that have been targeted, how many clients are
compliant, how many have failed the compliance evaluation, the count of client
computers that are noncompliant, and so on. The view is also listed and described in the
Compliance Settings Views in Configuration Manager topic. The view can be joined to
other views by using the CI_ID and CI_UniqueID columns.

v_ClientOfferSummary
Lists the standard package and program deployments, by OfferID, the count of
Configuration Manager client computers that have been targeted, and the count of
computers reporting not started, waiting, running, retrying, failed, and succeeded status
for the deployment. The view is also listed and described in the Application
Management Views in Configuration Manager topic. The view can be joined to other
views by using the OfferID and PkgID columns.

v_ComponentSummarizer
Lists summary status information for all Configuration Manager components for
different intervals. The view also provides the site code, server name, component name,
the count of information, warning, and error messages, and so on. The information in
this view contains the same information that is displayed in the Component Status node
of the Configuration Manager console, but the view contains information for all display

<!-- p.352 -->

intervals. The view is also listed and described in the Site Administration Views in
Configuration Manager topic.

  ７ Note

  The value in the Status column provides the current status for the component. A
  value of 0 indicates that the component is OK, a value of 1 indicates a warning state
  for the component, and a value of 2 indicates a critical state for the component.

The view can be joined to other views by using the SiteCode, MachineName, and
ComponentName columns.

v_FileUsageSummary
Lists software metering summary status information for file usage by site. The view is
also listed and described in the Software Metering Views in Configuration Manager
topic. The view can be linked by using the FileID column.

v_FileUsageSummaryIntervals
Lists software metering summary interval information for file usage. The view is also
listed and described in the Software Metering Views in Configuration Manager topic. It
is unlikely that this view will be joined to other views.

v_INSTALLED_SOFTWARE_DATA_Summary
Lists the count of the installed software applications on Configuration Manager clients
found through Asset Intelligence. This view contains the same source information as the
v_GS_INSTALLED_SOFTWARE view, but provides summary information instead of listing
the individual system resources. The view is also listed and described in the Asset
Intelligence Views in Configuration Manager topic. It is unlikely that this view will be
joined to other views.

v_MonthlyUsageSummary
Lists the Configuration Manager client computers, by ResourceID, and the usage
summary for metered files, as well as the logged-on user name, usage time, and time of
last usage. The view is also listed and described in the Software Metering Views in
Configuration Manager topic. The view can be joined to other views by using the
ResourceID, FileID, and MeteredUserID columns.

<!-- p.353 -->

v_PackageStatusDetailSumm
Lists all applications, task sequences, and packages and programs, by PackageID, the
originating site code, package name, site name, source version, the date for the
summary information, the targeted count for each package, and the count for installed,
retrying, and failed status. The view is also listed and described in the Application
Management Views in Configuration Manager topic. The view can be joined to other
views by using the PackageID column.

v_PackageStatusDistPointSumm
Lists all content packages, by PackageID, and the installation status for the package
source files on all associated distribution points. The view also provides information
such as the site code, path to the distribution point, path to source location, time of last
copy, and so on. The view is also listed and described in the Application Management
Views in Configuration Manager topic. The view can be joined to other views by using
the PackageID and ServerNALPath columns.

v_PackageStatusRootSummarizer
Lists all applications, task sequences, and packages and programs, by PackageID, the
package name, source version, source date, the source site, size of the source files, the
targeted count for each package, and the count for installed, retrying, and failed status.
The view is also listed and described in the Application Management Views in
Configuration Manager topic. The view can be joined to other views by using the
PackageID column.

v_SiteDetailSummarizer
Lists status summary information for all Configuration Manager sites, by SiteCode, for
different intervals. The view also provides the site name, site version, interval, the count
of information, warning, and error messages, and so on. The information in this view
contains the same information that is displayed in the Site Status node of the
Configuration Manager console, but the view contains information for all display
intervals. The view is also listed and described in the Site Administration Views in
Configuration Manager topic. The view can be joined to other views by using the
SiteCode column.

  ７ Note

<!-- p.354 -->

  The value in the Status column provides the current status for the site. A value of 0
  indicates that the site is OK, a value of 1 indicates a warning state for the site, and a
  value of 2 indicates a critical state for the site.

v_SiteSystemSummarizer
Lists status summary information for all Configuration Manager sites systems for
different intervals. The view also provides the object location, the site role for the site
system, total disk space, free disk space, and percentage of free disk space for the site
system, the time of the last status reported, and whether the site system is available. The
information in this view contains the same information that is displayed in the Site
System Status node of the Configuration Manager console. The view is also listed and
described in the Site Administration Views in Configuration Manager topic. The view can
be joined to other views by using the SiteCode column.

v_SummarizationInterval
Lists the status summarization interval. It is unlikely that this view will be joined to other
views.

v_SummarizerRootStatus
Lists the root summary status, which is the same status displayed on the System Status
node of the Configuration Manager console. It is unlikely that this view will be joined to
other views.

v_SummarizerSiteStatus
Lists the site summary status, which is the same status displayed for the <site code> -
<site name> node of the Configuration Manager console. The view is also listed and
described in the Site Administration Views in Configuration Manager topic. The view can
be joined to other views by using the SiteCode column.

v_SummaryTasks
Lists the tasks, by name and command, used to summarize Configuration Manager
information, as well as the run interval, last run duration, when the task last completed
successfully, next start time, and so on. It is unlikely that this view will be joined to other
views.

<!-- p.355 -->

v_Update_ComplianceSummary
Lists all software updates, by CI_ID, the last time summarization was run, the total count
of client computers, the count of client computers reporting unknown, not applicable,
missing (required), and present (already installed) states, and so on. The view is also
listed and described in the Software Updates Views in Configuration Manager topic. The
view can be joined to other views by using the CI_ID column.

v_Update_ComplianceSummary_Live
Lists all software updates, by CI_ID, the last time summarization was run, the total count
of client computers, the count of client computers reporting unknown, not applicable,
missing (required), and present (already installed) states, and so on. The view is also
listed and described in the Software Updates Views in Configuration Manager topic. The
view can be joined to other views by using the CI_ID column.

v_Update_DeploymentSummary_Live
Lists all software updates, by CI_ID, in active software update deployments, listed by
AssignmentID, and summarized state reported by targeted clients. The view includes the
target collection ID and name; the time of the last summarization; the total number of
client computers targeted; the count of client computers reporting unknown, not
applicable, missing (required), and present (already installed) states; the number of
clients that have installed the software update and failed to install the update; and so
on. The view is also listed and described in the Software Updates Views in Configuration
Manager topic. The view can be joined to other views by using the CI_ID, AssignmentID,
and CollectionID columns.

v_UpdateDeploymentSummary
Lists all software updates, by CI_ID, in software update deployments, listed by
AssignmentID, and summarized state reported by targeted clients. The view includes
the target collection ID and name; the time of the last summarization; the total number
of client computers targeted; the count of client computers reporting unknown, not
applicable, missing (required), and present (already installed) states; the number of
clients that have installed the software update and failed to install the update; and so
on. The view is also listed and described in the Software Updates Views in Configuration
Manager topic. The view can be joined to other views by using the CI_ID, AssignmentID,
and CollectionID columns.

<!-- p.356 -->

  ７ Note

  This view has been deprecated, no longer generates summary data, and may be
  removed in the future.

v_UpdateEnforcementSummaryPerCollection
Lists the summary state for all software updates that have been deployed. The view
provides the software update, by CI_ID, target collection, collection name, and
summarized enforcement state reported by clients in the collection. The view is also
listed and described in the Software Updates Views in Configuration Manager topic. The
view can be joined to other views by using the CI_ID column.

v_UpdateSummaryPerCollection
Lists the summary state for all software updates and the compliance state per collection.
The view includes the software update, by CI_ID; target collection ID and name; the time
of the last summarization; the total number of client computers targeted; the count of
client computers reporting not applicable, missing (required), present (already installed),
and unknown states; and so on. The view is also listed and described in the Software
Updates Views in Configuration Manager topic. The view can be joined to other views
by using the CI_ID and CollectionID columns.

Alert views
The alerts views are listed in this section.

v_Alert
Lists information about the events than can be generated by Configuration Manager.
This includes the severity of the alert, when it was created, and who created it. This view
can be joined to other views by using the Name and Severity columns.

v_AlertEvents
Lists information about the events that have been triggered on the Configuration
Manager site. This view can be joined to other views by using the AlertID and
EventMachineID columns.

<!-- p.357 -->

v_AlertValidFeatureArea
Lists information about each product component, by feature area ID, that might
generate alerts. It is unlikely that this view will be joined to other views.

v_AlertVariable_G
Lists system information about variables that are assigned to alerts. It is unlikely that this
view will be joined to other views.

v_SMS_Alert
Lists information about the built-in, and user created alerts that might be displayed in
the Configuration Manager console. It is unlikely that this view will be joined to other
views.

v_Report_StatusMessageDetail
Lists detailed information about status messages returned by each Configuration
Manager component. This includes the record ID, the time of the status message, the
component that generated the message, and more. This view can be joined to other
views by using the RecordID column.

v_StateMessageStatistics
Lists information about the number of state messages returned for each topic type. It is
unlikely that this view will be joined to other views.

v_StatMsgWithInsStrings
Lists detailed information about status messages returned by each Configuration
Manager component. This includes the record ID, the time of the status message, the
component that generated the message, and more. This view can be joined to other
views by using the RecordID column.

See also
SQL Server views in Configuration Manager

<!-- p.358 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.359 -->

Wake On LAN views in Configuration
Manager
Article • 10/10/2022

The Configuration�Manager Wake On LAN views contain information about the
objects, such as application management, software updates, and task sequence
deployments, that have Wake On LAN enabled, as well as the clients that are Wake On
LAN enabled, and clients that have deployments that are Wake On LAN enabled. There
is also a status view that contains information about the Wake On LAN error messages
that have been reported. Most often, the Wake On LAN views will be joined to discovery
views by using the ResourceID column, and to application management and compliance
settings views by using the ObjectID column.

The following sections provide detailed information about Wake On LAN views and the
Wake On LAN status view.

Wake On LAN views
The Wake On LAN views are described in this section.

v_WOLClientTimeZones
Lists the time zone offsets for all Wake On LAN�enabled clients. It is unlikely that this
view will be joined with other views.

v_WOLCommunicationHistory
Lists the Wake On LAN communication history, including the message description, time
of the communication, status message attribute, and so on. The BatchID, ObjectType,
and ID columns contain status message attributes, such as a deployment ID or unique
configuration item ID. The view can be joined to other views by using the BatchID,
ObjectType, and ID columns.

v_WOLEnabledAdvertisements
Lists the software deployments, by name and advertisement ID that have Wake On LAN
enabled. The ObjectType value for software deployment is 1, the ObjectName column
contains the name of the advertisement, and the ObjectID column contains the

<!-- p.360 -->

advertisement ID of the advertisement. The view can be joined to other views by using
the ObjectID column.

v_WOLEnabledAssignments
Lists the software update deployments, by name and unique deployment ID that have
Wake On LAN enabled. The ObjectType value for software updates is 2, the
ObjectName column contains the name of the deployment, and the ObjectID column
contains the unique assignment ID of the deployment. The view can be joined to other
views by using the ObjectID column.

v_WOLEnabledObjects
Lists the objects, by name and object ID, that have Wake On LAN enabled, as well as the
object type. For example, a software update deployment that has Wake On LAN enabled
will be listed with an ObjectType=2, the deployment name will be listed in the
ObjectName column, and the assignment unique ID will be listed in the ObjectID
column. The view can be joined to other views by using the ObjectID column and to the
v_WOLGetSupportedObjects view by using the ObjectType column.

v_WOLEnabledTaskSequences
Lists the task sequence advertisements, by object type, name and ID that have Wake On
LAN enabled. The ObjectType value for task sequence is 3, the ObjectName column
contains the name of the task sequence advertisement, and the ObjectID column
contains the advertisement ID of the task sequence advertisement. The view can be
joined to other views by using the ObjectID column.

v_WOLGetPendingObjectSchedules
Lists the objects, by the object ID that are scheduled for mandatory assignment,
including the object type, target collection, schedule, and so on. The view can be joined
to other views by using the Object column, which is the same as the ObjectID columns
in other Wake On LAN views, and to the v_WOLGetSupportedObjects view by using the
ObjectType column.

v_WOLGetSupportedObjects
Lists the Wake On LAN object types, by object type and object name. For example,
object type 1 is for software distribution, object type 2 is for software updates, and
