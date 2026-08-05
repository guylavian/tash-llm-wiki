---
title: "ftp open"
type: reference
domain: windows-server
slug: administration-ftp-open-1
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ftp-open_1
family: administration
documentKind: "reference"
abstract: "Reference article for the ftp open command, which connects to the specified ftp server."
---

# ftp open

# ftp open



Connects to the specified ftp server.

## Syntax

```
open <computer> [<port>]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<computer>` | Specifies the remote computer to which you are trying to connect. You can use an IP address or computer name (in which case a DNS server or Hosts file must be available). |
| `[<port>]` | Specifies a TCP port number to use to connect to an ftp server. By default, TCP port 21 is used. |

### Examples

To connect to the ftp server at *ftp.microsoft.com*, type:

```
open ftp.microsoft.com
```

To connect to the ftp server at *ftp.microsoft.com* that is listening on TCP port *755*, type:

```
open ftp.microsoft.com 755
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [Additional FTP guidance](/previous-versions/orphan-topics/ws.10/cc756013(v=ws.10))
