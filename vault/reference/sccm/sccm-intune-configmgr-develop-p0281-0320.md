---
title: "Configuration Manager SDK documentation — pages 281-320"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0281-0320
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0281-0320
family: sccm
documentKind: "doc"
abstract: "Lists information about the sound devices found on Configuration Manager clients. The view can be joined with other views by using the ResourceID column. v_GS_SYSTEM Lists information about the active Configuration Manager clients, including domain, name, system role, system typ"
---

# Configuration Manager SDK documentation — pages 281-320

<!-- p.281 -->

Lists information about the sound devices found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column.

v_GS_SYSTEM
Lists information about the active Configuration Manager clients, including domain,
name, system role, system type, and more. The view can be joined with other views by
using the ResourceID column.

v_GS_SYSTEM_ACCOUNT
Lists information about the system accounts on Windows computers. The view can be
joined with other views by using the ResourceID column.

v_GS_SYSTEM_CONSOLE_USAGE
Lists all system console usage information for Configuration Manager clients found
through Asset Intelligence by polling the Windows System Security Event Log. The view
is also listed and described in the Asset intelligence views in Configuration Manager
topic. The view can be joined with other views by using the ResourceID column.

v_GS_SYSTEM_CONSOLE_USAGE_MAXGROUP
Lists all system console usage information for Configuration Manager clients found
through Asset Intelligence by polling the Windows System Security Event Log. This view
contains a subset of information from the v_GS_SYSTEM_CONSOLE_USAGE view. The
view is also listed and described in the Asset intelligence views in Configuration
Manager topic. The view can be joined with other views by using the ResourceID
column.

v_GS_SYSTEM_CONSOLE_USER
Lists all system console user information for Configuration Manager clients found
through Asset Intelligence by polling the Windows System Security Event Log. The view
is also listed and described in the Asset intelligence views in Configuration Manager
topic. The view can be joined with other views by using the ResourceID column.

v_GS_SYSTEM_DEVICES

<!-- p.282 -->

Lists information about the system devices found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column.

V_GS_SYSTEM_DRIVER
Lists information about the drivers found on Configuration Manager clients. The view
can be joined with other views by using the ResourceID column.

v_GS_SYSTEM_ENCLOSURE
Lists information about the system enclosure found on Configuration Manager clients,
including chassis types, serial number, SMBIOS asset tag, and so on. The view can be
joined with other views by using the ResourceID column.

v_GS_SYSTEM_ENCLOSURE_UNIQUE
Lists information about the unique system enclosures found on Configuration Manager
clients, including serial number, SMBIOS asset tag, and so on. This view contains a
subset of information from the v_GS_SYSTEM_ENCLOSURE view. The view can be joined
with other views by using the ResourceID column.

v_GS_SYSTEMBOOTDATA
Lists information about the computer boot times. This includes BIOS duration, boot
duration, event log start, group policy duration, system start time and update duration.

The view can be joined with other views by using the ResourceID column.

v_GS_TAPE_DRIVE
Lists information about the tape drives found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column.

v_GS_TIME_ZONE
Lists information about the time zone settings on clients. This view can be joined with
other views by using the ResourceID column.

v_GS_TPM

<!-- p.283 -->

Lists information about the Trusted Platform Model (TPM) chip when it is found on client
computers. This view can be joined with other views by using the ResourceID column.

v_GS_TS_ISSUED_LICENSE
Lists information about issued Terminal Services licenses. The view can be joined with
other views by using the ResourceID column.

v_GS_TS_LICENSE_KEY_PACK
Lists information about Terminal Services key packs found on client computers. The view
can be joined with other views by using the ResourceID column.

v_GS_USB_CONTROLLER
Lists information about the USB controllers found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column.

v_GS_USB_DEVICE
Lists information about the USB devices found on Configuration Manager clients
through Asset Intelligence. The view is also listed and described in the Asset intelligence
views in Configuration Manager topic. The view can be joined with other views by using
the ResourceID column.

v_GS_USER_PROFILE
Lists information about user profiles found on client computers including the path to
the profile, roaming preferences and more. This view can be joined to other views by
using the ResourceID column.

v_GS_VIDEO_CONTROLLER
Lists information about the video controllers found on Configuration Manager clients.
The view can be joined with other views by using the ResourceID column.

v_GS_VIRTUAL_APPLICATION_PACKAGES
Lists virtual application package information found on Configuration Manager clients.
The view can be joined with other views by using the ResourceID column.

<!-- p.284 -->

v_GS_VIRTUAL_APPLICATIONS
Lists information about virtual applications found on Configuration Manager clients. The
view can be joined with other views by using the ResourceID column.

v_GS_VIRTUAL_MACHINE
Lists information about the virtual machines found on Configuration Manager clients.
The view can be joined with other views by using the ResourceID column.

V_GS_WEBAPP_APPLICATION
Lists information about Web applications found on clients. This includes the name and
URL to the application. The view can be joined with other views by using the ResourceID
column.

v_GS_WINDOWS8_APPLICATION
Lists the installed modern Windows applications found on client computers. This view
can be joined to other views by using the ResourceID column.

v_GS_WINDOWS8_APPLICATION_USER_INFO
Lists user account information for the modern Windows applications found on client
computers. This view can be joined to other views by using the ResourceID column.

v_GS_WINDOWSUPDATEAGENTVERSION
Lists information about the Windows Update Agent found on Configuration Manager
clients. The view can be joined with other views by using the ResourceID column.

v_GS_WORKSTATION_STATUS
Lists workstation status information for Configuration Manager clients, including last
hardware scan, default locale ID, time zone offset, and so on. The view can be joined
with other views by using the ResourceID column.

v_GS_WRITE_FILTER_STATE

<!-- p.285 -->

Lists information about whether the write filter is enabled on Windows Embedded
devices. The view can be joined with other views by using the ResourceID column.

v_GS_X86_PC_MEMORY
Lists information about the memory found on Configuration Manager clients. The view
can be joined with other views by using the ResourceID column.

v_Network_DATA_Serialized
Lists information about the network item found on Configuration Manager clients, and
organized by ResourceID and then by GroupID. The GroupID column starts at 1 for the
first network item for a client and increments by 1 for each additional network item. The
view lists the IP address for the default gateway, the IP address for the DHCP server,
DNS domain, IP address, MAC address, and so on. The view can be joined with other
views by using the ResourceID column.

v_SystemInventoryChanges
Lists information about the inventory changes on Configuration Manager clients,
including name, MIF class, time stamp, change type, and more. The view can be joined
with other views by using the ResourceID column.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.286 -->

Software inventory views in
Configuration Manager
Article • 10/10/2022

The Configuration Manager software inventory views contain information about the files
and their associated products that are found on Configuration Manager clients during
software inventory scanning. Software inventory, by default, will scan for all executable
file types (*.exe) on clients. The software inventory options are configured for the site
and will determine which files are inventoried and how much information is collected
about each. For more information, see How to configure software inventory in the
Configuration Manager Documentation Library.

Software inventory view schema
There is not a specific software inventory schema view, but the following query joins the
v_GS_SoftwareProduct and v_FullCollectionMembership views to generate the software
inventory view schema by product name for the All Systems collection:

  SELECT MIN(PRD.ProductID) AS ProductID, PRD.ProductName,

  PRD.ProductVersion, COUNT(DISTINCT PRD.ResourceID) AS 'Count'

  FROM v_GS_SoftwareProduct PRD INNER JOIN v_FullCollectionMembership FCM

  ON PRD.ResourceID = FCM.ResourceID

  WHERE FCM.CollectionID = 'SMS00001'

  GROUP BY PRD.ProductName, PRD.ProductVersion

  ORDER BY PRD.ProductName

Software inventory views
Some of the software inventory views created in Configuration Manager store system
data, and others contain general product and file data. As a general rule, view names
that start with v_GS contain data for Configuration Manager clients and can be joined to
other views that contain system data by using the ResourceID for that client. Software

<!-- p.287 -->

inventory views that start with v_ contain file and product data, but it is not specific to
individual computers. The software inventory views are described in this section.

v_GS_CollectedFile
Lists the files collected by software inventory on each Configuration Manager client. The
view can be joined to other views by using the ResourceID column.

v_GS_LastSoftwareScan
Lists the last time each Configuration Manager client was scanned for software
inventory. The view can be joined to other views by using the ResourceID column.

v_GS_Mapped_Add_Remove_Programs
Lists the software applications on each Configuration Manager client that is mapped to
list of installed software in Windows Control Panel. The view can be joined to other
views by using the ResourceID column.

v_GS_SoftwareFile
Lists the files and associated product IDs on each Configuration Manager client. The
view can be joined to other views by using the ResourceID column.

v_GS_SoftwareProduct
Lists the products found on each Configuration Manager client. The view can be joined
to other views by using the ResourceID column.

v_GS_UnknownFile
Lists the files that are not associated with an identified product, on each Configuration
Manager client. The view can be joined to other views by using the ResourceID column.

v_ProductFileInfo
Lists all of the distinct files, by file ID, that have been inventoried in the site, including
file name, description, file size, file version, and so on. The view can be joined to other
views by using the FileID column.

<!-- p.288 -->

v_SoftwareFile
Lists all of the distinct files, by file ID, that have been inventoried in the site, including
file name, file version, description, file size, and associated product. The view can be
joined to other views by using the FileID and ProductID columns.

v_SoftwareProduct
Lists all of the distinct software products that have been inventoried in the site. The view
can be joined to other views by using the ProductID column.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.289 -->

Asset intelligence views in Configuration
Manager
Article • 10/04/2022

The Asset Intelligence views in Configuration Manager contain information about
software applications that are in use throughout the Configuration Manager hierarchy,
software license management in the enterprise, Asset Intelligence configuration settings,
and so on. The Asset Intelligence information is retrieved from clients only after the
specific reporting classes have been enabled. By default, the Asset Intelligence reporting
classes are disabled, and until the classes are enabled and Configuration Manager
clients collect hardware inventory, these views will not contain any information. Other
Asset Intelligence views contain information from the Asset Intelligence catalog,
summary information, and product licensing information. There are external
dependencies and dependencies within the product that should be considered before
implementing Asset Intelligence or using the SQL views.

For information about the Asset Intelligence prerequisites, see Prerequisites for asset
intelligence in Configuration Manager in the Configuration Manager Documentation
Library.

For the step-by-step procedure for enabling Asset Intelligence, see Configuring asset
intelligence in Configuration Manager in the Configuration Manager Documentation
Library.

The following sections provide detailed information about Asset Intelligence views,
Asset Intelligence hardware inventory views, and Asset Intelligence status views.

Asset intelligence views
The Asset Intelligence views are described in this section.

v_AI_MVLS
Lists the Microsoft Volume Licensing (MVLS) product pools, by MLSProductPool, and
the product family name, version, effective quantity, and unresolved quantity. It is
unlikely that this view will be joined to other views.

v_AI_NON_MS_LICENSE

<!-- p.290 -->

Lists the non-Microsoft product license information, including the product name,
publisher, version, language, effective quantity, date of purchase, and so on. It is unlikely
that this view will be joined to other views.

v_AIProxy
Lists proxy information for the Asset Intelligence synchronization point, if one is
configured. It is unlikely that this view will be joined to other views.

v_CAL_INSTALLED_SOFTWARE_DATA
Lists information about the installed software applications on Configuration Manager
clients found through Asset Intelligence. This view contains the same information as the
v_GS_INSTALLED_SOFTWARE view, but it limits the columns displayed. The view can be
joined with other views by using the MachineID column, which is the same as the
ResourceID column in other views.

v_CAL_Processor_Count
Lists the number of processors found on Configuration Manager clients. This view uses
the same hardware inventory data as the v_GS_PROCESSOR view, but it displays only
the count for processors on each client. The view can be joined with other views by
using the MachineID column, which is the same as the ResourceID column in other
views.

v_LU_CAL_ProductList
Lists the products, by SoftwareCode, that are being tracked for CALs, as well as the
software hash, product category, license type, and when the product license was last
updated. The view can be joined to other views by using the SoftwareCode column.

v_LU_Category
Lists information about the Asset Intelligence software categories, by category ID and
category name, as well as the language ID, description, and whether the category was
created locally. The information contained in this view can be displayed and customized
from the Catalog node in the Configuration Manager console. The view can be joined to
other views by using the CategoryID column.

v_LU_Category_Editable

<!-- p.291 -->

Lists information about the Asset Intelligence software categories, software families, and
custom labels, including the category ID, category name, language ID, description, type,
whether the category was created locally, and so on. This view contains information that
is found in the v_LU_Category, v_LU_Family, and v_LU_Tags views. It is unlikely that this
view will be joined to other views.

v_LU_Family
Lists information about the Asset Intelligence software families, by family ID and family
name, as well as language ID, description, and whether the family was created locally.
The information contained in this view can be displayed and customized from the
Software Families node in the Configuration Manager console. The view can be joined
to other views by using the FamilyID column.

v_LU_HardwareReadiness
Lists information about the hardware requirements for specific software applications,
including product, minimum CPU, minimum RAM, minimum hard disk size, minimum
hard disk free space, and more. The information contained in this view can be displayed
and customized from the Hardware Requirements node in the Configuration Manager
console. It is unlikely that this view will be joined to other views.

v_LU_MSProd
Lists information about the Microsoft products contained in the Asset Intelligence
catalog, including part number, family name, product name, version, language, license
type, and so on. It is unlikely that this view will be joined to other views.

v_LU_SoftwareCode
Lists information about the software application codes contained in the Asset
Intelligence catalog, as well as the associated software ID and when the software was
last updated. The view can be joined to other Asset Intelligence and hardware inventory
views by using the SoftwareCode and SoftwareID columns.

v_LU_SoftwareHash
Lists information about the software applications contained in the Asset Intelligence
catalog, by software property hash, including application name, version, publisher,
software ID, and when the software was last updated. The view can be joined to other

<!-- p.292 -->

Asset Intelligence and Asset Intelligence hardware inventory views by using the
SoftwarePropertiesHash and SoftwareID columns.

v_LU_SoftwareList
Lists information about the software applications contained in the Asset Intelligence
catalog, by software ID and name, including the version, publisher, software category ID,
software family ID, custom labels, and so on. The view can be joined to other Asset
Intelligence and Asset Intelligence hardware inventory views by using the SoftwareID,
CategoryID, FamilyID, Tag1ID, Tag2ID, and Tag3ID columns.

v_LU_SoftwareList_Editable
Lists information about the software applications, by software ID and name, where the
software category, software family, or custom label can be configured with items from
the custom catalog. The view also provides the software code, software properties hash,
publisher, version, category name and ID, family name and ID, custom labels, and so on.
The information contained in this view can be displayed and customized from the All
Inventoried Software Titles node in the Configuration Manager console. The view can
be joined to other Asset Intelligence and Asset Intelligence hardware inventory views by
using the CategoryID, FamilyID, Tag1ID, Tag2ID, and Tag3ID columns.

v_LU_SoftwareList_Local
Lists information about the software applications contained in the Asset Intelligence
catalog, by software ID and name that have a custom software category, custom
software family, or custom label. The view also provides the version, publisher, category
ID, family ID, label ID (tag ID), last updated date, and so on. This view contains the same
source data as the v_LU_SoftwareIdentity_Local_Repl view. The view can be joined to
other Asset Intelligence and Asset Intelligence hardware inventory views by using the
SoftwareID, CategoryID, FamilyID, Tag1ID, Tag2ID, and Tag3ID columns.

v_LU_Tags
Lists information about the Asset Intelligence custom labels, by tag ID and tag name, as
well as the language ID and a description. The information contained in this view can be
displayed and customized from the Custom Labels node in the Configuration Manager
console. The view can be joined to other views by using the TagID column, which is the
same as the CategoryID column in the v_LU_Category_Editable view.

<!-- p.293 -->

v_LU_LicensedProduct
Lists information about the licensed products contained in the Asset Intelligence
catalog, by licensed product ID. This includes the family name, the product name, and
the version code. It is unlikely that this view will be joined to other views.

Asset intelligence hardware inventory views
The Asset Intelligence hardware inventory views contain information that is retrieved
from Configuration Manager client computers using hardware inventory. For more
information about the hardware inventory views, see Hardware Inventory Views in
Configuration Manager. The hardware inventory views that contain Asset Intelligence
information are described in this section.

v_GS_AUTOSTART_SOFTWARE
Lists information about the applications on Configuration Manager clients that start
automatically with the operating system found through Asset Intelligence. The view can
be joined with other views by using the ResourceID column.

v_GS_BROWSER_HELPER_OBJECT
Lists information about the browser objects found on Configuration Manager clients
through Asset Intelligence. While some browser helper objects are beneficial, most
software considered "malware" is in the form of browser helper objects. The view can be
joined with other views by using the ResourceID column.

v_GS_INSTALLED_EXECUTABLE
Lists information about the installed software application executables on Configuration
Manager clients found through Asset Intelligence. The view can be joined with other
views by using the ResourceID column.

v_GS_INSTALLED_SOFTWARE
Lists information about the installed software applications on Configuration Manager
clients found through Asset Intelligence. The view can be joined with other views by
using the ResourceID column and with Asset Intelligence views by using the
SoftwareCode0 and SoftwarePropertiesHash0 columns.

<!-- p.294 -->

v_GS_INSTALLED_SOFTWARE_CATEGORIZED
Lists information about the installed software applications on Configuration Manager
clients found through Asset Intelligence. This view contains the information in the
v_GS_INSTALLED_SOFTWARE view provides additional details about the installed
software. The view can be joined with other views by using the ResourceID column and
with Asset Intelligence views by using the SoftwareCode0, SoftwarePropertiesHash0,
FamilyID, CategoryID, and SoftwareID columns.

v_GS_INSTALLED_SOFTWARE_MS
Lists information about the installed Microsoft software applications on Configuration
Manager clients found through Asset Intelligence. The view can be joined with other
views by using the ResourceID column.

v_GS_SOFTWARE_LICENSING_PRODU
Lists software licensing product information for Windows Configuration Manager clients
found through Asset Intelligence. The view can be joined with other views by using the
ResourceID column.

v_GS_SOFTWARE_LICENSING_SERVICE
Lists software licensing service information for Windows Configuration Manager clients
found through Asset Intelligence. The view can be joined with other views by using the
ResourceID column.

v_GS_SOFTWARE_SHORTCUT
Lists software shortcut information for Configuration Manager clients found through
Asset Intelligence. The view can be joined with other views by using the ResourceID
column.

v_GS_SYSTEM_CONSOLE_USAGE
Lists all system console usage information for Configuration Manager clients found
through Asset Intelligence by polling the System Security Event Log. The view can be
joined with other views by using the ResourceID column.

v_GS_SYSTEM_CONSOLE_USAGE_MAXGROUP

<!-- p.295 -->

Lists all system console usage information for Configuration Manager clients found
through Asset Intelligence by polling the Windows System Security Event Log. This view
contains a subset of information from the v_GS_SYSTEM_CONSOLE_USAGE view. The
view can be joined with other views by using the ResourceID column.

v_GS_SYSTEM_CONSOLE_USER
Lists all system console user information for Configuration Manager clients found
through Asset Intelligence by polling the System Security Event Log. The view can be
joined with other views by using the ResourceID column.

v_GS_USB_DEVICE
Lists information about the USB devices found on Configuration Manager clients
through Asset Intelligence. The view can be joined with other views by using the
ResourceID column.

Asset intelligence status view
The Asset Intelligence status view contains summary information about the software
applications on Configuration Manager clients. For more information about status views,
see Status and alert views in Configuration Manager. The status view that contains Asset
Intelligence information is described in this section.

v_INSTALLED_SOFTWARE_DATA_Summary
Lists the count of the installed software applications on Configuration Manager clients
found through Asset Intelligence. This view contains the same source information as the
v_GS_INSTALLED_SOFTWARE view, but it provides summary information instead of
listing the individual system resources. It is unlikely that this view will be joined to other
views.

See also
SQL Server views in Configuration Manager

Feedback

<!-- p.296 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.297 -->

Migration views in Configuration
Manager
Article • 10/10/2022

Migration views contain information about the tasks involved in migrating to a
Configuration Manager site.

For more information about migration in Configuration Manager, see Migrating
hierarchies in Configuration Manager.

Migration views
The views for migration are shown in this section:

v_MIG_SiteMapping
Lists the current migration source site. SiteMappingID is used to uniquely identify a
migration source site.

  ７ Note

  If IsDecommissioned or IsDeleted has a value of true, it means this migration
  source site has either stopped migration data gathering or is deleted.

This view can be joined to other views by using the SourceSiteCode column.

v_MIG_SiteRelation
This view is no longer used in Configuration Manager.

v_MIG_MigratedDPs
Lists the shared distribution points from source sites. AttachingSiteCode is the source
site code that the distribution point belongs to in the source hierarchy, and SiteCode is
the site code of the destination site. This view can be joined to other views by using the
NALPath column.

v_MIG_JobEntity

<!-- p.298 -->

Lists the relationship between a migration job and objects for migration. This is useful
for listing the objects contained in a migration job. This view can be joined to other
views by using the JobID column.

v_MIG_Job
Lists the migration jobs that have been created. The JobID column uniquely identifies a
migration job and is usually used to join with other migration job related tables or views.

v_MIG_EntityState
Lists the state of migration objects. This view can be joined to other views by using the
EntityID column.

v_MIG_EntityReference
Lists the migration object dependency relationship. This can be used to find out the
dependent objects for an object. This view can be joined to other views by using the
EntityID column.

v_MIG_Entities
Lists the objects available for migration in the source site. This view can be joined to
other views by using the EntityID column.

v_MIG_Dashboard
Lists the overall migration status from a source site hierarchy. Migration status in the
Configuration Manager console information is based on this view.

v_MIG_Collections
Lists collection information in a source site. The SiteID column represents the source site
ID. This view can be joined to other views by using the SiteID column.

v_MIG_ClientState
This view is no longer used in Configuration Manager.

v_MIG_Clients

<!-- p.299 -->

This view is no longer used in Configuration Manager.

v_MIG_ClientGroupState
This view is no longer used in Configuration Manager.

vSMS_MigrationSourceSite
Lists the source site information. This view is similar to v_MIG_SiteMapping, but only
contains information about the source site.

vSMS_MigrationCollectionInfo
This view is based on v_MIG_Collections and queries the list of collection information in
a source site. Use this view to query collection information.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.300 -->

Mobile device management views in
Configuration Manager
Article • 10/10/2022

Mobile device management views in Configuration Manager contain information about
the mobile device configuration items and configuration packages. The mobile device
management status views provide client deployment and client health state information,
and the mobile device management hardware inventory views contain information
about the inventory collected from mobile device.

The following sections provide detailed information about mobile device management
views, mobile device management status views, and mobile device management
hardware inventory views.

Mobile device management status views
The mobile device management status views contain information about the mobile
device deployment and client health states. For more information about status views,
see Status and alert views in Configuration Manager. The status views that contain
mobile devices information are described in this section.

v_DeviceClientDeploymentState
Lists all Configuration Manager mobile device clients, by device client ID, NetBIOS name,
and device ID, and the last device deployment state reported, as well as the assigned
site code, device client version, and so on. The view is also listed and described in the
Client deployment views in Configuration Manager topic. The view can be joined to
other views by using the DeviceClientID, DeviceNetBiosName, and
DeviceDeploymentState columns. The DeviceDeploymentState column contains the
state ID for topic type 800. The DeviceClientID column contains the same information as
the SMS_Unique_Identifier0 column in the v_R_System view. The Configuration
Manager states are listed in the v_StateNames view.

v_DeviceClientHealthState
Lists all Configuration Manager mobile device clients, by device client ID, NetBIOS name,
and device ID, and the health state of the device, as well as the assigned site code,
owner name, and so on. The view is also listed and described in the Client status views
in Configuration Manager topic. The view can be joined to other views by using the

<!-- p.301 -->

DeviceClientID, DeviceNetBiosName, HealthType, and HealthState columns. The
DeviceClientID column in this view contains the same information as the
SMS_Unique_Identifier0 column in the v_R_System view. The HealthType column in this
view contains the same information as the TopicType column in the v_StateNames view
and the HealthState column in this view contains the same information as the StateID
column in the v_StateNames status view. Client health state messages have a state type
from 1000 to 1004. The Configuration Manager states are listed in the v_StateNames
view.

v_DeviceClientUpdateState
Lists information about client updates applied to the mobile device client. The view can
be joined to other views by using the DeviceClientID, DeviceNetBiosName, and
DeviceDeploymentState columns. The DeviceDeploymentState column contains the
state ID for topic type 800. The DeviceClientID column contains the same information as
the SMS_Unique_Identifier0 column in the v_R_System view. The Configuration
Manager states are listed in the v_StateNames view.

v_RBAC_WinRTSideLoadingKeys
Lists information about the configured sideloading keys for Windows RT including a
description, the maximum number of activations allowed, the type of key and more. It is
unlikely that this view will be joined to other views.

Mobile device management views
The mobile device management views contain information about the status of mobile
devices in your hierarchy and contain the information described in this section.

v_DM_RetireRecords
Lists information about devices that have been retired from management. The view can
be joined with other views by using the DeviceName column.

v_DM_WipeRecords
Lists information about devices that have been wiped by Configuration Manager. The
view can be joined with other views by using the DeviceName column.

<!-- p.302 -->

Mobile device management hardware
inventory views
The mobile device management hardware inventory views contain information about
mobile devices that is retrieved as part of hardware inventory. For more information
about hardware inventory views, see Hardware inventory views in Configuration
Manager. The hardware inventory views that contain mobile device information are
described in this section.

v_GS_DEVICE_CERTIFICATES
Lists information about the certificates on devices, including the revision ID, issuer,
where it is located in the certificate store, the subject, the dates the certificate is valid,
and so on. The view can be joined with other views by using the ResourceID column.

v_GS_DEVICE_COMPUTERSYSTEM
Lists information about the Configuration Manager devices, including the manufacturer,
model, phone number, processor, and more. The view can be joined with other views by
using the ResourceID column.

v_GS_DEVICE_DISPLAY
Lists information about the displays found on Configuration Manager devices including
the display resolution, number of colors and more. The view can be joined with other
views by using the ResourceID column.

v_GS_DEVICE_MEMORY
Lists information about the memory found on Configuration Manager devices. The view
can be joined with other views by using the ResourceID column.

v_GS_DEVICE_OS_INFORMATION
Lists information about the operating system found on Configuration Manager devices.
The view can be joined with other views by using the ResourceID column.

v_GS_DEVICE_POWER

<!-- p.303 -->

Lists information about power settings and the battery on Configuration Manager
devices. The view can be joined with other views by using the ResourceID column.

v_GS_DEVICE_CLIENT
Lists information about the device client on Configuration Manager managed devices.
This view can be joined with other views by using the ResourceID column.

v_GS_DEVICE_CLIENTAGENTVERSION
Lists information about the client version installed on Configuration Manager managed
client devices. This view can be joined with other views by using the ResourceID column.

v_GS_DEVICE_EMAIL
Lists information about the email settings on a device. This includes the email address,
domain, synchronization server and more. This view can be joined with other views by
using the ResourceID column.

v_GS_DEVICE_ENCRYPTION
Lists information about the encryption settings on devices including for email, phone
memory and external storage devices. This view can be joined with other views by using
the ResourceID column.

v_GS_DEVICE_BLUETOOTH
Lists information about whether Bluetooth is enabled on device clients. This view can be
joined with other views by using the ResourceID column.

v_GS_DEVICE_CAMERA
Lists information about the camera on mobile devices including whether it is enabled.
This view can be joined with other views by using the ResourceID column.

v_GS_DEVICE_EXCHANGE
Lists Microsoft Exchange settings for mobile devices, such as the maximum size of file
attachment, when email is sent, synchronization settings and more. This view can be
joined with other views by using the ResourceID column.

<!-- p.304 -->

v_GS_DEVICE_INFO
Lists general information about mobile devices including the manufacturer and model,
the operating system and more. This view can be joined with other views by using the
ResourceID column.

v_GS_DEVICE_INSTALLEDAPPLICATIONS
Lists the name and version of all applications installed on the device. This view can be
joined with other views by using the ResourceID column.

v_GS_DEVICE_IRDA
Lists information about the IRDA (infra-red) port on devices and whether it is enabled.
This view can be joined with other views by using the ResourceID column.

v_GS_DEVICE_MEMORY_ADDRESS
Lists the memory address ranges found on the device. This view can be joined with
other views by using the ResourceID column.

v_GS_DEVICE_PASSWORD
Lists information about the password settings on mobile devices, such as the maximum
incorrect passwords that can be entered before the device is wiped, when the password
expires, and more. This view can be joined with other views by using the ResourceID
column.

v_GS_DEVICE_POLICY
Lists information about policies assigned to devices. This view can be joined with other
views by using the ResourceID column.

v_GS_DEVICE_WINDOWSSECURITYPOLICY
Lists information about the Windows Security policy assigned to Windows Mobile
devices. This view can be joined with other views by using the ResourceID column.

v_GS_DEVICE_WLAN

<!-- p.305 -->

Lists information about network settings on mobile devices, including whether the
network is enabled. This view can be joined with other views by using the ResourceID
column.

Exchange ActiveSync views

v_EAS_Organization
Lists information about the Exchange Server and the organization that manage mobile
devices. It is unlikely that this view will be joined to other views.

v_EAS_Property
Lists information about all devices that are managed by Exchange ActiveSync. This
includes the device ID, name, domain, the operating system of the device and more. This
view can be joined to other views by using the DeviceID column.

v_DeviceJailBrokenStatus
Lists, by ItemKey, devices and whether they have been jailbroken. It is unlikely that this
view will be joined to other views.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.306 -->

Operating system deployment views in
Configuration Manager
Article • 10/10/2022

The Configuration Manager operating system deployment views contain information
about boot image packages, computer association state migrations, operating system
image packages, task sequences, driver packages, and so on. There is also a status view
that contains information about the status of task sequence steps.

The following sections provide detailed information about operating system
deployment views and operating system deployment status views.

Operating system deployment views
The operating system deployment views are described in this section.

v_BootImagePackage
Lists the boot image packages in the Configuration Manager site hierarchy, including
package ID, package name, the path of the package source files, source site, priority,
package flags, last refresh time, and more. The view can be joined to other views by
using the PackageID column.

v_BootImagePackage_References
Lists the boot image packages, by pkgID, the configuration item ID for the drivers that
have been added to the boot image package, as well as the path to the driver source
files. The view can be joined to the v_ConfigurationItems view by using the CI_ID
column and other views by using the PkgID column, which contains the same package
ID information as the PackageID column in other views.

v_DriverContentToPackage
Lists the driver packages, by package ID and package name, the configuration item IDs
for the drivers contained in the package, and the content IDs for the drivers. The view
can be joined to the v_ConfigurationItems view by using the CI_ID column, the
v_Contents view by using the Content_ID column, and other views by using the PkgID
column, which contains the same package ID Information as the PackageID column in
other views.

<!-- p.307 -->

v_DriverPackage
Lists the driver packages in the Configuration Manager site hierarchy, including package
ID, package name, the path of the package source files, source site, priority, package
flags, last refresh time, and more. The driver packages are created in the Driver Packages
node of the Configuration Manager console. The view can be joined to other views by
using the PackageID column.

v_ImagePackage
Lists the operating system image packages in the Configuration Manager site hierarchy,
including package ID, package name, the path of the package source files, source site,
priority, package flags, last refresh time, and more. The operating system image
packages are created in the Operating System Images node of the Configuration
Manager console. The view can be joined to other views by using the PackageID
column.

V_LastPXEDeployment
Lists information about the last PXE deployment including the Mac address of the
computer, the NetBIOS name and more. The view can be joined to other views by using
the MachineID column.

v_MachineSettings
Lists the Configuration Manager clients, by ResourceID, that have operating system
deployment computer settings, including the source site, locale, and the date the
settings were last modified. The view can be joined to other views by using the
ResourceID column.

v_StateMigration
Lists the computer associations, by MigrationID, that have been created in the User
State Migration node of the Configuration Manager console. Computer associations
organize the migration of user state and settings from a source computer to a
destination computer. The view provides information about the migration type, source
computer name, source client resource ID, last logged on user, restore computer name,
restore client resource ID, and so on. The view can be joined to other views by using the
SourceClientResourceID and RestoreClientResourceID columns.

<!-- p.308 -->

v_TaskSequencePackage
Lists the task sequences in the Configuration Manager site hierarchy, including the task
sequence package ID, package name, source site, priority, package flags, last refresh
time, boot image package ID, and more. The BootImageID column contains the
package ID for the boot image package defined in the task sequence. The task
sequences are created in the Task Sequences node of the Configuration Manager
console. The view can be joined to other views by using the PackageID and
BootImageID columns. The BootImageID column contains the same package ID
information as the ReferencePackageID column in the v_TaskSequenceReferencesInfo
view, and the same package ID information as the PackageID column in other views.

v_TaskSequencePackageReferences
Lists the packages in a task sequence that reference other packages. This view can be
joined to other views by using the PackageID and RefPackageID columns.

v_TaskSequenceReferenceDps
Lists the task sequences, by Task sequence ID, which is the task sequence package ID,
the boot image package ID, server NAL path (path to distribution point), site code, task
sequence source version, and task sequence hash. The view can be joined to other views
by using the TaskSequenceID and PackageID columns. The TaskSequenceID column in
this view contains the same package ID information as the PackageID column in other
views.

v_TaskSequenceReferencesInfo
Lists the task sequences, by Package ID, and the reference package ID for the associated
boot image, as well as the reference name, reference version, and so on. The view can
be joined to other views by using the PackageID and RefPackageID columns. The
RefPackageID column contains the same package ID information as the BootImageID
column in the v_TaskSequencePackage view, and the same package ID information as
the PackageID column in other views.

v_UserStateMigration
Lists the user accounts, by Domain\Username, that will be migrated as specified for the
computer associations created in the User State Migration node of the Configuration
Manager console. The locale ID, source client resource ID, and restore client resource ID

<!-- p.309 -->

are also listed. The view can be joined to other views by using the
SourceClientResourceID and RestoreClientResourceID columns, which contain the
same information as the ResourceID column in other views.

v_TaskSequenceAppReferenceDps
Lists, by task sequence ID, information about the content packages that are associated
with task sequences. This view can be joined to other views by using the PackageID and
TaskSequenceID columns.

v_TaskSequenceAppReferencesInfo
Lists, by package ID, the content packages that are referenced by a task sequence that
installs an application. This view can be joined to other views by using the PackageID
column.

Operating system deployment status view
The operating system deployment status view contains status information for operating
system deployment task sequence steps. For more information about the status views,
see Status and alert views in Configuration Manager. The status view that contains
operating system deployment information is described in this section.

v_TaskExecutionStatus
Lists the status for operating system deployment task sequence steps, as well as the
advertisement ID, resource ID, action name, and so on. The view can be joined to other
views by using the AdvertisementID or ResourceID columns.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.310 -->

Power management views in
Configuration Manager
Article • 10/10/2022

Information about the power plans applied to computers by Configuration Manager and
the power capabilities of computers is retrieved by Configuration Manager hardware
inventory.

For more information about power management, see Power management in
Configuration Manager.

Wake-up proxy is used to supplement the traditional wake-up packet method by using
the wake-up proxy client settings. Wake-up proxy uses a peer-to-peer protocol and
elected computers to check whether other computers on the subnet are awake, and to
wake them if necessary.

For more information about wake-up proxy, see the Power Management section of the
About client settings in Configuration Manager topic in the Configuration Manager
Documentation Library.

Power management views
The power management views are described in this section.

v_GS_POWER_MANAGEMENT_CAPABILITIES
Lists information about the power management capabilities collected from each client
computer, sorted by resource ID, including information about the last time this
information was collected, information about the battery, if present, and information
about the wake up capabilities of the computer. The view can be joined to other views
by using the ResourceID column.

v_GS_POWER_MANAGEMENT_CLIENTOPTOUT_SETTINGS
Lists information for each client computer about whether the administrator allows the
computer to opt out from power management settings and whether the client computer
has been opted out from the settings. This view is sorted by resource ID.

v_GS_POWER_MANAGEMENT_CONFIGURATION

<!-- p.311 -->

Lists information about power plan names and the duration of each power plan that
have been applied to client computers. The view can be joined to other views by using
the ResourceID column.

v_GS_POWER_MANAGEMENT_DAY
Lists information about power activity on computers for each hour of the day. The view
can be joined to other views by using the ResourceID column.

v_GS_POWER_MANAGEMENT_MONTH
List information about power activity on computers for the previous month, such as
when the computer was active, when it was turned on, and when it was inn sleep mode.
The view can be joined to other views by using the ResourceID column.

v_GS_POWER_MANAGEMENT_SETTINGS
Lists information about the power management settings applied to each computer,
sorted by resource ID. These settings include the power plan applied to the computer,
the delay before the screen and hard disks are turned off, and the action that will be
taken when the computer power button is pressed. The view can be joined to other
views by using the ResourceID column.

v_GS_POWER_MANAGEMENT_SUSPEND_ERROR
Lists information, by Resource ID, about power management suspend operations that
didn't complete successfully. The view can be joined to other views by using the
ResourceID column.

Wake up proxy views
The wake up proxy views are described in this section.

v_WakeupProxyDeploymentState
Lists information about the computers in each collection and whether that computer is
enabled for wake-up proxy. This view is sorted by collection ID. This view can be joined
to other views by using the CollectionID column.

<!-- p.312 -->

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.313 -->

Query views in Configuration Manager
Article • 10/10/2022

Configuration Manager has only one query view, v_Query. It contains information about
all the queries in the Configuration Manager hierarchy. The query ID, query name,
comment, target class name, and the collection ID to which the query is limited, if
applicable, are all listed.

The v_Query view can be joined to the v_CollectionRuleQuery collection view by using
the QueryID column and to collection views by using the LimitToCollectionID column,
which contains the same information as the CollectionID column in other views. It's also
possible to join the query view to a security view so that the query name can be
displayed when listing the class or instance permissions on the specific query object. An
example is available in the section Sample queries for queries in Configuration Manager.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.314 -->

Reporting views in Configuration
Manager
Article • 10/10/2022

Reporting in Configuration Manager uses the SQL Server Reporting Services (SSRS) to
store and generate reports. For this reason, information about built-in and user-created
reports is stored in the SQL Server Reporting Services database and not the
Configuration Manager database.

You can run the following query against your Reporting Services database to retrieve a
list of the built-in and user-created reports at your site.

  SQL

        SELECT *
        FROM <report server name>.dbo.Catalog
        ORDER BY Name

For more information about the built-in reports supplied with Configuration Manager,
see List of reports in Configuration Manager.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.315 -->

Schema views in Configuration Manager
Article • 10/10/2022

The Configuration�Manager schema views provide information about the schema that
can be used when creating reports, as well as the discovery schema views, inventory
schema views, and the compliance settings schema view.

View schema views
The Configuration Manager view schema views can be joined together and used to
retrieve specific data. They provide information about all of the views in a Configuration
Manager site that are in the Configuration Manager view schema family. The view
schema views are described in this section.

v_SchemaViews
Lists all the SQL views and SQL view types in the view schema family. The view can be
joined to the v_ReportViewSchema view by using the ViewName column.

v_ReportViewSchema
Lists all the Configuration Manager SQL views in the view schema family and the column
names for each view. The view can be joined to the v_ReportViewSchema view by using
the ViewName column.

The following query uses the v_SchemaViews view to retrieve a list of all the view
schema family views and their associated view category:

  SQL

  SELECT Type, ViewName

  FROM v_SchemaViews

  ORDER BY Type, ViewName

Each of the Configuration Manager views has multiple columns, and determining which
of these columns to use when building queries for the required data can be difficult. The
following query joins the v_SchemaViews and v_ReportViewSchema views to list all of
the views in the Configuration Manager view schema family, each of the columns within
each view, and the view category:

<!-- p.316 -->

     SQL

     SELECT RVS.ViewName, RVS.ViewColumnName, SV.Type

     FROM v_SchemaViews as SV INNER JOIN v_ReportViewSchema as RVS

     ��ON SV.ViewName = RVS.ViewName

     ORDER BY SV.Type, RVS.ViewName, RVS.ViewColumnName

The output from this query and the information provided throughout this document
provide information to help you use the correct view and view column to build queries
for effective reporting.

Discovery schema views
The discovery schema views provide information about all resources in a Configuration
Manager site and are described in this section. The two resource schema information
views are v_ResourceMap and v_ResourceAttributeMap. The v_ResourceMap view
contains a list of all the resource types for discovered data. By default, Configuration
Manager has the Unknown System, User Group, User, and System Resource types, each
of which has its own resource type number and individual view. The view can be joined
to other views by using the ResourceType column. his section represents the default
data contained in the v_ResourceMap view.

                                                                           ﾉ   Expand table

 Resource type             Display name                  Resource class name

 2                         Unknown System                v_R_UnknownSystem

 3                         User Group                    v_R_UserGroup

 4                         User                          v_R_User

 5                         System                        v_R_System

 6                         IP Network                    V_R_IPNetwork

The v_ResourceAttributeMap view contains all of the attributes that will be discovered
for each of the resource types, such as NetBIOS name, operating system, user name,
user group name, domain name, and so forth. The v_ResourceAttributeMap view can be
joined to other views by using the ResourceType column. For more information about
the discovery views, see Discovery Views in Configuration Manager.

<!-- p.317 -->

Hardware inventory schema views
The hardware inventory schema is important to understand when creating queries for
Configuration Manager reports that contain hardware inventory information. Most of
the client data within Configuration Manager is contained in one of the two hardware
inventory schema views: v_GroupMap and v_GroupAttributeMap. The v_GroupMap
view contains a list of all the hardware inventory groups and the associated view for
each of the groups. The v_GroupAttributeMap view contains all of the attributes that
are inventoried for each of the groups. Both views can be joined together by using the
GroupID column and joined to the v_ResourceMap discovery schema view by using the
ResourceType column.

Because hardware inventory can be modified and extended, one Configuration Manager
site's SQL Server database might have different hardware inventory views and schema
when compared to another site. The following query joins the v_GroupMap and
v_GroupAttributeMap views to generate the hardware inventory view schema, based on
the specific settings for the site:

  SQL

  SELECT DISTINCT GM.DisplayName, GM.InvClassName,

  ��GM.InvHistoryClassName, GAM.AttributeName,

  ��GAM.ColumnName, GM.MIFClass

  FROM v_GroupMap GM INNER JOIN v_GroupAttributeMap GAM

  ��ON GM.GroupID = GAM.GroupID

For more information about the hardware inventory views, see Hardware Inventory
Views in Configuration Manager.

Software inventory view schema
There is not a specific software inventory schema view, but the following query joins the
v_GS_SoftwareProduct and v_FullCollectionMembership software inventory views to
generate the software inventory view schema by product name for the All Systems
collection:

  SQL

  SELECT MIN(PRD.ProductID) AS ProductID, PRD.ProductName,

<!-- p.318 -->

  PRD.ProductVersion, COUNT(DISTINCT PRD.ResourceID) AS 'Count'

  FROM v_GS_SoftwareProduct PRD INNER JOIN v_FullCollectionMembership FCM

  ON PRD.ResourceID = FCM.ResourceID

  WHERE FCM.CollectionID = 'SMS00001'

  GROUP BY PRD.ProductName, PRD.ProductVersion

  ORDER BY PRD.ProductName

For more information about the software inventory views, see Software Inventory Views
in Configuration Manager.

Compliance settings schema view
There is one compliance settings schema view, v_CIRelationTypeMapping, that lists the
configuration item elements, such as configuration baselines and software updates, the
relation type value, and a description for the relation type. The view can be joined to
other compliance settings views by using the RelationType column. For more
information about the desired configuration management views, see Compliance
Settings Views in Configuration Manager.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.319 -->

Security views in Configuration
Manager
Article • 10/10/2022

The security views in Configuration Manager contain information about the permissions
that are granted to users and user groups to perform operations on secured
Configuration Manager object classes and instances, such as collections, applications,
deployments, and more.

Security views
Security views can be used to query for Configuration Manager class or instance
permissions for secured objects. In each SQL view, class and instance permission values
are listed as a decimal value that is the result of converting bit fields reserved for each
security right. More information can be found in the next section. The security views are
described in This section.

v_SecuredObject
Describes the different types of objects in the Configuration Manager system that can
be secured, such as collections, applications, deployments, Wi-Fi and VPN profiles, client
settings and many more. The view lists the Configuration Manager objects by object ID
and name. The view can be joined to the other security views by using the ObjectTypeID
or ObjectTypeName columns.

v_AllItems
Lists all securable objects in the Configuration Manager site by name. It is unlikely that
this view will be joined to other views.

V_CategoryPermissions
Lists, for each object type, the permissions for each Configuration Manager collection.
The view can be joined to the other security views by using the AdminID column.

Configuration Manager secured objects

<!-- p.320 -->

Class and instance permissions can be set on more than 20 secured objects in
Configuration Manager. These Configuration Manager secured objects and their
associated object keys are listed in the following table.

                                                                      ﾉ   Expand table

 Object key            Object Name

 1                     Collection

 2                     Package

 4                     Status message

 6                     Site

 7                     Query

 9                     Software metering rule

 11                    Configuration items

 14                    OS install package

 15                    Deployment template

 16                    Deployment

 17                    Computer association

 18                    OS image

 19                    Boot image package

 20                    Task sequence package

 21                    Device setting package

 22                    Device setting item

 23                    Driver package

 24                    Deployment package

 25                    Device driver

 26                    Asset intelligence software list

 27                    Security roles

 28                    Site administrator settings
