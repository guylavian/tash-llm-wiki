---
title: "showmount"
type: reference
domain: windows-server
slug: administration-showmount
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/showmount
family: administration
documentKind: "reference"
abstract: "Reference article for the showmount command, which displays information about mounted file systems exported by Server for NFS on a specified computer."
---

# showmount

# showmount



You can use **showmount** to display information about mounted file systems exported by Server for NFS on a specified computer. If you don't specify a server, this command displays information about the computer on which the **showmount** command is run.

## Syntax

```
showmount {-e|-a|-d} <server>
```

### Parameters

| Parameter | Description |
|--|--|
| -e | Displays all the file systems exported on the server. |
| -a | Displays all Network File System (NFS) clients and the directories on the server each has mounted. |
| -d | Displays all directories on the server that are currently mounted by NFS clients. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [Services for Network File System Command Reference](services-for-network-file-system-command-reference.md)
