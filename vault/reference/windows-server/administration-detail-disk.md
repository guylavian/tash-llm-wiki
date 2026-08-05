---
title: "detail disk"
type: reference
domain: windows-server
slug: administration-detail-disk
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/detail-disk
family: administration
documentKind: "reference"
abstract: "Reference article for the detail disk command, which displays the properties of the selected disk and the volumes on that disk."
---

# detail disk

# detail disk

Displays the properties of the selected disk and the volumes on that disk. Before you begin, you must select a disk for this operation to succeed. Use the [select disk](select-disk.md) command to select a disk and shift the focus to it. If you select a virtual hard disk (VHD), this command will show the disk's bus type as *Virtual*.

## Syntax

```
detail disk
```

## Examples

To see the properties of the selected disk, and information about the volumes in the disk, type:

```
detail disk
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [detail command](detail.md)
