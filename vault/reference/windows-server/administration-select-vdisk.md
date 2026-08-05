---
title: "select vdisk"
type: reference
domain: windows-server
slug: administration-select-vdisk
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/select-vdisk
family: administration
documentKind: "reference"
abstract: "Reference article for the select vdisk command, which selects the specified virtual hard disk (VHD) and shifts the focus to it."
---

# select vdisk

# select vdisk



Selects the specified virtual hard disk \(VHD\) and shifts the focus to it.

## Syntax

```
select vdisk file=<full path> [noerr]
```

### Parameters

| Parameter | Description |
|--|--|
| file=`<full path>` | Specifies the full path and file name of an existing VHD file. |
| noerr | Used for scripting only. When an error is encountered, DiskPart continues to process commands as if the error did not occur. Without this parameter, an error causes DiskPart to exit with an error code. |

## Examples

To shift the focus to the VHD named *c:\test\test.vhd*, type:

```
select vdisk file=c:\test\test.vhd
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [attach vdisk](attach-vdisk.md)

- [compact vdisk](compact-vdisk.md)

- [detach vdisk](detach-vdisk.md)

- [detail vdisk](detail-vdisk.md)

- [expand vdisk](expand-vdisk.md)

- [merge vdisk](merge-vdisk.md)

- [list](list.md)

- [select disk command](select-disk.md)

- [select partition command](select-partition.md)

- [select volume command](select-volume.md)
