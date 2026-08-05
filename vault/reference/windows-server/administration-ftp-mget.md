---
title: "ftp mget"
type: reference
domain: windows-server
slug: administration-ftp-mget
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ftp-mget
family: administration
documentKind: "reference"
abstract: "Reference article for the ftp mget command, which copies remote files to the local computer using the current file transfer type."
---

# ftp mget

# ftp mget



Copies remote files to the local computer using the current file transfer type.

## Syntax

```
mget <remotefile>[ ]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<remotefile>` | Specifies the remote files to copy to the local computer. |

### Examples

To copy remote files *a.exe* and *b.exe* to the local computer using the current file transfer type, type:

```
mget a.exe b.exe
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [ftp ascii command](ftp-ascii.md)

- [ftp binary command](ftp-binary.md)

- [Additional FTP guidance](/previous-versions/orphan-topics/ws.10/cc756013(v=ws.10))
