---
title: "ftp recv"
type: reference
domain: windows-server
slug: administration-ftp-recv
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ftp-recv
family: administration
documentKind: "reference"
abstract: "Reference article for the ftp recv command, which copies a remote file to the local computer using the current file transfer type."
---

# ftp recv

# ftp recv



Copies a remote file to the local computer using the current file transfer type.

> [!NOTE]
> This command is the same as the [ftp get command](ftp-get.md).

## Syntax

```
recv <remotefile> [<localfile>]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<remotefile>` | Specifies the remote file to copy. |
| `[<localfile>]` | Specifies the name of the file to use on the local computer. If *localfile* isn't specified, the file is given the name of the *remotefile*. |

### Examples

To copy *test.txt* to the local computer using the current file transfer, type:

```
recv test.txt
```

To copy *test.txt* to the local computer as *test1.txt* using the current file transfer, type:

```
recv test.txt test1.txt
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [ftp get command](ftp-get.md)

- [ftp ascii command](ftp-ascii.md)

- [ftp binary command](ftp-binary.md)

- [Additional FTP guidance](/previous-versions/orphan-topics/ws.10/cc756013(v=ws.10))
