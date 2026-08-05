---
title: "expand vdisk"
type: reference
domain: windows-server
slug: administration-expand-vdisk
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/expand-vdisk
family: administration
documentKind: "reference"
abstract: "Reference article for the expand vdisk command, which expands a virtual hard disk (VHD) to a specified size."
---

# expand vdisk

# expand vdisk



Expands a virtual hard disk (VHD) to a specified size.

A VHD must be selected and detached for this operation to succeed. Use the [select vdisk command](select-vdisk.md) to select a volume and shift the focus to it.

## Syntax

```
expand vdisk maximum=<n>
```

### Parameters

 | Parameter | Description |
 |---------- | ----------- |
 | maximum=`<n>` | Specifies the new size for the VHD in megabytes (MB). |

### Examples

To expand the selected VHD to 20 GB, type:

```
expand vdisk maximum=20000
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [select vdisk command](select-vdisk.md)

- [attach vdisk command](attach-vdisk.md)

- [compact vdisk command](compact-vdisk.md)

- [detach vdisk command](detach-vdisk.md)

- [detail vdisk command](detail-vdisk.md)

- [merge vdisk command](merge-vdisk.md)

- [list command](list.md)
