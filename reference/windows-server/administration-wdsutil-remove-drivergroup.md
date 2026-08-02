---
title: "remove-DriverGroup"
type: reference
domain: windows-server
slug: administration-wdsutil-remove-drivergroup
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-remove-drivergroup
family: administration
documentKind: "reference"
abstract: "Reference article for remove-DriverGroup, which removes a driver group from a server."
---

# remove-DriverGroup

# remove-DriverGroup

Removes a driver group from a server.

## Syntax

```
wdsutil /Remove-DriverGroup /DriverGroup:<Group Name> [/Server:<Server name>]
```

### Parameters

|Parameter|Description|
|---------|-----------|
|/DriverGroup:\<Group Name>|Specifies the name of the driver group to remove.|
|[/Server:\<Server name>]|Specifies the name of the server. This can be the NetBIOS name or the FQDN. If a server name is not specified, the local server is used.|

## Examples

To remove a driver group, type one of the following:
```
wdsutil /Remove-DriverGroup /DriverGroup:PrinterDrivers
```
```
wdsutil /Remove-DriverGroup /DriverGroup:PrinterDrivers /Server:MyWdsServer
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
