---
title: "simulate restore"
type: reference
domain: windows-server
slug: administration-simulate-restore
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/simulate-restore
family: administration
documentKind: "reference"
abstract: "Reference article for the simulate restore command, which tests whether writer involvement in restore sessions will be successful on the computer without issuing PreRestore or PostRestore events to writers."
---

# simulate restore

# Simulate restore

Tests whether writer involvement in restore sessions will be successful on the computer without issuing **PreRestore** or **PostRestore** events to writers.

> [!NOTE]
> A DiskShadow metadata file must be selected for the **simulate restore** command to succeed. Use the [load metadata command](load-metadata.md) to load the selected writers and components for the restore.

## Syntax

```
simulate restore
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [load metadata command](load-metadata.md)
