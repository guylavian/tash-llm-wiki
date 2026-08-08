---
title: "bitsadmin util and repairservice"
type: reference
domain: windows-server
slug: administration-bitsadmin-util-and-repairservice
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-util-and-repairservice
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin util and repairservice command, which fixes known issues in various versions of BITS service."
---

# bitsadmin util and repairservice

# bitsadmin util and repairservice

If BITS fails to start, this switch attempts to resolve errors related to incorrect service configuration and dependencies on Windows services (such as LANManworkstation) and the network directory. This switch also generates output that indicates if the issues that were resolved.

> [!NOTE]
> This command isn't supported by BITS 1.5 and earlier.

## Syntax

```
bitsadmin /util /repairservice [/force]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| /force | Optional. Deletes and creates the service again.|

> [!NOTE]
> If BITS creates the service again, the service description string might be set to English even in a localized system.

## Examples

To repair the BITS service configuration:

```
bitsadmin /util /repairservice
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin util command](bitsadmin-util.md)

- [bitsadmin command](bitsadmin.md)
