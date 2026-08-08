---
title: "Update-ServerFiles"
type: reference
domain: windows-server
slug: administration-wdsutil-update-serverfiles
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-update-serverfiles
family: administration
documentKind: "reference"
abstract: "Reference article for Update-ServerFiles, which updates files in the REMINST shared folder by using the latest files that are stored in the server's %Windir%\\System32\\RemInst folder."
---

# Update-ServerFiles

# Update-ServerFiles

Updates files in the REMINST shared folder by using the latest files that are stored in the server's %Windir%\System32\RemInst folder. To ensure the validity of your Windows Deployment Services installation, you should run this command once after each server upgrade, service pack installation, or update to Windows Deployment Services files.

## Syntax

```
wdsutil [Options] /Update-ServerFiles [/Server:<Server name>]
```

### Parameters

|Parameter|Description|
|---------|-----------|
|[/Server:\<Server name>]|Specifies the name of the server. This can be either the NetBIOS name or the fully qualified domain name (FQDN). If no server name is specified, the local server will be used.|

## Examples

To update the files, type one of the following:
```
wdsutil /Update-ServerFiles
wdsutil /Verbose /Progress /Update-ServerFiles /Server:MyWDSServer
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
