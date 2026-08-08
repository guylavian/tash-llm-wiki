---
title: "bitsadmin getaclflags"
type: reference
domain: windows-server
slug: administration-bitsadmin-getaclflags
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getaclflags
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getaclflags command, which retrieves the access control list (ACL) propagations flags."
---

# bitsadmin getaclflags

# bitsadmin getaclflags

Retrieves the access control list (ACL) propagations flags, reflecting whether items are inherited by child objects.

## Syntax

```
bitsadmin /getaclflags <job>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |

### Remarks

Returns one or more of the following flag values:

- **o** - Copy owner information with file.

- **g** - Copy group information with file.

- **d** - Copy discretionary access control list (DACL) information with file.

- **s** - Copy system access control list (SACL) information with file.

## Examples

To retrieve the access control list propagation flags for the job named *myDownloadJob*:

```
bitsadmin /getaclflags myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
