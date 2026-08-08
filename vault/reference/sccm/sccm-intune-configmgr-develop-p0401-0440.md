---
title: "Configuration Manager SDK documentation — pages 401-440"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0401-0440
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0401-0440
family: sccm
documentKind: "doc"
abstract: "Sample queries for collections in Configuration Manager Article • 10/10/2022 The following sample queries demonstrate how to join some of the most commonly used collection views to other views. Joining collection views The following query lists the resources in the Configuration"
---

# Configuration Manager SDK documentation — pages 401-440

<!-- p.401 -->

Sample queries for collections in
Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join some of the most commonly
used collection views to other views.

Joining collection views
The following query lists the resources in the Configuration Manager hierarchy that are
in a collection, the assigned site for client computers, the collection ID, collection name,
and the last time the collection was refreshed. The v_FullCollectionMembership view is
joined to the v_Collection view by using the CollectionID column. The query results are
sorted by resource name and then by collection ID.

  SQL

        SELECT FCM.Name, FCM.SiteCode, FCM.CollectionID,
        ��COL.Name, COL.LastRefreshTime
        FROM v_FullCollectionMembership FCM INNER JOIN v_Collection COL
        ��ON FCM.CollectionID = COL.CollectionID
        ORDER BY FCM.Name, FCM.CollectionID

Joining collection and resource views
The following query lists all of the discovered resources that do not have a
Configuration Manager client installed. The query lists the domain, computer name, and
all discovered IP addresses using data by joining three views. The
v_CM_RES_COLL_SMS00001 collection view is joined to the v_R_System and
v_RA_IPAddresses discovery views by using the ResourceID column.

  SQL

        SELECT SYS.Resource_Domain_OR_Workgr0, COLL1.Name,
        ��SYSIP.IP_Addresses0
        FROM v_CM_RES_COLL_SMS00001 COLL1
        ��INNER JOIN v_R_System SYS
        ��ON COLL1.ResourceID = SYS.ResourceID
        ��INNER JOIN v_RA_System_IPAddresses SYSIP
        ��ON COLL1.ResourceID = SYSIP.ResourceID

<!-- p.402 -->

        WHERE COLL1.IsClient = 0
        ORDER BY SYS.Resource_Domain_OR_Workgr0, COLL1.Name

Joining collection and deployment views
The following query lists all of the resources in the Configuration Manager hierarchy
that have been targeted for an advertisement, as well as the source site code,
advertisement ID and advertisement name, program name, and target collection name,
and then it sorts the data by the name of the resource. The v_FullCollectionMembership
collection view is joined to the v_Advertisement software distribution view and
v_Collection collection view by using the CollectionID column.

  SQL

        SELECT FCM.Name AS ResourceName, FCM.ResourceID,
        ��ADV.SourceSite, ADV.AdvertisementID, ADV.AdvertisementName,
        ��ADV.ProgramName, COL.Name AS CollectionName
        FROM v_FullCollectionMembership FCM INNER JOIN v_Advertisement ADV
        ��ON FCM.CollectionID = ADV.CollectionID INNER JOIN
        ��v_Collection COL ON FCM.CollectionID = COL.CollectionID
        ORDER BY FCM.Name

See also
Collection views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.403 -->

Sample queries for compliance settings
in Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join Configuration Manager
compliance settings views to each other and to views from other view categories.
Compliance settings views will most often use the CI_ID, AssignmentID, and ResourceID
columns when joining to other views.

Joining compliance settings and software
updates Views
The following query retrieves all configuration items with the type of Software Updates
(CIType_ID = 1) or Software Updates Bundle (CIType_ID = 8) that have been deployed
to clients (IsDeployed =1), listing the article ID, software update name, and software
update description. The results are sorted in descending order by article ID. The query
joins the v_ConfigurationItems and v_CITypes compliance settings views by using the
CIType_ID column, joins the v_ConfigurationItems and v_LocalizedCIProperties
compliance settings views by using the CI_ID column, and joins the
v_ConfigurationItems view with the v_UpdateInfo software updates view by using the
CI_ID column.

  SQL

      SELECT v_UpdateInfo.ArticleID, v_LocalizedCIProperties.DisplayName,
  v_LocalizedCIProperties.Description
      FROM v_ConfigurationItems INNER JOIN v_CITypes ON
  v_ConfigurationItems.CIType_ID = v_CITypes.CIType_ID
      ��INNER JOIN v_LocalizedCIProperties ON v_ConfigurationItems.CI_ID =
  v_LocalizedCIProperties.CI_ID
      ��INNER JOIN v_UpdateInfo ON v_ConfigurationItems.CI_ID =
  v_UpdateInfo.CI_ID
      WHERE (v_CITypes.CIType_ID = 1 OR v_CITypes.CIType_ID = 8) AND
  (v_ConfigurationItems.IsDeployed = 1)
      ORDER BY v_UpdateInfo.ArticleID DESC

Joining compliance settings, status, and
discovery views

<!-- p.404 -->

The following query retrieves the configuration baselines that have been evaluated on
clients, the configuration baseline description, a list of the clients that have a non-
compliant state for the configuration baseline, the IP address for the client, and the date
and time for the last compliance state message. The results are sorted by configuration
baseline name and then computer name. The query joins the
v_CIComplianceStatusDetail status message with the v_RA_System_IPAddresses
discovery view by using the ResourceID column, and it joins the
v_CI_ComplianceStatusDetail view with the v_LocalizedCIProperties compliance
settings view by using the CI_ID column. A filter could be added to the query to specify
the client computer or the configuration baseline to reduce the query results.

  SQL

      SELECT DISTINCT v_LocalizedCIProperties.DisplayName AS [Baseline Name],
      ��v_LocalizedCIProperties.Description AS [Baseline Description],
      ��v_CIComplianceStatusDetail.Netbios_Name0 AS [Computer Name],
      ��v_RA_System_IPAddresses.IP_Addresses0 AS [IP Address],
  v_CIComplianceStatusDetail.RuleSeverity,
      ��v_CIComplianceStatusDetail.LastComplianceMessageTime AS [Last
  Compliance Message]
      FROM�v_CIComplianceStatusDetail INNER JOIN v_RA_System_IPAddresses ON
      ��v_CIComplianceStatusDetail.ResourceID =
  v_RA_System_IPAddresses.ResourceID
      ��INNER JOIN v_LocalizedCIProperties ON
  v_CIComplianceStatusDetail.CI_ID = v_LocalizedCIProperties.CI_ID
      ORDER BY [Baseline Name], [Computer Name]

Joining compliance settings, status, and
assignment views
The following query retrieves the names of computers that have been targeted for an
assignment, the configuration item name assigned to the computer, the compliance
state for the item, the assignment name that contains the item, and the target collection
for the assignment. The results are sorted by the compliance state, assigned
configuration item, and then the computer name. The query joins the
v_CICurrentComplianceStatus status view to the v_CIAssignmentToCI compliance
settings view by using the CI_ID column; joins the v_CIAssignment and
v_CIAssignmentToCI compliance settings views by using the AssignmentID column;
joins the v_LocalizedCIProperties compliance settings view to the
v_CICurrentComplianceStatus view by using the CI_ID column; joins the v_StateNames
and v_CICurrentComplianceStatus status views by using the StateID and
ComplianceState columns, respectively; and joins the v_R_System discovery view to the
v_CICurrentComplianceStatus view by using the ResourceID column. The retrieved

<!-- p.405 -->

information is filtered by the topic type of 401, which includes state messages for
configuration item compliance.

  SQL

      SELECT v_R_System.Netbios_Name0 AS [Computer Name],
  v_LocalizedCIProperties.DisplayName AS [Assigned Item],
      ��v_StateNames.StateName, v_CIAssignment.AssignmentName,
  v_CIAssignment.CollectionID
      FROM v_CICurrentComplianceStatus
      ��INNER JOIN v_CIAssignmentToCI ON v_CICurrentComplianceStatus.CI_ID =
  v_CIAssignmentToCI.CI_ID
      ��INNER JOIN v_CIAssignment ON v_CIAssignmentToCI.AssignmentID =
  v_CIAssignment.AssignmentID
      ��INNER JOIN v_LocalizedCIProperties ON
  v_CICurrentComplianceStatus.CI_ID = v_LocalizedCIProperties.CI_ID
      ��INNER JOIN v_StateNames ON
  v_CICurrentComplianceStatus.ComplianceState = v_StateNames.StateID
      ��INNER JOIN v_R_System ON v_CICurrentComplianceStatus.ResourceID =
  v_R_System.ResourceID
      WHERE (v_StateNames.TopicType = 401)
      ORDER BY v_StateNames.StateName, [Assigned Item], [Computer Name]

See also
Compliance settings views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.406 -->

Sample queries for content
management in Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join the most common content
management views to other views.

Joining software distribution and package
status views
The following query lists all packages by package ID and package name, the current
status of each package, the Network Abstraction Layer (NAL) path for the distribution
point, and the last time the package was refreshed on the distribution point. The
v_Package view is joined to the v_PackageStatusDetailSumm status view and
v_DistributionPoint software distribution view by using the PackageID columns.

  SQL

        SELECT PCK.PackageID, PCK.Name as PackageName, PSD.Targeted,
        PSD.Installed, PSD.Retrying, PSD.Failed, DP.ServerNALPath,
        DP.LastRefreshTime
        FROM v_Package PCK INNER JOIN v_PackageStatusDetailSumm PSD
        ON PCK.PackageID = PSD.PackageID INNER JOIN v_DistributionPoint DP
        ON PCK.PackageID = DP.PackageID
        ORDER BY PCK.PackageID

See also
Content management views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.407 -->

Sample queries for discovery in
Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join Configuration Manager discovery
views to each other and views from other view categories. Discovery views use the
ResourceID column when joining to other views.

Joining discovery views
The following query retrieves all resources and their associated IP addresses. The query
joins the v_R_System and v_RA_System_IPAddresses discovery views by using the
ResourceID column.

  SQL

        SELECT DISTINCT SYS.Netbios_Name0, SYSIP.IP_Addresses0
        FROM v_R_System SYS INNER JOIN v_RA_System_IPAddresses SYSIP
        ��ON SYS.ResourceID = SYSIP.ResourceID
        ORDER BY SYS.Netbios_Name0

Joining resource and inventory views
The following query retrieves all resources that have a local fixed disk listed in inventory
and displays the NetBIOS name, the free disk space, and sorts the data in ascending
order by free disk space. The query joins the v_R_System discovery view and the
v_GS_LOGICAL_DISK hardware inventory view by using the ResourceID column.

  SQL

        SELECT DISTINCT SYS.Netbios_Name0, LD.FreeSpace0
        FROM v_R_System SYS INNER JOIN v_GS_LOGICAL_DISK LD
        ��ON SYS.ResourceID = LD.ResourceID
        WHERE LD.Description0 LIKE 'Local fixed disk'
        ORDER BY LD.FreeSpace0

Joining resource and collection views
The following query retrieves all resources in the All Systems collection and displays the
NetBIOS name, domain name, and associated IP addresses. The query results are sorted

<!-- p.408 -->

by NetBIOS name. The query joins the v_R_System and v_RA_System_IPAddresses
discovery views, and joins the v_FullCollectionMembership collection view by using the
ResourceID column.

  SQL

         SELECT DISTINCT SYS.Netbios_Name0, FCM.Domain, SYSIP.IP_Addresses0
         FROM v_R_System SYS INNER JOIN v_FullCollectionMembership FCM
         ON SYS.ResourceID = FCM.ResourceID
         INNER JOIN v_RA_System_IPAddresses SYSIP
         ON SYS.ResourceID = SYSIP.ResourceID
         WHERE FCM.CollectionID = 'SMS00001'
         ORDER BY SYS.Netbios_Name0

Joining resource, software updates, and status
views
The following query retrieves all resources that have performed a scan for software
updates, the last scan time, the last scan state, and the Windows Update Agent version
on the client. The query joins the v_R_System discovery view and v_UpdateScanStatus
software updates view by using the ResourceID column, and it uses LEFT OUTER JOIN
between the v_UpdateScanStatus software updates view and v_StateNames status view
by using the LastScanState and StateID columns. The state message topic types are
filtered by TopicType = 501, which indicates scan-state messages.

  ７ Note

  The state topic type, state ID, state name, and state description for all Configuration
  Manager state messages are listed in the v_StateNames view.

  SQL

         SELECT DISTINCT v_R_System.Netbios_Name0 AS [Computer Name],
         ��v_UpdateScanStatus.LastScanTime AS [Last Scan],
         ��v_UpdateScanStatus.LastWUAVersion AS [WUA Version],
         ��v_StateNames.StateName AS [Last Scan State]
         FROM v_UpdateScanStatus INNER JOIN v_R_System ON
         ��v_UpdateScanStatus.ResourceID = v_R_System.ResourceID LEFT OUTER
  JOIN
      ��v_StateNames ON v_UpdateScanStatus.LastScanState =
  v_StateNames.StateID
      WHERE (v_StateNames.TopicType = 501)

<!-- p.409 -->

See also
Discovery views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.410 -->

Sample queries for endpoint protection
in Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join the most common Endpoint
Protection views to other views.

Joining endpoint protection and collection
views
The following query lists the deployment state of the Endpoint Protection client on all
computers by using the v_GS_EPDeploymentState view. For each computer, it also adds
the client name and site code by joining by ResourceID to the
v_ClientCollectionMembers view.

  SQL

      SELECT   v_GS_EPDeploymentState_1.ResourceID,
  v_ClientCollectionMembers.Name, v_ClientCollectionMembers.SiteCode,
                       v_GS_EPDeploymentState_1.LastMessageTime,
  v_GS_EPDeploymentState_1.DeploymentState, v_GS_EPDeploymentState_1.Error,
                       v_GS_EPDeploymentState_1.ErrorCode
      FROM    v_GS_EPDeploymentState AS v_GS_EPDeploymentState_1 INNER JOIN
              v_ClientCollectionMembers ON v_GS_EPDeploymentState_1.ResourceID
  = v_ClientCollectionMembers.ResourceID

See also
Endpoint protection views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.411 -->

Sample queries for hardware inventory
in Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join Configuration Manager hardware
inventory views to other views that contain system data. Hardware inventory views use
the ResourceID column when joining to other views.

List all client OS versions
The following query lists all inventoried Configuration Manager client computers and
the operating system and service pack that are running on the client computer. The
v_GS_OPERATING_SYSTEM hardware inventory view and v_R_System discovery view are
joined by using the ResourceID column, and the results are sorted by the computer
name.

  SQL

  SELECT SYS.Name0,
           OS.Caption0,
           OS.CSDVersion0,
           OS.ResourceID
  FROM v_GS_OPERATING_SYSTEM OS
  INNER JOIN v_R_System SYS
      ON OS.ResourceID = SYS.ResourceID

List clients with hardware inventory scans more
than two days old
The following query lists all active Configuration Manager clients that have not been
scanned for hardware inventory in more than two days. The
v_GS_WORKSTATIONSTATUS hardware inventory view and
v_RA_System_SMSInstalledSites discovery view are joined to the v_R_System discovery
view by using the ResourceID column.

  SQL

        SELECT SYS.Netbios_Name0 as 'Computer Name',
        SIS.SMS_Installed_Sites0 as 'SMS Site', WS.LastHWScan,
        DATEDIFF(day,WS.LastHWScan,GETDATE()) as 'Days Since HWScan'
        FROM v_GS_WORKSTATION_STATUS WS INNER JOIN v_R_System SYS

<!-- p.412 -->

      ON WS.ResourceID = SYS.ResourceID INNER JOIN
  v_RA_System_SMSInstalledSites SIS
      ON WS.ResourceID = SIS.ResourceID
      WHERE SYS.Client_Type0 = 1 AND SYS.Active0 = 1 AND
      WS.LastHWScan < DATEADD([day],-2,GETDATE())

See also
Hardware inventory views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.413 -->

Sample queries for software inventory
in Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how the Configuration Manager software
inventory views can be joined to other views to retrieve specific data. The software
inventory views are typically joined to other views by using the ProductID, FileID, and
ResourceID columns.

Joining software inventory views
The following query lists all software files for the Configuration Manager product that
have been inventoried on Configuration Manager clients. The v_GS_SoftwareProduct
and v_GS_SoftwareFile views are joined by using the ProductID columns.

  SQL

        SELECT DISTINCT SF.FileName, SF.FileDescription, SF.FileVersion
        FROM v_GS_SoftwareProduct SP INNER JOIN v_GS_SoftwareFile SF
        ��ON SP.ProductID = SF.ProductId
        WHERE SP.ProductName = 'Configuration Manager'
        ORDER BY SF.FileName

Joining software inventory and discovery views
The following query lists all inventoried products and the associated files for a computer
with the NetBIOS name of COMPUTER1. The v_R_System and v_GS_SoftwareProduct
views are joined by using the ResourceID column, and the v_GS_SoftwareProduct and
v_GS_SoftwareFile views are joined by using the ProductID columns.

  SQL

        SELECT DISTINCT SP.ProductName, SF.FileName
        FROM v_R_System SYS INNER JOIN v_GS_SoftwareProduct SP
        ��ON SYS.ResourceID = SP.ResourceID INNER JOIN v_GS_SoftwareFile SF
        ��ON SP.ProductID = SF.ProductId
        WHERE SYS.Netbios_Name0 = 'COMPUTER1'
        ORDER BY SP.ProductName

<!-- p.414 -->

Joining software inventory, discovery, and
hardware inventory views
The following query lists all computers that have Microsoft Office installed and have less
than 1 GB of free space on the local C drive. The v_GS_SoftwareFile and
v_SoftwareProduct views are joined by the ProductID column, and the
v_GS_LOGICAL_DISK and v_R_System views are joined to v_GS_SoftwareFile by using
the ResourceID columns.

  SQL

        SELECT DISTINCT SYS.Netbios_Name0, SYS.User_Domain0, LD.FreeSpace0
        FROM v_GS_SoftwareFile SF INNER JOIN v_SoftwareProduct SP
        ��ON SF.ProductId = SP.ProductID
        ��INNER JOIN v_GS_LOGICAL_DISK LD
        ��ON SF.ResourceID = LD.ResourceID
        ��INNER JOIN v_R_System SYS
        ��ON SF.ResourceID = SYS.ResourceID
        WHERE (LD.Description0 = 'local Fixed Disk')
        ��AND (SP.ProductName LIKE 'Microsoft Office%')
        ��AND (LD.FreeSpace0 < 1000)
        ��AND (LD.DeviceID0 = 'C:')

Joining software inventory, discovery, and
software metering views
The following query lists all files that have been metered through software metering
rules and sorted first by NetBIOS name, and then by product name, and then by file
name. The v_GS_SoftwareProduct and v_MeteredFiles views are joined by the
ProductID column, and the v_GS_SoftwareProduct and v_R_System views are joined by
using the ResourceID columns.

  SQL

        SELECT SYS.Netbios_Name0, SP.ProductName, SP.ProductVersion,
        ��MF.FileName, MF.MeteredFileVersion
        FROM v_GS_SoftwareProduct SP INNER JOIN v_MeteredFiles MF
        ��ON SP.ProductID = MF.MeteredProductID INNER JOIN v_R_System SYS
        ��ON SP.ResourceID = SYS.ResourceID
        ORDER BY SYS.Netbios_Name0, SP.ProductName, MF.FileName

See also

<!-- p.415 -->

Software inventory views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.416 -->

Sample queries for asset intelligence in
Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join the most common Asset
Intelligence views to other views.

Joining asset intelligence views
The following sample query demonstrates how to join asset intelligence views to asset
intelligence hardware inventory and discovery views. Most often, the asset intelligence
hardware inventory views will be used when creating asset intelligence reports for
resources and joined to other views by using the ResourceID column. The asset
intelligence views can be joined to the asset intelligence hardware inventory views to list
product information by using the SoftwareCode column.

This sample query lists the publisher, product, installation date, and installation path for
software identified during a hardware inventory on the Workstation1 computer. The
query results are sorted by the latest installation date and then product name. The query
joins the v_GS_INSTALLED_SOFTWARE asset intelligence hardware inventory view to the
v_LU_SoftwareCode asset intelligence view by using the SoftwareCode0 and
SoftwareCode columns, respectively, and then joins the asset intelligence views,
v_LU_SoftwareList and v_LU_SoftwareCode by using the SoftwareID columns. Finally,
the query joins the v_GS_INSTALLED_SOFTWARE view with the v_R_System discovery
view by using the ResourceID column. A LEFT OUTER JOIN is used when joining the
views to display only information contained in the v_GS_INSTALLED_SOFTWARE view.

  SQL

      SELECT v_LU_SoftwareList.CommonPublisher AS Publisher,
        v_LU_SoftwareList.CommonName AS [Product Name],
        v_LU_SoftwareList.CommonVersion AS Version,
        v_GS_INSTALLED_SOFTWARE.InstallDate0 AS [Install Date],
        v_GS_INSTALLED_SOFTWARE.InstalledLocation0 AS Path
      FROM v_GS_INSTALLED_SOFTWARE LEFT OUTER JOIN v_LU_SoftwareCode ON
        v_GS_INSTALLED_SOFTWARE.SoftwareCode0 = v_LU_SoftwareCode.SoftwareCode
  INNER JOIN v_LU_SoftwareList ON
        v_LU_SoftwareList.SoftwareID = v_LU_SoftwareCode.SoftwareID LEFT OUTER
  JOIN v_R_System ON
        v_GS_INSTALLED_SOFTWARE.ResourceID = v_R_System.ResourceID
      WHERE (v_R_System.Netbios_Name0 LIKE 'Workstation1')
      ORDER BY [Install Date] DESC, [Product Name]

<!-- p.417 -->

See also
Asset intelligence views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.418 -->

Sample queries for mobile device
management in Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join mobile device management
views to other views when the device is managed by Configuration Manager. Mobile
device management views will most often be joined to other views by using the
ResourceID and DeviceClientID columns.

Joining mobile device management hardware
inventory and discovery views
The following query retrieves all mobile device Configuration Manager clients, by
NetBIOS name, the operating system, the amount of storage space on the device, and
the amount of free storage space on the device. The results are sorted by the NetBIOS
name. The query joins the v_GS_DEVICE_COMPUTER_SYSTEM mobile device
management hardware inventory view with the v_R_System discovery view by using the
ResourceID column, and it joins the v_GS_DEVICE_COMPUTER_SYSTEM and
v_GS_DEVICE_MEMORY mobile device management hardware inventory views by using
the ResourceID column.

  SQL

      SELECT v_R_System.Netbios_Name0,
      ��v_R_System.Operating_System_Name_and0,
      ��v_GS_DEVICE_MEMORY.Storage0,
      ��v_GS_DEVICE_MEMORY.StorageFree0
      FROM v_GS_DEVICE_COMPUTER_SYSTEM INNER JOIN v_R_System ON
      ��v_GS_DEVICE_COMPUTER_SYSTEM.ResourceID = v_R_System.ResourceID
      ��INNER JOIN v_GS_DEVICE_MEMORY ON
      ��v_GS_DEVICE_COMPUTER_SYSTEM.ResourceID =
  v_GS_DEVICE_MEMORY.ResourceID
      ORDER BY v_R_System.Netbios_Name0

Joining mobile device management and status
views
The following query retrieves the deployment state for all mobile device Configuration
Manager clients, including the state name and description, NetBIOS name for the
device, IP address, assigned site code, and deployment date and time. The results are

<!-- p.419 -->

sorted by the deployment state and then the NetBIOS name. The query joins the
v_DeviceClientDeploymentState mobile device management view with the
v_StateNames status view by using the StateID column. The retrieved information is
filtered by the topic type of 800, which includes state messages for client deployment.

  SQL

      SELECT v_StateNames.StateName AS [Deployment State],
      ��v_StateNames.StateDescription AS Description,
      ��v_DeviceClientDeploymentState.DeviceNetBiosName AS [Device Name],
      ��v_DeviceClientDeploymentState.IPAddress AS [IP Address],
      ��v_DeviceClientDeploymentState.AssignedSiteCode AS [Assigned Site],
      ��v_DeviceClientDeploymentState.DeviceDeploymentTime AS [Time
  Deployed]
      FROM v_DeviceClientDeploymentState INNER JOIN v_StateNames ON
      ��v_DeviceClientDeploymentState.DeviceDeploymentState =
  v_StateNames.StateID
      WHERE (v_StateNames.TopicType = 800)
      ORDER BY [Deployment State], [Device Name]

See also
Mobile device management views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.420 -->

Sample queries for operating system
deployment in Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join operating system deployment
views to each other and to compliance settings views. You can join the operating system
deployment views to other operating system deployment views and application
management views by using the view column that contains the package ID, which might
have different column names depending on the view. You can join the operating system
deployment views to compliance settings views by using the CI_ID column, and they can
be joined to discovery views by using the ResourceID column.

Joining operating system deployment and
application management views
The following query lists all task sequence packages, by package ID and package name,
the associated boot image package, by package ID and package name, and the source
path for the boot image package. The query results are sorted by the task sequence
package ID. A LEFT OUTER JOIN is used to join the v_TaskSequencePackage and
v_BootImagePackage operating system deployment views by using the BootImageID
and PackageID columns, respectively.

  SQL

        SELECT DISTINCT
        ��v_TaskSequencePackage.PackageID AS [Task Sequence Package ID],
        ��v_TaskSequencePackage.Name AS [Task Sequence Package Name],
        ��v_TaskSequencePackage.BootImageID AS [Boot Image Package ID],
        ��v_BootImagePackage.Name AS [Boot Image Package Name],
        ��v_BootImagePackage.PkgSourcePath AS [Boot Image Package Source Path]
        FROM v_TaskSequencePackage LEFT OUTER JOIN v_BootImagePackage ON
        ��v_TaskSequencePackage.BootImageID = v_BootImagePackage.PackageID
        ORDER BY [Task Sequence Package ID]

Joining operating system deployment and
compliance settings views
The following query lists all operating system deployment boot image packages, by
package ID and package name, the drivers that are contained in the boot image

<!-- p.421 -->

package, and the source path for the driver. The query results are sorted by the boot
image package ID and then by the driver name. The v_BootImagePackage and
v_BootImagePackage_References operating system deployment views are joined by
using the PackageID and PkgID columns, respectively; the
v_BootImagePackage_References view is joined to the v_ConfigurationItems
compliance settings view by using the CI_ID column; and the v_ConfigurationItems view
is joined to the v_LocalizedCIProperties compliance settings view by using the CI_ID
column.

  SQL

        SELECT v_BootImagePackage.PackageID AS [Boot Image Package ID],
        ��v_BootImagePackage.Name AS [Boot Image Package Name],
        ��v_LocalizedCIProperties.DisplayName AS [Driver Name],
        ��v_BootImagePackage_References.SourcePath AS [Driver Source Path]
        FROM v_BootImagePackage INNER JOIN v_BootImagePackage_References ON
        ��v_BootImagePackage.PackageID = v_BootImagePackage_References.PkgID
        ��INNER JOIN v_ConfigurationItems ON
        ��v_BootImagePackage_References.CI_ID = v_ConfigurationItems.CI_ID
        ��INNER JOIN v_LocalizedCIProperties ON
        ��v_ConfigurationItems.CI_ID = v_LocalizedCIProperties.CI_ID
        ORDER BY [Boot Image Package ID], [Driver Name]

See also
Operating system deployment views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.422 -->

Sample queries for power management
in Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join power management views to
other views.

Joining power management views to discovery
views
The following query lists all computers, by Netbios name, that are excluded from power
management because the user chose to exclude them.

The query returns the Netbios name and the domain of the computer and also the client
opt-out setting where this value is 1 (indicating that the computer has been excluded
from power management).

  SQL

        SELECT           v_R_System.Name0, v_R_System.Resource_Domain_OR_Workgr0,

  v_GS_POWER_MANAGEMENT_CLIENTOPTOUT_SETTINGS.IsClientOptOut0
      FROM            v_R_System INNER JOIN
                               v_GS_POWER_MANAGEMENT_CLIENTOPTOUT_SETTINGS ON
                               v_R_System.ResourceID =
  v_GS_POWER_MANAGEMENT_CLIENTOPTOUT_SETTINGS.ResourceID
      WHERE
  (v_GS_POWER_MANAGEMENT_CLIENTOPTOUT_SETTINGS.IsClientOptOut0 = 1)

See also
Power management views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.423 -->

Sample queries for the query view in
Configuration Manager
Article • 10/10/2022

The following sample query demonstrates how the query view can be joined to a
security view. In most cases, the v_Query view won't be used in reports.

Joining query and security views
The following query lists the query ID, query name, user name, and instance permissions
for the user on the query object. The v_Query view is joined to the
v_UserInstancePermNames security view by using the QueryID from v_Query and
InstanceKey from v_UserInstancePermNames. Because there might be other secured
objects with the same value as the InstanceKey (for example, MCM00001 could be a
custom query or a package), the query also filters specifically for query objects by using
the WHERE clause and an ObjectKey value of 7.

  SQL

        SELECT Q.QueryID, Q.Name AS QueryName, UIP.UserName, UIP.PermissionName
        FROM v_Query Q INNER JOIN v_UserInstancePermNames UIP
        ON Q.QueryID = UIP.InstanceKey
        WHERE UIP.ObjectKey = 7
        ORDER BY Q.Name, UIP.UserName

See also
Query views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.424 -->

Sample queries for security in
Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join security views to other views.

Joining security views
The following query lists the user name, object name, and class permission name that
the user has on the secured object. The v_SecuredObject view is joined to the
v_UserClassPermNames view by using the ObjectKey column.

  SQL

        SELECT UCP.UserName, SO.ObjectName, UCP.PermissionName
        FROM v_SecuredObject SO INNER JOIN v_UserClassPermNames UCP
        ON SO.ObjectKey = UCP.ObjectKey
        ORDER BY UCP.UserName, SO.ObjectName, UCP.PermissionName

Joining security and collection views
The following query lists all collections, by collection ID and collection name, the user
name, and the instance permissions for that collection. The v_Collection collection view
is joined to the v_UserInstancePermNames security view by using the CollectionID
column and the InstanceKey column, respectively.

  SQL

        SELECT COL.CollectionID, COL.Name AS CollectionName, UIP.UserName,
        UIP.PermissionName
        FROM v_Collection COL INNER JOIN v_UserInstancePermNames UIP
        ON COL.CollectionID = UIP.InstanceKey
        ORDER BY COL.CollectionID

The output from the preceding query will list all instance permissions for individual
collections. If a user has class permissions for the collections object (which includes all
instances), another query will need to be run to get all of the permissions for users on
the collections object. (An object key of 1 refers to the collection object.)

The following query can be run from the v_UserClassPermNames view to list all user
class permissions for the collections object.

<!-- p.425 -->

  SQL

        SELECT UserName, PermissionName
        FROM v_UserClassPermNames
        WHERE ObjectKey = 1

When using the two preceding queries together, a list of user permissions for all
collection classes and instances can be obtained.

See also
Security views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.426 -->

Sample queries for site administration in
Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how the Configuration Manager site
administration views can be joined to other views to retrieve specific data.

Joining site administration views
The following sample query demonstrates how to join a site view to another site view.
This query lists the boundaries for each site in the Configuration Manager hierarchy, the
type of boundary, the boundary value, whether the connection is fast or slow, and the
boundary description. The v_Site and v_BoundaryInfo site views are joined by using the
SiteCode column. The query results are sorted by site code, boundary type, and then
value. The CASE function is used to take a numeric value for boundary type and
connection speed and to provide friendly names based on the value.

  SQL

      SELECT v_Site.SiteCode, v_Site.ServerName,
      ��CASE v_BoundaryInfo.BoundaryType
      ����WHEN 0 THEN 'IP subnet'
      ����WHEN 1 THEN 'Active Directory site'
      ����WHEN 2 THEN 'IPv6 Prefix'
      ����WHEN 3 THEN 'IP address range'
      ��END AS [Boundary Type], v_BoundaryInfo.Value,
      ��CASE v_BoundaryInfo.BoundaryFlags
      ����WHEN 0 THEN 'Fast'
      ����WHEN 1 THEN 'Slow'
      END AS Connection, v_BoundaryInfo.DisplayName AS Description
      FROM v_BoundaryInfo INNER JOIN v_Site ON v_BoundaryInfo.SiteCode =
  v_Site.SiteCode
      ORDER BY v_Site.SiteCode, [Boundary Type], v_BoundaryInfo.Value

See also
Site administration views in Configuration Manager

Feedback

<!-- p.427 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.428 -->

Sample queries for software metering in
Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join the most common software
metering views to other views.

Joining software metering, software inventory,
and discovery views
The following query lists all resources that have run metered files, including the resource
name, file ID, file name, file version, and start time. The v_MeterData software metering
view is joined to the v_ProductFileInfo software inventory view by using the FileID
column and to the v_R_System discovery view by using the ResourceID column.

  SQL

        SELECT SYS.Netbios_Name0, PFI.FileID, PFI.FileName,
        PFI.FileVersion, MD.StartTime
        FROM v_MeterData MD INNER JOIN v_ProductFileInfo PFI
        ON MD.FileID = PFI.FileID INNER JOIN v_R_System SYS
        ON MD.ResourceID = SYS.ResourceID
        ORDER BY SYS.Netbios_Name0, PFI.FileName

Joining software metering, status, and software
inventory views
The following query lists all users who have run metered files. The query returns the user
domain, user name, file name, file version, usage count, total time of usage, and the last
time the file was used. The v_MeteredUser software metering view is joined to the
v_MonthlyUsageSummary status view by using the MeteredUserID column. The
v_MonthlyUsageSummary status view is joined to the v_GS_SoftwareFile software
inventory view by using the FileID column.

  SQL

        SELECT MU.Domain, MU.UserName, SF.FileName, SF.FileVersion,
        MUS.UsageCount, MUS.UsageTime, MUS.LastUsage
        FROM v_MeteredUser MU INNER JOIN v_MonthlyUsageSummary MUS
        ON MU.MeteredUserID = MUS.MeteredUserID INNER JOIN

<!-- p.429 -->

       v_GS_SoftwareFile SF ON MUS.FileID = SF.FileID
       ORDER BY MU.Domain, MU.UserName, SF.FileName

See also
Software metering views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.430 -->

Sample queries for software updates in
Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join software updates views to each
other and to views from other view categories. Software updates views will most often
use the CI_ID column when joining to other views.

Joining software updates, discovery, and status
views
The following query retrieves the article ID, bulletin ID, software update title, last
enforcement state for the update, the time of the last enforcement check, and the time
that the last enforcement state message was sent by the Computer1 client. The results
are sorted by state name and then by the last modified date for the software update.
The query joins the v_UpdateComplianceStatus status view with the v_UpdateInfo
software updates view by using the CI_ID column, the v_UpdateComplianceStatus
status view with the v_R_System discovery view by using the ResourceID column, and
the v_UpdateComplianceStatus status view with the v_StateNames status view by using
the LastEnforcementStatus and StateID columns, respectively. The retrieved information
is filtered by the topic type of 402, which includes state messages for configuration item
enforcement, and a computer with the NetBIOS name of Computer1.

  SQL

      SELECT v_UpdateInfo.ArticleID, v_UpdateInfo.BulletinID,
  v_UpdateInfo.Title,
      ��v_StateNames.StateName,
  v_UpdateComplianceStatus.LastStatusCheckTime,
      ��v_UpdateComplianceStatus.LastEnforcementMessageTime
      FROM v_R_System INNER JOIN v_UpdateComplianceStatus ON
      ��v_R_System.ResourceID = v_UpdateComplianceStatus.ResourceID INNER
  JOIN v_UpdateInfo ON
      ��v_UpdateComplianceStatus.CI_ID = v_UpdateInfo.CI_ID INNER JOIN
  v_StateNames ON
      ��v_UpdateComplianceStatus.LastEnforcementMessageID =
  v_StateNames.StateID
      WHERE (v_StateNames.TopicType = 402) AND (v_R_System.Netbios_Name0 LIKE
  'Computer1')
      ORDER BY v_StateNames.StateName, v_UpdateInfo.DateLastModified

<!-- p.431 -->

Joining software updates and compliance
settings views
The following query retrieves the software update deployments, by assignment ID
(software update deployment ID) and assignment name (deployment name); the
software updates that are contained in the deployment, by article ID, bulletin ID, and
software update title; and the target collection for the deployment. The results are
sorted by the assignment ID and then by article ID. The query joins the v_UpdateInfo
software updates view with the v_CIAssignmentToCI compliance settings view by using
the CI_ID column, and it joins the v_CIAssignmentToCI view to the v_CIAssignment
compliance settings view by using the AssignmentID column.

  SQL

      SELECT v_CIAssignment.AssignmentID, v_CIAssignment.AssignmentName,
      ��v_UpdateInfo.ArticleID, v_UpdateInfo.BulletinID, v_UpdateInfo.Title,
      ��v_CIAssignment.CollectionName, v_CIAssignment.CollectionID
      FROM v_UpdateInfo INNER JOIN v_CIAssignmentToCI ON
      ��v_UpdateInfo.CI_ID = v_CIAssignmentToCI.CI_ID INNER JOIN
  v_CIAssignment ON
      ��v_CIAssignmentToCI.AssignmentID = v_CIAssignment.AssignmentID
      ORDER BY v_CIAssignment.AssignmentID, v_UpdateInfo.ArticleID

See also
Software updates views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.432 -->

Sample queries for status and alerts in
Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join some of the most commonly
used status message views to other views.

Joining the status message and status message
attribute views
The following query lists status messages, by status message ID, the component that
created the status message, the count of the status message reported by the
component, the attribute value, and the computer name where the component is
installed. The attribute value could be a package ID for a package status message, a
collection ID for a collection status message, a user name for a status message
concerning a user, and so forth. The v_StatusMessage view is joined to the
v_StatMsgAttributes view by using the RecordID column.

  SQL

        SELECT SM.Component, SM.MessageID,
        ��COUNT(*) AS 'Count', SMA.AttributeValue, SM.MachineName
        FROM v_StatusMessage SM LEFT OUTER JOIN v_StatMsgAttributes SMA
        ��ON SM.RecordID = SMA.RecordID
        GROUP BY SM.Component, SM.MessageID, SM.MachineName, SMA.AttributeValue
        ORDER BY SM.Component, SM.MessageID

Joining the distribution point status and
package views
The following query lists the distribution points that have been selected for each
package and the installation status for the distribution point. The
v_PackageStatusDistPointSumm view is joined to the v_Package view by using the
PackageID column.

  SQL

        SELECT DPS.PackageID, PCK.Name, PCK.SourceSite,
        ��DPS.ServerNALPath, DPS.InstallStatus
        FROM v_PackageStatusDistPointsSumm DPS INNER JOIN v_Package PCK

<!-- p.433 -->

        ��ON DPS.PackageID = PCK.PackageID
        ORDER BY DPS.PackageID

Joining the deployment status, deployment,
collection, and resource views
The following query lists the clients that have been targeted for a deployment, the
deployment ID, the deployment name, the collection that was targeted in which the
client is a member, and the last status message received from the client for the
deployment. The v_ClientAdvertisementStatus view is joined to the v_R_System view by
using the ResourceID column and the v_Advertisement view by using the
AdvertisementID column. The v_Advertisement view is joined to the v_Collection view
by using the CollectionID column. The results are sorted by NetBIOS name and then by
advertisement ID.

  SQL

        SELECT SYS.Netbios_Name0, ADV.AdvertisementID, ADV.AdvertisementName,
        ��COL.Name AS TargetedCollection, CAS.LastStatusMessageIDName
        FROM v_ClientAdvertisementStatus CAS INNER JOIN v_R_System SYS
        ��ON CAS.ResourceID = SYS.ResourceID INNER JOIN v_Advertisement ADV
        ��ON CAS.AdvertisementID = ADV.AdvertisementID INNER JOIN
        ��v_Collection COL ON ADV.CollectionID = COL.CollectionID
        ORDER BY SYS.Netbios_Name0, ADV.AdvertisementID

Joining the software metering status, software
inventory, and resource views
The following query lists the software metering usage data for files defined in the
software metering rules. The NetBIOS name of the client, file name, file path, how many
times the file has run on the computer, and last usage date are retrieved. The results are
sorted by NetBIOS name, and then file name, and then file path. The
v_MonthlyUsageSummary view is joined to the v_R_System view by using the
ResourceID column and to the v_GS_SoftwareFile view by using the FileID column.

  SQL

        SELECT SYS.Netbios_Name0, SF.FileName, SF.FilePath,
        ��MUS.UsageCount, MUS.LastUsage
        FROM v_MonthlyUsageSummary MUS INNER JOIN v_R_System SYS
        ��ON MUS.ResourceID = SYS.ResourceID INNER JOIN v_GS_SoftwareFile SF

<!-- p.434 -->

        ��ON MUS.FileID = SF.FileID
        ORDER BY SYS.Netbios_Name0, SF.FileName, SF.FilePath

Joining the software updates status and
discovery views
The following query lists the enforcement state reported by the VISTACLIENT1 client
computer for all software updates that have been assigned to the client. The article ID,
bulletin ID, and title for the software update are listed, as well as the enforcement state,
the date for the last enforcement scan on the client, and the date when the last
enforcement state message was sent from the client. The results are filtered by a topic
type of 402, which is the topic type for enforcement state messages, and for the
VISTACLIENT1 client. The results are also sorted by state name, and then by the date the
software update was last modified. The v_UpdateComplianceStatus status view is joined
to the v_R_System discovery view by using the ResourceID column. The
v_UpdateComplianceStatus view is joined to the v_UpdateInfo software updates view
by using the CI_ID column. The v_UpdateComplianceStatus view is joined to the
v_StateNames status view by using the LastEnforcementMessageID and StateID
columns, respectively.

  SQL

      SELECT v_UpdateInfo.ArticleID, v_UpdateInfo.BulletinID,
  v_UpdateInfo.Title,
      ��v_StateNames.StateName,
  v_UpdateComplianceStatus.LastStatusCheckTime,
      ��v_UpdateComplianceStatus.LastEnforcementMessageTime
      FROM v_R_System INNER JOIN v_UpdateComplianceStatus ON
      ��v_R_System.ResourceID = v_UpdateComplianceStatus.ResourceID INNER
  JOIN v_UpdateInfo ON
      ��v_UpdateComplianceStatus.CI_ID = v_UpdateInfo.CI_ID INNER JOIN
  v_StateNames ON
      ��v_UpdateComplianceStatus.LastEnforcementMessageID =
  v_StateNames.StateID
      WHERE (v_StateNames.TopicType = 402) AND (v_R_System.Netbios_Name0 LIKE
  'VISTACLIENT1')
      ORDER BY v_StateNames.StateName, v_UpdateInfo.DateLastModified

See also
Status and alert views in Configuration Manager

<!-- p.435 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.436 -->

Sample queries for Wake On LAN in
Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join Wake On LAN views to
application management, discovery, and compliance settings views. The Wake On LAN
views are most often joined to other views by using the ObjectID and ResourceID
columns, and to other Wake On LAN views by using the ObjectType column.

Joining Wake On LAN, application
management, and compliance settings views
The following query retrieves the Configuration Manager object type, the deployment ID
or advertisement ID, and the name for all objects that have Wake On LAN enabled. The
results are sorted by object type and then by object name. The query joins the
v_WOLGetSupportedObjects and v_WOLEnabledObjects Wake On LAN views by using
the ObjectType column; joins the v_WOLEnabledObjects view with the v_Advertisement
software distribution view by performing a LEFT OUTER JOIN on the ObjectType and
AdvertisementID columns, respectively; and joins the v_WOLEnabledObjects view with
the v_CIAssignment desired configuration management view by performing a LEFT
OUTER JOIN on the ObjectType and Assignment_UniqueID columns, respectively. Using
the LEFT OUTER JOIN retrieves all records from the v_WOLEnabledObjects view and
only the associated records from the v_Advertisement and v_CIAssignment views.

  SQL

      SELECT v_WOLGetSupportedObjects.Name AS [Object Type],
      v_CIAssignment.AssignmentID AS DeploymentID,
  v_Advertisement.AdvertisementID
      ��v_WOLEnabledObjects.ObjectName AS Name
      FROM v_WOLGetSupportedObjects INNER JOIN v_WOLEnabledObjects ON
      ��v_WOLGetSupportedObjects.ObjectType = v_WOLEnabledObjects.ObjectType
      ��LEFT OUTER JOIN v_Advertisement ON
      ��v_WOLEnabledObjects.ObjectID = v_Advertisement.AdvertisementID
      ��LEFT OUTER JOIN v_CIAssignment ON
      ��v_WOLEnabledObjects.ObjectID = v_CIAssignment.Assignment_UniqueID
      ORDER BY [Object Type], Name

Joining Wake On LAN and discovery views

<!-- p.437 -->

The following query retrieves client computers, by NetBIOS name, that have been
targeted for an advertisement or deployment with Wake On LAN enabled, as well as the
name of the advertisement or deployment, the type of object, and the advertisement ID
or deployment ID. The results are sorted by NetBIOS name, object type, and then object
ID. The query joins the v_WOLTargetedClients Wake On LAN view with the v_R_System
discovery view by using the ResourceID column, joins the v_WOLEnabledObjects and
v_WOLTargetedClients Wake On LAN views by using the ObjectID column, joins the
v_WOLGetSupportedObjects and v_WOLEnabledObjects Wake On LAN views by using
the ObjectType column.

  SQL

      SELECT v_R_System.Netbios_Name0 AS Computer,
  v_WOLEnabledObjects.ObjectName,
      ��v_WOLGetSupportedObjects.Name AS ObjectType,
  v_WOLEnabledObjects.ObjectID
      FROM v_WOLTargetedClients INNER JOIN v_R_System ON
      ��v_WOLTargetedClients.ResourceID = v_R_System.ResourceID INNER JOIN
  v_WOLEnabledObjects ON
      ��v_WOLTargetedClients.ObjectID = v_WOLEnabledObjects.ObjectID INNER
  JOIN v_WOLGetSupportedObjects ON
      ��v_WOLEnabledObjects.ObjectType = v_WOLGetSupportedObjects.ObjectType
      ORDER BY Computer, v_WOLGetSupportedObjects.ObjectType,
  v_WOLEnabledObjects.ObjectID

See also
Wake On LAN views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.438 -->

SQL statement reference for
Configuration Manager reports
Article • 10/10/2022

Many useful Microsoft SQL Server statements can be used when creating
Configuration�Manager reports, and they are briefly described in this section. To follow
this discussion, you should have a basic level of SQL query statement knowledge and
the ability to write queries such as the following:

  SQL

  SELECT Name, Comment, CollectionID

  FROM v_Collection

  WHERE Name LIKE 'All Windows%'

  ORDER BY Name

For information about how to write basic queries, see your SQL Server documentation.

Aggregate functions
Aggregate functions (such as SUM, AVG, COUNT, COUNT(*), MAX, and MIN) generate
summary values in query result sets. An aggregate function (with the exception of
COUNT(*)) processes all the selected values in a single column to produce a single result
value. Aggregate functions can be applied to all rows in a view, to a subset of the view
specified by a WHERE clause, or to one or more groups of rows in the view. When an
aggregate function is applied, a single value is generated from each set of rows.

  ） Important

  Be aware that NULL values are not included in aggregate results. For example, if
  you have 100 records and 8 of them have a NULL column value for the property
  that you are counting, the count will return only 92 results.

An example of using the COUNT(*) aggregate function is displayed in the following
query (from the Count clients for each site predefined report) and example result set.

  SQL

<!-- p.439 -->

  SELECT v_Site.SiteCode, v_Site.SiteName, v_Site.ReportingSiteCode,

  Count(SMS_Installed_Sites0) AS 'Count'

  FROM v_Site, v_RA_System_SMSInstalledSites InsSite

  WHERE v_Site.SiteCode = InsSite.SMS_Installed_Sites0

  GROUP BY SiteCode, SiteName, ReportingSiteCode

  ORDER BY SiteCode

                                                                     ﾉ   Expand table

 SiteCode            SiteName          ReportingSiteCode                 Count

 ABC                 ABC Site                                            928

 123                 123 Site          ABC                               1010

Date and Time functions
Many built-in reports use the Date and Time functions. The most common functions
used are the GETDATE, DATEADD, DATEDIFF, and DATEPART.

GETDATE ()
The GETDATE function produces the current date and time in SQL Server internal format
for datetime values. GETDATE takes the NULL parameter ().

The following example results in the current system date and time:

  SQL

  SELECT GETDATE()

                                                                     ﾉ   Expand table

 (no column name)

 2005-05-29 10:10:03.001

<!-- p.440 -->

DATEADD (datepart, number, date)
The DATEADD function returns a new datetime value based on adding an interval to the
specified date.

Datepart is the parameter that specifies on which part of the date to return a new value
(for example, year, month, day, hour, minute, and so forth), number is the value used to
increment datepart, and date is the starting date.

The following example results in a date that is two days from May 29, 2005:

  SQL

  SELECT DATEADD([day], 2, '2005-05-29 10:10:03.001')

                                                                           ﾉ   Expand table

 (no column name)

 2005-05-31 10:10:03.001

DATEDIFF (datepart , startdate , enddate)
The DATEDIFF function returns the number of date and time boundaries crossed
between two specified dates.

Datepart is the parameter that specifies on which part of the date to return a new value
(for example, year, month, day, hour, minute, and so forth), startdate is the starting date,
enddate is the ending date.

The following example results in the number of minutes between the first and second
dates:

  SQL

  SELECT DATEDIFF (minute, '2005-05-29 10:10:03.001',

  '2005-06-12 09:28:11.111')

                                                                           ﾉ   Expand table
