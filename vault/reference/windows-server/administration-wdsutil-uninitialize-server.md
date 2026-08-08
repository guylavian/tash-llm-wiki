---
title: "wdsutil uninitialize-server"
type: reference
domain: windows-server
slug: administration-wdsutil-uninitialize-server
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-uninitialize-server
family: administration
documentKind: "reference"
abstract: "Reference article for uninitialize-Server, which reverts changes made to the server during the initial server configuration."
---

# wdsutil uninitialize-server

# wdsutil uninitialize-server



Reverts changes made to the server during the initial server configuration. This includes changes made by either the **/initialize-server** option or the Windows Deployment Services mmc snap-in. Note that this command resets the server to an unconfigured state. This command does not modify the contents of the remoteInstall shared folder. Rather, it resets the server's state so that you can reinitialize the server.

## Syntax
```
wdsutil [Options] /Uninitialize-Server [/Server:<Server name>]
```
### Parameters

|Parameter|Description|
|-------|--------|
|[/Server:\<Server name\>]|Specifies the name of the server. This can be either the NetBIOS name or the fully qualified domain name (FQDN). If no server name is specified, the local server will be used.|

## Examples
To reinitialize the server, type one of the following:
```
wdsutil /Uninitialize-Server
wdsutil /verbose /Uninitialize-Server /Server:MyWDSServer
```
## Related links
- [Command-Line Syntax Key](command-line-syntax-key.md)
- [wdsutil disable-server command](wdsutil-disable-server.md)
- [wdsutil enable-server command](wdsutil-enable-server.md)
- [wdsutil get-server command](wdsutil-get-server.md)
- [wdsutil initialize-server command](wdsutil-initialize-server.md)
- [wdsutil set-server command](wdsutil-set-server.md)
- [wdsutil start-server command](wdsutil-start-server.md)
- [wdsutil stop-server command](wdsutil-stop-server.md)
