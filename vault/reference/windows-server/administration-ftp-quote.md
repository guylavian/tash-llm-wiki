---
title: "ftp quote"
type: reference
domain: windows-server
slug: administration-ftp-quote
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ftp-quote
family: administration
documentKind: "reference"
abstract: "Reference article for the ftp quote command, which sends verbatim arguments to the remote ftp server."
---

# ftp quote

# ftp quote



Sends verbatim arguments to the remote ftp server. A single ftp reply code is returned.

> [!NOTE]
> This command is the same as the [ftp literal command](ftp-literal_1.md).

## Syntax

```
quote <argument>[ ]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<argument>` | Specifies the argument to send to the ftp server. |

### Examples

To send a **quit** command to the remote ftp server, type:

```
quote quit
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [ftp literal command](ftp-literal_1.md)

- [Additional FTP guidance](/previous-versions/orphan-topics/ws.10/cc756013(v=ws.10))
