---
title: "detail volume"
type: reference
domain: windows-server
slug: administration-detail-volume
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/detail-volume
family: administration
documentKind: "reference"
abstract: "Reference article for detail volume, which displays the disks on which the current volume resides."
---

# detail volume

# detail volume

Displays the disks on which the current volume resides. Before you begin, you must select a volume for this operation to succeed. Use the [select volume](select-volume.md) command to select a volume and shift the focus to it. The volume details aren't applicable to read-only volumes, such as a DVD-ROM or CD-ROM drive.

## Syntax

```
detail volume
```

## Examples

To see all the disks in which the current volume resides, type:

```
detail volume
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [select volume](select-volume.md)

- [detail command](detail.md)
