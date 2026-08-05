---
title: "ftp mdelete"
type: reference
domain: windows-server
slug: administration-ftp-mdelete-1
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ftp.mdelete_1
family: administration
documentKind: "reference"
abstract: "Reference article for the ftp mdelete command, which deletes files on the remote computer."
---

# ftp mdelete

# ftp mdelete



Deletes files on the remote computer.

## Syntax
```
mdelete <remotefile>[...]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<remotefile>` | Specifies the remote file to delete. |

### Examples

To delete remote files *a.exe* and *b.exe*, type:

```
mdelete a.exe b.exe
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [Additional FTP guidance](/previous-versions/orphan-topics/ws.10/cc756013(v=ws.10))
