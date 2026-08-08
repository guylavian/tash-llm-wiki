---
title: "bdehdcfg driveinfo"
type: reference
domain: windows-server
slug: administration-bdehdcfg-driveinfo
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bdehdcfg-driveinfo
family: administration
documentKind: "reference"
abstract: "Reference article for the bdehdcfg driveinfo command, which displays the drive letter, the total size, the maximum free space, and the partition characteristics."
---

# bdehdcfg driveinfo

# bdehdcfg: driveinfo



Displays the drive letter, the total size, the maximum free space, and the partition characteristics. Only valid partitions are listed. Unallocated space is not listed if four primary or extended partitions already exist.

>[!NOTE]
> This command is informational only and makes no changes to the drive.

## Syntax

```
bdehdcfg -driveinfo <drive_letter>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| <drive_letter> | Specifies a drive letter followed by a colon. |

## Example

To display the drive information for the C: drive:

```
bdehdcfg -driveinfo C:
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bdehdcfg](bdehdcfg.md)
