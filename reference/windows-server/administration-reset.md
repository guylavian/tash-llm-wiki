---
title: "reset"
type: reference
domain: windows-server
slug: administration-reset
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reset
family: administration
documentKind: "reference"
abstract: "Reference article for the reset command, which resets DiskShadow.exe to the default state."
---

# reset

# reset

Resets DiskShadow.exe to the default state. This command is especially useful in separating compound DiskShadow operations, such as **create**, **import**, **backup**, or **restore**.

> [!IMPORTANT
> After you run this command, you will lose state information from commands, such as **add**, **set**, **load**, or **writer**. This command also releases IVssBackupComponent interfaces and loses non-persistent shadow copies.

## Syntax

```
reset
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [create command](create.md)

- [import command](import_1.md)

- [backup command](begin-backup.md)

- [restore command](begin-restore.md)

- [add command](add.md)

- [set command](./set.md)

- [load command](reg-load.md)

- [writer command](writer.md)
