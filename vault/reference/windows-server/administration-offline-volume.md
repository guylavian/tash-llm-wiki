---
title: "offline volume"
type: reference
domain: windows-server
slug: administration-offline-volume
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/offline-volume
family: administration
documentKind: "reference"
abstract: "Reference article for the offline volume command, which takes the online volume with focus to the offline state."
---

# offline volume

# offline volume

Takes the online volume with focus to the offline state.

> [!NOTE]
> A volume must be selected for the **offline volume** command to succeed. Use the [select volume](select-volume.md) command to select a disk and shift the focus to it.

## Syntax

```
offline volume [noerr]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| noerr | For scripting only. When an error is encountered, DiskPart continues to process commands as if the error did not occur. Without this parameter, an error causes DiskPart to exit with an error code. |

### Examples

To take the disk with focus offline, type:

```
offline volume
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
