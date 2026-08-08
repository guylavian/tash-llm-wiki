---
title: "wdsutil disable-server"
type: reference
domain: windows-server
slug: administration-wdsutil-disable-server
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-disable-server
family: administration
documentKind: "reference"
abstract: "Reference article for the wdsutil disable-server command, which disables all services for a Windows Deployment Services server."
---

# wdsutil disable-server

# wdsutil disable-server

Disables all services for a Windows Deployment Services server.

## Syntax

```
wdsutil [Options] /Disable-Server [/Server:<Server name>]
```

### Parameters

| Parameter | Description |
|--|--|
| [/Server:`<Servername>`] | Specifies the name of the server. This can be either the NetBIOS name or the fully qualified domain name (FQDN). If no server name is specified, the local server will be used. |

## Examples

To disable the server, type either:

```
wdsutil /Disable-Server
```

```
wdsutil /Verbose /Disable-Server /Server:MyWDSServer
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [Windows Deployment Services cmdlets](/powershell/module/wds)
