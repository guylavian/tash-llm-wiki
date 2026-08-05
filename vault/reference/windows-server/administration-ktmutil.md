---
title: "ktmutil"
type: reference
domain: windows-server
slug: administration-ktmutil
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ktmutil
family: administration
documentKind: "reference"
abstract: "Reference article for the ktmutil command, which starts the Kernel Transaction Manager utility."
---

# ktmutil

# ktmutil

Starts the Kernel Transaction Manager utility. If used without parameters, **ktmutil** displays available subcommands.

## Syntax

```
ktmutil list tms
ktmutil list transactions [{TmGUID}]
ktmutil resolve complete {TmGUID} {RmGUID} {EnGUID}
ktmutil resolve commit {TxGUID}
ktmutil resolve rollback {TxGUID}
ktmutil force commit {GUID}
ktmutil force rollback {GUID}
ktmutil forget
```

## Examples


To force an Indoubt transaction with GUID 311a9209-03f4-11dc-918f-00188b8f707b to commit, type:

```
ktmutil force commit {311a9209-03f4-11dc-918f-00188b8f707b}
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
