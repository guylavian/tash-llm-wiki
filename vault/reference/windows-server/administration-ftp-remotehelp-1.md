---
title: "ftp remotehelp"
type: reference
domain: windows-server
slug: administration-ftp-remotehelp-1
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ftp-remotehelp_1
family: administration
documentKind: "reference"
abstract: "Reference article for the ftp remotehelp command, which displays help for remote commands."
---

# ftp remotehelp

# ftp remotehelp



Displays help for remote commands.

## Syntax

```
remotehelp [<command>]
```

### Parameters

| Parameter | Description |
| ------- | -------- |
| `[<command>]` | Specifies the name of the command about which you want help. If `<command>` isn't specified, this command displays a list of all remote commands. You can also run remote commands using [ftp quote](ftp-quote.md) or [ftp literal](ftp-literal_1.md). |

### Examples

To display a list of remote commands, type:

```
remotehelp
```

To display the syntax for the *feat* remote command, type:

```
remotehelp feat
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [ftp quote](ftp-quote.md)

- [ftp literal](ftp-literal_1.md)

- [Additional FTP guidance](/previous-versions/orphan-topics/ws.10/cc756013(v=ws.10))
