---
title: "remove-DriverGroupFilter"
type: reference
domain: windows-server
slug: administration-wdsutil-remove-drivergroupfilter
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-remove-drivergroupfilter
family: administration
documentKind: "reference"
abstract: "Reference article for remove-DriverGroupFilter, which removes a filter rule from a driver group on a server."
---

# remove-DriverGroupFilter

# remove-DriverGroupFilter



Removes a filter rule from a driver group on a server.

## Syntax

```
wdsutil /Remove-DriverGroupFilter /DriverGroup:<Group Name> [/Server:<Server name>] /FilterType:<Filter Type>
```

### Parameters

|Parameter|Description|
|---------|-----------|
|/DriverGroup:\<Group Name>|Specifies the name of the driver group.|
|[/Server:\<Server name>]|Specifies the name of the server. This can be the NetBIOS name or the FQDN. If a server name is not specified, the local server is used.|
|[/FilterType:\<FilterType>]|Specifies the type of the filter to remove from the group. \<FilterType> can be one of the following:</br>**BiosVendor**</br>**BiosVersion**</br>**ChassisType**</br>**Manufacturer**</br>**Uuid**</br>**OsVersion**</br>**OsEdition**</br>**OsLanguage**|

## Examples

To remove a filter, type one of the following:
```
wdsutil /Remove-DriverGroupFilter /DriverGroup:PrinterDrivers /FilterType:Manufacturer
```
```
wdsutil /Remove-DriverGroupFilter /DriverGroup:PrinterDrivers /FilterType:Manufacturer /FilterType:OSLanguage
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
