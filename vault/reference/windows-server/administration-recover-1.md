---
title: "recover (DiskPart)"
type: reference
domain: windows-server
slug: administration-recover-1
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/recover_1
family: administration
documentKind: "reference"
abstract: "Reference article for the DiskPart recover command, which refreshes the state of all disks in a disk group, attempt to recover disks in an invalid disk group, and resynchronizes mirrored volumes and RAID-5 volumes that have stale data."
---

# recover (DiskPart)

# recover (DiskPart)

Refreshes the state of all disks in a disk group, attempt to recover disks in an invalid disk group, and resynchronizes mirrored volumes and RAID-5 volumes that have stale data. This command operates on disks that are failed or failing. It also operates on volumes that are failed, failing, or in failed redundancy state.

This command operates on groups of dynamic disks. If this command is used on a group with a basic disk, it won't return an error, but no action will be taken.

> [!NOTE]
> A disk that is part of a disk group must be selected for this operation to succeed. Use the [select disk command](select-disk.md) to select a disk and shift the focus to it.

## Syntax

```
recover [noerr]
```

### Parameters

| Parameter | Description |
|--|--|
| noerr | For scripting only. When an error is encountered, DiskPart continues to process commands as if the error did not occur. Without this parameter, an error causes DiskPart to exit with an error code. |

## Examples

To recover the disk group that contains the disk with focus, type:

```
recover
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
