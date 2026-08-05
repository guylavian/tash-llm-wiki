---
title: "Using the verbose command"
type: reference
domain: windows-server
slug: administration-wdsutil-verbose
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-verbose
family: administration
documentKind: "reference"
abstract: "Reference article for verbose, which displays verbose output for a specified command."
---

# Using the verbose command

# Using the verbose command

Displays verbose output for a specified command. You can use **/verbose** with any other wdsutil commands that you run. Note that you must specify **/verbose** and **/progress** directly after **wdsutil**.

## Syntax

```
wdsutil /verbose <commands>
```

## Examples

To delete approved computers from the Auto-Add database and show verbose output, type:

```
wdsutil /Verbose /progress /Delete-AutoAddDevices /Server:MyWDSServer /DeviceType:ApprovedDevices
```
