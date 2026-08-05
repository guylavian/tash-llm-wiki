---
title: "wdsutil disable-transportserver"
type: reference
domain: windows-server
slug: administration-wdsutil-disable-transportserver
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-disable-transportserver
family: administration
documentKind: "reference"
abstract: "Reference article for the wdsutil disable-transportserver command, which disables all services for a Transport Server."
---

# wdsutil disable-transportserver

# wdsutil disable-transportserver



Disables all services for a Transport Server.

## Syntax

```
wdsutil [Options] /Disable-TransportServer [/Server:<Servername>]
```

### Parameters

|Parameter|Description|
|-------|--------|
|[/Server:`<Servername>`]|Specifies the name of the Transport Server to be disabled. This can be either the NetBIOS name or the fully qualified domain name (FQDN). If no Transport Server name is specified, the local server will be used.|

## Examples

To disable the server, type either:

```
wdsutil /Disable-TransportServer
```

```
wdsutil /verbose /Disable-TransportServer /Server:MyWDSServer
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [wdsutil enable-transportserver command](wdsutil-enable-transportserver.md)

- [wdsutil get-transportserver command](wdsutil-get-transportserver.md)

- [wdsutil set-transportserver command](wdsutil-set-transportserver.md)

- [wdsutil start-transportserver command](wdsutil-start-transportserver.md)

- [wdsutil stop-transportserver command](wdsutil-stop-transportserver.md)

- [Windows Deployment Services cmdlets](/powershell/module/wds)
