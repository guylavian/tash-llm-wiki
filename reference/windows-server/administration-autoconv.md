---
title: "autoconv"
type: reference
domain: windows-server
slug: administration-autoconv
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/autoconv
family: administration
documentKind: "reference"
abstract: "Reference article for the autoconv command, which converts file allocation table (Fat) and Fat32 volumes to the NTFS file system."
---

# autoconv

# autoconv



Converts file allocation table (Fat) and Fat32 volumes to the NTFS file system, leaving existing files and directories intact at startup after **autochk** runs. volumes converted to the NTFS file system cannot be converted back to Fat or Fat32.

> [!IMPORTANT]
> You can't run **autoconv** from the command-line. This can only run at startup, if set through **convert.exe**.

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [autochk command](autochk.md)

- [convert command](convert.md)
