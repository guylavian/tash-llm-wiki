---
title: "SMS_SearchFolder Class"
type: reference
domain: sccm
slug: develop-sms-searchfolder-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/console/sms_searchfolder-server-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn how to use SMS_SearchFolder WMI class in Configuration Manager to perform search operations."
---

# SMS_SearchFolder Class

# SMS_SearchFolder Server WMI Class
The `SMS_SearchFolder` WMI class is an SMS Provider server class, in Configuration Manager, that behaves the same as `SMS_ObjectContainerNode`, but is only used for search operations.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_SearchFolder : SMS_BaseClass
{
   UInt32 FolderId;
   String GroupID;
   Boolean IsSystem;
   String Name;
   UInt32 ObjectType;
   String SearchString;
   String SourceSite;
};
```

## Methods
 The `SMS_SearchFolder` class does not define any methods.

## Properties
 `FolderId`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: [key]

 The unique ID of this search folder.

 `GroupID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: None

 The Group ID of the search folder.

 `IsSystem`
 Data type: `Boolean`

 Access type: Read-only

 Qualifiers: [read, not_null]

 A flag that indicates whether this is a system folder.

 `Name`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [not_null]

 Folder name. Default value is New Folder.

 `ObjectType`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: None

 The type of the folder.

 `SearchString`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: None

 Search string get/set by AdminConsole.

 `SourceSite`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [read, not_null]

 The sidecode of the site that the folder originated from.

## Remarks
 In Configuration Manager, the search folder and folders were one class.  Now, in Configuration Manager, they are separate classes.  `SMS_SearchFolders` folders appear in the "Manage Searches" class of menus in the console.  The `SMS_SearchFolders` folders have no dedicated node and are used for node searches only.  `SMS_SearchFolders` folders cannot be used for global searches.

 There are no special class qualifiers for this class. For more information about both the class qualifiers and the property qualifiers that are included in the Properties section, see [Configuration Manager Class and Property Qualifiers](../../../../../develop/reference/misc/class-and-property-qualifiers.md).

## Requirements

### Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See also

[SMS_ObjectContainerItem Server WMI Class](../../../../../develop/reference/core/servers/console/sms_objectcontaineritem-server-wmi-class.md)
