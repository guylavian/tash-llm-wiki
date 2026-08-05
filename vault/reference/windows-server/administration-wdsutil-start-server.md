---
title: "wdsutil start-server"
type: reference
domain: windows-server
slug: administration-wdsutil-start-server
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-start-server
family: administration
documentKind: "reference"
abstract: "Reference article for Subcommand start-Server, which starts all services for a Windows Deployment Services server."
---

# wdsutil start-server

# wdsutil start-server



Starts all services for a Windows Deployment Services server.

## Syntax
```
wdsutil [Options] /start-Server [/Server:<Server name>]
```
### Parameters

|Parameter|Description|
|-------|--------|
|[/Server:\<Server name\>]|Specifies the name of the server to be started. This can be either the NetBIOS name or the fully qualified domain name (FQDN). If no server name is specified, the local server will be used.|

## Examples
To start the server, type one of the following:
```
wdsutil /start-Server
wdsutil /verbose /start-Server /Server:MyWDSServer
```
## Related links
- [Command-Line Syntax Key](command-line-syntax-key.md)
- [wdsutil disable-server command](wdsutil-disable-server.md)
- [wdsutil enable-server command](wdsutil-enable-server.md)
- [wdsutil get-server command](wdsutil-get-server.md)
- [wdsutil initialize-server command](wdsutil-initialize-server.md)
- [wdsutil set-server command](wdsutil-set-server.md)
- [wdsutil stop-server command](wdsutil-stop-server.md)
- [wdsutil start-server command](wdsutil-start-server.md)
- [wdsutil uninitialize-server command](wdsutil-uninitialize-server.md)
