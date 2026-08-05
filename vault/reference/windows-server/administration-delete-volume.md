---
title: "delete volume"
type: reference
domain: windows-server
slug: administration-delete-volume
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/delete-volume
family: administration
documentKind: "reference"
abstract: "Reference article for the delete volume command, which deletes the selected volume."
---

# delete volume

# delete volume

Deletes the selected volume. Before you begin, you must select a volume for this operation to succeed. Use the [select volume](select-volume.md) command to select a volume and shift the focus to it.

> [!IMPORTANT]
> You can't delete the system volume, boot volume, or any volume that contains the active paging file or crash dump (memory dump).

## Syntax

```
delete volume [noerr]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| noerr | For scripting only. When an error is encountered, DiskPart continues to process commands as if the error did not occur. Without this parameter, an error causes DiskPart to exit with an error code. |

## Examples

To delete the volume with focus, type:

```
delete volume
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [select volume](select-volume.md)

- [delete command](delete.md)
