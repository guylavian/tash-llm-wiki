---
title: "wdsutil progress"
type: reference
domain: windows-server
slug: administration-wdsutil-progress
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-progress
family: administration
documentKind: "reference"
abstract: "Reference article for wdsutil progress, which displays progress while a command is running."
---

# wdsutil progress

# wdsutil /progress

Displays progress while a command is running. You can use **/progress** with any other wdsutil commands that you run. If you want to turn on verbose logging for this command, you must specify **/verbose** and **/progress** directly after **wdsutil**.

## Syntax

```
wdsutil /progress <commands>
```

## Examples

To initialize the server and display progress, type:

```
wdsutil /verbose /progress /Initialize-Server /Server:MyWDSServer /RemInst:C:\RemoteInstall
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
