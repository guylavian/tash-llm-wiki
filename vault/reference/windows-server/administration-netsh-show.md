---
title: "netsh show"
type: reference
domain: windows-server
slug: administration-netsh-show
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh-show
family: administration
documentKind: "reference"
abstract: "The netsh show command displays the alias and DLL helper modules available within the netsh in Windows."
---

# netsh show

# netsh show

The `netsh show` command displays information about defined command aliases and available dynamic link library (DLL) modules.

## Syntax

```
netsh show <alias> <helper>
```

## Parameters

| Parameter | Description |
|--|--|
| `alias` | Lists all the defined aliases in the `netsh` context. Aliases are shortcuts that can be created for longer commands or sequences. |
| `helper` | Lists all the top-level DLL helpers available. |

## Examples

To see the aliases used within your environment, run the following command:

```cmd
netsh show alias
```

To see a list of the DLL helper files used within your environment, run the following command:

```cmd
netsh show helper
```

## See also

- [Command-Line Syntax Key](command-line-syntax-key.md)
