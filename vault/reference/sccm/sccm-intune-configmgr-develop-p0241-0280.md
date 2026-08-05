---
title: "Configuration Manager SDK documentation — pages 241-280"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0241-0280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0241-0280
family: sccm
documentKind: "doc"
abstract: "Lists configuration items that have associated content, by CI_ID, the configuration item ID for the configuration item in which the content is associated, the content ID, whether the content has been provisioned, and so on. The configuration item ID for a configuration item bund"
---

# Configuration Manager SDK documentation — pages 241-280

<!-- p.241 -->

Lists configuration items that have associated content, by CI_ID, the configuration item
ID for the configuration item in which the content is associated, the content ID, whether
the content has been provisioned, and so on. The configuration item ID for a
configuration item bundle is listed multiple times in the CI_ID column, and the
configuration item IDs for the configuration items that are part of the bundle are listed
in the ContentCI_ID column. For example, a configuration item that is not a bundle
would have the same configuration item ID in the CI_ID and ContentCI_ID columns. A
bundle configuration item would have one listing with the configuration item ID in the
CI_ID column and the same configuration item ID in the ContentCI_ID columns, and
then new listings would contain the configuration item ID for the bundle configuration
item in the CI_ID column and the configuration item ID for the bundled configuration
items in the ContentCI_ID column. The ContentLevel column represents how many
times a configuration item ID is listed in the ContentCI_ID column. The view can be
joined to other views by using the CI_ID, ContentCI_ID, and Content_ID columns.

v_CICurrentSettingsComplianceStatusDetail
Lists the configuration items, by CI_ID, that are in a configuration baseline, that have
been assigned to Configuration Manager clients, and are reporting a validation error or
noncompliance. The information includes the NetBIOS name of the client, configuration
item name, setting name, setting type, setting description, constraint name, constraint
description, and validation rule. The view can be joined to other views by using the CI_ID
and ResourceID columns.

v_CIEULA_LocalizedContent
Lists the configuration items, by CI_ID, that have associated license terms, as well as the
locale ID, the content unique ID for the license terms, the license terms text, and the
source site. The view can be joined to other views by using the CI_ID column.

v_CIRelation
Lists configuration items, by configuration item ID in the FromCIID column, the
configuration items that are related to the first configuration item, by configuration item
ID in the TOCIID column, and the type of relation. Configuration items with a bundle
level of 1 are listed in the ToCIID column. For example, if the configuration item ID for
an update bundle is listed in the FromCIID column and another update bundle is part of
the first bundle, only the configuration item ID for the update bundle will be listed in the
ToCIID column and not the software updates that are part of the second update bundle.
The view can be joined to other views by using the FromCIID, ToCIID, and RelationType

<!-- p.242 -->

columns. The FromCIID column in this view contains the same information as the CI_ID
column, and the ToCIID column contains the same information as the ReferencedCI_ID
column in the v_CIRelation_All view.

  ７ Note

  The configuration item relation types can be retrieved from the v_CIRelationTypes
  view.

v_CIRelation_All
Lists the relationships between configuration items, by CI_ID, and other configuration
items, by ReferencedCI_ID, as well as how deep the relationship is between the
configuration items, by level. The CI_ID column lists the configuration item to which the
configuration item in the ReferencedCI_ID is related, such as a software updates bundle
and associated software updates that are part of the bundle or a configuration baseline
and the associated configuration items that are part of the baseline. Configuration items
are also listed with a relationship to themselves, which is indicated by a value of 0. For
example, the configuration item ID for an update bundle is listed in the CI_ID column,
the same configuration item ID is listed in the ReferencedCI_ID column, and the Level is
0. In a different row, a configuration item ID for a different update bundle is listed in the
CI_ID column, the configuration item ID for the same software update that was part of
the previous update bundle is listed in the ReferencedCI_ID column because it is also
part of this update bundle, and the Level is 1. In a different row, a configuration item ID
for an update list is listed in the CI_ID column, the configuration item ID for the same
software update that was part of the previous update bundle is listed in the
ReferencedCI_ID column because it is also part of this update list, and the Level is 3. The
view can be joined to other views by using the CI_ID and ReferencedCI_ID columns. The
CI_ID column in this view is the same as the FromCIID column, and the ReferencedCI_ID
column is the same as the ToCIID column in the v_CIRelation and v_CIRelationEx views.

  ７ Note

  The configuration item relation types can be retrieved from the v_CIRelationTypes
  view.

v_CIRelationEx

<!-- p.243 -->

Lists the relationships between configuration items, by FromCIID, TOCIID, RelationType,
and RelationDepth. The FromCIID column is the configuration item to which the
configuration item in the ToCIID is related, such as a software updates bundle and
associated software updates that are part of the bundle or a configuration baseline and
the associated configuration items that are part of the baseline. The RelationType
column indicates the type of relationship between the configuration items, and the
RelationDepth column indicates how deep the relationship is for a configuration item
listed in the ToCIID column. This view does not display configuration items with a
RelationDepth of 0, which is the relationship of the configuration item to itself. For
example, if the configuration item ID for an update bundle is listed in the FromCIID
column and the configuration item ID for a software update that is part of the bundle is
listed in the ToCIID column. The RelationType in this case is 1 (Bundled), and the
RelationDepth is 1. In the next row, a configuration item ID for an update bundle that
also contains the previous update is listed in the FromCIID column, the same
configuration item ID for the update is listed in the FromCIID column, the RelationType
is still 1, and the RelationDepth is now 2. In the next row, a configuration item ID for an
update list that contains the same update is listed in the FromCIID column, the same
configuration ID for the update is listed in the FromCIID column, the RelationType is still
1, and the RelationDepth is now 3. The view can be joined to other views by using the
FromCIID, ToCIID, and RelationType columns. The FromCIID column in this view
contains the same information as the CI_ID column, and the ToCIID column contains the
same information as the ReferencedCI_ID column in the v_CIRelation_All view.

  ７ Note

  The configuration item relation types can be retrieved from the v_CIRelationTypes
  view.

v_CIRelationTypeMapping
Lists the configuration item elements, such as configuration baselines and software
updates, the relation type value, and a description for the relation type. The view can be
joined to other compliance settings views by using the RelationType column.

v_CIRelationTypes
Lists the relation type values, a description for the relation type, and whether the
relation type is recursive. The view can be joined to other compliance settings views by
using the RelationType column.

<!-- p.244 -->

v_CITargetedCollections
Lists configuration items, by CI_ID, and the collection that the configuration item
targets, by LocalCollectionID, CollectionID, and CollectionName. The view can be
joined to other compliance settings views by using the CI_ID, LocalCollectionID, and
CollectionID columns.

v_CITargetedMachines
Lists configuration items, by CI_ID, and the Configuration Manager clients that the
configuration item targets, by ResourceID. The view can be joined to other views by
using the CI_ID and ResourceID columns.

v_CITypes
Lists the configuration item types, by CIType_ID, and the type name. For example,
software updates have a CIType_ID of 1, configuration baselines have a CIType_ID of 2,
and so on. The view can be joined to other views by using the CIType_ID column, but it
is more likely that this view will be used as a reference when filtering configuration item
data retrieved from configuration item views in the report SQL statement.

v_CIValidationSeverity
Lists the possible configuration item validation severities, by severity, and a description,
such as Informational, Warning, and Error. It is unlikely that this view will be joined to
other views, but it can be used as a reference when filtering configuration item data
retrieved from configuration item views in the report SQL statement.

v_ConfigurationItems
Lists the configuration items in the Configuration Manager site hierarchy, by CI_ID and
CI_UniqueID, and details about the configuration item such as configuration item type
ID, configuration item version, date the configuration item was created and last
modified, whether it is part of a bundle, whether it is a hidden configuration item,
whether it has been deployed, whether it is enabled, the source site for the
configuration item, and so on. When creating SQL statements for the desired
configuration management, software updates, and operating system deployment
features, this view will most often be joined to other views when creating the report SQL
statement. The view can be joined to other views by using the CI_ID, CI_UniqueID,
ModelName, SDMPackage_ID, and CIType_ID columns.

<!-- p.245 -->

v_LocalizedCategories
Lists the configuration item category instances in the Configuration Manager site
hierarchy, by CategoryInstanceID and CategoryInstanceName, and the locale for the
category instance. Category instances consist of languages, update categories, products,
product families, custom categories for desired configuration management, and so on.
The view can be joined to other views by using the CategoryInstanceID column.

v_LocalizedCategories_SiteLoc
Lists the configuration item category instances for the local Configuration Manager site,
by CategoryInstanceID and CategoryInstanceName, the locale that the category
instance is for, and the localized category instance name, which is the locale and
category instance name combined. Category instances consist of languages, update
categories, products, product families, custom categories for desired configuration
management, and so on. The view can be joined to other views by using the
CategoryInstanceID column.

v_LocalizedCIProperties
Lists the configuration items in the Configuration Manager site hierarchy, by CI_ID, that
contain localized properties, such as the display name, description, and informative URL
for a software update. The view can be joined to other views by using the CI_ID column.

v_LocalizedCIProperties_SiteLoc
Lists the configuration items for the local Configuration Manager site, by CI_ID, that
contain localized properties, such as the localized properties for a software update. The
information includes the locale ID, display name, description, and configuration item
informative URL. The view can be joined to other views by using the CI_ID column.

v_SDMErrorCategories
Lists the SDM error categories, by Category, and the description for the error. It is
unlikely that this view will be joined to other views.

v_SDMLocalizedData_SiteLoc
Lists the SDM packages, by ModelName, the SDM package version, the localeID for the
data in the SDM package, and the localized data in XML format. The view can be joined

<!-- p.246 -->

to other views by using the ModelName column.

v_SMSConfigurationItems
This view can be joined to other views by using the CI_ID and ModelID columns.

v_CIRules
Lists all rules that have been created in the Configuration Manager site. Includes the rule
name, ID, and description. This view can be joined to other views by using the CI_ID
column.

v_CIRulesAll
Lists all configuration item rules that are currently being used in the Configuration
Manager site. This view can be joined to other views by using the CI_ID column.

v_CISettingReferences
Lists all settings that are currently deployed in the Configuration Manager site. This view
can be joined to other views by using the CI_ID column.

v_CISettings
Lists all available settings that can be used in the Configuration Manager site. This view
can be joined to other views by using the CI_ID column.

v_CIToContent
Lists, by CI_ID, any content packages that are associated with a configuration item. This
view can be joined to other views by using the CI_ID and Content_UniqueID columns.

v_CIComplianceStatusErrorDetail
Lists, by CI_ID, information about the last compliance message returned by clients that
evaluated the configuration item for compliance. This includes the time the last message
was received and information about settings contained in the configuration item. This
view can be joined to other views by using the CI_ID column.

v_CIComplianceStatusReificationDetail

<!-- p.247 -->

Lists, by model ID instances where Configuration Manager remediated settings on client
devices. This includes the settings ID and the value of the setting before and after it was
remediated. This view can be joined to other views by using the ModelID column.

v_CIConfigPointTypes
Lists the different system configuration point types by type and name. It is unlikely that
this view will be joined to other views.

v_CIConflictCode
Lists the various error codes and descriptions that might be returned when
configuration data contains conflicting settings. It is unlikely that this view will be joined
to other views.

v_CIContentPackage
Lists each configuration item together with the ID of any associated packages. This view
can be joined to other views by using the CI_ID, or PkgID columns.

v_SMS_CIRelation
Lists, by FromCIID, the relationships between configuration items. It is unlikely that this
view will be joined to other views.

v_SMSCICurrentComplianceStatus
Lists compliance information for each configuration item that has been deployed. This
includes whether the configuration item is applicable, it's version, the last time it
reported about compliance, and more. This view can be joined to other views by using
the CI_CurrentComplianceStatusID column.

v_CI_CurrentErrorDetails
Lists, by record ID, the configuration items that have generated an error when they were
evaluated for compliance. This includes the error type, information about the setting,
and the error code. This view can be joined to other views by using the CI_ID column.

v_CIAppDependenceRelations

<!-- p.248 -->

Lists information about the application dependencies that are currently active in
deployment types. It is unlikely that this view will be joined to other views.

v_CIAssignmentToGroup
No description.

v_CIComplianceStatusComplianceDetail
Lists, by CI_ID, deployed configuration items, and the compliance status of each setting
in the configuration item. This view can be joined to other views by using the CI_ID
column.

v_CIComplianceStatusConflictsDetail
Lists details about conflicts that were found when configuration item settings and rules
were evaluated for compliance. This includes the time of the last status, information
about the settings and rules, and the conflict error code. This view can be joined to
other views by using the ResourceID column.

v_CICurrentRuleDetail
Lists, by record ID, the current compliance status of configuration item rules. This view
can be joined to other views by using the RecordID column.

v_CIErrorDetails
Lists information about configuration items that reported errors when they were
evaluated for compliance. This includes information about the configuration item, its
settings and rules, and details about the error that was generated. This view can be
joined to other views by using the CI_ID and ResourceID columns.

v_CI_CurrentComplianceStatus
Lists, by CI_ID, the currently deployed configuration items, and detailed information
about their current compliance status. This view can be joined to other views by using
the CI_ID and ResourceID columns.

v_CIAssignmentStatusSummary

<!-- p.249 -->

Lists details about the compliance status of currently deployed configuration data. This
view can be joined to other views by using the AssignmentID column.

v_CIAssignmentSummary
Lists summary information for deployed configuration items, including the
summarization time, success and failure statistics, requirements not met, and more. This
view can be joined to other views by using the AssignmentID column.

Compliance settings status views
The compliance settings status views contain information about the compliance,
evaluation, and enforcement state of configuration items. For more information about
the status views, see Status and alert views in Configuration Manager. The status views
that contain compliance settings information are described in this section.

v_CIAssignmentStatus
Lists the enforcement and evaluation state messages received from Configuration
Manager client computers for all assigned configuration items, including assigned
software update deployments and assigned configuration baselines. The assignment ID,
resource ID, last enforcement state message ID, last evaluation state message ID, and so
on are provided. The view can be joined to other views by using the AssignmentID and
ResourceID columns.

v_CIComplianceHistory
Lists the configuration items, by CI_UniqueID and CI_ID, that are configuration baselines
or a configuration item in a configuration baseline, have been assigned to a
Configuration Manager client (listed by ResourceID), and it lists compliance information
for the configuration item. The information includes the compliance start and end dates,
whether the configuration item is applicable to the client, whether the client is
compliant for the configuration item, and so on. The view can be joined to other views
by using the CI_UniqueID, CI_ID, and ResourceID columns.

v_CIComplianceStatusDetail
Lists the configuration items, by CI_ID and CI_UniqueID, that are in a configuration
baseline, have been assigned to a Configuration Manager client (listed by ResourceID),

<!-- p.250 -->

and have a state value of Non-Compliant. The view can be joined to other views by
using the CI_ID, CI_UniqueID, ResourceID, and ModelName columns.

v_CICurrentComplianceStatus
Lists the compliance and enforcement states for configuration items, by configuration
item ID, as well as the resource ID, whether the configuration item is applicable to the
resource, and information related to the compliance and evaluation of the configuration
item. The view can be joined to other views by using the CI_ID, ResourceID,
CI_UniqueID, ModelName, ComplianceState, and LastEnforcementMessageID
columns. The ComplianceState column provides the state ID for state messages with a
topic type of 401. The LastEnforcementMessageID column provides the state ID for
state messages with a state message topic type of 402.

v_DCMClientStatusInformation
Lists all possible compliance settings client states. It is unlikely that this view will be
joined to other views.

Compliance settings status summarizer views
The compliance settings status summarizer views provide summary information for
configuration item deployments and configuration baselines. For more information
about the status summarizer views, see Status and alert views in Configuration Manager.
The status summarizer views that contain compliance settings information are described
in this section.

v_AssignmentSummaryPerTopic
Lists the deployments, by assignment ID, the type of deployment state message, the
state ID for the type, the count of Configuration Manager client computers that are in
the deployment state, and the total count of client computers that have been targeted
for the deployment. The view can be joined to other views by using the AssignmentID
column.

  ７ Note

<!-- p.251 -->

  There are three deployment states. A state type of 300 is deployment compliance,
  type 301 is deployment enforcement, and type 302 is deployment evaluation. You
  can find a list of the state IDs by looking in the v_StateNames view.

v_CIComplianceSummary
Lists the compliance settings configuration baselines, by CI_ID, and the count of
Configuration Manager client devices that have been targeted, how many clients are
compliant, how many have failed the compliance evaluation, how many are
noncompliant, and more. The view can be joined to other views by using the CI_ID and
CI_UniqueID columns.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.252 -->

Content management views in
Configuration Manager
Article • 10/04/2022

Content management in Configuration Manager provides the tools for you to manage
content files for applications, packages, software updates, and operating system
deployment.

Content management views
The content management views are described in the following table.

v_ContentDistributionReport
Lists information about the content packages sent to each distribution point together
with the status of the distribution and the current state of the distribution. This view can
be joined to other views by using the PkgID column.

v_ContentDistributionMessages
Lists status returned by the content distribution process for Configuration Manager
content packages, by ID. Returns the ID of the content package, recent status messages,
and more. This view can be joined to other views by using the PkgID column.

v_DistributionPointInfoBase
Lists detailed information about each distribution point in the site, including the server
name, the NAL path, any configured share name, whether it's Internet-facing and more.
This view can be joined to other views by using the ServerName column.

v_DistributionPointMessages
List information about status messages sent by packages on each distribution point in
the site. This info includes the last time that status was sent and the ID of the status
message that was sent. This view can be joined to other views by using the ID, DPID, or
PkgID columns.

v_DistributionPoints

<!-- p.253 -->

Lists information about each distribution point in the Configuration Manager hierarchy,
including the ID, the server name that hosts the distribution point, the site code,
whether it's a pull distribution point, and more. This view can be joined to other views
by using the DPID column.

v_DistributionStatus
Lists each content package and the current distribution status of the package. This
includes the package ID, the ID of the distribution point, the time that status was last
reported and more. This view can be joined to other views by using the PkgID column.

v_DistributionPointDriveInfo
Lists information about the location and the status of content on distribution points.
This info includes the site code, NAL path, drive where the content is stored, total and
free space on the drive, and more. It's unlikely that this view will be joined to other
views.

v_DPGroupContentDetails
Lists information, by group ID about the content stored on distribution point groups.
This includes the group ID, content package ID, number of packages pending install,
number of packages successfully installed, and more. This view can be joined to other
views by using the GroupID or PkgID columns.

v_DPGroupContentInfo
Lists, for each distribution point, the number of content packages installed, in progress,
or failed. This view can be joined to other views by using the GroupID column.

v_DPGroupMembers
Lists, by group ID, the path to each distribution point in the group. It's unlikely that this
view will be joined to other views.

v_DPGroupPackages
Lists, by group ID, the content packages that have been deployed to each distribution
point group. It's unlikely that this view will be joined to other views.

<!-- p.254 -->

v_DPStatusSummary
Lists, by NAL path, the summary status of each distribution point. This includes the
number of packages distributed to the distribution point, the number of content
distributions installed, in progress and failed. This view can be joined to other views by
using the DPNalPath column.

v_Content
Lists, by package ID, each content package at the site, including the content ID, version,
size of the source files in bytes, and more. This view can be joined to other views by
using the PkgID column.

v_ContDistStatSummary
Lists, by package ID, each content package at the site, with details about which
distribution points have been targeted with that content, together with the last status
time, number if successful, pending and failed content distributions, and more. This view
can be joined to other views by using the PkgID column.

v_ContentDistribution
Lists information about the content packages, by package ID, that have been sent to
distribution points. This includes the ID of the distribution point, the current state and
the date of the last status summary. This view can be joined to other views by using the
PkgID column.

v_ContentDistributionHighlights
This view can be joined to other views by using the PkgID column.

v_ContentDistributionReport_DP
Lists, sorted by distribution point NA: path, the current status of each distribution point.
This includes the last status time, number of packages on the distribution point, number
of content distributions in progress and the number of errors. This view can be joined to
other views by using the DPNalPath column.

v_ContentDistributionVersions

<!-- p.255 -->

Lists, by package ID, the package versions on each distribution point. This includes the
site code, the NAL path of the distribution point, the latest source version and state, and
more. This view can be joined to other views by using the PkgID column.

v_ContentInfo
This view lists information about content associated with an application or deployment.
This includes the source location of the content, information about related content and
more. This view can be joined to other views by using the Content_ID column.

v_SMS_DistributionPointGroup
Lists all distribution point groups in the site hierarchy by GroupID. Contains the name of
the distribution point group, who created it and when, the number of distribution points
in the group and more. It's unlikely that this view will be joined to other views.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.256 -->

Discovery views in Configuration
Manager
Article • 10/04/2022

The Configuration Manager discovery views consist of system resource objects, which
include any resources that were discovered on the network. The four main discovery
views are v_R_System for system resources, v_R_User for user resources, v_R_UserGroup
for user group resources, and v_R_UnknownSystem for unknown systems.

Each of these discovered resources has a defined resource type, which is stored in the
v_resourcemap schema view.

Discovery schema views
The discovery schema views provide information about all resources in a Configuration
Manager site. The two discovery schema views are v_ResourceMap and
v_ResourceAttributeMap. The v_ResourceMap view contains a list of all the resource
types for discovered data. By default, Configuration Manager has the Unknown System,
User Group, User, and System Resource types, each of which has its own resource type
number and individual view. The view can be joined to other views by using the
ResourceType column. The following table contains the default data stored in the
v_ResourceMap view.

v_R_System_Valid
Lists information about valid computers. This view is sorted by ResourceID and includes
the client version, the processor type, the client's domain, the NetBIOS name, the
operating system and more. This view can be joined to other views by using the
ResourceID column.

                                                                        ﾉ   Expand table

 Resource type            Display name                Resource Class Name

 2                        Unknown System              v_R_UnknownSystem

 3                        User Group                  v_R_UserGroup

 4                        User                        v_R_User

 5                        System                      v_R_System

<!-- p.257 -->

 Resource type            Display name                 Resource Class Name

 6                        IP Network                   V_R_IPNetwork

The v_ResourceAttributeMap contains all of the attributes that will be discovered for
each of the resource types, such as NetBIOS name, operating system, user name, user
group name, domain name, and so forth. The v_ResourceAttributeMap view can be
joined to other views by using the ResourceType column. The discovery schema views
are also listed and described in the Schema views in Configuration Manager topic.

Configuration Manager discovery views
The v_R_System view can be joined with any other view that contains system data
(system discovery array views, inventory views, collection views, status views, and so
forth) by using the ResourceID column. The v_R_System view will be one of the most
often used when joining views. The v_R_UnknownSystem, v_R_User, and v_R_UserGroup
views also use the ResourceID column to join with views that contain data for their
resource type. Most of the remaining discovery views contain data where there can be
more than one value for a resource, such as IP address or user organizational unit (OU)
name. The discovery views are described in the following table.

v_AgentDiscoveries
Lists all resources that have been discovered in the Configuration Manager hierarchy
and by what discovery agent. The view contains data about the resource type, resource
ID, agent that discovered the resource, site code where the agent resides, and time of
the discovery. The view can be joined to other views by using the ResourceID column.

v_ClientMachines
Lists all discovered system resources, by resource ID, that are not in an obsolete or
decommissioned state and whether the system resource is a Configuration Manager
client. The view can be joined to other views by using the ResourceID column.

v_ClientMode
Lists all discovered system resources, by resource ID, that are not in an obsolete or
decommissioned state and the associated client mode. The view can be joined to other
views by using the ResourceID column.

<!-- p.258 -->

v_R_System
Lists all discovered system resources by resource ID, resource type, whether the resource
is a client, what type of client, client version, NetBIOS name, user name, operating
system, unique identifier, and more. The view can be joined to other views by using the
ResourceID, ResourceType, Netbios_Name0, and SMS_Unique_Identifier0 columns.

v_RA_System_SMS_Resident
Lists the resident site of discovered devices. The view can be joined to other views by
using the ResourceID column.

v_R_System_Valid
Lists all discovered system resources that are not in an obsolete or decommissioned
state. This view is a subset of the v_R_System view and includes the resource ID,
resource type, whether the resource is a client, what type of client, client version,
NetBIOS name, user name, operating system, unique identifier, and so forth. The view
can be joined to other views by using the ResourceID, ResourceType, and
Netbios_Name0 columns.

v_R_UnknownSystem
Lists all unknown system resources that have been discovered, including resource ID,
resource type, user name, domain, and so forth. The view can be joined to other views
by using the ResourceID, ResourceType, and SMS_Unique_Identifier0 columns.

v_R_User
Lists all discovered user resources by resource ID, resource type, user name, domain,
and so forth. The view can be joined to other views by using the ResourceID,
ResourceType, and Unique_User_Name0 columns.

v_R_UserGroup
Lists all discovered user group resources by ID, type, user group name, domain, and
more. The view can be joined to other views by using the ResourceID and ResourceType
columns.

v_RA_System_IPAddresses

<!-- p.259 -->

Lists the IP addresses for discovered system resources. The view can be joined to other
views by using the ResourceID column.

v_RA_System_IPSubnets
Lists the IP subnets for discovered system resources. The view can be joined to other
views by using the ResourceID column.

v_RA_System_IPv6Addresses
Lists the IPv6 addresses for discovered system resources. The view can be joined to
other views by using the ResourceID column.

v_RA_System_IPv6Prefixes
Lists the IPv6 prefixes for discovered system resources. The view can be joined to other
views by using the ResourceID column.

v_RA_System_IPXAddresses
Lists the IPX addresses for discovered system resources. The view can be joined to other
views by using the ResourceID column.

v_RA_System_MACAddresses
Lists the MAC addresses for discovered system resources. The view can be joined to
other views by using the ResourceID column.

v_RA_System_ResourceNames
Lists all discovered system resources by resource ID and fully qualified domain name.
The view can be joined to other views by using the ResourceID column.

v_RA_System_SMSAssignedSites
Lists all system resources, by resource ID, that are assigned to a site, together with the
site code. The view can be joined to other views by using the ResourceID column.

v_RA_System_SMSInstalledSites

<!-- p.260 -->

Lists all system resources, by resource ID that have been installed as clients and the site
code they belong to. The view can be joined to other views by using the ResourceID
column.

v_RA_System_SystemContainerName
Lists all system resources, by resource ID, that are in an associated Active Directory
container. The view can be joined to other views by using the ResourceID column.

v_RA_System_SystemGroupName
Lists all system resources, by resource ID, that are in an associated Active Directory
group. The view can be joined to other views by using the ResourceID column.

v_RA_System_SystemOUName
Lists all system resources, by resource ID, that and their associated Active Directory OU.
The view can be joined to other views by using the ResourceID column.

v_RA_System_SystemRoles
Lists all system resources, by resource ID, that have an associated site system role (site
server, management point, software update point, and so forth). The view can be joined
to other views by using the ResourceID column.

v_RA_User_UserContainerName
Lists all user resources, by resource ID, that are in an associated Active Directory
container. The view can be joined to other views by using the ResourceID column.

v_RA_User_UserGroupName
Lists all user resources, by resource ID, that are in an associated Active Directory group.
The view can be joined to other views by using the ResourceID column.

v_RA_User_UserOUName
Lists all user resources, by resource ID, that are in an associated OU. The view can be
joined to other views by using the ResourceID column.

<!-- p.261 -->

v_R_IPNetwork
Lists information about IP subnets discovered by Configuration Manager network
discovery, sorted by ResourceID. This includes information about subnet addresses,
masks, names and topology. This view can be joined to other views by using the
ResourceID column.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.262 -->

Endpoint protection views in
Configuration Manager
Article • 10/04/2022

The Configuration�Manager�Endpoint�Protection views provide information about
the status of Endpoint Protection clients and malware activity in your Configuration
Manager site.

The following sections provide detailed information about the Endpoint Protection
views.

Endpoint protection views
The Endpoint Protection views are described in this section.

v_AM_NormalizedDetectionHistory
No description.

v_OverallThreatActivity
This view lists each collection in the Configuration Manager site, by collection ID. For
each collection, information such as the number of infected computers, the computers
that require a restart and information about any malware that was recently removed are
listed. This view can be joined to other views by using the CollectionID column.

v_OverallThreatActivity_History
This view lists each collection in the Configuration Manager site, by collection ID. For
each collection, historical information such as the number of infected computers, the
computers that require a restart and information about any malware that was recently
removed are listed. This view can be joined to other views by using the CollectionID
column.

v_EndpointProtectionCollections
Contains the collection ID and collection name of all collections that have the option
View this collection in the Endpoint Protection dashboard checked on the Alerts tab of

<!-- p.263 -->

the collection name�Properties dialog box. This view can be joined to other views by
using the CollectionID and CollectionName columns.

v_EndpointProtectionHealthStatus
Lists the collections protected by Endpoint Protection with information about the
number of clients in each collection, clients that are considered at risk, clients that
haven't been installed yet, clients that aren't supported and more. This view can be
joined to other views by using the CollectionID column.

v_EndpointProtectionHealthStatus_History
Lists historical information about the collections protected by Endpoint Protection with
information about the number of clients in each collection, clients that are considered at
risk, clients that haven't been installed yet, clients that aren't supported and more. This
view can be joined to other views by using the CollectionID column.

v_GS_AntimalwareHealthStatus
Lists information about the antimalware client installed on each Configuration Manager
client computer, including whether the antimalware and antivirus components are
enabled, the last scan time and date, the antimalware engine version, and more. This
view can be joined to other views by using the ResourceID column.

v_GS_AntimalwareInfectionStatus
Lists information about the status of clients protected by Endpoint Protection, such as
the status of the computer, whether it's pending a full scan or a restart, whether manual
steps are required to resolve a malware infection, and more. This view can be joined to
other views by using the ResourceID column.

v_EndpointProtectionStatus
Provides an overall summary of the status of Endpoint Protection clients for each
computer, sorted by resource ID. This includes whether the client is protected, whether
it's considered at risk, whether it supports Endpoint Protection, whether it requires a
restart, and more. This view can be joined to other views by using the ResourceID
column.

v_GS_Threats

<!-- p.264 -->

Lists threats discovered on clients, sorted by resource ID. This view can be joined to
other views by using the ResourceID column.

v_TopThreatsDetected
Lists, by collection ID, the top malware threats found on client computers. Includes the
threat name, the number of computers in the collection that are affected, and more. This
view can be joined to other views by using the CollectionID column.

v_ThreatSummary
Lists the possible descriptions of each malware threat that can be detected by Endpoint
Protection. It's unlikely that this view will be joined to other views.

v_ThreatSeverities
Lists the threat severities, by severity ID that can be displayed in the Endpoint Protection
dashboard to indicate the severity of discovered malware. It's unlikely that this view will
be joined to other views.

v_ThreatDefaultActions
Lists the default actions, by default action ID that can be taken when malware is
discovered on client computers. It's unlikely that this view will be joined to other views.

v_ThreatCategories
Lists the available threat categories, by category ID, that malware can be sorted into,
such as trojans and spyware. It's unlikely that this view will be joined to other views.

v_ThreatCatalog
Lists all known threats, by threat ID. Includes the name, severity, and summary for the
threat, together with the action that Endpoint Protection will take if the threat is
discovered on client computers. This view can be joined to other views by using the
ThreatID, SeverityID, CategoryID and DefaultActionID columns.

v_GS_EPDeploymentState

<!-- p.265 -->

Lists, by resource ID, the current state of the Endpoint Protection client deployment to
computers. Includes the last status sent by the client, the state of the deployment, and
any errors that have been generated. This view can be joined to other views by using the
ResourceID column.

v_CurrentThreatOutbreak
Lists, by resource ID, the malware threats that have been detected on client computers.
This includes the threat ID, the threat name, when the threat was first detected and
when it was last detected. This view can be joined to other views by using the
ResourceID column.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.266 -->

Inventory views in Configuration
Manager
Article • 10/10/2022

Inventory views contain hardware and software inventory information about the clients,
files, products, and so forth, in the Configuration Manager hierarchy. Configuration
Manager collects inventory data when you enable the Hardware Inventory Client Agent
or Software Inventory Client Agent. Because you can configure which hardware
inventory to collect during the hardware inventory scan cycle and which file types to
scan for during the software inventory scan cycle, each site will have a unique set of
inventory that is collected.

For each Configuration Manager site, it's possible to retrieve a list of the hardware and
software inventory schema to determine exactly what is inventoried. The articles in this
section provide examples of how to do get the hardware and software inventory lists,
and detailed information about the typical Configuration Manager SQL views.

In This Section
      Hardware inventory views in Configuration Manager

      Software inventory views in Configuration Manager

      Asset intelligence views in Configuration Manager

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.267 -->

Hardware inventory views in
Configuration Manager
Article • 01/27/2023

The hardware inventory views contain information about the computer hardware
scanned on Configuration Manager client computers. Many hardware inventory views
are created in Configuration Manager by default, and many more can be enabled or
creating classes by using the hardware inventory classes dialog box, accessible from
client settings. Because of this, it is likely that Configuration Manager sites collect
different hardware inventory resulting in different hardware inventory views.

For more information about extending Configuration Manager hardware inventory, see
How to extend hardware inventory in Configuration Manager.

Hardware inventory schema views
The hardware inventory schema is important to understand when creating queries for
Configuration Manager reports. Most of the client data within Configuration Manager is
contained in one of the two hardware inventory schema views: v_GroupMap and
v_GroupAttributeMap. The v_GroupMap view contains a list of all the hardware
inventory groups and the associated view for each of the groups. The
v_GroupAttributeMap view contains all of the attributes that are inventoried for each of
the groups. Both views can be joined together by using the GroupID column and joined
to the v_ResourceMap discovery schema view by using the ResourceType column.

Because hardware inventory can be extended, one Configuration Manager site's SQL
Server database might have different hardware inventory views and schema when
compared to another site. The following query joins the v_GroupMap and
v_GroupAttributeMap to generate the hardware inventory view schema, based on the
specific settings for the site:

  SQL

  SELECT DISTINCT GM.DisplayName, GM.InvClassName,

     GM.InvHistoryClassName, GAM.AttributeName,

     GAM.ColumnName, GM.MIFClass

  FROM v_GroupMap GM INNER JOIN v_GroupAttributeMap GAM

<!-- p.268 -->

    ON GM.GroupID = GAM.GroupID

Hardware inventory views
Most of the hardware inventory views start with the v_GS_ view name followed by the
name of the hardware component, such as CDROM (for example, v_GS_CDROM). As a
general rule, each hardware inventory view has an associated inventory history view that
starts with the v_HS_ view name. The hardware inventory views can all be joined with
other system data views by using the ResourceID column, which is demonstrated in
Appendix A, in the topic Sample queries for hardware inventory in Configuration
Manager. The standard hardware inventory views are described in this section.

  ７ Note

  Not all of the items listed are collected by default when using Configuration
  Manager hardware inventory. For information about how to enable or disable
  hardware inventory classes, see the How to extend hardware inventory in
  Configuration Manager topic in the Configuration Manager Documentation Library

v_InventoryClass
Lists the WMI classes that are collected by Configuration Manager hardware inventory
by class ID. The view also shows the WMI namespace, the class name and the name of
the class as it will be displayed in Resource Explorer. This view can be joined to other
views by using the ClassID column.

v_InventoryClassProperty
Lists the properties collected from each inventory class by Configuration Manager
hardware inventory. This view is unlikely to be joined to other views.

v_InventoryReport
Lists information about the last inventory taken by Configuration Manager. This can
include hardware inventory, software inventory, and discovery. This view is unlikely to be
joined to other views.

v_InventoryReportClass

<!-- p.269 -->

Lists the inventory classes and properties used by Configuration Manager hardware
inventory. This view is unlikely to be joined to other views.

v_CustomInventoryReport
Lists details about hardware inventory collected from clients that have custom hardware
inventory client settings deployed. This view can be joined to other views by using the
CollectionID column.

v_Add_Remove_Programs
Lists information about the software installed on Configuration Manager clients that is
registered in Add or Remove Programs or Programs and Features list. The view can be
joined with other views by using the ResourceID column.

v_GS_1394_CONTROLLER
Lists details about 1394 controllers on clients. This includes the manufacturer, the install
date and more. This view can be joined to other views by using the ResourceID column.

v_GS_ACTIVESYNC_CONNECTED_DEVICE
Lists information about devices connected to Configuration Manager clients by using
Exchange ActiveSync. The view can be joined with other views by using the ResourceID
column.

v_GS_ACTIVESYNC_SERVICE
Lists information about the Exchange ActiveSync service on Configuration Manager
clients, including the version and last synchronization time. The view can be joined with
other views by using the ResourceID column.

v_GS_ADD_REMOVE_PROGRAMS
Lists information about the software installed on Configuration Manager clients that is
shown in the list of installed programs in Windows Control Panel. The view can be joined
with other views by using the ResourceID column.

v_GS_ADD_REMOVE_PROGRAMS_64

<!-- p.270 -->

Lists information about the 64-bit software installed on Configuration Manager client
computers that is shown in the list of installed programs in Windows Control Panel. The
view can be joined with other views by using the ResourceID column.

v_GS_ADVANCED_CLIENT_SSL_CONFIGURATIONS
Lists all Configuration Manager clients, by resource ID, and associated Secure Sockets
Layer (SSL) information for the resource, if applicable. The view can be joined with other
views by using the ResourceID column.

v_GS_APPV_CLIENT_APPLICATION
Lists computers that have the App-V client application installed. The view can be joined
with other views by using the ResourceID column.

V_GS_APPV_CLIENT_PACKAGE
Lists computers that have the App-V client package installed. The view can be joined
with other views by using the ResourceID column.

v_GS_AUTOSTART_SOFTWARE
Lists information about the applications on Configuration Manager clients that start
automatically with the operating system found through Asset Intelligence. The view is
also listed and described in the Asset intelligence views in Configuration Manager topic.
The view can be joined with other views by using the ResourceID column.

v_GS_BASEBOARD
Lists information about the motherboard on Configuration Manager client computers.
This includes the serial number of the motherboard, a description and more. This view
can be joined to other views by using the ResourceID column.

v_GS_BATTERY
Returns details about any computer that contains a battery, such as a notebook
computer. Includes information about the type of battery, any errors it has reported,
when it was installed, and more. The view can be joined with other views by using the
ResourceID column.

<!-- p.271 -->

v_GS_BOOT_CONFIGURATION
Lists information about the folders and resources Windows uses to start on client
computers, such as the startup folder, the location of Windows, the boot partition and
more. This view can be joined to other views by using the ResourceID column.

v_GS_BROWSER_HELPER_OBJECT
Lists information about the browser objects found on Configuration Manager clients
through Asset Intelligence. While some browser helper objects are beneficial, malware
might be delivered is in the form of browser helper objects. The view is also listed and
described in the Asset intelligence views in Configuration Manager topic. The view can
be joined with other views by using the ResourceID column.

v_GS_CCM_RECENTLY_USED_APPS
Lists information about the applications found on Configuration Manager clients,
through software metering, that were recently run. The view can be joined with other
views by using the ResourceID column.

v_GS_CDROM
Lists information about CDROM devices found on Configuration Manager clients. This
view can be joined with other views by using the ResourceID column.

v_GS_COMPUTER_SYSTEM
Lists information about the Configuration Manager clients, including domain, computer
name, Configuration Manager roles, status, system type, and more. The view can be
joined with other views by using the ResourceID column.

v_GS_COMPUTER_SYSTEM_PRODUCT
Lists general information about inventoried client devices including the manufacturer
and model. This view can be joined to other views by using the ResourceID column.

v_GS_DESKTOP
Lists information about the desktop settings on client computers including the icon size,
wallpaper settings, fonts and more. The view can be joined with other views by using the

<!-- p.272 -->

ResourceID column.

v_GS_DESKTOP_MONITOR
Lists information about the desktop monitors found on Configuration Manager client
computers. The view can be joined with other views by using the ResourceID column.

v_GS_DEVICE_CERTIFICATES
Lists information about the certificates on devices, including the revision ID, issuer,
where it is located in the certificate store, the subject, the dates the certificate is valid,
and so on. The view is also listed and described in the Mobile device management views
in Configuration Manager topic. The view can be joined with other views by using the
ResourceID column.

v_GS_DEVICE_COMPUTERSYSTEM
Lists information about the Configuration Manager devices, including the device ID,
number of processors, platform type, processor type, and so on. The view is also listed
and described in the Mobile device management views in Configuration Manager topic.
The view can be joined with other views by using the ResourceID column.

v_GS_DEVICE_DISPLAY
Lists information about the displays found on Configuration Manager devices. The view
is also listed and described in the Mobile device management views in Configuration
Manager topic. The view can be joined with other views by using the ResourceID
column.

v_GS_DEVICE_MEMORY
Lists information about the memory found on Configuration Manager devices. The view
is also listed and described in the Mobile device management views in Configuration
Manager topic. The view can be joined with other views by using the ResourceID
column.

v_GS_DEVICE_OSINFORMATION
Lists information about the operating system found on Configuration Manager devices.
The view is also listed and described in the Mobile device management views in

<!-- p.273 -->

Configuration Manager topic. The view can be joined with other views by using the
ResourceID column.

v_GS_DEVICE_POWER
Lists information about power settings and the battery on Configuration Manager
devices. The view is also listed and described in the Mobile device management views in
Configuration Manager topic. The view can be joined with other views by using the
ResourceID column.

v_GS_DISK
Lists information about the disk drives found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column.

v_GS_DMA_CHANNEL
Lists information about the Direct Memory Access (DMA) channels found on client
computers. This view can be joined to other views by using the ResourceID column.

v_GS_EMBEDDED_DEVICE_INFO
Lists information about Windows Embedded devices, including the model name of the
device. The view can be joined with other views by using the ResourceID column.

v_GS_ENCRYPTABLE_VOLUME
Lists the encryptable disk volumes found on Windows computers. The view can be
joined with other views by using the ResourceID column.

v_GS_ENVIRONMENT
Lists details about the Windows environment variables found on client computers. The
view can be joined with other views by using the ResourceID column.

v_GS_FOLDER_REDIRECTION_HEALTH
Lists information about the status of folder redirection on Windows computers. The view
can be joined with other views by using the ResourceID column.

<!-- p.274 -->

v_GS_IDE_CONTROLLER
Lists information about the IDE controllers found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column.

v_GS_INSTALLED_EXECUTABLE
Lists information about the installed executable files (files with the extension .exe) on
Configuration Manager clients found through Asset Intelligence. The view is also listed
and described in the Asset intelligence views in Configuration Manager topic. The view
can be joined with other views by using the ResourceID column.

v_GS_INSTALLED_SOFTWARE
Lists information about the installed software applications on Configuration Manager
clients found through Asset Intelligence. The view is also listed and described in the
Asset intelligence views in Configuration Manager topic.

The view can be joined with other views by using the ResourceID column and with Asset
Intelligence views by using the SoftwareCode0 and SoftwarePropertiesHash0 columns.

v_GS_INSTALLED_SOFTWARE_CATEGORIZED
Lists information about the installed software applications on Configuration Manager
clients found through Asset Intelligence. This view contains the information in the
v_GS_INSTALLED_SOFTWARE view and joins several other tables to provide additional
details about the installed software. The view is also listed and described in the Asset
intelligence views in Configuration Manager topic.

The view can be joined with other views by using the ResourceID column and with Asset
Intelligence views by using the SoftwareCode0, SoftwarePropertiesHash0, FamilyID,
CategoryID, and SoftwareID columns.

v_GS_INSTALLED_SOFTWARE_MS
Lists information about the installed Microsoft software applications on Configuration
Manager clients found through Asset Intelligence. The view is also listed and described
in the Asset intelligence views in Configuration Manager topic.

The view can be joined with other views by using the ResourceID column.

<!-- p.275 -->

v_GS_IRQ
List information about Interrupt Requests (IRQ's) found on client computers. This view
can be joined to other views by using the ResourceID column.

v_GS_KEYBOARD_DEVICE
Lists information about keyboards found on Configuration Manager clients. The view
can be joined with other views by using the ResourceID column.

v_GS_LOGICAL_DISK
Lists information about the logical disks found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column.

v_GS_MODEM_DEVICE
Lists information about modems found on Configuration Manager clients. The view can
be joined with other views by using the ResourceID column.

v_GS_MOTHERBOARD_DEVICE
Lists information about the motherboard found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column.

v_GS_NETWORK_ADAPTER
Lists information about the network adapters found on Configuration Manager clients,
including adapter type, description, MAC address, manufacturer, service name, and so
on. This view can be joined with other views by using the ResourceID column.

v_GS_NETWORK_ADAPTER_CONFIGURATION
Lists information about the configuration for network adapters found on Configuration
Manager clients, including default IP gateway, whether DHCP is enabled, the DHCP
server, DNS domain, IP address, IP subnet, and so on. The view can be joined with other
views by using the ResourceID column.

v_GS_NETWORK_CLIENT

<!-- p.276 -->

Lists information about the network clients found on Configuration Manager clients,
including description, manufacturer, name, status, and more. The view can be joined
with other views by using the ResourceID column.

V_GS_NETWORK_LOGIN_PROFILE
Lists information about the login profiles found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column.

v_GS_NT_EVENTLOG_FILE
Lists detailed information about the Windows Event Logs found on client computers.
This includes file names, paths, maximum and current sizes, and more.

The view can be joined with other views by using the ResourceID column.

v_GS_OPERATING_SYSTEM
Lists information about the operating system found on Configuration Manager clients.
The view can be joined with other views by using the ResourceID column.

V_GS_OS_RECOVERY_CONFIGURATION
Lists information about the actions that Windows clients take when they experience an
unrecoverable error. The view can be joined with other views by using the ResourceID
column.

v_GS_PAGE_FILE_SETTING
List information about the paging file on Windows computers. This includes the initial
size and the maximum size for the page file. This view can be joined with other views by
using the ResourceID column.

v_GS_PARALLEL_PORT
Lists information about parallel ports found on Configuration Manager clients. The view
can be joined with other views by using the ResourceID column.

v_GS_PARTITION

<!-- p.277 -->

Lists information about disk partitions found on Configuration Manager clients. The view
can be joined with other views by using the ResourceID column.

v_GS_PC_BIOS
Lists information about the BIOS found on Configuration Manager clients. This view can
be joined with other views by using the ResourceID column.

v_GS_PCMCIA_CONTROLLER
Lists information about the type, capabilities and status of any PCMCIA controllers
inventoried on client computers. This view can be joined with other views by using the
ResourceID column.

v_GS_PHYSICAL_MEMORY
Lists information about the physical memory installed in devices. Includes the capacity,
manufacturer, description and more. The view can be joined with other views by using
the ResourceID column.

v_GS_PORT
Lists information about the ports on each client computer. This view can be joined with
other views by using the ResourceID column.

v_GS_PORTABLE_BATTERY
Lists information about the battery on portable computers, including its status, type,
voltage and expected life. This view can be joined to other views by using the
ResourceID column.

v_GS_POWER_SUPPLY
Lists information about the power supply used by the Configuration Manager client
device. This includes information about remaining charge, reported errors, power
management capabilities and more. This view can be joined to other views by using the
ResourceID column.

v_GS_POINTING_DEVICE

<!-- p.278 -->

Lists information about the pointing devices connected to Configuration Manager
clients. The view can be joined with other views by using the ResourceID column.

v_GS_PNP_DEVICE_DRIVER
Lists information about the device drivers found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column.

v_GS_PRINT_JOB
Lists, by resource ID, information about jobs that are in the printer queue of client
computers. This view can be joined with other views by using the ResourceID column.

v_GS_PRINTER_CONFIGURATION
Lists information about the configuration of printers attached to a device, including the
printer name, whether it has double-sided (duplex) capabilities, its driver version and
more. This view can be joined with other views by using the ResourceID column.

v_GS_PRINTER_DEVICE
Lists information about the print devices attached to clients, including the model, print
capabilities and current status at the time the inventory was ran. This view can be joined
with other views by using the ResourceID column.

v_GS_PROCESS
Lists information about the Windows processes that were running on client computers
at the time they ran hardware inventory. This view can be joined with other views by
using the ResourceID column.

v_GS_PROCESSOR
Lists information about the processors found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column and to the
v_LU_CPU asset intelligence view by using the CPUHash0 column.

v_GS_PROTECTED_VOLUME_INFO

<!-- p.279 -->

Lists information about protected disk volumes found on client computers. The view can
be joined with other views by using the ResourceID column.

v_GS_PROTOCOL
Lists detailed information about the network protocols used by client computers. The
view can be joined with other views by using the ResourceID column.

v_GS_QUICK_FIX_ENGINEERING
Lists information about Windows hotfixes installed on client computers. Includes the
name of the hotfix, who installed it and when, a description of the hotfix, and more. The
view can be joined with other views by using the ResourceID column.

v_GS_REGISTRY
Lists information about the registry on client computers such as its current size and its
maximum size. This view can be joined to other views by using the ResourceID column.

v_GS_SCSI_CONTROLLER
Lists information about the SCSI controllers found on Configuration Manager clients.
The view can be joined with other views by using the ResourceID column.

v_GS_SERVER_FEATURE
Lists the server features that are installed on Windows Server computers. The view can
be joined with other views by using the ResourceID column.

v_GS_SERIAL_PORT
Lists information about the type, capabilities and status of serial ports inventoried on
client computers. This view can be joined with other views by using the ResourceID
column.

v_GS_SERIAL_PORT_CONFIGURATION
Lists information about the serial ports on clients. This view can be joined to other views
by using the ResourceID column.

<!-- p.280 -->

v_GS_SERVICE
Lists information about the Windows services found on Configuration Manager clients.
The view can be joined with other views by using the ResourceID column.

v_GS_SHARE
Lists information about shared folders found on client computers. The view can be
joined with other views by using the ResourceID column.

v_GS_SMS_ADVANCED_CLIENT_STATE
Lists information about the name and version of Configuration Manager client
components found on clients. The view can be joined with other views by using the
ResourceID column.

v_GS_SOFTWARE_LICENSING_PRODUCT
Lists software licensing product information for Windows Configuration Manager clients
found through Asset Intelligence. The view is also listed and described in the Asset
intelligence views in Configuration Manager topic. The view can be joined with other
views by using the ResourceID column.

v_GS_SOFTWARE_LICENSING_SERVICE
Lists software licensing service information for Windows Configuration Manager clients
found through Asset Intelligence. The view is also listed and described in the Asset
intelligence views in Configuration Manager topic. The view can be joined with other
views by using the ResourceID column.

v_GS_SOFTWARE_SHORTCUT
Lists software shortcut information for Configuration Manager clients found through
Asset Intelligence. The view is also listed and described in the Asset intelligence views in
Configuration Manager topic. The view can be joined with other views by using the
ResourceID column.

v_GS_SOUND_DEVICE
