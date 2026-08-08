---
title: "netsh delete"
type: reference
domain: windows-server
slug: administration-netsh-delete
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh-delete
family: administration
documentKind: "reference"
abstract: "Reference article for the netsh delete command that removes a helper dll."
---

# netsh delete

# netsh delete

The `netsh delete` command is used to remove helper Dynamic Link Libraries (DLL) allowing for more specialized network configurations.

## Syntax

```
netsh delete helper [file]
```

## Parameters

| Command | Description |
|--|--|
| helper | Calls the helper DLL file. |

## Example

To remove a helper DLL located at **C:\dlls\HelperDLL.dll**, run the following command:

```cmd
netsh delete helper C:\dlls\HelperDLL.dll
```
