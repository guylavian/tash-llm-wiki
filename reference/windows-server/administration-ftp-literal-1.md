---
title: "ftp literal"
type: reference
domain: windows-server
slug: administration-ftp-literal-1
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ftp-literal_1
family: administration
documentKind: "reference"
abstract: "Reference article for the ftp literal command, which sends verbatim arguments to the remote ftp server."
---

# ftp literal

# ftp literal



Sends verbatim arguments to the remote ftp server. A single ftp reply code is returned.

> [!NOTE]
> This command is the same as the [ftp quote command](ftp-quote.md).

## Syntax

```
literal <argument> [ ]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<argument>` | Specifies the argument to send to the ftp server. |

### Examples

To send a **quit** command to the remote ftp server, type:

```
literal quit
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [ftp quote command](ftp-quote.md)

- [Additional FTP guidance](/previous-versions/orphan-topics/ws.10/cc756013(v=ws.10))
