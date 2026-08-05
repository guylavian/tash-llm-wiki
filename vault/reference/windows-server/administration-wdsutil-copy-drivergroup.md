---
title: "copy-drivergroup"
type: reference
domain: windows-server
slug: administration-wdsutil-copy-drivergroup
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-copy-drivergroup
family: administration
documentKind: "reference"
abstract: "Reference article for the copy-drivergroup command, which duplicates an existing driver group on the server including the filters, driver packages, and enabled/disabled status."
---

# copy-drivergroup

# copy-drivergroup

Duplicates an existing driver group on the server including the filters, driver packages, and enabled/disabled status.

## Syntax

```
wdsutil /Copy-DriverGroup [/Server:<Server name>] /DriverGroup:<Source Groupname> /GroupName:<New Groupname>
```

### Parameters

| Parameter | Description |
|--|--|
| /Server:`<Servername>` | Specifies the name of the server. This can be the NetBIOS name or the FQDN. If no server name is specified, the local server is used. |
| /DriverGroup:`<Source Groupname>` | Specifies the name of the source driver group. |
| /GroupName:`<New Groupname>` | Specifies the name of the new driver group. |

## Examples

To copy a driver group, type either:

```
wdsutil /Copy-DriverGroup /Server:MyWdsServer /DriverGroup:PrinterDrivers /GroupName:X86PrinterDrivers
```

```
wdsutil /Copy-DriverGroup /DriverGroup:PrinterDrivers /GroupName:ColorPrinterDrivers
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [Windows Deployment Services cmdlets](/powershell/module/wds)
