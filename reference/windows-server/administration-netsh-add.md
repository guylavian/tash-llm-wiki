---
title: "netsh add"
type: reference
domain: windows-server
slug: administration-netsh-add
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh-add
family: administration
documentKind: "reference"
abstract: "Reference article for the netsh add command that adds a helper dll."
---

# netsh add

# netsh add

The `netsh add` command is used to install helper Dynamic Link Libraries (DLL) allowing for more specialized network configurations.

## Syntax

```
netsh add helper [file]
```

## Parameters

| Command | Description |
|--|--|
| helper | Adds a helper DLL file. |

## Example

To add a helper DLL located at **C:\dlls\HelperDLL.dll**, run the following command:

```cmd
netsh add helper C:\dlls\HelperDLL.dll
```
