---
title: "telnet open"
type: reference
domain: windows-server
slug: administration-telnet-open
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/telnet-open
family: administration
documentKind: "reference"
abstract: "Reference article for the telnet open command, which connects to a telnet server."
---

# telnet open

# telnet: open



Connects to a telnet server.

## Syntax

```
o[pen] <hostname> [<port>]
```

### Parameters

| Parameter | Description |
|--|--|
| `<hostname>` | Specifies the computer name or IP address. |
| `[<port>]` | Specifies the TCP port that the telnet server is listening on. The default is TCP port 23. |

## Examples

To connect to a telnet server at *telnet.microsoft.com*, type:

```
o telnet.microsoft.com
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
