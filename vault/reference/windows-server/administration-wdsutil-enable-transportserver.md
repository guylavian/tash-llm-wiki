---
title: "wdsutil enable-transportserver"
type: reference
domain: windows-server
slug: administration-wdsutil-enable-transportserver
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-enable-transportserver
family: administration
documentKind: "reference"
abstract: "Reference article for the wdsutil enable-transportserver command, which enables all services for the Transport Server."
---

# wdsutil enable-transportserver

# wdsutil enable-transportserver



Enables all services for the Transport Server.

## Syntax

```
wdsutil [options] /Enable-TransportServer [/Server:<Servername>]
```

### Parameters

| Parameter | Description |
|--|--|
| [/Server:`<Servername>`] | Specifies the name of the server. This can be the NetBIOS name or the fully qualified domain name (FQDN). If no server name is specified, the local server is used. |

## Examples

To enable the services on the server, type either:

```
wdsutil /Enable-TransportServer
```

```
wdsutil /verbose /Enable-TransportServer /Server:MyWDSServer
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [wdsutil disable-transportserver command](wdsutil-disable-transportserver.md)

- [wdsutil get-transportserver command](wdsutil-get-transportserver.md)

- [wdsutil set-transportserver command](wdsutil-set-transportserver.md)

- [wdsutil start-transportserver command](wdsutil-start-transportserver.md)

- [wdsutil stop-transportserver command](wdsutil-stop-transportserver.md)

- [Windows Deployment Services cmdlets](/powershell/module/wds)
