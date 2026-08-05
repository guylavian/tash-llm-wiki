---
title: "netsh exec"
type: reference
domain: windows-server
slug: administration-netsh-exec
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh-exec
family: administration
documentKind: "reference"
abstract: "Reference article for the netsh exec command that runs a script file containing a series of netsh commands to automate network configuration tasks."
---

# netsh exec

# netsh exec

The `netsh exec` command executes a script file. This script file contains a series of `netsh` commands that are run sequentially when the script is executed. It automates network configuration tasks by performing complex operations without you needing to manually enter the entries.

## Syntax

```
netsh exec <ScriptFile>
```

## Parameters

| Command | Description |
|--|--|
| exec `<ScriptFile>` | Loads and runs the target script file. |

## Example

To load and run your script from the location **C:\NetshScripts\network_script.txt**, run the following command:

```cmd
netsh exec "C:\NetshScripts\network_script.txt"
```
